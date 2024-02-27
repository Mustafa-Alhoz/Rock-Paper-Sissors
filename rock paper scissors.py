import random


enterance = '''
    _______             _______                _______
---'   ____)        ---'   ____)____       ---'   ____)____
      (_____)                 ______)                 ______)
      (_____)                 _______)              __________)
      (____)                _______)             (____)
---.__(___)       ---.__________)          ---.__(___)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)
'''
print(enterance)
print("\nWLECOME TO THE ROCK , PAPER , SCISSORS GAME \nTHIS GAME WAS MADE BY THE BEST PROGRAMMER EVER @mustafa_alhoz")
user_choice=input("\nPLEASE TYPE \n===> R  FOR ROCK \n===> P  FOR PAPER \n===> S  FOR SCISSORS\n").lower()
pc_choice=random.randint(0,2)




if pc_choice==0:
    if  user_choice=="r":
        print(f"YOUR CHOICE IS : \n{rock}")
        print(f"COUMPUTER'S CHOICE IS : \n{rock}")
        print("THE RESULT IS : DRAW\n")
    elif user_choice=="p":
        print(f"YOUR CHOICE IS : \n{paper}")
        print(f"COUMPUTER'S CHOICE IS : \n{rock}")
        print("THE RESULT IS : YOU WON\n")
    elif user_choice=="s":
        print(f"YOUR CHOICE IS : \n{scissors}")
        print(f"COUMPUTER'S CHOICE IS : \n{rock}")  
        print("THE RESULT IS : YOU LOST\n") 
    else :
        print("IT IS NOT THAT HARD TO TYPE A LETTER\n")     
elif pc_choice==1:
    if  user_choice=="r":
        print(f"YOUR CHOICE IS : \n{rock}")
        print(f"COUMPUTER'S CHOICE IS : \n{paper}")
        print("THE RESULT IS : YOU LOST\n")
    elif user_choice=="p":
        print(f"YOUR CHOICE IS : \n{paper}")
        print(f"COUMPUTER'S CHOICE IS : \n{paper}")
        print("THE RESULT IS : DRAW\n")
    elif user_choice=="s":
        print(f"YOUR CHOICE IS : \n{scissors}")
        print(f"COUMPUTER'S CHOICE IS : \n{paper}")  
        print("THE RESULT IS : YOU WON\n") 
    else :
        print("IT IS NOT THAT HARD TO TYPE A LETTER\n")     
else:   
    if  user_choice=="r":
        print(f"YOUR CHOICE IS : \n{rock}")
        print(f"COUMPUTER'S CHOICE IS : \n{scissors}")
        print("THE RESULT IS : YOU WON\n")
    elif user_choice=="p":
        print(f"YOUR CHOICE IS : \n{paper}")
        print(f"COUMPUTER'S CHOICE IS : \n{scissors}")
        print("THE RESULT IS : YOU LOST\n")
    elif user_choice=="s":
        print(f"YOUR CHOICE IS : \n{scissors}")
        print(f"COUMPUTER'S CHOICE IS : \n{scissors}")  
        print("THE RESULT IS : DRAW\n") 
    else :
        print("IT IS NOT THAT HARD TO TYPE A LETTER\n")     


