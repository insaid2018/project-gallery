
# <center>**Aviation Accident Analysis**</center>

## **Table of Contents**

**1.**  [**Introduction**](#Section1)
**2.**  [**Problem Statement**](#Section2)
**3.**  [**Installed & Imported Libraries**](#Section3)
**4.**  [**Data Pre-processing Steps**](#Section4)
**5.**  [**Insights from the EDA**](#Section5)

<a id=Section1></a>

## **1. Introduction**

- **FIFA** (Fédération Internationale de Football Association) is a non-profit organization that describes itself as an international governing body of **association football**, **futsal**, and **beach soccer**

- The actual dataset can be found [**here**](https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset)

<center><img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/FIFA_logo_without_slogan.svg/1200px-FIFA_logo_without_slogan.svg.png"  width=50%></center>

- It is the **highest governing body** of **association football**.

- The EDA Notebook can be found at [**`FIFA Player Analysis.ipynb`**]() 

<a  name = Section2></a>

## **2. Problem Statement**

- A game developer, in association with FIFA, wants to **analyze the attributes of players** for their upcoming game.

- They plan on introducing a **Team Creation System**, that allows players to use player's virtual characters in a customized team.

- But there are **many attributes** that make a great player, not to forget **goalkeepers** and **non-goalkeepers** have an entirely **different set** of attributes.

- Comparing **more than 18000 players** manually **over 100+ attributes** can be tedius and time-consuming.

<center><img  src="https://www.conceptdraw.com/How-To-Guide/picture/soccer-football-formation/Sport-Soccer-Football-Formation-3-2-5-WM.png"  width=70%></center>

- The developer has reached out to you - a data scientist to perform a **general analysis** and easily detemine which attributes should they consider for player selections.

- **Before diving deeper**, it is necessary to lay out a **upper-level analysis** of some of the **commonly interpreted attributes**, which is the **primary goal** of this case study.

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

<a  name = Section4></a>

## **4. Data Pre-processing Steps**

<a  name = Section41></a>

### **4.1 Dataset Description**:

<center>

|Dataset| Records | Features | Dataset Size |
| :--: | :--: | :--: | :--: |
| **FIFA Player Analysis** | 18944 | 106 | 9.43 MB |



</center>

### **4.2 Data Cleaning**

- In this section, we will actually create some new features and simplify some other features for our analysis.

- Firstly, we will rename ***some*** column names according to our requirements.

- Further, we will only use the first mentioned positions of the player in the player_position feature. For example: **Lionel Messi** plays **RW, ST, CF**. But we will only **extract and use RW (Right Wing)** since it is his primary position.

- Also, we will **assign a fuzzy position name** to the extracted position. This wil be helpful to **compare and judge similar players**. The following table shows the conversion:

| Actual Position | Converted Position |
| :--: | :--: |
| ST, CF | ST |
| LW, RW, LM, RM | WF |
| CAM, CDM, CM | CM |
| LWB, RWB, LB, RB | WB |
| CB | CB |
| GK | GK |

<a name=Section5></a>

## **5. Insights from the EDA**

<center><img  src="https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/35674/business-man-good-idea-clipart-xl.png" width=30%></center>

- We had to limit ourselves to a **lesser number of features** to carry out the analysis.

- The **skillsets** had to be **generalized** to make our analysis easier.

- **Paris Saint-Germain's**  **Kylian Mbappé Lottin** is the **highest valued player** (and Striker) in FIFA with **105.5M Euros**, followed by the **Neymar Jr.** with **90M Euros** and **Kevin De Bruyne** with **87M Euros**.

- Messi is the highest rated player in the FIFA records.

- Both players - Messi and Ronaldo have almost similar attributes - with **Messi** excelling at **passing** and **Ronaldo** excelling at **pacing**.

- **CB**, **ST**, **CM**, and **GK** have **significant proportions** as compared to the rest of the positions.


- **Pacing**, **Shooting** and **Defending** are some of the most important attributes for a non-GK player as we observed that these attributes have higher values in distribution for players.

- Similarly, **Reflexes, Diving** and **Positioning** are **essential for a goalkeeper** in a match.

- There are **681 unique clubs** identified in this dataset.

- **FC Bayern Munchen** holds the top spot in **average rating of teams**, followed by **Real Madrid**, **Chelsea**, **FC Barcelona**, and **Liverpool**.

- The **median age** of players in a club seem to be **24 years**, with an **age gap** as **wide as 23 years** between eldest and youngest players.

- European countries like **UK, France**, and **Germany**, along with **Brazil** and **Argentina** have produced a significant number of international footballers.


<!--stackedit_data:
eyJoaXN0b3J5IjpbODc0NDA2MjAyXX0=
-->