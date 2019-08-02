import getpass
import os
import time

class Hangman(object):
    def __init__(self):
        self.letters = []
        self.failed = 0
        self.guess = ""
        self.tried = 0
        self.trials = 0
        self.word =''
        self.gui = ['   _____   ',
                    '   |   |   ',
                    '   |       ',
                    '   |       ',
                    '   |       ',
                    '   |       ',
                    ' [___]     ']

    def show(self):
        for i in self.gui:
            print(i)

    def lost(self, nr):
        if nr == 0:
            self.show()
        elif nr == 1:
            self.gui[2] = '   |   O  '
            self.show()
        elif nr == 2:
            self.gui[2] = '   |   O  '
            self.gui[3] = '   |  /|\\  '
            self.show()
        elif nr == 3:
            self.gui[2] = '   |   O  '
            self.gui[3] = '   |  /|\  '
            self.gui[4] = '   |   |   '
            self.show()
        elif nr == 4:
            self.gui[2] = '   |   O   '
            self.gui[3] = '   |  /|\  '
            self.gui[4] = '   |   |   '
            self.gui[5] = '   |  / \  '
            self.show()

    def infopage(self):
        os.system('cls')
        print('--------------> THE HANGMAN GAME ! <--------------')
        print('**************************************************')
        print(f'Failed {self.failed}')
        print()
        self.lost(self.failed)
        print()
        print(f"The length of the word is {len(self.word)} letters.")

        print(f'Guess the word letters! Try nr {self.tried}/{self.trials}')
        print()
        print(f'TRIED ALREADY:  [{" ".join(self.letters)}]\n')

    def start(self):
        i=0
        os.system('cls')
        self.word = getpass.getpass('Enter the guessed word >> ')
        letterlist = self.word
        make = letterlist.maketrans(letterlist, len(letterlist) * "*")
        trans = letterlist.translate(make)
        self.trials =  len(self.word) + 3
        finished = False
        while self.tried < self.trials and self.failed < 4 and finished == False:
            self.infopage()
            trans = letterlist.translate(make)
            print(trans)
            if trans == self.word:
                for item in "YOU WON!":
                    i += 2
                    time.sleep(0.15)
                    print(end=i*" ")
                    print(item)
                print()
                finished = True
                break
            self.guess = input('Guess >> ')
            while len(self.guess) != 1:
                print('You have to insert 1 letter only! Try again!')
                self.guess = input('Guess >> ')
            if ord(self.guess) in make.keys() and self.guess not in self.letters:
                print('Got it')
                del make[ord(self.guess)]
            elif self.guess in self.letters:
                print('This letter was already guessed')
            elif self.guess not in self.letters and self.guess not in self.word:
                self.failed += 1
            self.letters.append(self.guess)
            self.tried += 1

            if self.failed == 4 or self.tried == self.trials:
                self.infopage()
                finished = True
                if self.failed == 4:
                    print("\nYou failed too many times!\n")
                elif self.tried == 8:
                    print("\nYou tried too many times!\n")
                for item in "GAME IS OVER":
                    i += 2
                    time.sleep(0.15)
                    print(end=i*" ")
                    print(item)
                break
        return

hangman = Hangman()
hangman.start()

