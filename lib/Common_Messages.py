"""
TODO

filename: parent_class2.py
"""

# project imports 
from Spotify_CSV_Handler import Spotify_CSV_Handler
from Spotify_PKL_Handler import Spotify_PKL_Handler
from Spotify_Data_Handler import Spotify_Data_Handler
from lib.config import CONFIG

class Common_Messages:
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
        self.analyzer_csv = Spotify_CSV_Handler(cfg)
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
        self.analyzer_plk = Spotify_PKL_Handler()
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
        self.analyzer_parent = Spotify_Data_Handler()
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
        print(
            "Welcome to The Three's 3400 Project\n\n"
            "Options:\n"
            "1-Run Mode\n"
            "2-Debug Mode"
        )
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
        print(
            "Options:\n"
            "1-Generate Violin Plot\n"
            "2-Generate Whisker Plot\n"
            "3-Generate Scatter Plot\n"
            "4-Artist Search\n"
            "5-Generate Dot Product\n"
            "6-Generate Projection\n"
            "7-Generate Angle Calculations\n"
            "8-Generate Histogram\n"
            "9-Generate Line Plot\n"
            "10-List All Artists\n"
            "11-List All Genres\n"
            "12-List Top 10 Artists\n"
            "13-Exit\n"
        )
    
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
        print(
            "Parent Options:\n"
            "1-Generate Histogram\n"
            "2-Generate Line Plot\n"
            "3-List All Artists\n"
            "4-List All Genres\n"
            "5-List Top 10 Artists")
        
        print(
            "Child CSV Options:\n"
            "6-Generate Violin Plot\n"
            "7-Generate Whisker Plot\n"
            "8-Generate Scatter Plot\n"
            "9-Artist Search"
        )

        print(
            "Child PKL Options:\n"
            "10-Display Joint Counts\n"
            "11-Export Joint Counts\n"
            "12-Display Joint Probability\n"
            "13-Export Joint Probability\n"
            "14-Display Conditional Probability\n"
            "15-Export Conditional Probability\n"
            "16-Display Mean\n"
            "17-Export Mean\n"
            "18-Display Median\n"
            "19-Export Median\n"
            "20-Display Mode\n"
            "21-Export Mode\n"
            "22-Display Position Vector\n"
            "23-Export Position Vector\n"
            "24-Display Unit Vector\n"
            "25-Export Unit Vector\n"
            "26-Display Projection Vector\n"
            "27-Export Projection Vector\n"
            "28-Display Dot Product\n"
            "29-Check Orthogonality\n"
            "30-Display Angle Calculations\n"
            "31-Display Permutations\n"
            "32-Display Combinations\n"
            "33-Obtain Unique Values\n"
            "34-Exit Debug Mode"
        )
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