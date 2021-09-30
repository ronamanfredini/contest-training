A = 1
B = 3
C = 5
D = 10
E = 25
F = 50
G = 100
entrada = int(input())

if (entrada <= A):
    print("Top", A)

if (entrada > A and entrada <= B):
    print("Top", B)

if (entrada > B and entrada <= C):
    print("Top", C)

if (entrada > C and entrada <= D):
    print("Top", D)

if (entrada > D and entrada <= E):
    print("Top", E)

if (entrada > E and entrada <= F):
    print("Top", F)

if (entrada > F and entrada <= G):
    print("Top", G)
