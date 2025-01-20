from WorkoutTracker import WorkoutTracker

class UserProfile:
    """A class representing a user's profile for tracking health and workout records.

    Args:
        name (str): The name of the user.
    """    
    def __init__(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """        
        
        self.name = name
        self.height = []  # cm
        self.weight = []  # kg
        self.personal_record = [] # 
        #self.personal_record = WorkoutTracker()
        
    def calculate_bmi(self):
        """Calculate the user's Body Mass Index (BMI).

        Returns:
            float: The calculated BMI value.
        """
        bmi = self.weight[-1] / ((self.height[-1]) / 100) ** 2
        bmi = round(bmi, 2)
        return bmi
    
    def store_record(self, workout_record):
        """Store a workout record in the user's profile.

        Args:
            workout_record (WorkoutTracker): The workout record to store.
        """
        if not self.personal_record:
            # if the list is empty, then add WorkoutTracker
            self.personal_record.append(workout_record)
        else:
            # if it's already exist, then replace it with new WorkoutTracker
            self.personal_record[0] = workout_record
        
    
    def add_weight(self, weight):
        """Add a weight record to the user's profile.

        Args:
            weight (float): The weight to add (in kg).
        """
        self.weight.append(weight)
        
    def add_height(self, height):
        """Add a height record to the user's profile.

        Args:
            height (float): The height to add (in cm).
        """
        self.height.append(height)
    
    def get_weight_record(self):
        """Get the user's weight records.

        Returns:
            list: A list of weight records.
        """
        return self.weight
    
    def display_name(self):
        """Display the user's name.

        Returns:
            str: The name of the user.
        """
        return self.name
        
        