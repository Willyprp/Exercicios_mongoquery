from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()
#sem evolucoes
pokemons = db.collection.find({ "prev_evolution": {"$exists": False}, "next_evolution": {"$exists": False} })
#possui 2 evolucoes
pokemons = db.collection.find({"next_evolution.1":{"$exists": True}})
#candy count maior que 50
pokemons = collection.find({"candy_count": {"$gt": 50}})
# pesa 50kg
pokemons = collection.find({"weight": "50 kg"})

# media de spawn maior que 100
pokemons = collection.find({"avg_spawns": {"$gt": 100}})
writeAJson(pokemons, "pokemons")
