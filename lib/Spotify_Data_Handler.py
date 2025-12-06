"""
data manager for loading, querying, and plotting csv-based music dataset.

filename: parent_class.py
"""


# external imports alphabetically
import os
from typing import Optional, Sequence
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
# project imports 
from lib.config import CONFIG



class Spotify_Data_Handler_Class:
    """
    Purpose:
        This class demonstrates file handling, processing, and
        data analysis using pandas and vizulation wtih matplotlib and seaborn.

    Instance variables:
        self.data: pandas DataFrame or None
        self.config: sotres configuration setting

    Methods:
        - load_data
        - summary_statistics
        - list_all_artists
        - histogram_plot
        - plot_line
        - export_to_csv
    """
    
    # default plotting and behavior constants (can be overriden via config!) 
    DEFAULT_BINS = 20
    DEFAULT_FIGSIZE = (8, 5)
    SMOOTH_NUM_POINTS = 300


    def __init__(self, config=None):
        """
        Purpose:
            Initialize the ParentClass instance with configuration values.
        INPUT:
            config (dict or None): configuration mapping. Expected keys (optional):
                Expected keys used below: CSV_PATH, PLOT_BINS, PLOT_FIGSIZE
        OUTPUT:
            None (initializes instance attributes)
        """
        # choose provided config or fallback to project-level CONFIG (avoid globals!)
        self.config = config or CONFIG
        # save resolve file path; keep attribute name clear and use PEP-8 style
        self.file_path = self.config.get("CSV_PATH", "")
        # plotting configuration (use config values if present; else defaults)
        self.plot_bins = int(self.config.get("PLOT_BINS", self.DEFAULT_BINS))
        self.plot_figsize = tuple(self.config.get("PLOT_FIGSIZE", self.DEFAULT_FIGSIZE))
        self.smooth_num_points = int(self.config.get("SMOOTH_NUM_POINTS", self.SMOOTH_NUM_POINTS))
        # dataframe placeholder (initialized to None)
        self.data: Optional[pd.DataFrame] = None
    #

    def load_data(self, file_path: Optional[str] = None) -> Optional[pd.DataFrame]:
        """
        Purpose:
            Load CSV data from configured file path into a pandas DataFram and store on self.data
        INPUT:
            file_path (str or None) : optional override CSV path. If None, uses self.file_path.
        OUTPUT:
            pd.DataFrame or None: the loaded DataFrame (also stored in self.data)    
            """
        path_to_load = file_path or self.file_path
        if not path_to_load:
            print("Error: CSV_PATH not provided in configuration.", flush=True)
            return None
        
        try:
            path_to_load = os.path.expanduser(path_to_load)
            path_to_load = os.path.abspath(path_to_load)
        except Exception as e:
            print(f"Error resolving path: {e}", flush=True)
            return None
    #
    
        try:
            df = pd.read_csv(path_to_load)
            # minimal sanity check: must be a DataFrame

            if not isinstance(df, pd.DataFrame):
                print("Loaded object is not a DataFrame.", flush=True)
                return None
            
            self.data = df
            print(f"Data loaded successfully. ({len(self.data)} rows, {len(self.data.columns)} columns)", flush=True)
            return self.data
        except FileNotFoundError:
            print(f"Error: File not found at '{path_to_load}'.", flush=True)
        except pd.errors.EmptyDataError:
            print("Error: CSV file is empty.", flush=True)  # #
        except pd.errors.ParserError as e:
            print(f"Error parsing CSV: {e}", flush=True)  # #
        except Exception as e:
            print(f"Error loading data: {e}", flush=True)  # #
        return None
    

    def basic_query(self, column, condition):
        """
        Purpose:
            Query the DataFrame for rows where a column equals a given condition
        INPUT:
            column (str) : column name to search (must be present in self.data.columns)
            condition (any) : value to match in the column (equality check)
        OUTPUT:
            pd.DataFrame or None ; filtered DataFrame of matches, or None on failure.
        """
        # precondition - data must be loaded
        if self.data is None:   # warning for if the csv hasnt been loaded
            print("No data loaded.", flush=True)
            return None
        #
        
        # validate column exists in dataframe
        if column not in self.data.columns:   # check to make sure column name is valid
            print(f"Column '{column}' not found in data.", flush=True)
            return None
        #
        
        # perform safe equality selection, avoid wrapping condition in braces
        try:
            # create boolean mask and filter #
            mask = self.data[column] == condition  # #
            result_df = self.data.loc[mask].copy()  # deep-ish copy to avoid shared-mutable pitfalls #
        except Exception as e:
            print(f"Error during query operation: {e}", flush=True)  # #
            return None
    #
        # post-query reporting
        if result_df.empty:       
            print(f"No matches found for {column} == {condition}", flush=True)
        else:
            print(f"Found {len(result_df)} result(s) for {column} == {condition}", flush=True)

        return result_df       

    def plot_histogram(self, column: str, bins: Optional[int] = None, figsize: Optional[tuple] = None) -> None:  # column so we can call parent.plot_histogram("genre") for ex.
        """
        Purpose:
            Plot a histogram for a numeric column.
        INPUT:
            column (str) : column name to plot.
            bins (int or None) : number of histogram bins to use (defaults to self.plot_bins).
            figsize (tuple or None) : figure size override (defaults to self.plot_figsize).
        OUTPUT:
            None (pops up a matplotlib figure).
        """
        # validate dataset and column #
        if self.data is None:
            print("No data loaded.", flush=True)  # #
            return  # #
        if column not in self.data.columns:
            print(f"Column '{column}' not found in data.", flush=True)  # #
            return  # #

        #
        
        # extract series and ensure numeric dtype for histogram
        series = self.data[column].dropna()
        if series.empty:
            print(f"No data available in column '{column}' to plot.", flush=True)
            return
        
        # attempt numeric cast if not numeric but convertible #
        if not np.issubdtype(series.dtype, np.number):
            try:
                numeric_series = pd.to_numeric(series, errors="coerce").dropna()  # #
                if numeric_series.empty:
                    print(f"Column '{column}' cannot be interpreted as numeric for histogram.", flush=True)  # #
                    return  # #
                series = numeric_series  # #
            except Exception:
                print(f"Could not coerce column '{column}' to numeric type.", flush=True)  # #
                return
        
        
        bins_to_use = int(bins or self.plot_bins)
        figsize_to_use = tuple(figsize or self.plot_figsize)
        plt.figure(figsize=figsize_to_use)
        plt.hist(series, bins=bins_to_use, edgecolor="black")
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        # standard grid for readability
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.show()
        # cleanup temporary objects to free memory
        del series
    #



    def plot_line(self, x_col: str, y_col: str, smooth: bool = True, figsize: Optional[tuple] = None) -> None:
        """
        Purpose:
            Plot a line chart of y_col vs x_col using aggregated mean of y grouped by x.
            Optionally smooth the line using a B-spline when numeric.
        INPUT:
            x_col (str) : column for x-axis (grouping key).
            y_col (str) : numeric column for y-axis (aggregated by mean).
            smooth (bool) : whether to attempt spline smoothing for numeric data.
            figsize (tuple or None) : optional override of figure size.
        OUTPUT:
            None (displays matplotlib figure).
        """
        # preconditions: data loaded and columns exist
        if self.data is None: 
            print("No data loaded.", flush=True)
            return
        #

        if x_col not in self.data.columns or y_col not in self.data.columns:
            print("One or both columns are not found in data.", flush=True)
            return
        
        #
        
        # aggregate by x_col (mean of y_col) and create a clean DataFrame
        df_agg = (
            self.data.loc[:, [x_col, y_col]]
            .dropna(subset=[x_col, y_col])
            .groupby(x_col, sort=True, as_index=False)[y_col]
            .mean()
            .reset_index(drop=True)
        ) #

        if df_agg.empty:
            print("No data after aggregation to plot.", flush=True)
            return
        
        df_agg = df_agg.sort_values(x_col).reset_index(drop=True)

        x = df_agg[x_col]
        y = df_agg[y_col]

        figsize_to_use = tuple(figsize or self.plot_figsize)
        plt.figure(figsize=figsize_to_use)
        

        # decide if numeric smoothing is possible #
        x_is_num = np.issubdtype(x.dtype, np.number)  # #
        y_is_num = np.issubdtype(y.dtype, np.number)  # #

        if smooth and x_is_num and y_is_num:
            # attempt B-spline smoothing, but only if enough points exist
            x_values = x.values
            y_values = y.values
            num_points = len(x_values)
            try:
                if num_points >= 4:
                    k = min(3, num_points - 1)
                
                    spline = make_interp_spline(x_values, y_values, k=k)
                    x_smooth = np.linspace(x_values.min(), x_values.max(), self.smooth_num_points)
                    y_smooth = spline(x_smooth)
                    plt.plot(x_smooth, y_smooth, linewidth=2, label="Smoothed")
                    # show original points for transparency
                    plt.scatter(x_values, y_values, label='Original points', marker="o")
                else:
                    # fallback to plotting regular line when not enough points
                    plt.plot(x_values, y_values, marker="o", linestyle="-", linewidth=2, label="Line")
            except Exception as e:
                print("Could not smooth line: {e}. Using regular line plot instead.", flush=True)
                plt.plot(x_values, y_values, marker="o", linestyle='-', linewidth=2, label="Line")
            #
        
        else:
            # non-numeric or smoothing disabled: plain line plot
            plt.plot(x.values, y.values, marker='o', linestyle='-', linewidth=2, label="Line")
        #

        plt.title(f"{y_col} vs {x_col}", fontsize=14)
        plt.xlabel(x_col, fontsize=12)
        plt.ylabel(y_col, fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
    
        try:
            if x_is_num and y_is_num:
                x_range = float(np.nanmax(x.values) - np.nanmin(x.values))
                y_range = float(np.nanmax(y.values) - np.nanmin(y.values)) 
                # if neither range is zero and they are within two orders of magnitude, set equal 
                if x_range > 0 and y_range > 0:
                    ratio = max(x_range / y_range, y_range / x_range) 
                    if ratio <= 100:  # safe threshold to avoid visual distortion
                        ax = plt.gca()
                        ax.set_aspect("equal", adjustable="box")  
        except Exception:
            # silently ignore aspect setting issues (avoid interrupting plot) #
            pass

        plt.tight_layout()
        plt.show()  

        # cleanup local variables for memory efficiency
        del df_agg, x, y
    #

    def list_all_artists(self) -> Optional[np.ndarray]:
        """
        Purpose:
            Return all unique artist names from the loaded data.
        INPUT:
            None
        OUTPUT:
            numpy.ndarray or None : unique artist names, or None if no data loaded.
        """
        if self.data is None:
            print("No data loaded.", flush=True)
            return None
    
        if "artist" not in self.data.columns:
            print("Column 'artist' not found in data.", flush=True)
            return None
        #
        
        artists = self.data["artist"].dropna().unique()
        return artists
    #

    def list_all_genres(self):
        """
        Purpose:
            Return all unique genre names from the loaded data.
        INPUT:
            None
        OUTPUT:
            numpy.ndarray or None : unique genres, or None if no data loaded.
        """
        if self.data is None:
            print("No data loaded.", flush=True) 
            return None 
        # prefer the column name used by dataset; handle common variants 
        possible_genre_cols = ["top genre", "genre", "genres"]  
        for col in possible_genre_cols:
            if col in self.data.columns:
                genres = self.data[col].dropna().unique()  
                return genres  
        print("No genre column found among expected names.", flush=True)  
        return None  
    
    #

    def top_10_artists(self) -> Optional[pd.Series]:
        """
        Purpose:
            Return the top 10 artists by number of songs in the dataset.
        INPUT:
            None
        OUTPUT:
            pandas.Series or None : counts of top 10 artists ordered descending, or None if no data.
        """
        if self.data is None:
            print("No data loaded", flush=True)
            return None
        if "artist" not in self.data.columns:
            print("Column 'artist' not found in data.", flush=True)
            return None
        
        top_artists = self.data["artist"].value_counts().head(10)
        print("Top 10 Artists:\n", top_artists.to_string(), flush=True)
        return top_artists
    #
    
    def create_test_dataset(num_rows: int = 100) -> pd.DataFrame:
        """
        Purpose:
            Generate an artificial DataFrame for testing methods without external files.
        INPUT:
            num_rows (int) : number of rows to create.
        OUTPUT:
            pandas.DataFrame : synthetic dataset containing columns 'artist', 'top genre', and 'plays'.
        """
        rng = np.random.default_rng(seed=42)  # deterministic test data generator #
        artists = [f"Artist_{i}" for i in range(1, 11)]  # #
        genres = ["rock", "pop", "electronic", "folk"]  # #

        df_test = pd.DataFrame(
            {
                "artist": rng.choice(artists, size=num_rows),  # #
                "top genre": rng.choice(genres, size=num_rows),  # #
                "plays": rng.integers(0, 10000, size=num_rows),  # #
            }
        )  # #
        return df_test  # #
    #

# end class


# quick demonstration / test 
if __name__ == "__main__":
    # create class with default CONFIG and inject synthetic data for testing #
    pc = Spotify_Data_Handler_Class(config={"CSV_PATH": ""})  # #

    # create and assign artificial dataset for local testing #
    test_df = Spotify_Data_Handler_Class.create_test_dataset(200)  # #
    pc.data = test_df  # #
    print("Artificial test data assigned.", flush=True)  # #

    # exercise basic methods to validate functionality (sanity checks) #
    _ = pc.basic_query("artist", "Artist_1")  # #
    pc.plot_histogram("plays")  # #
    pc.plot_line("top genre", "plays", smooth=False)  # #
    _ = pc.top_10_artists()  # #
# class end