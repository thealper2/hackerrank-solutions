if __name__ == '__main__':
    inputs = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        inputs.append([name, score])
    
    inputs = sorted(inputs, key=lambda x: x[1])
    second_min = list(set([_[1] for _ in inputs]))[1]
    students = [_[0] for _ in inputs if _[1] == second_min]
    print('\n'.join(sorted(students)))