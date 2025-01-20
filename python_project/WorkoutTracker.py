

class WorkoutTracker:
    """A class for tracking workouts by date.

    Attributes:
        date_workouts (dict): A nested dictionary storing workout records by date.
    """
    def __init__(self):
        self.date_workouts = {}  # a nested dict storing workout records by date 
        
    def add_workout(self, date, muscle_group, sub_muscle, equipment, sets, reps, weights:list):
        """Add a workout record for a specific date.

        Args:
            date (datetime): The date of the workout.
            muscle_group (str): The main muscle group trained.
            sub_muscle (str): The specific muscle trained.
            equipment (Equipment): The equipment used for the workout.
            sets (int): The number of sets performed.
            reps (int): The number of reps per set.
            weights (list): A list of weights used for sets. each weight refer to each set
        """ 
        
        if date not in self.date_workouts:
            self.date_workouts[date] = {
                "muscle_group": [],
                "sub_muscle": [],
                "equipment": [],
                "sets": [],
                "reps": [],
                "weights": [],
            }
        
        self.date_workouts[date]["muscle_group"].append(muscle_group)
        self.date_workouts[date]["sub_muscle"].append(sub_muscle)
        self.date_workouts[date]["equipment"].append(equipment)
        self.date_workouts[date]["sets"].append(sets)
        self.date_workouts[date]["reps"].append(reps)
        self.date_workouts[date]["weights"].append(weights)
        print(f"Workout added for {date}: {muscle_group}, {sub_muscle}, {equipment}, {sets}, {reps}, {weights}")

    
    def view_workouts(self, date):
        """View the workouts recorded for a specific date.

        Args:
            date (datetime): The date to view workouts for.

        Returns:
            str: A formatted string of workouts recorded on that date or a message if no workouts are found.
        """
            
        if date not in self.date_workouts:
            print(f"No workouts recorded on {date}.")
            return []
        else:
            output = f"Date: {date.strftime('%Y-%m-%d')}\n"
            data = self.date_workouts[date]
            for i in range(len(data["muscle_group"])):
                output += f"Muscle Group: {data['muscle_group'][i]}\n"
                output += f"  Sub Muscle: {data['sub_muscle'][i]}\n"
                output += f"    Equipment: {data['equipment'][i].name} ({data['equipment'][i].typ})\n"
                output += f"    Sets: {data['sets'][i]}\n"
                output += f"    Reps per Set: {data['reps'][i]}\n"
                output += f"    Weights: {data['weights'][i]}\n"
        return output
                
                