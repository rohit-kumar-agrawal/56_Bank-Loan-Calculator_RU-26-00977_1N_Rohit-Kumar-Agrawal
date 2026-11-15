
def calculate_emi(principal, annual_rate, months):
    """Monthly EMI, rounded to 2 decimals. Handles the 0% rate case."""
    if annual_rate == 0:
        return round(principal / months, 2)
    r = annual_rate / 12 / 100
    emi = principal * r * (1 + r) ** months / ((1 + r) ** months - 1)
    return round(emi, 2)


def calculate_total_payable(emi, months):
    """Total payable uses the already-rounded EMI."""
    return round(emi * months, 2)


def calculate_total_interest(total_payable, principal):
    return round(total_payable - principal, 2)


def check_eligibility(emi, income):
    """Eligible if EMI is at most 40% of monthly income."""
    max_emi = round(income * 0.40, 2)
    return emi <= max_emi, max_emi


def read_number(prompt):
    """Read a number, return None if the user types something else."""
    try:
        return float(input(prompt))
    except ValueError:
        return None


def main():
    principal = read_number("Principal: ")
    if principal is None or principal <= 0:
        print("Invalid loan amount. Enter a positive amount.")
        return

    rate = read_number("Annual rate: ")
    if rate is None or rate < 0 or rate > 30:
        print("Invalid interest rate. Enter a rate between 0 and 30.")
        return

    months = read_number("Tenure (months): ")
    if months is None or months != int(months) or months < 1 or months > 360:
        print("Invalid tenure. Enter whole months between 1 and 360.")
        return
    months = int(months)

    income = read_number("Monthly income: ")
    if income is None or income <= 0:
        print("Invalid income. Enter a positive amount.")
        return

    emi = calculate_emi(principal, rate, months)
    total_payable = calculate_total_payable(emi, months)
    total_interest = calculate_total_interest(total_payable, principal)
    eligible, max_emi = check_eligibility(emi, income)

    print()
    if eligible:
        print(f"EMI: Rs. {emi:.2f} | Total Payable: Rs. {total_payable:.2f}")
        print(f"Total Interest: Rs. {total_interest:.2f} | Eligible: Yes")
    else:
        print(f"EMI: Rs. {emi:.2f}")
        print(f"Maximum allowed EMI (40% of income): Rs. {max_emi:.2f}")
        print("Loan not eligible: EMI exceeds the allowed limit.")


main()