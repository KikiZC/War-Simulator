import random 

# tabulky se statama
staty_table = {
    "vojak":        {"hp": 100, "atack": 10, "atack speed": 3, "armor": 50, "armor toughness": 4},
    "lukostřelec":  {"hp": 80, "atack": 15, "atack speed": 2, "armor": 20, "armor toughness": 2},
    "jezdec":       {"hp": 50, "atack": 16, "atack speed": 4, "armor": 10, "armor toughness": 6},
    "kavalerie":    {"hp": 70, "atack": 25, "atack speed": 5, "armor": 30, "armor toughness": 10},
}

misto_table = {
    "vojak":        {"planina": 10, "hory": -2, "řeka": 0, "les": 5},
    "lukostřelec":  {"planina": 15, "hory": 10, "řeka": 10, "les": -10},
    "jezdec":       {"planina": 17, "hory": 0, "řeka": -2, "les": -20},
    "kavalerie":    {"planina": 25, "hory": 0, "řeka": -5, "les": -20},
}

pocasi_table = {
    "vojak":        {"hezky": 0, "pršet": -5, "sníh": -15, "mlha": -15, "bouřka": -25, "vedro": -20, "zima": -30},
    "lukostřelec":  {"hezky": 0, "pršet": -25, "sníh": -20, "mlha": -15, "bouřka": -40, "vedro": -10, "zima": -10},
    "jezdec":       {"hezky": 0, "pršet": -5, "sníh": -10, "mlha": -10, "bouřka": -25, "vedro": -10, "zima": -30},
    "kavalerie":    {"hezky": 0, "pršet": -10, "sníh": -10, "mlha": -20, "bouřka": -30, "vedro": -15, "zima": -40},
}

event_table = {
    "vojak":        {"úpal": -30, "zmrznutí": -25, "zásah bleskem": -50, "uklouznutí": -60, "zapadnutí": -40, "utonutí": -100, "rozmačkáno stromem": -100},
    "lukostřelec":  {"úpal": -40, "zmrznutí": -30, "zásah bleskem": -20, "uklouznutí": -30, "zapadnutí": -60, "utonutí": -100, "rozmačkáno stromem": -100},
    "jezdec":       {"úpal": -100, "zmrznutí": -70, "zásah bleskem": -90, "uklouznutí": -95, "zapadnutí": -100, "utonutí": -100, "rozmačkáno stromem": -100},
    "kavalerie":    {"úpal": -10, "zmrznutí": -5, "zásah bleskem": -30, "uklouznutí": -50, "zapadnutí": -60, "utonutí": -100, "rozmačkáno stromem": -100},
}

mistni_pocasi_table = {
    "planina": {"hezky": 42, "pršet": 20, "sníh": 1, "mlha": 6, "bouřka": 6, "vedro": 20, "zima": 5},
    "les":     {"hezky": 31, "pršet": 15, "sníh": 1, "mlha": 30, "bouřka": 20, "vedro": 1, "zima": 2},
    "hory":    {"hezky": 15, "pršet": 10, "sníh": 20, "mlha": 20, "bouřka": 10, "vedro": 5, "zima": 20},
    "řeka":    {"hezky": 15, "pršet": 10, "sníh": 5, "mlha": 35, "bouřka": 5, "vedro": 1, "zima": 29},
}

random_misto_vec = {
    "planina":  {"úpal": 5, "zmrznutí": 2, "zásah bleskem": 2, "uklouznutí": 3, "zapadnutí": 3, "utonutí": 0, "rozmačkáno stromem": 1, "nic":84},
    "les":      {"úpal": 0, "zmrznutí": 3, "zásah bleskem": 1, "uklouznutí": 1, "zapadnutí": 3, "utonutí": 2, "rozmačkáno stromem": 5, "nic":85},
    "hory":     {"úpal": 2, "zmrznutí": 5, "zásah bleskem": 3, "uklouznutí": 4, "zapadnutí": 3, "utonutí": 1, "rozmačkáno stromem": 1, "nic":81},
    "řeka":     {"úpal": 2, "zmrznutí": 1, "zásah bleskem": 1, "uklouznutí": 5, "zapadnutí": 2, "utonutí": 6, "rozmačkáno stromem": 3, "nic":80},
}

