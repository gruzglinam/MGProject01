import math
import re
import MyFunctions
import asyncio


"""
from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

lbl1 = Label(window, text="Hello")
lbl1.grid(column=0, row=0)

lbl2 = Label(window, text="Here you go", font=("Arial Bold", 50))
lbl2.grid(column=0, row=30)

window.mainloop()

xxxxx = 0
"""

# xx1 = 5
# exval = "(xx1 + 2) * 3 + xx1*xx1*xx1"
#
# calc = eval(exval)


# async def main():
#     print('hello')
#     await asyncio.sleep(3)
#     print('world')
#
# asyncio.run(main())
#
# x = 22
#
# pass


# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt).lower()
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
#
#
# ask_ok("Continue? ", 3, "Try more")
#
#
# pass
#
# lst77 = ["?", "!", ".", ":", ";", ","]

# Learning Files Input abd Output April 2

def fnc_skiplines(f, n):
    for i in range(n):
        next(f)
    return


lstsss = ['Alice', 'Mayya', 'Vera', 'Aaron', 'Maple', 'Linden', 'Oak', 'Mum', 'Tenor', ' Reason', 'Aaron', 'Memphis', 'Aaron']
lstsss.remove('Aaron')

file_sample = open("SampleFile.txt", "r+", encoding='utf8', errors='ignore')
text = file_sample.read()
lst_txt = text.split('\n')

for i in range(0, len(lst_txt)):
    if re.match(r'^\s*$', lst_txt[i]):
        lst_txt[i] = ''

while True:
    try:
        lst_txt.remove('')
    except ValueError:
        break

file_sample.seek(0, 0)
for item in lst_txt:
    file_sample.write(item + '\n')


file_sample.close()


eeev1 = '45*3 - (12+34)/2'
eeev2 = eval('45*3 - (12+34)/2')

lst2001 = '[45, "hello", 56, 78.56, "mayya", [109, 56, "vesna", 67, 8], 890]'
lst2002 = eval(lst2001)

MyFile = open("Myfile1.txt", "a+")
# for inx in range(10):
#    MyFile.write("%s\n" % (['a', 'b', 'c', (inx+1)]))

MyFile.seek(0, 0)

sum = 0

fnc_skiplines(MyFile, 11)

for line in MyFile:
   xval = line
   lstvar1 = eval(line)
#  lstvar2 = line.strip('[').strip(']').split(", ")
#   sum += lstvar1[3]
   for curr_elm in lstvar1:
       if type(curr_elm) == int:
           sum += curr_elm

print("Total: %s " % (sum))










# f = open("migfile.txt", "a+")
#
# for i in range(10):
#     f.write("This is a new line %d\n" % (i+1))
#
# f.seek(0, 0)
#
# # f01 = open("migfile.txt", "r")
#
# for line in f:
#     print(line, lineend=' ')

MyFile.close()

# Learning Files input and output April 01

x = MyFunctions.fnc_fnd_max([11, 22, 33, 44])




# 03.31.2020 learning Input @ Output

flt01 = 3627365845.329

print("To {1:#^28,.4f} be {0:10} ot not {0:30} to be? This is the question".format(451, flt01 ))


qs = "quoted \t\tstring"
print( f'{qs}' )

print( f'{"quoted string"}' )



lit_name = 'Mayya'
lit_age = 60

format_lt = f'I know {lit_name}\'s age is {lit_age}'
print(format_lt)



yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
teststr = '{:12} YES votes {:-21.4%}'.format(yes_votes, percentage + 2.3)
print(teststr)


a = [0, 1, 2]
for element in a:
    if not element:
        pass
    print(element)

for element in a:
    if not element:
        continue
    print(element)

# change this code
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")



string01 = " Today I am learning  text formatting"

print("Length of string01 = %d" % len(string01))
print("The first occurrence of the letter I = %d" % string01.index("I"))
print("The total num of letter t used in string = %d" % string01.lower().count("t"))

# boolean variables to evaluate conditions.
x = 2
print("testing boolean if x = 2 :",  (x == 2))
print(x == 3)
print(x < 3)

name = "Mayya"
if name in ["Mayya", "Rick"]:
    print("Your name is either Mayya or Rick.")



class Pair():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = "Great"

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r}, {0.name!r})'.format(self)

    def __str__(self):
        return 'instance Pair({0.x!s}, {0.y!s})'.format(self)

