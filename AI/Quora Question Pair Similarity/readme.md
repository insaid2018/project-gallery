
## Table of Contents

 - Requirements
 - Title
 - Motivation
 - Goal
 - Data
 - Credits
 ## 1. Requirements
 This project requires **Python** and the following Python libraries installed and the dataset:
 
 - Numpy
 - Pandas
 - matplotlib
 - scikit-learn
 - Dataset-https://www.kaggle.com/c/quora-question-pairs
 ## Title
 #### Quora Question Pairs
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/5/57/Quora_logo.svg)
 -   Quora is a place to **gain and share knowledge**—about anything. It’s a platform to ask questions and connect with people who contribute unique insights and quality answers. This empowers people to learn from each other and to better understand the world.
 ## Motivation
 ![enter image description here](https://www.surveylegend.com/wordpress/wp-content/uploads/2020/12/best-open-ended-questions.png)
 Over **100 million people visit Quora** every month, so it's no surprise that many people ask similarly worded questions. **Multiple questions with the same intent** can cause seekers to spend **more time finding the best answer** to their question, and make writers feel they need to answer multiple versions of the same question. Quora values canonical questions because they provide a better experience to active seekers and writers, and offer more value to both of these groups in the long term.
 ## Goal
 ![enter image description here](https://miro.medium.com/max/1400/1*13TmGydM208lZp3ixRqMYA.jpeg)
 The goal of this competition is to predict which of the **provided pairs of questions contain two questions with the same meaning**. The ground truth is the set of labels that have been supplied by human experts. The ground truth labels are inherently subjective, as the true meaning of sentences can never be known with certainty. Human labeling is also a 'noisy' process, and reasonable people will disagree. As a result, the ground truth labels on this dataset should be taken to be 'informed' but not 100% accurate, and may include incorrect labeling. We believe the labels, on the whole, to represent a reasonable consensus, but this may often not be true on a case by case basis for individual items in the dataset.

## Data
![enter image description here](https://i.ibb.co/68H3QSs/red.png)

-   **id**  - the id of a training set question pair
-   **qid1, qid2**  - unique ids of each question (only available in train.csv)
-   **question1, question2**  - the full text of each question
-   **is_duplicate**  - the target variable, set to 1 if question1 and question2 have essentially the same meaning, and 0 otherwise.
 


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg3NjU3NzQ1OV19
-->