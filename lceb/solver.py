import itertools

global best_path, best


def runit(game: dict):
    global best_path, best
    best_path = []
    best = 0

    solve(game['numbers'], game['target'], [])
    return {'operations': best_path, 'best': best}


def solve(numbers: list, target, solution: list):
    global best_path, best
    if len(numbers) > 1:
        for x, y in set(itertools.combinations(numbers, 2)):
            x, y = (x, y) if x >= y else (y, x)
            for op, result in operator(x, y):
                current_state = f'{x} {op} {y} = {result}'
                if result == target:
                    best_path = solution + [current_state]
                    best = result
                elif abs(result - target) < abs(best - target):
                    best_path = solution + [current_state]
                    best = result
                else:
                    sub_numbers = numbers + [result]
                    sub_numbers.remove(x)
                    sub_numbers.remove(y)
                    solve(sub_numbers, target, solution + [current_state])


def operator(x, y):
    yield '+', x + y
    if x > y:
        yield '-', x - y
    if y > 1:
        yield '*', x * y
        if x % y == 0 and y > 1:
            yield '/', int(x / y)
