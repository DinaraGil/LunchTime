from read_gs import Data
from read_card import Read_card

card_id = Read_card.card_id
df = Data.df

student = df[df['id'] == card_id]

print(df)

print(student['name'], student['lunch type'])