import pandas as pd
import numpy as np

"""
from parent_class import ParentClass
"""
#ParentClass
class PickleChild:

    """
    Takes data from the Spotify Top 100 csv file and makes a pkl file containing the same information
    """
    def load_data():
        #File path for the pkl file
        pkl_file_path = "Input\SpotifyTop100.pkl"

        #File path of the csv file
        csv_file_path = "Input\SpotifyTop100.csv"
        #Creates a data fram with the csv file
        df = pd.read_csv(csv_file_path)

        #Converts that data frame into a pickle file
        df.to_pickle(pkl_file_path)
        pickle = pd.read_pickle(pkl_file_path)


        print(pickle)

        #self.data = pd.read_pickle(self.file_path)

    def calculate_probabilities(self):
        """Compute joint and conditional probabilities."""
        # pass

    def vector_operations(self, vec1, vec2):
        """Perform dot product, projection, and angle calculations."""
        # pass

    def get_unique_values(self, column):
        """Return unique values from a categorical column."""
        # pass

    def generate_permutations(self, column):
         """Generate permutations of categorical values."""
        # pass

    def generate_combinations(self, column):
        """Generate combinations of categorical values."""
        # pass