random_pocasi_vec = {
    "hezky":    {"úpal": 5, "zmrznutí": 0, "zásah bleskem": 0, "uklouznutí": 2, "zapadnutí": 3, "utonutí": 3, "rozmačkáno stromem": 3, "nic":84},
    "pršet":    {"úpal": 0, "zmrznutí": 1, "zásah bleskem": 2, "uklouznutí": 4, "zapadnutí": 2, "utonutí": 1, "rozmačkáno stromem": 3, "nic":87},
    "sníh":     {"úpal": 0, "zmrznutí": 5, "zásah bleskem": 0, "uklouznutí": 3, "zapadnutí": 1, "utonutí": 0, "rozmačkáno stromem": 2, "nic":89},
    "mlha":     {"úpal": 0, "zmrznutí": 2, "zásah bleskem": 3, "uklouznutí": 4, "zapadnutí": 5, "utonutí": 5, "rozmačkáno stromem": 3, "nic":78},
    "bouřka":   {"úpal": 0, "zmrznutí": 2, "zásah bleskem": 5, "uklouznutí": 5, "zapadnutí": 3, "utonutí": 3, "rozmačkáno stromem": 6, "nic":76},
    "vedro":    {"úpal": 7, "zmrznutí": 0, "zásah bleskem": 5, "uklouznutí": 2, "zapadnutí": 1, "utonutí": 3, "rozmačkáno stromem": 3, "nic":79},
    "zima":     {"úpal": 0, "zmrznutí": 7, "zásah bleskem": 0, "uklouznutí": 3, "zapadnutí": 2, "utonutí": 0, "rozmačkáno stromem": 2, "nic":86},
}

moralka_table = {
    "nízká":        {"vojak": -20, "lukostřelec": -25, "jezdec": -10, "kavalerie": -15},
    "běžná":        {"vojak": 0, "lukostřelec": 0, "jezdec": 0, "kavalerie": 0},
    "zvedající":    {"vojak": 10, "lukostřelec": 5, "jezdec": 6, "kavalerie": 6},
    "vysoká":       {"vojak": 15, "lukostřelec": 15, "jezdec": 10, "kavalerie": 15},
    "vynikající":   {"vojak": 30, "lukostřelec": 30, "jezdec": 20, "kavalerie": 25},
}

deadly_event = ["zásah bleskem", "utonutí", "rozmačkáno stromem"]

# třídy věcí
class Jednotka:
    def __init__(self, name:str, hp:int, armor:int, atack:int, atkspeed:float, armor_toughness:int, moralka: str):
        Jednotka.event = Ovlivneni.Get_Random_Event()
        self.event = Jednotka.event
        
        self.jmeno = name

        self.zivoty = Jednotka.Vypocet_HP(hp, name)
        self.max_hp = hp
        
        self.sila_utoku = Jednotka.Vypocet_Sili(atack, name, moralka)
        self.rychlost_utoku = atkspeed

        self.brneni = armor
        self.armor_toughness = armor_toughness

        self.moralka = moralka


    def Vypocet_Sili(atack, jmeno, moralka):
        # výpočet síli vojáka
        efekt_mista = misto_table.get(jmeno, {})

        misto_efekt = efekt_mista.get(Ovlivneni.teren, 1) / 100

        event = Jednotka.event

        if event != "nic":
            efekt_eventu = event_table.get(jmeno, {})
            event_efect = efekt_eventu.get(event,1) / 100
        else:
            event_efect = 0

        vliv_moralky = Ovlivneni.Get_Ovlivneni_Moralkou(moralka, jmeno)

        konecna_sila = atack + (atack * misto_efekt) + (atack * event_efect) + atack * vliv_moralky

        return konecna_sila
    
    def Vypocet_HP(hp, jmeno):
        # výpočet počtu hp na základě přízni počasí
        efekty_pocasi = pocasi_table.get(jmeno, {})

        pocasi_efekt = efekty_pocasi.get(Ovlivneni.pocasi, 1) / 100

        event = Jednotka.event

        if event != "nic":
            if event not in deadly_event:
                efekt_eventu = event_table.get(jmeno, {})
                event_efect = efekt_eventu.get(event,1) / 100
            else:
                event_efect = -100
                pocasi_efekt = -100
        else:
            event_efect = 0

        konecna_hp = hp + (hp * pocasi_efekt) + (hp * event_efect)

        return konecna_hp

