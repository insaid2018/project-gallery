print(tf.__version__)
# <center>**COVID-19 Analysis**</center>

## **Table of Contents**

**1.**  [**Introduction**](#Section1)<br>
**2.**  [**Problem Statement**](#Section2)<br>
**3.**  [**Installed & Imported Libraries**](#Section3)<br>
**4.**  [**Data Pre-processing Steps**](#Section4)<br>
**5.**  [**Insights from the EDA**](#Section5)

<a id=Section1></a>

## **1. Introduction**

- Almost **a year after the vaccination programs started** globally, we decided to perform an analysis on the rate of various vaccination campaigns.

- The datasets that are used in this project are collected from [**Covid-19 Global Dataset**](https://www.kaggle.com/josephassaker/covid19-global-dataset) and [**COVID-19 World Vaccination Progress**](https://www.kaggle.com/gpreda/covid-world-vaccination-progress) which are updated on a daily basis.

- So whenever you run the notebooks after downloading the datasets from kaggle,  just run them once and you will get the **latest report** of the vaccination progress.

- The EDA Notebook can be found at [**`Covid-19 Analysis.ipynb`**]() 

<a  id = Section2></a>

## **2. Problem Statement**

- **F.E.A.S.T.** (Food, Emergency Aid, Shelter and Training) is a charity to help the homeless and underprivileged, established around the globe.

- They have **shelters** established across **various countries** where they provide **food**, **shelter**, and **workforce training** for homeless and jobless people.

<center><img  src="https://library.kissclipart.com/20181210/ktw/kissclipart-volunteer-hands-clipart-volunteering-non-profit-or-349928f96e9ae55e.png"  width=70%></center>

- Due to the covid-19 pandemic, they had to **stop their operations** and **shelters** to **aid the medical bodies** by providing their shelters.

- After the worst has passed, they plan on **resuming their operations**, but they want to determine which countries would be the right candidates to resume operations.

- To determine this, they have hired you - a data scientist - where you will analyze the global effects of pandemic and the vaccination progress across various countries.

- You have been provided with a dataset from **worldometer** and **WHO** which can be used for the required analysis.

<a  id = Section3></a>

## **3. Installed & Imported Libraries**

<a  id = Section31></a>

### **3.1 Installed Libraries**

- For starters, we installed the `pandas_profiling` library which gives a quick, general overview of the dataset.
- Additionally, we have installed the `datascience` library that is required by pandas profiling library.

<a  id = Section32></a>

### **3.2 Imported Libraries**

The following libraries have been imported in the notebook:
<center><img  src="https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/187550926/original/cde47296f9d02346b6561eee753741d7272bfce6/do-data-analysis-in-python-using-numpy-pandas-matplotlib-seaborn.jpg"  width=50%></center>

- **Pandas**: Importing for panel data analysis
- **Pandas Profiling**: To perform data profiling
- **Numpy**: For numerical python operations
- **Matplotlib (Pyplot)**: A popular plotting library used along with pandas
- **Seaborn**: A library, built on matplotlib, to create beautiful plots
- **Plotly**: To create interactive graphs

<a  id = Section4></a>

## **4. Data Pre-processing Steps**

<a  id = Section41></a>

### **4.1 Dataset Description**:

<center>

- worldometer_coronavirus_summary_data:

|Dataset| Records | Features | Dataset Size |
| :--: | :--: | :--: | :--: |
| worldometer_coronavirus_summary_data | 221 | 12 | 20 KB |

- worldometer_coronavirus_daily_data:

|Dataset| Records | Features | Dataset Size |
| :--: | :--: | :--: | :--: |
| worldometer_coronavirus_daily_data | 145221 | 7 | 6.87 MB |

- country_vaccinations:

|Dataset| Records | Features | Dataset Size |
| :--: | :--: | :--: | :--: |
| country_vaccinations | 61820 | 15 | 12.1 MB |

</center>

### **4.2 Data Cleaning**

- In this section, we will actually create some new features and simplify some other features for our analysis.

- We will first **standardize country names** between the vaccine and summary datasets.

- We will **combine** the **summary dataset** with a **subset of vaccine dataset**, based on **country** names since they both contain up-to-date cumulative data of the countries.

- Finally, we will **extract the date** based features from the daily cases dataset.

<a id=Section5></a>

## **5. Insights from the EDA**

- The above graphs shows how slowly but surely, the vaccines are being administered in increasingly large numbers each day.

- If we look carefully, we can also identify a slight downward trend in the number of new cases each day, as the vaccinations progress.

- We can also observe **decrease in death rate** due to covid-19, which is thanks to the **vaccination programs**.

<center><img src="https://media.istockphoto.com/vectors/corona-virus-covid19-vaccineinjection-vaccine-bottle-vector-vector-id1221655483?k=20&m=1221655483&s=612x612&w=0&h=fCKfOWuIb5JMVXP2OeMPFjruVIxGlECfomLhAR6Fezw=" width=50%></center>

- **South-Asian countries** seemed to have suffered the most, but they have recovered and are **getting immunized**.

- We have many combinations of vaccines used in **many countries**, which boosts the vaccination programs.

- A **predictive model** can help to determine whether the **future trend** will **increase of decrease** in terms of **number of cases**.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMwOTc4MDE0XX0=
-->
