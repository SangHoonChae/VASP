import matplotlib.pyplot as plt
X = [2.6, 2.7, 2.8, 2.9, 3.0, 3.1]
Y = [-.20441847E+04,-.20442558E+04,-.20442877E+04,-.20442952E+04, -.20442846E+04, -.20442584E+04]

plt.figure(figsize=(6,4))
plt.title('fullerene on graphene. C-ATP')
plt.plot(X,Y, 'bo--')
plt.xlabel('Gr - C60 distance (angstrom)')
plt.ylabel('energy without entropy')
plt.show()