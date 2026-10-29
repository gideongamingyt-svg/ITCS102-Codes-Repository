# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)

age = int(input("Enter your age --->   "))
is_employed = bool(input("Are you current employed (True/False) --->   "))
credit_score = int(input("Enter your current credit score --->   "))
annual_income = float(input("How much is your  annual income --->   "))
has_collateral_ = bool(input("Do you have any collateral (True/False ) --->   )"))

baserate = 0.0

if age >= 19 and is_employed == True:
    print("Applicant pass baseline repirement")
    if credit_score >= 780: #tier1
        print("You have a high credit score")
        if annual_income >= 120000:
            base_rate = 4.5
            print("You have a high salary and high credit score, your interest rate is",base_rate)
        else:
            base_rate = 5.0
            print("You have a high salary and high credit score, your interest rate is",base_rate)  
    elif credit_score >= 600 and credit_score < 780:
        if has_collateral_ == True:
            base_rate = 7.0 
            print("You have a high salary and high credit score, your interest rate is",base_rate)
        elif annual_income <= 120000
        print("Low salary with Fair Credit Score")
        base_rate = 9.5 
        print("You have a high salary and high credit score, your interest rate is",base_rate)
    else: 
        print("Fair credit score with no collateral")
        base_rate = 8.0
        print("You have a high salary and high credit score, your interest rate is",base_rate
        print("failed") 
else: 
    print("Rejected: fails baseline criteria")               