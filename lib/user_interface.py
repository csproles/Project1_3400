import logging
import pandas as pd
from lib.config import CONFIG
from lib.Common_Messages import Common_Messages_Class
import matplotlib.pyplot as plt
#
class User_Interface_Class(Common_Messages_Class):

    def __init__(self):
        print("Loaded class:", self.__class__.__name__)
        super().__init__()
        logging.basicConfig(
            filename = CONFIG["LOG_FILE"],
            level = logging.INFO,
            format = '%(asctime)s - %(levelname)s - %(message)s'
        )
    #

    def start(self):
        
        while True:
            self.display_initial_options()
            logging.info("Initial Options Displayed")
        
            try:
                initial_choice = int(input("Please Enter Your Selection in number form: "))
            except ValueError:
                logging.error("Invalid Entry Made")
                self.display_invalid_message()
                continue

            if initial_choice == 100:
                logging.info("Program Exited")
                self.display_exit_message()
                exit()

            elif initial_choice == 1:
                logging.info("Run Mode Entered")
                self.run_mode_menu()

            elif initial_choice == 2:
                logging.info("Debug Mode Entered")
                self.debug_mode_menu()

            else:
                logging.error("Invalid Entry Made")
                self.display_invalid_message()
    
    def show_plot(self, func, *args, **kwargs):
        result = func(*args, **kwargs)
        plt.show()
        return result
        
    def run_mode_menu(self):
        run_actions = {
        1: lambda: self.show_plot(self.analyzer_csv.violin_plot),
        2: lambda: self.show_plot(self.analyzer_csv.box_whisker_year),
        3: lambda: self.show_plot(self.analyzer_csv.scatter_dance_vs_energy),
        4: lambda: self.analyzer_csv.query_artist_search(
            input("Enter an artist name to search in childCSV: ")
        ),
        5: lambda: print(self.analyzer_plk.calculate_dot_product(
            input("Enter the first column: "), input("Enter the second column: ")
        )),
        6: lambda: print(self.analyzer_plk.generate_projection(
            input("Enter the first column: "), input("Enter the second column: ")
        )),
        7: lambda: print(self.analyzer_plk.generate_angle_calculations(
            input("Enter the first column: "), input("Enter the second column: ")
        )),
        8: lambda: self.show_plot(self.analyzer_parent.plot_histogram, "year"),
        9: lambda: self.show_plot(self.analyzer_parent.plot_line, "year", "bpm"),
        10: lambda: print("\n".join(self.analyzer_parent.list_all_artists())),
        11: lambda: print("\n".join(self.analyzer_parent.list_all_genres())),
        12: lambda: self.analyzer_parent.top_10_artists(),
        13: lambda: (self.display_exit_message(), exit())
}


        


        while True:
            self.display_run_options()
            try:
                choice = int(input("Please Enter Your Selection in Number Format:"))
            except ValueError:
                self.display_invalid_message()
                continue
            
            action = run_actions.get(choice)
            if action:
                action()
                if choice != 100:
                    input("Press enter to return to run mode menu.")
            else:
                self.display_invalid_message()

# debug submenu
    def debug_mode_menu(self):
        actions = {
            1: lambda: self.analyzer_parent.plot_histogram("year"),
            2: lambda: self.analyzer_parent.plot_line("year", "bpm"),
            3: lambda: print("\n".join(self.analyzer_parent.list_all_artists())),
            4: lambda: print("\n".join(self.analyzer_parent.list_all_genres())),
            5: self.analyzer_parent.top_10_artists,
            6: self.analyzer_csv.violin_plot,
            7: self.analyzer_csv.box_whisker_year,
            8: self.analyzer_csv.scatter_dance_vs_energy,
            9: lambda: self.analyzer_csv.query_artist_search(
                input("Enter an artist name to search in childCSV: ")
            ),
            10: lambda : self.analyzer_plk.display_joint_counts_table(
                input("enter the first column: "), input("enter the second column: ")
            ),
            11: lambda: self.analyzer_plk.export_joint_counts_table(
                input("Enter the first column: "), input("Enter the second column: ")
            ),
            12: lambda: self.analyzer_plk.display_joint_probability_table(
                input("Enter the first column: "), input("Enter the second column: ")
            ),
            13: lambda: self.analyzer_plk.export_joint_probability_table(
                input("Enter the first column: "), input("Enter the second column: ")
            ),
            14: lambda: self.analyzer_plk.display_conditional_probability_table(
                input("Enter the first column: "), input("Enter the second column: ")
            ),
            15: lambda: self.analyzer_plk.export_conditional_probability_table(
                input("Enter the first column: "), input("Enter the second column: ")
            ),
            16: lambda: self.analyzer_plk.display_mean(input("Enter the column: ")),
            17: lambda: self.analyzer_plk.export_mean(input("Enter the column: ")),
            18: lambda: self.analyzer_plk.display_median(input("Enter the column: ")),
            19: lambda: self.analyzer_plk.export_median(input("Enter the column: ")),
            20: lambda: self.analyzer_plk.display_mode(input("Enter the column: ")),
            21: lambda: self.analyzer_plk.export_mode(input("Enter the column: ")),
            22: lambda: self.analyzer_plk.display_position_vector(
                input("Enter the first column: "), input("Enter the second column: ")
            ),
            23: lambda: self.analyzer_plk.export_position_vector(
                input("Enter the first column: "), input("Enter the second column: ")
            ),
            24: lambda: self.analyzer_plk.display_unit_vector(
                input("Enter the first column: "), input("Enter the second column: ")
            ),
            25: lambda: self.analyzer_plk.export_unit_vector(
                input("Enter the first column: "), input("Enter the second column: ")
            ),
            26: lambda: self.analyzer_plk.display_projection_vector(
                input("Enter the first column: "), input("Enter the second column: ")
            ),
            27: lambda: self.analyzer_plk.export_projection_vector(
                input("Enter the first column: "), input("Enter the second column: ")
            ),
            28: lambda: print(self.analyzer_plk.calculate_dot_product(
                input("Enter the first column: "), input("Enter the second column: ")
            )),
            29: lambda: print(self.analyzer_plk.check_orthogonality(
                input("Enter the first column: "), input("Enter the second column: ")
            )),
            30: lambda: print(self.analyzer_plk.generate_angle_calculations(
                input("Enter the first column: "), input("Enter the second column: ")
            )),
            31: lambda: print(self.analyzer_plk.generate_permutations(
                input("Enter the column: "), input("Enter the iterable: ")
            )),
            32: lambda: print(self.analyzer_plk.generate_combinations(
                input("Enter the column: "), input("Enter the iterable: ")
            )),
            33: lambda: print(self.analyzer_plk.obtain_unique_values(input("Enter the column: "))),
            34: lambda: (self.display_exit_message(), exit())
        }

        while True:
            self.display_debug_options()
            try:
                choice = int(input("Please Enter Your Selection in number form: "))
            except ValueError:
                logging.error("Invalid Entry Made")
                self.display_invalid_message()
                continue

            action = actions.get(choice)
            if action:
                action()
                if choice != 34:
                    input("\nPress Enter to return to Debug")
            else:
                self.display_invalid_message()
        
        
            
      