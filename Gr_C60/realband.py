
a = open('/home/csh/Downloads/forscp/EIGENVAL_2')
b = a.readlines()

band = []
for i in range(7, len(b)):
    temp = b[i].split()
    if len(temp) == 3:
        tempL.append(float(temp[1]))
    elif len(temp) == 4:
        tempL = []
        #print(temp)
    elif len(temp) == 0:
        band.append(tempL)
band.append(tempL)

##################################################################
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
##################################################################

band = np.asarray(band)
band = np.matrix.transpose(band)
###################################################################

disp = 10
x  = list(np.arange(0, 3*disp))
#x += list(np.arange(disp-1,2*disp-1))
#x += list(np.arange(2*disp-2,3*disp-2))
#x += list(np.arange(3*disp-3,4*disp-3))
#x += list(np.arange(4*disp-4,5*disp-4))
#x += list(np.arange(5*disp-5,6*disp-5))
#x += list(np.arange(6*disp-6,6*disp-6))
#x += list(np.arange(7*disp-7,6*disp-7))
#x += list(np.arange(8*disp-8,6*disp-8))
#x += list(np.arange(9*disp-9,6*disp-9))

print(x)

print('Number of k-points: ' + str(len(x)))

####################################################################
fig = plt.figure()
ax = plt.subplot()

VBM = -2.7516
for i in range(len(band)):
    ax.plot(x,band[i]-VBM,'-',color='b',lw=1) # plotting x-axis & y-axis

plt.xlabel('k-point',size=18)
plt.ylabel('Energy (eV)',size=18)

plt.ylim(-23,5)
plt.xlim(min(x),max(x))

plt.axvline(x[disp], color='k', lw=1, ls='-')
plt.axvline(x[2*disp], color='k', lw=1, ls='-')
plt.axvline(x[3*disp-1], color='k', lw=1, ls='-')
#plt.axvline(x[4*disp], color='k', lw=1, ls='-')
#plt.axvline(x[5*disp], color='k', lw=1, ls='-')
#plt.axvline(x[6*disp], color='k', lw=1, ls='-')
#plt.axvline(x[7*disp], color='k', lw=1, ls='-')
#plt.axvline(x[8*disp], color='k', lw=1, ls='-')
#plt.axvline(x[9*disp], color='k', lw=1, ls='-')

ax.set_xticks([0,x[disp],x[2*disp],x[3*disp-1]])
#ax.set_xticklabels([r'$\Gamma$','x','U/K',r'$\Gamma$','L','W','X'])
#ax.set_xticklabels(['L',r'$\Gamma$','x','U/K',r'$\Gamma$'])
ax.set_xticklabels([r'$\Gamma$', 'X/$\Gamma$', 'Y/$\Gamma$', r'Z'])

ytick =  np.arange(-20,6)
yticklabels = list(np.arange(-20,6))
ax.set_yticks(ytick)
for i in range(len(yticklabels)):
    if(int(yticklabels[i]) % 2) == 0:
        pass
    else:
        yticklabels[i] = ''


ax.set_yticklabels(yticklabels)


for label in ax.get_yticklabels() + ax.get_xticklabels():
    label.set_fontsize(18)

fig.subplots_adjust(bottom=0.15,top=0.95,hspace=0.3,left=0.15)
plt.grid()
plt.show()
fig.savefig("test.png", dpi=300)
