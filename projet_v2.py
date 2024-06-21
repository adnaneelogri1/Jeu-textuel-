import os, random

run = True
menu = True #Menu page
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

HP = 50
HPMAX = 50
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

        #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
map = [["plaines",   "plaines",   "plaines",   "plaines",   "foret", "montagne",   "Grotte"],    # y = 0
       ["foret",   "foret",   "foret",   "foret",   "foret",    "hills",   "montagne"],    # y = 1
       ["foret",   "des champs",   "pont",   "plaines",    "collines",   "foret", "collines"],    # y = 2
       ["plaines",     "boutique",  "ville",    "maire",   "plaines",    "collines",  "mountagne"],    # y = 3
       ["plaines",   "des champs",   "des champs",   "plaines", "collines", "montagne", "montagne"]]    # y = 4

y_len = len(map)-1
x_len = len(map[0])-1

biom = {
    "plains": {
        "t": "plaines",
        "e": True},
    "forest": {
        "t": "les bois",
        "e": True},
    "fields": {
        "t": "DES CHAMPS",
        "e": False},
    "bridge": {
        "t": "DES SOUCIS",
        "e": True},
    "town": {
        "t": "Centre Ville",
        "e": False},
    "shop": {
        "t": "Boutique",
        "e": False},
    "mayor": {
        "t": "Maire",
        "e": False},
    "cave": {
        "t": "Grotte",
        "e": False},
    "mountain": {
        "t": "MONTAGNE",
        "e": True},
    "hills": {
        "t": "Collines",
        "e": True,
    }
}

e_list = ["Goblin", "Orque", "Vase"]

mobs = {
    "Goblin": {
        "hp": 15,
        "at": 3,
        "go": 8
    },
    "Orque": {
        "hp": 35,
        "at": 5,
        "go": 18
    },
    "Vase": {
        "hp": 30,
        "at": 2,
        "go": 12
    },
    "Dragon": {
        "hp": 100,
        "at": 8,
        "go": 100
    }
}


def clear():
    os.system("cls")


def draw():
    print("xX--------------------xX")


def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()


def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(name + " Votre santé est : " + str(HP) + "!")


def battle():
    global fight, play, run, HP, pot, elix, gold, boss
    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]
    while fight:
        clear()
        draw()
        print("Vous avez gagner contre " + enemy + "!")
        draw()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(name + "'s HP: " + str(HP) + "/" + str(HPMAX))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - utilisation de potion (30HP)")
        if elix > 0:
            print("3 - utilisation de elexir (50HP)")
        draw()
        choice = input("# ")

        if choice == "1":
            hp -= ATK
            print(name + " distribué " + str(ATK) + " degat à " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " distribué " + str(atk) + " Degat à " + name + ".")
            input("> ")
        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " distribué " + str(atk) + " degat à " + name + ".")
            else:
                print("Pas de potion!")
            input("> ")
        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " distribué " + str(atk) + " degat à " + name + ".")
            else:
                print("pas d'elexir!")
            input("> ")

        if HP <= 0:
            print(enemy + " Vaincue " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print("Vous avez perdu la game")
            input("> ")

        if hp <= 0:
            print(name + " Vaincue  " + enemy + "!")
            draw()
            fight = False
            gold += g
            print("Vous avez trouver " + str(g) + " gold!")
            if random.randint(0, 100) < 30:
                pot += 1
                print("Vous avez trouver une potion!")
            if enemy == "Dragon":
                draw()
                print("Félicitation, vous avez terminer la game")
                boss = False
                play = False
                run = False
            input("> ")
            clear()
def shop():
    global buy, gold, pot, elix, ATK

    while buy:
        clear()
        draw()
        print("Bienvenue a la boutique")
        draw()
        print("GOLD: " + str(gold))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        print("ATK: " + str(ATK))
        draw()
        print("1 - Acheter une potion (30HP) - 5 GOLD")
        print("2 - Acheter une elexir (MAXHP) - 8 GOLD")
        print("3 - améliorer une arme (+2ATK) - 10 GOLD")
        print("4 - sortir")
        draw()
        choice = input("# ")
        if choice == "1":
            if gold >= 5:
                pot += 1
                gold -= 5
                print("Vous avez acheter une potion potion!")
            else:
                print("pas de gold!")
            input("> ")
        elif choice == "2":
            if gold >= 8:
                elix += 1
                gold -= 8
                print("vous avez acheter une elixir!")
            else:
                print("pas de gold!")
            input("> ")
        elif choice == "3":
            if gold >= 10:
                ATK += 2
                gold -= 10
                print("Vous avez ameliorer votre arme!")
            else:
                print("pas de gold!")
            input("> ")
        elif choice == "4":
            buy = False


def mayor():
    global speak, key
    while speak:
        clear()
        draw()
        print("Bonjour, " + name + "!")
        if ATK < 10:
            print("Tu n'es pas encore assez fort pour affronter le dragon ! Continuez à pratiquer et revenez plus tard!")
            key = False
        else:
            print("Vous voudrez peut-être affronter le dragon maintenant ! Prenez cette clé mais attention à la bête !")
            key = True
        draw()
        print("1 - sortir")
        draw()
        choice = input("# ")
        if choice == "1":
            speak = False


def cave():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("Ici se trouve la grotte du dragon. Que vas-tu faire?")
        draw()
        if key:
            print("1 - UTILISER LA CLÉ")
        print("2 - FAIRE DEMI-TOUR")
        draw()

        choice = input("# ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False



while run:
    while menu:
        print("1, Commencer une nouvelle partie")
        print("2, Sauvegarde")
        print("3, Les regles du jeux")
        print("4, Sortir du jeux")

        if rules:
            print("Je suis le créateur de ce jeu et voici les règles.")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("# Comment t'appelles-tu, héros ? ")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    print("Welcome back, " + name + "!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file!")
                    input("> ")
            except OSError:
                print("No loadable save file!")
                input("> ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()  # autosave
        clear()

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) < 30:
                    fight = True
                    battle()

        if play:
            draw()
            print("LOCATION: " + biom[map[y][x]]["t"])
            draw()
            print("NAME: " + name)
            print("HP: " + str(HP) + "/" + str(HPMAX))
            print("ATK: " + str(ATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("GOLD: " + str(gold))
            print("COORD:", x, y)
            draw()
            print("0 - SAVE AND QUIT")
            if y > 0:
                print("1 - Le Nord")
            if x < x_len:
                print("2 - EST")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - SUD")
            if pot > 0:
                print("5 - Utiliser POTION (30HP)")
            if elix > 0:
                print("6 - Utiliser ELIXIR (50HP)")
            if map[y][x] == "Boutique" or map[y][x] == "Maire" or map[y][x] == "Grotte":
                print("7 - ENTER")
            draw()

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                if pot > 0:
                    pot -= 1
                    heal(30)
                else:
                    print("Manque de potions!")
                input("> ")
                standing = True
            elif dest == "6":
                if elix > 0:
                    elix -= 1
                    heal(50)
                else:
                    print("manque de elixirs!")
                input("> ")
                standing = True
            elif dest == "7":
                if map[y][x] == "Boutique":
                    buy = True
                    shop()
                if map[y][x] == "Maire":
                    speak = True
                    mayor()
                if map[y][x] == "Grotte":
                    boss = True
                    cave()
            else:
                standing = True
