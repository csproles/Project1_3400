
import pandas as pd
import numpy as np
from config import CONFIG

class ParentClass2:
    def __init__(self, file_path=None):
        """Initialize data and configuration."""
        self.file_path = file_path or CONFIG.get("PICKLE_PATH", None)
        self.data = None

    def load_data(self):
        """To be implemented by the child class."""
        raise NotImplementedError("load_data() must be implemented in the child class.")

    def calculate_joint_counts(self, col1, col2):
        """Return joint counts for two categorical columns."""
        if self.data is None:
            raise ValueError("No data loaded.")
        return pd.crosstab(self.data[col1], self.data[col2])

    def calculate_joint_probabilities(self, col1, col2):
        """Return joint probabilities."""
        joint_counts = self.calculate_joint_counts(col1, col2)
        return joint_counts / joint_counts.values.sum()

    def calculate_conditional_probabilities(self, col1, col2):
        """Return conditional probabilities P(col1 | col2)."""
        joint = self.calculate_joint_counts(col1, col2)
        return joint.div(joint.sum(axis=0), axis=1)

    def calculate_summary_stats(self, column):
        """Compute mean, median, and mode of a numeric column."""
        if self.data is None:
            raise ValueError("No data loaded.")
        return {
            "mean": self.data[column].mean(),
            "median": self.data[column].median(),
            "mode": self.data[column].mode().iloc[0],
        }

    def get_position_vector(self, x, y):
        """Return position vector as a NumPy array."""
        return np.array([x, y])

    def get_unit_vector(self, vector):
        """Return unit vector."""
        magnitude = np.linalg.norm(vector)
        return vector / magnitude if magnitude != 0 else np.zeros_like(vector)

    def calculate_dot_product(self, vec1, vec2):
        """Return dot product and angle in degrees."""
        dot = np.dot(vec1, vec2)
        angle = np.degrees(
            np.arccos(dot / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
        )
        return {"dot_product": dot, "angle_deg": angle}

    def check_orthogonality(self, vec1, vec2, tol=1e-10):
        """Check if two vectors are orthogonal."""
        return abs(np.dot(vec1, vec2)) < tol
