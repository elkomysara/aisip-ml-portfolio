# Categorizes an African country's income level based on GDP per capita
country = input("Enter the name of the African country: ")
gdp = float(input(f"Enter the GDP per capita for {country} (in USD): "))

# Thresholds based on general World Bank classifications
if gdp < 1135:
    income_level = "Low"
elif 1136 <= gdp <= 13845:
    income_level = "Middle"
else:
    income_level = "High"

print(f"{country} is categorized as a '{income_level}' income country.")
