def sol1():
    while True:
        target = int(input())

        add = 0
        price = 1
        days = 1

        add += 1
        while days < target:
            for i in range(add):
                days += 1
                price += 1
                if days >= target:
                    break

            if days >= target:
                break

            days += 1
            price -= 1
            add += 1

            if days >= target:
                break

        print(price)


def calc(target):
    if target == 1:
        return 1

    if target == 2:
        return 2

    days = 2
    down_days = 0
    while days < target:
        down_days += 1
        days += (down_days + 1)

    return target - down_days


def sol2():
    while True:
        target = int(input())
        print(int(target))


sol2()
