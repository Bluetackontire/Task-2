#recall functions from its file
from functions import login, dice_roll, winner, tie, result

login()
dice_roll()

#ouputs the total points for each player
print(login.name1, "got", dice_roll.score1, "points")
print(login.name2, "got", dice_roll.score2, "points")
print()

winner()
tie()
result()