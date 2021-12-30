
# <center>**French Second hand cars data**</center>

## **Table of Contents**

**1.**  [**Problem Statement**](#Section1)<br>
**2.**  [**Installed & Imported Libraries**](#Section2)<br>
**3.**  [**Data Pre-processing Steps**](#Section3)<br>
**4.**  [**Insights from the EDA**](#Section4)<br>
**5.**  [**Referencecs**](#Section5)


<a  id=section1></a>

# **1. Problem Statement**



- The **dataset** contains all the scraper ads from a **French websites** specializes in **uploading used car ads**.

  

- There are **ads** from **professionals** or **individuals**.

  

- There are **columns** which are only for **electric type** cars

  

- This is a **one-time T data set**.

  

- The fixed price cannot be representative of the real value of the vehicle because it is freely fixed

  
  

<center>

<img  src="https://c1.wallpaperflare.com/preview/185/408/881/car-french-citroen-classic.jpg"  width="800"  height="400">

</center>

  

### **Scenario:**

  

- You have been hired as a data analyst for the **French automobiles company**.

  

- You are supposed to perform **exploratory data analysis** on this **dataset** that has been given to you.

  

- In order to do that you are supposed to **read and understand** the dataset properly.

  

- You are expected to deliver the **actionable insights** from the **observations** that you'll make from the **entire dataset**.
## **2. Installed & Imported Libraries**

<a  name = Section31></a>

### **2.1 Installed Libraries**
<center><img  src="https://www.itronixsolutions.com/wp-content/uploads/2019/11/datascience.gif"  width=80%></center>

- For starters, we installed the `pandas_profiling` library which gives a quick, general overview of the dataset.
- Additionally, we have installed the `datascience` library that is required by pandas profiling library.

<a  name = Section32></a>

### **2.2 Imported Libraries**

The following libraries have been imported in the notebook:
<center><img  src="https://cdn.analyticsvidhya.com/wp-content/uploads/2020/11/Untitled-design24.png"  width=80%></center>

- **Pandas**: Importing for panel data analysis
- **Pandas Profiling**: To perform data profiling
- **Numpy**: For numerical python operations
- **Matplotlib (Pyplot)**: A popular plotting library used along with pandas
- **Seaborn**: A library, built on matplotlib, to create beautiful plots
- **Plotly**: To create interactive graphs


<a  name = Section4></a>

## **3. Data Pre-processing Steps**

<a  name = Section41></a>

<center><img  src="https://thethinkcloud.co/wp-content/uploads/2020/07/data-presentation.gif"  width=80%></center>


### **3.1 Dataset Description**:

<center>


- We have **918 samples** and for each of sample **12 different** properties are recorded.
 
| **Column Name** | **Description** |
| :------------: |:------------|
| publishedsince | date of first publication of the advertisement|
| carmodel | contains the make and model name of the car |
| price | price of the car |
| année | year of first registration |
| miseencirculation | date of first registration |
| contrôletechnique |the car requires a technical check |
| kilométragecompteur |Number of km the car has on the odometer |
| énergie |Car energy|
| boîtedevitesse |Gearbox type|
| couleurextérieure |Outside car color|
| nombredeportes |Car's number of door|
| nombredeplaces |Car's number of seats|
| garantie |How long the car is guaranted|
| premièremain(déclaratif) | Is the car first hand |
| nombredepropriétaires | number of previous owners |
| puissancefiscale | french metric of car power |
| puissancedin | car power |
| crit'air | french metric to assess assess pollution 1 good, 4 bad 
| émissionsdeco2 | CO2 emission |
| consommationmixte | Energy consumption per 100km |
| normeeuro | euro norm |
| options | An array of options availaible with the car |
| departement | french district |
| id | id of the add in the scraped website |
| waranty | warranty in months |
| vendeur | is the seller a professional one or an individual |
| vérifié&garanti | Energy consumption per 100km |
| rechargeable | only for electric car, is the car rechargeable |
| autonomiebatterie | autonomy of the battery |
| capacitébatterie | size of the battery |
| conso.batterie | battery consumption |
| couleurintérieure | Inside color of the car |
| puissancemoteur | power of electric engine |
| primeàlaconversion | eligibility to French government welfare |
| garantieconstructeur | is the car still under maker waranty |
| provenance | where the car come from |
| prixinclutlabatterie | is the price includes the battery |
| voltagebatterie | number of volts of the battery |
| ntensitébatterie | power of the battery |
| prixinclutlabatterie |is the price includes the battery |

### **Observations:**


- The average of all the records recorded for the feature **année** is recorded to be **2018**.

  

- The measures on an average differ at a rate of **4.91** from the mean of année.

  

- The average of all the records recorded for the feature **nombredeportes** is recorded to be **4.56** .

  

- The measures on an average differ at a rate of **0.94** from the mean of **nombredeportes.**

  

- The average of all the records recorded for the feature **nombredeplaces** is recorded to be **4.75** .

  

- The measures on an average differ at a rate of **0.877** from the mean of **nombredeplaces.**

  

- The average of all the records recorded for the feature **nombredepropriétaires** is recorded to be **1.5** .

- The measures on an average differ at a rate of **0.9** from the mean of **nombredepropriétaires.**

  

- The average of all the records recorded for the feature **crit'air** is recorded to be **1.5** .

### **3.2 Data Cleaning**

- In this section, we performed the **cleaning** operations on the data using information from the previous section.

- We saw there are **too many missing values** in the data.

- As we can see most of the datapoints from **vérifié&garanti** to **prixinclutlabatterie.1** are missing, we will simply **drop them**.

- We will also drop those features who have a **missing value % greater than 50%**.

- Hence, we will drop **nombredepropriétaires** as well.

- For the rest of the features we **treated** them  with **mean** and **mode replacement** for **numerical** and **categorical variables** respectively.

- We saw there were **no duplicate datapoints recorded** in the dataset(s).

<a name=Section5></a>
## **4. Insights from the EDA**

<center><img  src="https://www.grazitti.com/assets/2020/02/Analytics_amp_Data_Science.gif"></center>

- The data was **successfully studied** and hence, the **insights** were **marked down** in order to make proper **business decisions**.

  

- There are too many outliers in the **price** column and it is sensetive to outliers as well.

  

- **price** shows us a **right skewed distribution**.

  

- We can use **log transformation or box-cox transformation** to treat the **outliers**.

  

- There are too many outliers in the **annee** column and it is sensetive to outliers as well.

  

- **annee**shows us a **left skewed distribution**.

  

- We can use **log transformation or box-cox transformation** to treat the **outliers**

  

- We can see that the highest distribution is recorded in between the range of **10,000 to 20,000 in euros**.

  

- The highest **frequency count** recorded is **800**.

  

- This means that cars with price range **10,000 to 20,000 in euros** have the **highest count recorded.**

  

- The car model **PEUGEOT 3008 (2E GEN)** has the hishest counts recorded.

  

- The car model **HYUNDAI SANTA FE 4** has the **lowest counts recorded.**

  

- The modelname **PEUGEOT** has the **highest counts recorded.**

  

- The highest cars recorded are from the year **2019**.

  

- **Dissel type** of **car engines** are recorded with the **most number of records.**

  

- **blanc colours** are recorded with the **most number of records.**

  

- **7 seater cars** are having the **highest records in the dataset.**

  

- **1926 number of cars** are recorded with **5 doors** having the **most number of records.**

  

- **Door number** has the highest correlation with the **seat numbers.**

- For the dealers it is advised that they should buy and sell cars keeping the budget range in between **10K to 20K** euros.

  

- This is because the **demand for this price range** in between the consumers are **highest.**

  

- Apart from that they should keep in mind that the year of registration **should not be less than 2019.**

  

- This is because for **most of the 2nd hand cars**, most of the consumers demand **year of registration to be 2019.**

  

- They should more try to onboard **dissel type** of **car engines** as this type has the **highest demand.**

  

- Going with **7 seater cars** is a **good choice** but one needs to keep in mind with the **budget** and **the year of registration.**

<a name=Section5></a>
## **5. References**

- **Dataset Link:**  
You can get dataset by clicking [here](https://www.kaggle.com/spicemix/french-second-hand-car/code).
