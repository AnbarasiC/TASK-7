#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program using Function to which will do the following-
# a) The function will create a text file with the current timestamp.
# b) The file content should have the content of the current timestamp.

import datetime

def create_text_file_with_timestamp():
    # Get the current timestamp
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")

    # Create and write to the text file
    file_name = f"file_{timestamp}.txt"
    with open(file_name, 'w') as file:
        file.write(f"This is a text file created at {current_time}.")

    print(f"Text file {file_name} created.")

create_text_file_with_timestamp()


# In[4]:


# 2. Write another Python function to read from a text file. The function will take the name of the text file and 
# display the content of the file into console.

def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of the file {file_name}:\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "file_2023-10-24_10-20-01.txt"  # The name of the text file
read_text_file(file_name)

