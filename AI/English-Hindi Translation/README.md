<br>
<h2><b>English to Hindi Translation using Encoders and Decoders</b></h2>
<br>

## **Table of Contents**

1. [**Project Description**](#Section1)<br>
2. [**Dataset Description**](#Section2)<br>
3. [**Approach towards the problem**](#Section3)<br>
4. [**Libraries Used**](#Section4)<br>
5. [**Summary**](#Section5)<br>
6. [**References**](#Section6)<br>

<center><img src="https://www.techrounder.com/wp-content/uploads/2020/11/english-hindi-translation.jpg" height= 400 width=1000 ></center>

<br>

<a name=Section1></a>
# **1. Project Description**

- **Natural Language Processing** in **Artificial Intelligence** is the application of computational techniques to the analysis and synthesis of natural language and speech.

- In this project the objective is **to deliver the hindi translation of the english text** that has been given in the <a href="https://www.kaggle.com/aiswaryaramachandran/hindienglish-corpora">dataset</a>.

- For a hypothetical scenario it has been assumed one is working as a **NLP Engineer** in a technical start-up who have onboarded this project from one of their clients.

- The objective is to deliver the **Best fit model** as per the project deliverables are concerned.

- The prime **Business Constraint** is to deliver **Quality** in terms of making this case study.

- The evaluation metric for this problem statement is set as **Accuracy.**

<br>

<a name=Section2></a>
# **2. Dataset Description**

- The following is the description of the entire dataset. For reference you can visit <a href="https://www.kaggle.com/aiswaryaramachandran/hindienglish-corpora">**here**</a>. 

<br>

| Records | Features | Dataset Size | 
| :-- | :-- | :-- | 
| 127607 | 3 | 41.4 MB|  

<br>

|**Serial**|**Name of the Feature**|**Description**|
| :-- | :-- | :-- |
|1|Source| Three types of sources are there ted, tides and indic2012|
|2|english_sentence| Sentences in english|
|3|hindi_sentence| translation of hindi formed from sentences in english|

<br>

<a name=Section3></a>
# **3. Approach towards the problem**

- The approach in this case study was to make a machine learning model that can **predict the hindi words translation** from a **given english sentence.**

- Initially, libraries were installed and upgraded.

- Followed by that it was found that the dataset has  
  - **50,000 source** datapoints **tides** categorized as **tides**.
  - **39,881 source** datapoints **tides** categorized as **ted**.
  - **37,726 source** datapoints **tides** categorized as **indic2012**
  
- It was found that in the dataset 2 values were missing from the **english_sentence** feature which was encountered by treating with **Logical NOT**.

- Then through **exploratory data analysis** it was found that 
  - Most of the datapoints have have **<50 words**.
  - Sentences with **word count>=100** are very less and hencem they can be avoided.
  - The **highest length** of an **hindi sentence** is found under the class name **indic2012** for **source**.
  - The **lowest length** of a hindi sentence is found under the class name **ted** for **source**.
  - Hence, only **ted** was for the **source**. 
  
- After that certain data post processing operations were performed such as **genarating new features**, **feature encoding** and **feature extraction**

- After that the **encoder-decoder architecture** was defined keeping **latent_dim =300**.
<br>
 <center><img src="https://github.com/ghoshpronay18071997/english_to_hindi_with_encoder_decoder/blob/main/Encoder_decoder_architecture.png" height= 400 width=800 ></center>
 <br>
 
 - In the architecture one **embedding encoder layer** was defined followed by an **encoder lstm** layer.
 
 - The final dense layer was made of output shape **(None,None,17541)**.
 
 - The total **trainable parameters** were found to be **16,193,541**.
 
 <br>
 <center><img src="https://github.com/ghoshpronay18071997/english_to_hindi_with_encoder_decoder/blob/main/Encoder_decoder_loss.png" height= 400 width=800 ></center>
 <br>

- After that the model was trained on **30 epochs** and a batch size of **128** and on the final validation loss we recived a loss of **2.74**

- After that the **decoder layer** was made which would **take up the encoded sequence as the input and decode the sentence as output.**


- After that **predictions** were made for a given datapoint. Example of a prediction is as shown in the following figure.
 
 <br>
  
 <center><img src="https://github.com/ghoshpronay18071997/english_to_hindi_with_encoder_decoder/blob/main/Encoder_decoder_output_new.jpg" height= 154 width=568></center>
 
 <br>

<a name=Section4></a>
# **4. Libraries Used**

Following are the list of **libraries** that were used for making this project.

- **Tensorflow** and **Keras** were used in order to make the model architecture, training and testing.  
- **numpy** was used in order to calcucate numercal operations.
- **pandas** was used to make the dataframes, profiling and processing the data.
- **Pyplot** was used to render out vizualizations in order to draw insights.
-  **Scikit Learn** was used to split the data into training and testing datasets.
<br>

<a name=Section5></a>
# **5. Summary**

- We had successfully built this **encoder-decoder** model that can convert **english text to hindi text.**

- As the **number of epochs increase** so does the **accuracy** and hence, **loss gets reduced.**

- This model was trained on **30 epochs**, however, training this model with more number of epochs can bring up better results.

- Future scope of work would be to apply **transformer layer** on top of encoder-decoder architecture and hence, it is expected that it will return **lesser training loss**.

<a name=Section6></a>
# **6. References**

- **Keras:** https://keras.io/
- **Tensorflow**: https://www.tensorflow.org/
- **Encoder Decoder architecture**: https://machinelearningmastery.com/encoder-decoder-recurrent-neural-network-models-neural-machine-translation/#:~:text=An%20Encoder%2DDecoder%20architecture%20was,of%20sequence%20token%20was%20reached.
- **Scikit Learn**: https://scikit-learn.org/stable/
- **Kaggle**: https://www.kaggle.com/aiswaryaramachandran/english-to-hindi-neural-machine-translation


