import random
clef=0
i=0
players=[0,0,0]
def fouras():
    global clef
    x="Le Carré"
    print("Il peut être fait de soie,")
    print("Ou encore de chocolat.")
    print("Ce parfait quadrilatère,")
    print("Et une belle main au poker.")
    reponse=input("Qui est-il ? ")
    if reponse==x:
        print("Bravo, c'était bien Le Carré! Voici une clef en récompense.")
        clef+=1
    else:
        print("Mauvaise réponse, il fallait dire Le Carré.")


def Nim():
    global clef
    y = 21
    z=None
    print("il y a 21 barres,choisissez si vous en retirez 1,2,ou 3 de la pile. Vous affronterez un des grands maitres de la tour, bonne chance!")
    while y > 1:
        joueur=int(input("choisissez combien de barres vous retirez: "))
        y-=joueur
        print("il reste ", y, " barres")
        if y==1:
            print("c'est gagné, bravo!! Voici une clef en récompense.")
            clef+=1
        elif joueur==1:
            z=3
        elif joueur==3:
            z=1
        else:
            z=2
        g=random.randint(1,10)
        if g==7:
            z=random.randint(1,3)
        y-=z
        print("Le maitre retire ",z," barres, il en reste ",y,)
        if y==1:
            print("C'est perdu, dommage. Vous aurez plus de chance la prochaine fois.")


def pileface():
    global clef
    chance = input("pile ou face? ")
    bob = random.choices(['pile', "face"])
    chance = [chance]
    if bob == chance:
        print("c'est gagné, bravo!! Voici une clef en récompense.")
        clef+=1
    else:
        print("Perdu, la réponse était ", bob)
        print("A LA FOSSE AU LIONS")


def HUIT():
    global clef
    print("calculez le résultat:")
    print("8+8*8*8*8*8*8*8*8*8*8*8*8*8*0*8*8*8*8*8*8*8*8*8*8*8*8*8*8*8*8*8*8*8")
    z=int(input())
    if z==8:
        print("c'est gagné, bravo!! Voici une clef en récompense.")
        clef += 1
    else:
        print("C'est perdu, dommage. Vous aurez plus de chance la prochaine fois.")


def Coffre():
    global clef
    recomp=0
    bim=["rien","mim","cl"]
    print("Vous avez 3 coffres devant vous, un est vide, une possède un morceau de clef et un vous fais perdre l'épreuve, bonne chance!")
    while recomp!=3:
        random.shuffle(bim)
        z=int(input("Coffre 1,2 ou 3? "))
        if bim[z-1]=="mim":
            print("C'est perdu, dommage. Vous aurez plus de chance la prochaine fois.")
            return
        elif bim[z-1]=="cl":
            recomp+=1
            print("Bravo, vous avez trouvé un morceau de clef, plus que ",3-recomp,"!")
        else:
            print("il n'y avait rien, on rééssaie!")
    if recomp==3:
        print("c'est gagné, bravo!! Voici une clef en récompense.")
        clef+=1


def Diable():
    global clef
    print("Timothé veut acheter des Schoko-bons a 3,90. Il lui manque 3 Euros pour pouvoir les acheter, il décide donc de vendre son âme au diable")
    print("il décide donc de vendre son âme au diable pour obtenir la somme manquante.")
    print("Le diable refuse de dépenser plus d'1,20 euro pour son âme. Quel est le taux de réduction de l'âme de Timothé proposé par le Diable? ")
    z=int(input("écrivez votre réponse sous la forme numérique:14%=14,27%=27, etc"))
    if z==40:
        print("c'est gagné, bravo!! Voici une clef en récompense.")
        clef+=1
    else:
        print("C'est perdu, dommage. Vous aurez plus de chance la prochaine fois.")


def Deux():
    x=random.randint(1,17)
    print("Quelle est la ",x,"ieme puissance de 2?")
    g=int(input())
    if g==2**x:
        print("c'est gagné, bravo!! Voici une clef en récompense.")
    else:
        print("C'est perdu, dommage. Vous aurez plus de chance la prochaine fois.")



while i<=2:
    players[i] = input("quel est le nom du joueur ?")
    i+=1
print(players)
if clef == 3:
    print("félicitation, c'est gagné")
else:
    print("C'est au tour de", players[random.randint(0,2)]," de jouer!")
    HUIT()
    print("vous avez ",clef,"clef, plus que ",3-clef," avant la fin")
if clef==3:
    print("félicitation, c'est gagné")
else:
    print("C'est au tour de", players[random.randint(0, 2)], " de jouer!")
    Coffre()
    print("vous avez ", clef, "clef, plus que ", 3 - clef, " avant la fin")
if clef==3:
    print("félicitation, c'est gagné")
else:
    print("C'est au tour de", players[random.randint(0, 2)], " de jouer!")
    fouras()
if clef==3:
    print("félicitation, c'est gagné")
else:
    print("vous avez ", clef, "clef, plus que ", 3 - clef, " avant la fin")
    print("C'est au tour de", players[random.randint(0, 2)], " de jouer!")
    Diable()
if clef==3:
    print("félicitation, c'est gagné")
else:
    print("vous avez ", clef, "clef, plus que ", 3 - clef, " avant la fin")
    print("C'est au tour de", players[random.randint(0, 2)], " de jouer!")
    Nim()
if clef==3:
    print("félicitation, c'est gagné")
else:
    print("vous avez ", clef, "clef, plus que ", 3 - clef, " avant la fin")
    print("C'est au tour de", players[random.randint(0, 2)], " de jouer!")
    Deux()
if clef==3:
    print("félicitation, c'est gagné")
else:
    print("vous avez ", clef, "clef, plus que ", 3 - clef, " avant la fin")
    print("C'est au tour de", players[random.randint(0, 2)], " de jouer!")
    pileface()
if clef==3:
    print("félicitation, c'est gagné")
else:
    print("vous avez ", clef, "clef, plus que ", 3 - clef, " avant la fin")
    print("C'était la derniere épreuve, dommage!")