#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox


# In[2]:


import os
import pandas as pd
from datetime import datetime
from tkinter import Tk, filedialog


# In[3]:


def select_input_dir():
    input_dir = filedialog.askdirectory(title="Select the Input Directory")
    if input_dir:
        input_dir_var.set(input_dir)


# In[4]:



def select_output_dir():
    output_dir = filedialog.askdirectory(title="Select the Output Directory")
    if output_dir:
        output_dir_var.set(output_dir)


# In[5]:


def merge_files():
    input_dir = input_dir_var.get()
    output_dir = output_dir_var.get()
    
    if not os.path.exists(input_dir):
        messagebox.showerror("Error", f"Input directory {input_dir} does not exist.")
        return
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        messagebox.showinfo("Info", f"Output directory {output_dir} created.")

    files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    if not files:
        messagebox.showerror("Error", f"No files found in input directory {input_dir}.")
        return


# In[6]:


def select_input_dir():
    input_dir = filedialog.askdirectory(title="Select the Input Directory")
    if input_dir:
        input_dir_var.set(input_dir)

def select_output_dir():
    output_dir = filedialog.askdirectory(title="Select the Output Directory")
    if output_dir:
        output_dir_var.set(output_dir)

def merge_files():
    input_dir = input_dir_var.get()
    output_dir = output_dir_var.get()
    
    if not os.path.exists(input_dir):
        messagebox.showerror("Error", f"Input directory {input_dir} does not exist.")
        return
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        messagebox.showinfo("Info", f"Output directory {output_dir} created.")

    files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    if not files:
        messagebox.showerror("Error", f"No files found in input directory {input_dir}.")
        return

    # Flag to choose sorting by date modified or date created
    sort_by_modified = True  # Set to False to sort by date created

    if sort_by_modified:
        files.sort(key=lambda x: os.path.getmtime(os.path.join(input_dir, x)))
    else:
        files.sort(key=lambda x: os.path.getctime(os.path.join(input_dir, x)))

    dfs = []

    for file in files:
        df = pd.read_csv(os.path.join(input_dir, file))
        dfs.append(df)

    merged_df = pd.concat(dfs)
    now = datetime.now()
    output_file = os.path.join(output_dir, f"merged_{now.strftime('%Y%m%d')}.csv")
    merged_df.to_csv(output_file, index=False)
    
    messagebox.showinfo("Success", f"Files merged and saved to {output_file}")


# In[7]:


# Create the main window
root = tk.Tk()
root.title("File Merger")

# Variables to store the directory paths
input_dir_var = tk.StringVar()
output_dir_var = tk.StringVar()

# Create and place the widgets
tk.Label(root, text="Input Directory:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=input_dir_var, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_input_dir).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Output Directory:").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=output_dir_var, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_output_dir).grid(row=1, column=2, padx=10, pady=5)

tk.Button(root, text="Merge Files", command=merge_files).grid(row=2, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()


# In[ ]:




