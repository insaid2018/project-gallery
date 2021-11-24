
# <center>**Aviation Accident Analysis**</center>

## **Table of Contents**

**1.**  [**Introduction**](#Section1)
**2.**  [**Problem Statement**](#Section2)
**3.**  [**Installed & Imported Libraries**](#Section3)
**4.**  [**Data Pre-processing Steps**](#Section4)
**5.**  [**Insights from the EDA**](#Section5)

<a name=Section1></a>

## **1. Introduction**

- A lot can go wrong at **33,000 feet (10,058.4 m)** above the ground, and if you’re unlucky enough to be aboard when something does, the decisions you make could mean the difference between life and death.

- An Exploratory Data Analysis of **Aviation Crashes since 1908** has been performed and the dataset can be found [**here**](https://www.kaggle.com/saurograndi/airplane-crashes-since-1908).
<center><img  src="https://thumbs.dreamstime.com/b/isometric-plane-crash-ditched-20382935.jpg"  width=50%></center>

- **Almost 95% of airplane crashes have survivors**, so even if the worst does happen, your odds aren't as bad as you might think.

- The EDA Notebook can be found at [**`Aviation Accident Analysis.ipynb`**]() 

<a  name = Section2></a>

## **2. Problem Statement**

- **The Aviation Institue** (TIA) is a newly organized committee for aviation regulations.

- They want to **analyze** and **compare** the number of **aviation incidents** over the a **century worth** of observed crashes data
<center><img  src="https://png.pngitem.com/pimgs/s/5-57201_aircraft-clipart-airplane-wing-silhouette-transparent-background-airplane.png"  width=50%></center>

- The Institue has provided a dataset that contains data of **airplane accidents** involving **civil**, **commercial** and **military** transport worldwide **from 1908-09-17** to **2009-06-08**.

<a  name = Section3></a>

## **3. Installed & Imported Libraries**

<a  name = Section31></a>

### **3.1 Installed Libraries**

- For starters, we installed the `pandas_profiling` library which gives a quick, general overview of the dataset.
- Additionally, we have installed the `datascience` library that is required by pandas profiling library.

<a  name = Section32></a>

### **3.2 Imported Libraries**

The following libraries have been imported in the notebook:
<center><img  src="https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/187550926/original/cde47296f9d02346b6561eee753741d7272bfce6/do-data-analysis-in-python-using-numpy-pandas-matplotlib-seaborn.jpg"  width=50%></center>

- **Pandas**: Importing for panel data analysis
- **Pandas Profiling**: To perform data profiling
- **Numpy**: For numerical python operations
- **Matplotlib (Pyplot)**: A popular plotting library used along with pandas
- **Seaborn**: A library, built on matplotlib, to create beautiful plots
- **Plotly**: To create interactive graphs
- **WordCloud**: To create wordclouds
- **PIL.Image**: To import an image.

<a  name = Section4></a>

## **4. Data Pre-processing Steps**

<a  name = Section41></a>

### **4.1 Dataset Description**:

<center>

|Dataset| Records | Features | Dataset Size |
| :--: | :--: | :--: | :--: |
| Aviation Accident Analysis | 5268 | 13 | 1.52 MB |

<br>

|ID|Feature name|Feature description|
|:--|:--|:--|
|1|**Date**| Date of accident, in the format - January 01, 2001 |
|2|**Time**| Local time, in 24 hr. format unless otherwise specified |
|3|**Location**| Location of the accident |
|4|**Operator**| Airline or operator of the aircraft |
|5|**Flight #**| Flight number assigned by the aircraft operator |
|6|**Route**| Complete or partial route flown prior to the accident |
|7|**Type**| Aircraft type |
|8|**Registration**| ICAO registration of the aircraft |
|9|**cn/In**| Construction or serial number / Line or fuselage number |
|10|**Aboard**| Total aboard (passengers / crew) |
|11|**Fatalities**| Total fatalities aboard (passengers / crew) |
|12|**Ground**| Total fatalities on the ground |
|13|**Summary**| Brief description of the accident and cause if known |

</center>

### **4.2 Data Cleaning**

- In this section, we will perform the **cleaning** operations on the data using information from the previous section.

- We have to **clean the Time feature** extensively.

- We will also conver the **Date feature** to appropriate type and extract **Year**, **Month**, and **day** features from it.

- Next, we will convert all the strings in **Operator** feature to **uppercase** to avoid confusion.

- Finally, we will **drop the Ground feature**.

<a name=Section5></a>

## **5. Insights from the EDA**

<center><img  src="https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/35674/business-man-good-idea-clipart-xl.png" width=30%></center>

- The number of crashes **peaked in 1972** and have sustained **below 100** after that, with minimum crashes in 1983 (61 crashes).

- We need to observe here that **number of airlines** have kept on **increasing** over the years, and yet the number of **crashes are consistent**.

- Even though **fatalities increase** over the years, we don't have enough data like **number of passengers** over the years that used air transport to check the **true rate of fatalities**. 

- Most of the crashes are from **passenger airlines** in the dataset.


- The winter months of **December** and **January** have seen the **most number of crashes**.


- **AEROFLOT**, a Russian airline and **US Air Force** have seen the most number of crashes, with **more than 150 crashes each**.

- These two operators are responsible for **most fatalities** as well.

- For Aeroflot, the number of crashes **peaked in the 1970s** but gradually came down with a **no crashes** recorded between **1996 and 2008**.

- **Most of the notable crashes** are in the **USA** but we can observe many crashes in **Brazil** and **Russia** as well.

- Many commonly occuring words from the **crash summary** are **crew, approach, runway, landing, takeoff, weather conditions, short runway, failure, mountain, stalled**, and **engine failure** which can be used as a basis to indicate the reasons for crashes.