class Ovlivneni: 
    def Pocasi(misto):
        # výběr terénu
        teren = list(mistni_pocasi_table.keys())[misto - 1]
        Ovlivneni.teren = teren

        # počítání šance na jednotlivá počasí
        vahy = mistni_pocasi_table.get(teren, {})
        vahy_pocasi = [vahy[pocasi_typ] for pocasi_typ in vahy]
        moznosti_pocasi = [pocasi_typ for pocasi_typ in vahy]
        Ovlivneni.pocasi = random.choices(moznosti_pocasi, weights=vahy_pocasi, k=1)[0]
    
    def Get_Random_Event():
        # nulováni promněných
        typ_veci = None
        vahy_veci = None
        moznosti_veci = None
        vec_misto_typ = None
        typ_veci2 = None
        vahy_veci2 = None
        moznosti_veci2 = None
        vec_pocasi_typ = None

        # získání random eventu z tabulky na základě místa
        typ_veci = random_misto_vec.get(Ovlivneni.teren, {})
        vahy_veci = [typ_veci[vec_typ] for vec_typ in typ_veci]
        moznosti_veci = [vec_typ for vec_typ in typ_veci]
        vec_misto_typ = random.choices(moznosti_veci, weights=vahy_veci, k=1)[0]

        # získání random eventu z tabulky na základě počasí
        typ_veci2 = random_pocasi_vec.get(Ovlivneni.pocasi, {})
        vahy_veci2 = [typ_veci2[vec_typ2] for vec_typ2 in typ_veci2]
        moznosti_veci2 = [vec_typ2 for vec_typ2 in typ_veci2]
        vec_pocasi_typ = random.choices(moznosti_veci2, weights=vahy_veci2, k=1)[0]

        # konečné vyhodnocení
        if vec_misto_typ == vec_pocasi_typ:
            event = vec_misto_typ
        else:
            event = "nic"
        
        return event
    
    def Get_Ovlivneni_Moralkou(moralka, jmeno):
        pocty = moralka_table.get(moralka, {})
        ovlivneni = pocty.get(jmeno,1)

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
                a1_atack = Valka.Get_Atack(army1[a1_i].sila_utoku, army2[a2_i].brneni, army2[a2_i].armor_toughness, army2[a2_i])
                a2_atack = Valka.Get_Atack(army2[a2_i].sila_utoku, army1[a1_i].brneni, army1[a1_i].armor_toughness, army1[a1_i])

                # smyčka na souboj 1v1 vojáků
                souboj = True
                ticks = 0

                while(souboj):
                    if ticks == a1_atk_speed:
                        army2[a2_i].zivoty -= a1_atack
                        a1_atk_speed += army1[a1_i].rychlost_utoku
                    
                    if ticks == a2_atk_speed:
                        army1[a1_i].zivoty -= a2_atack
                        a2_atk_speed += army2[a2_i].rychlost_utoku

                    ticks += 1

                    if army1[a1_i].zivoty < 1 or army2[a2_i].zivoty < 1:
                        souboj = False

                # vymazíní mrtvých vojáků z tabulky
                if army1[a1_i].zivoty < 1:
                    army1.pop(a1_i)
                
                if army2[a2_i].zivoty < 1:
                    army2.pop(a2_i)

                if (len(army1) == 0 or len(army2) == 0):
                    bojovani = False

        # zjištění kdo vyhrála
        if (len(army1) == 0 and len(army2) != 0):
            win = "Armáda 2"

        if (len(army2) == 0 and len(army1) != 0):
            win = "Armáda 1"

        if(len(army2) == 0 and len(army1) == 0):
            win = "Remíza"

        return win
    
    def Get_Atack(atack, armor, armor_tgh, komu):
        # výpočet celkové síli vojáka v závyslosti na brnění oponenta
        if armor_tgh > 0:
            komu.armor_toughness -= 1
            return atack - atack * (armor / 100)
        else:
            return atack

