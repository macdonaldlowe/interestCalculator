accrualRate = 1.04
money = 1000.00

withdrawl = 100.00
yearCounter = 0

# for x in range(20):
#     yearCounter += 1
#     if yearCounter > 10:
#         break;
#     print(f"year:  {yearCounter}")


for x in range(20):
    yearCounter += 1
    if money < withdrawl:
        break
    money = money - withdrawl
    money = money * accrualRate
    print(f"Year: {yearCounter}, Money: {money}")
