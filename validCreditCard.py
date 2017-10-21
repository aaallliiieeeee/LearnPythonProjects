# reg exps        : taken from http://www.regular-expressions.info/creditcard.html
# luhn validation : taken from wikipedia

import re
import sys

visa = r'^4[0-9]{12}(?:[0-9]{3})?$', "Your Visa Card is Valid"
mastercard = r'^5[1-5][0-9]{14}$', "Your Master Card is Valid"
am_express = r'^3[47][0-9]{13}$', "Your American Express Card is Valid"
diners_club = '^3(?:0[0-5]|[68][0-9])[0-9]{11}$', "Your Diners Club Card is Valid"
discover = r'^6(?:011|5[0-9]{2})[0-9]{12}$', "Your Discover Card is Valid"
jcb = r'^(?:2131|1800|35\d{3})\d{11}$', "Your JCB Card is Valid"

cards = [visa, mastercard, am_express, diners_club, discover, jcb]
invalid_message = "Sorry, this is an Invalid Card Number"
unidentified_message = "Sorry, this is an Unidentified Card Type"


def luhn_checksumisvalid(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10


def is_luhn_valid(card_number):
    return luhn_checksumisvalid(card_number) == 0


def main(card_string):
    card_string = card_string.replace(" ", "")
    card_string = card_string.replace("-", "")
    try:
        card_int = int(card_string)
        if not is_luhn_valid(card_int):
            return invalid_message
        for exp, message in cards:
            mat = re.match(exp, card_string)
            if mat:
                return message
        return unidentified_message
    
    except ValueError:
        return invalid_message


if __name__ == '__main__':
    args = len(sys.argv)
    cardnumer = raw_input("Enter card number : ")
    print main(cardnumer)
