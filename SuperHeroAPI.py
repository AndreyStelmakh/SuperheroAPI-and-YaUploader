import requests

def superhero_id(superhero_name):
    result = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{superhero_name}", timeout=30)

    return int(result.json()["results"][0]["id"])

def superhero_powerstat(superhero_id, stat_name):
    result = requests.get(f"https://superheroapi.com/api/2619421814940190/{superhero_id}/powerstats", timeout=30)

    return int(result.json()[stat_name])


superhero_names = ["Captain America", "Thanos", "Hulk"]

list = []
for superhero_name in superhero_names:

    id = superhero_id(superhero_name)
    intelligence = superhero_powerstat(id, "intelligence")

    list += [(superhero_name, intelligence)]

_, max_intelligence_superhero = max(enumerate(list), key=lambda x: x[1])

print(list)
print(f"Самый умный супергерой — {max_intelligence_superhero[0]}")