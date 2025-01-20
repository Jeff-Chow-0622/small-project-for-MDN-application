

from datetime import datetime
from Training import Bodypart
from Equipment import Equipment
from UserProfile import UserProfile
from TrackWorkout import WorkoutTracker

def register_user(user_dict, user_id):
    """Register a new user.

    Args:
        user_dict (dict): A dictionary to store user data with user IDs as keys.
        user_id (int): The current user ID.

    Returns:
        int: The updated user ID after registering the new user.
    """
    user_id += 1
    name = input("Enter your name: ")
    weight = float(input("Enter your current weight: "))
    height = float(input("Enter your current height: "))
    user_dict[user_id] = UserProfile(name)
    user_dict[user_id].add_weight(weight)
    user_dict[user_id].add_height(height)
    bmi = user_dict[user_id].calculate_bmi()
    print(f"Hello {name}, your ID is {user_id}, and your BMI is {bmi}")
    return user_id

def put_new_record(user_dict, bodypart, equipment_dict):
    """Record a new workout for an existing user.

    Args:
        user_dict (dict): A dictionary containing user data.
        bodypart (Bodypart): An instance of the Bodypart class, containing muscle group information.
        equipment_dict (dict): A dictionary to track equipment usage by users.
    """
    tracker = WorkoutTracker()

    user_id = int(input("Enter your ID: "))
    user_data = user_dict[user_id]

    if not user_data.personal_record:
        user_data.store_record(tracker)
    else:
        tracker = user_data.personal_record[0]

    print(f"\nWelcome back {user_data.display_name()}, let's record your training!")

    while True:
        try:
            user_input = input("Enter the date you exercised (format: DD/MM/YYYY): ")
            user_datetime = datetime.strptime(user_input, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid format. Please use the format DD/MM/YYYY.")

    while True:
        muscle_map = bodypart.display_all()
        selected_muscle_id = int(input("\nSelect the muscle part you've trained (Enter number), or type 0 to finish: "))
        if user_id not in equipment_dict:
            equipment_dict[user_id] = []

        if selected_muscle_id in muscle_map:
            group_name, sub_name = muscle_map[selected_muscle_id]
            print(f"You selected {group_name}: {sub_name}")
            user_equipment_list = equipment_dict.get(user_id, [])
            relevant_equipments = [
                equip for equip in user_equipment_list if (group_name, sub_name) in equip.trained_muscles
            ]

            if relevant_equipments:
                for index, equip in enumerate(relevant_equipments, 1):
                    print(f"{index}. {equip}")
                print("Enter 0 to type in new equipment.")
            else:
                print("No equipment recorded yet. Enter 0 to type in new equipment.")

            equipment_choice = int(input("Select equipment (Enter number): "))

            if equipment_choice == 0:
                equipment_name = input("Enter new equipment name: ")
                equipment_type = input("Enter equipment type (e.g., Free Weights, Machines, Cardio): ")
                new_equipment = Equipment(equipment_name, equipment_type)
                new_equipment.add_trained_muscle(group_name, sub_name)
                user_equipment_list.append(new_equipment)
                trained_equip = new_equipment
                print(f"New equipment added: {new_equipment}")
            elif 1 <= equipment_choice <= len(relevant_equipments):
                trained_equip = relevant_equipments[equipment_choice - 1]
                print(f"Using existing equipment: {trained_equip}")
            else:
                print("Invalid selection!")
                continue

            sets = int(input("How many sets have you trained: "))
            reps = int(input("How many reps have you done: "))
            weights = [float(input(f"Enter your weight on set {i + 1}: ")) for i in range(sets)]

            tracker.add_workout(user_datetime, group_name, sub_name, trained_equip, sets, reps, weights)
        elif selected_muscle_id == 0:
            break
        else:
            print("Invalid selection!")

    user_dict[user_id].store_record(tracker)
    print(tracker.date_workouts)

def view_record(user_dict):
    """View workout records for a specific date.

    Args:
        user_dict (dict): A dictionary containing user data.
    """
    user_id = int(input("Enter your ID: "))
    user_input = input("Enter the date you exercised (format: DD/MM/YYYY): ")
    user_datetime = datetime.strptime(user_input, "%d/%m/%Y")
    print(user_dict[user_id].personal_record[0].view_workouts(user_datetime))

def register_equipment(bodypart, equipment_dict):
    """Register new training equipment.

    Args:
        bodypart (Bodypart): An instance of the Bodypart class, containing muscle group information.
        equipment_dict (dict): A dictionary to store equipment details by category.
    """
    equipment_name = input("Enter the equipment name: ")
    equipment_type = input("What type is it (Free Weights, Machines, Cardio): ")
    category = input(f"What is it trained for? {bodypart.display_main_part()}: ")
    sub_category = input(f"Which part specifically does it train for? {bodypart.display_main_part()}: ")
    new_equipment = Equipment(equipment_name, equipment_type)
    new_equipment.add_trained_muscle(category, sub_category)
    equipment_dict.setdefault(category, {}).setdefault(sub_category, []).append(new_equipment)
    print(new_equipment)

def add_muscle_part(bodypart):
    """Add a new muscle group or submuscle.

    Args:
        bodypart (Bodypart): An instance of the Bodypart class, containing muscle group information.
    """
    while True:
        category = input(f"Choose categories: {bodypart.display_main_part()}, or type 'add' to add a new category: ")
        if category == "add":
            new_category = input("Type the new category that you want to add: ")
            bodypart.add_bodypart(new_category)
        elif category in bodypart.musclegroup:
            muscle_part = input("Type the muscle part that you want to add: ")
            bodypart.add_sub_bodypart(category, muscle_part)
        else:
            print("Invalid category!")
            continue
        break

def main():
    """Main function to initialize the program and handle user interactions."""
    bodypart = Bodypart()
    bodypart.add_bodypart("chest")
    bodypart.add_bodypart("lower body")
    bodypart.add_bodypart("back")
    bodypart.add_bodypart("shoulder")
    bodypart.add_sub_bodypart("chest", "upper chest")
    bodypart.add_sub_bodypart("chest", "mid chest")
    bodypart.add_sub_bodypart("chest", "lower chest")
    bodypart.add_sub_bodypart("lower body", "Quadriceps")
    bodypart.add_sub_bodypart("lower body", "Glutes")
    bodypart.add_sub_bodypart("back", "Lats")
    bodypart.add_sub_bodypart("back", "Traps")
    bodypart.add_sub_bodypart("shoulder", "middle delts")
    bodypart.add_sub_bodypart("shoulder", "front delts")
    bodypart.add_sub_bodypart("shoulder", "rear delts")

    selection = 0
    equipment_dict = {}
    user_dict = {}
    user_id = 0

    while selection != 6:
        print("Main Menu")
        print("1. Register a user")
        print("2. Put a new record")
        print("3. View your record")
        print("4. Register a new equipment")
        print("5. Add muscle part that you want to train")
        print("6. Exit")

        try:
            selection = int(input("Enter your option: "))
            if selection < 1 or selection > 6:
                print("Please select between option 1 to 6.")
                continue
        except ValueError:
            print("Please enter a valid number (must be an integer).")
            continue

        if selection == 1:
            user_id = register_user(user_dict, user_id)
        elif selection == 2:
            put_new_record(user_dict, bodypart, equipment_dict)
        elif selection == 3:
            view_record(user_dict)
        elif selection == 4:
            register_equipment(bodypart, equipment_dict)
        elif selection == 5:
            add_muscle_part(bodypart)

if __name__ == "__main__":
    main()                    