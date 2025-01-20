class Equipment():
    """A class representing a piece of equipment used for workouts.

    Args:
        name (str): The name of the equipment.
        typ (str): The type of equipment (e.g., Free Weights, Machines, Cardio).
    """
    
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ
        self.trained_muscles = []
       # Equipment.all_equipments.append(self)
        print("An equipment instance has been created!")
    
    def add_trained_muscle(self, muscle_group, sub_bodypart):
        """Store the muscle groups and submuscles trained by the equipment.

        Args:
            muscle_group (str): The main muscle group trained.
            sub_bodypart (str): The specific muscle trained.
        """
        
        self.trained_muscles.append((muscle_group, sub_bodypart))
    
   
    def display_trained_muscles(self):
        """Display the trained muscles by the equipment.

        Returns:
            str: A formatted string of trained muscles or a message if none recorded.
        """
    
        if self.trained_muscles:
            return ", ".join([f"{group} -> {sub}" for group, sub in self.trained_muscles])
        return "No trained muscles recorded yet."
    

        
    def __str__(self):
        """String representation of the Equipment instance.

        Returns:
            str: A formatted string representing the equipment and its trained muscles.
        """
        trained_muscle_info = self.display_trained_muscles()
        return f"Equipment(name={self.name}, type={self.typ}, trained muscles={trained_muscle_info})"
    
    
    
    
   
        
