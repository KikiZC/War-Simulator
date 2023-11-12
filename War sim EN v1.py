import random 

# tabulky se statama
stats_table = {
    "vojak":        {"hp": 100, "attack": 10, "attack speed": 3, "armour": 50, "armour toughness": 4},
    "lukostřelec":  {"hp": 80, "attack": 15, "attack speed": 2, "armour": 20, "armour toughness": 2},
    "jezdec":       {"hp": 50, "attack": 16, "attack speed": 4, "armour": 10, "armour toughness": 6},
    "kavalerie":    {"hp": 70, "attack": 25, "attack speed": 5, "armour": 30, "armour toughness": 10},
}

place_table = {
    "vojak":        {"plain": 10, "mountains": -2, "river": 0, "forest": 5},
    "lukostřelec":  {"plain": 15, "mountains": 10, "river": 10, "forest": -10},
    "jezdec":       {"plain": 17, "mountains": 0, "river": -2, "forest": -20},
    "kavalerie":    {"plain": 25, "mountains": 0, "river": -5, "forest": -20},
}

Weather_table = {
    "vojak":        {"nothinge": 0, "rain": -5, "snow": -15, "fog": -15, "thunder": -25, "heat": -20, "cold": -30},
    "lukostřelec":  {"nothinge": 0, "rain": -25, "snow": -20, "fog": -15, "thunder": -40, "heat": -10, "cold": -10},
    "jezdec":       {"nothinge": 0, "rain": -5, "snow": -10, "fog": -10, "thunder": -25, "heat": -10, "cold": -30},
    "kavalerie":    {"nothinge": 0, "rain": -10, "snow": -10, "fog": -20, "thunder": -30, "heat": -15, "cold": -40},
}

event_table = {
    "vojak":        {"sunstroke": -30, "freezing": -25, "lightning strike": -50, "slip": -60, "fitting in": -40, "drowned": -100, "crushed by a tree": -100},
    "lukostřelec":  {"sunstroke": -40, "freezing": -30, "lightning strike": -20, "slip": -30, "fitting in": -60, "drowned": -100, "crushed by a tree": -100},
    "jezdec":       {"sunstroke": -100, "freezing": -70, "lightning strike": -90, "slip": -95, "fitting in": -100, "drowned": -100, "crushed by a tree": -100},
    "kavalerie":    {"sunstroke": -10, "freezing": -5, "lightning strike": -30, "slip": -50, "fitting in": -60, "drowned": -100, "crushed by a tree": -100},
}

place_weather_table = {
    "plain": {"nothinge": 42, "rain": 20, "snow": 1, "fog": 6, "thunder": 6, "heat": 20, "cold": 5},
    "forest":     {"nothinge": 31, "rain": 15, "snow": 1, "fog": 30, "thunder": 20, "heat": 1, "cold": 2},
    "mountains":    {"nothinge": 15, "rain": 10, "snow": 20, "fog": 20, "thunder": 10, "heat": 5, "cold": 20},
    "river":    {"nothinge": 15, "rain": 10, "snow": 5, "fog": 35, "thunder": 5, "heat": 1, "cold": 29},
}

random_misto_vec = {
    "plain":  {"sunstroke": 5, "freezing": 2, "lightning strike": 2, "slip": 3, "fitting in": 3, "drowned": 0, "crushed by a tree": 1, "nothing":84},
    "forest":      {"sunstroke": 0, "freezing": 3, "lightning strike": 1, "slip": 1, "fitting in": 3, "drowned": 2, "crushed by a tree": 5, "nothing":85},
    "mountains":     {"sunstroke": 2, "freezing": 5, "lightning strike": 3, "slip": 4, "fitting in": 3, "drowned": 1, "crushed by a tree": 1, "nothing":81},
    "river":     {"sunstroke": 2, "freezing": 1, "lightning strike": 1, "slip": 5, "fitting in": 2, "drowned": 6, "crushed by a tree": 3, "nothing":80},
}

random_Weather_vec = {
    "nothinge":    {"sunstroke": 5, "freezing": 0, "lightning strike": 0, "slip": 2, "fitting in": 3, "drowned": 3, "crushed by a tree": 3, "nothing":84},
    "rain":    {"sunstroke": 0, "freezing": 1, "lightning strike": 2, "slip": 4, "fitting in": 2, "drowned": 1, "crushed by a tree": 3, "nothing":87},
    "snow":     {"sunstroke": 0, "freezing": 5, "lightning strike": 0, "slip": 3, "fitting in": 1, "drowned": 0, "crushed by a tree": 2, "nothing":89},
    "fog":     {"sunstroke": 0, "freezing": 2, "lightning strike": 3, "slip": 4, "fitting in": 5, "drowned": 5, "crushed by a tree": 3, "nothing":78},
    "thunder":   {"sunstroke": 0, "freezing": 2, "lightning strike": 5, "slip": 5, "fitting in": 3, "drowned": 3, "crushed by a tree": 6, "nothing":76},
    "heat":    {"sunstroke": 7, "freezing": 0, "lightning strike": 5, "slip": 2, "fitting in": 1, "drowned": 3, "crushed by a tree": 3, "nothing":79},
    "cold":     {"sunstroke": 0, "freezing": 7, "lightning strike": 0, "slip": 3, "fitting in": 2, "drowned": 0, "crushed by a tree": 2, "nothing":86},
}

