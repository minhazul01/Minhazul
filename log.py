healthy_income = False
high_credit = True
#if healthy_income and high_credit:
##  print("Eligible for loan")
#else:
   # print("Not eligible for loan")
if healthy_income or high_credit : #and not healthy_income:
    print("Eligible for loan")
else:
    print("Not eligible for loan")