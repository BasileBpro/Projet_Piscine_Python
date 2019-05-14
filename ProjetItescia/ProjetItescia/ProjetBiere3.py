from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import datetime
import serial
from threading import Thread

class WaitingBadge(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        ser = serial.Serial('COM3', 115200)
        # cette info est donnee par l'interface java arduino
        print(ser)
        global y
        y = True
        while (y == True):  # mettre autre condition, un compteur par exemple
            x = ser.readline()  # read one byte
            print("x=", x)
            if (x != ""):
                #move()
                y = False
        ser.close()


# VARIABLES GLOBAL
global solde
global Frame2
state = True

#LECTURE CARTE/FICHIER
mon_fichier = open("TireuseBiere.txt", "r")
infos = mon_fichier.read()
infos = infos.replace(';', " ")
infos = infos.split()
mon_fichier.close()

fichier_conso = open("Consos.txt", "r")
consommations = fichier_conso.read()
consommations = consommations.split()
fichier_conso.close()

""""#RAJOUTER DE L'ARGENT
def rajoutArgent():
    if infos[4] == "Oui":
        infos[0] = int(infos[0]) + int(argentRajout.get())
        montantBase.config(text="Montant de base : " + str(infos[0]) + "€")"""

"""def verifCompte():
    if infos[4] == "Oui":
        rajout.config(state=NORMAL)
    else:
        rajout.config(state=DISABLED)"""


def fen1():
    def soldeRestant(var):
        if (var == 1):
            infos[0] = int(infos[0]) + int(rajout.get())
        else:
            fichier_conso = open("Consos.txt", "r")
            consommations = fichier_conso.read()
            consommations = consommations.split()
            fichier_conso.close()
            depenses = 0
            for i in range(3, len(consommations), 4):
                depenses = depenses + float(consommations[i])
            depenses = str(round(int(infos[0]) - depenses, 2))
            canvasFirst.itemconfig(montantFinal, text=depenses)
    #Calcul le solde restant
    def soldeRestantBis(var):

        fichier_conso = open("Consos.txt", "r")
        consommations = fichier_conso.read()
        consommations = consommations.split()
        fichier_conso.close()
        depenses = 0
        for i in range(3, len(consommations), 4):
             depenses = depenses + float(consommations[i])
        depenses = str(round(int(infos[0]) - depenses, 2))
        canvasFirst.itemconfig(montantFinal, text=depenses)


    # FONCTION CHOIX DE LA BIERE
    def Remplissage():
        if (value.get() == 1):
            canvasFirst.itemconfig(choixBiere, text="   Vous pouvez vous servir en Leif", justify='center')
        elif (value.get() == 2):
            canvasFirst.itemconfig(choixBiere, text="   Vous pouvez vous servir en 1664", justify='center')
        elif (value.get() == 3):
            canvasFirst.itemconfig(choixBiere, text="    Vous pouvez vous servir en Vanpur", justify='center')
        elif (value.get() == 4):
            canvasFirst.itemconfig(choixBiere, text="    Vous pouvez vous servir en Fisher", justify='center')
        elif (value.get() == 5):
            canvasFirst.itemconfig(choixBiere, text="    Vous pouvez vous servir en Chimay", justify='center')
        elif (value.get() == 6):
            canvasFirst.itemconfig(choixBiere, text="    Vous pouvez vous servir en Corona", justify='center')
        soldeRestant(0)
    def validation():
        """choixValide = Label(fenetre, text="Servez vous en bière " + str(value.get()), font="Arial 16")
        choixValide.place(relx=0.375, rely=0.625)"""
        fichier_conso = open("Consos.txt", "r")
        save = fichier_conso.read()
        fichier_conso.close()
        fichier_conso = open("Consos.txt", "w")
        date = datetime.datetime.now()
        data = " " + str(date.day) + "/" + str(date.month) + " " + str(date.hour) + ":" + str(date.minute) + " "
        if (value.get() == 1):
            prix = 6.5
            save = save + data + "Biere" + str(value.get()) + " " + str(prix)
        elif (value.get() == 2):
            prix = 4.8
            save = save + data + "Biere" + str(value.get()) + " " + str(prix)
        elif (value.get() == 3):
            prix = 5.2
            save = save + data + "Biere" + str(value.get()) + " " + str(prix)
        elif (value.get() == 4):
            prix = 3.1
            save = save + data + "Biere" + str(value.get()) + " " + str(prix)
        elif (value.get() == 5):
            prix = 4.7
            save = save + data + "Biere" + str(value.get()) + " " + str(prix)
        elif (value.get() == 6):
            prix = 7.1
            save = save + data + "Biere" + str(value.get()) + " " + str(prix)
        fichier_conso.write(save)
        print(save)

    def fen2():
        # FONCTION SOLDE RESTANT
        def soldeRestant(var):
            if(var==1):
                infos[0] = int(infos[0]) + int(rajout.get())
            else:
                fichier_conso = open("Consos.txt", "r")
                consommations = fichier_conso.read()
                consommations = consommations.split()
                fichier_conso.close()
                depenses = 0
                liste.delete(0, END)
                for i in range(3, len(consommations), 4):
                    depenses = depenses + float(consommations[i])
                depenses = str(round(int(infos[0]) - depenses, 2))
                canvasFirst.itemconfig(montantFinal, text=depenses)
                j = 0
                for i in range(0, len(consommations), 4):
                    j += 1
                    liste.insert(j, consommations[i] + " " + consommations[i + 1] + "   " + consommations[
                        i + 2] + "               " + consommations[i + 3])

        # CREATION DE LA FENETRE
        fenetre2 = Toplevel()
        fenetre2.title("Dépenses")
        fenetre2.geometry("620x480")

        # CANVAS PAGE APPLICATION
        image = PhotoImage(file="ResultatPython3.png")
        canvasSecond = tk.Canvas(fenetre2, width=620, height=480)
        canvasSecond.pack(fill=BOTH, expand=1)
        canvasSecond.create_image(-175, 0, image=image, anchor=NW)

        # CREATION LISTE DEPENSES
        liste = tk.Listbox(fenetre2)
        liste.place(relx=0.49, rely=0.475, anchor=CENTER, height=250, width=225)

        # RAJOUTER DE L"ARGENT
        argentRajout = StringVar()
        rajout = tk.Entry(fenetre2, textvariable=argentRajout)
        boutonAjout = tk.Button(fenetre2, text="Réapprovisionner", command=lambda :soldeRestant(1), relief='groove')

        rajout.place(relx=0.38, rely=0.8)
        boutonAjout.place(relx=0.40, rely=0.85)

        soldeRestant(0)
        fenetre2.mainloop()

    fenetre0.destroy()
    fenetre = tk.Tk()
    fenetre.title("Tireuse à bières")
    fenetre.resizable(width=False, height=False)

    # PARAMETRES DE LA FENETRE
    fenetre.geometry("1000x650")

    # CANVAS PAGE APPLICATION
    testtt = PhotoImage(file='SecondGround.png')
    canvasFirst = tk.Canvas(fenetre, width=1000, height=650)
    canvasFirst.pack(fill=BOTH, expand=1)
    canvasFirst.create_image(0, 0, image=testtt, anchor=NW)

    # DONNEES UTILISATEUR
    nomC = StringVar()
    nomC = "Nom-Prenom :"
    nomCtext = canvasFirst.create_text(850, 150, text=nomC, font="Gabriola 25 underline", justify='center')

    nomCbis = StringVar()
    nomCbis = infos[2] + " " + infos[3]
    nomCbisText = canvasFirst.create_text(850, 185, text=nomCbis, font="Gabriola 22", justify='center')
    cb = StringVar()
    cb = "Carte bleue liée :"
    canvasFirst.create_text(850, 250, text=cb, font="Gabriola 25 underline", justify='center')
    cbbis = StringVar()
    cbbis = infos[4]
    canvasFirst.create_text(850, 285, text=cbbis, font="Gabriola 22", justify='center')
    montantB = StringVar()
    montantB = "Solde restant :"
    canvasFirst.create_text(850, 340, text=montantB, font="Gabriola 25 underline", justify='center')
    montantBbis = StringVar()
    montantBbis = infos[0] + "€"
    montantFinal = canvasFirst.create_text(850, 370, text=montantBbis, font="Gabriola 22", justify='center')

    value = IntVar()
    value.set(0)

    # LISTE DES BIERES A CHOISIR
    bouton1 = Radiobutton(fenetre, text="Leif 6€50/L", font="Gabriola 12", variable=value, value="1", command=Remplissage, indicatoron=0, width=15)
    bouton2 = Radiobutton(fenetre, text="1664 4€80/L", font="Gabriola 12", variable=value, value="2", command=Remplissage, indicatoron=0, width=15)
    bouton3 = Radiobutton(fenetre, text="Vanpur 5€20/L", font="Gabriola 12", variable=value, value="3", command=Remplissage, indicatoron=0, width=15)
    bouton4 = Radiobutton(fenetre, text="Fisher 3€10/L", font="Gabriola 12", variable=value, value="4", command=Remplissage, indicatoron=0, width=15)
    bouton5 = Radiobutton(fenetre, text="Chimay 4€70/L", font="Gabriola 12", variable=value, value="5", command=Remplissage, indicatoron=0, width=15)
    bouton6 = Radiobutton(fenetre, text="Corona 7€10/L", font="Gabriola 12", variable=value, value="6", command=Remplissage, indicatoron=0, width=15)

    # CHOIX DE LA BIERE
    choixBiere = canvasFirst.create_text(475, 545,text="Vous pouvez vous servir en ?", font="Gabriola 24")

    # VALIDATION DU CHOIX DE LA BIERE
    valider = Button(fenetre, text="Valider votre choix", font="Arial 14", command=validation, relief='ridge')

    # RECUPERER LE SOLDE RESTANT DU CLIENT
    solde = StringVar()

    """"#AFFICHER LE SOLDE RESTANT DU CLIENT
    soldeRes = Label(fenetre, textvariable=solde,font="Arial 12")
    soldeRes["bg"]="white"
    soldeRes.place(relx=0.77,rely=0.97, width=175, height=20)"""

    # POSITIONNEMENT DES BOUTONS
    bouton1.place(relx=0.08, rely=0.18)
    bouton2.place(relx=0.08, rely=0.25)
    bouton3.place(relx=0.08, rely=0.32)
    bouton4.place(relx=0.08, rely=0.39)
    bouton5.place(relx=0.08, rely=0.46)
    bouton6.place(relx=0.08, rely=0.53)
    valider.place(relx=0.395, rely=0.93)

    # CREATION BOUTON DEPENSES
    ImageBtn = tk.PhotoImage(file="settings.png")

    boutonDep = tk.Button(fenetre, image=ImageBtn, command=fen2)
    boutonDep.place(relx=0.96, rely=0.94)
    soldeRestantBis(0)
    # LANCEMENT DE LA FENETRE
    fenetre.mainloop()



label_status = 'place'

fenetre0 = tk.Tk()
fenetre0.title("Tireuse à bières")
fenetre0.resizable(width=False, height=False)

# PARAMETRES DE LA FENETRE
fenetre0.geometry("1000x650")

# CANVAS ANIMATION
can = tk.Canvas(fenetre0, width=1200, height=800)
can.pack()

def clignotement():
    global label_status

    if label_status == 'place':
        # CACHE LE TEXTE
        btn.place_forget()
        can.itemconfig(labelll, state=HIDDEN)
        label_status = 'not_place'
    else:
        # AFFICHAGE DU TEXTE
        btn.place(relx=0.0, rely=0.0)
        can.itemconfig(labelll, state=NORMAL)
        label_status = 'place'

        # BOUCLE TOUTES LES 750MS
    fenetre0.after(750, clignotement)

def move():
    btn.destroy()

    # INITIASION VARIABLES DEPLACEMENT
    x=-2
    y=0

    # ANIMATION
    can.move(img,x,y)
    can.move(img2,-x,y)
    if(can.coords(img)[0]>-100):
        can.after(25, move)
    else:
        fen1()

# IMAGE POUR L'ANIMATION
img_import = tk.PhotoImage(file="G.png")
img = can.create_image(400, 800, image=img_import)
img2_import = tk.PhotoImage(file="D.png")
img2 = can.create_image(400, 800, image=img2_import)

# POSITIONNEMENT IMAGE
can.coords(img2, 801, 325)
can.coords(img, 200, 325)

# CREATION TEXTE CLIGNOTEMENT
labelll = can.create_text(500, 615, text="Inserer votre badge", font="Terminal 30", fill="white")
btn = tk.Button(fenetre0, width=20, text="Inserer votre badge", font="Terminal 18", command=move, bg=None)
btn.place(relx=0.0, rely=0.0)

# LANCEMENT CLIGNOTEMENT TEXTE

clignotement()

# LANCEMENT THREAD ATTENTE DU BADGE
thread_1 = WaitingBadge()
thread_1.start()
thread_1.join()

# LANCEMENT DE LA FENETRE
fenetre0.mainloop()


#LE BOUTON SUR LA PAGE DE DEBUT EST SEULEMENT LA DANS LE BUT D ETRE UTILISE SANS LA RASPBERRY MAIS PEUT ETRE RETIRE