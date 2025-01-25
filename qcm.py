# -*- coding: utf-8 -*-
import random
from question import Question

class QCM:
    def __init__(self):
        self.questions = self._creer_questions()
        self.score = 0

    def _creer_questions(self):
        questions = [
            Question(
                "Quelle est la capitale de la France ?",
                ["Londres", "Paris", "Berlin"],
                1
            ),
            Question(
                "Quel est le plus grand ocean du monde ?",
                ["Atlantique", "Indien", "Pacifique"],
                2
            ),
            Question(
                "Combien de continents y a-t-il sur Terre ?",
                ["5", "6", "7"],
                2
            ),
            Question(
                "Qui a peint La Joconde ?",
                ["Van Gogh", "Michel-Ange", "Leonard de Vinci"],
                2
            ),
            Question(
                "Quelle est la planete la plus proche du Soleil ?",
                ["Venus", "Mercure", "Mars"],
                1
            ),
            Question(
                "En quelle annee a eu lieu la Revolution francaise ?",
                ["1789", "1792", "1799"],
                0
            ),
            Question(
                "Quel est le symbole chimique de l'or ?",
                ["Ag", "Au", "Cu"],
                1
            ),
            Question(
                "Qui a ecrit 'Les Miserables' ?",
                ["Victor Hugo", "Emile Zola", "Gustave Flaubert"],
                0
            ),
            Question(
                "Quelle est la plus haute montagne du monde ?",
                ["Mont Blanc", "K2", "Mont Everest"],
                2
            ),
            Question(
                "Quel est l'element le plus abondant dans l'univers ?",
                ["Oxygene", "Carbone", "Hydrogene"],
                2
            )
        ]
        return questions

    def lancer_quiz(self):
        # Melanger l'ordre des questions
        random.shuffle(self.questions)
        
        for i, question in enumerate(self.questions, 1):
            print(f"\nQuestion {i}/10:")
            question.afficher_question()
            
            # Demander et verifier la reponse
            while True:
                reponse = input("\nVotre reponse (a/b/c) : ")
                if reponse.lower() in ['a', 'b', 'c']:
                    break
                print("Veuillez repondre par a, b ou c.")
            
            # Verifier la reponse et mettre a jour le score
            if question.verifier_reponse(reponse):
                print("Correct !")
                self.score += 1
            else:
                print("Incorrect.")

    def afficher_resultats(self):
        print(f"\nVotre score final : {self.score}/10")
        print("\nCorrige :")
        for question in self.questions:
            question.afficher_correction()