__author__ = 'SerifPerida'

#import modules
import math


#print start
print("")
print("| Statistical Data Value Counter |")
print("----------------------------------")
print("")

#ask data values
num = []
print("Enter data set separated with commas (e.g 1, 2, 3, 4, 5)")
print("! NOTE: Do not add any 0s as that will add to the array count. !")
print("! Remember that the 0s in a set array does not count in mathematics. !")
dataset=input("Data Set: ")

#data sorting
print("")
print('Compiling Data...')
n = ''
for i in range(len(dataset)):
    if dataset[i]==',':
        num.append(float(n))
        n = ''
    else:
        n += dataset[i]
num.append(float(n))

numlength = len(num)
num.sort()
print("Data Loaded!")
print("")

#ask what calculation
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
    return (num[float((numlength/2)-1)] + num[float(numlength/2)])/2
  else:
    return num[math.ceil(numlength/2)-1]


#range
def ranges():
  return num[numlength-1]-num[0]

#ifstates
print("")
print("Running Scripts...")
print("")
print("The array you have inputed is: ", num)
if calc=="mean":
    print("The mean of the data set is:", + mean())
if calc=="mad":
    print("The mad of the data set is:", + mad())
if calc=="median":
    print("The median of the data set is:", + median())
if calc=="ranges":
    print("The range of the data set is:", + ranges())

#input exit
print("")
print("Thank you for using the Statistical Data Value Counter.")
enter = input('Press enter key to exit')
if enter:
    exit(0)
