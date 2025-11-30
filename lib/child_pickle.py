import pandas as pd
import numpy as np
import itertools
from lib.config import CONFIG

"""
from parent_class import ParentClass
"""
#ParentClass
class PickleChild:

    def __init__(self):
        self.pickleFile = None

    
    def load_data(self):
        """
        Takes data from the Spotify Top 100 csv file and makes a pkl file containing the same information
        """
        #File path for the pkl file
        pkl_file_path = CONFIG["PICKLE_PATH"]

        #File path of the csv file
        csv_file_path = CONFIG["CSV_PATH"]
        #Creates a data fram with the csv file
        df = pd.read_csv(csv_file_path)

        #Converts that data frame into a pickle file
        df.to_pickle(pkl_file_path)
        self.pickleFile = pd.read_pickle(pkl_file_path)
    #
    
    """
    Calculates, displays, and exports the JOINT COUNTS
    Joint Counts: TODO
    """

    #Calulates the joint count of two columns (that the user gives) and makes a table
    def calculate_joint_counts_table(self, column1, column2):
        return (pd.crosstab(index=self.pickleFile[column1], columns=self.pickleFile[column2], margins=True, normalize=True) * 100)
    #

    #Prints the joint count of two columns (that the user gives) as a table
    def display_joint_counts_table(self, column1, column2):
        print(self.calculate_joint_counts_table(column1, column2))
    #

    #Exports the joint count of two columns (that the user gives) to a TODO
    def export_joint_counts_table(self, column1, column2):
        df = self.calculate_joint_counts_table(column1, column2)
        df.to_csv('output\Output_Joint_Counts_Table.csv', index=True)
    #

    """
    Calculates, displays, and exports the JOINT PROBABILITIES
    Joint Probability: The likelyhood that condition 1 will occur WITH condition 2
    """
    
    #Calulates the joint probability of two columns (that the user gives) and makes a table
    def calculate_joint_probability_table(self, column1, column2):
        joint_counts = self.calculate_joint_counts_table(column1, column2)
        return (joint_counts / joint_counts.values.sum())
    #

    #Prints the joint probability of two columns (that the user gives) as a table
    def display_joint_probability_table(self, column1, column2):
        print(self.calculate_joint_probability_table(column1, column2))
    #

    #Exports the joint probability of two columns (that the user gives) to a TODO
    def export_joint_probability_table(self, column1, column2):
        df = self.calculate_joint_probability_table(column1, column2)
        df.to_csv('output\Output_Joint_Probability_Table.csv', index=True)
    #

    """
    Calculates, displays, and exports the CONDITIONAL PROBABILITIES
    Condition probability: The likelyhood that condition 1 will occur given condition 2 occurs
    Conition 2 is the given probability
    """
    
    #Calulates the conditional probaility of two conditions (that the user gives) and generates a table
    def calculate_conditional_probability_table(self, column1, column2):
        joint_counts = self.calculate_joint_counts_table(column1, column2)
        return (joint_counts.div(joint_counts.sum(axis=0), axis=1))
    #

    #Prints the conditional probaility of two columns (that the user gives) as a table
    def display_conditional_probability_table(self, column1, column2):
        print(self.calculate_conditional_probability_table(column1, column2))
    #

    #Exports the conditional probability of two columns (that the user gives) to a TODO
    def export_conditional_probability_table(self, column1, column2):
        df = self.calculate_conditional_probability_table(column1, column2)
        df.to_csv('output\Output_Conditional_Probability_Table.csv', index=True)
    #

    """
    Calculates, displays, and exports the MEAN, MEDIAN, and MODE
    Mean: TODO
    Median: TODO
    Mode: TODO
    """

    #Calculate the mean, median, and mode
    def calculate_mean(self, column):
        return self.pickleFile[column].mean()
    #

    def calculate_median(self, column):
        return self.pickleFile[column].median()
    #

    def calculate_mode(self, column):
        return self.pickleFile[column].mode()
    #

    #Display the mean, median, and mode
    def display_mean(self, column):
        print(self.calculate_mean(column))
    #

    def display_median(self, column):
        print(self.calculate_median(column))
    #
    def display_mode(self, column):
        print(self.calculate_mode(column))
    #

    #Export the mean, median, and mode
    def export_mean(self, column):
        mean = self.calculate_mean(column)
        with open(f"output\Output_{column}_Mean.txt", 'w') as f:
            f.write(str(mean))
        #
    #

    def export_median(self, column):
        median = self.calculate_median(column)
        with open(f"output\Output_{column}_Median.txt", 'w') as f:
            f.write(str(median))
        #
    #

    def export_mode(self, column):
        mode = self.calculate_mode(column)
        with open(f"output\Output_{column}_Mode.txt", 'w') as f:
            f.write(str(mode))
        #
    #

    """
    Calculates, displays, and exports the POSITION VECTOR
    Position vector: TODO
    """

    def calculate_position_vector(self, x, y):
        """Return position vector as a NumPy array."""
        return np.array([x, y])
    #

    def display_position_vector(self, x, y):
        print(f"Array: {self.calculate_position_vector(x, y)}")
    #

    def export_position_vector(self, x, y):
        position_vector = self.calculate_position_vector(x, y)
        np.save('output\Output_Position_Vector.npy', position_vector)
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

    """
    Takes in the column that you want the data from and returns it as a set
    """
    def get_unique_values(self, column):
        #Returns the data as a set (basically a list without repeats)
        return set(self.pickleFile[column].tolist())
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
