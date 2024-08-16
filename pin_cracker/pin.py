# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:07:20 2024

@author: IAN CARTER KULANI
"""

# Generate all 3-digit PINs and save them to pin.txt
with open('pin.txt', 'w') as file:
    for pin in range(1000):
        file.write(f"{pin:03}\n")  # Format PIN with leading zeros
