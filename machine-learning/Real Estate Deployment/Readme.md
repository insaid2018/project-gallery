
# <center>**Real Estate Deployment**</center>

## **Table of Contents**

**1.**  [**Problem Statement**](#Section1) <br>

**2.**  [**Installed & Imported Libraries**](#Section2) <br>

**3.**  [**Data Pre-processing Steps**](#Section3)<br>

**4.**  [**Insights from the EDA**](#Section4)<br>

**5.**  [**Data Postprocessing**](#Section5)<br>

**6.**  [**Modelling, Hyperparameter Tuning and Prediciton**](#Section6)<br>

**7.**  [**Deployment**](#Section7)

**8.**  [**How to run this on your local host / system**](#Section8)<br>


<a  name=Section1></a>
---
# **1. Problem Statement:-**


  

- **ChennaiEstate** is a **real estate firm** based in **Chennai** that is involved in the property business for the past 5 years.

  

- Since, they are in the business for so long, they have enough data of all the real estate transactions in the city.

  

- They decided to venture into Analytics and have now started a division called **Chennai Estate Analytics** to give consumers as much information as possible about housings and the real estate market in Chennai.

  

- A home is often the largest and most expensive purchase a person makes in his or her lifetime. Ensuring real-estate owners have a trusted way to monitor the asset is incredibly important.

  

- Hence, they have hired you as a consultant to help them give insights and develop a model to accurately predict real estate prices.

  

- Based on the **train** dataset, you will need to develop a model that accurately predicts the real estate price in **Chennai**.

  

<center><img  src = "https://therealdeal.com/national/wp-content/uploads/2021/03/CoreLogic-Home-Price-Reports-Highest-Growth-Since-2013.gif"></center>

  

### **Scenario**

  

- You are given a dataset consisting of **required details**

  

- Your task is to build a **regression model** using the dataset

  

- Because there was **no machine learning model for this problem** in the company, you don’t have a quantifiable win condition. You need to build the best possible model

<a  name = Section2></a>

## **2. Installed & Imported Libraries**

<a  name = Section31></a>

### **2.1 Installed Libraries**

- For starters, we installed the `pandas_profiling` library which gives a quick, general overview of the dataset.
- Additionally, we have installed the `datascience` library that is required by pandas profiling library.

<a  name = Section32></a>
### **2.2 Imported Libraries**

The following libraries and tools were used for the project:
<center><img  src="https://cdn.analyticsvidhya.com/wp-content/uploads/2020/11/Untitled-design24.png"  width=80%></center>

- **Pandas**: Importing for panel data analysis
- **Pandas Profiling**: To perform data profiling
- **Numpy**: For numerical python operations
- **Matplotlib (Pyplot)**: A popular plotting library used along with pandas
- **Seaborn**: A library, built on matplotlib, to create beautiful plots
- **Scikit Learn**: To perform all tasks realted to Machine Learning
- **Flask** : To perform operations related to REST API
- **Pycharm:** The Runtime environment for development of app.py
- **html:** To make the **render templates**




<a  name = Section3></a>

## **3. Data Pre-processing Steps**

<a  name = Section41></a>

### **3.1 Dataset Description**:

<center>


- We have **7109 Samples**  and for each of sample **19 different** properties are recorded.

  
  

| **Column Name** | **Description** |
| ------------: |:------------|
|  INT_SQFT |  The interior Sq. Ft of the property
   | N_BEDROOM | The number of Bed rooms
   | N_BATHROOM | The number of bathrooms
   | N_ROOM | Total Number of Rooms
   | QS_ROOMS | The quality score assigned for rooms based on buyer reviews
   | QS_BATHROOM | The quality score assigned for bathroom based on buyer reviews
   | QS_BEDROOM | The quality score assigned for bedroom based on buyer reviews
  | QS_OVERALL | The Overall quality score assigned for the property
   | SALE_COND | The Sale Conditio|    | BUILDTYPE | The type of building |AREA | The property in which the real estate is located
   | DIST_MAINROAD | The distance of the property to the main road
   | PARK_FACIL | Whether parking facility is available
 |    UTILITY_AVAIL | What facilities are available | 
 |STREET| Kind of the Street|
 |MZzone|Zone of the area|
|  PRT_ID | The Property Transaction ID assigned by ChennaiEstate
  | COMMIS | The Commission paid to the agent
   | SALES_PRICE | The total sale price of the property
</center>


### Observations:
- There are total  **13 numerical data-type and 8 object type data files**  recorded.
-  The mean of the **SALES_PRICE** is found to be **10894909.63919**


### **3.2 Data Cleaning**

- In this section, we **cleaned out** our data based on the information retrieved from the previous observations.

- Hence, we performed the following subtasks.

- Checking for **missing values** and manipulating them.

- Checking the **datatype**.

- Checking the  **Spelling Correction**
<a name=Section4></a>

## **4. Insights from the EDA**

<center><img  src="https://cdn-images-1.medium.com/max/1000/1*Owa2rsDG6Rwv1IM_RdsL3A.gif"></center>

- The data was **successfully studied** and hence, the **insights** were **marked down** in order to make proper **business decisions**.

- The freq of **RL** is maximum for **MZZONE**

- **Paved** type streets has been reported maximum number of times.

- **UTILITY_AVAIL** has **AllPub** recorded the maximum number of times.
<a name=Section5></a>

## **5. Data Postprocessing**

- In this section we performed the **Data Encoding**.

- Then we further genarated a few **new features**.

- Next we performed **Data Extraction**.


<a name=Section6></a>
## **6. Modelling and Hyperparameter Tuning and Prediciton**
<center><img  src="https://cdn.dribbble.com/users/1571442/screenshots/6356637/dribbbble_machinelearning_4x.png"></center>

- We performed modelling with most of the commonlu used **Machine Learning** models.

-  As a **Baseline** it was found that **CatBoost Regressor** was giving us the highest **r2 score** and least **overfitting**.

- We further tuned the model with **RandomSearchCV** and found that we had a very low improvement of **0.005** in the **validation data**.

- However, still this was giiving the lowest overfitting on validation data. hence, we selected this model as the **best fit**.

- Finall , we made predicitoins with this model and found that this model was giving us an **r_2 score** of **0.99** on **unseen data** and was **generalising well**.


<a name=Section7></a>

## **7. Deployment**

- After finding the best fit we dropped the model as a **pickle file (.pkl file)**.

- Now we developed the **templates** in order to render the **form** that should take in inputs from the end user.

- Finally we connected the templates with the **app.py** file and embed the model in pickle format.

- Finally we were able to successfully make a **request** 
and get **response** through the app,py file.


<a name=Section8></a>
## **8. How to run this on your local host / system**

- Downlaod the complete repo into your local system and save it into the same **directory.**

- Install **PyCharm Community Edition** or any other **IDE** like **Spyder** into your local system and open **app.py** file in that **IDE**.

- After that run the code on the **app.py file** (If you're using Pycharm then then simply press **ctrl +F5** )

<center><img  src="https://github.com/ghoshpronay18071997/real_estate_deployed/blob/main/Photos%20for%20Deployment/Documentary.png"></center>

- Check the console you'll be getting a **link**.

- Clciking this link will open a new **browser** (typically the **default** one)

- Give in the values and click on **predict** button.

- You'll have the **results** in front of you.


