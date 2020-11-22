# Package Research - Pandas

## Package Summary
> Pandas is a python package that provides fast, flexible, and expressive data structures designed to make working with labeled data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis and manipulation tool available in any language.

> Pandas is well suited for many different kinds of data such as:

> * Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet

> * Ordered and unordered (not necessarily fixed-frequency) time series data.

> * Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels

> * Any other form of observational / statistical data sets. The data actually need not be labeled at all to be placed into a pandas data structure

> Its popularity rises over time as the template shows. 

> ![image of pandas popularity](https://149351115.v2.pressablecdn.com/wp-content/uploads/2017/09/common_other_tags-1-1024x1024.png)

## Install and Run Instructions
> The easiest way to install Pandas is to install it as part of the [Anaconda](https://docs.continuum.io/anaconda/) since not only Pandas, also it has sciPy stack so user doesn't have to download additional prgram. In addition, it doesn't require admin rights so user can install it directly to home directory. If you choose to use this method, this [website](https://www.geeksforgeeks.org/how-to-install-python-pandas-on-windows-and-linux/) has the specific instructions for installation. 

>Other than that, it is also possible to install the package from source, [PyPI](https://pypi.org/project/pandas/) -- type `pip install pandas` on the command prompt for installation, [ActivePython](https://www.activestate.com/products/python/downloads/) or various Linux distributions. 

> Pandas is available in Python 3.6.1 and above, 3.7, 3.8, and 3.9.

## Code
> I wrote the code that could go over the list of various types of alcohol that consumed over the world, and compare the amount of wine comsumption between Albania and Algeria.

> I loaded the data in csv file first:

```
import pandas as pd

df = pd.read_csv(r"/Users/annahyunjin/Desktop/project/alcohol.csv")
```

> Then drop the columns below cloumn 5 by using `drop` function. After that, I used the `mean` function to get the average amount of each type of alcohol that countries consume overall to show the differences in amount of them.  

> As the preparation for my final goal, I chose Algeria and Albania columns and convert the data to integers by using `for loop`. Then, by using operator, I wrote down the condition in the `if..else..` conditional expression that compares the the amount of wine consumption in Algeria and Albania. 

```
albwine = first_row[3]
algwine = second_row[3]

if albwine > algwine:
    print("Albania comsumes more wine than Algeria.")
else:
    print("Algeria consumes more wine than Albania.")
```

## Future Idea
> Although I couldn't do much since it was my first time interacting with the Pandas, if I have a chance to use it for the final project, I would create the file that compares the rate of unemployment around the world and see which country has the lowest rate. This package would help me to extract unnecssary information and use the numbers conviently for the comparison. 
