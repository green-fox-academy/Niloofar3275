a = 24
out = 0
if a % 2 ==out:
    print(a-1)

# if a is even increment out by one

b = 13
if b>=10 and b<=20:
    out2 = "Sweet!"
    print(out2)
elif b<10:
    out2 = "Less!"
    print(out2)
elif b>20:
    out2="More!"
    print(out2)

# if b is between 10 and 20 set out2 to "Sweet!"
# if less than 10 set out2 to "Less!",
# if more than 20 set out2 to "More!"

c = 123
credits = 100
is_bonus = False
if credits >=50 and is_bonus:
    if credits <50 and is_bonus:
        if is_bonus and is_bonus:
            print(c)

# if credits are at least 50,
# and is_bonus is false decrement c by 2
# if credits are smaller than 50,
# and is_bonus is false decrement c by 1
# if is_bonus is true c should remain the same

d = 4
time = 120
out3 = ""
if d % 4 ==0 and time <= 200:
    out3="Check"
    print(out3)
elif time>200:
        out3="Time out"
        print(out3)
else:
        out3="Run Forest Run!"
        print(out3)

# if d is dividable by 4
# and time is not more than 200
# set out3 to "check"
# if time is more than 200
# set out3 to "Time out"
# otherwise set out3 to "Run Forest Run!"