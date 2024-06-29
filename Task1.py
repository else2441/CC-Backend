import requests
import sys

if len(sys.argv)==2:
    name = sys.argv[1]
    url = "https://pokeapi.co/api/v2/pokemon/"+name
else:
     print("Kindly check Pokemon input.")

"""
# If the above code does not work, try the following after commenting the previous block
name = input()
url = "https://pokeapi.co/api/v2/pokemon/"+name
"""
try:
    response = requests.get(url)
    if response.status_code == 200:
            posts = response.json()
    elif response.status_code == 404:
         print("Pokemon does not exist.")
    else:
         print("Unrecognised server side error occurred.")
except:
      print("Unknown client side error occurred.")


try:
    if response.status_code == 200:
        typesname = []
        for i in posts["types"]:
            typesname.append(i["type"]["name"].upper())#can we color this somehow?

        abilities = []
        for i in posts["abilities"]:
            abilities.append(i["ability"]["name"].title())

        stats = []
        for i in posts["stats"]:
            stats.append(i["stat"]["name"].title()+": "+str(i["base_stat"]))

        def download_image(url, save_as):
            response = requests.get(url)
            with open(save_as, 'wb') as file:
                file.write(response.content)

        print("Name: " + name[0].upper()+name[1:] )
        print("National Number: "+str(posts['id']))
        print("Type: "+ " ".join(typesname))
        print("Abilities: "+" ".join(abilities))
        print("Height: "+ str(posts["height"]/10)+" m")
        print("Weight: "+ str(posts["weight"]/10)," kg", end = "\n\nBase stats:\n")
        for i in stats:
            print(i)
        for value in posts["sprites"].values():
            if type(value) == str:
                download_image(value, "sprite.png")
                break
        else:
            print("No valid image found.")
except:
    print("Unknown client side error occurred.")
