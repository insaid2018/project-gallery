
# <center>**Wine Price Analysis**</center>

## **Table of Contents**

**1.**  [**Problem Statement**](#Section1)<br>
**2.**  [**Installed & Imported Libraries**](#Section2)<br>
**3.**  [**Data Pre-processing Steps**](#Section3)<br>
**4.**  [**Insights from the EDA**](#Section4)



<a  id=section1></a>

# **1. Problem Statement**


- **The Indian Wine Co.** is India’s most popular wine production company that serves nationwide in **500+ cities** using their digital platform.

  

- It was founded in **1997** and is a subsidiary of **The Great Wine Production Group**.

  

- It has access to **270 supermarkets** and **60 compact hypermarkets** all over India.

  

- Its main motive is to **offer innovative** and **quality wine** and **wine-based products** at **affordable prices** to customers.

  

- It targets an **entire cross-section** of customers through **Hypermarkets**.

  

- To provide the best price to its customers **The Indian Wine Co.** wants to **analyze** and **optimize** the cost of each product for each purchase.

  

<center><img  src="https://2.bp.blogspot.com/-wyiW6CdEYwE/WovLV9WIkfI/AAAAAAAAANM/v0kwVKbwLAAVuFXbwK-50Ktyy72Zo_thgCLcBGAs/s1600/934372-red-wine-wallpaper-2880x1800-hd.jpg"  width=50%></center>

## **2. Installed & Imported Libraries**

<a  name = Section31></a>

### **2.1 Installed Libraries**

- For starters, we installed the `pandas_profiling` library which gives a quick, general overview of the dataset.
- Additionally, we have installed the `datascience` library that is required by pandas profiling library.

<a  name = Section32></a>

### **2.2 Imported Libraries**

The following libraries have been imported in the notebook:
- **Pandas**: Importing for panel data analysis
- **Pandas Profiling**: To perform data profiling
- **Numpy**: For numerical python operations
- **Matplotlib (Pyplot)**: A popular plotting library used along with pandas
- **Seaborn**: A library, built on matplotlib, to create beautiful plots
- **Plotly**: To create interactive graphs


<a  name = Section4></a>

## **3. Data Pre-processing Steps**

<a  name = Section41></a>

### **3.1 Dataset Description**:

<center>


- We have **120744 training** samples and for each of sample **11 different** properties are recorded.

  
  

| **Column Names** | **Description** |
| ------------: |:------------|
|**Id** | Unique ID |
**country** | country name at which the wine is produced
**description** | The Description of the wine
**designation** | designation / label of the wine
**points** | points acquired by the wine
**province** | at which zone does this wine belongs to
**region_1** | The wine growing area in a province or state
**region_2** | Sometimes there are more specific regions specified within a wine growing area but this value can sometimes be blank
**variety** | The type of grapes used to make the wine
**winery** | The winery that made the wine
**price** | The price of the winery
</center>

<br>

### Observations about the Data:
- There are **3 numerical** and **8 categorical** values as per the **profile-report**.
- In **country** column **US** records the **highest frequency**.
- In **designation** column **Reserve** records the **highest frequency**
- The mean of **points** recorded in the dataset is **21**.
- There are **1026 distinct region_1** records recorded.
- For **region_1** the frequency of **Napa Valley** is recorded to be **meximum**.
- For **region_2** the frequency of **Central Coast** is recorded to be **meximum**.

### **3.2 Data Cleaning**

- In this section, we performed the **cleaning** operations on the data using information from the previous section.
- We saw that **price** had a **right-skewed distribution**.
- We  performed **log-transformation** to treat these outliers.
- Apart from that there were **no missing** and **duplicate values** found in the dataset.
<a name=Section5></a>

## **4. Insights from the EDA**

<center><img  src="https://cdn-images-1.medium.com/max/1000/1*Owa2rsDG6Rwv1IM_RdsL3A.gif"></center>

- The data was **successfully studied** and hence, the **insights** were **marked down** in order to make proper **business decisions**.
- **Cuyo** has the least **number of records** with **region_1**.
- **Montrachet** has the highest **number of records** with **all the designations**.
- **Cabernet Shiraz** has the highest **number of records** with **all the varieties**.
- **Clos du Mesnil** has the highest **price** amongst **all the designations**.
- **England** has the highest number of **price**.
- **England** has the highest number of **points**.
- **Cuyo** can be a very good target spot depending upon the data and it can be targetted as the prime production units.
- This how the company will save huge cost in production and maintenance.
- Eventually this will lead them to a good amount of profit.
- **Cabernet Shiraz** has the highest amount of demand in the marketspace.
- hence, the production for this winery is a must. The company should **multiply the production** for this **winery** based upon **best resources** and thus is expected to **gain tremendous** amount of **profit**.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4OTc3ODA0ODgsLTE2MTM2MTc2OTldfQ
==
-->
