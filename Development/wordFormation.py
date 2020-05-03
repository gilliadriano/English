# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:19:18 2020

@author: Casal 10
"""
import tkinter
from tkinter.ttk import *
import pandas as pd
import textwrap
from tkinter import messagebox


def clc(WordFormation):
    list = WordFormation.pack_slaves()
    for l in list:
        l.destroy()


def wordFormationExercise(Nright, Nexec):
    global i, exercise, already_tried, txt1, txt2, txt3, asw1, asw2, asw3, score, my_errors, exerciseList

    def clicked():
        global Nexec, Nright, already_tried, exercise, txt1, txt2, txt3, words, score, my_errors
        value1 = txt1.get()
        value2 = txt2.get()
        value3 = txt3.get()

        if already_tried:
            score["text"] = str((
                ((value1 == exercise[4]) * 1 + (value2 == exercise[5]) * 1 + (value3 == exercise[6]) * 1) / 3)*100)
        else:
            already_tried = True
            Nexec = Nexec + 3
            score["text"] = str((
                ((value1 == exercise[4]) * 1 + (value2 == exercise[5]) * 1 + (value3 == exercise[6]) * 1) / 3)*100)
            Nright = Nright + (value1 == exercise[4]) * 1 + (value2 == exercise[5]) * 1 + (value3 == exercise[6]) * 1
            words["text"] = "1." + exercise[4] + ", 2." + exercise[5] + ", 3." + exercise[6]
            if Nright != 3:
                my_errors = my_errors.append(exercise)

    def build_new(exercise):
        global I3, txt1, txt2, txt3, words, score
        # I0 is just a blank space.
        I0 = tkinter.Label(WordFormation, text=" ", font=("Arial Bold", 12)).pack()
        # Root Word 
        I0 = tkinter.Label(WordFormation, text="Word Formation: " + str(exercise[0]), font=("Arial Bold", 12)).pack()
        I0 = tkinter.Label(WordFormation, text=" ", font=("Arial Bold", 12)).pack()

        # 1st sentence
        firstSentence = textwrap.wrap("1 - " + exercise[1], width=80)
        for i in range(len(firstSentence)):
            tkinter.Label(WordFormation, text=firstSentence[i], font=("Arial bold", 12)).pack()

        # Text Entry
        txt1 = Entry(WordFormation, width=30)
        txt1.pack()
        I0 = tkinter.Label(WordFormation, text=" ", font=("Arial", 12)).pack()

        # 2nd sentence
        secondSentence = textwrap.wrap("2 - " + exercise[2], width=80)
        for i in range(len(secondSentence)):
            tkinter.Label(WordFormation, text=secondSentence[i], font=("Arial bold", 12)).pack()

        # Text Entry
        txt2 = Entry(WordFormation, width=30)
        txt2.pack()
        I0 = tkinter.Label(WordFormation, text=" ", font=("Arial", 12)).pack()

        # 3rd sentence
        thirdSentence = textwrap.wrap("3 - " + exercise[3], width=80)
        for i in range(len(thirdSentence)):
            tkinter.Label(WordFormation, text=thirdSentence[i], font=("Arial bold", 12)).pack()

        # Text Entry
        txt3 = Entry(WordFormation, width=30)
        txt3.pack()
        I0 = tkinter.Label(WordFormation, text=" ", font=("Arial", 12)).pack()

        # middleframe=Frame(WordFormation)
        # middleframe.pack()
        # Score calculation:
        I0 = tkinter.Label(WordFormation, text="Score: ", font=("Arial", 12)).pack()
        score = tkinter.Label(WordFormation, text="", font=("Arial", 12))
        score.pack()

        # lowerframe=Frame(WordFormation)
        # lowerframe.pack()

        I0 = tkinter.Label(WordFormation, text=" ", font=("Arial", 12)).pack()

        I0 = tkinter.Label(WordFormation, text="Words:", font=("Arial", 12)).pack()
        words = tkinter.Label(WordFormation, text=" ", font=("Arial", 12))
        words.pack()

        # The button Done corrects the exercise.
        I4 = tkinter.Button(WordFormation, text="Done", font=("Arial Bold", 12), width=30, command=clicked).pack(
            side="left")
        # The button Next ends this exercise.
        I5 = tkinter.Button(WordFormation, text="Next", font=("Arial Bold", 12), width=30, command=nxtquestion).pack(
            side="right")

    def nxtquestion():
        global i, exerciseList, already_tried, exercise, Nexec, Nright, my_errors
        if i < (len(exerciseList) - 1):
            clc(WordFormation)
            i = i + 1
            exercise = exerciseList.iloc[i]
            build_new(exercise)
            already_tried = False
        else:
            messagebox.showinfo("Resultado Final",
                                "O numero de acertos foi de " + str(Nright) + " em " + str(Nexec) + ". Ou " + str(
                                    Nright / Nexec * 100) + "%. O programa irá repetir os exercícios que não foram acertados de primeira.")
            if my_errors.empty == 1:
                WordFormation.destroy()
            else:
                clc(WordFormation)
                i = 0
                already_tried = False
                exerciseList = my_errors
                exercise = exerciseList.iloc[i]
                build_new(exercise)
                my_errors = pd.DataFrame(columns=['Root Word', 'Sentence1', 'Sentence2', 'Sentence3', 'Word1', 'Word2', 'Word3'])
                Nexec = 0
                Nright = 0

            #WordFormation.destroy()

    my_errors = pd.DataFrame(columns=['Root Word', 'Sentence1', 'Sentence2', 'Sentence3', 'Word1', 'Word2', 'Word3'])

    exercise = exerciseList.iloc[i]

    build_new(exercise)

    WordFormation.mainloop()


# Read excel repository
exerciseList = pd.read_excel('WordFormation.xls')

Nexec = 0
Nright = 0

WordFormation = tkinter.Tk()

WordFormation.title("Word Formation Exercise")
WordFormation.geometry("1200x600")
i = 0
already_tried = False
wordFormationExercise(Nright, Nexec)
