# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Create a code that calculate the quotient of two numbers with exception handling and pickling code.
# ChangeLog (Who,When,What):
# MKarumuhinzi,05.23.2021,Modified Assignment 06 to calculate quotient of two numbers instead of adding task to list.
# MKarumuhinzi,05.23.2021,Added pickling code.
# MKarumuhinzi,05.23.2021,Added exception handling code.
# ---------------------------------------------------------------------------- #


import pickle


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Write data to a file from a list of rows

        :param file_name: (string) with name of file
        :param list_of_rows: (list) of data saved to file
        :return: (list, boolean) of rows and True if succeeded writing in the file, False otherwise
        """
        is_success = False
        
        try:
            file = open(file_name, "wb")
            pickle.dump(list_of_rows, file)
            file.close()
            is_success = True
        except FileNotFoundError as e:
            print("Data file not found: ", file_name)
        except Exception as e:
            print("There was a non-specific error: ")
            print(e, e.__doc__, type(e), sep='\n')
        
        return list_of_rows, is_success

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of rows
        
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list, boolean) of rows and True if the file contains some data, False otherwise
        """
        is_success = False

        try:
            list_of_rows.clear()  # clear current data
            file = open(file_name, "rb")
            list_of_rows = pickle.load(file)
            file.close()
            is_success = True
        except FileNotFoundError as e:
            print("Data file not found: ", file_name)
        except Exception as e:
            print("There was a non-specific error: ")
            print(e, e.__doc__, type(e), sep='\n')
        
        return list_of_rows, is_success
    
    @staticmethod
    def add_data_to_list(f_number, s_number, quotient, list_of_rows):
        """ Add a new item to the list/Table

        :param f_number: (float) first number:
        :param s_number: (float) second number:
        :param quotient: (float) quotient:
        :param list_of_rows: (list) of data to add item to:
        :return: (list, boolean) of rows and True
        """
        list_of_rows.append(str(f_number) + " / " + str(s_number) + " = " + str(quotient))
        return list_of_rows, True
    
    @staticmethod
    def convert_to_float(cur_number):
        """ convert the number into a float
        
        :param cur_number: (float) number to convert:
        :return: (float, boolean) the number and True or False if the conversion succeeded
        """
        converted = False
        try:
            if cur_number.isnumeric() == False:
                raise InvalidNumberError()
            else:
                cur_number = float(cur_number)
                converted = True
        except InvalidNumberError as e:
            print("You entered an invalid number.")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was a non-specific error:")
            print(e, e.__doc__, type(e), sep='\n')      
            
        return cur_number, converted
    
    @staticmethod
    def get_quotient(f_number, s_number):
        """ Get the quotient of two numbers
        
        :param f_number: (float) first number:
        :param s_number: (float) second number:
        :return: (float, boolean) the quotient and True or False if the operation succeeded
        """
        is_success = False
        quotient = None
        try:
            if s_number == 0:
                raise Exception('The second number can not be 0.')
            else:
                quotient = f_number / s_number
                is_success = True
        except Exception as e:
            print("There was a non-specific error:")
            print(e, e.__doc__, type(e), sep='\n')      
            
        return quotient, is_success


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Get quotient
        2) Save Data to File        
        3) Reload Data from File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice
    
    @staticmethod
    def print_current_data_in_list(list_of_rows):
        """ Shows the current data in the list of rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current data are: *******")
        for row in list_of_rows:
            print(row)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_first_and_second_numbers():
        """ Gets first and second numbers from the user

        :return: (float, float, boolean) first and second numbers and True or False if both numbers are valid
        """
        is_valid = False
        s_number = None
        
        f_number = input("Enter a first number:")
        f_number, converted = Processor.convert_to_float(f_number)
        
        if converted == True:
            s_number = input("Enter a second number:")
            s_number, converted = Processor.convert_to_float(s_number)
            if converted == True:
                is_valid = True

        return f_number, s_number, is_valid


class InvalidNumberError(Exception):
    """  validate the number  """

    def __str__(self):
        return 'Invalid number.'    


# Presentation ------------------------------------ #
strFileName = "AppData.dat"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strStatus = ""  # Captures the status of an processing functions

# Step 1 - When the program starts, Load data from AppData.dat.
lstTable, bSuccess = Processor.read_data_from_file(strFileName, lstTable)  # read file data
print()

# Step 1 - Display a menu of choices to the user
while(True):
    # Step 2 Show current data
    IO.print_current_data_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 3 - Process user's menu choice
    if strChoice.strip() == '1':  # Get quotient
        f_number, s_number, is_valid = IO.input_first_and_second_numbers()
        
        if is_valid == True:
            quotient, is_success = Processor.get_quotient(f_number, s_number)
            print()
            if is_success == True:
                print("The quotient of " + str(f_number) + " and " + str(s_number) + " is: " + str(quotient))
                lstTable, is_success = Processor.add_data_to_list(f_number, s_number, quotient, lstTable)
            else:
                print("Operation failed")

        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstTable, bSuccess = Processor.write_data_to_file(strFileName, lstTable)
            print()
            if bSuccess == True:
                print("Data saved.")
                IO.print_current_data_in_list(lstTable)
            else:
                print("Data not saved.")
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '3':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable, bSuccess = Processor.read_data_from_file(strFileName, lstTable)
            print()
            if bSuccess == True:
                IO.print_current_data_in_list(lstTable)
            else:
                print('No task found.')
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  #  Exit Program
        print("Goodbye!")
        break  # and Exit

