import math
import asyncio

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

cusip_rate_dct = {"ABC123": {"OCC":2.55, 'DRT' : 1.25, "TRX": 1.55 }, "DEF567": {"MBC": 5.45, "CNN":1.75}, "GHN978": {"FOX": 1.54}}

dct_cusip_bmr = {}
dct_cusip_bmr['ABC123'] = {"OCC":2.55, 'DRT' : 1.25, "TRX": 1.55}

dct_bmr01 = {}
dct_bmr01["OCC"] = 2.55
dct_bmr01["Z99"] = 2.75

dct_cusip_bmr["yut987"] = dct_bmr01
print(dct_cusip_bmr["yut987"])



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


for word in sorted(dct_word_freq, key = lambda x: x.lower()):
    print(word, dct_word_freq[word])

print("==============================")

for word in sorted(dct_word_freq, key = lambda x: dct_word_freq[x], reverse=True):
    print(word, dct_word_freq[word])


pass




print(('aa', 'ab') < ('abc', 'a'))

print(('aa', ) < ('abc', ))

print(('aa', 'ab') < ('abc', 'a'))


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b


def fib3(n, plst, pflag):   # return Fibonacci series up to n
    if pflag: plst.clear()

    a, b = 0, 1
    while a < n:
        plst.append(a)
        a, b = b, a+b
    return

lst_to_func = ['dummy', 'asshole']
fib3(15, lst_to_func, False)





def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
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

lst88.sort(key=lambda x: x[1:4].upper())   # order by substring


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

testing_sets = {"Apple",  "Orange",  "Apricot",  "Plum"}
print(testing_sets)


a = set("abcda")
b = set("efghie")
c = a | b
print(c)
print(a - b)
print(b - a)
print(a & b)


# create a list of two tuples
lst_2tups = [(x,  x * 2) for x in range(10)]
print(lst_2tups)


# dictionary - curly brackets, pair keys, separated by coma
tel = {"Jack": 4098,  "Sape": 4139}
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
dct92 = {x: x**2 for x in (2, 4, 6, 8)}

for k, v in dctr01.items():
    print(k, v)
for i in reversed(range(1, 10, 2)):
    print(i)


lst01 = ["Mayya", "Yura", "Sasha", "abra", "cadabra", "donkey", "bat", "apple", "Katya", "Phuog-Anh", "Olga", "mini-Me", "donkey", "abra", "apple", "apple"]
for i, v in enumerate(lst01):
    print(i, v)


lst01.sort(key=lambda x: x.upper(),  reverse=True)


# reversed
var_iter = iter(lst01)

while True:
    try:
        print (next(var_iter))
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


questions = ["Name",  "Interest",  "Colour"]
answers = ["Mayya",  "Music",  "Purple"]
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
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

tup = ('physics', 'chemistry', 1997, 2000)
print (tup)
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
