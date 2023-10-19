#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
options=("rock","paper","scissor")
playing=True
player =None
while playing:
    computer =random.choice(options)
    player =input("enter a choice(rock,paper,scissor): ")
    if options.count(str(player))>0:
        print("player====",player)
        print(f"player:{player}")
        print(f"computer:{computer}")
        if player==computer:
            print("its a tie!")
        elif player=="rock" and computer=="scissor":
            print("you win!")
        elif player=="paper" and computer=="rock":
            print("you win!")
        elif player=="scissor" and computer=="paper":
            print("you win!")
        else:
            print("you lose!")
            play_again=input("play_again?(y/n)").lower()
            if not play_again=="y":
                running=False
                print("thanks for playing!")
    
    else:
        print(f"Please select any one of the choice (rock,paper,scissor)")
        running=True
        




# In[ ]:




