start = '''
One day a dog named Beebo ran away from his home in New York City. He felt lonely and wanted to explore the busy and captivating city. Help beebo find his way home!
'''
print(start)

print("To decide which direction he should go, type 'left' to go left or 'right' to go right.")
print()
user_input = input()
if user_input == "left":
    print()
    print("Beebo goes left and ends up at the park.")
    print("He sees a squirrel. Type 'bark' or 'attack' to decide what he does next.")
    print()
    user_input = input()
    if user_input == "bark":
        print()
        print("His owner sees him and takes him home!")
        print("Yay! You helped him find his home!:)")
        print()
    elif user_input == "attack":
        print()
        print("Oh no! He was sent to the dog pound. :(")
        print("What should he do? Type 'wait' if he should wait for his owner or type 'escape' is he should escape!")
        print()
        user_input = input()
        if user_input == "wait":
            print()
            print("Beebo Dies. :(")
            print("End of story.")
            print()
        elif user_input == "escape":
            print()
            print("He finds his owner and gets to go home!")
            print("Yay! You helped him find his home!:)")
            print()
        else:
            print()
            print ("Incorrect input!Try again.")
            print()
    else:
        print()
        print ("Incorrect input!Try again.")
        print()
elif user_input == "right":
    print()
    print("Beebo goes right and ends up in the sketchy streets of New York.")
    print("He sees a women getting robbed. Type 'fight' to fight against the robbers or 'walk' to walk away and not get involved.")
    print()
    user_input = input()
    if user_input == 'fight':
        print()
        print("Beebo breaks his paw during the rough fight, but wins in the end. The woman wants to take him to vet.")
        print("What should Beebo do next? Type 'walk' to tell him to keep looking for his owner with a broken paw or type 'vet'  to go to the vet with the mysterious woman.")
        print()
        user_input = input()
        if user_input == "walk":
            print()
            print("Sadly, Beebo is in a lot of pain and can't continue to walk. He dies. :(")
            print("End of story.")
            print()
        elif user_input == "vet":
            print()
            print("She takes him to the vet and the vet knows the dog's owner! The vet calls Beebo's owner and she comes to get him and takes him home!")
            print("Yay! You helped him find his home!:)")
            print()
        else:
            print()
            print ("Incorrect input!Try again.")
            print()
    elif user_input == "walk":
        print()
        print("His owner sees him and takes him home!")
        print("Yay! You helped him find his home!:)")
        print()
    else:
        print()
        print ("Incorrect input!Try again.")
        print()
else:
    print()
    print ("Incorrect input!Try again.")
    print()