pair1 = Pair(7, 12)
vrepr = pair1.__repr__()
vstr  = pair1.__str__()

print(pair1)
print(vrepr)
print(vstr)





print(dir())


class Day():
    def __init__(self, pvisit, pcontact):
        self.visit = pvisit
        self.contact = pcontact

    def __add__(self, pday):
         return Day(self.visit + pday.visit, self.contact + pday.contact)


d1 = Day(5, 7)
d2 = Day(3, 9)
d3 = Day(5, 2)
d4 = d1 + d2
d5 = d1 + d2 + d3

# var1 = 35 + 3*(43 - 15)

# interview question - find the largest number in the list


lst_interview = [11, 22, -33, 44, 55, 66, 77, 88, 99]

# var_sum = sum(lst_interview, 7)
varx = lst_interview[-1]
varx = lst_interview[-6:-1]
var_sum = sum(lst_interview[-6:-2])







# lst_interview = [11]


# def fnc_fnd_max(plist):
#     max = plist[0]
#
#     for inx in range(1, len(lst_interview)):
#         if plist[inx] > max:
#             max = plist[inx]
#     return max


max_back = fnc_fnd_max(lst_interview)
print("max_back :", max_back)


# project: get familiar with CLASS 03/26/2020

class Car:

    def __init__(self, pmake, pmodel, pyear, pcolor):
        self.make = pmake
        self.model = pmodel
        self.year = pyear
        self.color = pcolor

    def __eq__(self, p_other_car):
        if self.make == p_other_car.make and self.model == p_other_car.model and self.year == p_other_car.year:
            return True
        else:
            return False

    def all_info(self):
        return self.make + ' ' + self.model + ' ' + str(self.year) + ' ' + self.color


car101 = Car("Honda", "Accord", 1995, "orange")
car102 = Car("Honda", "Civic", 2010, "white")
car103 = Car("Honda", "Accord", 1995, "black")
car104 = Car("Nissan", "Civic", 2010, "grey")

if car101 == car102:
    print(car101.all_info(), " == ", car102.all_info())
else:
    print(car101.all_info(), " != ", car102.all_info())

if car101 == car103:
    print(car101.all_info(), " == ", car103.all_info())
else:
    print(car101.all_info(), " != ", car103.all_info())

car09 = Car('Ford', 'Fusion', 2014, 'red')

# car08 = Car('GM', 'Malibu')

print(car09.all_info())
# print(car08.All_info())

# car08.year = 2017
# car08.color = 'yellow'


car1 = Car()
car1.make = 'Nissan'
car1.model = "Sentra"
car1.year = 2018
car1.color = "white"

car2 = Car()
car2.make = "Honda"
car2.model = "Civic"
car2.year = 2018
car2.color = "Blue"

print(hash(car1))
print(hash(car2))

lst_cars = []

lst_cars.append(Car())
lst_cars.append(Car())
lst_cars.append(Car())

lst_cars[1].make = "Toyota"
lst_cars[1].model = "Camry"
lst_cars[1].year = 2015
lst_cars[1].color = "Black"

# Project: Dictionary: Key = [list with data types: int, str, float, tuples.] Create new dictionary with the same key, and list [int: ctr of int, str: ctr of str, float: ctr of float 03/26/2020
dic_orig_t = {"lst01": ["Trivia", 123, 321, 2.34, (4, 32)], "lst02": [345, 543, ("Connie", 3.45), 5.43],
              "lst03": [4.56, 5, 67, 6, 78, "Iseland", 7.89], "lst04": ["Sonya", (678, "Oleg"), "Natalie"]}
dic_new_t = {}

for curr_key in dic_orig_t.keys():
    dic_new_t[curr_key] = {"int": 0, "float": 0, "str": 0}
    for lst_elm in dic_orig_t[curr_key]:
        if type(lst_elm) == int:
            dic_new_t[curr_key]["int"] += 1
        elif type(lst_elm) == str:
            dic_new_t[curr_key]["str"] += 1
        elif type(lst_elm) == float:
            dic_new_t[curr_key]["float"] += 1
        elif type(lst_elm) == tuple:
            for inx in list(lst_elm):
                if type(inx) == int:
                    dic_new_t[curr_key]["int"] += 1
                elif type(inx) == str:
                    dic_new_t[curr_key]["str"] += 1
                elif type(inx) == float:
                    dic_new_t[curr_key]["float"] += 1

