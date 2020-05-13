import math
import re
import MyFunctions
import calendar
#import python_dateutil
from dateutil.relativedelta import *
from datetime import date, time, timedelta, datetime

import smtplib, ssl


import asyncio

import pyodbc

#learning lambda

lst_of_str = ['Apple','Orange','Cherry','Melon', 'Potato']
lst_by_lgth = list(filter(lambda x: (len(x) == 6), lst_of_str))
print(lst_by_lgth)

lst_st_with = list(filter(lambda x: (x.startswith('A')), lst_of_str))
print(lst_st_with)

lst_end_with = list(filter(lambda x: (x.endswith('e')), lst_of_str))
print(lst_end_with)

lst_with_pattern = list(filter(lambda x: ('pp' in x or 'rr' in x), lst_of_str))
print(lst_with_pattern)

lst_with_pattern1 = list(filter(lambda x: (x.find('rr') >= 0 or x.find('pp') >= 0 ), lst_of_str))
print(lst_with_pattern1)


compute_remainder = lambda x, y: x % y
r = compute_remainder(7, 2)

print(r)

# learning filtering -->  for d in data ... if d > 50  .... return  --> list comprehention

data = [66, 15, 91, 30, 35, 38, 43, 20, 38, 28, 98, 50, 7, 80, 99]
filtered = [d for d in data if d > 50]
print(filtered)

# same using lambda:

filtered = list(filter(lambda x: (x > 50), data))
print(filtered)

# Map example without lambda

mapped = [(x / 2) for x in data]
print(mapped)

#Map  with lambda

mapped = list(map(lambda x: (x / 2), data))
print(mapped)



# print('Hello World')
# print('*'*10)

tpl_sal_upd = [
    ('Gruzglina', 150000),
    ('King', 125000),
    ('Fuller', 135000),
    ('Peacock', 145000)
]

lst_emp_ins = [('Gnom', 'Grumpy', 'Chef', 'Mr.', '1959-05-02', '1996-10-26', '2 North Pole', 'Dreamland', 'Laplandia', '08960', 'USA', '(973) 714-6530', \
               None, None, None, 5, None, 150000)]


sql_emp_ins = \
  """
    insert into Employees (     
	[LastName],
	[FirstName],
	[Title],
	[TitleOfCourtesy],
	[BirthDate],
	[HireDate],
	[Address],
	[City],
	[Region],
	[PostalCode],
	[Country],
	[HomePhone],
	[Extension],
	[Photo],
	[Notes],
	[ReportsTo],
	[PhotoPath],
	[Salary]
	) Values 
	( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
	"""
print(sql_emp_ins)

sql_rollup = \
"""
WITH OrdRpt AS
  (SELECT  
    O.OrderId, D.ProductID, O.CustomerId, O.EmployeeId, D.UnitPrice, D.Quantity
    FROM  Orders O
    INNER JOIN [Order Details] D on O.OrderId = D.OrderId
    WHERE   DATEPART(YY, O.OrderDate) = 1998 and DATEPART(MM, O.OrderDate) = 05
  )
 SELECT CustomerID, EmployeeId, OrderId, ProductId, SUM(UnitPrice * Quantity) as Total
  FROM  OrdRpt
 GROUP BY ROLLUP(CustomerID, EmployeeId, OrderId, ProductId)
"""


conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DELL-LAPTOP-MG\\MSSQL_VENUS;'
    'Database=Northwind;'
    'User=sa;'
    'Passwd=Vanhe1sing!'

)


cur = conn.cursor()
new_ins = conn.execute("{CALL spEmpInsert (?,?,?)}", ('Galushka', 'Igor', 115000))
print(new_ins)
conn.commit()


#add_upd = cur.execute("{CALL spAddressUpd (?,?,?,?,?,?)}", (11, '2 Beech Lane', 'Parsippany', 'NJ', '07960', 'UK' ))
#print(add_upd)
#conn.commit()


#sp_res001 = cur.execute("exec [spOrderRpt](?)", (date(1998, 5, 25),))
#sp_res001 = cur.execute("exec spOrderRpt @OrderDate = ?", ( date(1998, 5, 25), ) )

sp_res001 = cur.execute("{CALL spOrderRpt (?)}", ( '1998-05-25', ))

