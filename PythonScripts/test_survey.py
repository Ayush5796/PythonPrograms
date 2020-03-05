import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test the Class AnonymousSurvey"""
    def setUp(self):
        """Create a survey and set of responses for test methods"""
        question = "Which language did you first learned??"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Sanskrit']


    def test_store_single_response(self):
        """Test wether the function can store the single value"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)


    def test_store_three_response(self):
        """Test wether the function can store the three value"""
        for res in self.responses:
            self.my_survey.store_response(res)
        for res in self.responses:
            self.assertIn(res, self.my_survey.responses)

unittest.main()