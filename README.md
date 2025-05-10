# LING 250 — Final Project
###### *by Serena Wong*

### TOPIC: Word length in news headlines

>#### In this repository:
>This repository contains the files I used for my final project: the original, untouched data, the data I ended up analysing, and the code I wrote that processed and cleaned my data. 

## INTRODUCTION
News headlines are meant to be eye-catching — they must convey a lot of information in a very short span of time. By the time a reader has scanned an article's title, they need to know the main points of an entire article from a single line of words. Because these headlines need to be short, every single word matters. How much information does this word carry? Is there a better choice? With those questions in mind, I investigated another aspect that may have some bearing on how writers choose to title their articles: word length. Longer words naturally take more time to read — your eye needs to move farther. The main question is if writers avoid using long words in their titles. Further, are there genres of reporting that are more or less likely to have long words in their headlines, and does the content of each genre have an impact on the choice of words?

This project 

#### Research questions:
- Is there a difference in average length of words (in characters) between different categories/genres of articles?
- What is considered a 'long word' in the context of news headlines?
- Are  more likely to appear in particular categories of articles? Why?
- Does word count have an impact on the length of words? 
    - For example, if a headline has more words, are those less likely to be LWs because the headline itself is already long?

## Data
*Overview of the data you've used for this project. This should be pretty close to your data statement milestone. This is also where to provide summary statistics of the data.*

#### The corpus 
The corpus I used for this project was created by Rishabh Misra and Jigyasa Grover. Consisting of 210,294 entries, the main part of the data is the collection of news article headlines, but the corpus also contains information about the author(s) of the article, the publication date, and the category under which the article falls. Each entry also provides the links to the articles, as well as a short description of the content of each article. 

This corpus was compiled between the years of 2012 and 2022 from Huffpost’s archiving feature, so all the articles were written by Huffpost authors. The vast majority of the data points are from 2012 - May 2018. 

This is the first entry of the data, as an example:
        
    {"link": "https://www.huffpost.com/entry/covid-boosters-uptake-us_n_632d719ee4b087fae6feaac9", "headline": "Over 4 Million Americans Roll Up Sleeves For Omicron-Targeted COVID Boosters", "category": "U.S. NEWS", "short_description": "Health experts said it is too early to predict whether demand would match up with the 171 million doses of the new boosters the USA ordered for the fall.", "authors": "Carla K. Johnson, AP", "date": "2022-09-23"}

>Misra, Rishabh. "News Category Dataset." arXiv preprint arXiv:2209.11429 (2022).

>Misra, Rishabh and Jigyasa Grover. "Sculpting Data for ML: The first act of Machine Learning." ISBN 9798585463570 (2021).


#### Description of my data
I downloaded the data from the corpus as a .JSON file. Unfortunately, something was wrong with the formatting, and I had to convert it to text in order to work with it. 

From the original 210,294 entries, I began with 209,518 entries in my dataset. I then went through and manually removed those that were blank, had no category, or were unusable for various reasons. The cleaning process took a long time and a lot of code (which you can look at in the other files in this repository), since there were specific conditions I wanted to control for. A detailed explanation of my cleaning process can be found in the next section of this write-up. My data in its raw form had the same columns as the original dataset. After processing it, however, I had 4 columns: category, headline, word count, and character length. Ultimately, I ended up with 208,085 useable entries that I used for my statistical analysis.

##### About categories:
The creators of the corpus had 41 categories in the original dataset. To cut down on the number of groups, I combined labels that seemed to be for the same type of content (i.e., "ARTS", "ARTS & CULTURE", and "CULTURE & ARTS") into one category, ending up with 30 categories. The top 10 categories are listed below, along with the number of articles that belong to each category. 

The full list of categories and their respective counts can be found in [category_count.txt](https://github.com/rena-w/SW-FINAL-PROJECT/blob/main/category_count.txt)!

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

#### My variables
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

#### **CLEANING THE DATA**

**Items I removed and why they were problematic**
1. Punctuation and other non-alphanumeric characters
2. hashtags — treated as one single word (+=1 in word count) but ignored for character count, since hashtags are often several words in sequence with no spaces
    - this results in an incorrect judgement — it would indicate that there are LWs in that entry when there aren't (false positive)
3. Items that consisted of only numeric digits
    - when counting words, the input was the entire entry. I first replaced all instances of digits

#### **Finding the standard**
Rough average word count per CLEAN headline: 6.351774071917449

#### **WC vs. CL**
- numbers are counted as their own words, but 

#### **Determining outliers**
- formula = Q1 - 3*IQR, Q3 - 3*IQR 
    - the increased threshold for outliers is due to the very small IQR found from the data

#### **Testing**
I conducted two stages of statistical testing: 
1. one-way ANOVA and post-hoc testing
2. comparing between the standard and samples from each category



#### ANOVA & POST-HOC
##### ANOVA
The first test, the one-way ANOVA test, was conducted using formula = CL ~ CATEGORY. There were 30 levels of the independent variable. 

Null hypothesis: the average word length in characters is the same across all 30 categories of news articles.

Alternative hypothesis: the average word length in characters is not the same across all 30 categories; at least one category average is significantly different.



##### Post-hoc tests
For post-hoc testing, my first instinct was to use many Student's t-tests. However, since I am testing the means of 10 different samples against each other, there would be a very high chance of a false positive. So, the post-hoc test method I used for this project is Tukey's test, which is specifically designed to be a follow-up to ANOVA. 

Null hypotheses:
Alternative hypotheses:

#### **RESEARCH QUESTIONS**

## Results
*A practice I follow is to have a separate "results" and "analysis" section. For results, you should describe the outcomes of your statistical without any "editorializing". I.e. describe the results as objectively as possible, without saying what you think those results mean. This is where you should state p-values and other direct results of your statistical tests. This is also where you should say if the Null hypothesis is rejected or maintained.*

## Analysis
*This is where you can go into more detail about what the results mean, and what significance they hold in relation to the subject area and the question you set out to answer.*

## Conclusion
*This can be fairly short. Briefly re-state the high-level takeaways from your project, as well as a few ideas of how the research direction could be continued/improved in future work.*

#### **Potential sources of error / things that could be improved**
- 