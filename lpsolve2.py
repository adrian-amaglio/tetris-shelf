from lpsolve55 import *
unite=240

epaisseur = 18
#liste de la taille des planches
taille_planche=9*[2000]
##taille_planche=13*[unite]+14*[unite+epaisseur]+2*[2*unite]+10*[2*unite+2*epaisseur]+2*[3*unite+epaisseur]+1*[3*unite+2*epaisseur]+2*[4*unite+2*epaisseur]+[2000]

nb_planche=len(taille_planche)


largeur_unité=272

x=[largeur_unité-2*epaisseur, largeur_unité, largeur_unité+epaisseur, 2*largeur_unité-2*epaisseur, 2*largeur_unité, 3*largeur_unité-epaisseur, 3*largeur_unité, 4*largeur_unité]

nb_x = [13,10,4,2,10,2,1,2]
##min_x=0
##max_x=(sum(taille_planche_total)/(27+2*12+3*3+2*4)+3*epaisseur)
##While max_x-min_x!=1
##X=(max_x+min_x)//2

#création d'une liste de taille nb planche composé de liste d'entier
#ces entiers sont les découpage de planche espacés d'autant de 0 qu'il y a de planche (exmple [[x[1],0,x[2],0,x[3],0],[0,x[1],0,x[2],0,x[3]]])
planche=(nb_planche)*[[]]
for i in range (0,(nb_planche)) :
    planche[i]=(i)*[0]
    for j in range (0,(len(x)-1)):
        planche[i]+=[x[j]]+(nb_planche-1)*[0]
    planche[i]+=[x[j+1]]+(nb_planche-1-i)*[0]

#liste objectif : nb planche de taille x[1] dans la planche 1, nb planche de taille x[1] dans la planche 2(...) 
L=[]
for i in range (0,len(x)):
    L+=nb_planche*[x[i]]

lp = lpsolve('make_lp', 0, len(x)*nb_planche)
lpsolve('set_obj_fn', lp, L)

#la somme de toutes les planches de taille x[i] doit être égale aux nombres de planche x[i] voulu
for i in range(0, len(x)*nb_planche, nb_planche):
    lpsolve('add_constraint', lp, i*[0]+nb_planche*[1]+((len(x)*nb_planche)-nb_planche-i)*[0], EQ, nb_x[i//nb_planche])

#la somme des tailles des planches découpés dans la planche[i] ne doit pas dépasser la taille de la planche[i]
for i in range (0, nb_planche):
    lpsolve('add_constraint', lp, planche[i], LE, taille_planche[i])

#la varible d'indice i doit être un entier
for i in range(0, len(x)*nb_planche):
	lpsolve('set_int', lp, i, 1)

lpsolve('solve', lp)
print("blue")
t=lpsolve('get_variables', lp)

##if lpsolve('get_objective',lp) == insoluble:
##	max_x=X
##else :
##	min_x=X

print(X)
tab=[int(x)for x in t[0]]
tableau=[]
for i in range (0,len(x)):
	tableau+=[tab[i*nb_planche:i*nb_planche+nb_planche]]
	print(tableau[i])
