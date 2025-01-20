class Bodypart:
    """A class for managing muscle groups and submuscle parts.

    Attributes:
        musclegroup (dict): A dictionary storing muscle groups and their corresponding submuscles.
    """
    def __init__(self):
        self.musclegroup = {}
        
        
    def add_bodypart(self, bodypart):
        """Add a new muscle group to the profile.

        Args:
            bodypart (str): The name of the muscle group to add.
        """
        if bodypart not in self.musclegroup:
            self.musclegroup[bodypart] = {}
        
    def add_sub_bodypart(self, category, sub_bodypart):
        """Add a new submuscle part to a specific muscle group.

        Args:
            category (str): The muscle group to which the submuscle will be added.
            sub_bodypart (str): The name of the submuscle part to add.
        """
        if category in self.musclegroup:
            if sub_bodypart not in self.musclegroup[category]:
                self.musclegroup[category][sub_bodypart] = []
        
   
    
    def get_mainpart(self):
        """Get the main parts (muscle groups).

        Returns:
            dict: A dictionary of muscle groups and their corresponding submuscles.
        """
        return self.musclegroup
    
    def display_all(self):
        """Display all muscle groups and their corresponding submuscles.

        Returns:
            dict: A dictionary mapping of numbered submuscles to their respective groups.
        """
        
        counter = 1
        muscle_map = {}
        for category, subgroups in self.musclegroup.items():
            print(f"\n{category.upper()}:")
            for sub_bodypart in subgroups:
                muscle_map[counter] = (category, sub_bodypart)
                print(f"    {counter}.  {sub_bodypart}")
                counter += 1
        return muscle_map
    def display_main_part(self):
        """Display the main parts (muscle groups).

        Returns:
            str: A formatted string of muscle groups.
        """
        return ", ".join(self.musclegroup)
    
    
        