#sp_res001 = cur.execute("{CALL spOrderRpt2 (?, ?)}", (1998, 5) )

for row in sp_res001:
    print(row)


cntr = cur.execute(sql_rollup)

for row in cntr:
    count = len([elem for elem in list(row) if elem == None])
    if count == 0:
        d = "{0:8s}  {1:5d}  {2:8d}  {3:8d}  {4:12.2f}".format(row[0], row[1], row[2], row[3], row[4])
        print(d)
    elif count == 4:
        print("Grand Total:                        ", row[4])
    elif count == 3:
        print("Total by Customer:                  ", row[4])
        print()
    elif count == 2:
        print("Total by Customer/Employee:         ", row[4])
    elif count == 1:
        print("Total by Customer/Employee/Order:   ", row[4])





#cntr = cur.execute("delete Employees where EmployeeId = 8")
cntr = cur.execute(sql_emp_ins, lst_emp_ins[0])

conn.commit()
print ('Total # of rows: ', cntr)


for curr_item in tpl_sal_upd:
    cntr = cur.execute("update Employees set Salary = ? where LastName = ?", (curr_item[1], curr_item[0])).rowcount
conn.commit()


cntr = cur.execute("SELECT * FROM [Employees] where city =  'London' ").rowcount


for row in cur:
    print(row.Title, row.City, row.Country)

cntr = cur.execute("update Employees set Salary = 110000 where LastName in('Gruzglina', 'King') ").rowcount
conn.commit()
print ('Total # of rows: ', cntr)
conn.close()





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


#   Learning how to deal with email  2020-04-03

# to_email   = 'mayya.gruzglina@outlook.com'
# gmail_user = 'igor.sklyarskiy33@gmail.com'
# gmail_pwd  = 'Arizona33!'
#
# smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
# smtpserver.ehlo()
# smtpserver.starttls()
# smtpserver.ehlo()    # extra characters to permit edit
# smtpserver.login(gmail_user, gmail_pwd)
#
# header = 'To:' + to_email+ '\n' + 'From: ' + gmail_user + '\n' + 'Subject: Sending our 5th email testing how to send emails in Python\n'
# print(header)
#
# msg = header + '\n Mayya,\n\nThis is email #0004,\nit was sent by your husband Yuriy\nfrom your father\'s second email account'
# smtpserver.sendmail(gmail_user, to_email, msg)
# smtpserver.quit()
#
# print('done!')
#
#
#
#
#
# #port = 465  # For SSL
# port = 587  # for TTL
#
# smtp_server   = "smtp.gmail.com"       # sender's server
#
# sender_email  = "i.s33@gmail.com"
# password = input("Type your password and press enter: ")
# receiver_email = "@kkk.com"       # receiver email address
#
# # Create a secure SSL context
# context = ssl.create_default_context()
#
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.connect()
#     server.login("i.s33@gmail.com", password)
# #    server.ehlo()  # Can be omitted
# #    server.starttls(context=context)
# #    server.ehlo()  # Can be omitted
# server.login("i.s33@gmail.com", password)
#
# message = """\
# Subject: Hi there
#
# This message is sent from Python by your husband
#
# Yuriy.
# """
# server.sendmail(sender_email, receiver_email, message)

# Learning calendar (import calendar)

#(NOL, ODIN, DVA, TRI, CHETYRE) = range(7)

#Write a Python program to find a missing number from a list.
#Input : [1,2,3,4,6,7,8]
#Output : 5

#lst_input = [1, 2, 3, 4, 6, 7, 8]
lst_input = [1, 2, 3, 4, 6, 7, 10]
dic_interval = {}
step = 1

for x in range(0, len(lst_input) - 1):
    if (lst_input[x + 1]) - (lst_input[x]) < step:
        step = lst_input[x + 1] - lst_input[x]

for x in range(0, len(lst_input) - 1):
    if (lst_input[x + 1]) - (lst_input[x]) > 1:
        dic_interval[x] = (lst_input[x + 1])

for k, v in dic_interval.items():
    curr_val = lst_input[k] + 1
    curr_ind = k + 1
    while curr_val < v:
        print('inserting at index', curr_ind, ' value ', curr_val)
        lst_input.insert(curr_ind, curr_val)
        curr_ind += 1
        curr_val += 1





