import os
import unittest


class HomeworkTest(unittest.TestCase):
    test_path = 'tests/'
    for root, dirs, files in os.walk(test_path):
        test_files = []
        answer_files = []
        for file in files:
            if file[-2:] != '.a':
                test_files.append(file)
            else:
                answer_files.append(file)

    for file in test_files:
        with open(test_path + file, 'r') as f1:
            input_test = f1.read()
        with open(test_path + file + '.a', 'r') as f2:
            answer = f2.read()

        def test_function(self, input_test, answer):
            self.input_test = input_test
            self.answer = answer
            my_answer = answer
            assert self.answer == answer



