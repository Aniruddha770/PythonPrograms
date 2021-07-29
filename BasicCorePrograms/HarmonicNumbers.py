"""
   * Author - Aniruddha
   * Date -  27July2021
   * Time -  22:00
   * Title - Print the Nth Harmonic Value.
"""


def harmonic(number):
    i = 1
    sum = 0

    while i <= number:
        sum += 1 / i
        i += 1
        print(sum)


number = int(input("Enter Number: "))
if number <= 0:
    print("Please enter the no greater than zero.")
else:
    harmonic(number)
