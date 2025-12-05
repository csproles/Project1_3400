"""
data manager for TODO

filename: child_pickle.py
"""


# external imports alphabetically
import itertools
import numpy as np
import pandas as pd
# project imports 
from lib.config import CONFIG
from lib.Spotify_Data_Handler import Spotify_Data_Handler_Class

class Spotify_PKL_Handler_Class(Spotify_Data_Handler_Class):
    """
    Purpose:
        This class demonstrates file handling, processing, and
        data analysis using pandas, numpy, and itertools 

    Instance variables:
        self. TODO

    Methods:
        - load_data
        - calculate_joint_counts_table
        - display_joint_counts_table
        - export_joint_counts_table
        - calculate_joint_probability_table
        - display_joint_probability_table
        - export_joint_probability_table
        - calculate_conditional_probability_table
        - display_conditional_probability_table
        - export_conditional_probability_table
        - calculate_mean
        - calculate_median
        - calculate_mode
        - display_mean
        - display_median
        - display_mode
        - export_mean
        - export_median
        - export_mode
        - obtain_position_vector
        - display_position_vector
        - export_position_vector
        - obtain_unit_vector
        - display_unit_vector
        - export_unit_vector
        - obtain_projection_vector
        - display_projection_vector
        - export_projection_vector
        - calculate_dot_product
        - check_orthogonality
        - generate_angle_calculations
        - generate_permutations
        - generate_combinations
        - obtain_unique_values
    """

    def __init__(self, config=CONFIG):
        """
        Purpose:
            Initialize the PickleChild instance with configuration values.
        INPUT:
            config
        OUTPUT:
            None
        """
        super().__init__(config)
        self.pickleFile = None
    #
    
    def load_data(self):
        """
        Purpose:
            Load PKL file to a configured file path using the data from the Spotify Top 100 csv file
        INPUT:
            None
        OUTPUT:
            None
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

    def calculate_joint_counts_table(self, column1, column2):
        """
        Purpose:
            Calulates the joint count of two columns (that the user gives) and makes a table (data frame)
            Joint Counts definition: The frequencies of occurrences for combinations of two or more variables
            Can take Quantative and Qualitative Data
        INPUT:
            column1 (str) : the first column in the joint counts table (MUST BE EXACT SPELLING)
            column2 (str) : the second column in the joint counts table (MUST BE EXACT SPELLING)
        OUTPUT:
            Data frame
        """
        return (pd.crosstab(index=self.pickleFile[column1], columns=self.pickleFile[column2], margins=True, normalize=True) * 100)
    #

    def display_joint_counts_table(self, column1, column2):
        """
        Purpose:
            Prints the joint count of two columns (that the user gives) as a table (data frame)
            Joint Counts definition: The frequencies of occurrences for combinations of two or more variables
            Can take Quantative and Qualitative Data
        INPUT:
            column1 (str) : the first column in the joint counts table (MUST BE EXACT SPELLING)
            column2 (str) : the second column in the joint counts table (MUST BE EXACT SPELLING)
        OUTPUT:
            SAMPLE: (will vary based on the data input)
                a1  a2  a3 All
            b1  #   #   #   #
            b2  #   #   #   #
            All #   #   #   #
        """
        print(self.calculate_joint_counts_table(column1, column2))
    #

    def export_joint_counts_table(self, column1, column2):
        """
        Purpose:
            Exports the joint count of two columns (that the user gives) to a csv file
            Joint Counts definition: The frequencies of occurrences for combinations of two or more variables
            Can take Quantative and Qualitative Data
        INPUT:
            column1 (str) : the first column in the joint counts table (MUST BE EXACT SPELLING)
            column2 (str) : the second column in the joint counts table (MUST BE EXACT SPELLING)
        OUTPUT:
            A csv file
        """
        df = self.calculate_joint_counts_table(column1, column2)
        df.to_csv('output\Output_Joint_Counts_Table.csv', index=True)
    #
    
    def calculate_joint_probability_table(self, column1, column2):
        """
        Purpose:
            Calulates the joint probability of two columns (that the user gives) and makes a table (data frame)
            Joint Probability definition: The likelyhood that condition 1 will occur WITH condition 2
            Can take Quantative and Qualitative Data
        INPUT:
            column1 (str) : the first column in the joint probability table (MUST BE EXACT SPELLING)
            column2 (str) : the second column in the joint probability table (MUST BE EXACT SPELLING)
        OUTPUT:
            Data frame
        """
        joint_counts = self.calculate_joint_counts_table(column1, column2)
        return (joint_counts / joint_counts.values.sum())
    #

    def display_joint_probability_table(self, column1, column2):
        """
        Purpose:
            Prints the joint probability of two columns (that the user gives) as a table
            Joint Probability definition: The likelyhood that condition 1 will occur WITH condition 2
            Can take Quantative and Qualitative Data
        INPUT:
            column1 (str) : the first column in the joint probability table (MUST BE EXACT SPELLING)
            column2 (str) : the second column in the joint probability table (MUST BE EXACT SPELLING)
        OUTPUT:
            SAMPLE: (will vary based on the data input)
                a1  a2  a3 All
            b1  #   #   #   #
            b2  #   #   #   #
            All #   #   #   #
        """
        print(self.calculate_joint_probability_table(column1, column2))
    #

    def export_joint_probability_table(self, column1, column2):
        """
        Purpose:
            Exports the joint probability of two columns (that the user gives) to a csv file
            Joint Probability definition: The likelyhood that condition 1 will occur WITH condition 2
            Can take Quantative and Qualitative Data
        INPUT:
            column1 (str) : the first column in the joint probability table (MUST BE EXACT SPELLING)
            column2 (str) : the second column in the joint probability table (MUST BE EXACT SPELLING)
        OUTPUT:
            csv file
        """
        df = self.calculate_joint_probability_table(column1, column2)
        df.to_csv('output\Output_Joint_Probability_Table.csv', index=True)
    #
   
    def calculate_conditional_probability_table(self, column1, column2):
        """
        Purpose:
            Calulates the conditional probaility of two conditions (that the user gives) and generates a table (data frame)
            Condition probability definition: The likelyhood that condition 1 will occur given condition 2 occurs
            Conition 2 is the given probability
            Can take Quantative and Qualitative Data
        INPUT:
            column1 (str) : the first column in the conditional probability table (MUST BE EXACT SPELLING)
            column2 (str) : the second column in the conditional probability table (MUST BE EXACT SPELLING)
        OUTPUT:
            Data frame
        """
        joint_counts = self.calculate_joint_counts_table(column1, column2)
        return (joint_counts.div(joint_counts.sum(axis=0), axis=1))
    #

    def display_conditional_probability_table(self, column1, column2):
        """
        Purpose:
            Prints the conditional probaility of two columns (that the user gives) as a table (data frame)
            Condition probability definition: The likelyhood that condition 1 will occur given condition 2 occurs
            Conition 2 is the given probability
            Can take Quantative and Qualitative Data
        INPUT:
            column1 (str) : the first column in the conditional probability table (MUST BE EXACT SPELLING)
            column2 (str) : the second column in the conditional probability table (MUST BE EXACT SPELLING)
        OUTPUT:
            SAMPLE: (will vary based on the data input)
                a1  a2  a3 All
            b1  #   #   #   #
            b2  #   #   #   #
            All #   #   #   #
        """
        print(self.calculate_conditional_probability_table(column1, column2))
    #

    def export_conditional_probability_table(self, column1, column2):
        """
        Purpose:
            Exports the conditional probability of two columns (that the user gives) to a csv file
            Condition probability definition: The likelyhood that condition 1 will occur given condition 2 occurs
            Conition 2 is the given probability
            Can take Quantative and Qualitative Data
        INPUT:
            column1 (str) : the first column in the conditional probability table (MUST BE EXACT SPELLING)
            column2 (str) : the second column in the conditional probability table (MUST BE EXACT SPELLING)
        OUTPUT:
            A csv file
        """
        df = self.calculate_conditional_probability_table(column1, column2)
        df.to_csv('output\Output_Conditional_Probability_Table.csv', index=True)
    #

    #Calculate the mean, median, and mode
    def calculate_mean(self, column):
        """
        Purpose:
            To calculate the mean of a column
            Mean Definition: The average of a set of numbers
            Can take Quantative Data
        INPUT:
            column (str) : the column whose mean will be calculated (must contain numerical data)
        OUTPUT:
            A float
        """
        return self.pickleFile[column].mean()
    #

    def calculate_median(self, column):
        """
        Purpose:
            To calculate the median of a column
            Mean Definition: The middle value of a dataset when it is arranged in order from smallest to largest
            Can take Quantative Data
        INPUT:
            column (str) : the column whose median will be calculated (must contain numerical data)
        OUTPUT:
            A float
        """
        return self.pickleFile[column].median()
    #

    def calculate_mode(self, column):
        """
        Purpose:
            To calculate the mode of a column
            Mean Definition: The value that appears most frequently in a data set
            Can take Quantative Data
        INPUT:
            column (str) : the column whose mode will be calculated (must contain numerical data)
        OUTPUT:
            A float
        """
        return self.pickleFile[column].mode()
    #

    def display_mean(self, column):
        """
        Purpose:
            To display the mean of a column
            Mean Definition: The average of a set of numbers
            Can take Quantative Data
        INPUT:
            column (str) : the column whose mean will be calculated (must contain numerical data)
        OUTPUT:
            #
        """
        print(self.calculate_mean(column))
    #

    def display_median(self, column):
        """
        Purpose:
            To display the median of a column
            Mean Definition: The middle value of a dataset when it is arranged in order from smallest to largest
            Can take Quantative Data
        INPUT:
            column (str) : the column whose median will be calculated (must contain numerical data)
        OUTPUT:
            #
        """
        print(self.calculate_median(column))
    #
    def display_mode(self, column):
        """
        Purpose:
            To display the mode of a column
            Mean Definition: The value that appears most frequently in a data set
            Can take Quantative Data
        INPUT:
            column (str) : the column whose mode will be calculated (must contain numerical data)
        OUTPUT:
            #
        """
        print(self.calculate_mode(column))
    #

    #Export the mean, median, and mode
    def export_mean(self, column):
        """
        Purpose:
            To export the mean of a column to a txt file
            Mean Definition: The average of a set of numbers
            Can take Quantative Data
        INPUT:
            column (str) : the column whose mean will be calculated (must contain numerical data)
        OUTPUT:
            A txt file
        """
        mean = self.calculate_mean(column)
        with open(f"output\Output_{column}_Mean.txt", 'w') as f:
            f.write(str(mean))
        #
    #

    def export_median(self, column):
        """
        Purpose:
            To export the median of a column to a txt file
            Mean Definition: The middle value of a dataset when it is arranged in order from smallest to largest
            Can take Quantative Data
        INPUT:
            column (str) : the column whose median will be calculated (must contain numerical data)
        OUTPUT:
            A txt file
        """
        median = self.calculate_median(column)
        with open(f"output\Output_{column}_Median.txt", 'w') as f:
            f.write(str(median))
        #
    #

    def export_mode(self, column):
        """
        Purpose:
            To export the mode of a column to a txt file
            Mean Definition: The value that appears most frequently in a data set
            Can take Quantative Data
        INPUT:
            column (str) : the column whose mode will be calculated (must contain numerical data)
        OUTPUT:
            A txt file
        """
        mode = self.calculate_mode(column)
        with open(f"output\Output_{column}_Mode.txt", 'w') as f:
            f.write(str(mode))
        #
    #

    def obtain_position_vector(self, x, y):
        """
        Purpose:
            To calculate the position vector of TODO what does this want???
            Position vector definition: A vector that shows the location of a point in space relative to a fixed origin
            TODO takes what type of data?????
        INPUT:
            x (TODO) : TODO
            y (TODO) : TODO
        OUTPUT:
            numpy array
        """
        return np.array([x, y])
    #

    def display_position_vector(self, x, y):
        """
        Purpose:
            To display the position vector of TODO what does this want???
            Position vector definition: A vector that shows the location of a point in space relative to a fixed origin
            TODO takes what type of data?????
        INPUT:
            x (TODO) : TODO
            y (TODO) : TODO
        OUTPUT:
            SAMPLE: (will vary based on the data input)
            [#, #, #]
        """
        print(self.obtain_position_vector(x, y))
    #

    def export_position_vector(self, x, y):
        """
        Purpose:
            To export the position vector of TODO what does this want??? to a file
            Position vector definition: A vector that shows the location of a point in space relative to a fixed origin
            TODO takes what type of data?????
        INPUT:
            x (TODO) : TODO
            y (TODO) : TODO
        OUTPUT:
            A npy file
        """
        position_vector = self.obtain_position_vector(x, y)
        np.save('output\Output_Position_Vector.npy', position_vector)
    #

    def obtain_unit_vector(self, vector):
        """
        Purpose:
            To calculate the unit vector of TODO what does this want???
            Unit vector definition: A vector with a magnitude of exactly one, which is used to represent direction without any influence from magnitude. Conceptually, it's a "pure" direction
            TODO takes what type of data?????
        INPUT:
            vector (TODO) : TODO
        OUTPUT:
            numpy array
        """
        magnitude = np.linalg.norm(vector)
        if magnitude == 0:
            return np.zeros_like(vector)
        return vector / magnitude
    #

    def display_unit_vector(self, vector):
        """
        Purpose:
            To display the unit vector of TODO what does this want???
            Unit vector definition: A vector with a magnitude of exactly one, which is used to represent direction without any influence from magnitude. Conceptually, it's a "pure" direction
            TODO takes what type of data?????
        INPUT:
            vector (TODO) : TODO
        OUTPUT:
            SAMPLE: (will vary based on the data input)
            [#, #, #]
        """
        print(self.obtain_unit_vector(vector))
    #

    def export_unit_vector(self, vector):
        """
        Purpose:
            To export the unit vector of TODO what does this want??? to a file
            Unit vector definition: A vector with a magnitude of exactly one, which is used to represent direction without any influence from magnitude. Conceptually, it's a "pure" direction
            TODO takes what type of data?????
        INPUT:
            vector (TODO) : TODO
        OUTPUT:
            A npy file
        """
        unit_vector = self.obtain_unit_vector(vector)
        np.save('output\Output_Unit_Vector.npy', unit_vector)
    #

    def obtain_projection_vector(self, column1, column2):
        """
        Purpose:
            To calculate the projection vector of TODO what does this want???
            Projection vector definition: The "shadow" a vector casts on another vector, as if a light were shining from above
            TODO takes what type of data?????
        INPUT:
           TODO
        OUTPUT:
            numpy array
        """
        #Makes the columns arrays
        column1_data_arr = np.array(column1)
        column2_data_arr = np.array(column2)

        denom = np.dot(column1_data_arr, column2_data_arr)

        if denom == 0:
            return np.zeros_like(column2_data_arr)

        #Projecting column1 onto column2; Using numpy dot products (dot(a,b) / dot(b,b)) * b 
        projection = (np.dot(column1_data_arr, column2_data_arr) / denom) * column2_data_arr

        #Returns projection
        return projection
    #

    def display_projection_vector(self, column1, column2):
        """
        Purpose:
            To display the projection vector of TODO what does this want???
            Projection vector definition: The "shadow" a vector casts on another vector, as if a light were shining from above
            TODO takes what type of data?????
        INPUT:
           TODO
        OUTPUT:
            SAMPLE: (will vary based on the data input)
            [#, #, #]
        """
        print(self.obtain_projection_vector(column1, column2))
    #

    def export_projection_vector(self, column1, column2):
        """
        Purpose:
            To export the projection vector of TODO what does this want??? to a file
            Projection vector definition: The "shadow" a vector casts on another vector, as if a light were shining from above
            TODO takes what type of data?????
        INPUT:
           TODO
        OUTPUT:
            A npy file
        """
        projection = self.obtain_position_vector(column1, column2)
        np.save('output\Output_Projection_Vector.npy', projection)
    #

    def calculate_dot_product(self, vec1, vec2):
        """
        Purpose:
            To calculate the dot product of TODO what does this take????
            Dot product definition: Measures the extent to which two vectors are aligned.
            TODO takes what type of data?????
        INPUT:
           TODO
        OUTPUT:
            dot product and angle in degrees
        """
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        """Return dot product and angle in degrees."""
        dot = np.dot(vec1, vec2)
        denom = np.linalg.norm(vec1) * np.linalg.norm(vec2)

        if denom == 0:
            angle = np.nan
        else:
            cosθ = dot / denom
            cosθ = np.clip(cosθ, -1.0, 1.0)
            angle = np.degrees(np.arccos(cosθ))
    
        return {"dot_product": dot, "angle_deg": angle}
    #

    """
    Checks the ORTHOGONALITY
    Orthogonality: TODO
    TODO CHECKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
    """
    def check_orthogonality(self, vec1, vec2, tol=1e-10):
        """
        Purpose:
            Checks if two vectors are orthogonal
            Orthofonality definition: Means that two or more things are at a right angle (90°) to each other, like the x and y axes in a coordinate plane
            TODO takes what type of data?????
        INPUT:
           TODO
        OUTPUT:
           bool
        """
        return abs(np.dot(vec1, vec2)) < tol
    #

    """
    Generates the angle calculation of 2 columns
    ONLY WORKS FOR NUMERICAL COLUMNS
    """
    def generate_angle_calculations(self, column1, column2):
        """
        Purpose:
            Generates the angle calculation of 2 columns
            Angle calculations definition: The angle between two non-zero vectors is defined using the dot product and their magnitudes
            Can take Quantative Data
        INPUT:
           column1 (str)
           column2 (str)
        OUTPUT:
           float
        """
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

    def generate_permutations(self, column):
        """
        Purpose:
            Makes a data frame full of all the permutations of a given column
            Permutation: All possible orders of a column given an iterable
            WARNING: CAN BE A LOT FOR YOUR COMPUTER - IT CRASHED MINE BUT I KNOW IT WORKS CAUSE ITS PERFECT FOR THE COLUMNS WITH VERY FEW VALUES (YEAR)
            Takes Quantative and Qualatative data
        INPUT:
           column (str)
        OUTPUT:
           a data frame
        """
        #Makes a sorted set of all the values in a column
        column_data = sorted(self.obtain_unique_values(column))

        #Uses itertools to generate all the permutations of the column
        all_column_permutations = list(itertools.permutations(column_data))

        #Puts all the permutations into a data frame
        df_all_column_permutations = pd.DataFrame(all_column_permutations)

        #Returns the data frame
        return df_all_column_permutations
    #

    def generate_combinations(self, column, iterable):
        """
        Purpose:
            Makes a data frame full of all the combinations of a given columnn
            Combinations: All possible groups of a column
            Takes Quantative and Qualtative Data
        INPUT:
           column (str)
           iterable (int)
        OUTPUT:
           a data frame
        """
        #Makes a sorted set of all the values in a column
        column_data = sorted(self.obtain_unique_values(column))

        #Uses itertools to generate all the combinations of the column
        all_column_combinations = list(itertools.combinations(column_data, iterable))

        #Puts all the cominations into a data frame
        df_all_column_combinations = pd.DataFrame(all_column_combinations)

        #Returns the data frame
        return df_all_column_combinations
    #

    def obtain_unique_values(self, column):
        """
        Purpose:
            Takes in the column that you want the data from and returns it as a set with only the unique values
            Takes Quantative and Qualtative Data
        INPUT:
           column (str)
        OUTPUT:
           returns the data as a set (basically a list without repeats)
        """
        return set(self.pickleFile[column].tolist())
    #