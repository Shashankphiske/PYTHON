from cgitb import text
from cmath import e
from hashlib import new
from multiprocessing.connection import answer_challenge
from tkinter import E
from turtle import pos, position
from art import logo
answer = input("do you want to continue :yes or no :")
while answer == "yes":
    print(logo)
    answer = ""
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    word = input("give your text :").lower()
    choice = int(input("do you want to encrypt or decrypt ?give 1 or 2 "))
    shifting = int(input("how much is the shift :"))
    
    def encryption(text ,shift,real_choice):
        real_text = ""

        if real_choice == 1:
            for i in text:
                if i not in alphabet:
                    real_text += i
                else:
                    position = alphabet.index(i)
                    if position + shift > 25:
                        position = position + shift - 25 
                        
                    else:
                        position += shift 
                    new_word = alphabet[position]
                    real_text += new_word 
               
        else:
            for i in text:
                if i not in alphabet:
                    real_text += i
                else:
                    position = alphabet.index(i)
                    if position - shift < 0:
                        position = position - shift + 25 
                    else:
                        position -= shift 
                    new_word = alphabet[position]
                    real_text += new_word 
                
        print(real_text)
    encryption(text = word, shift = shifting,real_choice = choice)
    answer = input("do you want to continue:  yes or no :")                            
      


  