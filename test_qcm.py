import unittest
from question import Question
from qcm import QCM

class TestQuestion(unittest.TestCase):
    def setUp(self):
        self.question = Question(
            "Test question?",
            ["Réponse 1", "Réponse 2", "Réponse 3"],
            1
        )

    def test_verifier_reponse_correcte(self):
        self.assertTrue(self.question.verifier_reponse('b'))
        self.assertTrue(self.question.verifier_reponse('B'))

    def test_verifier_reponse_incorrecte(self):
        self.assertFalse(self.question.verifier_reponse('a'))
        self.assertFalse(self.question.verifier_reponse('c'))

class TestQCM(unittest.TestCase):
    def setUp(self):
        self.qcm = QCM()

    def test_creation_questions(self):
        self.assertEqual(len(self.qcm.questions), 10)
        self.assertIsInstance(self.qcm.questions[0], Question)

    def test_score_initial(self):
        self.assertEqual(self.qcm.score, 0)

if __name__ == '__main__':
    unittest.main()