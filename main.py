def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    text = "How many vowels and consonants are in this sentence?"
    vowel_counter = len([c for c in text if c in vowels])
    consonant_counter = len([c for c in text if c not in vowels])
    print(f'The number of vowels in the string is: {vowel_counter}')
    print(f'The number of consonants in the string is: {consonant_counter}')

if __name__ == "__main__":
    main()