# Project: Dictionary: Key = [list with data types: int, str, float.] Create new dictionary with the same key, and list [int: ctr of int, str: ctr of str, float: ctr of float

dic_orig = {"str01": ["Trivia", 123, 321, 2.34, 4.32], "str02": [345, 543, "Connie", 3, 45, 5.43],
            "str03": [4.56, 5, 67, 6, 78, "Iseland", 7.89], "str04": ["Sonya", 678, "Oleg", "Natalie"]}
dic_new = {}

zxc = list(dic_orig.keys())
print(zxc[2])

for curr_ky in dic_orig.keys():
    dic_new[curr_ky] = {"int": 0, "float": 0, "str": 0}
    for y in dic_orig[curr_ky]:

        if type(y) == int:
            dic_new[curr_ky]["int"] += 1
        elif type(y) == str:
            dic_new[curr_ky]["str"] += 1
        elif type(y) == float:
            dic_new[curr_ky]["float"] += 1

print(dic_new)

lst_to_dic = ["abc", 123, 321, 234, \
              "cba", 432, 345, 543, \
              "abc", 456, 654, 567, \
              "dcb", 789, 987, 890, \
              "cde", 901, 109, 111, \
              "edc", 222, 333, 444, \
              "def", 555, 666, 777, \
              "abc", 888, 999, 122, \
              "cde", 233, 344, 455, \
              "cde", 566, 677, 788]

dic_from_lst = {}
dic_dup_ctr = {}

ttt = list(range(0, len(lst_to_dic), 4))
yyyy = lst_to_dic.index("dcb")

for i in range(0, len(lst_to_dic), 4):
    if lst_to_dic[i] not in dic_from_lst:
        dic_from_lst[lst_to_dic[i]] = [lst_to_dic[i + 1], lst_to_dic[i + 2], lst_to_dic[i + 3]]
    else:
        curr_ky = lst_to_dic[i]
        dic_from_lst[curr_ky].extend([lst_to_dic[i + 1], lst_to_dic[i + 2], lst_to_dic[i + 3]])
        if curr_ky[i] not in dic_dup_ctr:
            dic_dup_ctr[curr_ky] = 2
        else:
            dic_dup_ctr[curr_ky] += 1

print(dic_from_lst)
print(dic_dup_ctr)

lst77 = "?!,.:;-_@()"
str55 = "At 11 am local time Friday, major national  and  regional radio station major the country's national anthem, allowing residents in isolation to listen major sing together from behind closed doors."
for x in lst77:
    str55 = str55.replace(x, " ")

lst55 = str55.split()

mydict = {}

for x in lst55:
    if x not in mydict:
        mydict[x] = 1
    else:
        mydict[x] = mydict[x] + 1

for k, v in mydict.items():
    print(k, v)

xitems = mydict.items()

dctbmr = {}

dctbmr['OCC'] = 2.55
dctbmr['FLD'] = 3.75
dctbmr['DRT'] = 1.25
dctbmr['Z99'] = 1.75
dctbmr['FUK'] = 1.05
x = dctbmr['Z99']

dct001 = {'OCC': 2.55, 'FLD': 3.75}
print(dct001)

cusip_rate_dct = {"ABC123": {"OCC": 2.55, 'DRT': 1.25, "TRX": 1.55}, "DEF567": {"MBC": 5.45, "CNN": 1.75},
                  "GHN978": {"FOX": 1.54}}

dct_cusip_bmr = {}
dct_cusip_bmr['ABC123'] = {"OCC": 2.55, 'DRT': 1.25, "TRX": 1.55}

dct_bmr01 = {}
dct_bmr01["OCC"] = 2.55
dct_bmr01["Z99"] = 2.75

dct_cusip_bmr["yut987"] = dct_bmr01
print(dct_cusip_bmr["yut987"])

tpl_element1 = ("Chamber music", "Opera", "Piano")
tpl_element2 = ("Hisoty", "Wild life")

lst_element1 = ["Boston Symphony", "Tanglwood Symphony"]
lst_element2 = ["Carmen", "Figaro", "Eugin Onegin"]
lst_element3 = ["Clibern", "Richter", "Horowitz"]

lst_element4 = ["WW2", "French revolution", "Cold War"]
lst_element5 = ["Yellow Stone", "Africa safary"]
lst_element6 = ["Europe", "Asia", "Africa"]

st_element1 = {"WW2", "French revolution", "Cold War"}

dct_inerest1 = {}

# dct_inerest1[tpl_element1] = 100
# dct_inerest1[tpl_element2] = 200
# dct_inerest1[st_element1] = 300

dic_interest = {"Music": 100, "Travel": 200, "History": 300, "Dup": 100, "Zhopa": 230, "Huy": 100, "Sharp": 121,
                "Flat": 100}

listOfKeys = [zad for (zad, pered) in dic_interest.items() if pered == 100]

listoftpl = [(zad, pered) for (zad, pered) in dic_interest.items() if (pered == 100) | (pered == 300)]


def srch_dic_interest(p_dic_interest, p_value):
    lstret = []
    lst_of_items = p_dic_interest.items()
    for item in lst_of_items:
        if item[1] == p_value:
            lstret.append(item)
    return lstret


zzz = srch_dic_interest(dic_interest, 100)

vowels = "aeiouy"
dct_training = {}

lst_for_dict1 = [201, 5, 34, 43, 341, 12]
lst_for_dict2 = [21, 73, 48, 96, 103, 38, 41]
lst_for_dict3 = [3, 7, 2, 0, 95, 51, 12, 84, 47, 58]
lst_for_dict4 = ["Mayya", 123, "Yura", 456.54, "Alex", 789, "Katya", 987]

# dct_training["Sailor"] = lst_for_dict1
# dct_training["Uppercse"] = lst_for_dict2
# dct_training["Tan"] = lst_for_dict3

dct_training["Sailor"] = [23, "Peter", "Victor", 34.876, 567, "Haha", "Yuriy", 890]
dct_training["Uppercse"] = ["abc", 123, "def", 456, ("TupTvouMat", 1243, "Tired"), "ghi", 789]
dct_training["Tan"] = ["Chip", 678, "And", ["iuyiuy", 987987, "yyyyry"], 9879, "Dale", 567567]
dct_training["Mfamily"] = lst_for_dict4

x1 = 453
x2 = "hello"
x3 = 24.90

tx1 = type(x1)

if type(x1) == int:
    print("x1 is int")

if type(x2) == str:
    print("x2 is str")

if type(x3) == float:
    print("x2 is float")

tx2 = type(x2)
tx3 = type(x3)


def fnc_cntvowels(pkey):
    pctr = 0
    for alp_let in vowels:
        pctr += pkey.lower().count(alp_let)
    return pctr


dic_new = {}

for curr_ky in dct_training.keys():
    if fnc_cntvowels(curr_ky) == 3 or len(curr_ky) < 4:
        for x in dct_training[curr_ky]:
            if type(x) == int or type(x) == float:
                if curr_ky + "_num" not in dic_new:
                    dic_new[curr_ky + "_num"] = [x]
                else:
                    dic_new[curr_ky + "_num"].append(x)
            elif type(x) == str:
                if curr_ky + "_alp" not in dic_new:
                    dic_new[curr_ky + "_alp"] = [x]
                else:
                    dic_new[curr_ky + "_alp"].append(x)

print(dic_new)

dic_new = {}

for curr_ky in dct_training.keys():
    if fnc_cntvowels(curr_ky) == 3 or len(curr_ky) < 4:
        for x in dct_training[curr_ky]:
            if (x % 2) > 0:
                if curr_ky not in dic_new:
                    dic_new[curr_ky] = [x]
                else:
                    dic_new[curr_ky].append(x)

print(dic_new)

# def fnc_cnt1 (pkey):
#     pctr = 0
#     for x in vowels:
#         pctr += pkey.count(x)
#     return pctr
#
#
# def fnc_cnt2 (pkey):
#     pctr = 0
#     for x in pkey.lower():
#         pctr += vowels.count(x)
#     return pctr
#
#
# def fnc_cnt (pkey):
#     pctr = 0
#     for x in vowels:
#         for y in pkey:
#              if x == y:
#                  pctr = pctr + 1
#     return pctr
#
# fld_sum = 0
#
#
# for curr_key in dct_training.keys():
#     if fnc_cnt2(curr_key) == 3:
#         for x in dct_training[curr_key]:
#             if (x % 2) == 0:
#                 fld_sum += x
# print(fld_sum)
#
#
# for curr_key in dct_training:
#     if fnc_cnt2(curr_key) == 3:
#         for x in dct_training[curr_key]:
#             if (x % 2) == 0:
#                 fld_sum += x
# print(fld_sum)
#
#
# for curr_tpl  in dct_training.items():
# #   y = fnc_cnt2(curr_tpl[0])
# #    if y == 3:
#      if fnc_cnt2(curr_tpl[0]) == 3:
#         for x in curr_tpl[1]:
#             if  (x % 2) == 0:
#                 fld_sum += x
# print(fld_sum)


# for number in range(1, 10):
#    if(number % 2 != 0):
#        print(number)


rrr1 = fnc_cnt2("abracadabra")
rrr1 = fnc_cnt("inerestingornot")
rrr1 = fnc_cnt("bcdfghjklmnpqrstvqxz")

for item in lst_of_wovles:
    lst_of_tup.spl = lst_of_tup[0].split()
    if item in st_of_tup.spl == itm in lst_of_wovles:
        lst_of_tup.num = lst_of_tup[1].split()

# tup_rslt = tpl_res()
#    print(tup_rslt)


print(dct_inerest1)

print()

with open("C:\\Users\\Mayya\\Documents\\PythonProjData\\Article01.txt", errors="replace") as f:
    str55 = f.read()

for x in lst77:
    str55 = str55.replace(x, " ")

lst55 = str55.split()
for i in range(0, len(lst55)):
    lst55[i] = lst55[i].lower()

dct_word_freq = dict()

for item in lst55:
    if item not in dct_word_freq:
        dct_word_freq[item] = 1
    else:
        dct_word_freq[item] += 1

for word in sorted(dct_word_freq, key=lambda x: x.lower()):
    print(word, dct_word_freq[word])

print("==============================")

for word in sorted(dct_word_freq, key=lambda x: dct_word_freq[x], reverse=True):
    print(word, dct_word_freq[word])

pass

print(('aa', 'ab') < ('abc', 'a'))

print(('aa',) < ('abc',))

print(('aa', 'ab') < ('abc', 'a'))


def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


def fib3(n, plst, pflag):  # return Fibonacci series up to n
    if pflag: plst.clear()

    a, b = 0, 1
    while a < n:
        plst.append(a)
        a, b = b, a + b
    return


lst_to_func = ['dummy', 'asshole']
fib3(15, lst_to_func, False)


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


Lst_rslt = fib2(15)

fib(1000)

print('')

pass

# zzz = (1, "ytr", 34, "Hello", 401)
#
# for item in zzz
#     print(item)

lst88 = ["Pear", "Apricot", "apple", "Cherry", "Apple", "Apple"]
lst88.sort(key=lambda x: x.upper())

lst88.sort(key=lambda x: x[1:4].upper())  # order by substring

print(lst88)
print('test point 1')

for i in range(0, len(lst88)):
    lst88[i] = lst88[i].upper()
print(lst88)
print('test point 2')

lst99 = set(lst88)
print(lst99)
print('test point 3')

for i, v in enumerate(lst99):
    print(i, v)

for i in sorted(set(lst88)):
    print(i)

# for item in set99:
#    print(item)


# comb_lst01 = []
# for x in ["A", "B", "C"]:
#     for y in ["D", "E", "A"]:
#         if x != y:
#            comb_lst01.append(x + y)
# print(comb_lst01)

# comb_lst02 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(comb_lst02)

# vec_lst = [-4, -2, 0, 2, 4]
# vec_lst01 = [x * 2 for x in vec_lst]

# vec_lst01a = [x + 2 for x in vec_lst]

# vec_lst01b = tuple([x + 2 for x in vec_lst])


# vec_lst03 = [x for x in vec_lst01 if x > 0]
# vec_lst04 = [abs(x) for x in vec_lst]

# squares = []
# for x in range(10):
#    squares.append(x**2)

# sets

testing_sets = {"Apple", "Orange", "Apricot", "Plum"}
print(testing_sets)

a = set("abcda")
b = set("efghie")
c = a | b
print(c)
print(a - b)
print(b - a)
print(a & b)

# create a list of two tuples
lst_2tups = [(x, x * 2) for x in range(10)]
print(lst_2tups)

# dictionary - curly brackets, pair keys, separated by coma
tel = {"Jack": 4098, "Sape": 4139}
print(tel)
tel["Mayya"] = 205
print(tel)
tel["MIG"] = 206
print(tel)
del tel["MIG"]
print(tel)
Bln = "Mayya" in tel
Bln1 = "Yura" in tel
print(Bln)
print(Bln1)
dctr01 = dict(Yura=426, Mayya=502, Alex=1026, Katya=307)
print(dctr01)
dct92 = {x: x ** 2 for x in (2, 4, 6, 8)}

