"""
   * Author - Aniruddha
   * Date -  27July2021
   * Time -  18:15
   * Title - Flip Coin and print percentage of Heads and Tails
"""
import random

number = input("Please Enter the number:")
number = int(number)
if number <= 0:
    print("Please Enter Positive Integer")
head = 0
tail = 0
for i in range(number):
    coin = random.randint(0, 1)
    if coin <= 0.5:
        print("Tails")
        tail += 1
        tailpercent = (tail / number) * 100
        print(tailpercent)
    else:
        print("Heads")
        head += 1
        headpercent = (head / number) * 100
        print(headpercent)
