import json
import random

# fetching data from json
f = open('word.json')
data = json.load(f)


def get_word():
    """Get random word from word.json"""
    word_list = data['word_list']
    word = random.choice(word_list)
    return word.casefold()


def play(word):
    letters_guessed = []
    word_guessed = []

    word_string = list('_' * len(word))

    word_list = list(word)
    number_of_guesses = 0

    while number_of_guesses < 6:
        index_positions_list = []

        # number of lives remaining
        n_lives = 6 - number_of_guesses
        print(f'You have {n_lives} lives remaining')

        # guessed words appearing
        print(*word_string)
        print(*word_list)
        print()
        guess = input('guess letter or word: ').lower()
        if len(guess) == 1:
            if guess in word_list:
                for position, letter in enumerate(word_list):
                    if letter == guess:
                        index_positions_list.append(position)

                for index_position in index_positions_list:
                    word_string[index_position] = guess

            else:
                if number_of_guesses < 6:
                    print('-' * 10)
                    print('Incorrect')
                    number_of_guesses += 1
                else:
                    break

        elif len(guess) > 1:
            if guess == word:
                print(f'Congratulations, the word was {word}')
                break
            else:
                if number_of_guesses < 6:
                    print(f'Wrong, the word was {word}')
                break


def main():
    ran_word = get_word()
    play(ran_word)

    play_again = input('play again? (y/n): ').casefold()
    while play_again.casefold() == 'y':
        ran_word = get_word()
        play(ran_word)


if __name__ == '__main__':
    main()
