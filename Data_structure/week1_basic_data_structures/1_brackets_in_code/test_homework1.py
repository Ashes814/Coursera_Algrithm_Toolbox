import os
from test_exe import f

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
    my_answer = f(input_test)
    try:
        assert my_answer == answer
    except:
        print("My answer is {}, Correct answer is {}, the number of test {}, the input of test {}".format(
              my_answer, answer, file, input_test)
        )




