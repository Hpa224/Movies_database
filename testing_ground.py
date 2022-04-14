import time
favorites = ["serpentis", "crazy_kart", "skyrim", "paranoid", "rizomata", "standing", "mist", "frostdrake", "wanderers", "Ridorana", "Temple", "ice"]
current_map = "none"
count = 0
favoriteMap = ""

def send():
    return print("we sent a text")

while True:

    for i in favorites:
        if i in favoriteMap:
            print("we wont send a text")
            break

        if i in current_map.lower():
            send()
            favoriteMap = current_map 
            break        

    time.sleep(.5)
