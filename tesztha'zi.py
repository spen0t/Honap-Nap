honapok = ["Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus","Szeptember", "Október", "November", "December"]
napok=[31,29,31,30,31,30,31,31,30,31,30,31]

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

        
"""Erre a def-re azért volt szükség, mert ha nem határozom meg külön azt az esetet, amikor csak a beírt nap a hibás,
   akkor a hónapot ettől függetlenül kiírja és mellé írja a "Hibás adatmegadás!" üzenetet is.
   Viszont azt is észrevettem hogy return használatakor két  vagy több def-nél más a megjelenített formátum.
   Nélküle: "Március 15." def foProgram-mal együtt pedig: "('Március', '15.')"""
   
def foProgram():
    if napValaszto()=="Hibás adatmegadás!":
        return "Hibás adatmegadás!"
    else:
        return (honapNev(),napValaszto())
    
print (foProgram())

    
