import tkinter as tk


def creer_grille(fenetre):
    joueur_actuel = "X"

    def jouer(bouton):
        nonlocal joueur_actuel

        if bouton["text"] == "":
            bouton["text"] = joueur_actuel
            joueur_actuel = "O" if joueur_actuel == "X" else "X"

    cadre = tk.Frame(fenetre)
    cadre.pack(expand=True)

    for ligne in range(3):
        for colonne in range(3):
            bouton = tk.Button(
                cadre,
                text="",
                font=("Arial", 32),
                width=4,
                height=2,
            )
            bouton.config(command=lambda case=bouton: jouer(case))
            bouton.grid(row=ligne, column=colonne)


def main():
    fenetre = tk.Tk()
    fenetre.title("Morpion")
    fenetre.resizable(False, False)

    creer_grille(fenetre)

    fenetre.mainloop()


if __name__ == "__main__":
    main()