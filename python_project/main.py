from datetime import datetime
from Bodypart import Bodypart
from Equipment import Equipment
from UserProfile import UserProfile
from WorkoutTracker import WorkoutTracker

def register_user(user_dict, id):
    """Register a new user.

    Args:
        user_dict (dict): A dictionary to store user data with user IDs as keys.
        id (int): The current user ID.

    Returns:
        int: The updated user ID after registering the new user.
    """
    id += 1
    name = input("enter you name: ")
    weight = float(input("enter your current weight: "))
    height = float(input("enter your current height: "))
    user_dict[id] = UserProfile(name)
    user_dict[id].add_weight(weight)
    user_dict[id].add_height(height)
    bmi = user_dict[id].calculate_bmi()
    print(f"hello {name}, your id is {id}, and your BMI is {bmi}")
    return id

def put_new_record(user_dict, bodypart, equipment_dict):
    """Record a new workout for an existing user.

    Args:
        user_dict (dict): A dictionary containing user data.
        bodypart (Bodypart): An instance of the Bodypart class, containing muscle group information.
        equipment_dict (dict): A dictionary to track equipment usage by users.
    """
    tracker = WorkoutTracker()
    validInput = False
    rgistd_id = int(input("enter your id: "))
    user_data = user_dict[rgistd_id]

    if not user_data.personal_record:
        tracker = WorkoutTracker()
        user_data.store_record(tracker)
    else:
        tracker = user_data.personal_record[0]  # 使用列表中的第一個元素

    print(f"\nwelcome back {user_data.display_name()}, let's record your training!")
    while not validInput:
        user_input = input("enter the date you exercise (format：DD/MM/YYYY)：")
        try:
            user_datetime = datetime.strptime(user_input, "%d/%m/%Y")
            validInput = True
        except ValueError:
            print("Invalid format. Please use the format DD/MM/YYYY.")

    while True:
        muscle_map = bodypart.display_all()
        selected_muscle_id = int(input("\nSelect the muscle part you've trained(Enter number): or type 0 to finish"))
        if rgistd_id not in equipment_dict:
            equipment_dict[rgistd_id] = []
        if selected_muscle_id in muscle_map:
            selected_muscle: tuple = muscle_map[selected_muscle_id]
            print(f"You selected {selected_muscle[0]}: {selected_muscle[1]}")
            user_equipment_list = equipment_dict.get(rgistd_id, [])
        elif selected_muscle_id == 0:  # user finish entering the records
            break
        else:
            print("Invalid selection!")

        group_name, sub_name = muscle_map[selected_muscle_id]
        print(f"you chose {group_name}: {sub_name}")

        relevant_equipments = [] # initialise a list storinig equipments related to chosen muscle group
        if user_equipment_list:
            for equip in user_equipment_list: # traverse the user's equipment list regardless of which muscle
                if (group_name, sub_name) in equip.trained_muscles: # trained_muscles is a list storing the muscle groups trained by the equipment
                    relevant_equipments.append(equip)

        if relevant_equipments:
            index = 1
            # this for loop display the equipments related to ur trained muscle you used previously
            for equip in relevant_equipments: 
                print(f"{index}. {equip}")
                index += 1
            print("Enter 0 to type in new equipment.")
        else:
            print("No equipment recorded yet. Enter 0 to type in new equipment.")

        equipment_choice = int(input("Select equipment (Enter number): "))
        if equipment_choice == 0:
            equipment_name = input("Enter new equipment name: ")
            equipment_type = input("Enter equipment type (e.g., Free Weights, Machines, Cardio): ")
            user_equipment_list.append(Equipment(equipment_name, equipment_type)) # user_equipment_list saves user's equipments the type of each element is Equipment

            user_equipment_list[-1].add_trained_muscle(group_name, sub_name)
            trained_equip = user_equipment_list[-1]
            print(f"New equipment added: {user_equipment_list[-1]}")
        elif 1 <= equipment_choice <= len(user_equipment_list):
            selected_equipment = user_equipment_list[equipment_choice - 1]
            print(f"Using existing equipment: {selected_equipment}")
            trained_equip = selected_equipment
        else:
            print("Invalid selection!")

        sets = int(input("how many sets have you trained: "))
        reps = int(input("how many reps have you done: "))
        weights = []
        for i in range(sets):
            weights.append(float(input(f"enter your weight on {i+1} th set")))

        tracker.add_workout(user_datetime, group_name, sub_name, trained_equip, sets, reps, weights)
    user_dict[rgistd_id].store_record(tracker)
    print(tracker.date_workouts)
    print(user_dict[rgistd_id].personal_record)

def view_record(user_dict, bodypart):
    
    rgistd_id = int(input("type in ur id: "))
    user_input = input("enter the date you exercise (format：DD/MM/YYYY)：")
    user_datetime = datetime.strptime(user_input, "%d/%m/%Y")
    print(user_dict[rgistd_id].personal_record[0].view_workouts(user_datetime)) # user_dict[rgistd_id].personal_record[0] is the WorkoutTracker class object
    
    sub_selec = int(input("would you like to see your improvement? (1. Yes 0. No)"))
    if sub_selec == 1:
        user_input_day1 = input("enter the date 1 (format：DD/MM/YYYY)：")
        user_datetime_1 = datetime.strptime(user_input, "%d/%m/%Y")
        user_input_day2 = input("enter the date 2 (format：DD/MM/YYYY)：")
        user_datetime_2 = datetime.strptime(user_input, "%d/%m/%Y")
        
        muscle_map = bodypart.display_all()
        selected_muscle_id = int(input("\nSelect the muscle part you want to see the improvement: "))
        
        selected_muscle: tuple = muscle_map[selected_muscle_id]
        
    
        
        improvement = user_dict[rgistd_id].personal_record[0].compare_progress(user_datetime_1, user_datetime_2, selected_muscle[1])
        print(improvement)
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
    flag = 1
    while flag == 1:
        flag = 0
        catagory = input(f"Choose categories: {bodypart.display_main_part()}: or type \"add\" to add a new catagory: ")
        if catagory == "add":
            new_catag = input("type the new categorey that you want to add: ")
            bodypart.add_bodypart(new_catag)
        elif catagory in bodypart.musclegroup.keys():
            muscle_part = input("type the muscle part that you want to add: ")
            bodypart.add_sub_bodypart(catagory, muscle_part)
        else:
            print("please enter a valid name!")
            flag = 1

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
    user_dict = {} #key is user's id, and the element is user's profile including user's information and workout records

    id = 0
    while selection != 6:
        print("main menu")
        print("1. register a user")
        print("2. put a new record")
        print("3. view your record")
        print("4. register a new equipment")
        print("5. add muscle part that you want to train")
        print("6. Exit")

        try:
            selection = int(input("enter your option: "))
            if selection < 1 or selection > 6:
                print("Please select between option 1 to 6")
                selection = int(input("enter your option: "))
        except ValueError:
            print("please enter valid number(must be an integer):")
            selection = int(input("enter your option: "))

        if selection == 1:
            id = register_user(user_dict, id)
        elif selection == 2:
            put_new_record(user_dict, bodypart, equipment_dict)
        elif selection == 3:
            view_record(user_dict, bodypart)
        elif selection == 4:
            register_equipment()
        elif selection == 5:
            add_muscle_part(bodypart)
    
if __name__ == "__main__":
    main()
    
    

