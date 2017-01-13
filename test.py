import sys

def printf(x):
    sys.stdout.write(x)

nb=['_zero','_un','_deux','_trois','_quatre','_cinq','_six','_sept','_huit','_neuf']
    
nb_planche=9    
L=[chr(x) for x in range(97, 97+7)]

printf("/* Objective function */\nmax: ")
for i in range (1, nb_planche+1):
    printf("planche"+nb[i]+" + ")
printf("X;\n")
printf("\n/* Variable bounds */\nepaisseur = 18;\ntaille_planche = 2000;\nx_un = X-2*epaisseur;\nx_deux = X-epaisseur;\nx_trois = 2X-2*epaisseur;\nx_quatre = 2X;\nx_cinq = 3X-epaisseur;\nx_six = 3X;\nx_sept = 4X;\n\na = 13;\nb = 14;\nc = 2;\nd = 10;\ne = 2;\nf = 1;\ng = 2;\n\n")

for y in L:
    printf(y+" = ")
    for x in range (1,nb_planche):
        printf(y+nb[x]+" +")
    printf(y+nb[x+1]+";\n")

printf('\n')
for a in range (1,nb_planche+1):
    x=nb[a]
    printf("planche"+x+" = ")
    for z in range (1,7):
        y=L[z-1]
        printf(y+x+" x"+nb[z]+" +")
    y=L[z]
    printf(y+x+" x"+nb[z+1]+";\n")

printf('\n')
for x in range (1,nb_planche+1):
    print("planche"+nb[x]+" <= taille_planche;")

printf("\n/*Integer definitions*/\nint ")
for y in L:
    printf(y+", ")
    for i in range (1, nb_planche+1):
        printf(y+nb[i]+", ")
for i in range (1,8):
      printf("x"+nb[i]+", ")
for i in range (1,nb_planche+1):
      printf("planche"+nb[i]+", ")
printf("epaisseur, taille_planche, X;")

##for y in L:
##    print(y+" >= 0;")
##    for i in range (1, nb_planche+1):
##        print(y+str(i)+" >= 0;")
##for i in range (1,8):
##      print("x"+str(i)+" >= 0;")
##for i in range (1,nb_planche+1):
##      print("planche"+str(i)+" >= 0;")
##printf("epaisseur >= 0;\ntaille_planche >= 0;\nX >= 0;")
#taille_planche >= z1;
#z1 : a1*x1 + b1*x2 + c1*x3 +d1*x4 + e1*x5 + f1*x6 + g1*x7;