morality_table = {
    "low":        {"vojak": -20, "lukostřelec": -25, "jezdec": -10, "kavalerie": -15},
    "normal":        {"vojak": 0, "lukostřelec": 0, "jezdec": 0, "kavalerie": 0},
    "lifting":    {"vojak": 10, "lukostřelec": 5, "jezdec": 6, "kavalerie": 6},
    "hight":       {"vojak": 15, "lukostřelec": 15, "jezdec": 10, "kavalerie": 15},
    "excellent":   {"vojak": 30, "lukostřelec": 30, "jezdec": 20, "kavalerie": 25},
}

deadly_event = ["lightning strike", "drowned", "crushed by a tree"]

# třídy věcí
class Jednotka:
    def __init__(self, name:str, hp:int, armour:int, attack:int, atkspeed:float, armour_toughness:int, morality: str):
        Jednotka.event = Ovlivneni.Get_Random_Event()
        self.event = Jednotka.event
        
        self.name = name

        self.lives = Jednotka.Vypocet_HP(hp, name)
        self.max_hp = hp
        
        self.sila_utoku = Jednotka.Vypocet_Sili(attack, name, morality)
        self.rychlost_utoku = atkspeed

        self.brneni = armour
        self.armour_toughness = armour_toughness

        self.morality = morality


    def Vypocet_Sili(attack, name, morality):
        # výpočet síli vojáka
        efekt_mista = place_table.get(name, {})

        misto_efekt = efekt_mista.get(Ovlivneni.teren, 1) / 100

        event = Jednotka.event

        if event != "nothing":
            efekt_eventu = event_table.get(name, {})
            event_efect = efekt_eventu.get(event,1) / 100
        else:
            event_efect = 0

        vliv_moralky = Ovlivneni.Get_Ovlivneni_Moralkou(morality, name)

        konecna_sila = attack + (attack * misto_efekt) + (attack * event_efect) + attack * vliv_moralky

        return konecna_sila
    
    def Vypocet_HP(hp, name):
        # výpočet počtu hp na základě přízni počasí
        efekty_Weather = Weather_table.get(name, {})

        Weather_efekt = efekty_Weather.get(Ovlivneni.Weather, 1) / 100

        event = Jednotka.event

        if event != "nothing":
            if event not in deadly_event:
                efekt_eventu = event_table.get(name, {})
                event_efect = efekt_eventu.get(event,1) / 100
            else:
                event_efect = -100
                Weather_efekt = -100
        else:
            event_efect = 0

        konecna_hp = hp + (hp * Weather_efekt) + (hp * event_efect)

        return konecna_hp

class Ovlivneni: 
    def Weather(misto):
        # výběr terénu
        teren = list(place_weather_table.keys())[misto - 1]
        Ovlivneni.teren = teren

        # počítání šance na jednotlivá počasí
        vahy = place_weather_table.get(teren, {})
        vahy_Weather = [vahy[Weather_typ] for Weather_typ in vahy]
        moznosti_Weather = [Weather_typ for Weather_typ in vahy]
        Ovlivneni.Weather = random.choices(moznosti_Weather, weights=vahy_Weather, k=1)[0]
    
    def Get_Random_Event():
        # nulováni promněných
        typ_veci = None
        vahy_veci = None
        moznosti_veci = None
        vec_misto_typ = None
        typ_veci2 = None
        vahy_veci2 = None
        moznosti_veci2 = None
        vec_Weather_typ = None

        # získání random eventu z tabulky na základě místa
        typ_veci = random_misto_vec.get(Ovlivneni.teren, {})
        vahy_veci = [typ_veci[vec_typ] for vec_typ in typ_veci]
        moznosti_veci = [vec_typ for vec_typ in typ_veci]
        vec_misto_typ = random.choices(moznosti_veci, weights=vahy_veci, k=1)[0]

        # získání random eventu z tabulky na základě počasí
        typ_veci2 = random_Weather_vec.get(Ovlivneni.Weather, {})
        vahy_veci2 = [typ_veci2[vec_typ2] for vec_typ2 in typ_veci2]
        moznosti_veci2 = [vec_typ2 for vec_typ2 in typ_veci2]
        vec_Weather_typ = random.choices(moznosti_veci2, weights=vahy_veci2, k=1)[0]

        # konečné vyhodnocení
        if vec_misto_typ == vec_Weather_typ:
            event = vec_misto_typ
        else:
            event = "nothing"
        
        return event
    
    def Get_Ovlivneni_Moralkou(morality, name):
        pocty = morality_table.get(morality, {})
        ovlivneni = pocty.get(name,1)

        return ovlivneni / 100

