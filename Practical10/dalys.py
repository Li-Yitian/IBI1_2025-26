#import nessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head())
print(dalys_data.info())
print(dalys_data.describe())
#show the third and fourth columns for the first 10 rows
print(dalys_data.iloc[0:10, 2:4])
#the year that has the highest dalys rate in afghanistan in the last 10 years
afg = dalys_data[dalys_data['Entity'] == 'Afghanistan']
afg_10=afg.head(10)
max_year = afg_10.loc[afg_10['DALYs'].idxmax()]['Year']
print("The year that has the highest DALYs rate in Afghanistan in the last 10 years is:", max_year)
#The year that has the highest DALYs rate in Afghanistan in the last 10 years is: 1998
#use == to filter the data for the country
zimbabwe = dalys_data[dalys_data['Entity'] == 'Zimbabwe']
print(zimbabwe[['Year', 'DALYs']])
#find the countries with the highest and the smallest dalys rate in 2019
dalys_2019 = dalys_data[dalys_data['Year'] == 2019]
max_country = dalys_2019.loc[dalys_2019['DALYs'].idxmax()]['Entity']
min_country = dalys_2019.loc[dalys_2019['DALYs'].idxmin()]['Entity']
print("The country with the highest DALYs rate in 2019 is:", max_country)
print("The country with the smallest DALYs rate in 2019 is:", min_country)
#The country with the highest DALYs rate in 2019 is: Lesotho
#The country with the smallest DALYs rate in 2019 is: Singapore

#draw a plot
country_data = dalys_data[dalys_data['Entity'] == 'Lesotho']
plt.plot(country_data["Year"], country_data["DALYs"], 'b+')#I think b+ is for blue plus markers
plt.xticks(rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs over time")
plt.show()