class Tabulky:
    def Get_Old_Tabulka(tabulka_objektu):
        tabulka = []
        for objekt in tabulka_objektu:
            radek = f"Jmeno: {objekt.jmeno}, hp: {objekt.zivoty}, event: {objekt.event}, útok: {objekt.sila_utoku}, rychlost utoku: {objekt.rychlost_utoku}, brnění: {objekt.brneni}, pevnost brnění: {objekt.armor_toughness}"
            tabulka.append([radek])
        
        return tabulka
    
    def Get_Misto_Tabulka():
        print("+----------------+")
        print("Vyber místo boje.")  
        x = 0
        for misto in mistni_pocasi_table:
            print(f"{misto} - {x}")
            x += 1
        print("+----------------+")
        return input("Místo: ")
    
    def Get_Moralka():
        print("+----------------+")
        print("Jaká je morálka armády? ")
        x = 0 
        for moralka in moralka_table:
            print(f"{moralka} - {x}")
            x += 1
        print("+----------------+")

        index = int(input())

        try:
            moralka = list(moralka_table.keys())[index]
            pass
        except Exception:
            moralka = "běžná"

        return moralka




misto = Tabulky.Get_Misto_Tabulka()

try:
    misto = int(misto)
    if misto > len(misto_table):
        misto = 0
except Exception:
    misto = 0

Ovlivneni.Pocasi(misto)

# tvoření první armády
armada1_tabulka = []
print("První armáda.")
print("")
moralka1 = Tabulky.Get_Moralka()
print("")
for jmeno, staty in staty_table.items():
    print("Zadej počet " + jmeno)
    pocet = input()
    try:
        pocet = int(pocet)
        for x in range(pocet):
            armada1_tabulka.append(Jednotka(jmeno, staty["hp"], staty["armor"], staty["atack"], staty["atack speed"], staty["armor toughness"], moralka1))
    except Exception:
        print("Nepovedlo se přidat.")

print("")

# tvoření druhé armády
armada2_tabulka = []
print("Druhá armáda.")
print("")
moralka2 = Tabulky.Get_Moralka()
print("")
for jmeno, staty in staty_table.items():
    print("Zadej počet " + jmeno)
    pocet = input()
    try:
        pocet = int(pocet)
        for x in range(pocet):
            armada2_tabulka.append(Jednotka(jmeno, staty["hp"], staty["armor"], staty["atack"], staty["atack speed"], staty["armor toughness"], moralka2))
    except Exception:
        print("Nepovedlo se přidat.")

old_army1 = Tabulky.Get_Old_Tabulka(armada1_tabulka)
old_army2 = Tabulky.Get_Old_Tabulka(armada2_tabulka)

# zýskání výsledku na základě boje
win = Valka.Boj(armada1_tabulka, armada2_tabulka)

# vypsání výsledku
print("")
print("Výsledek bitvy: " + win)

print("Zbylo:")
for x in armada1_tabulka:
    print(f"jmeno: {x.jmeno}, hp: {x.zivoty} / {x.max_hp}, event: {x.event}")

for x in armada2_tabulka:
    print(f"jmeno: {x.jmeno}, hp: {x.zivoty} / {x.max_hp}, event: {x.event}")

print("")

if input("Chceš vypsat obě armády? a/N ") == "a":
    print("Obě armády:")

    for x in old_army1:
        print(x[0])

    print("")

    for x in old_army2:
        print(x[0])
