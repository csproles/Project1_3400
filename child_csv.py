import pandas as pd
import seaborn as sns
from .parent_class import ParentClass

class BabyNamesCSV(ParentClass):
    def load_data(self):
        """Read CSV data."""
        self.data = pd.read_csv(self.file_path)

    def plot_violin(self, column):
        pass

    def plot_box(self, column):
        pass

    def plot_scatter(self, x, y):
        pass

    def query_advanced(self, conditions_dict):
        """Use boolean indexing and lambda functions."""
        pass
