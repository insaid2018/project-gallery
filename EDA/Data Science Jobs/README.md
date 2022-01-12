
# <center>**Data Science Jobs**</center>

## **Table of Contents**

**1.**  [**Introduction**](#Section1)
**2.**  [**Problem Statement**](#Section2)
**3.**  [**Installed & Imported Libraries**](#Section3)
**4.**  [**Data Description**](#Section4)
**5.**  [**Insights from the EDA**](#Section5)

<a name=Section1></a>

## **1. Introduction**

- GlassHut is a website where current and former employees **anonymously review** companies. GlassHut also allows users to anonymously **submit and view salaries** as well as search and apply for jobs on its platform.

<center><img  src="https://analyticsindiamag.com/wp-content/uploads/2020/06/data-science-job-titles.png"  width=50%></center>

<a  name = Section2></a>

## **2. Problem Statement**

-  **The Analyst Excel**  is a newly organized MNC works in the field of data analysis.
-  They want to  **analyze**  and  **compare**  the number of  **Data Science Jobs**  over a period of time.
<center><img  src="https://c4f2d3i3.stackpathcdn.com/gb/wp-content/uploads/sites/17/2021/03/insights.png"  width=50%></center>

 -    To do so, they have hired your company - a data analytics firm.
- You are required to perform exploratory data analysis and come with great insights.

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

<a  name = Section4></a>

## **4. Data Description **

<a  name = Section41></a>

<center>

|Dataset| Records | Features | 
| :--: | :--: | :--: | :--: |
| Data Science Jobs | 742 | 41 |

<br>

|ID|Feature name|Feature description|
|:--|:--|:--|
|1|**Job Title**| Designation of Job|
|2|**Salary Estimate**| Salary in dollars |
|3|**Job Description**| Job details |
|4|**Rating**| Rating for job |
|5|**Company Name**|Name of company |
|6|**Location**| Location of job |
|7|**Headquarters**| HQ  of company |
|8|**Size**| Size of company|
|9|**Founded**| Date of founding |
|10|**Type of ownership**| Private/Public |
|11|**Industry**|Type of company  |
|12|**Sector**| Field of work |
|13|**Revenue**| Revenue |
|14|**Competitors**| Yes or No |
|15|**Hourly**| Tells us if the salary reported was hourly or yearly. 1: Hourly, 0: not hourly. |
|16|**Employer provided**| 1: If the salary was provided by the employee of the company, 0: otherwise. |
|17|**Lower Salary**| Lower salary range |
|18|**Upper Salary**| Upper salary range |
|19|**Avg Salary(K)**| Avg salary range|
|20|**company_txt**| Name of company |
|21|**Job Location**| Location of job |
|22|**Multiple skill columns (python, spark, aws, excel etc)**| 1: Skill is required by the company, 0: It is not required.|
|23|**Jobtitle_sim**| It contains the title of the job like Data scientist, ML engineer etc. |
|24|**Seniority_by_title**| Senority of the position, it is extracted from the Job Title. |
|25|**Degree**|If the job description mention that the company gives experience credit for a master(M) or Ph.D degree(P). |



</center>


<a name=Section5></a>

## **5. Insights from the EDA**

<center><img  src="https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/35674/business-man-good-idea-clipart-xl.png" width=30%></center>

- **California** has the most number of jobs

- **Maryland** has the lowest average annual salary because it is hiring less number of people and the jobs are also distributed among high salary and low salary job titles.

- Both **California and Illinois** has almost the same average minimal annual salary.

- **Biotech & Pharmaceuticals**  Industry has maximum number of jobs followed by Insurance carriers.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg5NzA2OTAxMl19
-->