class Valka():

    def Boj(army1, army2):
        bojovani = True

        if not len(army1) < 1 or len(army2) < 1:

            while(bojovani):
                # získání random vojáka
                a1_i = random.randint(0, len(army1) - 1)
                a2_i = random.randint(0, len(army2) - 1)

                # zjištění rychlosti síli vojáka
                a1_atk_speed = army1[a1_i].rychlost_utoku
                a2_atk_speed = army2[a2_i].rychlost_utoku

                # zjištění síli vojáka na základě brnění toho druhého
                a1_attack = Valka.Get_attack(army1[a1_i].sila_utoku, army2[a2_i].brneni, army2[a2_i].armour_toughness, army2[a2_i])
                a2_attack = Valka.Get_attack(army2[a2_i].sila_utoku, army1[a1_i].brneni, army1[a1_i].armour_toughness, army1[a1_i])

                # smyčka na souboj 1v1 vojáků
                souboj = True
                ticks = 0

                while(souboj):
                    if ticks == a1_atk_speed:
                        army2[a2_i].lives -= a1_attack
                        a1_atk_speed += army1[a1_i].rychlost_utoku
                    
                    if ticks == a2_atk_speed:
                        army1[a1_i].lives -= a2_attack
                        a2_atk_speed += army2[a2_i].rychlost_utoku

                    ticks += 1

                    if army1[a1_i].lives < 1 or army2[a2_i].lives < 1:
                        souboj = False

                # vymazíní mrtvých vojáků z tabulky
                if army1[a1_i].lives < 1:
                    army1.pop(a1_i)
                
                if army2[a2_i].lives < 1:
                    army2.pop(a2_i)

                if (len(army1) == 0 or len(army2) == 0):
                    bojovani = False

        # zjištění kdo vyhrála
        if (len(army1) == 0 and len(army2) != 0):
            win = "Army 2"

        if (len(army2) == 0 and len(army1) != 0):
            win = "Army 1"

        if(len(army2) == 0 and len(army1) == 0):
            win = "Draw"

        return win
    
    def Get_attack(attack, armour, armour_tgh, komu):
        # výpočet celkové síli vojáka v závyslosti na brnění oponenta
        if armour_tgh > 0:
            komu.armour_toughness -= 1
            return attack - attack * (armour / 100)
        else:
            return attack

class Tabulky:
    def Get_Old_Tabulka(tabulka_objektu):
        tabulka = []
        for objekt in tabulka_objektu:
            radek = f"name: {objekt.name}, hp: {objekt.lives}, event: {objekt.event}, attack: {objekt.sila_utoku}, attack speed: {objekt.rychlost_utoku}, armour: {objekt.brneni}, armour toughness: {objekt.armour_toughness}"
            tabulka.append([radek])
        
        return tabulka
    
    def Get_Misto_Tabulka():
        print("+----------------+")
        print("Chose plece of war.")  
        x = 0
        for misto in place_weather_table:
            print(f"{misto} - {x}")
            x += 1
        print("+----------------+")
        return input("Place: ")
    
    def Get_morality():
        print("+----------------+")
        print("What is the morale of the army? ")
        x = 0 
        for morality in morality_table:
            print(f"{morality} - {x}")
            x += 1
        print("+----------------+")

        index = int(input())

        try:
            morality = list(morality_table.keys())[index]
            pass
        except Exception:
            morality = "normal"

        return morality




misto = Tabulky.Get_Misto_Tabulka()

try:
    misto = int(misto)
    if misto > len(place_table):
        misto = 0
except Exception:
    misto = 0

Ovlivneni.Weather(misto)

# tvoření první armády
army1_table = []
print("First army.")
print("")
morality1 = Tabulky.Get_morality()
print("")
for name, stats in stats_table.items():
    print("Number of " + name)
    pocet = input()
    try:
        pocet = int(pocet)
        for x in range(pocet):
            army1_table.append(Jednotka(name, stats["hp"], stats["armour"], stats["attack"], stats["attack speed"], stats["armour toughness"], morality1))
    except Exception:
        print("Failed to add.")

print("")

# tvoření druhé armády
army2_table = []
print("Second army.")
print("")
morality2 = Tabulky.Get_morality()
print("")
for name, stats in stats_table.items():
    print("Number of " + name)
    pocet = input()
    try:
        pocet = int(pocet)
        for x in range(pocet):
            army2_table.append(Jednotka(name, stats["hp"], stats["armour"], stats["attack"], stats["attack speed"], stats["armour toughness"], morality2))
    except Exception:
        print("Failed to add.")

old_army1 = Tabulky.Get_Old_Tabulka(army1_table)
old_army2 = Tabulky.Get_Old_Tabulka(army2_table)

# zýskání výsledku na základě boje
win = Valka.Boj(army1_table, army2_table)

# vypsání výsledku
print("")
print("The result of the battle: " + win)

print("Remain:")
for x in army1_table:
    print(f"name: {x.name}, hp: {x.lives} / {x.max_hp}, event: {x.event}")

for x in army2_table:
    print(f"name: {x.name}, hp: {x.lives} / {x.max_hp}, event: {x.event}")

print("")

if input("Do you want to list both armies? y/N ") == "y":
    print("Both armies:")

    for x in old_army1:
        print(x[0])

    print("")

    for x in old_army2:
        print(x[0])
