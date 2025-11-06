import pandas as pd
from config import CONFIG

class ParentClass:
    def __init__(self, file_path=None):
        self.file_path = file_path or CONFIG["CSV_PATH"]
        self.data = None

    def load_data(self):
        """To be implemented by child classes."""
        #pass

    def basic_query(self, column, condition):
        """Filter data by condition."""
        #pass

    def plot_histogram(self, column):
        """Create histogram."""
        #pass

    def plot_line(self, x_col, y_col):
        """Create line plot."""
        #pass
