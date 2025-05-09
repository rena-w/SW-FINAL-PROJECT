# LING 250 — Final Project
###### *by Serena Wong*

### Topic: word choice in news headlines, dependent on word length in characters

## In this repository:
*Describe the contents of the repository.*

## Introduction
*Motivate your project by introducing the subject matter, the question you want to answer, and the motivation for answering that question*

## Data
*Overview of the data you've used for this project. This should be pretty close to your data statement milestone. This is also where to provide summary statistics of the data.*

#### Cleaning data

At the start, I had 209,518 entries in my dataset. I went through and manually removed those that were blank, had no category, or were unusable for various reasons. I then 


#### Data table
The variables of interest are: 
- **Word count** (WC) — the number of items* in a headline 

            wc = len(headline) 
- **Character length** (CL) - the average length (in alphabetic characters) of a word in a headline. 

    - *This was calculated by counting the number of alphabetic characters in each word, then finding the overall average of all the words in the entire headline.*

        
            for word in headline:
                count = 0
                for char in word: 
                    if char.isalpha():
                        count += 1 
                entry_count.append(count)
            avg = average(entry_count)
            return avg

My tabled data is divided into six columns. Each entry contains the category of the article, followed by the original & cleaned versions of the headline, WC, and CL. 

The creators of the corpus had 41 categories in the original dataset. To cut down on the number of groups, I combined labels that seemed to be for the same type of content (i.e., "ARTS", "ARTS & CULTURE", and "CULTURE & ARTS") into one category, ending up with 30 categories. The top 10 most common are listed below, along with the number of articles that belong to each category. The full list of categories and their respective counts can be found in [categories.txt](https://github.com/rena-w/SW-FINAL-PROJECT/blob/main/categories.txt)!

|Category|# of articles|
| -------- | ------- |
|POLITICS|35600|
|HEALTH & WELLNESS|24639|
|ENTERTAINMENT & MEDIA|20305|
|PARENTING|12746|
|STYLE & BEAUTY|12068|
|TRAVEL|9900|
|WORLD NEWS|9541|
|FOOD & DRINK|8436|
|BUSINESS & ECONOMY|7747|
|QUEER VOICES|6346|

## Methodology 
*This is one of the most important sections. A scientific paper should provide enough information that another scientist would be able to replicate the results. You don't have to cover every single detail of how your code is implemented, etc, but you should minimally describe any processing you apply to the data, as well as the specific statistical tests you use. This section should also formalize your hypotheses. If you decide to create a Github repository (see extra-credit section), you may cite portions of the code where appropriate.*

#### **Cleaning the data**

**Items I removed and why they were problematic**
1. Numbers and non-alphabetic characters — even though you often see numbers in headlines, they don't count as words.

#### **Finding the standard**
Rough average word count per CLEAN headline: 6.351774071917449

#### **Non-standard terms**
- hashtags — treated as one single word (+=1 in word count) but ignored for character count, since hashtags are often several words in sequence with no spaces
    - this results in an incorrect judgement — it would indicate that there are LWs in that entry when there aren't (false positive)
- numbers — treated as one single word
    - when counting words, the input was the entire entry. I first replaced all instances of digits

#### **WC vs. CL**
- numbers are counted as their own words, but 

#### **Determining outliers**
- formula = Q1 - 3*IQR, Q3 - 3*IQR 
    - the increased threshold for outliers is due to the very small IQR found from the data

#### **Testing**
The statistical test I used for this part of the project was a one-way ANOVA test, with CATEGORY being the independent variable. 

#### **RESEARCH QUESTIONS**

- is there a difference in average length of words (in characters) between different categories/genres of articles?
    - are LWs more likely to appear in particular categories of articles? 
    - *discussion* = possible reasons why,
- does word count have an impact on the length of words? 
    - i.e., if a headline has more words, are those less likely to be LWs because the headline itself is already long?


## Results
*A practice I follow is to have a separate "results" and "analysis" section. For results, you should describe the outcomes of your statistical without any "editorializing". I.e. describe the results as objectively as possible, without saying what you think those results mean. This is where you should state p-values and other direct results of your statistical tests. This is also where you should say if the Null hypothesis is rejected or maintained.*

## Analysis
*This is where you can go into more detail about what the results mean, and what significance they hold in relation to the subject area and the question you set out to answer.*

## Conclusion
*This can be fairly short. Briefly re-state the high-level takeaways from your project, as well as a few ideas of how the research direction could be continued/improved in future work.*