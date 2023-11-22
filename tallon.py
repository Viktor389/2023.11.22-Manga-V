# 1. Írj programot, ami kiírja a képernyőre, hogy ”Hello world!”!

szovegKiir = f"Hello world"
print(szovegKiir)

# 2. Írj programot, beolvassa a felhasználó nevét, majd köszön neki

# Változok 
nev,szovegKiir = "", ""

nev = input("Hogyan Hivnak: ")

szovegKiir = f"Hello {nev}!"
print(szovegKiir)

# 3. Írj programot, ami beolvas egy számot, majd kiírja a kétszeresét

#Változok 
alapSzam, ketszeres, szovegKiir = 0, 0, ""

alapSzam =int(input("Kérem a számot: " ))
ketszeres = 2 *alapSzam
szovegKiir = f"A szám: {alapSzam} kétszerese: {ketszeres}"

print(szovegKiir)

"""
# 4. Írj programot, ami beolvas két számot, majd kiírja:
a. az összegüket;
b. különbségüket;
c. szorzatukat;
d. hányadosukat, ha lehet!
""" 

#Változok 
elso, masodik, osszeg, kulonbseg, szorzat, hanyados, szovegKiir = 0, 0, 0, 0, 0, 

elso = int(input("Kérem az elsö számot: ")) 
masodik = int(input("Kérem a második számot: ")) 

osszeg = elso + masodik 
kulonbseg = elso - masodik 
szorzat = elso * masodik 
hanyadosa = elso / masodik 

szovegKiir  = f"A számok: {elso}, {masodik}"
szovegKiir += f"\nösszege: {osszeg}" 
szovegKiir += f"\nkülönbsége: {kulonbseg}"
szovegKiir += f"\nszorzata: {szorzat}"
szovegKiir += f"\nhányadosa: {hanyadosa}"

print(szovegKiir)


#  5. Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!

#Változok 
elso,masodik, nagyobb, szovegKiir = 0, 0, 0,  ""

elso = int(input("Kérem az elsö számot: ")) 
masodik = int(input("Kérem a második számot: ")) 

if elso < masodik:
    nagyobb = masodik 
else:
    nagyobb = elso 
    
szovegKiir = f"A nagyobb szám: {nagyobb}"

print(szovegKiir)


# 6. Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!

#Változó
elso,masodik,harmadik, legkisebb,  szovegKiir = 0, 0, 0, 0, ""

elso = int(input("Kérem az elsö számot: ")) 
masodik = int(input("Kérem a második számot: ")) 
harmadik = int(input("Kérem a harmadik számot: ")) 

# Sehédváltozó

if elso <= masodik:
    kisebb = elso
else: 
    kisebb = masodik

if kisebb <= harmadik:
        legkisebb = kisebb
else:
    legkisebb=harmadik

    szovegKiir = f"A legkisebb szám: {legkisebb} "  
    print(szovegKiir)