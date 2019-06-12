from django.http import JsonResponse
import json
import requests
import os
from random import randint


KEY = os.environ.get("GIPHY_KEY")

def pokemon_view(request, id):

    poke_res = requests.get(f"http://pokeapi.co/api/v2/pokemon/{id}/")
    pokemon = json.loads(poke_res.content)
    name  = pokemon["name"]
    types = [t["type"]["name"] for t in pokemon["types"]]

    giphy_res = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={KEY}&q={name}&rating=g")
    results = json.loads(giphy_res.content)
    num = randint(0, 9)
    gif = results['data'][num]["url"]

    return JsonResponse({
        "id": id,
        "name": name,
        "types": types,
        "gif": gif
    })

# Earlier we just grabbed the first GIF from the set that GIPHY returned to us, and sent that through our API. It would be better if we could send a random one instead.

