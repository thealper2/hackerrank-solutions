class EvenStream:
    def __init__(self):
        self.current = -2

    def get_next(self):
        self.current += 2
        return self.current

class OddStream:
    def __init__(self):
        self.current = -1

    def get_next(self):
        self.current += 2
        return self.current

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    
    for _ in range(n):
        print(stream.get_next())

queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
