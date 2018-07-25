# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-25
#
# Description: My solution to the below exercise posed by Eric Appelt
#
# Exercise: Save the csv content below into a file. This information is the
# last name, first name, and age of employees of an imaginary company,
# animals.com. Write a script to read in the csv file and then write a new
# file with all the information as well as a fourth column with the email
# address of each employee. The email address of an employee is comprised of
# their last name (up to the first seven letters, all lowercase) followed by
# the first letter of their first name (lowercase) at animals.com. For
# example, I am Eric Appelt and my email would be appelte@animals.com. Ada
# Lovelace would be lovelaca@animals.com.
# Aardvark,Alice,27
# Badger,Bob,44
# Catfish,Cynthia,32
# Dingo,Drew,61
# Elephant,Emily,24
# Frog,Ferdinand,41
# Gerbil,Greta,33
# Heron,Harold,19
# Iguana,Isabella,29
# Jaguar,John,61
# Kangaroo,Kate,63
# Lemur,Leonard,54
# Millipede,Marsha,47
# Newt,Norman,21
# Octopus,Olivia,42
# Pelican,Peter,29
# Quail,Quinlan,30
# Raccoon,Rocky,50
# Salamander,Stacy,36
# Termite,Terrence,20
# Uakari,Ursula,27
# Vulture,Vincent,61
# Warthog,Wanda,50
# Xenops,Xavier,21
# Yak,Yolanda,44
# Zebra,Zackery,49


# Constants
LAST_NAME = 0 # Column number with last name

if __name__ == '__main__':
    with open("../../data/03/info.csv", mode="r") as read_file, \
            open("../../output/03/output.csv", mode="w+") as write_file:
        # Process each line separately in the input file.
        for line in read_file:
            # Remove new line character
            line_stripped = line.strip()
            # Get individual fields
            info_list = line_stripped.split(",")
            # Process email
            email_str = "{}@animals.com".format(info_list[LAST_NAME].lower()[
                                                0:7])
            # Format new line to write to write file
            new_str = "{},{}\n".format(line_stripped, email_str)
            write_file.write(new_str)