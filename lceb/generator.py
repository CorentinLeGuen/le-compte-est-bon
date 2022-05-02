numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100]
target_range = range(100, 999)


def new_game() -> dict:
    """Generate a new game"""
    import random
    return {'numbers': random.sample(numbers, 6), 'target': random.choice(target_range)}
