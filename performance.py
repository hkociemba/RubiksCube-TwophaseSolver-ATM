import solver as sv
import cubie


def test(n, t):
    """
    :param n: The number of generated random cubes
    :param t: The time in seconds to spend on each cube
    :return: A dictioneary with the solving statistics
    """
    cc = cubie.CubieCube()
    cnt = [0] * 31
    for i in range(n):
        cc.randomize()
        fc = cc.to_facelet_cube()
        s = fc.to_string()
        print(s)
        s = sv.solve(s, 0, t)
        print(s)
        print()
        cnt[int(s.split('(')[1].split('a')[0])] += 1
    avr = 0
    for i in range(31):
        avr += i*cnt[i]
    avr /= n
    return 'average ' + '%.2f' % avr + ' moves', dict(zip(range(22), cnt))
