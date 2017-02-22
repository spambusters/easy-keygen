import random
import string
from sys import stdout


def sum(key):
    """Calcatule a key's ASCII sum

    :param key: The key to be tested (a string)
    :returns: The sum of the key's ASCII values

    """
    char_sum = 0
    for char in key:
        char_sum += ord(char)
    # Make it look cool
    stdout.write(f'{char_sum} | {key}\r')
    stdout.flush()
    return char_sum


def keygen():
    """Find valid keys for ASCII target_sum
    
    By reading the disassembly of a program, we discover that a fictional
        company uses a very simple alogrithm for its licensing keys.
    It adds each char's ASCII value until a sum of 808 is reached.
    In other words, any string whose ASCII values equal 808 will be considered
        a valid key.

    """
    key = ''
    keys = []
    key_count = 0
    target_sum = 808

    while True:
        try:
            max_keys = int(input('How many keys do you want? ')) or 0
            break
        except ValueError:
            print('\n[!] - Please enter an integer')

    while True:
        key += random.choice(string.ascii_letters + string.digits)
        ascii_sum = sum(key)
        if ascii_sum > target_sum:
            # Too big, start over!
            key = ''
        elif ascii_sum == target_sum:
            print(f'Found valid key: {key}')
            keys.append(key)
            key_count += 1

        if key_count >= max_keys:
            with open('keys.txt', 'w') as file:
                for key in keys:
                    file.write(f'{key}\n')
            return print(f'\nFound {max_keys} keys!\n')


if __name__ == '__main__':
    keygen()
