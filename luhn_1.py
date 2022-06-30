def luhn_check(card_no):
    digits = len(card_no)
    sum = 0
    second = False

    for i in range(digits -1, -1, -1):
        digit = ord(card_no[i]) - ord('0')

        if (second == True):
            digit = digit * 2
        sum += digit // 10
        sum += digit % 10

        second = not second

    if (sum % 10 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    print("Enter a card number: ")
    card_nr = input()
    while len(card_nr) == 0:
        card_nr = input()

    if (luhn_check(card_nr)):
        print("This is a valid card number")
    else:
        print("This is not a valid card number")
