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

def clc(phrasalVerb):
    list = phrasalVerb.pack_slaves()    
    for l in list:
        l.destroy()
    

def phrasalExercise(Nright,Nexec):
    global already_tried,I6,I3,i,exercise,exerciseList,my_errors
    
    def clicked():
        global Nexec,Nright,already_tried,I6,I3,exercise,my_errors
        value = I3.get()

        if (value == exercise[3]):
            if already_tried:
                I6.destroy()
                I6 = tkinter.Label(phrasalVerb,text="Correct",bg="green",font=("Arial Bold",15))
                I6.pack()
            else:
                I6 = tkinter.Label(phrasalVerb,text="Correct",bg="green",font=("Arial Bold",15))
                I6.pack()
                already_tried=True
                Nexec=Nexec+1
                Nright=Nright+1
        else:
            if already_tried:
                I6.destroy()
                I6 = tkinter.Label(phrasalVerb,text="Incorrect",bg="red",font=("Arial Bold",15))
                I6.pack()
            else:
                I6 = tkinter.Label(phrasalVerb,text="Incorrect",bg="red",font=("Arial Bold",15))
                I6.pack()
                Nexec=Nexec+1
                already_tried=True
                my_errors=my_errors.append(exercise)
    
    def build_new(exercise):
        global I3
        # I0 is just a blank space.
        I0 = tkinter.Label(phrasalVerb,text=" ",font=("Arial Bold",15)).pack()
        
        # Definition.... first a test to see if it will pass the maximum number of characters
        PhrVrb = textwrap.wrap("Phrasal Verb: " + exercise[0],width=80)
        for i in range(len(PhrVrb)):
            I1 = tkinter.Label(phrasalVerb,text= PhrVrb[i],font=("Arial bold",15)).pack()
        I0 = tkinter.Label(phrasalVerb,text=" ",font=("Arial",15)).pack()
        
        
        # Phrase with Phrasal verb
        Phrase = textwrap.wrap(exercise[1],width=80)
        for i in range(len(Phrase)):
            I2 = tkinter.Label(phrasalVerb,text= Phrase[i],font=("Arial normal",15)).pack()
        I0 = tkinter.Label(phrasalVerb,text=" ",font=("Arial",15)).pack()   
            
        # Combobox
        I3 = Combobox(phrasalVerb,font=("Arial",12), width = 25)
        
        # The values are all in the same cell, separated by commas.
        values = exercise[2].split(',')
        I3["values"]=values
        I3.current = 0
        
        I3.pack()
        
        # The button Done corrects the exercise.
        I4 = tkinter.Button(phrasalVerb,text="Done",font=("Arial Bold",12),width=30,command=clicked).pack(side="left")
        # The button Next ends this exercise.
        I5 = tkinter.Button(phrasalVerb,text="Next",font=("Arial Bold",12),width=30,command=nxtquestion).pack(side="right")
        
    def nxtquestion():
        global i, exerciseList, already_tried, I3, exercise, Nexec, Nright, my_errors
        if i<(len(exerciseList)-1):
            clc(phrasalVerb)
            i = i+1
            exercise = exerciseList.iloc[i]
            build_new(exercise)
            already_tried = False
        else:
            messagebox.showinfo("Resultado Final","O numero de acertos foi de "+str(Nright)+" em "+ str(Nexec)+". Ou "+ str(Nright/Nexec*100)+"%. O programa irá repetir os exercícios que não foram acertados de primeira.")
            if my_errors.empty==1:
                phrasalVerb.destroy()
            else:
                clc(phrasalVerb)
                i = 0
                already_tried = False
                exerciseList = my_errors
                exercise = exerciseList.iloc[i]
                build_new(exercise)
                my_errors = pd.DataFrame(columns=['Definition','Phrase','Options','Right Option'])
                Nexec = 0
                Nright = 0
    
    my_errors = pd.DataFrame(columns=['Definition','Phrase','Options','Right Option'])
    
    exercise = exerciseList.iloc[i]
    
    build_new(exercise)    
    
    phrasalVerb.mainloop()

    return my_errors

#----------Main Program  

# Read excel repository
exerciseList = pd.read_excel('PhrasalVerb.xls')

Nexec = 0
Nright = 0

phrasalVerb = tkinter.Tk()
    
phrasalVerb.title("Phrasal Verb Exercise")
phrasalVerb.geometry("1200x500+10+10")
i=0
already_tried = False
phrasalExercise(Nright,Nexec)
