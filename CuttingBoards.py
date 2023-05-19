import sys

def boardCutting(cost_y, cost_x):
    data = {'lst': [], 'flag': [True] * (len(cost_x) + len(cost_y))}
    for i in range(len(cost_y)):
        data['lst'].append(cost_y[i])
        data['flag'][i] = False
    for i in range(len(cost_x)):
        data['lst'].append(cost_x[i])

    sorted_keys = sorted(range(len(data['lst'])), key=lambda k: data['lst'][k], reverse=True)
    sorted_data = {key: data[key] for key in data}

    total_cost = 0
    row = 1
    column = 1

    for key in sorted_keys:
        if not sorted_data['flag'][key]:
            row += 1
            total_cost += sorted_data['lst'][key] * column
        else:
            column += 1
            total_cost += sorted_data['lst'][key] * row

    return total_cost % (10**9 + 7)

def main():
    q = int(input()) 
    results = [] 
    for _ in range(q):
        m, n = map(int, input().split())  
        cost_y = list(map(int, input().split()))  
        cost_x = list(map(int, input().split()))  
        result = boardCutting(cost_y, cost_x)
        results.append(result)
    sys.stdout.write(''.join(str(result) + '\n' for result in results))
    sys.stdout.flush()

if __name__ == '__main__':
    main()