# delta = step
# for d in range(lst_input[k] + step, lst_input[k + 1]):
#     lst_input.insert(k + delta, d)
#     delta += step
#
# zzzz = 0
# #lst_input[]


import os.path
import struct

#Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
print(struct.calcsize("P") * 8)   # shall import struct



# check if file exists. should import os.path

#file_content = open('TestFile02.txt', 'w')
#print(os.path.isfile('TestFile02.txt'))  # returns true of false. should import os.path
var001 = os.path.abspath("TestFile02.txt")  # return exact path.should import os.path



# Write a Python program to check whether a file exists

# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

class Pif_agor():
    def __init__(self, px1, py1, px2, py2):
        self.x1 = px1
        self.y1 = py1
        self.x2 = px2
        self.y2 = py2
        self.catet1 = (self.x2 - self.x1) ** 2
        self.catet2 = (self.y2 - self.y1) ** 2
        self.hipotenuza = (self.catet1 + self.catet2)

    def calc_rtn(self):
        return math.sqrt(self.hipotenuza)

pif_inst = Pif_agor(4, 5, 9, 12)
distance = pif_inst.calc_rtn()
print(distance)



# Write a Python program to display your details like name, age, address in three different lines

lst_personal_info = []
str_personal_info = 'Mayya Gruzglina, 60 yrs old, 2 Beech lane Morristown NJ 07960'
lst_personal_info = str_personal_info.split(',')
for x in range(0, len(lst_personal_info)):
    print(lst_personal_info[x])


# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5 - add function to below class

class Calc_sum():
    def __init__(self, pnum01, pnum02):
        self.sum = pnum01 + pnum02
        self.num01 = pnum01
        self.num02 = pnum02

    def calc_two_num_sum(self):
        return 20 if 15 <= self.sum <= 20 else self.sum

    def true_or_false(self):
        return True if (self.num01 == self.num02) or (self.num01 - self.num02 == 5) or (self.num01 + self.num02 == 5) else False


parm_numbers = Calc_sum(10, 6)
sum_back = parm_numbers.calc_two_num_sum()
print(sum_back)
second_chk = parm_numbers.true_or_false()
print(second_chk)


#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

class Ret_a_sum():
    def __init__(self, pnum1, pnum2, pnum3):
        self.set01 = {pnum1, pnum2, pnum3}
        self.sum = pnum1 + pnum2 + pnum3

    def  calc_rtn(self):
        return 0 if len(self.set01) != 3  else self.sum


parms_to_class = Ret_a_sum(5, 3, 4)
sum_back = parms_to_class.calc_rtn()
print(sum_back)

# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_list3 = color_list_1 | color_list_2
print(color_list3)
print(color_list_1 - color_list_2)
print(color_list_2 - color_list_1)
print(color_list_1 & color_list_2)


#Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence


numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]

for x in numbers:
    if (x / 2).is_integer :
        print(x)
    elif x == 237:
        break

#Write a Python program to concatenate all elements in a list into a string and return it.

class Ret_a_string():

    def __init__(self, plist):
        self.list002 = plist
        self.string = ''

    def concat_rtn(self):
        for x in self.list002:
            self.string += x
        return self.string


parm_to_cls = Ret_a_string(['a', '3', '6', '4', 'f'])
str_back = parm_to_cls.concat_rtn()
print(str_back)


# Write a Python program to check whether a specified value is contained in a group of values.

class Value_chk():
    def __init__(self,pchk_value,plist):
        self.chk_value = pchk_value
        self.list_of_values = plist

    def check_value(self):
        for x in range(0, len(self.list_of_values)):
            return True if self.list_of_values[x] == self.chk_value else False


parms_to_cls = Value_chk(-1, [9, 1, 5, 3, 7, 2])
true_or_false = parms_to_cls.check_value()
print(true_or_false)



#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of
#whole string if the length is less than 2.


class Rtn_copy():
    def __init__(self,pnum, pstring):
        self.num = pnum
        self.string = pstring

    def ret_string_copy(self):
        return (self.string[0:2] * self.num) if len(self.string) > 2 else self.string[0] * self.num


parm_to_cls = Rtn_copy(3, 'a')
copy_back = parm_to_cls.ret_string_copy()
print(copy_back)


#Write a Python program to test whether a passed letter is a vowel or not.


