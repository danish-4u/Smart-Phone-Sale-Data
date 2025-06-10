import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(r'C:\Users\iqbal\OneDrive\Desktop\BIT_Internship\Projects\Practice_projects\SmartPhoneSalefrom5Countries.xlsx')

years = sorted(df['Year'].unique())
countries = df['Country'].unique()
bar_width = 0.08
x = np.arange(len(years))

plt.figure(figsize=(18, 7))
for i, country in enumerate(countries):
    sales = df[df['Country'] == country].sort_values('Year')['Smartphone Sales (Millions)']
    plt.bar(x + i*bar_width, sales, width=bar_width, label=country)

plt.xlabel('Year')
plt.ylabel('Smartphone Sales (Millions)')
plt.title('Smartphone Sales by Country (2015-2025)')
plt.xticks(x + bar_width*len(countries)/2, years)
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.show()
