"""
You need to set the annual payment in one function and print the respective monthly payment in a separate function.
How would you fix the suggested code to work properly?
"""

def SetAnnual():
  global annual
  annual=10000
  return annual
def PrintMonthly():
  return "Your monthly payment is "+str(annual/12)+" USD."
annual_payment=SetAnnual()
monthly=PrintMonthly()
print(f"The Annual Payment is : {annual_payment} & The Monthly Payment is : {monthly}")