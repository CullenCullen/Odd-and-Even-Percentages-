#Program Name: Odd and Even number Percentage Generator
#Author: Cullen Shortt
#Date: 12/4/2022
#Class: CSC 221
""" This program calculates how many values in a list of randomly generated integers are odd and how many are even 
with the following requirements: 
Get the number of values to be generated along with the range of values from the user(range always begins at 1). 
After calculating the total number of odd and even values, display the results and allow the user to continue to 
generate and count new sets of values until they choose to exit.
 """
import random #import random class to use functions to obtain random integers

validate = True #loop condition

#generates and returns random integer list
def getrandomint(nums, rangeend):
    x = 1
    numlist =[]
    while nums >= x: #condition statement 
        numlist.append(random.randint(1, rangeend)) #appends items to numlist
        nums = nums - 1
    return numlist

#calculates the percentage of even and odd numbers
def calcoddandeven(randomlist):
    oddnumcnt = 0
    evennumcnt = 0
    oddnumperc = 0
    evennumperc = 0

    for i in randomlist:
        if i % 2 == 1: 
            oddnumcnt += 1 #iterator for odd numbers
        elif i % 2 == 0:
            evennumcnt += 1 #iteraotr for even numbers

    oddnumperc = ((len(randomlist) - evennumcnt) / len(randomlist)) * 100 #calculates percentage of odd #s
    evennumperc =((len(randomlist) - oddnumcnt) / len(randomlist)) * 100 #calculates percentage of even #s
    print("Odd values:", f'{oddnumperc:.2f}%') #prints odd # percentage
    print("Even values:", f'{evennumperc:.2f}%') #prints even # percentage 
    

while validate == True: #while loop that promptes user for values and termination
  
  numnums = int(input("How many numbers do you want to generate?" )) #user prompt to get desired amount of numbers
  endrange = int(input("Enter high end of value range from 1 to: ")) #user prompt to get upper range
  
  randomlist = getrandomint(numnums,endrange) #calls method to generate random integer list
  calcoddandeven(randomlist) #calls method to get get percentage of odd and even numbers from list
  
  playagain = input("Do you want to generate a new set of values? Y/N :") #user prompt asking if they want to do again
  
  while playagain != 'Y' and playagain != 'y' and playagain != 'N' and playagain != 'n': #checks for valid input
    playagain = input("Please enter in either Y or N : ")

  if playagain == "N" or playagain == "n": #terminates program
    validate = False
  else:
    validate = True #program runs again
    
  
    
 


