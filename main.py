def main():
    ##################################################
    # Comlete your code here
    ##################################################
    workhours = int(input('Enter your number'))
    reg_hours = 40
    reg_rate = float(18.25)
    o_rate = float(27.78)
    overtime_hours = workhours - reg_hours
    regular_charge = reg_hours * reg_rate
    overtime_charge = overtime_hours * o_rate
    print(regular_charge) 
    print(overtime_charge)
    total_wage = regular_charge + overtime_charge
    print(total_wage)
pass 
if __name__ == '__main__':
    main()
