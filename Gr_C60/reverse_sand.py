
# each C60, Graphene
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
#print(dist)

# reverse sandwich E-bind
R2_ATP = float(-2581.26670886)
rev_RING2_ATP = float(2*C60 + G_9x9 - R2_ATP)
print('R2 ATP each sum = ',E_bind[0] + E_bind[5])
print('r_sand binding energy is ',rev_RING2_ATP)

R3_R3 = float(-.25812071E+04)
rev_R3_R3 = float(2*C60 + G_9x9 - R3_R3)
print('R3 R3 each sum = ',E_bind[6] + E_bind[6])
print('r_sand binding energy is ',rev_R3_R3)