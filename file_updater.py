# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 20:42:49 2025

@author: mitch
"""

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
