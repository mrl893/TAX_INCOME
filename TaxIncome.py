# initialize the constants
RATE = 0.85
TAX_RATE = 0.20
STANDARD_DEDUCTION = 100000.0
DEPENDENT_DEDUTION = 3000.0
EMPLOYMENT_INSURANCE = 546879.0

gross_income  = float(input(" Enter the gross income: "))
number_dependents = int(input("Enter the number of dependents: "))
tax_able_income = gross_income - STANDARD_DEDUCTION - \
    DEPENDENT_DEDUTION * number_dependents + EMPLOYMENT_INSURANCE
income_tax = tax_able_income * TAX_RATE 

print("The tax is $ " + str(income_tax))
