# key space = 26
def encrypt(msg, a, b, k):
    """ encrypts message according to the formula l' = a * l + b mod k """
    encrypted_message = ""
    for letter in msg:
        if letter == " ":
            encrypted_message += " "
        else:
            encrypted_letter_index = (a * (ord(letter) - ord('a')) + b) % k
            encrypted_message += chr(encrypted_letter_index + ord('a'))
    return encrypted_message

def inverses(k):
    """ calculates the inverses of each number in k space """
    inverse_numbers = dict()
    for i in range(k):
        if i in inverse_numbers:
            continue
        for j in range(i, k):
            if (i * j) % k == 1:
                inverse_numbers[i] = j
                inverse_numbers[j] = i
                break
    return inverse_numbers

def decrypt(msg, a, b, k):
    """ decrypts message according to the formula l = a^-1 (l' - b) mod k """
    decrypted_message = ""
    inverse_a = inverses(k)[a]
    for letter in msg:
        if letter == " ":
            decrypted_message += " "
        else:
            encrypted_letter_index = (inverse_a * ((ord(letter) - ord('a')) - b)) % k
            decrypted_message += chr(encrypted_letter_index + ord('a'))
    return decrypted_message

action = input("(e)ncrypt / (d)ecrypt = ").lower()
assert action != "", "empty action string"
assert action[0] == "d" or action[0] == "e", "invalid action string"
message = input("message = ").lower()
assert message != "", "empty message string"
assert message.replace(" ","").isalpha(), "invalid message string"
if action[0] == "d":
    decrypted_message = decrypt(message, 5, 7, 26)
    print("decrypted message = "+decrypted_message)
elif action[0] == "e":
    encrypted_message = encrypt(message, 5, 7, 26)
    print("encrypted message = "+encrypted_message)
