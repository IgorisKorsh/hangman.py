import viselica as v
import random as r
"""HANGMAN GAME"""

try_limit = 8
tries = 0

secret_words = [
    "Volkswagen", 'Honda', 'Toyota', 'Chevrolet',
    'Jeep', 'Ford', 'Audi', 'BMW', 'Maybach', 'Fiat',
    'Suzuki', 'Subaru', 'Renault', 'KIA', 'Lexus',
    'Bentley', 'AstonMartin', 'AvtoVAZ', 'Bugatti',
    'Cadillac', 'Chrysler', 'Citroen', 'Dacia',
    'Daihatsu', 'Dodge', 'Ferrari', 'GAZ', 'MAN',
    'Hyundai', 'Infinity', 'Lada', 'Lamborghini',
    'Maserati', 'Mazda', 'McLaren', 'MercedesBenz',
    'Mitsubishi', 'Nissan', 'Opel', 'Pagani', 'Peugeot',
    'Pontiac', 'Porsche', 'RollsRoyce', 'Skoda',
    'Tesla', 'Volvo'
]

secret_word = secret_words[r.randint(0, len(secret_words) - 1)]
guess = list('_' * len(secret_word))


def decorator(fun):
    def wrapper(txt):
        print('\n' + '-' * len(txt))
        print(txt)
        print('-' * len(txt) + '\n')
    return wrapper


@decorator
def print_text(txt):
    pass


def print_dead_man(trie):
    if trie == 1:
        print(v.d)
    if trie == 2:
        print(v.de)
    if trie == 3:
        print(v.dea)
    if trie == 4:
        print(v.dead)
    if trie == 5:
        print(v.dead_)
    if trie == 6:
        print(v.dead_m)
    if trie == 7:
        print(v.dead_ma)
    if trie == 8:
        print(v.dead_man)


print_text('Hello! Let\'s play a hangman game')

print('THE THEME IS "CARS"')
print('THE WORD IS ' + " ".join(guess))

while tries != try_limit:
    letter = input("Enter a letter: ")
    if letter.lower() in secret_word.lower():
        for i in range(len(secret_word)):
            if secret_word[i].lower() == letter.lower():
                guess[i] = letter
    else:
        tries += 1
        print_dead_man(tries)
        print_text(str(try_limit-tries) + ' tries remains')
    if "_" not in guess:
        print_text("YOU WIN!!!")
        print("The word is \'" + secret_word + '\'')
        break
    print(" ".join(guess))


if tries == try_limit:
    print_text('LOOSER')
    print_text('Right answer is ' + secret_word)
