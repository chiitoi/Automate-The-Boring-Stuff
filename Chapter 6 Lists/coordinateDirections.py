input_empty = False
direction_list = []
print("Enter N, S, E, or W as coordinates. Enter a blank string to end.")
while not input_empty:
    user_input = input(">")
    if not user_input:
        input_empty = True
    elif user_input.upper() not in "NSEW":
        print("Please enter N, S, E, or W")
    else:
        direction_list.append(user_input.upper())




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