# The main script imports the non-main one.
import random_indices as imported_script

# When 'main.py' is ran, it calls a function from the non-main file.
if __name__ == '__main__':
    imported_script.main()