class Check_letter():
    def __init__(self, pletter, plist):
        self.list01 = plist
        self.letter = pletter

    def chk_if_vow(self):
        for idx in range(0, len(self.list01)):
            if self.list01[idx] == self.letter:
                return 'The letter is a vowel'
            else:
                 return 'The letter is a consonance'


str_let = Check_letter('K', ['A', 'E', 'I', 'O', 'U', 'Y'])
str_back = str_let.chk_if_vow()
print(str_back)


#Write a Python program to count the number 4 in a given list.

lst002 = [2, 5, 4, 7, 5, 4, 4, 6, 1]

lst_cnt = lst002.count(4)
print(lst_cnt)


#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

class  Odd_even():
    def __init__(self,pnum):
        self.num = pnum

    def  calc_num(self):
        return "The number is even" if (self.num / 2).is_integer() else 'The number is odd'

pass_num = Odd_even(8)
odd_or_even = pass_num.calc_num()
print(odd_or_even)


#Write a Python program to get a new string from a given string where "Is" has been added to the front.
#if the given string already begins with "Is" then return the string unchanged.

str001 = 'Is the weather is rainy today?'
# print(str001.upper().startswith('IS'))
if (str001.upper().startswith('IS')):
    print(str001)
else:
    print('Is' + str001 + ' false')


#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

class Calc_sum():
    def __init__(self, pnum1, pnum2, pnum3):
        self.num1 = pnum1
        self.num2 = pnum2
        self.num3 = pnum3

    def calc_rtn(self):
        return (self.num1 + self.num2 + self.num3) * 3 if self.num1 == self.num2 and self.num1 == self.num3 else (self.num1 + self.num2 + self.num3)

sum_init = Calc_sum(3, 3, 3)
sum_rsl  = sum_init.calc_rtn()
print(sum_rsl)


#Write a Python program to test whether a number is within 100 of 1000 or 2000.

class Check_range():
    def __init__(self, pnum):
        self.num = pnum

    def num_within(self):
        if self.num  < 100 and self.num > 0:
            return 'Number within 100'
        elif self.num  <= 1000 and self.num >= 100:
            return 'Number within 1000'
        elif self.num <= 2000 and self.num > 1000:
            return 'Number within 2000'

test_num = Check_range(99)
str_back= test_num.num_within()
print(str_back)

test_num = Check_range(125)
str_back= test_num.num_within()
print(str_back)

test_num = Check_range(1432)
str_back= test_num.num_within()
print(str_back)






#Write a Python program to get the difference between a given number and 17,
#if the number is greater than 17 return double the absolute

class Calc_diff():
    given_num = 17

    def __init__(self, pnum):
        self.num = pnum

    def calc_num(self):
        # if (self.num > Calc_diff.given_num):
        #     return abs(Calc_diff.given_num - self.num) * 2
        # else:
        #     return Calc_diff.given_num  - self.num
        return abs(Calc_diff.given_num - self.num) * 2 if self.num > Calc_diff.given_num else Calc_diff.given_num - self.num



create_ins = Calc_diff(19)
num_back = create_ins.calc_num()
print(num_back)



#Write a Python program to calculate number of days between two dates.

#from datetime import date, time, timedelta, datetime

curr_dt01= date(2014, 7, 2)
curr_dt02 = date(2014, 7, 11)
print(curr_dt02)

dt_rel = relativedelta(curr_dt02, curr_dt01)  # difference between two days
print(dt_rel.days)
curr_dt01= date(2014, 7, 2)

curr_dt03 = curr_dt02 - curr_dt01
print(curr_dt03.days)

#print(dt_rel)




yy = 2017
mm = 11

# display the calendar
#print(calendar.month(yy, mm))
#print(calendar.calendar(2018, 2, 1, 6))
# print(calendar.February()
print(calendar.weekday(2020,4,21))
print(calendar.weekheader(10))



# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# N + NN + NNN ( 5 + 55 + 555) = 615

num1 = 5
num2 = eval( str(num1 + num1))
num3 = eval("'" + str(num1 + num1) + "'")


class Calc_sum():
    def __init__(self, pnum):
        self.num = pnum
        return

    def ret_sum(self):
        s = str(self.num)
