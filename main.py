print('''
 ___ _ __  _   _ 
/ __| '_ \| | | |
\__ \ |_) | |_| |
|___/ .__/ \__, |
    | |     __/ |
    |_|    |___/ 
''')
print("Welcome 007.")
print("Your mission is to find the chip to deactivate the bomb.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

#Quests
quest1 = input(
  'You\'re at a cross road. Where do you want to go? Type "left" or "right"?\n'
).lower()

if quest1 == "left":
  quest2 = input(
    "You come across a river with a strong current. Decide and type if you would like to 'Swim' across it or 'Wait' for the current to weaken?\n"
  ).lower()

  if quest2 == "wait":
    quest3 = input(
      'You swim across and come across a building with 3 doors. Do you open the "blue", "red" or "yellow" door?\n'
    ).lower()
    if quest3 == "yellow":
      print(
        "You see the chip in a glass container. Quickly run in and intercept the chip. You win!"
      )

    elif quest3 == "red":
      print(
        "Oh no! You entered a trap door and fell to your death. Game Over.")
    elif quest3 == "blue":
      print(
        "You enter the dark room and the door closes behind you. Flames light up the room and burn you alive. Game over."
      )

  else:
    print("You jumped into a pirrana dinner. You are dead!")

else:
  print("You're dead!")
