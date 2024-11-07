import itertools

with open('wordbank.txt', 'r', encoding='latin-1') as file:
    validWords = set()
    for word in file:
        if 3 <= len(word) <= 6:
            validWords.add(word.strip().lower())

def solveAnagram(letters):
    answers = set()
    ordered_answers = []
    
    for length in range(len(letters), 2, -1):
        for combo in itertools.permutations(letters, length):
            word = ''.join(combo).lower()
            if word in validWords:
                currentLen = len(answers)
                answers.add(word)
                if currentLen == len(answers):
                    ordered_answers.append(word)
        
    return ordered_answers

if __name__ == "__main__":
    print("\nWelcome to the Anagrams Solver!")
    print("Enter '-q' to quit the program")

    while True:
        gamepigeon_max_points = 0
        letters = input('\nEnter your letters here (min. 3): ').strip().lower()

        if letters == '-q':
            print('\nThanks for playing, goodybye!\n')
            break
        if not letters.isalpha():
            print('\nPlease enter only letters.')
            continue

        answers = solveAnagram(letters)

        if not answers:
            print('\nYour letters do not make any valid 3 to 6 letter words.')  
        else: 
            print(f"All valid words using '{letters}':")
            for word in answers:
                print('•', word)
            print(f"{len(answers)} possible words found")

            print(len(validWords))

"""perms = itertools.permutations('eramly', 5)
output = []
for perm in perms:
    word = ''.join(perm)
    output.append(word)
print(output)
print(True if 'realm' in validWords else False)"""