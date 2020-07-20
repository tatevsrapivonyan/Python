import sys
import math


args = sys.argv
lst = []


def split_(par):
    new_lst = []
    for param in range(len(par)):
        if par[param] == "=":
            new_lst.append(par[2:param])
            new_lst.append(par[param + 1:])
    
    return new_lst


def finder(lst1, el):
    for item in lst1:
        if el in item:
            return True
    return False


for arg in range(1, len(args)):
    lst.append(split_(args[arg]))


if len(args) != 5:
    print("Incorrect parameters.")
if lst[0][1] == "diff" and finder(lst, "payment"):
    print("Incorrect parameters.")
if not finder(lst, "interest"):
    print("Incorrect parameters.")

for i in range(1, len(lst)):
    if float(lst[i][1]) < 0:
        print("Incorrect parameters.")

p, i, a, n = 0, 0, 0, 0

for i in range(1, len(lst)):
    if lst[i][0] == "principal":
        p = int(lst[i][1])
    elif lst[i][0] == "interest":
        i = float(lst[i][1]) / (12 * 100)
    elif lst[i][0] == "payment":
        a = int(lst[i][1])
    elif lst[i][0] == "periods":
        n = int(lst[i][1])


if lst[0][1] == "diff":
    m = 1
    total_paid = 0
    while m <= n:
        dif = math.ceil(p / n + i * (p - ((p * (m - 1)) / n)))
        print(i)
        total_paid += dif
        print(f"Month {m}: paid out {dif}")
        m += 1
    print(f"Overpayment = {total_paid - p}")
elif lst[0][1] == "annuity":
    if a == 0:
        ans = round(p * (i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)) + 1
        print(f"Your annuity payment = {ans}!")
        print(f"Overpayment = {ans * n - p}")
    elif n == 0:
        ans = round(math.log(a / abs((a - i * p)), i + 1))
        if ans > 12 and ans % 12 != 0:
            print(f"You need {ans // 12} years and {(ans % 12) + 1} months to repay this credit!")
            print(f"Overpayment = {a * ans - p}")
        elif ans > 12 and ans % 12 == 0:
            print(f"You need {ans // 12} years to repay this credit!")
            print(f"Overpayment = {a * ans - p}")
        else:
            print(f"You need {ans} months to repay this credit!")
            print(f"Overpayment = {a * ans - p}")
    elif p == 0:
        ans = math.floor(a * ((1 + i) ** n - 1) / (i * (1 + i) ** n))
        print(f"Your credit principal = {ans}!")
        print(f"Overpayment = {n * a - ans}")
else:
    print("Incorrect parameters.")

