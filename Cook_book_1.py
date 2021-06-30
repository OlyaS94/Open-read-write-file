#!/usr/bin/env python
# coding: utf-8

# In[45]:


import os
def cook_book(file_n):
    c_book = {}
    list_1 = []
    with open(f'{file_n}', encoding ='utf-8') as file:
        for line in file:
            list_1.append(line.strip())
        for ind, val in enumerate(list_1):
            if val.isdigit():
                c_book[list_1[ind - 1]] = []
                for ingredient in list_1[ind + 1:ind + int(val) + 1]:
                    ingredient_name = ingredient.split('|')[0]
                    quantity = int(ingredient.split('|')[1])
                    measure = ingredient.split('|')[2]
                    c_book[list_1[ind - 1]].append({'ingredient_name': ingredient_name,
                                                          'quantity': quantity,
                                                          'measure': measure})
    return c_book
cook_book('recipe1.txt')


# In[47]:


def get_shop_list_by_dishes(dishes,book,person_count):
    for dish_name in dishes:
        if dish_name in book.keys():
            for value in book[dish_name]:
                value['quantity'] *= person_count
                res_1 = {}
                res_1['measure'] = value.get('measure')
                res_1['quantity'] = value.get('quantity')
                res = {}
                res[value.get('ingredient_name')] = res_1
                print(res)
                        
                    
get_shop_list_by_dishes(['Запеченный картофель','Омлет'],cook_book('recipe1.txt'), 2)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




