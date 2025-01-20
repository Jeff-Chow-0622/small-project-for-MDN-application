

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
    
    def compare_progress(self, date1, date2, muscle_group):
        """Compare workout progress for a specific muscle group between two dates.

        Args:
            date1 (datetime): The first workout date.
            date2 (datetime): The second workout date.
            muscle_group (str): The muscle group to compare.

        Returns:
            str: A summary of the progress made or a message if data is missing.
        """
        # Ensure both dates exist in records
        if date1 not in self.date_workouts or date2 not in self.date_workouts:
            return "One or both of the dates do not exist."

        # Ensure the muscle group data is available for both dates
        data1 = self.date_workouts[date1]
        data2 = self.date_workouts[date2]
        if muscle_group not in data1['sub_muscle'] or muscle_group not in data2["sub_muscle"]:
            return f"No data available for {muscle_group} on one or both of the dates."

        # Calculate the total weight lifted for each date
        sub_muscles1 = data1["sub_muscle"]
        Index1 = sub_muscles1.index(muscle_group)
        
        sub_muscles2 = data2["sub_muscle"]
        Index2 = sub_muscles2.index(muscle_group)
        
        weights1 = data1["weights"][Index1]
        
        reps1 = data1["reps"][Index1]
        
        weights2 = data2["weights"][Index2]
        
        reps2 = data2["reps"][Index2]
        
        total_weight1 = sum(weights1) * reps1
        total_weight2 = sum(weights2) * reps2

        # Calculate improvement
        improvement = total_weight2 - total_weight1
        return f"Improvement for {muscle_group}: {improvement} kg"            
                
