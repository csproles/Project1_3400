from config import CONFIG
from module_tmp import log_message
from lib.parent_class import ParentClass
from lib.parent_class2 import ParentClass2
from lib.child_csv import BabyNamesCSV
from lib.child_pickle import PickleChild
from lib.user_interface import UserInterface

def main():
    # Placeholder: user input, query type, etc.
    # Create and test objects of Parent or Child classes
    # Call query(), visualize(), calculate(), export() methods
    # pass
    
    pickleChild = PickleChild()
    pickleChild.load_data()
    pickleChild.calculate_joint_probability("year", "artist")
    #UserInterface.start()
    

if __name__ == "__main__":
    main()
