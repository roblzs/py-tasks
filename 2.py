numbers = [5, 10, 15, 20, 25, 50, 20]

printed = []

def check(n):
    for p in printed:
        if n <= p:
            return False

    return True

for n in numbers:
    can_append = check(n)

    if can_append:
        printed.append(n)

for p in printed:
    print(p)