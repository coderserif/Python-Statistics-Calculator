__author__ = 'SerifPerida'

#import modules
import math
import time


#print start
print("")
print("| Statistical Data Value Counter |")
print("----------------------------------")


#ask data values
print("")
print("Loading...")
time.sleep(1)
print("Running Startup...")
time.sleep(0.8)
print("Booting Compiler...")
time.sleep(0.5)
print("")
num = []
print("Enter data set separated with commas (e.g 1, 2, 3, 4, 5)")
print("! NOTE: Do not add any 0s as that will add to the array count. !")
print("! Remember that the 0s in a set array does not count in mathematics. !")
dataset=input("Data Set: ")

#data sorting
n = ''
for i in range(len(dataset)):
    if dataset[i]==',':
        num.append(int(n))
        n = ''
    else:
        n += dataset[i]
num.append(int(n))

numlength = len(num)
num.sort()


#ask what calculation
print("")
print("Compiling Data...")
time.sleep(1)
print("")
print("Thank you for inputing your values. What would you like to calculate?")
print("Type: 'mean', 'mad', 'median', or 'ranges'")
calc=input("Calculate the ")


#mean
def mean():
  mean = 0
  for i in range(numlength):
    mean += num[i]
  else:
    mean /= numlength
  return mean


#mad
def mad():
  madarr = []
  m = mean()
  for i in range(numlength):
    if num[i]>m:
      madarr.append(num[i] - m)
    else:
      madarr.append(m - num[i])
  else:
    mad = 0
    for i in madarr:
      mad += i
    mad /= numlength
    return mad


#median
def median():
  if not (numlength%2):
    return (num[int((numlength/2)-1)] + num[int(numlength/2)])/2
  else:
    return num[math.ceil(numlength/2)-1]


#range
def ranges():
  return num[numlength-1]-num[0]


#ifstates
print("")
if calc=="mean":
    print("")
    print("Running Scripts...")
    time.sleep(1)
    print("")
    print("The array you have inputed is: ", num)
    print("The mean of the data set is:", + mean())
if calc=="mad":
    print("")
    print("Running Scripts...")
    time.sleep(1)
    print("")
    print("The array you have inputed is", num)
    print("The mad of the data set is:", + mad())
if calc=="median":
    print("")
    print("Running Scripts...")
    time.sleep(1)
    print("")
    print("The array you have inputed is", num)
    print("The median of the data set is:", + median())
if calc=="ranges":
    print("")
    print("Running Scripts...")
    time.sleep(1)
    print("")
    print("The array you have inputed is", num)
    print("The range of the data set is:", + ranges())

#cool user input
print("")
print("Thank you for using the Statistical Data Value Counter.")
enter = input('Press enter key to exit')
if enter:
    exit(0)