#       stoeval = s + '+' + s + s + '+' + s + s + s
        stoeval = s + '+' + s*2 + '+' + s*3
        print(stoeval)
        return  eval(stoeval)

ev101 = Calc_sum(7)
res101 = ev101.ret_sum()

print(res101)


# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)

exam_st_date = (11, 12, 2014)
from datetime import date, time, timedelta, datetime

for x in range(0, len(exam_st_date)):
    print(exam_st_date[x])

x = datetime(exam_st_date[-1], exam_st_date[0], exam_st_date[1])
print(x.strftime("%Y/%m/%d"))
print(x)



# Write a Python program to display the first and last colors from the following list.
# ["Red","Green","White" ,"Black"]

color_list = ['Red', 'Green', 'White', 'Black']

print('First color and last color from the list: %s, %s' % (color_list[0], color_list[-1]) )


# Write a Python program to accept a filename from the user and print the extension of that.

class File_name():
    def __init__(self, pfile_n):
        self.file_n = pfile_n

    def file_ext(self):
#      lst_file_name = self.file_n.split('.')
#      ext = lst_file_name.pop()
#      return ext

       lsttmp = self.file_n.split('.')
       return lsttmp.pop() if len(lsttmp) > 1 else '<No extension>'



ext_name = File_name('abc.java')
ext_n = ext_name.file_ext()
print(ext_n)

ext_name101 = File_name('.ahahahahaha')
ext_n101 = ext_name101.file_ext()
print(ext_n101)

ext_name102 = File_name('hahaha')
ext_n102 = ext_name102.file_ext()
print(ext_n102)




# Write a Pyreturn [int(s) for s in self.strval.split(',')]thon program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

class List_and_tuple():
    def __init__(self, pstring):
        self.strval = pstring

    def  ret_list(self):
        return [int(s) for s in self.strval.split(',')]

    def ret_tuple(self):
        return tuple(  [int(s) for s in self.strval.split(',')]   )

    def xret_list(self):
        return eval('[' + self.strval + ']')

    def xret_tuple(self):
        return eval('(' + self.strval + ',)')


ins_out = List_and_tuple('3, 56, 139')
ins_out2 = List_and_tuple('549')

tpl201x = ins_out2.xret_tuple()
print(tpl201x)



lst101 = ins_out.ret_list()
print(lst101)

lst101x = ins_out.xret_list()
print(lst101)

tpl102 = ins_out.ret_tuple()
print(tpl102)

tpl102x = ins_out.xret_tuple()
print(tpl102x)




#Write a Python program which accepts the user's first and last name and print them n reverse order with a space between them.

class Person():
    def __init__(self, pfirst_name, plast_name):
        self.lst_person = [plast_name, pfirst_name]

    def __str__(self):
        return ' '.join(self.lst_person)

    def  rev_name(self):
        return ' '.join( list(reversed(self.lst_person)) )

prs01 = Person('Mayya', 'Gruzglina')
print(prs01)

print(prs01.rev_name())



class full_name():
    def __init__(self, pfirst_name, plast_name):
        self.first_name = pfirst_name
        self.last_name = plast_name

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    def  rev_name(self):
        return self.first_name + ' ' + self.last_name

    def to_dict(self):
        d = {}
        d["attr1"] = self.last_name
        d["attr2"] = self.first_name
        return d


full_name = full_name('Mayya', 'Gruzglina')
print(full_name)

rev101 = full_name.rev_name()
print(rev101)

print(rev102 := full_name.rev_name())




rev_name = full_name(d)







# display curr day excersise

from datetime import date, time, timedelta, datetime
d_today = date.today()
print(d_today, "testing curr date format")
d_time = datetime.today()
print(d_time, "curr time")
# ctime format   ##############
d_time1 = datetime.today().ctime()
print(d_time1)
print("tested ctime")
# strftime format ##############
x = datetime(2018, 9, 15)
print(x)
print(x.strftime("%b %d %Y %H:%M:%S"))
print("tested strftime")
print(x.strftime("%A %B %d %Y %H:%M:%S"))  # A - full day WEDNESDAY a - three letters, same with B - Month, or b
print("tested strftime with weekday")
print(x.strftime('%b/%d/%Y'))
print(d_today.year)
print(d_today.month)
print(d_today.day)
print(d_today.weekday())


