n = int(input())

for n1 in range(1, 9 + 1):
    for n2 in range(1, 9 + 1):
        for n3 in range(1, 9 + 1):
            for n4 in range(1, 9 + 1):
                is_special = n % n4 == 0 and n % n3 == 0 and n % n2 == 0 and n % n1 == 0

                if is_special:
                    print(f'{n1}{n2}{n3}{n4}', end=' ')
