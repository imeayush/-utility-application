#!/usr/bin/env python
# coding: utf-8

# In[24]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
from datetime import datetime


# In[4]:


input_dir = "C:/Users/Ayush Lokhande/OneDrive/Documents/AA"
output_dir = "C:/Users/Ayush Lokhande/OneDrive/Documents/BB"


# In[5]:


# Get a list of all files in the input directory
files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]


# In[6]:


files.sort(key=lambda x: os.path.getmtime(os.path.join(input_dir, x)))


# In[7]:


# Initialize an empty list to store dataframes
dfs = []


# In[8]:


# Read and append each file to the list
for file in files:
    df = pd.read_csv(os.path.join(input_dir, file))
    dfs.append(df)


# In[9]:


# Concatenate all dataframes into one
merged_df = pd.concat(dfs)


# In[10]:


# Get the current date and time
now = datetime.now()


# In[11]:


# Generate the filename with the current date
output_file = os.path.join(output_dir, f"merged_{now.strftime('%Y%m%d')}.csv")


# In[12]:


# Save the merged dataframe to the output directory
merged_df.to_csv(output_file, index=False)

print(f"Files merged and saved to {output_file}")


# In[ ]:





# In[ ]:




