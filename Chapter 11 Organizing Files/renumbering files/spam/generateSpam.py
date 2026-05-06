for i in range(1, 10):
    if i not in (3, 5, 7, 8):
        with open(f'spam{str(i).zfill(3)}.txt', 'w') as file:
            pass