current_year = int(input("enter the current year"))
final_year = int(input("enter the final year"))
for year in range(current_year,final_year +1):
    if (year % 4 == 0 and year %100 !=0 ):
        print(year)




