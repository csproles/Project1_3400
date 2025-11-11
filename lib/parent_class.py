import pandas as pd
import matplotlib.pyplot as plt   # for graph creation
import numpy as np
from lib.config import CONFIG
from scipy.interpolate import make_interp_spline



class ParentClass:
    def __init__(self, config=None):
        #initialize w/ option config or call back to dict
        self.config = config or CONFIG
        self.file_path = self.config["CSV_PATH"]
        self.data = None

    def load_data(self):
        """load data from CSV into a pandas DataFrame"""
        try:
            self.data = pd.read_csv(self.file_path)   # reads CSV and stores it in self.data
            print(f"Data loaded successfully. ({len(self.data)} rows, {len(self.data.columns)} columns)")  
            # len(self.data) counts how many rows were read
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"Error loading data: {e}")
    

    def basic_query(self, column, condition):
        """
        simple query the dataframe for rows matching a condition.
        takes two inputs as column and condition
        column is which column to search (maybe artist or genre)
        condition is what to match (like a specific artist name or something)
        """
        if self.data is None:   # warning for if the csv hasnt been loaded
            print("No data loaded.")
            return None
        
        if column not in self.data.columns:   # check to make sure column name is valid
            print(f"Column '{column}' not found in data.")
            return None
        
        result = self.data[self.data[column] == {condition}]  
        ''' self.data[column] == condition 
        - creates a boolean series to tell if that row meets the condition
        - the outer self.data[...] uses boolean indexing
        selects only the rows where the value in the boolean series was true'''
        if result.empty:
            print(f"No matches are found for {column} == {condition}")
        else:
            print(f"Found {len(result)} results:")
        return result
        ''' the filtered DataFrame is return to the function caller
        can be used to print or vizualize yadayada 
        '''                

    def plot_histogram(self, column):  # column so we can call parent.plot_histogram("genre") for ex.
        """ vizualization for a numeric column (histogram) """
        if self.data is None: # before plotting check that csv is loaded
            print("No data loaded")
            return
        if column not in self.data.columns: #checks if column name actually exists in the dataframe
            print(f"Column '{column}' not found in data.")
            return
        
        self.data[column].hist(bins=20, color='skyblue', edgecolor='black')
        ''' 
        self.data[column] - extracts just one column from datafram
        .hist - pandas is using matplotlib
        bins=20 - divides data into 20 intervals (finer detail)
        color - up for change, just first in list i was viewing
        '''
        plt.title(f"Histogram of {column}")
        # adds title to top of graph
        plt.xlabel(column)
        # labels x-axis w/ column name
        plt.ylabel("Frequency")
        # labels y-axis with frequency
        plt.show()
        # shows the plot



    def plot_line(self, x_col, y_col, smooth=True):
        ''' takes x_column to plot the name on x-axis, ditto for y_column
        overall - plot line graph of one column vs another.
        '''
        
        if self.data is None: # check if dataset is loaded or not
            print("No data loaded.")
            return
        if x_col not in self.data.columns or y_col not in self.data.columns:
            print("One or both columns are not found in data.")
            return
        ''' checks both the specified column names exist in datagrame, otherwise prints message'''
        
        df_agg = self.data.groupby(x_col)[y_col].mean().reset_index()
        x = df_agg[x_col]
        y = df_agg[y_col]

        plt.figure(figsize =(8, 5))
        ''' fixed uglies '''
        
        if smooth and np.issubdtype(x.dtype, np.number) and np.issubdtype(y.dtype, np.number):
            try:
                x_values = x.values
                y_values = y.values
                num_points = len(x_values)
                k = min(3, num_points - 1)
                if k < 1:
                    raise ValueError("Not enough points for spline smoothing")
                spline = make_interp_spline(x, y, k=3)
                x_smooth = np.linspace(x.min(), x.max(), 300)
                y_smooth = spline(x_smooth)
                plt.plot(x_smooth, y_smooth, color='teal', linewidth=2, label='Smoothed line')
                plt.scatter(x_values, y_values, color='coral', label='Original points')
            except Exception as e:
                print("Could not smooth line: {e}. Using regular line plot instead.")
            plt.plot(x, y, marker ='o', linestyle='-', color='teal', linewidth=2)
        else:
            plt.plot(x, y, marker='o', linestyle='-', color='teal', linewidth=2)

        plt.title(f"{y_col} vs {x_col}", fontsize=14)
        plt.xlabel(x_col, fontsize=12)
        plt.ylabel(y_col, fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def list_all_artists(self):
        """ listing all unique artist names """
        if self.data is not None:
            return self.data['artist'].unique()   # accesses arist column and tells pandas to find disctinct values
        print("No data loaded")

    def list_all_genres(self):
        """ listing all unique genres """
        if self.data is not None:
            return self.data['top genre'].unique() # same as prior but for genre
        print("No data loaded.")

    def top_10_artists(self):
        """ display top 10 artists by number of songs in dataset """
        if self.data is not None:
            top_artists = self.data['artist'].value_counts().head(10)
            ''' 
            artists - selects artist column
            .value_counts() - counts how many times each artist appears
            .head(10) - tales only the top 10 most frequent ones
            '''
            print("Top 10 Artists:\n", top_artists)
            return top_artists
        print("No data loaded")
        