# Twinkle excersise
file_sample = open("TestFile02.txt", "r", encoding='utf8', errors='ignore')
file_text = file_sample.read()
lst_file = []
out_str = None
for elm in file_text:
    if re.match(r'[A-HJ-Z]', elm):
        if out_str != None:
            lst_file.append(out_str)
        out_str = elm
    else:
        out_str += elm

if out_str != None:
    lst_file.append(out_str)

file_sample.close()


rx01 = re.split(r'\b[ABCDEFGHJKLMNOPQRSTUVWXYZ]', '   qkk2464 ')
rx01 = re.split(r'\b[ABCDEFGHJKLMNOPQRSTUVWXYZ]', ' Hello my little Boy. You got to go Home qkk2464 ')

rx01 = re.match(r'\b[ABCDEFGHJKLMNOPQRSTUVWXYZ]', ' Hello my little Boy. You got to go Home qkk2464 ')





rx01 = re.match(r'^\s*[akq]\d+\s*$', ' 2464 ')
rx01 = re.match(r'^\s*[akq]\d+\s*$', '   a2464 ')
rx01 = re.match(r'^\s*[akq]\d+\s*$', '   k2464 ')
rx01 = re.match(r'^\s*[akq]\d+\s*$', '   q2464 ')
rx01 = re.match(r'^\s*[akq]{3,5}\d+\s*$', '   qkk2464 ')



rx01 = re.match(r'^\s*\d+\s*$', ' 2464 ')
rx01 = re.match(r'^\s*\d+\s*$', 'g   2464 ')
rx01 = re.match(r'^\s*\d+\s*$', ' 24j64 ')

rx01 = re.match(r'^\s*\d+\s*$', '2464   ')
rx01 = re.match(r'^\s*\d+\s+$', '  2464')
rx01 = re.match(r'^\s*\d+\s*$', ' 2464g  ')




rx01 = re.match(r'.*\s+$', '')
rx01 = re.match(r'.*\s+$', '           ')


rx01 = re.match(r'.*\s+$', '  ')
rx01 = re.match(r'.*\s+$', '')
rx01 = re.match(r'.*\s+$', '           ')
rx01 = re.match(r'.*\s+$', ' v  ')
rx01 = re.match(r'.*\s+$', 'X    v  ')
rx01 = re.match(r'.*\s+$', 'd  ')
rx01 = re.match(r'.*\s+$', '  c')


print("Peter\nDonald")
print(r"Peter\nDonald")


def this_class_name(pinstance):
    return pinstance.__class__.__name__


#Write a Python class named Circle constructed by a radius and two methods
#which will compute the area and the perimeter of a circle.

class  circle_calc():
    def __init__(self, pradius):
        self.radius = pradius

    def calc_circle_area(self):
        return self.radius ** math.pi

    def calc_circle_perimeter(self):
        return self.radius * 2 * math.pi


circle_result_back = circle_calc(15)
print(this_class_name(circle_result_back))
print(circle_result_back.calc_circle_area())
print(circle_result_back.calc_circle_perimeter())


#Write a Python class named Rectangle constructed by a length and width
#and a method which will compute the area of a rectangle.

class  area_of_rectangle():
    def __init__(self, pwidth, plenght):
        self.width = pwidth
        self.lenght = plenght

    def calc_area(self):
        return self.width * self.lenght


result_back = area_of_rectangle(5, 6)
print(this_class_name(result_back))
print(result_back.calc_area())


#class that take string from the user, and print string

class Print_str():
    def __init__(self):
        self.string = None

    def get_String(self, pstring):
        self.string = pstring

    def print_String(self):
        print(self.string.upper())


my_str101 = Print_str()
my_str101.get_String("low case dummy teacher")
my_str101.print_String()


my_str = Print_str('all low case')
print(my_str)



#solving problems in python:
#Write a Python class to reverse a string word by word.

str001 = 'hello .py to be or not to be, this is the question'
lst001 = str001.split()
lst002 = reversed(lst001)

str_rev1 = ' '.join(lst002)

str_reversed = ' '.join(reversed( str001.split() ))



# for i in reversed(range(0, len(lst001)):
#     print(lst001)

#solving problems in python:
#Write a Python class to find the three elements that sum to zero from a set of n real numbers

lst_of_num = [-25, -10, -7, -3, 2, 4, 8, 10]
lst_of_three = []

