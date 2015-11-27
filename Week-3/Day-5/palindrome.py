import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def palindrome_generator(my_string):
    if my_string == '':
        return "YOU GAVE AN EMPTY STRING. TRY AGAIN"
    else:
        return my_string + my_string[::-1]

def palindrome_checker(string):
    string = string.lower()
    return (string == string[::-1]) and (len(string) >= 3)

def palindrome_listing(my_string):
    wordlist = [x for x in my_string.split() if len(x) >= 3]
    palindromel = []
    for word in wordlist:
        length = len(word)
        for start in range(length-1):
            for end in range(start+1, length):
                if palindrome_checker(word[start:end+1]):
                    palindromel.append(word[start:end+1])
    return palindromel

def menu():
    print('\n')
    choose = input("Choose which functions you'd like to use (A or B): ").lower()
    if choose == 'a':
        print('\nYour generated palindrome is: '+ palindrome_generator(input("\nGive a string to generate a palindrome: ")))
    elif choose == 'b':
        palindromel = palindrome_listing(input("\nGive a long string to generate a palindrome list: "))
        if palindromel != []:
            palindromel.sort(key=len, reverse=False)
            print('\nHere is your palindrome list:')
            for word in palindromel:
                print(word)
        else:
            print("YOU GAVE AN EMPTY STRING: TRY AGAIN")
    else:
        print("WRONG OPTION. SORRY, TRY AGAIN!")

def main():
    cls()
    print('\n','*'*80, '\n','*'*30,' Palindrome-Izer ','*'*30, '\n','*'*80)
    print('HY I HAVE TWO FUNCTIONS. \
    \nA: I CAN GENERATE A PALINDROME FROM ANY STRING YOU WANT.\nB: I CAN GIVE YOU A LIST OF PALINDROMES FROM ANY STRING YOU PUT IN,\n')
    chooser = input("DO YOU WANT TO TRY IT? Y/N: ").lower()
    while chooser != 'n':
        if chooser == 'y':
            menu()
        else:
            print("SORRY I DON'T UNDERSTAND")
        chooser = input("\nDO YOU WANT TO TRY AGAIN? Y/N: ").lower()
    if chooser == 'n':
        print("Goodbye! Have a nice day!")

main()
