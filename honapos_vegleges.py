honapok= ["Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október", "November", "December"]
napok=[31,29,31,30,31,30,31,31,30,31,30,31]
h=input("Hónap: ")
n=input("Nap: ")

def szamHiba():
    try:
        int(n)
        return True
    except ValueError:
        return False

def napHiba():
    nap=int(n)
    index=honapok.index(h)
    napmax=napok[index]
    if nap>=napmax and nap<0:
        return False

if szamHiba()==False:
    print("Hiba")
elif h not in honapok:
    print("Hiba")
elif napHiba()==False:
    print("Hiba")
else:
    print("{} {}.".format(h,n))   
