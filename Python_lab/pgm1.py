start_year=int(input("enter start year"))

end_year=int(input("enter end year"))

print("leap years")

for year in range(start_year ,end_year):
	if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
		print(year)
