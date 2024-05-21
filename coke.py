def main():
    amount = 50
    print_message(amount, "due")
    while amount >= 0:
        coin = get_coin()
        amount = calculate_amount(amount, coin)
        if amount > 0:
            print_message(amount, "due")
        elif amount == 0:
            print_message(amount, "owed")
            break
        else:
            print_message(-amount, "owed")
            break


def get_coin():
    # get coin input from user and return it
    coin = int(input("Insert Coin: "))
    return coin


def calculate_amount(amount, coin):
    # calculate new amount due or change owed and return it
    valid_coins = [5, 10, 25]
    if coin in valid_coins:
        if coin > amount:
            change = coin - amount
            return -change
        else:
            amount = amount - coin
            return amount
    else:
        return amount


def print_message(amount, type):
    if type == "due":
        print("Amount Due: " + str(amount))
    else:
        print("Change Owed: " + str(amount))


main()