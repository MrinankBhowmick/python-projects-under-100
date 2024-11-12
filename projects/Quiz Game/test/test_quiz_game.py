import unittest
from ..src.gamesystem import QuizGameSystem

class QuizGameTest(unittest.TestCase):
    def setUp(self):
        '''
            Set up the test cases
        '''
        self.system = QuizGameSystem()

    def test_get_questions_items(self):
        '''
            Test the get_questions_items
        '''
        questions = self.system.get_questions()
        self.assertEqual(questions[0]['question'], "Question 1: What is your Favourite programming language?")
        self.assertEqual(questions[0]['answer'], "python")

    def test_start_game_yes(self):
        '''
            Test when the user answered yes it returns true
        '''
        result = self.system.start_game(start="yes")
        self.assertTrue(result)

    def test_start_game_no(self):
        '''
            Test when the user answered no it returns false
        '''
        result = self.system.start_game(start="no")
        self.assertFalse(result)

    def test_show_result_all_correct(self):
        '''
            Test when the answer is all correct, it returns 100%
        '''
        mark = self.system.show_result(3,3)
        self.assertEqual(mark, 100)

    def test_show_result_correct_one(self):
        '''
            Test when one answer is correct, it returns 33%
        '''
        mark = self.system.show_result(1,3)
        self.assertEqual(mark, 33)

if __name__ == "__main__":
    unittest.main()