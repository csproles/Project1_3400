from lib.config import CONFIG
from lib.parent_class import ParentClass
from lib.child_csv import childCSV
from lib.child_pickle import PickleChild
from lib.user_interface import UserInterface

def main():
    cfg = CONFIG

    # ----------- Child CSV Testing -----------
    print(" Testing childCSV methods ")
    analyzer_csv = childCSV(cfg)
    analyzer_csv.load_data()

    # Example visualizations from childCSV
    analyzer_csv.violin_plot()
    analyzer_csv.box_whisker_year()
    analyzer_csv.scatter_dance_vs_energy()

    # Artist search
    artist_query = input("Enter an artist name to search in childCSV: ")
    analyzer_csv.query_artist_search(artist_query)

    # ----------- PickleChild Testing -----------
    print(" Testing PickleChild methods ")
    pickle_child = PickleChild()
    pickle_child.load_data()

    # Example calculations
    print("Dot Product:", pickle_child.generate_dot_product("year", "bpm"))
    print("Projection:", pickle_child.generate_projection("year", "bpm"))
    print("Angle Calculations:", pickle_child.generate_angle_calculations("year", "bpm"))

    # ----------- ParentClass Testing -----------
    print(" Testing ParentClass methods ")
    analyzer_parent = ParentClass()
    analyzer_parent.load_data()

    # Visualizations
    analyzer_parent.plot_histogram("year")
    analyzer_parent.plot_line("year", "bpm")

    # Unique values
    print("Unique artists:", analyzer_parent.list_all_artists())
    print("Unique genres:", analyzer_parent.list_all_genres())

    # Top 10 artists
    analyzer_parent.top_10_artists()

    print("\nAll processing complete.")

if __name__ == "__main__":
    main()
