# Python Program to Find the Largest Number in a List
def lareNumInList():
    list1 = [1,67,34,39,56]
    max = list1[0]
    for i in range(len(list1)):
        if(list1[i]>max):
            max = list1[i]
    return max

# Python Program to Find the Second Largest Number in a List
def secondLargestElemInList():
    list2 = [3,5,4]
    diff = {}
    maxele = max(list2)
    for i in range(len(list2)):
        if(maxele == list2[i]):
            continue
        diff[list2[i]] = maxele - list2[i]
    val = min(diff.values())
    for key, value in diff.items():
        if value == val:
            return key
        
# Python Program to Put Even and Odd elements in a List into Two Different Lists
def oddEvenList():
    filterlist = [1,2,3,4,5,6]
    evenList = []
    oddList = []
    for i in range(len(filterlist)):
        if(filterlist[i]%2==0):
            evenList.append(filterlist[i])
        else:
            oddList.append(filterlist[i])
    return evenList,oddList

# Python Program to check whether two lists are same.
def sameListorNot():
    list1 = [1,2,3]
    list2 = [1,2,3]
    if(list1 == list2):
        return True
    
# Python Program to Find the Union of Lists.
def UnionOfList():
    list1 = [1,2,3]
    list2 = [4,5,6]
    list3 = list1 + list2
    return list3

# Python Program to Find the Intersection of Lists.
def interscOfList():
    list1 = [1,2,3]
    list2 = [3,5,6]
    list3 = []
    for i in range(len(list1)):
        if(list1[i] in list2):
           list3.append(list1[i])
    return list3

# Python Program to find union and intersection of lists without repetition.
def intersecWithOutRepetition():
    list1 = [1,2,3,4]
    list2 = [2,3,4,5]
    list3 = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if(list1[i] == list2[j]):
                if(list2[j] not in list3):
                    list3.append(list2[j])
    print(list3)
intersecWithOutRepetition()

def unionOfListWithOutRep():
    list1 = [1,2,3,4]
    list2 = [2,3,4,5]
    list3 = []
    for i in range(len(list1)):
        if(list1[i] not in list3):
            list3.append(list1[i])
    for j in range(len(list2)):
        if(list2[j] not in list3):
            list3.append(list2[j])
    print(list3)

unionOfListWithOutRep()

# Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number.
def listOfTuple():
    square_tuple = ()
    for i in range(1,6):
        print(square_tuple.__add__((i,i*i)))

listOfTuple()

# Python Program to Remove the Duplicate Items from a List.
def removeDuplicate():
    list1 = [1,2,3,3,4,5,-5,-6]
    list2 = []
    for i in range(len(list1)):
        if(list1[i] not in list2):
            list2.append(list1[i])
    print(list2)

removeDuplicate()

# Python Program to Read a List of Words and Return the Length of the Longest One.
def lenOfLogestString():
    name1 = "Ananya"
    name2 = "Ramya"
    name3 = "Aditi"
    if(len(name1)>len(name2) and len(name1)>len(name3)):
        print(len(name1))
    elif(len(name2)>len(name1) and len(name2)>len(name3)):
        print(len(name2))
    else:
        print(len(name3))

lenOfLogestString()
    
        
# Python Program to Add a Key-Value Pair to the Dictionary
def decPair():
    my_dict = {'name': 'Ana', 'age': 22, 'city': 'Banglore'}
    new_key = 'job'
    new_value = 'Engineer'
    my_dict[new_key] = new_value
    print(my_dict)
decPair()

# Python Program to Concatenate Two Dictionaries Into One
def ConCatDict():
    myDisct1 = {'name1':"Ana",'age1':22}
    myDisct2 = {'name2':"Jenny",'age2':22}
    myDisct3 = {**myDisct1,**myDisct2}
    print(myDisct3)
ConCatDict()

# Python Program to Check if a Given Key Exists in a Dictionary or Not
def keyExists():
    d = {'name1':"A",'name2':"B"}
    key = "name2"
    if key in d.keys():
        print("Present")
    else:
        print("Not in dictionary")
keyExists()

# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
# o/p --> {'2':4,'3':9,'4':16}
def numDict(n):
    mydict = {}
    for i in range(n):
        mydict[i]=pow(i,2)
    print(mydict)

numDict(6)

# Python Program to Sum All the Items in a Dictionary
def sumOfItems():
    mydict = {1:7,2:2,3:4}
    print(sum(mydict.values()))
sumOfItems()

# Python Program to Multiply All the Items in a Dictionary
def mulOfItems():
    prod = 1
    mydict = {'A':2,'S':2,'Ss':4}
    for i in mydict.values():
        prod = prod*i
    print(prod)
mulOfItems()

# Python Program to Remove the Given Key from a Dictionary
def removeKey(key):
    mydict = {'A':2,'S':2,'Ss':4}
    mydict.pop(key)
    print(mydict)
removeKey("Ss")

#  Write a function is_empty(my_dict) that takes a dictionary my_dict and returns True if my_dict is empty and False otherwise.
my_dict1 = {}
def emptydict(my_dict):
    if(len(my_dict.keys()) == 0):
        print( True)
    else:
        print(False)
    
emptydict(my_dict1)
    
# Write a function make_dict(key_value_list) that takes a list of tuples key_value_list where each tuple is of the form (key, value) and 
# returns a dictionary with these keys and corresponding values.
def tupledect(t1,t2):
    created_dict = {}
    list_tuples = []
    list_tuples.append(t1)
    list_tuples.append(t2)
    for i in list_tuples:
        for j in range(len(i)):
            created_dict[i[j]] = i[j+1]
            break
    print(created_dict)

tupledect((2,3),(3,4))

# A simple substitution cipher is an encryption scheme where each letter in an alphabet to 
# replaced by a different letter in the same alphabet with the restriction that each letter's 
# replacement is unique. The template for this question contains an example of a substitution 
# cipher represented a dictionary CIPHER_DICTIONARY. Your task is to write a function 
# encrypt(phrase,cipher_dict) that takes a string phrase and a dictionary cipher_dict and returns 
# the results of replacing each character in phrase by its corresponding value in cipher_dict.

CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y':'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 
'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}
def encryptDict(string:str, CIPHER_DICT):
    # for i in string: #i=c,a,t
    #     for i in range(len(string)): #i=0,1,2
    for i in string:
        print(CIPHER_DICT[i])

encryptDict("ana",CIPHER_DICT)


# Write a function make_cipher_dict(alphabet) that takes a string of unique characters and 
# returns a randomly-generated cipher dictionary for the characters in alphabet . You should use 
# the shuffle() method in the random module to ensure that your returned cipher dictionary is 
# random.
import random

def make_cipher_dict(alphabet):
    cipher_dict = {}
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    for i, shuffled in zip(alphabet, shuffled_alphabet):
        cipher_dict[i] = shuffled
    print(cipher_dict)

make_cipher_dict("ananya")

# Write a python code to generate grade using dictionary. Dictionary should have student names 
# as keys (assuming names are unique) and subject_name and mark as value. There are 5 subjects 
# for each student. Marks should be converted to grades (90 – 100 A+, 80-89 A etc)

def calculate_grade(mark):
    if mark >= 90:
        return 'A+'
    elif mark >= 80:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 60:
        return 'C'
    else:
        return " "

def generate_grade_dictionary(student_data):
    grade_dict = {}
    for student, marks in student_data.items():
        subject_grades = {}
        for subject, mark in marks.items():
            subject_grades[subject] = calculate_grade(mark)
        grade_dict[student] = subject_grades
    return grade_dict

student_data = {
    'Rachel': {'APS': 85, 'BDA': 92, 'ML': 78, 'DSA': 90, 'ELE': 70},
    'Ross': {'APS': 95, 'BDA': 62, 'ML': 88, 'DSA': 90, 'ELE': 78},}

grade_dictionary = generate_grade_dictionary(student_data)
for student, grades in grade_dictionary.items():
    print(f"Grades for {student}:")
    for subject, grade in grades.items():
        print(f"  {subject}: {grade}")


    