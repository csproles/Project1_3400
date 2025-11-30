import pandas as pd
from lib.config import CONFIG
from lib.parent_class import ParentClass
from lib.child_csv import childCSV
from lib.child_pickle import PickleChild

class UserInterface:
    def __init__(self):
        cfg = CONFIG
        # ----------- Child CSV Testing -----------
        self.analyzer_csv = childCSV(cfg)
        self.analyzer_csv.load_data()

        # ----------- PickleChild Testing -----------
        self.pickle_child = PickleChild()
        self.pickle_child.load_data()

        # ----------- ParentClass Testing -----------
        self.analyzer_parent = ParentClass()
        self.analyzer_parent.load_data()
    #

    def start(self):
        print("Welcome to The Three's 3400 Project\n\nOptions:\n1-Generate Violin Plot\n2-Generate Whisker Plot\n3-Generate Scatter Plot\n4-Artist Search\n5-Generate Dot Product\n6-Generate Projection\n7-Generate Angle Calculations\n8-Generate Histogram\n9-Generate Line Plot\n10-List All Artists\n11-List All Genres\n12List Top 10 Artists\n13-Exit\n")
        choice = -1
        
        #self.pickle_child.display_joint_counts_table("year", "artist")
        #self.pickle_child.export_joint_counts_table("year", "artist")
        self.pickle_child.display_position_vector("bpm", "dnce")
        self.pickle_child.export_position_vector("bpm", "dnce")
        print("\n\n\n\n")
        #self.pickle_child.display_joint_probability_table("year", "artist")
        #self.pickle_child.export_joint_probability_table("year", "artist")
        

        # while(choice != 13):
        #     choice = int(input("Please Enter Your Selection in number form: "))

        #     if(choice == 1):
        #         self.analyzer_csv.violin_plot()
        #     #
        #     if(choice == 2):
        #         self.analyzer_csv.box_whisker_year()
        #     #
        #     if(choice == 3):
        #         self.analyzer_csv.scatter_dance_vs_energy()
        #     #
        #     if(choice == 4):
        #         artist_query = input("Enter an artist name to search in childCSV: ")
        #         self.analyzer_csv.query_artist_search(artist_query)
        #     #
        #     if(choice == 5):
        #         column1 = input("Enter the first column: ")
        #         column2 = input("Enter the second column: ")
        #         self.pickle_child.generate_dot_product(column1, column2)
        #     #
        #     if(choice == 6):
        #         column1 = input("Enter the first column: ")
        #         column2 = input("Enter the second column: ")
        #         self.pickle_child.generate_projection(column1, column2)
        #     #
        #     if(choice == 7):
        #         column1 = input("Enter the first column: ")
        #         column2 = input("Enter the second column: ")
        #         self.pickle_child.generate_angle_calculations(column1, column2)
        #     #
        #     if(choice == 8):
        #         self.analyzer_parent.plot_histogram("year")
        #     #
        #     if(choice == 9):
        #         self.analyzer_parent.plot_line("year", "bpm")
        #     #
        #     if(choice == 10):
        #         self.analyzer_parent.list_all_artists()
        #     #
        #     if(choice == 11):
        #         self.analyzer_parent.list_all_genres()
        #     #
        #     if(choice == 12):
        #         self.analyzer_parent.top_10_artists()
        #     #
        #     if(choice == 13):
        #         exit
        #     #
        #     else:
        #         print("INVALID INPUT")
        #     #
        # #
    #
#