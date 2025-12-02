"""
TODO

filename: parent_class2.py
"""

# project imports 
from lib.child_csv import childCSV
from lib.child_pickle import PickleChild
from lib.parent_class import ParentClass
from lib.config import CONFIG

class ParentClass2:
    """
    Purpose:
        This class demonstrates TODO

    Instance variables:
        self.TODO

    Methods:
        - __load_child_csv
        - __load_child_plk
        - __load_parent
        - display_initial_options
        - display_run_options
        - display_debug_options
        - display_exit_message
        - display_invalid_message
    """

    def __init__(self):
        """
        Purpose:
            Initialize the ParentClass2 and loads the data TODO good?
        INPUT:
            None
        OUTPUT:
            None (initializes instance attributes)
        """
        cfg = CONFIG
        self.__load_child_csv(cfg)
        self.__load_child_plk()
        self.__load_parent()
    #

    def __load_child_csv(self, cfg):
        """
        Purpose:
            Loads the data in the child csv class
        INPUT:
            config
        OUTPUT:
            None
        """
        self.analyzer_csv = childCSV(cfg)
        self.analyzer_csv.load_data()
    #
    
    def __load_child_plk(self):
        """
        Purpose:
            Loads the data in the child pickle class
        INPUT:
            None
        OUTPUT:
            None
        """
        self.analyzer_plk = PickleChild()
        self.analyzer_plk.load_data()
    #

    def __load_parent(self):
        """
        Purpose:
            Loads the data in the parent class
        INPUT:
            None
        OUTPUT:
            None
        """
        self.analyzer_parent = ParentClass()
        self.analyzer_parent.load_data()
    #

    def display_initial_options(self):
        """
        Purpose:
            To display the option to enter debug or run mode
        INPUT:
            None
        OUTPUT:
           Welcome to The Three's 3400 Project

           Options:
           1-Run Mode
           2-Debug Mode
        """
        print("Welcome to The Three's 3400 Project\n\nOptions:\n1-Run Mode\n2-Debug Mode")
    #

    def display_run_options(self):
        """
        Purpose:
            To display all the options in run mode
        INPUT:
            None
        OUTPUT:
            Options:
            1-Generate Violin Plot
            2-Generate Whisker Plot
            3-Generate Scatter Plot\n4-Artist Search
            5-Generate Dot Product\n6-Generate Projection
            7-Generate Angle Calculations\n8-Generate Histogram
            9-Generate Line Plot\n10-List All Artists
            11-List All Genres
            12List Top 10 Artists
            13-Exit
        """
        print("Options:\n1-Generate Violin Plot\n2-Generate Whisker Plot\n3-Generate Scatter Plot\n4-Artist Search\n5-Generate Dot Product\n6-Generate Projection\n7-Generate Angle Calculations\n8-Generate Histogram\n9-Generate Line Plot\n10-List All Artists\n11-List All Genres\n12List Top 10 Artists\n13-Exit\n")
    #
    
    def display_debug_options(self):
        """
        Purpose:
            To display the debug options (all the methods that we have)
        INPUT:
            None
        OUTPUT:
            Parent Options:
            1-Generate Histogram
            2-Generate Line Plot
            3-List All Artists
            4-List All Genres
            5-List Top 10 Artists
            Child CSV Options:
            6-Generate Violin Plot
            7-Generate Whisker Plot
            8-Generate Scatter Plot
            9-Artist Search
            Child PKL Options:
            10-Display Joint Counts
            11-Export Joint Counts
            12-Display Joint Probability
            13-Export Joint Probability
            14-Display Conditional Probability
            15-Export Conditional Probability
            16-Display Mean
            17-Export Mean
            18-Display Median
            19-Export Median
            20-Display Mode
            21-Export Mode
            22-Display Position Vector
            23-Export Position Vector
            24-Display Unit Vector
            25-Export Unit Vector
            26-Display Projection Vector
            27-Export Projection Vector
            28-Display Dot Product
            29-Check Orthogonality
            30-Display Angle Calculations
            31-Display Permutations
            32-Display Combinations
            33-Obtain Unique Values
            34-Exit")
        """
        print("Parent Options:\n1-Generate Histogram\n2-Generate Line Plot\n3-List All Artists\n4-List All Genres\n5-List Top 10 Artists")
        print("Child CSV Options:\n6-Generate Violin Plot\n7-Generate Whisker Plot\n8-Generate Scatter Plot\n9-Artist Search")
        print("Child PKL Options:\n10-Display Joint Counts\n11-Export Joint Counts\n12-Display Joint Probability\n13-Export Joint Probability\n14-Display Conditional Probability\n15-Export Conditional Probability\n16-Display Mean\n17-Export Mean\n18-Display Median\n19-Export Median\n20-Display Mode\n21-Export Mode\n22-Display Position Vector\n23-Export Position Vector\n24-Display Unit Vector\n25-Export Unit Vector\n26-Display Projection Vector\n27-Export Projection Vector\n28-Display Dot Product\n29-Check Orthogonality\n30-Display Angle Calculations\n31-Display Permutations\n32-Display Combinations\n33-Obtain Unique Values\n34")
    #

    def display_exit_message(self):
        """
        Purpose:
            To display the exit message
        INPUT:
            None
        OUTPUT:
            PROGRAM EXITED
        """
        print("PROGRAM EXITED")
    #

    def display_invalid_message(self):
        """
        Purpose:
            To display a message when a input does not meet a possible one
        INPUT:
            None
        OUTPUT:
            INVALID INPUT ENTERED
            
        """
        print("INVALID INPUT ENTERED\n")
    #

#