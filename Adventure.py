name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? (Left/Right): ").lower()

if answer == "left":
    answer = input("You came across a large river you can either swin through it or walk around it. What would you like to do? (swim/walk): ").lower()
    if answer == "swim":
        answer = input("You jump in the water and start swimming. After crossing the middle fight off an alligator! You are now on the other side of the river du you wanna ").lower()
    elif answer == "walk":
        answer = input("You start walking and after 2 hours you run out of water! You died of dehydration!").lower()





elif answer == "right":
    answer = input("You came across a large river you can either swin through it or walk around it. What would you like to do? (swim/walk): ").lower()
    if answer == "swim":
        answer = input("You jump in the water and start swimming. after crossing the middle of the river you get eaten by a alligator. You Died!").lower()
    elif answer == "walk":
        answer = input("You start walking and after 2 hours you run out of water! You died of dehydration!").lower()
