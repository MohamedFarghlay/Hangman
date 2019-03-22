import string
import random

#load the words 
def load_file():
    word_list=open("words.txt",'r')  #open the file in read mod
    content_of_file=word_list.read()
    words=content_of_file.split()
    #print("Loading word list from file...\n")
    #print(len(words),"words loades")
    return words

#make the computer select a random word from the given file (words.txt)
def select_random_word():
    words=load_file()
    random_word=random.choice(words) #this method choise a random value from a given set
    return random_word

#------------------------------------------------------------------
# function to determind if the word guessed or not
def is_word_guessed(secret_word , guessed_word):

    c=0 
    #convert to set to remove duplicated characters
    guessed_word=set(guessed_word)
    secret_word=set(secret_word)

    for ch in guessed_word:
        if ch in secret_word:
            c=c+1
    if c==len(secret_word):
        return True
    else:
        return False

#--------------------------------------------------------------#
#function to get the guessed word from the user and determind the 
#character the user has guessed and replace the remaining of the secret word wiht (_ )
def get_guessed_word(secret_word,guessed_word):
    
    remain_words=secret_word   #at the first the remain will be equal to the secret word
    secret_word=set(secret_word) #convert it to set to remove duplicated characters
    guessed_word=set(guessed_word) 
    for ch in guessed_word:   
        if ch in secret_word: 
            secret_word.remove (ch)   #remove the character from the secrect if it found

    #replace the remaining words in the secret words to (_ )  and return the remain words
    for ch in secret_word:
        remain_words= remain_words.replace(ch,'_ ')
    return remain_words

#-----------------------------------------#
#function to get available letters , it take the guessed letters by the user
# and return a string of all alphabet character removed from it the guessed letters
def get_available_letters(guessed_letters):

    alphabet_letters=list(string.ascii_lowercase) #fill it with englis lowercase letters and convert it to list
    
    for ch in guessed_letters:
        if ch in (alphabet_letters):  
            (alphabet_letters).remove(ch)   # remove the guessed letters from the englist letters
            
    return alphabet_letters

#-----------------------------------------
#how to play function is a set of instruction tell the user how to play the hangman game
def how_to_play():
    #TODO
    pass  

#check if it's a letter or not
def IsLetter(letter):
    if letter.isalpha():
        return True
    else:
        return False


#if the letter is woring guess
def worng_guess(secret_word,guessed_word):
    for ch in secret_word:
        if ch in guessed_word: #if found it that's mean it's not wrong guess
            return False
    return True


#===============================================================
#hangman function 

def hangman(secret_word):

    print("i'm selecting a word of length ", len(secret_word))
    print("-------------")

    guesses_left=6 # The user should start with 6 guesses
    guessed_word="" #entered by user
    left_letters=get_available_letters(guessed_word) #letter that not guessed yet
    removed_guessed_letters=""      #letters that already user guessed (to remove it from left letters)
    letters_guessed=""      #letters that guessed until now without (_ )
    letters="" 
    skip=""                 
    while(guesses_left>0):
        # Before each round should display to the user how many guesses
        if(guesses_left!=1):
            print("left ",guesses_left,"guesses only\n")
        else:
            print("Attention!!! only one guess left\n")

        print("Available letters:",left_letters)   #at the first all english letters are available

        guessed_word=input("\nenter guess letter: ") #get the guessed from user

        while((not IsLetter(guessed_word)) or len(guessed_word)>1):  # to sure that letters only the user will given
            if(len(guessed_word)>1):
                guessed_word=input("\nplease enter only one letter: ")
            else:
                guessed_word=input("\nplease enter letters only: ")

        for c in guessed_word: #if letter is already removed
            if c not in left_letters:
                print("'"+c+"'","Sorry Already guessed")
                print("---------------")
                skip="A" #set skip

        if(skip!="A"): # do nothing (skip)
            removed_guessed_letters+=guessed_word   #store the user's guessed words untill now to remove it from available letters

            left_letters=get_available_letters(removed_guessed_letters)#new left letters after remove guessed letters from it

            if(is_word_guessed(secret_word,guessed_word)): # if can guess the word from the first time
                print ("Congratulation!:) You guesssed the word!: ",secret_word)
                return  #exit

            else:
                letters_guessed=guessed_word  #first assign the guessd word to letters that is guessed until now
                letters_guessed+=letters.translate(str.maketrans("","","_ ")) #add the letters the user guesssed until now without (_ )
                
                letters= get_guessed_word(secret_word,letters_guessed) #letters guessed untill now with (_ )

                #if letters is match with the secret word then the use win
                if(is_word_guessed(secret_word, letters)):
                    print ("Congratulation!:) You guesssed the word : ",secret_word)
                    return

                good_bad="Good guess: "  
                #decrement the guesses only if the user enter a wrong guess           
                if(worng_guess(secret_word, guessed_word)):
                    guesses_left=guesses_left-1
                    good_bad="Oops! That letter is not in my word: "
                    if(guesses_left)==0: # if guesess end the the user can't guess the word
                        print(good_bad+letters,"\n")
                        print("-------")
                        print("Sorry you didn't guess the word, \n You lose! :(")
                        print("\nthe word was :",secret_word,"\n")
                        return

                print(good_bad+letters,"\n")  #print the letters to user
                print("-------")
        skip="" #reset skip

#Run the game
def Run(secret_word):
    print("\nWelcome to the HANGMAN game... Enjoy :)")
    print("------------------------------")
    choice=int(input("1-Start the game \n2-How to play \n3-Exit\n"))
    if choice==1:
        hangman(secret_word)
    elif choice==2:
        #How_to_play()
        pass
    else :
        print ("the game will exit")  # to exit from the program
        exit

    

if __name__=="__main__":  # call the main function

    secret_word=select_random_word() #select random word by computer
    Run(secret_word) #Run the hangman game