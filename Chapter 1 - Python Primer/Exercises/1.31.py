"""
Write a Python program that can “make change.” Your program should take
two numbers as input, one that is a monetary amount charged and the other
that is a monetary amount given. It should then return the number of each
kind of bill and coin to give back as change for the difference between the
amount given and the amount charged. The values assigned to the bills and
coins can be based on the monetary system of any current or former government.
Try to design your program so that it returns as few bills and coins as possible.
"""


def make_change(amount_paid, cost):
    denominations = {
        500: 0,
        200: 0,
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0
    }

    change = amount_paid - cost

    for denomination in denominations:
        denominations[denomination] = change // denomination
        change %= denomination

    output = ""

    for key, value in denominations.items():
        if value != 0:
            output += f"Number of {key} rupee denominations: {value}\n"

    return output


if __name__ == '__main__':
    print(make_change(1500, 1291))
