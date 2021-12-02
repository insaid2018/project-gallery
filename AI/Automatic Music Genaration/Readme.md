
<center><h2><b>Automatic Music Genaration</b></h2></center>

## **Table of Contents**

1. [**Project Description**](#Section1)<br>
2. [**Approach towards the problem**](#Section2)<br>
3. [**Limitations**](#Section3)<br>
4. [**Libraries Used**](#Section4)<br>
5. [**Summary**](#Section5)<br>
6. [**Applications**](#Section6)<br>
7. [**References**](#Section7)<br>

<center><img  src = "https://cdn.dribbble.com/users/316072/screenshots/10724786/laptop_music_animation_01_1600x1200.gif"></center>

<br>

<a id=Section1></a>
# **1. Project Description**

- **Natural Language Processing** in **Artificial Intelligence** is the application of computational techniques to the analysis and synthesis of natural language and speech.

- For a hypothetical scenario it was assumed that **ABC music prod. pvt.ltd** is a reknowned **audio-video production house** based out of **Mumbai, India**

- As **COVID-19** cases are increasing day by day it is almost impossible for the musicians to coop up with real time studio work.

- Hence, the company wants you to make an **AI based music genaration system.**

- The goal of this project is to make an **AI based music genaration system.**

- The key contraint to the problem is **accuracy.**

- You have been hired as a **freelance data scientist** for **ABC music prod. pvt.ltd**

- The model should read a text file in **abc format**.

- The model should genarate the **corresponding music** framed out of that note sequence.
<br>


<a id=Section2></a>
# **2. Approach towards the problem**

- The approach to this project was to make a **chat bot from scratch.**

- Initially all the necessary libraries were imported and installed.

- Then, the data corpus was formed. 

- A **data corpus** is a collection of linguistic data.

- Then while performing **preprocessing** we used lemmatization technique in order to process the data into desirable format. 

- Then after preprocessing, we genarated **various batches** to fit into the model.

- After that we build a **character  level RNN model** and trained the model for **100 epochs** with a  **batch size of 16** and a **sequence length of 64**

- For every 10 epochs the model would save the **updated weights** in the **main directory** 

- We received a validation accuracy of **92%**

- Now we genarated the **music code** which is nothing but the **predicted vocabulary**
 
- After that we went <a  href="https://www.abcjs.net/abcjs-editor.html">here</a> and we were successfully able to **genarate music.**  

<a id=Section3></a>
# 3. Limitation(s)   
- The only limitation of this model is that it is being trained with **very less data.**

- However, while getting trained on various intrument data this model can be further enhanced for **different instruments** as well.

- We have **trained this model for only 100 epochs**. As the **number of epochs increase** it is expected that the **accuracy of the model will increase**.
   
<a id=Section4></a>
# **4. Libraries Used**

Following are the list of **libraries** that were used for making this project.

- **Python** was used as the general purpose programming language 
- **Keras** was used to perform all **Deep Learning operation(s)** such as model bulding, compilation and training. 

- **numpy** was used in order to calculate numercal operations.


<a id=Section5></a>
# **5. Summary**
- In this project an **Automatic music genaration system** was made from scratch.

- Here, we recieved a **validation accuracy of 92%**

- This project can be widely used for **music production systems**

- The only limitation of this model is that it is being trained with **very less data.**

- However, while getting trained on various intrument data this model can be further enhanced for different instruments as well.

- This model can be used for in house **music production systems.**

- This can be widely used to automate **manual instruments.**

- This can be also used to make **automatic VST(virtual studio toolkit) plugins**
<a id=Section6></a>
# **6. Applications**

- This model can be used for in-house **music production systems.**

- This can be widely used to automate **manual instruments.**

- This can be also used to make **automatic VST(virtual studio toolkit) plugins**


<a id=Section7></a>
# **7. References**

- **python:** https://www.python.org/

-  **Keras:** https://www.python.org/

-  **Genarate Music here:** https://www.abcjs.net/abcjs-editor.html

- **TDS Blog:** https://towardsdatascience.com/music-generation-through-deep-neural-networks-21d7bd81496e

- **Music Composition using Recurrent Neural Networks:** https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1174/reports/2762076.pdf

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkwNjIzMDEwOSwtOTY5ODM1MzM5XX0=
-->