for i1 in range(0, len(lst_of_num)):
    for i2 in range((i1 +1), len(lst_of_num)):
        for i3 in range((i2 +1), len(lst_of_num)):
            if lst_of_num[i1] + lst_of_num[i2] + lst_of_num[i3] == 0:
                lst_of_three.append((i1, i2, i3))


#solving problems in python: Write a Python class to find a pair of elements (indices of the two numbers)
#from a given array whose sum equals a specific target number.

lst_in_num = [10, 20, 10, 40, 50, 60, 70]
target_num = 50


def two_num_indice(plst_in_num, ptarget_num):

    lst_of_tup = []

    for i in range(0, len(plst_in_num)):
        for j in range((i + 1), len(plst_in_num)):
            if plst_in_num[i] + plst_in_num[j] == ptarget_num:
                lst_of_tup.append((i, j))
    return lst_of_tup


print(two_num_indice(lst_in_num, target_num))


#salving problems in python
# Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

def chk_syntax(pstr):
    lst_stack = []
    for inx in pstr:
        if inx in ("[", "(", "{"):
            lst_stack.append(inx)
        elif inx in ("]", ")", "}"):
            if not lst_stack:
                return 1   # closing bracket and no opening
            else:
                chk_num = lst_stack.pop()
                if not ( (inx == ")" and chk_num == "(") or (inx == "]" and chk_num == "[") or (inx == "}" and chk_num == "{" ) ):
                    return 2  #  mismatching

    if lst_stack:
        return 3   # EOL and non matched opening brackets

    return 0


line_to_verify = "[[[[[((((ABCD###(EFG&&&)))))???]"
print(chk_syntax(line_to_verify))



    # learning classes April 8th - 9th 2020

class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __new__(cls, name, salary):
        if 0 < salary < 10000:
            return object.__new__(cls)
        else:
            return None

    def __str__(self):
         return '{0}  ( {1} )'.format(self.__class__.__name__, self.__dict__)


emp_tom = Employee('Tom', 8000)
print(emp_tom)

#  Employee({'name': 'Tom', 'salary': 8000})

emp_richard = Employee('Richard', 20000)
print(emp_richard)




class Cloth():
    def __init__(self, pgender, pseason, pdesigner):
        self.gender = pgender
        self.season = pseason
        self.designer = pdesigner

    def __str__(self):
        return "Gender: " + self.gender + " season: " + self.season + " designer: " + self.designer


class Talbot():
    def __init__(self, pdesigner, plocation):
        self.location = plocation



    def __str__(self):
        return "Gender: " + self.gender + " season: " + self.season + " designer: " + self.designer




item010 = Cloth('women', 'summer', 'vince')
print(item010)
item020 = Talbot('men', 'fall', 'vince', 'harding twn')
print(item020)










class Computer():
    def __init__(self, make, ram, storage):
        self.make = make
        self.ram = ram
        self.storage = storage


# Class Mobile inherits Computer
class Mobile(Computer):
    def __init__(self, make, ram, storage, model):
        super().__init__(make, ram, storage)
        self.model = model


mob_dev01 = Mobile('Apple', 2, 64, 'iPhone X')
print('The mobile is:', mob_dev01.make)
print('The RAM is:', mob_dev01.ram)
print('The storage is:', mob_dev01.storage)
print('The model is:', mob_dev01.model)



# Learning how to manipulate date/time

from datetime import date, time, timedelta, datetime

tdl101 = timedelta(weeks=2, minutes= 50)
print(tdl101.days)
tdl102 = timedelta(weeks = 5, minutes = 90)
tdl103 = tdl101 + tdl102
#tdl104 = tdl101 + 3


dtm101 = datetime(2020, 4, 6, 20, 30, 1)
dtm102 = dtm101 + timedelta(days=2, minutes=3, seconds=15)
print(dtm102, "result")

dt001 = date(2002, 12, 31)
print(dt001)

dt002 = dt001.replace(day=26)
print(dt002)

