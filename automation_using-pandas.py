import  pandas as pd

epl_table = pd.read_html("https://www.premierleague.com/tables")

print(epl_table[0]) # Prints the first table on the page
