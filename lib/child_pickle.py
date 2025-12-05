import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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

    def calculate_std(self, column):
        #Calculates the standard deviation of a column
        return self.pickleFile[column].std()

    def display_std(self, column):
        #Displays the standard deviation of a column
        print(self.calculate_std(column))

    def export_std(self, column):
        #Exports the standard deviation to a text file
        std = self.calculate_std(column)
        with open(f"output/Output_{column}_Std.txt", "w") as f:
            f.write(str(std))
    
    """
    Obtains, displays, and exports the POSITION VECTOR
    """

    def obtain_position_vector(self, x, y):
        """Return position vector as a NumPy array."""
        return np.array([float(x), float(y)])
    #

    def display_position_vector(self, x, y):
        print(self.obtain_position_vector(x, y))
    #

    def export_position_vector(self, x, y):
        position_vector = self.obtain_position_vector(x, y)
        np.save('output\Output_Position_Vector.npy', position_vector)
    #

    """
    Obtains, displays, and exports the UNIT VECTOR
    """
    def obtain_unit_vector(self, vector):
        #Converts input list into array and calculates its unit vector
        v = np.array(vector, dtype=float)
        mag = np.linalg.norm(v)
        #If magnitude is zero, return zero-vector
        return v / mag if mag != 0 else np.zeros_like(v)
    #

    def display_unit_vector(self, vector):
        print(self.obtain_unit_vector(vector))
    #

    def export_unit_vector(self, vector):
        unit_vector = self.obtain_unit_vector(vector)
        np.save('output\Output_Unit_Vector.npy', unit_vector)
    #

    """
    Obtains, displays, and exports the PROJECTION VECTOR
    """
    def obtain_projection_vector(self, column1, column2):
        #Makes the columns arrays
        column1_data_arr = np.array(column1)
        column2_data_arr = np.array(column2)

        denom = np.dot(column2_data_arr, column2_data_arr)

        if denom == 0:
            return np.zeros_like(column2_data_arr)

        #Projecting column1 onto column2; Using numpy dot products (dot(a,b) / dot(b,b)) * b 
        projection = (np.dot(column1_data_arr, column2_data_arr) / denom) * column2_data_arr

        #Returns projection
        return projection
    #

    def display_projection_vector(self, column1, column2):
        print(self.obtain_projection_vector(column1, column2))
    #

    def export_projection_vector(self, column1, column2):
        projection = self.obtain_projection_vector(column1, column2)
        np.save('output\Output_Projection_Vector.npy', projection)

    """
    Calculates the DOT PRODUCT
    """
    def calculate_dot_product(self, vec1, vec2):
        #Converts both inputs to numpy arrays for reliability
        vec1 = np.array(vec1, dtype = float)
        vec2 = np.array(vec2, dtype = float)
        """Return dot product and angle in degrees."""
        #Computes dot product using numpy
        dot = np.dot(vec1, vec2)
        #Denominator for angle calculation
        denom = np.linalg.norm(vec1) * np.linalg.norm(vec2)

        #If zero-vector present, angle is undefined
        if denom == 0:
            angle = np.nan
        else:
            cosθ = dot / denom
            #Avoid rounding issues using clipping
            cosθ = np.clip(cosθ, -1.0, 1.0)
            #Angle in degrees
            angle = np.degrees(np.arccos(cosθ))
    
        #Returns both values together
        return {"dot_product": dot, "angle_deg": angle}
    #

    """
    Checks the ORTHOGONALITY
    """
    def check_orthogonality(self, vec1, vec2, tol=1e-10):
        #Converts inputs to numeric arrays
        v1 = np.array(vec1, dtype=float)
        v2 = np.array(vec2, dtype=float)
        #Two vectors are orthogonal if their dot product is nearly zero
        return abs(np.dot(v1, v2)) < tol
    #

    """
    Generates the angle calculation of 2 columns
    ONLY WORKS FOR NUMERICAL COLUMNS
    """
    def generate_angle_calculations(self, column1, column2):
        #Makes the columns arrays
        column1_data_arr = np.array(column1)
        column2_data_arr = np.array(column2)
        
        #Getting the dot then divinding it by the magnitudes
        denom = np.linalg.norm(column1_data_arr) * np.linalg.norm(column2_data_arr)

        if denom == 0:
            return np.nan

        cos_of_columns = np.dot(column1_data_arr, column2_data_arr) / denom

        #Avoids rounding errors
        cos_of_columns = np.clip(cos_of_columns, -1.0, 1.0)

        #Makes the calculation to degrees using numpy
        calculate_angle = np.degrees(np.arccos(cos_of_columns))

        #Returns the angle
        return calculate_angle

    """
    Makes a DataFrame of all permutations from the unique values of a column.
    Each row represents one permutation of length 'iterable'.
    Each column in the resulting DataFrame corresponds to the position inside the permutation.
    """
    def generate_permutations(self, column, iterable):
        #Makes a sorted set of all the values in a column
        column_data = sorted(self.obtain_unique_values(column))

        # FIX: convert iterable to int
        r = int(iterable)

        #Uses itertools to generate all the permutations of the column
        all_column_permutations = list(itertools.permutations(column_data, r))

        #Puts all the permutations into a data frame
        df_all_column_permutations = pd.DataFrame(all_column_permutations)

        #Returns the data frame
        return df_all_column_permutations
    #

    """
    Makes a DataFrame of all combinations from the unique values of a column.
    Each row represents one combination of length 'iterable'.
    Each column in the resulting DataFrame corresponds to the position inside the combination.
    """
    def generate_combinations(self, column, iterable):
        #Makes a sorted set of all the values in a column
        column_data = sorted(self.obtain_unique_values(column))

        # FIX: convert iterable to int
        r = int(iterable)

        #Uses itertools to generate all the combinations of the column
        all_column_combinations = list(itertools.combinations(column_data, r))

        #Puts all the cominations into a data frame
        df_all_column_combinations = pd.DataFrame(all_column_combinations)

        #Returns the data frame
        return df_all_column_combinations
    #

    """
    Returns all unique, non-null values from the selected column as a sorted list.
    This serves as the input base for generating permutations and combinati
    """
    def obtain_unique_values(self, column):
        #Returns the data as a set (basically a list without repeats)
        return sorted(set(self.pickleFile[column].dropna().tolist()))
