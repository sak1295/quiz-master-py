# -*- coding: utf-8 -*-
class Question:
    def __init__(self, texte, reponses, bonne_reponse):
        self.texte = texte
        self.reponses = reponses  # Liste de 3 reponses
        self.bonne_reponse = bonne_reponse  # Index de la bonne reponse (0, 1 ou 2)

    def verifier_reponse(self, reponse_utilisateur):
        # Convertir la reponse a/b/c en index 0/1/2
        conversion = {'a': 0, 'b': 1, 'c': 2}
        return conversion.get(reponse_utilisateur.lower()) == self.bonne_reponse

    def afficher_question(self):
        print("\n" + self.texte)
        for i, reponse in enumerate(self.reponses):
            print(f"{chr(97 + i)}) {reponse}")

    def afficher_correction(self):
        print(f"\nQuestion : {self.texte}")
        print(f"La bonne reponse etait : {chr(97 + self.bonne_reponse)}) {self.reponses[self.bonne_reponse]}")