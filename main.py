def main():
    ##################################################
    # Comlete your code here
    ##################################################
    pass
workhours = int(input('Enter your number'))
reg_hours = 40
reg_rate = 18.25
o_rate = 27.7850
overtime_hours = int(workhours - reg_hours)
regular_charge = int(reg_hours * reg_rate)
overtime_charge = int(overtime_hours * o_rate)
print(regular_charge) 
print(overtime_charge)
total_wage = regular_charge + overtime_charge
print(total_wage)

if __name__ == '__main__':
    main()
