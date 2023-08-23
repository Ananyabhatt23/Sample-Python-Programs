# Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable.
def swap(x,y):
  x,y = y,x
  return x,y

# Python Program to Check Whether a Number is Positive or Negative.
def checkIsPositive(a):
  if(a>0):
    return True

# Python Program to Print all Numbers in a Range Divisible by a Given Number. [ if range is from 1 
# to 20 and number is 4, then the result should be 4, 8, 12, 16 and 20. ]
def divisibilityCheck(limits,n):
     list_1 = []
     for i in range(1,limits+1):
          if i%n == 0:
               list_1.append(i)
     return list_1

# Python Program to Read Two Numbers and Print Their Quotient and Remainder.
def remAndquo(num1,num2):
    rem = num1%num2
    quo = num1//num2
    return (rem,quo)

# Python Program to Print Odd Numbers Within a Given Range.
def odd_num(n):
    oddlist = []
    for i in range(1,n):
        if i%2 != 0:
            oddlist.append(i)
    return(oddlist)
odd_num(10)

# Python Program to Find the Sum of Digits in a Number.
def sum_of_digits(n:int):
    sum = 0
    while n!=0:
        digit = int(n%10)
        sum += digit
        n = n//10
    return sum  

# Python Program to Find the Smallest Divisor of an Integer.
def smallest_divisor(n):
    a = []
    for i in range(2,n):
        if(n%i==0):
            a.append(i)
    return(min(a))

# Python Program to Reverse a Given Number.
def reverse_of_number(n):
    rev = 0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return rev


def pow_of_num(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + pow(n,i)
    return sum

# Python Program to Calculate the Average of Numbers in a Given List.
def avg_of_list():
    list_1 = [1,2,3,4,5]
    sumofVal = sum(list_1)
    avg = sumofVal//len(list_1)
    return avg


# Python Program to Count the Number of Digits in a Number
def number_of_digits(n):
    return len(str(n))


# Python Program to Check if a Number is a Palindrome.
def palindrome_of_num(n):
    val1 = reverse_of_number(n)
    if(n==val1):
        return val1
    return 0


# Python Program to return true if all characters in the string are alphabetic and there is at least one other character, False.
def char_of_string_is_true(n):
    return n.isalpha()


# Python Program to Replace all Occurrences of ‘a’ with $ in a String.
def occurance_of_a(name):
    return name.replace("a","$")


# Python Program to Count the Number of Vowels in a String.
def vowels_inString(name):
    count = 0
    for i in range(len(name)):
        if name[i] == "a" or name[i] == "e" or name[i] == "i" or name[i] == "o" or name[i] == "u":
            count = count + 1
    return count


# Python Program to Take in a String and Replace Every Blank Space with Hyphen.
def blank_spaceInString(name):
    return (name.replace(" ","-"))


# Python Program to find the length of string without using any built-in functions.
def length_of_String(name):
    count = 0
    for i in name:
        count = count+1
    return count


# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.
def larger_strings(sen1,sen2):
    count1 = 0
    count2 = 0
    for i in sen1:
        count1 = count1+1
    for j in sen2:
        count2 = count2+1
    if(count1<count2):
        return sen2
    return sen1


#  Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String
def upper_lowerCase(Sen:str):
    count1 = 0
    count2 = 0
    for i in Sen:
        if i.isupper() == 1:
            count1 = count1 + 1
        elif i.islower() == 1:
            count2 = count2 + 1
    return(count1,count2)
        

# Python Program to Calculate the Number of Digits and Letters in a String.
def numberLettersInString(sent:str):
    cnum = 0
    cstrng = 0
    for i in sent:
        if(i.isalpha()):
            cstrng = cstrng + 1
        elif(i.isdecimal()):
            cnum = cnum + 1
    return(cstrng,cnum)


# Python Program to check whether a full pattern (not sub string) is present in the given sentence.
raw_str = str(input("Enter String: "))
sub_string = str(input("Enter substring: "))
if(raw_str.find(sub_string) == -1):
    print("Not a subsrting")
else:
    print("Matching :)")


# Write a program to generate 10 random integers. 
import random
def random_num():
    for i in range(10):
        print(random.randint(10,20))

random_num()

# Write a program to generate 10 random integers between 1 to 20 (both inclusive).
def random_numFromOneToTwenty():
    for i in range(10):
        print(random.randint(1,20))

random_numFromOneToTwenty()

# Write a program to generate 5 random integers between 1 to 20 such that numbers should be unique.
unique = []
for i in range(5):
    rand = random.randint(1,20)
    if rand not in unique:
        print(rand)
        unique.append(rand)


# Write a program to generate 10 random numbers between 1 to 100 such that there should one number between 1 to 10 one number 
# between 11 to 20 etc.
list1 = []
count  = 0
for i in range(10):
    rand = random.randint(1,30)
    if(rand >= 1 & rand <= 10):
        count = count + 1
    elif(rand >= 11 & rand <=20):
        list1.append(rand)


# Python Program to print the number of occurrence of a sub string in a given string
def count_substring_occurrences(main_string, sub_string):
    count = main_string.count(sub_string)
    return count


#  Python program to print the lowest index in the string where substring sub is found within the string.
def lowest_index_of_substring(main_string, sub_string):
    index = main_string.find(sub_string)
    return index

#  Python Program to Read a number n and Compute n+nn+nnn.
def n_series():
    n = int(input("Enter a number: "))
    nn = int(str(n) + str(n))
    nnn = int(str(n) + str(n) + str(n))
    result = n + nn + nnn
    print(f"The result of {n} + {nn} + {nnn} is: {result}")

n_series()
