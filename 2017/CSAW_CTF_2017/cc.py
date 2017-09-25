#!/usr/bin/python
# -*- coding: utf-8 -*-
# by ..:: crazyjunkie ::.. 2014
# If you need a Good Wordlist ====> http://uploaded.net/folder/j7gmyz

"""
gencc: A simple program to generate credit card numbers that pass the
MOD 10 check (Luhn formula).
Usefull for testing e-commerce sites during development.

by ..:: crazyjunkie ::.. 2014
"""

from random import Random
import copy
import socket

visaPrefixList = [
    ['4', '5', '3', '9'],
    ['4', '5', '5', '6'],
    ['4', '9', '1', '6'],
    ['4', '5', '3', '2'],
    ['4', '9', '2', '9'],
    ['4', '0', '2', '4', '0', '0', '7', '1'],
    ['4', '4', '8', '6'],
    ['4', '7', '1', '6'],
    ['4']]

mastercardPrefixList = [
    ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]

amexPrefixList = [['3', '4'], ['3', '7']]

discoverPrefixList = [['6', '0', '1', '1']]

dinersPrefixList = [
    ['3', '0', '0'],
    ['3', '0', '1'],
    ['3', '0', '2'],
    ['3', '0', '3'],
    ['3', '6'],
    ['3', '8']]

enRoutePrefixList = [['2', '0', '1', '4'], ['2', '1', '4', '9']]

jcbPrefixList = [['3', '5']]

voyagerPrefixList = [['8', '6', '9', '9']]


def completed_number(prefix, length):
    """
    'prefix' is the start of the CC number as a string, any number of digits.
    'length' is the length of the CC number to generate. Typically 13 or 16
    """

    ccnumber = prefix

    # generate digits

    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)

    # Calculate sum

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):

            sum += int(reversedCCnumber[pos + 1])

        pos += 2

    # Calculate check digit

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append(str(checkdigit))

    return ''.join(ccnumber)


def credit_card_number(rnd, prefixList, length):
    ccnumber = copy.copy(rnd.choice(prefixList))
    return completed_number(ccnumber, length)


def output(title, numbers):

    result = []
    result.append(title)
    result.append('-' * len(title))
    result.append('\n'.join(numbers))
    result.append('')

    return '\n'.join(result)

#
# Main
#

generator = Random()
generator.seed()        # Seed from current time

# print("credit card generator by ..:: crazyjunkie ::..\n")

# mastercard = credit_card_number(generator, mastercardPrefixList, 16, 10)
# print(output("Mastercard", mastercard))

# visa16 = credit_card_number(generator, visaPrefixList, 16, 10)
# print(output("VISA 16 digit", visa16))

# visa13 = credit_card_number(generator, visaPrefixList, 13, 5)
# print(output("VISA 13 digit", visa13))

# amex = credit_card_number(generator, amexPrefixList, 15, 5)
# print(output("American Express", amex))

# # Minor cards

# discover = credit_card_number(generator, discoverPrefixList, 16, 3)
# print(output("Discover", discover))

# diners = credit_card_number(generator, dinersPrefixList, 14, 3)
# print(output("Diners Club / Carte Blanche", diners))

# enRoute = credit_card_number(generator, enRoutePrefixList, 15, 3)
# print(output("enRoute", enRoute))

# jcb = credit_card_number(generator, jcbPrefixList, 16, 3)
# print(output("JCB", jcb))

# voyager = credit_card_number(generator, voyagerPrefixList, 15, 3)
# print(output("Voyager", voyager))

# print credit_card_number(generator, discoverPrefixList, 16)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('misc.chal.csaw.io', 8308))

client.send("")

resp = client.recv(2048)

while 1:
    print resp
    if "American" in resp:
        client.send(credit_card_number(generator, amexPrefixList, 15) + "\n")
    if "MasterCard" in resp:
        client.send(credit_card_number(generator, mastercardPrefixList, 16) + "\n")
    if "Discover" in resp:
        client.send(credit_card_number(generator, discoverPrefixList, 16) + "\n")
    if "Visa" in resp:
        client.send(credit_card_number(generator, visaPrefixList, 16) + "\n")
    if "card that starts with" in resp:
        needed = resp.split(" ")
        print (needed[len(needed) - 1]).trim()

    resp = client.recv(2048)