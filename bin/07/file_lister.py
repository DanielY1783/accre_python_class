# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-25
#
# Description: My solution to the below exercise posed by Eric Appelt:
#
# Exercise: Write a module with a public function that takes a directory path
# as an argument and returns a dictionary all (regular) file names and their
# associated size in bytes
#
# Hint: Use os.listdir for directory contents, os.is_file to filter
# non-regular files, and os.stat to get sizes.
#
# Allow the module to be run as a script, in which case it should (nicely)
# print the sizes for all files in the current directory. If the module is
# imported it should not do this.
#
# Add another function similar to the first but that returns a dictionary
# of the file names and the number of days since each file was modified
#
# Hint: Use datetime.fromtimestamp(...) and the st_mtime attribute of the
# os.stat(...) result to manipulate the modification time as a datetime object.

# Libraries
import datetime
import os


def dict_file_sizes(directory):
    """
    Creates and returns a dictionary containing keys as files in a directory
    and values as the sizes in the directory.

    :param directory: String of directory to look in. Exception will be
    raised if this is invalid.
    :return: Dictionary containing keys as files in directory and values as
    the sizes in the directory.
    """
    # Get list of files
    files_list = os.listdir(directory)

    # Get sizes of files and put in dictionary with key as file
    files_dict = {}
    for file in files_list:
        dir_and_file = os.path.join(directory, file)
        # Get valid files only
        if os.path.isfile(dir_and_file):
            files_dict[file] = os.path.getsize(dir_and_file)
    # Return dictionary with file names as keys and sizes as values.
    return files_dict


def print_file_sizes_dict(file_sizes_dict):
    """
    Print files and sizes from dictionary in nice format to standard output,
    with file in first column and size in second column.
    :param file_sizes_dict: Dictionary with file as key and size as value
    :return: None
    """
    for file, size in file_sizes_dict.items():
        print("File: {:<25} Size: {} bytes".format(file, size))


def dict_days_modified(directory):
    """
    Creates and returns a dictionary containing keys as files in a directory
    and values as integers of number of days since the file was last modified.

    :param directory: String of directory to look in. Exception will be
    raised if this is invalid.
    :return: Dictionary containing keys as files and values as integers of
    number of days since the file was last modified.
    """
    # Get list of files
    files_list = os.listdir(directory)

    # Get date of files and find number of days since last modification.
    # Store to dictionary as value, with file names as keys.
    files_dict = {}
    for file in files_list:
        dir_and_file = os.path.join(directory, file)
        # Get valid files only
        if os.path.isfile(dir_and_file):
            # Get last modified date
            last_modified_timestamp = os.stat(dir_and_file).st_mtime
            last_modified_date = datetime.date.fromtimestamp(
                last_modified_timestamp)
            # Store days since last modification to dictionary
            files_dict[file] = (datetime.date.today() - last_modified_date).days
    # Return dictionary with file names as keys and integer days since last
    # modification as value.
    return files_dict


def print_file_modified_dict(file_modified_dict):
    """
    Print files and sizes from dictionary in nice format to standard output,
    with file in first column and size in second column.
    :param file_sizes_dict: Dictionary with file as key and size as value
    :return: None
    """
    for file, days in file_modified_dict.items():
        print("File: {:<25} Days: {} days since last modification".format(file,
            days))


if __name__ == '__main__':
    file_sizes_dict = dict_file_sizes(os.getcwd())
    print_file_sizes_dict(file_sizes_dict)
    file_modified_dict = dict_days_modified("../../../Test_Project")
    print_file_modified_dict(file_modified_dict)
