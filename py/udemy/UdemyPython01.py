
##### TRUE OR FALSE TEST #####################
##boobquestion = input("Do you have boobs?")
#if boobquestion=="yes":
#    print("I have boobs. Oppai!")
#else: 
#    print("I dont have boobs. Flat justice.❤️‍🔥")

### True or False ID showing question.###################
#age = int(input('''
#How old are you? 
#Show me your ID!'''))
#age = int(age)

#age>=21

#if age>=21:
#    print('''Come on in and drink!
#    🍷🍸🍹🍺🍻🍾''')
#else: 
#    print("Go home kid!😠")

######################################################
### ELSE for every other option.

#color = "orange"

#if color == "green":
#    print("Beginner!")
#elif color == "blue":
#    print("Intermediate")
#elif color == "black":
#    print("ADVANCED!")
#else:
#    print("I have no idea what you are talking about!")

#first_name = input('What is your first name?')
#last_name = input('What is your last name?')
#print("***********************************")
#length = len(first_name)+len(last_name)

#if length>=12:
#    print(f"{first_name} {last_name} is longer than your average Australian name.")
#elif length>=5:
#    print(f"{first_name} {last_name}, that's a very short name!")
#print("*"*50)

#######################################
#import random  ##have to import things!
#print(random.randint(1,6))
######################### TWEET COUNTER #####
#tweet = input("enter your tweet")
#char_count = len(tweet)
#max_chars=130
#if char_count<max_chars:
#    print("It's not too long.")
#else: 
#    print(f"Your tweet is {char_count} is {char_count - max_chars } char tweet is too long ")

################ BMI CALCULATOR #################
#height = float(input("Enter your height"))
#weight = float(input("Enter your weight"))
#category = "none"
#bmi = ((weight*703) / (height ** 2))
#bmi = round(bmi,1)
#if bmi < 16:
#    category = "severely underweight"
#    print("You're underweight!")
#elif bmi <18.4:
#    category = "underweight"
#    print("Under weight.")
#elif bmi<24.9:
#    category = "normal"
#    print("Normal!")
#elif bmi <29.9:
#    category = "overweight"
#    print("Overweight")
#elif bmi < 34:
#    category = "obese"
#    print ("Obese")
#elif bmi < 39:
#    category = "morbidly obese"
#    print("Morbidly obese")

#print(f"Your BMI of {bmi} makes you {category}!")
###################################################
#num = 3<4 and 3>8
#if num == True and True:
#    print(num)
#else:
#    print("Thats wrong!")
################################################
#word = input("Type a word!:")

#if word[0]=="g" and len(word)>=3:
#    print("Word starts with G and is greater or less than three!")
#else:
#    print("Word invalid!")
################################################
#color = input("Enter a color!")
#if color:
#    print(f"{color} is my fave color too!")
#else:
#    print("NO.")

## 
#answer = input("Please say hi. :)")
#while answer !="hi":
#    answer=input("RUDE SAY HI.")
#print("Hi to you too!")

#count = 1;
#while count <=10:
    #print(f"Count is {count}.")
#    print("*"*count )
#    count+=1
#print("Count is greater than 10.")
#word = "asshole"
#for char in word:
#    print(char)

#for num in range(-5,10):
#    print(num)

#for num_bottles in range(99,0,-1): 
#    #stepping down means -1
#    print(f"{num_bottles} bottles of beer on the wall.")
#    print(f"{num_bottles} bottles of beer.")
#    if num_bottles==1:
#        print(f"Take one down, pass it around, no more bottles of beer on the wall.")
#    else:
#        print(f"Take one down, pass it around, {num_bottles-1} bottles of beer on the wall.")
#    print("*"*50)

#message = input("Say ass")
#while True:
#    if message =="ass":
#        break
#    message = input("please say ass")
#print("Finally! :)")
from random import randint
num_dice = int(input("How many dice are we rolling?"))
num_sides = int(input("How many sides are on each die?"))

while True:
    result="|"
    for die in range(num_dice):
        rand = randint(1,num_sides)
        result +=f"{rand}|"
    print(result)
    reply = input("Roll again? or type Q to quit:")
    if reply == "q":
        break












