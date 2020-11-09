honapok = ["Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus","Szeptember", "Október", "November", "December"]
napok=[31,29,31,30,31,30,31,31,30,31,30,31]
"""Syökőév napjai"""
napokSz=[31,28,31,30,31,30,31,31,30,31,30,31]

e=int(input("Év: "))
h=input("Hónap: ")
n=int(input("Nap: "))

index1 = honapok.index(h)


def honapNev():
    if h in honapok:  
        return h
    else:
        return "nem jo"
    
    
"""Ezt a részt vegül nem használtam fel, mert nem volt rá szükség"""
"""def honapValaszto():
       if h in honapok:
           return index1"""
    
def napValaszto():
    napmax= napok[index1]
    if n<=napmax and n>0:
        return "{}.".format(n)
    else:
        return "Hibás adatmegadás!"


def napValasztoSz():
    napmax2= napokSz[index1]
    if n<=napmax2 and n>0:
        return "{}.".format(n)
    else:
        return "Hibás adatmegadás!"

        
"""Erre a def-re azért volt szükség, mert ha nem határozom meg külön azt az esetet, amikor csak a beírt nap a hibás,
   akkor a hónapot ettől függetlenül kiírja és mellé írja a "Hibás adatmegadás!" üzenetet is.
   Viszont azt is észrevettem hogy return használatakor két  vagy több def-nél más a megjelenített formátum.
   Nélküle: "Március 15." def simaEvek-kel együtt pedig: "('Március', '15.')"""
   
def simaEvek():
    if napValaszto()=="Hibás adatmegadás!":
        return "Hibás adatmegadás!"
    else:
        return (honapNev(),napValaszto())
    
def szokoEvek():
    if napValaszto()=="Hibás adatmegadás!":
        return "Hibás adatmegadás!"
    else:
        return (honapNev(),napValasztoSz())


def milyenEv():
    if e%4==0:
        return szokoEvek()
    elif e%4==1:
        return simaEvek()
    else:
        return "Hibás adatmegadás!"

"""Ez a rész szintén leginkább a "Hibás adatmegadás!"  üzenetet hivatott kiírni,
abban az esetben ha csak a dátum hibás az eredeti üzenet így nézne ki:
1996 ('November', 'Hibás adatmegadás!')
viszont ezzel megfeleló"""
    
if napValaszto()=="Hibás adatmegadás!":
    print("Hibás adatmegadás!")
elif napValasztoSz()=="Hibás adatmegadás!":
    print("Hibás adatmegadás!")
else:
    print ("{} {} {}.".format(e,h,n))

    
