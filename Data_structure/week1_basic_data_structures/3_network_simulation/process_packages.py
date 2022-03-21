# python3
import os

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
        if self.finish_time == []:
            self.finish_time.append(request[0] + request[1])
            return Response(False, request[0])
        if request[0] >= self.finish_time[-1]:
            self.finish_time = []
        elif request[0] < self.finish_time[0]:
            pass
        else:
            for finish in self.finish_time:
                if request[0] >= finish:
                    self.finish_time.pop(0)
        if self.finish_time == []:
            self.finish_time.append(request[0])
            return Response(False, request[0])
        else:
            self.finish_time.append(self.finish_time[-1] + request[1])
            if self.size < len(self.finish_time):
                self.finish_time.pop()
                return Response(True, -1)
            else:
                return Response(False, self.finish_time[-2])


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():


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
        print(file)
        with open(test_path + file, 'r') as f1:
            input_test = f1.read().strip()
            line1 = input_test.split('\n')[0]
            buffer_size, n_requests = int(line1.split(' ')[0]), int(line1.split(' ')[1])  # map(int, input().split())
            requests_raw = input_test.split('\n')[1:]
            requests_test = [[] for raw in range(n_requests)]
            for i, r in enumerate(requests_raw):
                arrive_time = int(r.split(' ')[0])
                process_time = int(r.split(' ')[1])
                requests_test[i].append(arrive_time)
                requests_test[i].append(process_time)
            # buffer_size, n_requests = int(line1.split(' ')[0]), int(line1.split(' ')[1]) # map(int, input().split())
            requests = []
            for _ in range(n_requests):
                arrived_at, time_to_process =requests_test[_][0], requests_test[_][1] #map(int, input().split())
                requests.append(Request(arrived_at, time_to_process))

            buffer = Buffer(buffer_size)
            responses = process_requests(requests, buffer)
            with open(test_path + file + '.a', 'r') as f:
                answer = f.read().strip().split('\n')

            for i, response in enumerate(responses):
                if not response.was_dropped:
                    my_answer = response.started_at
                else:
                    my_answer = -1
                # print(response.started_at if not response.was_dropped else -1, end='|')
                # print(answer[i])
                try:
                    assert str(answer[i]) == str(my_answer)
                except:
                    print(file, my_answer, answer[i], i)


if __name__ == "__main__":
    main()
