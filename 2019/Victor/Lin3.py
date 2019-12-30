import math
import operator

inp = open('input.txt', 'r')
A = list(map(float, inp.readline().strip().split()))

B = list(map(float, inp.readline().strip().split()))

C = list(map(float, inp.readline().strip().split()))

D = list(map(float, inp.readline().strip().split()))
faces = [];
pq = list(map(operator.sub, A, B))
pr = list(map(operator.sub, C, B))
n = [pq[1]*pr[2] - pq[2]*pr[1], pq[0]*pr[2] - pq[2]*pr[0], pq[0]*pr[1] - pq[1]*pr[0]]
faces.append({'p':B, 'pq':pq, 'pr':pr, 'n':n})

print(faces)
rayDirection = list(map(float, inp.readline().strip().split()))

rayPoint = list(map(float, inp.readline().strip().split()))

energy = int(inp.readline().strip())
numOfMirrors = int(inp.readline().strip())
mirrors = []
for k in range(numOfMirrors):
    p = list(map(float, inp.readline().strip().split()))
    q = list(map(float, inp.readline().strip().split()))
    r = list(map(float, inp.readline().strip().split()))
    pq = list(map(operator.sub, q, p))
    pr = list(map(operator.sub, r, p))
    n = [0, 0, 0]
    mirrors.append({'p':p, 'pq':pq, 'pr':pr, 'n':n})
    mirrors[k]['n'][0] = mirrors[k]['pq'][1]*mirrors[k]['pr'][2] - mirrors[k]['pq'][2]*mirrors[k]['pr'][1]
    mirrors[k]['n'][1] = mirrors[k]['pq'][0] * mirrors[k]['pr'][2] - mirrors[k]['pq'][2] * mirrors[k]['pr'][0]
    mirrors[k]['n'][2] = mirrors[k]['pq'][0] * mirrors[k]['pr'][1] - mirrors[k]['pq'][1] * mirrors[k]['pr'][0]
inp.close()
print(mirrors)






# out = open('output.txt', 'w')
# if energy <= 0:
#     out.write(str(0) + "\n")
#     out.write(str(outpoint_x) + str(outpoint_y) + str(outpoint_z) + "\n")
# else:
#     out.write(str(1) + "\n")
#     out.write(str(energy) + "\n")
#     out.write(str(outpoint_x) + str(outpoint_y) + str(outpoint_z) + "\n")
#     out.write(str(outvector_x) + str(outvector_y) + str(outvector_z) + "\n")
# out.close()