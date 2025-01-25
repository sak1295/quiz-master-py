# -*- coding: utf-8 -*-
from qcm import QCM

def main():
    print("Bienvenue dans le QCM !")
    print("Pour chaque question, choisissez la reponse en tapant a, b ou c.")
    
    quiz = QCM()
    quiz.lancer_quiz()
    quiz.afficher_resultats()

if __name__ == "__main__":
    main()