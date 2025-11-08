import pandas as pd
import numpy as np

"""
from parent_class import ParentClass
"""
#ParentClass
class PickleChild:

    def __init__(self):
        self.pickleFile = None

    """
    Takes data from the Spotify Top 100 csv file and makes a pkl file containing the same information
    """
    def load_data(self):
        #File path for the pkl file
        pkl_file_path = "Input\SpotifyTop100Data.pkl"

        #File path of the csv file
        csv_file_path = "Input\SpotifyTop100Data.csv"
        #Creates a data fram with the csv file
        df = pd.read_csv(csv_file_path)

        #Converts that data frame into a pickle file
        df.to_pickle(pkl_file_path)
        self.pickleFile = pd.read_pickle(pkl_file_path)


        #print(self.pickleFile)
    #

    """
    Calulates the joint probaility of two conditions
    Joint probability: The likelyhood that condition 1 will occur WITH condition 2
    """
    def calculate_joint_probability(self, condition1, condition2):

        #Sorts the lists lexographically
        condition1_data = sorted(self.get_list_of_values(condition1))
        condition2_data = sorted(self.get_unique_values(condition2))

        #Calculates the total number of rows in the file
        total_rows = len(self.pickleFile)

        #This is to deal with repeat values, when something in the first conditions list is accessed, it gets added to this
        condition1_visited = []

        #Loops through the first conditions column list
        for a in condition1_data:
            #Checks to make sure that the data hasnt been accessed before
            if(a not in condition1_visited):
                #Loops through the second condiions columb list
                for b in condition2_data:
                    #Kinda a lot, makes a variable that is the length of a data frame that holds the rows where both conditions are met
                    joint_occurences = len(
                        self.pickleFile[
                            (self.pickleFile[condition1] == a) & 
                            (self.pickleFile[condition2] == b)
                        ]
                    )

                    #Calclates the joint probability by taking the occurances and dividing it by the total rows
                    joint_prob = joint_occurences / total_rows

                    print(f"Probability of {condition1}:{a} and {condition2}:{b} is {joint_prob:.3f}")
                #
                #Adds the value to the visited list so it isnt visited again
                condition1_visited.append(a)
            #
        #
    #

    def calculate_probabilities(self):
        """Compute joint and conditional probabilities."""
        # pass

    def vector_operations(self, vec1, vec2):
        """Perform dot product, projection, and angle calculations."""
        # pass

    """
    Takes in the column that you want the data from and returns it as a set
    """
    def get_list_of_values(self, column):
        return self.pickleFile[column].tolist()
    #

    """
    Takes in the column that you want the data from and returns it as a set
    """
    def get_unique_values(self, column):
        return set(self.pickleFile[column].tolist())
    #

    def get_times_appeared(self, column, value):
        times_appeared = 0

        column_data = self.get_list_of_values(column)

        for values in column_data:
            if(value == values):
                times_appeared += 1
            #
        #
        return times_appeared
    #

    def generate_permutations(self, column):
         """Generate permutations of categorical values."""
        # pass

    def generate_combinations(self, column):
        """Generate combinations of categorical values."""
        # pass
