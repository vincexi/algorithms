# It is a type of substitution cipher in which each letter in the 
# plaintext is replaced by a letter some fixed number of positions 
# down the alphabet. For example, with a left shift of 3, D would 
# be replaced by A, E would become B, and so on. The method is named 
# after Julius Caesar, who used it in his private correspondence.
# https://en.wikipedia.org/wiki/Caesar_cipher

def caesarCipher(string, key):
    if key > 26:
        key = key % 26
    out = ''
    for i in string:
        c = ord(i) + key
        if c > 122:
            c -= 26
        out += chr(c)
    return out