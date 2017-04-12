from lpsolve55 import *

X=272
epaisseur = 18
taille_planche=2000
nb_planche=9

x=[X-2*epaisseur, X, X+epaisseur, 2*X-2*epaisseur, 2*X, 3*X-epaisseur, 3*X, 4*X]

nb_x = [13,10,4,2,10,2,1,2]


planche=(nb_planche)*[[]]
for i in range (0,(nb_planche)) :
    planche[i]=(i)*[0]
    for j in range (0,(len(x)-1)):
        planche[i]+=[x[j]]+(nb_planche-1)*[0]
    planche[i]+=[x[j+1]]+(nb_planche-1-i)*[0]

L=[]
for i in range (0,len(x)):
    L+=nb_planche*[x[i]]

lp = lpsolve('make_lp', 0, len(x)*nb_planche)
lpsolve('set_obj_fn', lp, L)

for i in range(0, len(x)*nb_planche, nb_planche):
    lpsolve('add_constraint', lp, i*[0]+nb_planche*[1]+((len(x)*nb_planche)-nb_planche-i)*[0], EQ, nb_x[i//nb_planche])

for i in range (0, nb_planche):
    lpsolve('add_constraint', lp, planche[i], LE, taille_planche)

for i in range(1, len(x)*nb_planche):
	lpsolve('set_int', lp, i, 1)

lpsolve('solve', lp)
print(lpsolve('get_variables', lp))

