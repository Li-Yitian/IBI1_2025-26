population_data = {"UK":{"2020":66.7,"2024":69.2},
                   "China":{"2020":1426,"2024":1410},
                   "Italy":{"2020":59.4,"2024":58.9},
                   "Brazil":{"2020":208.6,"2024":212.0},
                   "USA":{"2020":331.6,"2024":340.1}}
#percentage change=(population in 2024 - population in 2020)/population in 2020 * 100
percentage_change = {}
for country, data in population_data.items():
    change = (data["2024"] - data["2020"]) / data["2020"] * 100
    percentage_change[country] = change
print("Population growth rate from 2020 to 2024:")
for country, change in percentage_change.items():
    print(f"{country}: {round(change, 2)}%")
#print the population growth rate in descending order
sorted_change = sorted(percentage_change.items(), key=lambda x: x[1], reverse=True)
print("\nPopulation growth rate in descending order:")
for country, change in sorted_change:
    print(f"{country}: {round(change, 2)}%")    
#print the country with the highest population growth rate using the sorted list
highest_growth_country = sorted_change[0][0]
print(f"\nCountry with the highest population growth rate: {highest_growth_country}")       
#print the country with the lowest population growth rate using the sorted list 
lowest_growth_country = sorted_change[-1][0]
print(f"Country with the lowest population growth rate: {lowest_growth_country}")
#similar to the previous part, but change = (population in 2024 - population in 2020) instead of percentage change
change= {}
#define population_2020 and population_2024 dictionaries
population_2020 = {country: data["2020"] for country, data in population_data.items()}
population_2024 = {country: data["2024"] for country, data in population_data.items()}
for country, population in population_2024.items():
    change[country] = population - population_2020[country]
#print the country that population increased the most using the change dictionary
highest_increase_country = max(change, key=change.get)
print(f"\nCountry with the highest population increase: {highest_increase_country}")
#print the country that population decreased the most using the change dictionary
lowest_increase_country = min(change, key=change.get)
print(f"Country with the lowest population decrease: {lowest_increase_country}")
#create a bar chart of population growth rate for each country
import matplotlib.pyplot as plt
countries = list(percentage_change.keys())
growth_rates = list(percentage_change.values())
plt.bar(countries, growth_rates, color=['lightcoral', 'lightblue', 'lightgreen', 'yellow', 'lightpink'])
plt.xlabel("Country")
plt.ylabel("Population Growth Rate (%)")
plt.title("Population Growth Rate from 2020 to 2024")
plt.ylim(-5, 5)
plt.axhline(0, color='gray', linewidth=0.8)
plt.show()#check the code