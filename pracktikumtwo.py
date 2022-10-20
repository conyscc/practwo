#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import shutil
import datetime

def create_file(name, text=None):
    with open(os.getcwd() + '\\' + name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)
            
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже существует')
        
        
def get_list(folders_only=False):
    result =os.listdir()
    if folders_only:
        result ={i for i in result if os.path.isdir(i)}
    print(result)

def delete_file(name):
    if os.path.isdir(os.getcwd() + '\\' + name):
        os.rmdir(os.getcwd() + '\\' + name)
    else:
        os.remove(os.getcwd() + '\\' + name)
    

def copy_file(name, new_name, new_dir = None):
    try:
        if os.path.isdir(os.getcwd() + '\\' + name):
            try:
                shutil.copytree(os.getcwd() + '\\' + name, os.getcwd() + '\\' + new_name)
            except FileExistsError:
                print('Такая папка уже существует')
        else:
            shutil.copy(os.getcwd() + '\\' + name, os.getcwd() + '\\' +  new_name)
            if new_dir:
                move_file(os.getcwd() + '\\'  + new_name, new_dir)
    except FileNotFoundError:
        print('Такого файла не существует')
        
def rename_file(name, new_name):
    try:
        os.rename(os.getcwd() + '\\' + name, os.getcwd() + '\\' + new_name)
    except FileNotFoundError:
        print("Не существует такого файла")
        
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result +'\n')
        
def add_text_to_file(name, text):
    try:
        with open(os.getcwd() + '\\' + name, 'a', encoding='utf8') as f:
            f.write(text)
    except FileNotFoundError:
        print("Не существует такого файла")
        
def show_text_file(name):
    try:
        with open(os.getcwd() + '\\' + name, 'r', encoding='utf8') as f:
            print(f.read())
    except FileNotFoundError:
        print("Не существует такого файла")
        
def change_directory(new_dir):
    try:
        os.chdir(new_dir)
    except FileNotFoundError:
        print('Не существует такой папки')
        
def go_to_the_root():
    os.chdir('C:\\practwo')
        
def move_file(name, which_dir):
    try:
        os.replace(os.getcwd() + '\\' + name, which_dir)
    except FileNotFoundError:
        print('Не существует такой папки')


# In[8]:


os.getcwd()


# In[9]:


create_folder('library')


# In[ ]:




