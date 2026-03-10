#original infection 5
#increase infection rate by 40% each day
#stop if infected people exceed 91
n = 91
a = 5
b = 0.4
day = 1
while a < n:
    print("Day", day, ":", int(a), "infected people")
    a = a * (1 + b)
    day += 1
print("In day", day,", evryone is infected")
    