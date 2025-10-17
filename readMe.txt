Project for CMPS 3400

Project must meet these specific requirements as stated in the slideshow:

MODULES:
    []- use module_tmp.py
    []- main.py
    []- config.py: holds common configuration constants {optional}
    []- parent class
    []- child class
    []- others as needed

FUNCTIONALITIES:
    []- read from a file
        []- csv file
        []- pickle file
    []- query
    []- calculate
    []- log progress and errors
    []- visualize
    []- export
        []- csv file
        []- pickle file
        []- picture

FOLDERS:
    [/]- input
    [/]- output
    [/]- doc
    []- lib {optional}
    []- others as needed

VARIABLE TYPES:
    []- immutable types: for read-only operations
    []- mutable types: for objects to be updated

CHECKS FOR POSSIBLE ERRORS:
    []- log operations
    []- catch errors and continue running if not crucial

UTILIZE FOLLOWING VARIABLE TYPES:
    []- global
    []- nonlocal
    []- private like

UTILIZE FOLLOWING TYPE OF FUNCTION PARAMETERS:
    []- *arg
    []- **kwarg
    []- positional arguments

UTILIZE:
    []- boolean indexing
    []- eval()
    []- lambda function

FUNCTIONALITIES:
    []- query dataframe
    []- write an mxn numpy array into a dataframe

CREATE TWO CLASSES AS A PARENT AND CHILD CLASS:
    PARENT CLASS-1:
        []- store configuration constants in a dictionary {optional, reading from the config.py}
        []- visualize data in each column using either
            []- histogram for distributions
            []- line plot to visualize numeric data
        []- query data for searching
            []- a simple value (simple condition)

    CHILD CLASS-1:
        []- read data from a csv file
            []- store into a dataframe
        []- utilize configuration constants
        []- visualize distributions in each column using
            []- violin plot
            []- whisker-box plot
            []- scatter plot
        []- query data for searching and display
            []- a set of numeric and string values
                []- using boolean indexing
    
    PARENT CLASS-2:
        []- ...your design...
    
    CHILD CLASS-2:
        []- read data from a pickle file
        []- utilize configuration constants {optional, reading from the config.py}
        []- visualize
            []- ...
        []- probability: calculate, display, export
            []- joint counts
            []- joint probabilities
            []- conditional probabilities
            []- mean, median, state
        []- vector operators: display, export
            []- obtain position vector
            []- obtain unit vectors
            []- obtain projection vectors
            []- calculate the dot product
                []- the angle between two vectors
                []- check for orthogonality
        []- for a categorical attribute do the following and display
            []- obtain unique values
            []- generate permutations
            []- generate combinations
