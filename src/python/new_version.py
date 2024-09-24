src = '8'
key = 2 + 62 + 62

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

enc = alphabet[(alphabet.index(src) + key) % len(alphabet)]
print(f"from {src} with key {key} find {enc}")

assert enc == 'a'

i = alphabet.index(enc) - key
while -i >= len(alphabet):
    i += len(alphabet)
dec = alphabet[i]
print(f"from {enc} with key {-key} find {dec}")

assert dec == src
