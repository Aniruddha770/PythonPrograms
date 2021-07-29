"""
   * Author - Aniruddha
   * Date -  27July2021
   * Time -  17:59
   * Title - User Input and Replace String Template
"""
name = input("Please Enter Name:")
name = str(name)
nameLength = len(name)
if nameLength >= 3:
 print(nameLength)
 print("Hello "+name+" How are you?")
else: print("Invalid Name")