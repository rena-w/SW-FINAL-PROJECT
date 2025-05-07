# LING 250 — Final Project
### by Serena Wong for LING 250 — Spring 2025

##

### Topic: word choice in news headlines, dependent on word length in characters

## In this repository:
*Describe the contents of the repository.*

## Introduction
*Motivate your project by introducing the subject matter, the question you want to answer, and the motivation for answering that question*

## Data
*Overview of the data you've used for this project. This should be pretty close to your data statement milestone. This is also where to provide summary statistics of the data.*

- combined "ARTS", "ARTS & CULTURE", and "CULTURE & ARTS" into one category

#### **Determining outliers**
- formula = Q1 - 3*IQR, Q3 - 3*IQR 
    - the increased threshold for outliers is due to the very small IQR found from the data


## Methodology 
*This is one of the most important sections. A scientific paper should provide enough information that another scientist would be able to replicate the results. You don't have to cover every single detail of how your code is implemented, etc, but you should minimally describe any processing you apply to the data, as well as the specific statistical tests you use. This section should also formalize your hypotheses. If you decide to create a Github repository (see extra-credit section), you may cite portions of the code where appropriate.*

#### **Non-standard terms**
- hashtags — treated as one single word (+=1 in word count) but ignored for character count, since hashtags are often several words in sequence with no spaces
    - this results in an incorrect judgement — it would indicate that there are LWs in that entry when there aren't (false positive)
- numbers — treated as one single word
    - when counting words, the input was the entire entry. I first replaced all instances of digits

## Results
*A practice I follow is to have a separate "results" and "analysis" section. For results, you should describe the outcomes of your statistical without any "editorializing". I.e. describe the results as objectively as possible, without saying what you think those results mean. This is where you should state p-values and other direct results of your statistical tests. This is also where you should say if the Null hypothesis is rejected or maintained.*

## Analysis
*This is where you can go into more detail about what the results mean, and what significance they hold in relation to the subject area and the question you set out to answer.*

## Conclusion
*This can be fairly short. Briefly re-state the high-level takeaways from your project, as well as a few ideas of how the research direction could be continued/improved in future work.*