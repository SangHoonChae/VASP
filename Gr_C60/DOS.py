import matplotlib.pyplot as plt

xx = []
yy = []

with open('/home/csh/Desktop/VESTA/reverse_sandwich/ring_ring/DOSCAR', 'r') as DOSCAR:
    lines = DOSCAR.readlines()

header = lines[5].split()
print(header)
E_fermi = float(header[3])
NEDOS = int(header[2])
print (E_fermi, NEDOS)

for i in range(6, 6+NEDOS):
    m = lines[i].split()
    energy = float(m[0])
    DOS = float(m[1])
    DOS_integrated = float(m[2])
    xx.append(energy - E_fermi)
    yy.append(DOS)

plt.figure(figsize=(6,4))
plt.plot(xx, yy)
plt.xlabel("Energy(eV)")
plt.ylabel("DOS(1/eV)")
plt.axvline(0, color="grey", linestyle="--", label="E_Fermi")
plt.axis([-2.0,2.0,-2.0,80.0])
plt.title("RING-Graphene-RING DOS")
plt.legend()
plt.grid()
plt.show()
