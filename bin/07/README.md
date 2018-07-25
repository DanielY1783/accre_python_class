* Write a module with a public function that takes a directory path as an argument and returns a dictionary all (regular) file names and their associated size in bytes
* Hint: Use os.listdir for directory contents, os.is_file to filter non-regular files, and os.stat to get sizes.
* Allow the module to be run as a script, in which case it should (nicely) print the sizes for all files in the current directory. If the module is imported it should not do this.
* Add another function similar to the first but that returns a dictionary of the file names and the number of days since each file was modified
* Hint: Use datetime.fromtimestamp(...) and the st_mtime attribute of the os.stat(...) result to manipulate the modification time as a datetime object.