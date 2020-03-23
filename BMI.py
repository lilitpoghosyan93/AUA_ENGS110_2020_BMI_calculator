#!/usr/bin/env python
# coding: utf-8

# In[7]:


import json


# In[10]:


f = open("data.json")  
info = json.load(f)


# In[11]:


info


# In[54]:


def bmi_calc():
    oldBMI = None
    name = input('Insert your name: ')

    height = input('Insert your height [Centimeter]: ')
    height = float(height)

    weight = input('Insert your weight [Kilogram]: ')
    weight = float(weight)


    H_2 = height*height
    W_2 = weight

    bmi = W_2/H_2
    
    new_data = {'name' : name,
                'height' : height,
                'weight' : weight,
                'bmi' : bmi
    }
    
    for i in info:
        if new_data["name"] == i["name"]:
            oldBMI = i["bmi"]
            break
    


    info.append(new_data)

    with open("data.json", 'a', encoding = 'utf-8') as f:
        json.dump(info, f, ensure_ascii = False)
    

    if bmi < 18.5:
            print('You are underweight')

    elif bmi > 18.5 and bmi < 24.9:
            print('You are normal')

    elif bmi > 25 and bmi < 29.9:
            print('You are overweight')

    else:
            print('You are obese')
            
            
    if (oldBMI != None):
        if oldBMI > bmi:
            print('You decrease your BMI rate')
        elif oldBMI < bmi:
            print('You increase your BMI rate')
        else:
                print('You keep your BMI rate')




    
        
        
        
        


# In[55]:


def mainFunc():
    print('Welcome to the BMI system')
    bmi_calc()
    soal = input('Do you want to continue?[y/n]: ')
    while soal != 'n':
        bmi_calc()
        soal = input('Do you want to continue?[y/n]: ')


# In[ ]:


mainFunc()

