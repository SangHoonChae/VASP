C60 = float(-536.09823590)
G_9x9 = float(-1507.53175260)
tot = C60 + G_9x9
print('E_total = ',tot)

ATP       = [float(-2044.42189395), 2.90406]
BRI       = [float(-2044.39739236), 2.900775]
RING      = [float(-2044.40606180), 2.90155]
PTG       = [float(-2044.39914910), 2.900828]
PTG_RING  = [float(-2044.42659111), 2.900828]
RING2     = [float(-2044.45453298), 2.901395]
RING3     = [float(-2044.38533630), 2.90133]
TRP       = [float(-2044.39102027), 2.90090]

# binding energy (eV)
E_bind = []
E_bind.append(tot-ATP[0])
E_bind.append(tot-BRI[0])
E_bind.append(tot-RING[0])
E_bind.append(tot-PTG[0])
E_bind.append(tot-PTG_RING[0])
E_bind.append(tot-RING2[0])
E_bind.append(tot-RING3[0])
E_bind.append(tot-TRP[0])
print(E_bind)

# CONTCAR bonding length (Angstrom)
atp      = float(2.97269)
bri      = float(3.05734)
ring     = float(3.19243)
ptg      = float(3.108174667)
ptg_ring = float(3.155298)
ring2    = float(3.17495)
ring3    = float(3.197388333)
trp      = float(3.2199675)

dist = [atp,bri,ring,ptg,ptg_ring,ring2,ring3,trp]
print(dist)

# scatter graph
import matplotlib.pyplot as plt
import numpy as np

x = dist
y = E_bind

area = 20**2
colors = ('limegreen','violet','orange','dodgerblue','red','green','blue','brown')

plt.scatter(x, y, s=area, c=colors)
plt.axis([2.7, 3.7, 0.7, 0.9])
# text
plt.text(x[0]-0.01, y[0]+0.007, 'ATP', fontdict={'size': 12})
plt.text(x[1]-0.01, y[1]+0.007, 'BRI', fontdict={'size': 12})
plt.text(x[2]-0.01, y[2]+0.007, 'RING', fontdict={'size': 12})
plt.text(x[3]-0.01, y[3]+0.007, 'PTG', fontdict={'size': 12})
plt.text(x[4]-0.025, y[4]+0.007, 'PTG_RING', fontdict={'size': 12})
plt.text(x[5]-0.015, y[5]+0.007, 'RING2', fontdict={'size': 12})
plt.text(x[6]-0.02, y[6]+0.007, 'RING3', fontdict={'size': 12})
plt.text(x[7]-0.00, y[7]+0.006, 'TRP', fontdict={'size': 12})


plt.xlabel('SLG-C60 distance (Angstrom)')
plt.ylabel('Binding energy (eV)')
plt.grid(visible=True, linestyle='--')
plt.title('PBE-D3 model')
plt.show()

