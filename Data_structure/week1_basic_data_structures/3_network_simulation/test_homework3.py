import os


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
        input_test = f1.read().strip()
        line1 = input_test.split('\n')[0]
        buffer_size, n_requests = int(line1.split(' ')[0]), int(line1.split(' ')[1])
        requests_raw = input_test.split('\n')[1:]
        requests = [[] for raw in range(n_requests)]
        for i, r in enumerate(requests_raw):
            arrive_time = int(r.split(' ')[0])
            process_time = int(r.split(' ')[1])
            requests[i].append(arrive_time)
            requests[i].append(process_time)



    with open(test_path + file + '.a', 'r') as f2:
         answer = f2.read().strip()

    #
    # try:
    #     my_answer = compute_height(n, parents)
    #
    #
    #     assert str(my_answer) == answer.strip()
    # except:
    #     print('test {} Fail! , answer {} my_answer {}'.format(file, answer, my_answer))
    #
    # # else:
    # #     print('test {} Success'.format(file))



