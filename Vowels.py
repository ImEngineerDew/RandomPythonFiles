def vowels ():
    words = input("Please write your word: ").lower()
    vowels_list = ['a','e','i','o','u']

    counter = 0

    for i in vowels_list:
        repeats =   words.count(i)
        print("The vowel {} is {} in the word: {}".format(i,repeats,words))


if __name__ == '__main__':
    vowels()

