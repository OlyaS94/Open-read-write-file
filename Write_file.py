#!/usr/bin/env python
# coding: utf-8

# In[89]:


import os
import operator
def size(file1,file2):
    dict_m = {}
    with open (file1) as f, open (file2) as f2:
        lines = f.readlines()
        size = len(lines)
        lines2 = f.readlines()
        size2 = len(lines2)
        dict_m[file1]=size
        dict_m[file2]=size2
        sorted_values = sorted(dict_m.values())
        sorted_dict = {}
        for i in sorted_values:
            for k in dict_m.keys():
                if dict_m[k] == i:
                    sorted_dict[k] = dict_m[k]
        return(sorted_dict)


# In[107]:


def new_file(main_file):
    with open(main_file, 'w',encoding='utf-8') as file_main:
        dict_main = size('1.txt','2.txt')
        keys = list(dict_main.keys())
        values = list(dict_main.values())
        print(keys)
        file_main.write(f'{keys[0]}\n')
        file_main.write(f'{values[0]}\n')
        with open (f'{keys[0]}') as first, open (f'{keys[1]}') as second:
            f_1 = first.read()
            f_2 = second.read()
            file_main.write(f'{f_1}\n')
            file_main.write(f'{keys[1]}\n')
            file_main.write(f'{values[1]}\n')
            file_main.write(f'{f_2}\n')
size('1.txt','2.txt')
new_file('New_File.txt')

        
       


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




