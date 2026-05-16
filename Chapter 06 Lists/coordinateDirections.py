#Chapter 6 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter6.html

input_empty = False
direction_list = []
print("Enter N, S, E, or W as coordinates. Enter a blank string to end.")

#Prompts user to enter case insensitive N, S, E, W to simulate directions the user is taking
while not input_empty:
    user_input = input(">")
    if not user_input:
        input_empty = True
    elif user_input.upper() not in "NSEW":
        print("Please enter N, S, E, or W")
    else:
        direction_list.append(user_input.upper())

#In the list, it changes the coordinates based off the direction. N increases the y-axis and E increases the x-axis
def get_end_coordinates(directions):
    print("Directions entered:", directions)
    coordinates = [0,0]
    for direction in directions:
        if direction == "N":
            coordinates[1]+=1
        elif direction == "S":
            coordinates[1]-=1
        elif direction == "W":
            coordinates[0]-=1
        else:
            coordinates[0]+=1
    return coordinates

print(get_end_coordinates(direction_list))