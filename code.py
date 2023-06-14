import argparse
import math

# Function to calculate and print differentiated payments
def calculate_differentiated_payment(principal, periods, interest):
    total_payment = 0
    interest = interest / (12 * 100)  # Convert interest to monthly decimal
    for month in range(1, periods + 1):
        # Calculate differentiated payment using the formula
        differentiated_payment = principal / periods + interest * (principal - (principal * (month - 1)) / periods)
        total_payment += math.ceil(differentiated_payment)
        print(f"Month {month}: payment is {math.ceil(differentiated_payment)}")
    overpayment = total_payment - principal
    print(f"\nOverpayment = {math.ceil(overpayment)}")

# Function to calculate and print annuity payment
# def calculate_annuity_payment(principal, periods, interest):
#     interest_rate = interest / (12 * 100)
#     denominator = (1 - (1 + interest_rate) ** -periods)
#     annuity_payment = principal * (interest_rate / denominator)
#     return annuity_payment

def calculate_annuity_payment(principal, periods, interest):
    interest = interest / (12 * 100)  # Convert interest to monthly decimal
    annuity_payment = math.ceil(principal * (interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1))
    print(f"Your annuity payment = {annuity_payment}")
    calculate_overpayment(principal, annuity_payment, interest, periods)

# Function to calculate and print loan principal
# def calculate_principal(payment, periods, interest):
#     interest = interest / (12 * 100)  # Convert interest to monthly decimal
#     principal = payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
#     print(f"Your loan principal = {math.floor(principal)}!")
#     overpayment = payment * periods - principal
#     print(f"Overpayment = {math.ceil(overpayment)}")

def calculate_principal(periods, payment, interest):
    interest = interest / (12 * 100)  # Convert interest to monthly decimal
    principal = payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
    principal = math.floor(principal)
    overpayment = round(payment * periods - principal)
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {overpayment}")

def calculate_overpayment(principal, payment, interest, periods):
    overpayment = (payment * periods) - principal
    print(f"Overpayment = {round(overpayment)}")

# def calculate_overpayment(principal, payment, interest):
#     interest = interest / (12 * 100)  # Convert interest to monthly decimal
#     periods = math.log(payment / (payment - interest * principal), 1 + interest)
#     overpayment = payment * periods - principal
#     print(f"Overpayment = {math.ceil(overpayment)}")

# Function to calculate and print the number of periods
def calculate_periods(payment, principal, interest):
    interest = interest / (12 * 100)  # Convert interest to monthly decimal
    periods = math.log(payment / (payment - interest * principal), 1 + interest)
    periods = math.ceil(periods)  # Round up to the nearest whole number of periods
    years = periods // 12
    months = periods % 12
    if years == 1 and month > 0:
        print(f"You need {years} year and {months} months to repay this loan!")
    elif years == 1:
        print(f"You need {years} year to repay this loan!")
    elif years > 0 and months > 0:
        print(f"You need {years} years and {months} months to repay this loan!")
    elif years > 0:
        print(f"You need {years} years to repay this loan!")
    elif months > 0:
        print(f"You need {months} months to repay this loan!")
    else:
        print("You can repay the loan in 1 month!")
    overpayment = payment * periods - principal
    print(f"Overpayment = {round(overpayment)}")


# Main function to handle command-line arguments and execute the program
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, help="Type of payment: 'annuity' or 'diff'")
    parser.add_argument("--principal", type=float, help="Loan principal")
    parser.add_argument("--payment", type=float, help="Monthly payment amount")
    parser.add_argument("--periods", type=int, help="Number of monthly payments")
    parser.add_argument("--interest", type=float, help="Nominal interest rate (in percent)")

    args = parser.parse_args()
    if args.type == "diff":
        # Differentiated payment calculation
        if args.payment:
            # If payment is specified, it's an incorrect parameter for differentiated payment
            print("Incorrect parameters")
        elif args.principal and args.periods and args.interest:
            # If principal, periods, and interest are provided, calculate differentiated payment
            calculate_differentiated_payment(args.principal, args.periods, args.interest)
        else:
            # If any required parameters are missing, it's an incorrect parameter for differentiated payment
            print("Incorrect parameters")

    elif args.type == "annuity":
        if args.periods and args.payment and args.interest:
            calculate_principal(args.periods, args.payment, args.interest)
        elif args.payment and args.principal and args.interest:
            calculate_periods(args.payment, args.principal, args.interest)
        elif not args.principal or not args.periods or not args.interest:
            print("Incorrect parameters")
        else:
            # Calculate annuity payment
            calculate_annuity_payment(args.principal, args.periods, args.interest)
    else:
        # Incorrect type parameter
        print("Incorrect parameters")

# Execute the main function
if __name__ == "__main__":
    main()