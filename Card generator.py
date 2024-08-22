import random

def generate_visa_number():
    # Replace with a list of valid Visa BINs
    visa_bins = ["471391", "447816", "424145"]

    # Choose a random BIN
    bin_number = random.choice(visa_bins)

    # Generate a random account identifier
    account_number = str(random.randint(10000000, 99999999))

    # Calculate the check digit
    check_sum = 0
    doubled = False
    for digit in reversed(bin_number + account_number):
        digit = int(digit)
        if doubled:
            digit *= 2
            if digit > 9:
                digit -= 9
        check_sum += digit
        doubled = not doubled

    check_digit = (10 - (check_sum % 10)) % 10

    return bin_number + account_number + str(check_digit)

def is_valid_card(card_number):
    sum = 0
    doubled = False
    for digit in reversed(card_number):
        digit = int(digit)
        if doubled:
            digit *= 2
            if digit > 9:
                digit -= 9
        sum += digit
        doubled = not doubled
    return sum % 10 == 0

# Generate a Visa card number
card_number = generate_visa_number()

# Check if the generated card number is valid
def generate_valid_cards(num_cards):
    valid_cards = []
    while len(valid_cards) < num_cards:
        card_number = generate_visa_number()
        if is_valid_card(card_number):
            valid_cards.append(card_number)
    return valid_cards

# Generate valid card numbers
valid_cards = generate_valid_cards(200)
for card in valid_cards:
    print(card)