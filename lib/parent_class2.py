
import pandas as pd
import numpy as np
from lib.child_csv import childCSV
from lib.child_pickle import PickleChild
from lib.parent_class import ParentClass
from lib.config import CONFIG

class ParentClass2:

    def __init__(self):
        cfg = CONFIG
        self.__load_child_csv(cfg)
        self.__load_child_plk()
        self.__load_parent()
    #

    def __load_child_csv(self, cfg):
        self.analyzer_csv = childCSV(cfg)
        self.analyzer_csv.load_data()
    #\
    
    def __load_child_plk(self):
        self.analyzer_plk = PickleChild()
        self.analyzer_plk.load_data()
    #

    def __load_parent(self):
        self.analyzer_parent = ParentClass()
        self.analyzer_parent.load_data()
    #

    def display_initial_options(self):
        print("Welcome to The Three's 3400 Project\n\nOptions:\n1-Run Mode\n2-Debug Mode")
    #

    def display_run_options(self):
        print("Options:\n1-Generate Violin Plot\n2-Generate Whisker Plot\n3-Generate Scatter Plot\n4-Artist Search\n5-Generate Dot Product\n6-Generate Projection\n7-Generate Angle Calculations\n8-Generate Histogram\n9-Generate Line Plot\n10-List All Artists\n11-List All Genres\n12List Top 10 Artists\n13-Exit\n")
    #
    
    def display_debug_options(self):
        print("Parent Options:\n1-Generate Histogram\n2-Generate Line Plot\n3-List All Artists\n4-List All Genres\n5List Top 10 Artists")
        print("Child CSV Options:\n6-Generate Violin Plot\n7-Generate Whisker Plot\n8-Generate Scatter Plot\n9-Artist Search")
        print("Child PKL Options:\n10-Display Joint Counts\n11-Export Joint Counts\n12-Display Joint Probability\n13-Export Joint Probability\n14-Display Conditional Probability\n15-Export Conditional Probability\n16-Display Mean\n17-Export Mean\n18-Display Median\n19-Export Median\n20-Display Mode\n21-Export Mode\n22-Display Position Vector\n23-Export Position Vector\n24-Display Unit Vector\n25-Export Unit Vector\n26-Display Projection Vector\n27-Export Projection Vector\n28-Display Dot Product\n29-Check Orthogonality\n30-Display Angle Calculations\n31-Display Permutations\n32-Display Combinations\n33-Obtain Unique Values\n34")
    #

    def display_exit_message(self):
        print("PROGRAM EXITED")
    #

    def display_invalid_message(self):
        print("INVALID INPUT ENTERED\n")
    #

#