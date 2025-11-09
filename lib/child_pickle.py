import pandas as pd
import numpy as np
import itertools

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
    #

    """
    Calulates the joint probaility of two conitions (that the user gives)
    Joint probability: The likelyhood that condition 1 will occur WITH condition 2
    """
    def calculate_joint_probability(self, column1, a, column2, b):
        #Calculates the total number of rows in the file
        total_rows = len(self.pickleFile)

        #Kinda a lot, makes a variable that is the length of a data frame that holds the rows where both conditions are met
        joint_occurences = len(
            self.pickleFile[
                (self.pickleFile[column1] == a) & 
                (self.pickleFile[column2] == b)
            ]
        )
        #Calclates the joint probability by taking the occurances and dividing it by the total rows
        joint_prob = joint_occurences / total_rows

        return joint_prob
    #

    """
    Calulates the joint probaility of two columns (that the user gives)
    Joint probability: The likelyhood that condition 1 will occur WITH condition 2
    """
    def calculate_all_joint_probability(self, column1, column2):
        #Sorts the lists lexographically
        column1_data = sorted(self.get_unique_values(column1))
        column2_data = sorted(self.get_unique_values(column2))
        #Calculates the total number of rows in the file
        total_rows = len(self.pickleFile)

        #Loops through the first column list
        for a in column1_data:
            #Loops through the second columb list
            for b in column2_data:
                #Kinda a lot, makes a variable that is the length of a data frame that holds the rows where both conditions are met
                joint_occurences = len(
                    self.pickleFile[
                        (self.pickleFile[column1] == a) & 
                        (self.pickleFile[column2] == b)
                    ]
                )
                #Calclates the joint probability by taking the occurances and dividing it by the total rows
                joint_prob = joint_occurences / total_rows

                print(f"Probability of {column1}:{a} and {column2}:{b} is {joint_prob:.3f}")
            #
        #
    #

    """
    Calulates the conditional probaility of two conditions (that the user gives)
    conition 2 is the given probability
    Condition probability: The likelyhood that condition 1 will occur given condition 2 occurs
    """
    def calculate_conditional_probability(self, column1, a, column2, b):
        #Kinda a lot, makes a variable that is the length of a data frame that holds the rows where both conditions are met
        joint_occurences = len(
            self.pickleFile[
                (self.pickleFile[column1] == a) &
                (self.pickleFile[column2] == b)
            ]
        )

        #Counts how many rows fit conition 2
        given_occurrences = self.get_times_appeared(column2, b)

        #Calcilates the conditional probability
        conditional_prob = joint_occurences / given_occurrences

        return conditional_prob
    #

    """
    Calulates the conditional probaility of two columns (that the user gives)
    Column 2 is the given probability
    Condition probability: The likelyhood that condition 1 will occur given condition 2 occurs
    """
    def calculate_all_conditional_probability(self, column1, column2):
        #Sorts the lists lexographically
        column1_data = sorted(self.get_unique_values(column1))
        column2_data = sorted(self.get_unique_values(column2))

        #Loops through the first column list
        for a in column1_data:
            #Loops through the second columb list
            for b in column2_data:
                #Kinda a lot, makes a variable that is the length of a data frame that holds the rows where both conditions are met
                joint_occurences = len(
                    self.pickleFile[
                        (self.pickleFile[column1] == a) &
                        (self.pickleFile[column2] == b)
                    ]
                )

                given_occurrences = self.get_times_appeared(column2, b)

                #Calcilates the conditional probability
                conditional_prob = joint_occurences / given_occurrences

                print(f"Probability of {column1}:{a} and {column2}:{b} is {conditional_prob:.3f}")
            #
        #
    #

    """
    Takes in the column that you want the data from and returns it as a list
    """
    def get_list_of_values(self, column):
        #Returns the data as a list
        return self.pickleFile[column].tolist()
    #

    """
    Takes in the column that you want the data from and returns it as a set
    """
    def get_unique_values(self, column):
        #Returns the data as a set (basically a list without repeats)
        return set(self.pickleFile[column].tolist())
    #

    """
    Gets the times that a value appears in a column
    """
    def get_times_appeared(self, column, value):
        times_appeared = 0

        #Makes the data a list
        column_data = self.get_list_of_values(column)

        #Iterates through the list and counts every time it matches the given value
        for values in column_data:
            if(value == values):
                times_appeared += 1
            #
        #

        #Returns the number of times the value appears in the list
        return times_appeared
    #

    """
    Makes a data frame full of all the permutations of a given column
    Permutation: All possible orders of a column given an iterable
    WARNING: CAN BE A LOT FOR YOUR COMPUTER - IT CRASHED MINE BUT I KNOW IT WORKS CAUSE ITS PERFECT FOR THE COLUMNS WITH VERY FEW VALUES (YEAR)
    TODO: I added the iterable to see if it would run, it does but idk if we wanna keep it
    """
    def generate_permutations(self, column, iterable):
        #Makes a sorted set of all the values in a column
        column_data = sorted(self.get_unique_values(column))

        #Uses itertools to generate all the permutations of the column
        all_column_permutations = list(itertools.permutations(column_data, iterable))

        #Puts all the permutations into a data frame
        df_all_column_permutations = pd.DataFrame(all_column_permutations)

        #Returns the data frame
        return df_all_column_permutations
    #

    """
    Makes a data frame full of all the combinations of a given column
    Combinations: All possible groups of a column
    """
    def generate_combinations(self, column, iterable):
        #Makes a sorted set of all the values in a column
        column_data = sorted(self.get_unique_values(column))

        #Uses itertools to generate all the combinations of the column
        all_column_combinations = list(itertools.combinations(column_data, iterable))

        #Puts all the cominations into a data frame
        df_all_column_combinations = pd.DataFrame(all_column_combinations)

        #Returns the data frame
        return df_all_column_combinations
    #

    """
    Makes a column into an array
    """
    def make_data_to_arr(self, column):
        #Makes it a list
        column_data = self.get_list_of_values(column)

        #Makes it a numpy array
        column_data_arr = np.array(column_data)

        #Returns the array
        return column_data_arr
    #

    """
    Generates the dot product of 2 columns
    ONLY WORKS FOR NUMERICAL COLUMNS
    """
    def generate_dot_product(self, column1, column2):
        #Makes the columns arrays
        column1_data_arr = self.make_data_to_arr(column1)
        column2_data_arr = self.make_data_to_arr(column2)

        #Uses numpy to do the dot product
        dot_product = np.dot(column1_data_arr, column2_data_arr)

        #Returns the dot produt
        return dot_product
    #

    """
    Generates the projection of 2 columns
    ONLY WORKS FOR NUMERICAL COLUMNS
    """
    def generate_projection(self, column1, column2):
        #Makes the columns arrays
        column1_data_arr = self.make_data_to_arr(column1)
        column2_data_arr = self.make_data_to_arr(column2)

        #Projecting column1 onto column2; Using numpy dot products (dot(a,b) / dot(b,b)) * b 
        projection = (np.dot(column1_data_arr, column2_data_arr) / np.dot(column2_data_arr, column2_data_arr)) * column2_data_arr

        #Returns projection
        return projection
    #

    """
    Generates the angle calculation of 2 columns
    ONLY WORKS FOR NUMERICAL COLUMNS
    """
    def generate_angle_calculations(self, column1, column2):
        #Makes the columns arrays
        column1_data_arr = self.make_data_to_arr(column1)
        column2_data_arr = self.make_data_to_arr(column2)
        
        #Getting the dot then divinding it by the magnitudes
        cos_of_columns = np.dot(column1_data_arr, column2_data_arr) / (np.linalg.norm(column1_data_arr) * np.linalg.norm(column1_data_arr))

        #Avoids rounding errors
        cos_of_columns = np.clip(cos_of_columns, -1.0, 1.0)

        #Makes the calculation to degrees using numpy
        calculate_angle = np.degrees(np.arccos(cos_of_columns))

        #Returns the angle
        return calculate_angle
    #