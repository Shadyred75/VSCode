from PandasToList import PandasToList
import random

p = PandasToList()
list_tarot_card = p.tarot_deck("C:/Users/dsmit/Documents/VSCode/Python/TarotReading/lessoncards.csv")

while True:

    try:

        user_input = int(input(
            "\nDo you want one card or three?\n"
            "1: One Card\n"
            "3: Three Cards\n"
            "0: Exit\n"
            "Enter your choice: "))
        if user_input == 1:
            # if user input is equal to 1 then display one card
            list_tarot_random = random.sample(list_tarot_card, 1)
            print(list_tarot_random)

        elif user_input == 3:
            # if user input is equal to 3 then display three cards
            list_tarot_random = random.sample(list_tarot_random, 3)
            print(list_tarot_random)
        
        elif user_input == 0:
            # if user input is equal to 0 then exit the program
            break

    except ValueError:
        # value error exception for other inputs
        print("ERROR: Please enter a valid option.")