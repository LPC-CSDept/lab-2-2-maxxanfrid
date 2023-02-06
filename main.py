def main():
    ##################################################
    # Comlete your code here
    ##################################################
    pass
reg_hours = 40
reg_rate = 18.25
o_rate = 27.78
total_hours = 50
overtime_hours = total_hours - reg_hours
regular_wages = reg_hours * reg_rate
overtime_wages = overtime_hours * o_rate
print(overtime_hours)
print(regular_wages)
print(overtime_wages)
total_wages = regular_wages + overtime_wages
print(total_wages)

if __name__ == '__main__':
    main()
