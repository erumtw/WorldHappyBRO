import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
plt.style.use("seaborn-whitegrid")
import warnings            
warnings.filterwarnings("ignore")

url15 = 'https://raw.githubusercontent.com/misterjimza/WorldHappyBRO/main/World%20Happiness%20Report%20up%20to%202022/2015.csv'
url16 = 'https://raw.githubusercontent.com/misterjimza/WorldHappyBRO/main/World%20Happiness%20Report%20up%20to%202022/2016.csv'
url17 = 'https://raw.githubusercontent.com/misterjimza/WorldHappyBRO/main/World%20Happiness%20Report%20up%20to%202022/2017.csv'
url19 = 'https://raw.githubusercontent.com/misterjimza/WorldHappyBRO/main/World%20Happiness%20Report%20up%20to%202022/2019.csv'
url18 = 'https://raw.githubusercontent.com/misterjimza/WorldHappyBRO/main/World%20Happiness%20Report%20up%20to%202022/2018.csv'
url20 = 'https://raw.githubusercontent.com/misterjimza/WorldHappyBRO/main/World%20Happiness%20Report%20up%20to%202022/2020.csv'
url21 = 'https://raw.githubusercontent.com/misterjimza/WorldHappyBRO/main/World%20Happiness%20Report%20up%20to%202022/2021.csv'
url22 = 'https://raw.githubusercontent.com/misterjimza/WorldHappyBRO/main/World%20Happiness%20Report%20up%20to%202022/2022.csv'

y_2015 = pd.read_csv(url15, on_bad_lines='skip');
y_2016 = pd.read_csv(url16, on_bad_lines='skip');
y_2017 = pd.read_csv(url17, on_bad_lines='skip');
y_2018 = pd.read_csv(url18, on_bad_lines='skip');
y_2019 = pd.read_csv(url19, on_bad_lines='skip');
y_2020 = pd.read_csv(url20, on_bad_lines='skip');
y_2021 = pd.read_csv(url21, on_bad_lines='skip');
y_2022 = pd.read_csv(url22, on_bad_lines='skip');

data = pd.concat([y_2015, y_2016, y_2017, y_2018, y_2019, y_2020, y_2021, y_2022],sort=False)
print(data)

# แสดงค่าอธิบายข้อมูล
print(data.describe().T)
print(data.info())
data.rename(columns={
    "Overall rank": "rank",
    "Overall Rank": "rank",
    "Country or region": "country",
    "Score": "score",
    "GDP per capita": "gdp",
    "GDP per Capita": "gdp",
    "Social support": "social",
    "Healthy life expectancy": "healthy",
    "Freedom to make life choices": "freedom",
    "Generosity": "generosity",
    "Perceptions of corruption": "corruption"
},inplace=True)
del data["rank"]
print(data)
print(data.info())

# Missing value
data.columns[data.isnull().any()]
data.isnull().sum()
data[data["corruption"].isnull()]

avg_data_corruption = data[data["score"] > 6.774].mean().corruption
data.loc[data["corruption"].isnull(),["corruption"]] = avg_data_corruption