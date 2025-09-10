# 🐼 Programming Assignment - Pandas Data Analysis

This repository contains my programming assignments for **ECE 2112: Advanced Computer Programming and Algorithms**, focusing on data analysis using the Pandas library.

---

## ✧˖°. Contents

### ✨ [Experiment 3 – Python Data Analysis (Pandas)](Experiment3.ipynb)  
── Codes and functions incorporated in the Pandas library for data manipulation.

---

### Problem 1: Load Cars Dataset  
Load the CSV file into a DataFrame named `cars` and display the first and last five rows.

**Steps:**  
1. Download the dataset from [http://bit.ly/Cars_file](http://bit.ly/Cars_file).  
- **a.** Load it using `pandas.read_csv()`.  
- **b.** Display first and last five rows.

```python
import pandas as pd

cars = pd.read_csv('Cars.csv')
print(cars.head())
print(cars.tail())
```

### Problem 2: Data Extraction from Cars DataFrame
Using the `cars` DataFrame loaded in Problem 1, perform the following data extraction tasks:

- **a.** Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...).
- **b.** Display the row that contains the car model ‘Mazda RX4’.
- **c.** Find how many cylinders (‘cyl’) the car model ‘Camaro Z28’ has.
- **d.** Determine the number of cylinders (‘cyl’) and gear type (‘gear’) for the models:  
  ‘Mazda RX4 Wag’, ‘Ford Pantera L’, and ‘Honda Civic’.


```python
import pandas as pd

cars = pd.read_csv('Cars.csv')

print(cars.iloc[:5, ::2])

print(cars[cars['Model'] == 'Mazda RX4'])

print(cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0])

models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']])
```


## How to Run

1. Download the CSV dataset from: [http://bit.ly/Cars_file](http://bit.ly/Cars_file) and save it in your working directory.
2. Run **Surname_Pandas-P1.py** to load the dataset.
3. Run **Surname_Pandas-P2.py** to perform the required data extraction.
