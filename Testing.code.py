
from datetime import date, time, timedelta, datetime

from dateutil.relativedelta import *

def outputData(**kwargs):
    print( type(kwargs) )
    print( kwargs[ "name" ] )
    print( kwargs[ "num" ] )


outputData(name = "John Smith", num = 5, b = True)

def outputData(name, * args):
    print( type(args) )
    for arg in args:
        print(arg)


outputData("John Smith", 5, True, "Jess")

#generator
def square_int(p1, p2):
    for x in range(p1, p2 + 1):
        yield x**2

f1 = square_int(3, 10)
for item in f1:
    print(item)



def fib_gen():
    fib1 = 0
    fib2 = 1
    yield fib1
    yield fib2
    while True:
        result = fib1 + fib2
        fib1 = fib2
        fib2 = result
        yield result


f = fib_gen()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

for item in f:
    print(item)
    if item > 500:
        break

f2 = fib_gen()
for item in f2:
    print(item)
    if item > 500:
        break





#iterator

class Fibsec:
    def __iter__(self):
        self.status = 0
        self.f1 = 0
        self.f2 = 1
        return self

    def __next__(self):
        if self.status == 0:
            self.status = 1
            return self.f1
        elif self.status == 1:
            self.status = 2
            return self.f2
        else:
            _rslt = self.f1 + self.f2
            self.f1 = self.f2
            self.f2 = _rslt
            return _rslt


fb1 = iter(Fibsec())

for item in Fibsec():
    print (item)
    if item >= 5000:
        break


print(next(fb1))
print(next(fb1))
print(next(fb1))
print(next(fb1))
# print(next(fb1))
# print(next(fb1))
# print(next(fb1))
# print(next(fb1))
# print(next(fb1))
# print(next(fb1))







class Fib_ser:
    """Class to implement an iterator
    Fibonacci series """

    def __init__(self, max = 0):
        self.max = max
        self.next_n = []

    def __iter__(self):
        self.next_n.append(0)
        self.next_n.append(1)
        return self

    def __next__(self):
        if (self.next_n[-1] <= self.max):
            result = self.next_n[-1] + self.next_n[-2]
            self.next_n.append(result)
            return result
        else:
            raise StopIteration


for item in Fib_ser(500):
    print(item)

#Write an iterator class reverse_iter, that takes a list and iterates it from the reverse


class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if (self.n <= self.max) or self.max <= 0:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


for item in PowTwo(0):
    print(item)


x = PowTwo(30)
y = iter(x)

while True:
    try:
        print(next(y))
    except StopIteration:
        break







nums = [4, 3, 6, 7, 9]
it = iter(nums)
print(next(it))
print(next(it))

class Tst_iter():

    def __init__(self, max, pnums):
        self.max = max
        self.pnums = pnums
        self.lst_new = []

    def __iter__(self):
        return self

    def __next__(self):
         while True:
             for x in range(0, self.max):
                 if x <= self.max:
                     sorted(self.lst_new.append(self.nums[x]))
                 else:
                     raise StopIteration
             return self.lst_new


It = Tst_iter(3, nums)
print(next(it))


#Write a Python program to create Fibonacci series upto n using Lambda.

fib_next = lambda x, y: x + y
str_fib = [0, 1]
max_fib = 2000000
while True:
    new_elm = fib_next(str_fib[- 1], str_fib[ -2])
    if new_elm <= max_fib:
        str_fib.append(new_elm)
        print (str_fib[-1]/str_fib[-2])
    else:
        break


#Write a Python program to check whether a given string is number or not using Lambda.
mynum = lambda q: print(q)
mynum('accdefg')

is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))




isnum = 'Peter01'.isnumeric()
isnum = 'Good Morning'.isnumeric()
isnum = '123yuyuy'.isnumeric()
isnum = '45'.isnumeric()
isnum = '78.900'.isnumeric()

s = 'Region'
res = ''.join(filter(lambda c:  '0' <= c <= '9', s))

s = '2319'
res = ''.join(filter(lambda c:  '0' <= c <= '9', s))

s = 'Region9337'
res = ''.join(filter(lambda c:  '0' <= c <= '9', s))

s = 'Reg4747ion'
res = ''.join(filter(lambda c:  '0' <= c <= '9', s))


# true_false = str(lambda x: isnumeric(x))
#  r = true_false('12345654321')
#  print(r)

#Write a Python program to filter a list of integers using Lambda.

lst_mix = ['Orange', 123, 'Song', 765, 'Prince', 54]
filtered = list(filter(lambda x: isinstance(x, (int, float)), lst_mix))
print(filtered)

#Write a Python program to sort a list of dictionaries using Lambda.

d = { 5: 'Orange', 2: 'Cherry', 1: 'Apple', 4: 'Peach'}

itm = list(d.items())


sorted_d = sorted(d.items(), key=lambda x: x[0])
print(sorted_d)