for k, v in dctr01.items():
    print(k, v)
for i in reversed(range(1, 10, 2)):
    print(i)

lst01 = ["Mayya", "Yura", "Sasha", "abra", "cadabra", "donkey", "bat", "apple", "Katya", "Phuog-Anh", "Olga", "mini-Me",
         "donkey", "abra", "apple", "apple"]
for i, v in enumerate(lst01):
    print(i, v)

lst01.sort(key=lambda x: x.upper(), reverse=True)

# reversed
var_iter = iter(lst01)

while True:
    try:
        print(next(var_iter))
    except StopIteration:
        break


def func_rev(plst01):
    # return list(reversed(plst01))
    return sorted(set(plst01))


# def func_itr_rev(plst01):
#     return reversed(plst01)
#
#
# itr_lst01 = func_itr_rev(lst01)

# print(itr_lst01.__next__())


rev_out = func_rev(lst01)
print(rev_out)

questions = ["Name", "Interest", "Colour"]
answers = ["Mayya", "Music", "Purple"]
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# lst02 = ["Mother", "Father", "Son", "crap01", "crap02", "primat", "bird", "fruit", "Daughter"]
# lst02.insert(len(lst02) - 1, "WallE")
# lst02.insert(len(lst02) - 3, "WallE")
#
# print(lst01)
#
# del lst01[4]
# print(lst01)

# lst02.remove("WallE")
# print(lst02)


# while True:
#     try:
#         lst02.remove("WallE")
#     except ValueError:
#         break

# print(lst02)


def rem_dup(plist: list, pvalue: str):
    while True:
        try:
            plist.remove(pvalue)
        except ValueError:
            return


# rem_dup(lst02, "WallE")


def dist_func(plist: list):
    templst = []
    for x in plist:
        if templst.count(x) == 0:
            templst.append(x)

    plist.clear()
    plist.extend(templst)
    return


def dist_func1(plist: list) -> list:
    templst = []
    for x in plist:
        if templst.count(x) == 0:
            templst.append(x)
    return templst


def dist_func2(plist: list) -> list:
    templst = []
    for x in plist:
        try:
            templst.index(x)
        except ValueError:
            templst.append(x)
    return templst


#  dist_func(lst01)

lstrtnn = dist_func1(lst01)

# print(lstret)
print(lst01)

tplexample = ("Rose", "Tulip", 123, 987, "Go f__* ")

tpl99 = 12, 45, "ooo"

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
print("After deleting tup : ")
print(tup)

var1 = lst02.index("Daughter")
var2 = len(lst02)
var3 = len(lst02) - 1
var4 = lst02.count("WallE")
lst03 = []
lst03 = lst02.copy()
lst03.reverse()
stack01 = []
stack01.append(6)
stack01.append(3)
stack01.append(2)
p1 = stack01.pop()
p2 = stack01.pop()

myset01 = [5, 91, 78, 546]
tpl01 = (10, 40, 60, 80, 100)


def action_test(p):
    return p / 2


thirdy = map(action_test, myset01)
retval01 = map(action_test, tpl01)

# print(list(thirdy))
print(tuple(retval01))

lst01.extend(lst02)
print(lst01)

p1 = lst01.pop()
p2 = lst01.pop()

del lst01[4:6]
print(lst01)

print(lst01)

lst01.clear()
print(lst01)

a = 56
b = 28
c = a * b
print('Hello World!')
print('Product=' + str(a * b))

print(301, "Vasya", 23.456, "Hoho")

lst = ["mayya", 235, "yura", "katya"]

print(lst)

print(range(2, 17))

print(range(38, 53))

print(range(15))

for ix in range(1, 3):
    print(lst[ix])

test_list = [1, 3, 4, 3, 7, 6, 7]

# printing initial list
print("Original list : " + str(test_list))

# using naive method
# to find indices for 3
res_list = []
for i in range(0, len(test_list)):
    if test_list[i] == 3:
        res_list.append(i)

    # printing resultant list
print("New indices list : " + str(res_list))

print(math.sin(3.1415926 / 4))
print(1 / math.sqrt(2))

lst2 = ["anna"]

sss = "To be or not to be?"
words = sss.split()
print(words)
