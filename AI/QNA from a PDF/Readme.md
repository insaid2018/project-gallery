

<center><h2><b>Question Answer generation from the given PDF</b></h2></center>

## **Table of Contents**

1. [**Project Description**](#Section1)<br>
2. [**Approach towards the problem**](#Section3)<br>
3. [**Limitations**](#Section4)<br>
4. [**Libraries Used**](#Section4)<br>
5. [**Summary**](#Section5)<br>
6. [**Applications**](#Section5)<br>
7. [**References**](#Section6)<br>

<center><img  src="https://i.pinimg.com/originals/6b/6e/6a/6b6e6ad625caf5cfe546a67a2f545231.gif"  height= 450  width=800  ></center>

<br>

<a name=Section1></a>
# **1. Project Description**

- **Natural Language Processing** in **Artificial Intelligence** is the application of computational techniques to the analysis and synthesis of natural language and speech.

- The company is facing major issues when it comes to **genarating questions and answers from any text book.**

- For a hypothetical scenario it has been assumed one is working as a **freelance data scientist** in a  edu-tech start-up. 

- The major challenge is that this is a **very time consuming process** and needs a **bulk amount of manpower**

- Hence, they want to **automate this entire process** so that **no manual processing is needed.**

-  The goal of this project is to develop an **automatic question answering** system.

- This file should be able to take a **pdf book as an input** and return **best possible question(s)-answers** related to that book.


- The prime **Business Constraint** is to deliver **Quality** in terms of making this case study.

<br>


<a name=Section3></a>
# **2. Approach towards the problem**

- The approach in this case study was to make a machine learning model that can **genarate questions and answers** from a **given pdf book.**

- Initially, libraries were installed and upgraded.

- Followed by that it was found that the data could be extracted from **7 pages**

-   The pagecount includes the **cover page , the index and the acknowledgements** as well

  
- After  **data acquistition** a <b> <a href="https://github.com/patil-suraj/question_generation">_pre-trained model_</a></b> was used.

### Additional Approach:

- After fitting the model to the extracted data two common issues were being faced that has been successfully tackeled in this project:-

- It  was seen that when the model was not being able to genarate the answer to a question it would throw **Value Error** and when faced an empty string it would face **Assertion Error**

- These error(s) were successfully tackled using the **classical value error and assertion error techniques** specific to the above mentioned use cases.

- After tackling the raised issues we were successfully able to tackle down the problem and **genarate question-answer pairs for a given text corpus that has been extracted from a pdf book of 7 pages.**

# 3. Limitation(s)   
   - Post fine tuning this model fails to work for large scale data because of its  <a href="https://github.com/patil-suraj/question_generation">architecture</a> the time and space complexcities for the model is huge and hence, a good amount processing time and resource requirement is there.

   

# **4. Libraries Used**

Following are the list of **libraries** that were used for making this project.

- **PyPDF2** was used in order to make extract the text corpus from a given pdf book.  
- **numpy** was used in order to calcucate numercal operations.
- **pandas** was used to make the dataframes, profiling and processing the data.
- **Pyplot** was used to render out vizualizations in order to draw insights.
-  **Scikit Learn** was used to split the data into training and testing datasets.
<br>

<a name=Section5></a>
# **5. Summary**
- In this project we were able to successfully make a question answering system with the help of **transformers** and a **pre trained custom made pipeline**.

  

- We tested this model over a **7 paged pdf book of SQL**.

  

- We then checked if this can perform good for any test datapoint.

  

- Post that we saw that the model was throwing **value error and assertion error as exception(s)** when they didn't meet the specific use cases.

  

- These exceptions were tackled down by using, **value error and assertion error try catch exception handling technique(s)**

  

- Though the model predicts good quality **questions and answers** , this model is limited to work on large files

  

- As the file size increases so does the **computational time and space complexcities** which can be a major challenge in the near future

<a name=Section6></a>
# **6. Applications**

- This project can be used to genarate **questions and answers** to train chatbots like **RASA NLU**  

- For schools and colleges we can use this project in order to make **question banks and test papers**

- If tuned further and trained properly in large data this project can be used for **Open-domain Question Answering (ODQA)**



<a name=Section6></a>
# **7. References**

- **Transformers architecture**: https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)#:~:text=in%20successive%20layers.-,Architecture,thing%20to%20the%20encoder's%20output.
- **Scikit Learn**: https://scikit-learn.org/stable/
- **Github :** https://github.com/patil-suraj/question_generation


