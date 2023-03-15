total_rent= int(input("enter your total rent:"))
Total_electricity= int(input("enter your electricity unit:"))
electricity_charged= int(input("enter your electricity charged per unit:"))
unit_conversion= Total_electricity * electricity_charged
no_of_person= int(input("no. of person to be devide the amount:"))
Each_person_will_pay=(total_rent + unit_conversion)/(no_of_person)
print(f"Each_person_will_pay={round(Each_person_will_pay)}")