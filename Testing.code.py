
from datetime import date, time, timedelta, datetime

from dateutil.relativedelta import *


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