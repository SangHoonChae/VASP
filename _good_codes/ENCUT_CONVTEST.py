import matplotlib.pyplot as plt
xx = []
yy = []

with open('/home/csh/VASP_tutorials/bulk-part1/bulk/e02_fcc-Si-DOS/energy_conv_test.dat', 'r') as convtest:
    lines = convtest.readlines()

'''
for i in range(100, 601, 10):
    xx.append(i)
print(xx)
print(len(xx))
'''

for i in range(0, 51):
    
    parts = lines[i].split()
    print(parts)
    cutoff_en = float(parts[0])
    E0 = float(parts[5])
    xx.append(cutoff_en)
    yy.append(E0)

plt.plot(xx, yy)
plt.xlabel("ENCUT")
plt.ylabel("'E0=' (OSZICAR)")
plt.show()        