d_today = date.today()
print(d_today, "testing curr date format")
d_time = datetime.today()
print(d_time, "curr time")
# ctime format   ##############
d_time1 = datetime.today().ctime()
print(d_time1)
print("tested ctime")
# strftime format ##############
x = datetime(2018, 9, 15)
print(x)
print(x.strftime("%b %d %Y %H:%M:%S"))
print("tested strftime")
print(x.strftime("%A %B %d %Y %H:%M:%S"))  # A - full day WEDNESDAY a - three letters, same with Month name B, or b
print("tested strftime with weekday")
print(x.strftime('%b/%d/%Y'))
print(d_today.year)
print(d_today.month)
print(d_today.day)
print(d_today.weekday())
week_days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
print(week_days[d_today.weekday()])
d_tomorrow = d_today + timedelta(days = 1)
print(d_tomorrow)
d_yesterday = d_today + timedelta(days = - 1)
print(d_yesterday)

tm001 = time(3, 34, 56, 892)
print(tm001)

dt_today = datetime.today()
print(dt_today)
print(dt_today.timetz())

dt_now = datetime.now()
print(dt_now)
print(dt_now.timetz())

print("Year  in dt_now ",  dt_now.year)
print("Month in dt_now ", dt_now.month)
print("Day   in dt_now ", dt_now.day)

print("Hour   in dt_now ", dt_now.hour)
print("Minute in dt_now ", dt_now.minute)
print("Second in dt_now ",  dt_now.second)

print("Weekday in dt_now ",  dt_now.weekday())

curr_dt01 = datetime(2020, 4, 20, 10, 30, 8)
curr_dt02 = datetime(1981, 10, 26, 16, 20, 0)
Alex_age = curr_dt01 - curr_dt02

print(Alex_age)

print("Days ", Alex_age.days, "   Secs ",  Alex_age.seconds, "  Mcs ", Alex_age.microseconds, "  Resolution ",
       Alex_age.resolution, "  min ", Alex_age.min, "  max ", Alex_age.max)

dt_rel = relativedelta(curr_dt01, curr_dt02) # difference between two days


print(dt_rel, "relative data")

print(dt_rel.years)
print(dt_rel.months)
print(dt_rel.days)
print(dt_rel.hours)
print(dt_rel.minutes)
print(dt_rel.seconds)
print(dt_rel.microseconds)


weekno = datetime.today().weekday()

if weekno < 5 :
    print("Weekday")
else:
    print("Weekend")










# Learning Files Input abd Output April 2

def fnc_skiplines(f, n):
    for i in range(n):
        next(f)
    return

flo_sample = open("TestFile01.txt", "a+", encoding='utf8', errors='ignore')
flo_sample.seek(0, 0)
for idx in range(15):
    text = flo_sample.readline()
    print("What did I read? %6d %s" % (idx+1, text), end=' ')

flo_sample.write(" ******** Now Trying to append a new line ********** \n")
# txt.seek(0, 0)
flo_sample.close()



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
teststr = '{:12} YES votes {:-21.4%}'.format(yes_votes, percen
tage + 2.3)
print(teststr)

# Zero evaluated as false expression "If not element" apply to Zero
a = [0, 1, 2]

for element in a:
    if not element:
        pass
    print(element, "testing pass")

for element in a:
    if not element:
        continue
    print(element, "testing continue")

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
#var_sum = sum(lst_interview[-6:-2])







# lst_interview = [11]


# def fnc_fnd_max(plist):
#     max = plist[0]
#
#     for inx in range(1, len(lst_interview)):
#         if plist[inx] > max:
#             max = plist[inx]
#     return max


# max_back = fnc_fnd_max(lst_interview)
# print("max_back :", max_back)


# project: get familiar with CLASS 03/26/2020

class Car:

    sound = "Waff!"

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

    def __str__(self):
        return "Make=" + self.make + "##Model=" + self.model + "##Year=" + str(self.year) + "##Color=" + self.color

    def all_info(self):
        return self.make + ' ' + self.model + ' ' + str(self.year) + ' ' + self.color




car101 = Car("Honda", "Accord", 1995, "orange")
car101.doors = 4
print(car101)
car101str = str(car101)
print(car101str)
print(car101.all_info())
car102 = Car("Honda", "Civic", 2010, "white")
Car.sound = 'Grrr!'
car102.sound = 'rrraf!'
car103 = Car("Honda", "Accord", 1995, "black")
car104 = Car("Nissan", "Civic", 2010, "grey")

dt_mmm = datetime.now()
dt_mmm.haha = 78


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
