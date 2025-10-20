import pandas as pd
import numpy as np
from .parent_class import ParentClass

class BabyNamesPickle(ParentClass):
    def load_data(self):
        """Read Pickle data."""
        self.data = pd.read_pickle(self.file_path)

    def calculate_probabilities(self):
        """Compute joint and conditional probabilities."""
        pass

    def vector_operations(self, vec1, vec2):
        """Perform dot product, projection, and angle calculations."""
        pass

    def get_unique_values(self, column):
        pass

    def generate_permutations(self, column):
        pass

    def generate_combinations(self, column):
        pass
