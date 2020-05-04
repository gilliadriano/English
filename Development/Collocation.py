# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:26:55 2020

@author: Casal 10
"""
import tkinter
from tkinter.ttk import *
import pandas as pd
import textwrap
from tkinter import messagebox

def clc(frameobj):
    elements = frameobj.pack_slaves()
    for l in elements:
        l.destroy()

def collocationExercise2():
    global already_tried, i, exercise, my_errors, exerciseList2, Nexec, Nright
    
    def clicked():
        global Nexec, Nright, already_tried, I6, I3, exercise, my_errors
        value = I3.get()

        if (value == exercise[3]):
            if already_tried:
                I6.destroy()
                I6 = tkinter.Label(collocation,text="Correct",bg="green",font=("Arial Bold",15))
                I6.pack()
            else:
                I6 = tkinter.Label(collocation,text="Correct",bg="green",font=("Arial Bold",15))
                I6.pack()
                already_tried=True
                Nexec=Nexec+1
                Nright=Nright+1
        else:
            if already_tried:
                I6.destroy()
                I6 = tkinter.Label(collocation,text="Incorrect",bg="red",font=("Arial Bold",15))
                I6.pack()
            else:
                I6 = tkinter.Label(collocation,text="Incorrect",bg="red",font=("Arial Bold",15))
                I6.pack()
                Nexec = Nexec+1
                already_tried = True
                my_errors = my_errors.append(exercise)
    
    def build_new(exercise):
        global I3
        # I0 is just a blank space.
        I0 = tkinter.Label(collocation,text=" ",font=("Arial Bold",15)).pack()
        
        I0 = tkinter.Label(collocation,text="Please write a word that fits the three sentences.",font=("Arial Bold",15)).pack()
        
        I0 = tkinter.Label(collocation,text=" ",font=("Arial Bold",15)).pack()
        
        sentence1 = textwrap.wrap(exercise[0],width=80)
        for i in range(len(sentence1)):
            I1 = tkinter.Label(collocation,text= sentence1[i],font=("Arial bold",15)).pack()
        I0 = tkinter.Label(collocation,text=" ",font=("Arial",15)).pack()
        
        sentence2 = textwrap.wrap(exercise[1],width=80)
        for i in range(len(sentence2)):
            I1 = tkinter.Label(collocation,text= sentence2[i],font=("Arial bold",15)).pack()
        I0 = tkinter.Label(collocation,text=" ",font=("Arial",15)).pack()
        
        sentence3 = textwrap.wrap(exercise[2],width=80)
        for i in range(len(sentence3)):
            I1 = tkinter.Label(collocation,text= sentence3[i],font=("Arial bold",15)).pack()
        I0 = tkinter.Label(collocation,text=" ",font=("Arial",15)).pack()
            
        # Entry
        I3 = Entry(collocation,font=("Arial",12), width = 25)
        I3.pack()
        
        # The button Done corrects the exercise.
        I4 = tkinter.Button(collocation,text="Done",font=("Arial Bold",12),width=30,command=clicked).pack(side="left")
        # The button Next ends this exercise.
        I5 = tkinter.Button(collocation,text="Next",font=("Arial Bold",12),width=30,command=nxtquestion).pack(side="right")
        
    def nxtquestion():
        global i, exerciseList2,already_tried,I3,exercise,Nexec,Nright, my_errors
        if i<(len(exerciseList)-1):
            clc(collocation)
            i = i+1
            exercise = exerciseList2.iloc[i]
            build_new(exercise)
            already_tried = False
        else:
            messagebox.showinfo("Resultado Final","O numero de acertos foi de "+str(Nright)+" em "+ str(Nexec)+". Ou "+ str(Nright/Nexec*100)+"%. O programa irá repetir os exercícios que não foram acertados de primeira.")
            if my_errors.empty==1:
                collocation.destroy()
            else:
                clc(collocation)
                i = 0
                already_tried = False
                exerciseList2 = my_errors
                exercise = exerciseList2.iloc[i]
                build_new(exercise)
                my_errors = pd.DataFrame(columns=['Definition','Phrase','Options','Right Option'])
                Nexec = 0
                Nright = 0

    my_errors = pd.DataFrame(columns=['Sentence 1','Sentence 2','Sentence 3','word'])

    exercise = exerciseList2.iloc[i]
    
    build_new(exercise)    
    
    collocation.mainloop()

def collocationExercise1():
    global already_tried,i,exercise,exerciseList,my_errors,Nexec,Nright

    def clicked():
        global Nexec,Nright,already_tried,I6,I3,exercise,my_errors
        value = I3.get()
        if (value == exercise[3]):
            if already_tried:
                I6.destroy()
                I6 = tkinter.Label(collocation,text="Correct",bg="green",font=("Arial Bold",15))
                I6.pack()
            else:
                I6 = tkinter.Label(collocation,text="Correct",bg="green",font=("Arial Bold",15))
                I6.pack()
                already_tried=True
                Nexec=Nexec+1
                Nright=Nright+1
        else:
            if already_tried:
                I6.destroy()
                I6 = tkinter.Label(collocation,text="Incorrect",bg="red",font=("Arial Bold",15))
                I6.pack()
            else:
                I6 = tkinter.Label(collocation,text="Incorrect",bg="red",font=("Arial Bold",15))
                I6.pack()
                Nexec=Nexec+1
                already_tried=True
                my_errors = my_errors.append(exercise)
    
    def build_new(exercise):
        global I3
        # I0 is just a blank space.
        I0 = tkinter.Label(collocation,text=" ",font=("Arial Bold",15)).pack()
        
        # Definition.... first a test to see if it will pass the maximum number of characters
        PhrVrb = textwrap.wrap("Phrasal Verb: " + exercise[0],width=80)
        for i in range(len(PhrVrb)):
            I1 = tkinter.Label(collocation,text= PhrVrb[i],font=("Arial bold",15)).pack()
        I0 = tkinter.Label(collocation,text=" ",font=("Arial",15)).pack()
        
        
        # Phrase with Phrasal verb
        Phrase = textwrap.wrap(exercise[1],width=80)
        for i in range(len(Phrase)):
            I2 = tkinter.Label(collocation,text= Phrase[i],font=("Arial normal",15)).pack()
        I0 = tkinter.Label(collocation,text=" ",font=("Arial",15)).pack()   
            
        # Combobox
        I3 = Combobox(collocation,font=("Arial",12), width = 25)
        
        # The values are all in the same cell, separated by commas.
        values = exercise[2].split(',')
        I3["values"]=values
        I3.current = 0
        
        I3.pack()
        
        # The button Done corrects the exercise.
        I4 = tkinter.Button(collocation,text="Done",font=("Arial Bold",12),width=30,command=clicked).pack(side="left")
        # The button Next ends this exercise.
        I5 = tkinter.Button(collocation,text="Next",font=("Arial Bold",12),width=30,command=nxtquestion).pack(side="right")
        
    def nxtquestion():
        global i, exerciseList,already_tried,I3,exercise,Nexec,Nright,my_errors
        if i<(len(exerciseList)-1):
            clc(collocation)
            i = i+1
            exercise = exerciseList.iloc[i]
            build_new(exercise)
            already_tried = False
        else:
            messagebox.showinfo("Resultado Final","O numero de acertos foi de "+str(Nright)+" em "+ str(Nexec)+". Ou "+ str(Nright/Nexec*100)+"%. O programa irá repetir os exercícios que não foram acertados de primeira.")
            if my_errors.empty==1:
                collocation.destroy()
            else:
                clc(collocation)
                i = 0
                already_tried = False
                exerciseList = my_errors
                exercise = exerciseList.iloc[i]
                build_new(exercise)
                my_errors = pd.DataFrame(columns=['Definition','Phrase','Options','Right Option'])
                Nexec = 0
                Nright = 0

    my_errors = pd.DataFrame(columns=['Definition','Sentence','options','correct Option'])

    exercise = exerciseList.iloc[i]
    
    build_new(exercise)    
    
    collocation.mainloop()
    
#----------Main Program  

# Read excel repository
#fileName = "Collocation.xls"
exerciseList = pd.read_excel("Collocation.xls",sheet_name="type1")
exerciseList2 = pd.read_excel("Collocation.xls",sheet_name="type2")
Nexec = 0
Nright = 0
collocation = tkinter.Tk()
    
collocation.title("Collocation type 1 Exercise")
collocation.geometry("1200x450+10+10")
i=0
already_tried = False
collocationExercise1()

# Second type of exercise.
collocation = tkinter.Tk()
collocation.title("Collocation type 2 Exercise")
collocation.geometry("1200x500+10+10")
i=0
Nexec = 0
Nright = 0
already_tried = False
collocationExercise2()

