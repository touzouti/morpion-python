import tkinter as tk


class Morpion:
    def __init__(self, fenetre):
        self.joueur_actuel = "X"
        self.creer_grille(fenetre)

    def creer_grille(self, fenetre):
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
                bouton.config(
                    command=lambda case=bouton: self.jouer(case)
                )
                bouton.grid(row=ligne, column=colonne)

    def jouer(self, bouton):
        if bouton["text"] == "":
            bouton["text"] = self.joueur_actuel
            self.joueur_actuel = (
                "O" if self.joueur_actuel == "X" else "X"
            )


def main():
    fenetre = tk.Tk()
    fenetre.title("Morpion")
    fenetre.resizable(False, False)

    Morpion(fenetre)

    fenetre.mainloop()


if __name__ == "__main__":
    main()