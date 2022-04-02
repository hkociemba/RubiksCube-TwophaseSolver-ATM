import solver as sv
import cubie as cb
import face as fa
import performance as pf

cc = cb.CubieCube()
cc.multiply(cb.moveCube[0])
cc.multiply(cb.moveCube[15])
fc = cc.to_facelet_cube()
#s = fc.to_string()
#a = sv.solve(s, 2, 2000)  # solve with a maximum of 20 moves and a timeout of 2 seconds for example
#print(a)

print(pf.test(100, 1))
