import pandas as pd
import matplotlib.pyplot as plt   # for graph creation
from config import CONFIG

class ParentClass:
    def __init__(self, file_path=None):
        # load file path from argument or CONFIG
        self.file_path = file_path or CONFIG["CSV_PATH"] #if no specific file is given, it pulls from config
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



    def plot_line(self, x_col, y_col):
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
        
        plt.plot(self.data[x_col], self.data[y_col], marker='o', linestyle='-', color='teal')
        ''' 
        plt.plot - matplotlib function makes a line plot
        self.data[x_column] - takes the series of x-vals from dataframe
        self.data[y_column] - ditto for y-vals
        color - again, up for change
        marker='o' - adds circle markers at each data point'''
        plt.title(f"{y_col} vs {x_col}")
        # sets title of chart dynamically
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        # label axes with column names
        plt.grid(True)
        # adds a grid to the background
        plt.show()
        # shows

    def list_all_artists(self):
        """ listing all unique artist names """
        if self.data is not None:
            return self.data['artist'].unique()   # accesses arist column and tells pandas to find disctinct values
        print("No data loaded")

    def list_all_genres(self):
        """ listing all unique genres """
        if self.data is not None:
            return self.data['genre'].unique() # same as prior but for genre
        print("No data loaded.")

    def top_10_artists(self):
        """ display top 10 artists by number of songs in dataset """
        if self.data is not None:
            top_artists = self.data['artists'].value_counts().head(10)
            ''' 
            artists - selects artist column
            .value_counts() - counts how many times each artist appears
            .head(10) - tales only the top 10 most frequent ones
            '''
            print("Top 10 Artists:\n", top_artists)
            return top_artists
        print("No data loaded")
        