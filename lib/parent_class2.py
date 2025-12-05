
import pandas as pd
import numpy as np
from lib.child_csv import childCSV
from lib.child_pickle import PickleChild
from lib.parent_class import ParentClass
from lib.config import CONFIG

class ParentClass2:

    def __init__(self):
        cfg = CONFIG
        #Loads the child CSV analyzer (ParentClass -> childCSV)
        self.__load_child_csv(cfg)
        #Loads the pickle-based analyzer (ParentClass -> PickleChild)
        self.__load_child_plk()
        #Loads the parent analyzer (ParentClass alone)
        self.__load_parent()
    #

    def __load_child_csv(self, cfg):
        #Creates an instance of childCSV and loads its CSV data
        self.analyzer_csv = childCSV(cfg)
        self.analyzer_csv.load_data()
    #
    
    def __load_child_plk(self):
        #Creates an instance of PickleChild and loads its PKL data
        self.analyzer_plk = PickleChild()
        self.analyzer_plk.load_data()
    #

    def __load_parent(self):
        #Creates an instance of ParentClass and loads its CSV data
        self.analyzer_parent = ParentClass()
        self.analyzer_parent.load_data()
    #

    def display_initial_options(self):
        #Displays the first set of options (Run or Debug mode)
        print(
            "Welcome to The Three's 3400 Project\n\n"
            "Options:\n"
            "1-Run Mode\n"
            "2-Debug Mode"
        )
    #

    def display_run_options(self):
        #Run-mode menu for end users (general functionality)
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
    #
    
    def display_debug_options(self):
        #Debug options to test each function individually
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
        #Prints exit text when program ends
        print("PROGRAM EXITED")
    #

    def display_invalid_message(self):
        #Prints message for invalid input
        print("INVALID INPUT ENTERED\n")
    #
