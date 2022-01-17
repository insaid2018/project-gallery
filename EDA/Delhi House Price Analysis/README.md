
# <center>**Delhi House Price Analysis**</center>

## **Table of Contents**

**1.**  [**Introduction**](#Section1)<br>
**2.**  [**Problem Statement**](#Section2)<br>
**3.**  [**Installed & Imported Libraries**](#Section3)<br>
**4.**  [**Data Pre-processing Steps**](#Section4)<br>
**5.**  [**Insights from the EDA**](#Section5)

<a name=Section1></a>

## **1. Introduction**

- **NewBricks Pvt Ltd** is a website that provides a common platform for **property buyers** & **sellers** to locate properties of interest in India, and source information about all property related issues.

<center><img  src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fclipground.com%2Fimages%2Fcoloured-houses-clipart-5.jpg&f=1&nofb=1"  width=50%></center>

- Apart from buying, **selling** & **renting properties in India**, users have access to guides that cover all the essential steps and stages entailed in property buying.

  

- They also provide a **tool** which empowers **property seekers** and **investors** with detailed information on the **movement** of **residential apartment prices** and **supply of properties**.

<a  name = Section2></a>

## **2. Problem Statement**

- Recently, they have been seeing a **surge** in **number of listings** on their website.

- They want to leverage this **opportunity** and **determine** the **relation of prices** of listed housing properties with various factors.

 <center><img  src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.pngmart.com%2Ffiles%2F3%2FStock-Market-PNG-Clipart.png&f=1&nofb=1" width=30%></center>

- They have hired you - a data analyst to perform the analysis on houses that have been listed in and near Delhi.  

- Your job is to determine which **factors** result in **price fluctuations** of houses in Delhi.

<a  name = Section3></a>

## **3. Installed & Imported Libraries**

<a  name = Section31></a>

### **3.1 Installed Libraries**

- For starters, we installed the `pandas_profiling` library which gives a quick, general overview of the dataset.

<a  name = Section32></a>

### **3.2 Imported Libraries**

The following libraries have been imported in the notebook:
<center><img  src="https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/187550926/original/cde47296f9d02346b6561eee753741d7272bfce6/do-data-analysis-in-python-using-numpy-pandas-matplotlib-seaborn.jpg"  width=50%></center>

- **Pandas**: Importing for panel data analysis
- **Pandas Profiling**: To perform data profiling
- **Numpy**: For numerical python operations
- **Matplotlib (Pyplot)**: A popular plotting library used along with pandas
- **Seaborn**: A library, built on matplotlib, to create beautiful plots

<a  name = Section4></a>

## **4. Data Pre-processing Steps**

<a  name = Section41></a>

### **4.1 Dataset Description**:

<center>

|Dataset| Records | Features | Dataset Size |
| :--: | :--: | :--: | :--: |
| Delhi House Price Data | 1259 | 11 | 153 KB |

</center>

### **4.2 Data Cleaning**

- In this section, we will actually create some new features and simplify some other features for our analysis.

- We have removed **86 redundant rows** from the dataset.

  

- We have missing values in **5 features**.

  

- We have filled the missing values in **Furnishing**, **Parking** and **Type** with **mode**, **Bathroom** and **Per_Sqft** with the mean of the features.

<a name=Section5></a>

## **5. Insights from the EDA**

- We need a more clean dataset, specially the one which has precise and accurate information.

  

- We also need data from **secondary sources** that describe more about the **locality**, the **age** of house being listed, the **neighborhood area**.

  

- Knowing about the **type of neighborhood** like **residential** or **industrial** will also be helpful to determine if it affects the price of houses.

 
- **Price** is **highly related** to **Bathroom**, **Area, BHK** and, **Per_Sqft**.

  

- But we can also observe that **building floors** are more **expensive** than **apartments**.

  

- We can use this lot of information to **predict the prices of houses**, although **locality** is an **important factor** and we need more information on that.

  

- The company can use **this information** and **extrapolate** some of the observations throughout the country's listings.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcxMDk0OTI3OV19
-->
