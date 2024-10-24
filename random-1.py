# bestäm om det är udda eller jämnt
# rulla tärningar
# vinnaren är det som bestämts

from random import randint

rule = input("odd or even: ")
computer = randint(1, 6)
player = randint(1, 6)

if rule == "odd": 
  computer_result = computer % 2
  player_result = player % 2
  print(f"Computer rolled {computer_result} and the player {player_result}, game rule was {rule}")

else:
  computer_result = computer % 2
  player_result = player % 2
  print(f"Computer rolled {computer_result} and the player {player_result}, game rule was {rule}")