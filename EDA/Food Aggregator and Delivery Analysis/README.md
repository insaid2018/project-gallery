
# <center>**Food Aggregator and Delivery Analysis**</center>

## **Table of Contents**

**1.**  [**Introduction**](#Section1)<br>
**2.**  [**Problem Statement**](#Section2)<br>
**3.**  [**Installed & Imported Libraries**](#Section3)<br>
**4.**  [**Data Pre-processing Steps**](#Section4)<br>
**5.**  [**Insights from the EDA**](#Section5)<br>
<a name=Section1></a>

## **1. Introduction**

An Exploratory Data Analysis of a **Food Aggregator Dataset** has been performed and can be found [here](https://www.kaggle.com/shrutimehta/zomato-restaurants-data).

The dataset had a **seperate dataset** and a **country** data, so we combined the two files and uploaded it over [here](), which we used for further analysis.

The EDA Notebook can be found at [**`Food Aggregator and Delivery Analysis.ipynb`**]() 

<a  name = Section2></a>

## **2. Problem Statement**


- Foodazing, an India based food aggregator and online booking & delivery company has established a lot of presence across the globe.
<center><img  src="https://cdn2.iconfinder.com/data/icons/valentine-day-16/512/599_dinner_food_BBQ_love_valentine_valentine_valentines_day_love-512.png"  width=50%></center>
- On their 10 year anniversary, they want to release an analysis to the public about their global presence and wants to thank their collaborators.

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
- **nltk.flatten**: To perform a flatten operation in the notebook.

<a  name = Section4></a>

## **4. Data Pre-processing Steps**

<a  name = Section41></a>

### **4.1 Dataset Description**:

<center>

|Dataset| Records | Features | Dataset Size |
| :--: | :--: | :--: | :--: |
| Food Aggregator and Delivery Analysis | 9551 | 21 | 2.15 MB |

<br>

|ID|Feature name|Feature description|
|:--|:--|:--|
|1|**Restaurant ID**|Identification Number |
|2|**Restaurant Name**| Name Of the Restaurant|
|3|**Country Code**| Country identification|
|4|**City**| City name|
|5|**Address**|Address |
|6|**Locality**| Locality name|
|7|**Locality Verbose**|Long Address of the Restaurant |
|8|**Longitude**| Longitude|
|9|**Latitude**| Latitude|
|10|**Cuisines**|Types Of Cuisines Served |
|11|**Average Cost for two**| Average Cost if two people visit the Restaurant|
|12|**Currency**|Currency of the country where restaurant is |
|13|**Has Table booking**| Can we book tables in Restaurant? Yes/No|
|14|**Has Online delivery**| Can we have online delivery ? Yes/No|
|15|**Is delivering now**|Is the Restaurant delivering food now? Yes/No |
|16|**Switch to order menu**|Switch to order menu ? Yes/ No |
|17|**Price range**|Categorized price between 1 -4 |
|18|**Aggregate rating**|Categorizing ratings between 1-5 |
|19|**Rating color**| Different colors representing Customer Rating|
|20|**Rating text**| Different Rating like Excellent, Very Good ,Good, Avg., Poor, Not Rated|
|21|**Votes**|No.Of Votes received by restaurant from customers. |

</center>

### **4.2 Data Cleaning**

- In this section, we will perform the **cleaning** operations on the data using information from the previous section.

- We will simply **drop the 9 rows** with **missing cells**.

- There is an additional file that consists of **country names**  **corresponding** to a specific **country code**. We will **merge** this file with the original dataset.
<a name=Section5></a>

## **5. Insights from the EDA**

<center><img  src="https://i.pinimg.com/originals/1b/9c/5e/1b9c5edf895e27b842ce49c73d48a385.gif"  width=50%></center>

- Most of the Restaurants are from India (8156), followed by USA.

- Out of the 9000 restaurants, **more than 1800** are **Not Rated**.

- Most of the restaurants have Aggregate rating ranging **between 3.0 to 4.0**.

- There are **144 unique cuisines** across all the restaurants.

- **8340 restaurants** with less than **500 votes**.

- **Toit** has the **highest amount of customer votes** - 10,934 votes.

- **North Indian, Chinese, Indian, Fast Food, South Indian, Mughlai, Mithai, Street Food, Bakery, Deserts**, and **Italian** are the popular cuisines in India

- **Cafe Coffee Day, McDonald's, Domino's Pizza, Subway, Baskin Robbins, Keventers, Pizza Hut, Barbeque Nation, Green Chick Chop**, and **Haldiram's** have a lot of chains across India.

- Most of the Indian restaurants are **based in New Delhi** and its surrounding areas.

- A lot of New Delhi based restaurants are present in many localities like **Connaught Place, Aerocity, Barakhamba Road**, and **Janpath**.

- **Mumbai, Kolkata**, and **Bangalore** each **have 20 outlets** with Foodazing.

- Foodazing is established in **14 countries outside India**.

- **USA** has **highest number** of the restaurants outside India with **425 restaurants**, followed by the **UK with 80 restaurants**.

- **American, Burger, Seafood, Indian, Chinese, Cafe, Italian, Mexican**, and **Breakfast** are some of the most preferred **cuisines outside India**.
