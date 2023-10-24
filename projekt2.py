"""projekt2.py: I den här koden kan du lägga in ord i en numrerad lista samt ta bort och ändra dem. För att ändra är det "e", för att ta bort är det "x"
och för att sluta är det "q".

__author__  = "Norton Haglind Hilbers"
__version__ = "1.0.0"
__email__   = "norton.haglindhilbers@elev.ga.ntig.se"
"""


import os

from color import bcolors


os.system("cls")


def edit(editnumber, editname):
    namelist[editnumber - 1] = editname #det är minus för att listor börjar på 0
    show(listpos)


def remove(editnumber):
    namelist.pop(editnumber - 1)
    show(listpos)


def show(listpos):
    for i in namelist:
        print(bcolors.CYAN +f"{listpos}) {i}")
        listpos = listpos + 1

def error():
    print(bcolors.RED + f"skriv rätt dumbom🤦‍♂️🤔🤦‍♂️🤔") 

listpos = 1
active = True
print(bcolors.BLUE + f"Välkommen till Namnlist programmet, skriv in ord så kommer de hamna i en numrerad lista. Du kan även tabort med x, ändra med e  och för att avsluta använder du q")
namelist = []
while active:
    name = input(bcolors.YELLOW + f"skriv nåt roligt (sluta=q)(ta bort=x)(edit=e) ")
    if name.lower() == "e":     #ser om input-ens små bokstäver är i villkoret
        if len(namelist)>0:  #ser om listan har något i sig 
            while True:
                try:
                    editnumber = int(input(bcolors.YELLOW + f"vilken vil du ändra? "))
                    if 1 <= editnumber <= len(namelist): #ser om nummret som skrevs får plats i listan/är i listan 
                        editname = input(f"vad vill du skriva? ")
                        edit(editnumber, editname)
                    else:
                        error()
                        continue
                    break
                except:
                    error()
                    continue
        else:
            print(f"det finns inget att ändra")
            continue 
    elif name.lower() == "q":
        print(bcolors.BOLD + f"Din lista är {len(namelist)} ord lång.")

        active = False
    elif name.lower() == "x":
        if len(namelist)>0:
            while True:
                try:
                    editnumber = int(input(bcolors.YELLOW + f"vilken vill du ta bort? "))
                    if 1 <= editnumber <= len(namelist):
                        remove(editnumber)
                    else:
                        error()
                        continue

                    break
                except:
                    error()
                    continue
        else:
            print(f"det finns inget att ta bort")
            continue
    else:
        namelist.append(name)
        show(listpos)
