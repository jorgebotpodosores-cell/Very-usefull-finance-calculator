import sys


def main():
    try:
        if sys.argv[1] == "compound":
            while True:
                print("--- Investment Parameters ---")
                try:
                    amount = float(input("Monthly deposit (€): "))
                    rate = float(input("Annual interest rate (%): "))
                    years = int(input("Investment horizon (years): "))
                    start = float(input("Starting balance (€) [Press Enter for 0]: ") or 0)
                except ValueError:
                    print("Some value not number.")
                    continue
                else:
                    break
            value = compound(amount, rate, years, start)
            print(f"€{value:,}")
            sys.exit()
        elif sys.argv[1] == "IRPF":
            while True:
                try:
                    gross = float(input("Gross salary income: "))
                except ValueError:
                    continue
                else:
                    net, rate = IRPF(gross)
                    print("--- Results ---")
                    print(f"Net yearly income: €{net}")
                    print(f"Net monthly income: €{net / 14: .2f}")
                    if rate > 0:
                        print(f"Actual tax rate: {rate}%")
                    sys.exit()
        elif sys.argv[1] == "freedom":
            while True:
                try:
                    amount = float(input("Monthly freedom budget: "))
                except ValueError:
                    continue
                else:
                    n = freedom(amount)
                    print(f"Value of investments required: €{n:,.2f}")
                    sys.exit()
        elif sys.argv[1] == "gains":
            while True:
                try:
                    amount = float(input("Capital gains profit: "))
                except ValueError:
                    continue
                else:
                    n, a = capital(amount)
                    print(f"After taxes: €{n:,.2f}")
                    print(f"Effecive tax rate: {a:.2f}%")
                    sys.exit()
        elif sys.argv[1] == "emergency":
            while True:
                try:
                    amount = float(input("Mandatory fixed monthly expenses: "))
                    reserve = float(input("Money saved up in case of emergency: "))
                    if amount == 0:
                        continue
                except ValueError:
                    continue
                else:
                    n = fund(amount, reserve)
                    if n <= 3:
                        print(f"Bad score, reserve will last only {n:.0f} months")
                    elif n > 3 and n <= 12:
                        print(f"Ideal amount stored, start investing: {n:.0f} months")
                    else:
                        print(f"Bad score, start investing now or money will be lost aggressively to inflation: {n / 12:.0f} years")
                    sys.exit()
        elif sys.argv[1] == "savings":
            while True:
                try:
                    amount = float(input("Money saved every month: "))
                    years = float(input("Years this will be repeated: "))
                except ValueError:
                    continue
                else:
                    n, lost = savings(amount, years)
                    print(f"Money saved up over time: €{n:,}")
                    print(f"Money lost because of not invesing: €{lost:,}")
                    sys.exit()
        else:
            sys.exit("Terminal-line command incorrect")
    except IndexError:
        sys.exit("Terminal-line command required")




def compound(amount, rate, years, start=0):
    total_month = 0
    money = start
    rate = (rate / 100) / 12
    total_months = years * 12
    while total_month < total_months:
        money += amount
        monthgain = (money) * rate
        money += monthgain
        total_month += 1
    return round(money, 2)

def IRPF(gross):
    social = gross * 0.047
    taxable = gross - 5550 - social
    if taxable <= 0:
        return gross, 0.0
    # Create the variables and list
    brackets = [
    (12450, 0.19),
    (7750, 0.24),
    (15000, 0.30),
    (24800, 0.37),
    (240000, 0.45),
    (float('inf'), 0.47)]
    total_tax = 0
    for limit, rate in brackets:
        if taxable > limit:
            total_tax += limit * rate
            taxable -= limit
        else:
            total_tax += taxable * rate
            break
    effective_rate = ((total_tax + social)/gross) * 100
    net = gross - total_tax - social
    return round(net, 2), round(effective_rate, 2)

def freedom(m_budget):
    a_budget = m_budget * 12
    investment_amount = a_budget * 25
    return investment_amount

def capital(profit):
    original_profit = profit
    # Create the variables and list
    brackets = [
    (6000, 0.19),
    (18000, 0.21),
    (26000, 0.23),
    (150000, 0.27),
    (float('inf'), 0.28)]
    total_tax = 0
    for limit, rate in brackets:
        if profit > limit:
            total_tax += limit * rate
            profit -= limit
        else:
            total_tax += profit * rate
            break
    effective_rate = (total_tax / original_profit) * 100
    net = original_profit - total_tax
    return round(net, 2), round(effective_rate, 2)

def fund(amount, reserve):
    months_left = reserve / amount
    return months_left


def savings(month, years):
    yar_savings = month * 12
    total = yar_savings * years
    money = compound(month, 8, years)
    money_lost = money - total
    return round(total), round(money_lost, 2)







if __name__ == "__main__":
    main()
