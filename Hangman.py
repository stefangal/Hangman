import random
import os

s = ["""""","""
         000
        00000
         000 """,
"""
 0 0 0 0 0 0 0 0 0 0
 0     0 0 0 0     0""",
"""      
       0 0 0 0      
       0 0 0 0 """,
"""
        0 0 0 
        0   0
       0    0
     000     000
"""]

with open('hangman_words.txt', 'r') as file:
    selection = []
    for word in file.readlines():
        selection.append(word)
selected = str(random.choice(selection)).lower().strip()

counter, idx  = 0, 0
hidden = selected[1:-1]

trans_tab = selected.maketrans(hidden, len(hidden)*'*')
hidden_word = hidden.translate(trans_tab)
figure, used_words = [], []

while True:
    os.system('cls')
    print(f" You have {idx}/4 tries remaining")
    print(f'Used words and not hit: {used_words}')
    print(selected[0] + hidden_word + selected[-1])
    for i in range(1,idx+1):
        print(s[i],'\n')
    input_letter = input("Guess a letter >> ")

    if ord(input_letter) in trans_tab.keys():
        print(input_letter, 'Got it right this time !!! ')
        del trans_tab[ord(input_letter)]

        hidden_word = hidden.translate(trans_tab)
        print(selected[0] + hidden_word + selected[-1])    
    else:
        idx += 1
        used_words.append(input_letter)
    if bool(trans_tab) == False and idx <= 4:
        os.system('cls')
        for _ in range(5):
            print('YOU WON !!!')
        print(f'It was the word: {selected}')
        for i in range(1,idx+1):
            print(s[i],'\n')
        break
    elif bool(trans_tab) and idx == 4:
        os.system('cls')
        print(selected[0] + hidden_word + selected[-1],'\n')
        for _ in range(5):
            print('YOU LOST !!!') 
        print(f'It was the word: {selected}')        
        for i in range(1,idx+1):
            print(s[i],'\n')
        break
