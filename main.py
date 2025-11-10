from config import CONFIG
from module_tmp import log_message
from lib.parent_class import ParentClass
from lib.parent_class2 import ParentClass2
from lib.child_csv import BabyNamesCSV
from lib.child_pickle import BabyNamesPickle

def main():
    # Placeholder: user input, query type, etc.
    # Create and test objects of Parent or Child classes
    # Call query(), visualize(), calculate(), export() methods
    # pass
    print("hello World")

if __name__ == "__main__":
    main()
    cfg = CSVConfig(
        csv_path="Spotify_data.csv",
        parse_dates=(),
        dtype=None,
        numeric_cols=("Beats Per Minute", "Danceability", "Energy", "Year"),
        categorical_cols=("Genre", "artist"),
        title_prefix="Spotify Data",
        fig_size=(9, 5),
    )

    analyzer = BabyNamesCSV(cfg)
    analyzer.violin_plot()          
    analyzer.box_whisker_year()        
    analyzer.scatter_dance_vs_energy()   
    artist_query = input("Enter an artist name to search: ")
    analyzer.query_artist_search(artist_query)
