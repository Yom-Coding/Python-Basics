import random 

letters_lower = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a" "s", "d", "f", "g", "h", "j", "k", "l", 
                 "z", "x", "c", "v", "b", "n", "m"]

letters_upper = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A" "S", "D", "F", "G`", "H", "J", "K", "L", 
                 "Z", "X", "C", "V", "B", "N", "M"]

numbers = random.randint(10, 999)

special_characters = ["!", "@", "£", "$", "%", "^", "&", "*", "(", ")", "_" "-", "=", "+", "{", "}", ":", ";"]

a = random.choice(letters_lower)

b = random.choice(letters_upper)

c = random.choice(letters_lower)

d = random.choice(letters_upper)

e = random.choice(letters_lower)

f = random.choice(special_characters)

print(f"The Generated Password For You Is: {a}{b}{c}{d}{e}{numbers}{f}")