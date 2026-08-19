import tkinter as tk


def creer_grille(fenetre):
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
            bouton.grid(row=ligne, column=colonne)


def main():
    fenetre = tk.Tk()
    fenetre.title("Morpion")
    fenetre.resizable(False, False)

    creer_grille(fenetre)

    fenetre.mainloop()


if __name__ == "__main__":
    main()