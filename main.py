print("Welcome to Treasure Island! A game where you can see if you have what it takes! Let's Play!")
print('Your mission is to escape the island with your treasure!')
choice = str(input('Would you like to go left or right?' )).lower()

if choice == "left":
    second_choice =input('You come across a wide river. Do you want to walk along side the river or swim ahead? Choose WALK or SWIM. ').lower()
    if second_choice == "walk":
       third_choice = input('You find a working boat along the island shore with footprints leading away from it. Do you take the boat and leave, wait for the other person to come back, or keep walking along the shore? Choose LEAVE, WAIT, or WALK. ').lower()
       if third_choice == "wait":
           print('The other Pirate comes back. He helps you get off the island with 5%\ split of treasure.YOU WIN AND BECOME PIRATE KING!!!')
       elif third_choice == "leave":
           print('Rowing took too much out of you and you die lost at sea. GAME OVER!')
       elif third_choice == "walk":
           print('You die of exhaustion and pass out. Ohter Pirate takes your tresure and leaves you. GAME OVER!')
       else:
           print('GAME OVER!') 
    else:
        print('Baracuda attack. GAME OVER!')
else:
    print('You fell into a snake pit. GAME OVER!')