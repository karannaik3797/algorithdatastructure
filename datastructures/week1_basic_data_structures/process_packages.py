# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrival_time", "process_time"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        while len(self.finish_time)>0 and self.finish_time[0]<=request.arrival_time:
            self.finish_time.pop(0)
        if len(self.finish_time) < self.size:
            if len(self.finish_time) == 0:
                self.finish_time.append(request.arrival_time + request.process_time)
                return Response(True, request.arrival_time)
            else:
                start_time = request.arrival_time
                if self.finish_time[-1] > start_time:
                    start_time = self.finish_time[-1]
                elif self.finish_time[-1] == start_time:
                    start_time = self.finish_time[-1] + 1
                self.finish_time.append(start_time + request.process_time)
                return Response(True, start_time)
        else:
            return Response(False, -1)   



def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if response.was_dropped else -1)


if __name__ == "__main__":
    main()
