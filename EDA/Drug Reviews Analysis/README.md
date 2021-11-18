
# <center>**Drugs' Reviews Analysis**</center>

## **Table of Contents**

**1.**  [**Introduction**](#Section1)
**2.**  [**Problem Statement**](#Section2)
**3.**  [**Installed & Imported Libraries**](#Section3)
**4.**  [**Data Pre-processing Steps**](#Section4)
**5.**  [**Insights from the EDA**](#Section5)

<a name=Section1></a>

## **1. Introduction**

An Exploratory Data Analysis of the **UCI ML Repository Drug Review Dataset** has been performed which can be found [here](https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29)

The dataset had a **seperate train** and **test set**, so we combined the two files and uploaded it over [here](), which we used for further analysis.

The EDA Notebook can be found at [**`EDA Drug Reviews Analysis.ipynb`**]() 

<a  name = Section2></a>

## **2. Problem Statement**

- **ABC Pvt Ltd** is a **consumer healthcare online store** that provides consumers with on-demand, home delivered access to a wide range of prescription, OTC pharmaceutical, and other consumer healthcare products.

- Over the recent years, they are seeing an increase in **number of sales** as well as **reviews** on their website and app.

<center><img  src="https://flyclipart.com/downloadpage/images/medicine-clipart-obat-34445.png/34445"  width=30%></center>

- They have hired you - a data scientist whose job is to go through a **dataset scraped** from their website.

- The dataset provides **patient reviews** on specific drugs along with related conditions and a **10-star patient rating system** reflecting overall patient satisfaction.

- A **general analysis** has been performed before deep diving into the sentiment analysis.

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
- **Zip**: To ease with opening zip files
- **WordCloud**: To create wordclouds

<a  name = Section4></a>

## **4. Data Pre-processing Steps**

<a  name = Section41></a>

### **4.1 Dataset Description**:

<center>

|Dataset Name| Records | Features | Dataset Size |
| :--: | :--: | :--: | :--: |
| Drugs' Reviews Analysis | 215063 | 7 | 39.8 MB |

<br>

|ID|Feature name|Feature description|
|:--|:--|:--|
|1|**uniqueID**| Patient Identifier |
|2|**drugName**| Name of the Drug |
|3|**condition**| Patient's condition for which the drug was bought |
|4|**review**| Review given by the patient |
|5|**rating**| Rating given by the patient |
|6|**date**| Date of the review |
|7|**usefulCount**| How many other patients found this patient's review useful?|

</center>

### **4.2 Data Cleaning**

- The  **cleaning**  operations on the data have been performed based on information from data **description**, **information**, and **profiling report**.
    
- The missing values in the **`condition`** feature have been  **replaced** with  **mode**  of the feature.
    
- Additionally, a  **new feature**, named as  **`Review_Sentiment`**  will be created  **based on the `rating`**  feature.
    
- Also, the **year**,  **month**, and  **day of the week**  of the reviews have been extracted from the **`date`** feature.

<a name=Section5></a>

## **5. Insights from the EDA**

<center><img  src="https://i.pinimg.com/originals/1b/9c/5e/1b9c5edf895e27b842ce49c73d48a385.gif"  width=50%></center>

- - We observed an **increasing trend** in number of reviews over the years.

- Medication for **Birth Control**, **Depression**, **Pain**, **Anxiety**, and **Acne** are reviewed (and certainly bought) the most on the website.

- **Levonorgestrel**, **Phentermine**, **Etonogestrel**, **Varenicline** , **Ethinyl estradiol & norethindrone** , and **Escitalopram** are some of the most bought drugs.

- **More than 50%** of the ratings given to the medicinal drugs are good (i.e. **rating = 8, 9, or 10**) .