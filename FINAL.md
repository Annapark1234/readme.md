# The Effect of Covid-19 on Unemployment Rate in the United States

## Program Purpose
> The covid-19 outbreak caused various global problems, including rising unemployment. It significantly impacted young workers, women, workers with low educational attainment, part-time workers, and racial and ethnic minorities.
According to [Pew Research Center](https://www.pewresearch.org/fact-tank/2020/06/11/unemployment-rose-higher-in-three-months-of-covid-19-than-it-did-in-two-years-of-the-great-recession/#:~:text=Unemployment%20rose%20higher%20in%20three,years%20of%20the%20Great%20Recession&text=The%20COVID%2D19%20outbreak%20and,20.5%20million%20in%20May%202020),
The outbreak of COVID-19 and the economic downturn it generated have raised the ranks of unemployed Americans by over 14 million, from 6.2 million in February to 20.5 million in May 2020. 

>The program's purpose is to analyze the overall rate of unemployment throughout the United States and compare each state's status 
with an average rate to check how many states have low and high rate since Covid-19 started.

> For accuracy, this program's data was collected from the [Bureau of Labor Statistics](https://www.bls.gov/home.htm), a unit of the United States Department of Labor.
> As for the library, Pandas, Matplotlib, and BeautifulSoup, were used for the program. Each library was to manipulate tables and variables from data,
visualize the data frame, and pull data out of the HTML file. All libraries were used in Jupyter. 
> ![image of pandas, matplotlib](https://pythonforundergradengineers.com/posts/matplotlib/images/four_logos.png)

## Installation for Each Library:
* `pip install pandas`
* `pip3 install matplotlib`
* `pip install beautifulsoup4`

## Visualizing the unemployment rate between October 2019 and October 2020 
> To see the difference in rate after the covid-19 outbreak, the chart that shows [the civilian unemployment rate](https://www.bls.gov/opub/ted/2020/unemployment-rate-falls-to-6-point-9-percent-in-october-2020.htm#:~:text=The%20unemployment%20rate%20decreased%20by,February%20rate%20of%203.5%20percent.) was used for the program.
Since the file was in an HTML, the data was converted into a CSV file using BeautifulSoup.

```
import pandas as pd

import os

import sys

from bs4 import BeautifulSoup

path = 'unemployment rate.html'

data = []

# Getting the header from HTML file

list_header = [] 
soup = BeautifulSoup(open(path),'html.parser') 
header = soup.find_all("table")[0].find("tr") 

for items in header: 
    try: 
        list_header.append(items.get_text()) 
    except: 
        continue
        
# Getting the data

HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data: 
    sub_data = [] 
    for sub_element in element: 
        try: 
            sub_data.append(sub_element.get_text()) 
        except: 
            continue
    data.append(sub_data)
    
 # Storing data into Pandas
 
 dataFrame = pd.DataFrame(data = data, columns = list_header)
 
 # Converting Pandas DataFrame into csv file
 
 dataFrame.to_csv('unemploymentrate.csv.') 
 
 ```
> Then to create the bar graph out of the chart, matplotlib was used:
 
 ```
 import matplotlib.pyplot as plt
 
 df.plot(x ='Month', y='Unemployment Rate', kind = 'bar')
 plt.show()
 
 ```
> The result showed as:
 
> ![unemploymentrate-1](https://user-images.githubusercontent.com/40219635/102843161-9eba3d80-43d6-11eb-9414-f3d6e6342ee1.png)

## Calculate Average Rate of Unemployment
> To calculate average rate of unemployment, the [chart that shows unemployment rate for each state](https://www.bls.gov/web/laus/laumstrk.htm) was brought into
the program by using CSV and changed variables in the chart into numeric form to do math.
```
import csv

f = open("/Users/annahyunjin/Desktop/final/states.csv")
comparison = list(csv.reader(f))

print(comparison)

# Remove unnecessary row

comparison = comparison[1:]

print(comparison)

# Convert string to number for unemployment rate

rate = []

for cp in comparison:
    rate.append(cp[1])
    
print(rate)
```
> After getting the list of rate in numeric form, the average was calculated.
```
rate_avg = sum(rate)/len(rate)

print("Average unemployment rate is: ", rate_avg)
```
## Average Unemployement Rate VS. Each State's Status
> To determine how many states has the lower or higher unemployment rate than average rate, 'if..elif' was used.
```
low_rate = 0.0
high_rate = 0.0

for cp in comparison:
    rate = cp[1]
    if rate <= rate_avg:
        low_rate = low_rate + 1.0
        
    elif rate > rate_avg:
        high_rate = high_rate + 1.0
        

print("The number of states with LOW unemployment rate: ", low_rate)
print("The number of states with HIGH unemployment rate: ", high_rate)
```
> Outcome:
> <img width="481" alt="Comparison" src="https://user-images.githubusercontent.com/40219635/102845772-45eda380-43dc-11eb-95c8-6d11555cc7fe.png">

## Analysis of Results
> The unemployment rate in the United States was severely impacted by covid-19 outbreak. As the chart on below shows, it is noticeable that 
the rate increased drastically during the year, although the rate decreased a little after reaching the peak at the beginning of outbreak. 

> ![unemploymentrate-1](https://user-images.githubusercontent.com/40219635/102843161-9eba3d80-43d6-11eb-9414-f3d6e6342ee1.png)

> In comparing the average unemployment rate and each state's status in November 2020, 27 States have a lower rate than the average rate, and 24 States with a higher rate.
Though the results are unexpected after looking at the chart of unemployment rate differences during the year, the output indicates that there is a hope to recover the economy quicker compared to
the huge damage. 

## Future Idea
> For a future project, the program can focus on the group of minorities to understand how much economic damage they suffered because of covid-19.
