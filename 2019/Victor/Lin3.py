import math

inp = open('input.txt', 'r')
A = list(map(float, inp.readline().strip().split()))

B = list(map(float, inp.readline().strip().split()))

C = list(map(float, inp.readline().strip().split()))

D = list(map(float, inp.readline().strip().split()))
faces

rayDirection = list(map(float, inp.readline().strip().split()))

rayPoint = list(map(float, inp.readline().strip().split()))

energy = int(inp.readline().strip())
numOfMirrors = int(inp.readline().strip())
mirrors = []
for k in range(numOfMirrors):
    p = list(map(float, inp.readline().strip().split()))
    q = list(map(float, inp.readline().strip().split()))
    r = list(map(float, inp.readline().strip().split()))
    n = [0, 0, 0]
    mirrors.append({'p':p, 'q':q, 'r':r, 'n':n})
    mirrors[k]['n'][0] = mirrors[k]['p'][1]*mirrors[k]['q'][2] - mirrors[k]['p'][2]*mirrors[k]['q'][1]
    mirrors[k]['n'][1] = mirrors[k]['p'][0] * mirrors[k]['q'][2] - mirrors[k]['p'][2] * mirrors[k]['q'][0]
    mirrors[k]['n'][2] = mirrors[k]['p'][0] * mirrors[k]['q'][1] - mirrors[k]['p'][1] * mirrors[k]['q'][0]
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