from sourceserver.sourceserver import SourceServer
import time
from twilio.rest import Client

favorites = ["serpentis", "crazy_kart", "skyrim", "paranoid", "rizomata", "standing", "mist", "frostdrake", "wanderers", "ridorana", "temple"]
acounts_Id = "ACfb218f35228ea506cff7bace37c3592a"
auth_token = "8b288f863328a876b78a26f338b08f80"
twilio_number = "+19035322122"
my_number = "3056095089"
favorite_map = ""


def text(x):
    twilioCli = Client(acounts_Id, auth_token)
    twilioCli.messages.create(body=x, from_=twilio_number, to=my_number)

def server_command(ip):
    srv = SourceServer(ip)
    srv_name = srv.info["name"]
    current_map = srv.info["map"]
    players = srv.info['players']
    max_players = srv.info['max_players']
    info = [srv_name, current_map, players, max_players]
    return info

# while True:
#     srv = SourceServer("216.52.148.47:27015")
#     srv_name = srv.info["name"]
#     current_map = srv.info["map"]
#     players = srv.info['players']
#     max_players = srv.info['max_players']
#     message = f"{srv_name}\nNow Playing: {current_map}\nPlayers Online: {players}/{max_players}"
#     print(message)

#     for i in favorites:
#         if i in favorite_map:
#             print(f"we wont send a text")
#             break

#         if i in current_map.lower():
#             print(f"we send a text here {current_map}")
#             # text(message)
#             favorite_map = current_map
#             break

#     time.sleep(.5)
