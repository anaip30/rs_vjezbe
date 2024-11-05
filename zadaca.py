# # 7 validacija i provjera jakosti lozinke
# a = input("Upisilozinku:")
# b = ["password", "lozinka"]
# if not  len(a) >= 8 or not len(a) <=15:
#     print("Lozinka mora sadržavati između 8 i 15 znakova")
# elif   a in b:
#     print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
# elif a.isupper() and a.isdigit(): 
#     print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
# else: 
#     print("Lozinka je jaka!")


# 8 fitiranje parnih iz liste 
    
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def filtiriraj_parne(a):
#     nova = []
#     for b in lista:
#      if b % 2 == 0:
#         nova.append(b)
#     return nova 

# print(filtiriraj_parne(lista)) 

# #9 uklanjanje duplikata iz liste 

# lista1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# def ukloni_duplikate(a):
#   a = list( dict.fromkeys(a))
#   print(a)

# print(ukloni_duplikate(lista1)) # [1, 2, 3, 4, 5]

# # 11 Grupiranje elemenata po paritetu 

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def grupiraj_po_paritetu(lista):
#     parni = []
#     neparni = []
    
#     for b in lista:
#      if b % 2 == 0:
#         parni.append(b)
#      else:
#         neparni.append(b)

#     return (f"'Neparni:' {neparni}, 'Parni:' {parni}")


# print(grupiraj_po_paritetu(lista))

#12 Obrnite rječnik

# rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

# def obrni_rjecnik(a):
#     rijecnik = {v: k for k, v in a.items()}
#     print(rijecnik)
            
 
# print(obrni_rjecnik(rjecnik))


# #13 Napišite sljedeće funkcije:

#1. Funkcija koja vraća n-torku s prvim i zadnjim elementom liste u jednoj liniji koda.
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def prvi_i_zadnji(a):
#   brojac = 0
#   for x in a:
#       brojac= +1
#   print(a[0], a[-1])

# print(prvi_i_zadnji(lista)) # (1, 10)

#   #2 Funkcija koja n-torku s maksimalnim i minimalnim elementom liste, bez korištenja ugrađenih funkcija max() i min()
# lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

# def maks_i_min(a):  
#   maxic = max(a)
#   minic = min(a)
#   return ( maxic, minic)

# lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
# print(maks_i_min(lista))

#3. Funkcija presjek koja prima dva skupa i vraća novi skup s elementima koji se nalaze u oba skupa.
# skup_1 = {1, 2, 3, 4, 5}
# skup_2 = {4, 5, 6, 7, 8}

# def presjek(s1, s2):
    
#   print(s1.intersection(s2))

# print(presjek(skup_1, skup_2)) # {4, 5}

# # 14 prosti brojevi
# 1. Napišite funkciju isPrime() koja prima cijeli broj i vraća True ako je broj prost, a False ako nije. Prost broj je prirodan broj veći do 1 koji je dijeljiv jedino sa 1 i samim sobom.

# def isPrime(a):
#  if a%2 == 0:
#     return True
#  else:
#     return False

# print(isPrime(7))
# print(isPrime(10))

#2. Napišite funkciju primes_in_range() koja prima dva argumenta: start i end i vraća listu svih prostih brojeva u tom rasponu.

# def primes_in_range(a, b):
#  lista =  []
#  for x in range(a,b):
#     if not x % 2 == 0:
#      lista.append(x)
  
#  print(lista)


# print(primes_in_range(1, 10))

# # 15 pobroji samoglasnike i suglasnike 

def count_vowels_consonants(a):
 vowels = "aeiouAEIOU"
 consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
 bvowels = 0
 bconsonants = 0
 for x in a:
  if x in vowels:
      bvowels += 1
  elif x in consonants:
      bconsonants += 1

 return (bvowels , bconsonants)

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))