#Slst_tpl.sort(key=lambda x: x)ort function using Lambda
lst_tpl = [
    ("ABC", 123, 321),
    ("AAA", 767, 111),
    ("ZZZ", 565, 999)
    ]



print(lst_tpl)


lst88 = ["Pear", "Apricot", "apple", "Cherry", "Apple", "Apple"]
lst88.sort(key=lambda x: x.upper())
lstnew = lst88.sort(key=lambda x: x.upper())

lst88.sort(key=lambda x: x[1:4].upper())  # order by substring

print(lst88)
print('test point 1')
print(lstnew)




def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("Double the number of 15 =", result(15))




# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result.

r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))



class Money:

    currency_rates = {
        'USD': 1,
        'EUR': 0.88,
        'CAN' : 0.95,
        'BPS' :1.46,
        'SFR' : 1.12
    }

    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount

    def __repr__(self):
        return '%s amount %.4f pizda' % (self.symbol, self.amount)

    def __str__(self):
        return 'Cur: %s  Amt: %.4f' % (self.symbol, self.amount)

    def convert1(self, othersymbol, otheramount = 0):
        new_amount = (otheramount * self.currency_rates[othersymbol] / self.currency_rates[self.symbol] )
        return Money(self.symbol, new_amount)

    def convert2(self, other):
        new_amount = (other.amount * self.currency_rates[other.symbol] / self.currency_rates[self.symbol] )
        return Money(self.symbol, new_amount)

    def convert3(self, symbol_to):
        new_amount = (self.amount * self.currency_rates[self.symbol] / self.currency_rates[symbol_to] )
        return Money(symbol_to, new_amount)


money01 = Money('SFR', 560)
money02 = money01.convert('CAN', 345)





money01 = Money('$', 145.13)
rmoney01 = money01.__repr__()
print(rmoney01)
money02 = money01.convert(Money('€', 150))


class Pair():
    def __init__(self, x, y, pname):
        self.x = x
        self.y = y
        self.name = pname

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r}, {0.name!r})'.format(self)

    def __str__(self):
        return 'Pair({0.x!s}, {0.y!s}, {0.name!s})'.format(self)
(vstr3)





vrepr = pair1.__repr__()
vstr  = pair1.__str__()

print(pair1)
print(vrepr)
print(vstr)


lst_dynamic = ('[(x**2) for x in range(7)]')
lst_in = ('lst_lit = [(x**2) for x in range(7)]')

exec(lst_in)
print(lst_lit)

lst_out = eval(lst_dynamic)

# exec('print(dir())')

print(eval("5 == 5"))

print(eval("4 < 10"))

print(eval("8 + 4 - 2 * 3"))

print(eval("'py ' * 5"))

print(eval("10 ** 2"))

print(eval("'hello' + 'py'"))



seval = '31 + 13'
e01 = seval
print(e01)
e02 = eval(seval)
print(e02)



num1 = 5
num2 = eval(str(num1 + num1))

print(num2)

print('eval')


class Pair():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r}, {0.name!r})'.format(self)

    def __str__(self):
        return 'instance Pair({0.x!s}, {0.y!s}, {0.name!s})'.format(self)

pair1 = Pair(7, 12, 'Great')
vrepr = pair1.__repr__()
vstr  = pair1.__str__()

print(pair1)
print(vrepr)
print(vstr)

pair1a = eval(vrepr)


seval = '31 + 13'
e01 = seval
print(e01)
e02 = eval(seval)
print(e02)


seval02 = 'e03 = (555 + 666) * 2'
exec(seval02)
print(e03)





yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
teststr = '{:12} YES votes {:-21.4%}'.format(yes_votes, percentage + 2.3)
print(teststr)



flt01 = 3627365845.329

print("To {1:#^28,.4f} be {0:10} ot not {0:30} to be? This is the question".format(451, flt01 ))

print("To {1:#^28,.4f} be {0:10} ot not {2:@^30,.2f} to be? This is the question".format(451, flt01, 12345678987654.321 ))


lit_name = 'Mayya'
lit_age = 60

format_lt = f'I know {lit_name}\'s age is {lit_age}'
print(format_lt)


qs = "quoted \t\tstring"
print( f'{qs}' )

print( f'{"quoted string"}' )




curr_dt01= date(2014, 7, 2)
curr_dt02 = date(2014, 7, 11)
print(curr_dt02)

dt_rel = relativedelta(curr_dt02, curr_dt01)  # difference between two days
print(dt_rel.days)
curr_dt01= date(2014, 7, 2)

curr_dt03 = curr_dt02 - curr_dt01
print(curr_dt03.days)

#print(dt_rel)

# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)

exam_st_date = (11, 12, 2014)

for x in range(0, len(exam_st_date)):
    print(exam_st_date[x])

x = datetime(exam_st_date[-1], exam_st_date[0], exam_st_date[1])

# display curr day excersise


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