import csv, sqlite3

# Importación de datos de pokemon.csv

con = sqlite3.connect("pokedex.db")
cur = con.cursor()

with open('pokemon.csv','r') as pkfile:
    dr = csv.DictReader(pkfile)
    poke_db = [(i['#'],i['Name'],i['Type 1'],i['Type 2'],i['Total'],i['HP'],i['Attack'],i['Defense'],i['Sp. Atk'],i['Sp. Def'],i['Speed'],i['Generation'],i['Legendary']) for i in dr] 

# pk_file = open("pokemon.csv")
# new_pokemons = csv.reader(pk_file)
cur.executemany("INSERT INTO pokemon (num,name,typeu,typed,total,hp,attack,defense,spatk,spdef,speed,gen,legend) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", poke_db)
con.commit()
con.close()
