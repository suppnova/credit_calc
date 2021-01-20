# python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

import sys
import argparse
import math
parser = argparse.ArgumentParser(description="credit calculator")
parser.add_argument("--type", type=str, choices=["annuity", "diff"],
                    help="indicates the type of payment")
parser.add_argument("--principal", type=int,
                    help="the loan principal")
parser.add_argument("--periods", type=int,
                    help="denotes the number of months needed to repay the loan")
parser.add_argument("--interest", type=float,
                    help="annual interest rate, specified without a percent sign")
parser.add_argument("--payment", type=float,
                    help="the mounthly payment amount")
args = parser.parse_args()

def diff_payment():
    payments = 0
    for month in range(1, args.periods + 1):
        diff_payment = args.principal/args.periods + i * (
        args.principal - args.principal*(month - 1) / args.periods
        )
        print(f"Month {month}: payment is {math.ceil(diff_payment)}!")
        payments += math.ceil(diff_payment)
    print("\nOverpayment =", payments - args.principal)

def ann_payment():
    ann_payment = args.principal * i * (1 + i)**args.periods / (
                    (1 + i)**args.periods - 1
                    )
    print(f"Your annuity payment = {math.ceil(ann_payment)}!")
    print(
        "Overpayment =", math.ceil(ann_payment) * args.periods - 
        args.principal
    )

def y_end(years_number):
    if years_number == 1:
        return 'year'
    return 'years'

def m_end(pay_months_number):
    if pay_months_number == 1:
        return 'month'
    return 'months'

def periods_calc():
    months_to_pay = math.ceil(
        math.log(args.payment / (
            args.payment - i * args.principal
            )
            , 1 + i)
        )
    years = months_to_pay // 12
    months = months_to_pay % 12
    if years == 0:
        print(
        f"{months} {m_end(months)} to repay this loan!"
        )
    elif months == 0:
        print(
            f"It will take {years} {y_end(years)} to repay this loan!"
        )
    else:
        print(
            f"It will take {years} {y_end(years)} and " +
            f"{months} {m_end(months)} to repay this loan!"
        )
    print(
        "Overpayment =", int(args.payment * months_to_pay) - 
        args.principal
    )

def principal_calc():
    loan = math.floor(args.payment / (
        i * (1 + i)**args.periods / ((1 + i)**args.periods - 1))
    )
    print(f"Your loan principal = {loan}!")
    print(
        "Overpayment =", int(args.payment * args.periods) - loan
    )

def check_positive_args():
    if (
        (args.payment is None or args.payment >= 0)
        and
        (args.periods is None or args.periods >= 0)
        and
        (args.principal is None or args.principal >= 0)
        and
        (args.interest is not None and args.interest > 0)
    ):
        return True
    return False


if check_positive_args():
    i = args.interest / (12 * 100)

    if args.type == "diff":
        if args.payment == None:
            diff_payment()
        else:
            print("Incorrect parameters")

    elif args.type == "annuity":
        if args.payment == None:
            ann_payment()
        else:
            if args.periods == None:
                periods_calc()
            elif args.principal == None:
                principal_calc()
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")

    


