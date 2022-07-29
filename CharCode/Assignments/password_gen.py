# this generaes a random password

def password_gen(length):
    import random
    import string
    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters
                                  + string.digits
                                  + string.punctuation)
    return password


# this generates a random passphrase
def passphrase_gen(length):
    import random
    import os
    with open(os.path.join(os.path.dirname(__file__), 'words.txt'), 'r') as f:
        words = f.read().splitlines()
    passphrase = ''
    for i in range(length):
        passphrase += random.choice(words)
        if not i % 2:
            passphrase += ''
            passphrase = passphrase + words[i].upper()
        else:
            passphrase = passphrase + words[i].lower()
    return passphrase


def passphrase_gen2(length):
    import random
    import os
    import string
    with open(os.path.join(os.path.dirname(__file__), 'words.txt'), 'r') as f:
        words = f.read().splitlines()
    passphrase = ''
    for i in range(length):
        passphrase += random.choice(words) + random.choice(string.punctuation + string.digits)
        if not i % 2:
            passphrase += ''
            passphrase = passphrase + words[i].upper()
        else:
            passphrase = passphrase + words[i].lower()
    return passphrase


# prints five passwords
for i in range(5):
    import random

    print("Password: "+password_gen(random.randint(10, 20)))
    print("Passphrase: "+passphrase_gen(random.randint(3, 10)))
    print("Phrase w/ Digits, Punctuation: "+passphrase_gen2(random.randint(3, 10)))
    print('\n')

# print("-----------------------------------------------------\n")
#
# # prints five passphrases
# for i in range(5):
#     import random
#
#     print(passphrase_gen(random.randint(10, 20)))
#
# print("-----------------------------------------------------\n")
#
# # prints five passphrases
# for i in range(3):
#     import random
#
#     print(passphrase_gen2(random.randint(3, 10)))
