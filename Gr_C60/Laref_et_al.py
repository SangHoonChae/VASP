# scatter graph
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(143)

x = [2.82,3.10,3.32,3.15]
y = [0.91,0.84,0.83,0.90]

area = 20**2
colors = ('limegreen','violet','orange','green')

plt.scatter(x, y, s=area, c=colors)
plt.axis([2.78, 3.35, 0.82, 0.93])
# text
plt.text(x[0]-0.01, y[0]+0.007, 'ATP', fontdict={'size': 12})
plt.text(x[1]-0.01, y[1]+0.007, 'BRI', fontdict={'size': 12})
plt.text(x[2]-0.01, y[2]+0.007, 'RING', fontdict={'size': 12})
plt.text(x[3]-0.025, y[3]+0.007, 'RING2', fontdict={'size': 12})


plt.xlabel('SLG-C60 distance (Angstrom)')
plt.ylabel('Binding energy (eV)')
plt.grid(visible=True, linestyle='--')
plt.title('Laref et al. (2013, CPL)')
plt.show()
