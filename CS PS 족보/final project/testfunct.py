def sample_file_write(filename):
            """A function that demonstrates how to write a
            Python dictionary to an easily-readable file.
            """
            d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
            f = open(filename, 'w')      # Open file for writing.
            f.write(str(d))              # Writes the dictionary to the file.
            f.close()                    # Close the file.

def sample_file_read(filename):
            """A function that demonstrates how to read a
            Python dictionary from a file.
            """
            f = open(filename, 'r')    # Open for reading.
            d_str = f.read()           # Read in a string that represents a dict.
            f.close()

            d = dict(eval(d_str))      # Convert the string to a dictionary.

            print("Inside the newly-read dictionary, d, we have:")
            print(d)
