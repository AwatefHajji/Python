class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
# jason = {
#     	"name": "Jason Tatum", 
#     	"age":24, 
#     	"position": "small forward", 
#     	"team": "Boston Celtics"
# }
# kyrie = {
#     	"name": "Kyrie Irving", 
#     	"age":32,
#         "position": "Point Guard", 
#     	"team": "Brooklyn Nets"
# }
    
# Create your Player instances here!
# player_kevin =Player(kevin["name"],kevin["age"],kevin["position"],kevin["team"])
# print(player_kevin.name)
# player_jason =Player(jason["name"],jason["age"],jason["position"],jason["team"])
# print(player_jason.name)
# player_kyrie =Player(kyrie["name"],kyrie["age"],kyrie["position"],kyrie["team"])
# print(player_kyrie.name)
players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

new_team=[]
for i in range (len(players)):
    new_team.append(Player(players[i]["name"],players[i]["age"],players[i]["position"],players[i]["team"]))
for i in range (len(new_team)):
    print(f" Name : {new_team[i].name} Age: {new_team[i].age} Position: {new_team[i].position} Team : {new_team[i].team}" )

