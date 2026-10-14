class Player:
    pass


player_1 = Player()

player_1.name = "Omar"
player_1.team = "El-zamalk"
player_1.score = 100

player_2 = Player()

player_2.name = "Saeed"
player_2.team = "EL-Ahly"
player_2.score = 90

player_3 = Player()

player_3.name = "Shwaly"
player_3.team = "Smoha"
player_3.score = 89

print(
    f"player-1 is name : {player_1.name} and team name is : {player_1.team } and score the player = {player_1.score}"
)
print(
    f"player-2 is name : {player_2.name} and team name is : {player_2.team } and score the player = {player_2.score}"
)
print(
    f"player-3 is name : {player_3.name} and team name is : {player_3.team } and score the player = {player_3.score}"
)

player_1.score += 10
player_2.score += 10
player_3.score += 10


print(f"After edit score score player_1 = {player_1.score}")
print(f"After edit score score player_2 = {player_2.score}")
print(f"After edit score score player_3 = {player_3.score}")
