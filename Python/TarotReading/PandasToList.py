import pandas
# imports the pandas module that is used to parse our csv file
 
class PandasToList:
    # The PandasToList class creates a list out of our csv file
    def tarot_deck(self, deck_file):
        df_tarot_card = pandas.read_csv(deck_file)
        list_card = df_tarot_card["CARD"].values
        list_description = df_tarot_card["DESCRIPTION"].values
        list_tarot_card = [[card, desc] for card, desc in zip(list_card, list_description)]
        return list_tarot_card

