# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

prefix_path = "C:/_Continut/"
relative_path = "Instructiv/Computing/Python/TestGit/"
prefix_nume = 'Tangerine March2018'
unwanted_items = ['', ' ', '***6886', 'Add Friend', 'Close Friend', 'Friend', 'Friends']
cleaned = []


with open(prefix_path + relative_path + prefix_nume + ".txt") as textfile:
    content = textfile.read().splitlines()
    cleaned = [elem for elem in content if not (elem in unwanted_items)]
    cleaned.insert(1, "Percentage")
    cleaned[3] = "Category" 
    print('TRANZACTII ' + prefix_nume + ':')
    print(cleaned)
