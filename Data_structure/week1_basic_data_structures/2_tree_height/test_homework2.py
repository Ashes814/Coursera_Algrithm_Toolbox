import os
from tree_height import compute_height

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
        n = int(input_test.split('\n')[0])
        parents_s = input_test.split('\n')[1].split()
        parents = []
        for p in parents_s:
            parents.append(int(p))


    with open(test_path + file + '.a', 'r') as f2:
        answer = f2.read()


    try:
        my_answer = compute_height(n, parents)


        assert str(my_answer) == answer.strip()
    except:
        print('test {} Fail! , answer {} my_answer {}'.format(file, answer, my_answer))

    # else:
    #     print('test {} Success'.format(file))



