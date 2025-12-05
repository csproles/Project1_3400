import pandas as pd
from lib.config import CONFIG
from lib.parent_class2 import ParentClass2

class UserInterface(ParentClass2):

    def start(self):

        self.display_initial_options()
        initial_choice = -1
        
        while(initial_choice != 100):
            initial_choice = int(input("Please Enter Your Selection in number form: "))

            if(initial_choice == 1):
                choice = -1
                while(choice != 100):
                    self.display_run_options()
                    choice = int(input("Please Enter Your Selection in number form: "))


                    if(choice == 1):
                        pass
                    #
                    if(choice == 2):
                        pass
                    #
                    if(choice == 3):
                        pass
                    #
                    if(choice == 4):
                        pass
                    #
                    if(choice == 5):
                        pass
                    #
                    if(choice == 6):
                        pass
                    #
                    if(choice == 7):
                        pass
                    #
                    if(choice == 8):
                        pass
                    #
                    if(choice == 9):
                        pass
                    #
                    if(choice == 10):
                        pass
                    #
                    if(choice == 11):
                        pass
                    #
                    if(choice == 12):
                        pass
                    #
                    if(choice == 100):
                        self.display_exit_message()
                        exit
                    #
                    else:
                        self.display_invalid_message()
                    #
                #
                exit
            #
            if(initial_choice == 2):
                choice = -1
                while(choice != 100):
                    self.display_debug_options()
                    choice = int(input("Please Enter Your Selection in number form: "))

                    #Parent Generate Histogram
                    if(choice == 1):
                        self.analyzer_parent.plot_histogram("year")
                    #
                    #Parent Generate Line Plot
                    if(choice == 2):
                        self.analyzer_parent.plot_line("year", "bpm")
                    #
                    #Parent List All Artists
                    if(choice == 3):
                        self.analyzer_parent.list_all_artists()
                    #
                    #Parent List All Genres
                    if(choice == 4):
                        self.analyzer_parent.list_all_genres()
                    #
                    #Parent List Top 10 Artists
                    if(choice == 5):
                        self.analyzer_parent.top_10_artists()
                    #
                    #Child CSV Generate Violin Plot
                    if(choice == 6):
                        self.analyzer_csv.violin_plot()
                    #
                    #Child CSV Generate Box Whisker Plot
                    if(choice == 7):
                        self.analyzer_csv.box_whisker_year()
                    #
                    #Child CSV Generate Scatter Plot
                    if(choice == 8):
                        self.analyzer_csv.scatter_dance_vs_energy()
                    #
                    #Child CSV Artist Search
                    if(choice == 9):
                        artist_query = input("Enter an artist name to search in childCSV: ")
                        self.analyzer_csv.query_artist_search(artist_query)
                    #
                    #Child PKL Display Joint Counts
                    if(choice == 10):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.display_joint_counts_table(column1, column2)
                    #
                    #Child PKL Export Joint Counts
                    if(choice == 11):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.export_joint_counts_table(column1, column2)
                    #
                    #Child PKL Display Joint Probability
                    if(choice == 12):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.display_joint_probability_table(column1, column2)
                    #
                    #Child PKL Export Joint Probability
                    if(choice == 13):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.export_joint_probability_table(column1, column2)
                    #
                    #Child PKL Display Conditional Probability
                    if(choice == 14):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.display_conditional_probability_table(column1, column2)
                    #
                    #Child PKL Export Conditional Probability
                    if(choice == 15):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.export_conditional_probability_table(column1, column2)
                    #
                    #Child PKL Display Mean
                    if(choice == 16):
                        column = input("Enter the column: ")
                        self.analyzer_plk.display_mean(column)
                    #
                    #Child PKL Export Mean
                    if(choice == 17):
                        column = input("Enter the column: ")
                        self.analyzer_plk.export_mean(column)
                    #
                    #Child PKL Display Median
                    if(choice == 18):
                        column = input("Enter the column: ")
                        self.analyzer_plk.display_median(column)
                    #
                    #Child PKL Export Median
                    if(choice == 19):
                        column = input("Enter the column: ")
                        self.analyzer_plk.export_median(column)
                    #
                    #Child PKL Display Mode
                    if(choice == 20):
                        column = input("Enter the column: ")
                        self.analyzer_plk.display_mode(column)
                    #
                    #Child PKL Export Mode
                    if(choice == 21):
                        column = input("Enter the column: ")
                        self.analyzer_plk.export_mode(column)
                    #
                    #Child PKL Display Position Vector
                    if(choice == 22):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.display_position_vector(column1, column2)
                    #
                    #Child PKL Export Position Vector
                    if(choice == 23):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.export_position_vector(column1, column2)
                    #
                    #Child PKL Display Unit Vector
                    if(choice == 24):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.display_unit_vector(column1, column2)
                    #
                    #Child PKL Export Unit Vector
                    if(choice == 25):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.export_unit_vector(column1, column2)
                    #
                    #Child PKL Display Projection Vector
                    if(choice == 26):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.display_projection_vector(column1, column2)
                    #
                    #Child PKL Export Projection Vector
                    if(choice == 27):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        self.analyzer_plk.export_projection_vector(column1, column2)
                    #
                    #Child PKL Calculate Dot Product
                    if(choice == 28):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        print(self.analyzer_plk.calculate_dot_product(column1, column2))
                    #
                    #Child PKL Calculate Orthogonality
                    if(choice == 29):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        print(self.analyzer_plk.check_orthogonality(column1, column2))
                    #
                    #Child PKL Calculate Angle Calculations
                    if(choice == 30):
                        column1 = input("Enter the first column: ")
                        column2 = input("Enter the second column: ")
                        print(self.analyzer_plk.generate_angle_calculations(column1, column2))
                    #
                    #Child PKL Generate Permutations
                    if(choice == 31):
                        column = input("Enter the column: ")
                        iterable = input("Enter the iterable: ")
                        print(self.analyzer_plk.generate_permutations(column, iterable))
                    #
                    #Child PKL Generate Combinations
                    if(choice == 32):
                        column = input("Enter the column: ")
                        iterable = input("Enter the iterable: ")
                        print(self.analyzer_plk.generate_combinations(column, iterable))
                    #
                    #Child PKL Display Unique Values
                    if(choice == 33):
                        column = input("Enter the column: ")
                        print(self.analyzer_plk.obtain_unique_values(column))
                    #
                    #Exit
                    if(choice == 34):
                        self.display_exit_message()
                        exit
                    #
                    #If invalid input is put
                    else:
                        self.display_invalid_message()
                    #
                #
                exit
            #
            if(initial_choice == 100):
                self.display_exit_message()
                exit
            #
            else:
                self.display_invalid_message()
            #
        #

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