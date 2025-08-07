# Python-Algorithm File-Updater

### Objective
This project features a Python algorithm designed to automate network security policy enforcement. The script efficiently identifies and removes unauthorized IP addresses from a list by comparing them against a set of approved IPs. This method ensures network integrity and demonstrates a foundational understanding of proactive security measures and efficient data handling.

### Skills Learned

- File I/O reading and writing to files.
- String manipulation to parse and format data for specific purpose.
- Conditional logic and control flow through implemntation of if statements and for loops.

### Tools Used 
- Google Colab
- Python

## Steps
Each step will add on to the previous. The new code is located at the bottom of the provided images.
### Open the file that contains the allow list.

<img width="577" height="62" alt="image" src="https://github.com/user-attachments/assets/b0baee75-dee9-4e3f-9e57-3d28ff69e7a8" />

This opens the allow_list.txt file and places it into the variable import_file. Using the with and open commands, the first parameter import_file and the second parameter “r” so it can be read. The as file command places the opened file into the variable file.

### Read the file contents

<img width="480" height="85" alt="image" src="https://github.com/user-attachments/assets/f6476624-9454-49e8-8cea-405a06e925c1" />

Creating the variable ip_addresses  to place the read data using file.read().
 
### Convert file contents into list of substrings

<img width="477" height="328" alt="image" src="https://github.com/user-attachments/assets/c400ab9d-a0a7-42c8-96ab-3b11fc8c9a1f" />

Ip_addresses.split() turns the data in the allow_list.txt file into seperate substring data.

### Iterate through the remove list

<img width="612" height="130" alt="image" src="https://github.com/user-attachments/assets/8d5e2657-6d7f-43d3-9f49-a80426a33cf9" />

This is the start of the loop that will look for the variable(element) in the remove_list.


### Remove IP addresses found on remove list

<img width="617" height="142" alt="image" src="https://github.com/user-attachments/assets/f65dd1a7-0aa3-4cc9-9b06-7c4ad73b65d2" />

The loop then goes into a conditional statement matching the element variable to the ip_addresses list. If the element matches in ip_addresses and remove_list then it is removed from the ip_addresses list.


### Update the file with the revised IP address list

import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]


with open(import_file, "r") as file:
      ip_addresses = file.read()

ip_addresses = ip_addresses.split()

for element in remove_list
    if element in ip_addresses:
        ip_addresses.remove(element)

ip_addresses = "\n ".join(ip_addresses)    

with open(import_file, "w") as file:
      file.write(ip_addresses)


The .join() was used to combine the elements from the iterable into a string. The “\n” parameter is used to instruct python to place each element on a new line.

Using the with open the import_file is opened and parameter “w” is used so the .write() function will work. The next line file.write uses the ip_addresses to overwrite the file.


