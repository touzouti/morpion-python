import tkinter as tk


class Morpion:
    def __init__(self, fenetre):
        self.joueur_actuel = "X"
        self.partie_terminee = False
        self.boutons = []

        self.message = tk.Label(
            fenetre,
            text="Au tour du joueur X",
            font=("Arial", 16),
        )
        self.message.pack(pady=10)

        self.creer_grille(fenetre)

        bouton_recommencer = tk.Button(
            fenetre,
            text="Recommencer",
            font=("Arial", 12),
            command=self.recommencer,
        )
        bouton_recommencer.pack(pady=10)

    def creer_grille(self, fenetre):
        cadre = tk.Frame(fenetre)
        cadre.pack(padx=10, pady=10)

        for ligne in range(3):
            rangee = []

            for colonne in range(3):
                bouton = tk.Button(
                    cadre,
                    text="",
                    font=("Arial", 32),
                    width=4,
                    height=2,
                    command=lambda l=ligne, c=colonne: self.jouer(l, c),
                )
                bouton.grid(row=ligne, column=colonne)
                rangee.append(bouton)

            self.boutons.append(rangee)

    def jouer(self, ligne, colonne):
        bouton = self.boutons[ligne][colonne]

        if bouton["text"] != "" or self.partie_terminee:
            return

        bouton["text"] = self.joueur_actuel

        if self.verifier_victoire():
            self.message.config(
                text=f"Le joueur {self.joueur_actuel} a gagné !"
            )
            self.partie_terminee = True
            self.desactiver_grille()
        elif self.verifier_match_nul():
            self.message.config(text="Match nul !")
            self.partie_terminee = True
        else:
            self.joueur_actuel = (
                "O" if self.joueur_actuel == "X" else "X"
            )
            self.message.config(
                text=f"Au tour du joueur {self.joueur_actuel}"
            )

    def recommencer(self):
        self.joueur_actuel = "X"
        self.partie_terminee = False
        self.message.config(text="Au tour du joueur X")

        for rangee in self.boutons:
            for bouton in rangee:
                bouton.config(text="", state="normal")

    def verifier_victoire(self):
        combinaisons = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        return any(
            all(
                self.boutons[ligne][colonne]["text"]
                == self.joueur_actuel
                for ligne, colonne in combinaison
            )
            for combinaison in combinaisons
        )

    def verifier_match_nul(self):
        return all(
            bouton["text"] != ""
            for rangee in self.boutons
            for bouton in rangee
        )

    def desactiver_grille(self):
        for rangee in self.boutons:
            for bouton in rangee:
                bouton.config(state="disabled")


def main():
    fenetre = tk.Tk()
    fenetre.title("Morpion")
    fenetre.resizable(False, False)

    Morpion(fenetre)

    fenetre.mainloop()


if __name__ == "__main__":
    main()