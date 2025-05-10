# LING 250 — Final Project
### TOPIC: Word length in news headlines
#### *by Serena Wong*
---

### INTRODUCTION
News headlines are meant to be eye-catching — they must convey a lot of information in a very short span of time. By the time a reader has scanned an article's title, they need to know the main points of an entire article from a single line of words. Effectively, every word must matter. An author needs to consider 'How much information does this word carry? Is there a better choice?' and other similar questions when coming up with a headline. I investigated one specific aspect that may have some bearing on how writers choose to title their articles: word length in characters. Longer words naturally take more time to read — your eye needs to move farther across the page, or in the case of this dataset, across the screen. Visually, on a graphic design-level, longer words take up more space and leave less room for the rest of the headline. This project investigates the structure of headlines of online news articles, breaking them down into their word counts and the lengths of the words in them. 


**Why?** -- In an age where short-form media is preferred and novel content is constantly being generated, I think it is good to take a moment and consider how and what knowledge is being shared to the public. Looking into the statistical patterns behind headlines could reveal a lot about the way information spreads, what kinds of information are prioritized, and how that is controlled. While there may not be any intent, malicious or benevolent, behind the way headlines frame a story, it is still valuable to notice the patterns of behavior that repeat themselves in media. In my opinion, it is particularly important for us as the readers and the target audience to be aware of the factors contributing to our perception and understanding of new information. 

#### Guiding questions:
- Is there a difference in average length of words (in characters) between different categories/genres of articles?
- What is considered a 'long word' in the context of news headlines?
- Do writers avoid using long words in their titles? 
- Are long words more likely to appear in particular categories of articles? Why?
- Does the word count of a headline have an impact on the length of words within it? (i.e., if a headline has more words, are those less likely to be long words because the headline itself is already long?)


**In this repository:**
> ---
>This repository contains the files I used for my final project: the original data, cleaned data that was used for statistical testing and analysis, and the code I wrote that processed my data. 

---
---

# Data
The corpus I used for this project was created by Rishabh Misra and Jigyasa Grover. Consisting of 210,294 entries, the main part of the data is the collection of news article headlines, but the corpus also contains information about the author(s) of the article, the publication date, and the category under which the article falls. Each entry also provides the links to the articles, as well as a short description of the content of each article. 

This corpus was compiled between the years of 2012 and 2022 (though the vast majority of the data were collected in 2012 to 2018) from Huffpost’s archiving feature, so all the articles were written by Huffpost authors. 

The first entry of the data, as an example:
        
    {"link": "https://www.huffpost.com/entry/covid-boosters-uptake-us_n_632d719ee4b087fae6feaac9", "headline": "Over 4 Million Americans Roll Up Sleeves For Omicron-Targeted COVID Boosters", "category": "U.S. NEWS", "short_description": "Health experts said it is too early to predict whether demand would match up with the 171 million doses of the new boosters the USA ordered for the fall.", "authors": "Carla K. Johnson, AP", "date": "2022-09-23"}

>Misra, Rishabh. "News Category Dataset." arXiv preprint arXiv:2209.11429 (2022).

>Misra, Rishabh and Jigyasa Grover. "Sculpting Data for ML: The first act of Machine Learning." ISBN 9798585463570 (2021).

---

## Summary of data

From the original 210,294 entries, I started with 209,518 entries in my dataset. I then went through and manually removed those that were blank, had no category, or were unusable for various reasons. The whole cleaning process took a long time and a lot of code (which you can look at in the [other files](https://github.com/rena-w/SW-FINAL-PROJECT/blob/main/1finalproject.py) in this repository), since there were specific conditions I wanted to control for. A detailed explanation of my cleaning process can be found in the next section of this write-up. 

**About summary statistics**: I will stick to summarizing the dataset as a whole here and leave the discussion of individual categories for later sections. After the data was fully cleaned, I collected relevant quantities and statistics to summarize the different aspects of all the headlines I looked at.

**Basic stats:**

>Number of raw headlines: 209,518
    
>**Total** number of entries: 209,518 entries
    
>Number of **useable** entries: 208,085 entries

### About variables
In its raw form, my data had the same 6 columns as the original dataset. However, I really only used 2 out of the 6: the category and the headlines themselves. After processing it, I ended up with 4 columns, listed in the order they appear (left-to-right) in the data table: the **category**, the **headline**, and two of my own variables, **word count** and **character length**. 

**Category** — the genre of each article 

**Article headline** (often shortened to HL) — the text of the title of each article

**Word count** (WC) — the number of items\* in a headline. 
(\*not all the items were words)

**Character length** (CL) - the average length (in alphabetic characters) of a word in a headline. 

This is an entry from my final, *fully cleaned* dataset:

    ('US NEWS', 'Million Americans Roll Sleeves Omicron Targeted COVID Boosters', 8, 6.875)

**Statistics, continued:**

>Number of words **before cleaning** (total word count): 2,033,105 words

>Number of words **after cleaning** (cleaned word count): 1,343,496 words  

>Number of **unique words**: 57,116 words

**Word count (WC):**

>Average WC of headlines **before cleaning**: 9.704 words per headline

>Average WC of headlines **after cleaning**: 6.412 words per headline

**Character length** (calculated with *clean* data only):

>Average CL of **all words**: 5.975 letters

>Average CL of **unique words**: 7.379 letters

---

### About categories
The creators of the corpus had 41 categories in the original dataset. To cut down on the number of groups, I combined labels that seemed to be for the same type of content (i.e., "ARTS", "ARTS & CULTURE", and "CULTURE & ARTS") into one category, ending up with 30 categories. The top 10 categories are listed below, along with the number of articles that belong to each category. 

|Category|# of articles|
|:--- | :--- |
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

The full list of categories and their respective counts can be found in [category_count.txt](https://github.com/rena-w/SW-FINAL-PROJECT/blob/main/category_count.txt)!

---

Below are some fun statistics I found along the way:

**Top 10s** (in descending order):

>Most common **words**: 'Trump', 'new', 'Donald', 'says', 'day', 'best', 'Trumps'/'Trump's', 'make', 'one', 'us'/'U.S.'

>Most common **WCs** (before cleaning): 10 words, 11 words, 9 words, 12 words, 8 words, 7 words, 13 words, 6 words, 14 words, 5 words

>Most common **WCs** (after cleaning): 7 words, 8 words, 6 words, 5 words, 4 words, 9 words, 3 words, 10 words, 2 words, 11 words

>Most common **CLs**: 5 letters, 4 letters, 6 letters, 7 letters, 8 letters, 3 letters, 9 letters, 10 letters, 11 letters, 2 letters

**The longest word:** 'selenofriggatriskaidekaphobics' (30 letters, appears one time)

---
---

# Methodology 
*This is one of the most important sections. A scientific paper should provide enough information that another scientist would be able to replicate the results. You don't have to cover every single detail of how your code is implemented, etc, but you should minimally describe any processing you apply to the data, as well as the specific statistical tests you use. This section should also formalize your hypotheses. If you decide to create a Github repository (see extra-credit section), you may cite portions of the code where appropriate.*

In this section, I will cover the process of cleaning the data, processing it, and my reasoning for each decision. I will also discuss the different statistical tests I decided to use for the analytic part of this project. 

---
## **The cleanup process!**

Unfortunately, something was wrong with the formatting of the original data, so I had to convert it into text and reformat the dataset before I could do anything else. Each entry was already on its ownline, so the initial challenge was separating the items within each individual entry. I also had to make sure they were all in the same order, since the original dataset seemed to be inconsistent with the order of their variables. 

Once I got the entries separated, my focus then turned to the lexical content of each headline and if I needed to change anything. I really underestimated the amount of issues I would run into as I continued to work with the headlines — especially because I just had so much of them to account for — so the code I wrote kept getting longer and more complicated.

### **Working with the text**

**Items I removed and why they were problematic:**
1. **Punctuation** and other **non-alphanumeric characters**
2. hashtags — treated as one single word (+=1 in word count) but ignored for character count, since hashtags are often several words in sequence with no spaces
    - this results in an incorrect judgement — it would indicate that there are LWs in that entry when there aren't (false positive)
3. Items that consisted of only numeric digits
    - when counting words, the input was the entire entry. I first replaced all instances of digits


### Finding variables
As described above, the dataset has four variables, with the first two (category and the headline itself) being categorical and the latter two (word count and character length) being quantitative.

**Category** — the genre of news for each article
- Other than the recategorization I mentioned earlier, this column didn't need to be changed very much. 

**Word count** (WC) — the number of items* in a headline. 

- The code used in the function `findWC` was basically `wc = len(headline)`, just phrased in a way that allowed for different types of inputs to be processed successfully.

**Character length** (CL) - the average length (in alphabetic characters) of a word in a headline. 

    for word in headline:
        count = 0
        for char in word: 
            if char.isalpha():
                count += 1
            entry_count.append(count)
        avg = average(entry_count)

Initially, the word count was simply the number of words in each headline. However, if you look at news headlines, you will find that numbers or values are never written out as words. Hashtags such as #MeToo or #BlackLivesMatter were also common occurrences, so I had to work around these non-standard items without impacting the rest of the structure of each title, or risking a skewed dataset if I removed too much of any headline.

My plan for character length was to calculate it by counting the number of alphabetic characters in each word, then finding the overall average of all the words in the entire headline. This would then repeat for every entry. 

#### **WC vs. CL**
- numbers are counted as their own words, but 


---

## **Testing**
I conducted my statistical testing in two parts:

**Part 1:** comparing each category (between samples)

**Part 2:** comparing between a standard and samples


### Part 1: ANOVA & POST-HOC
#### ANOVA

With ANOVA, the aim was to look at the average character lengths of each category in comparison to each other. The one-way ANOVA was conducted using `formula = CL ~ CATEGORY`, so there were 30 levels of the independent variable corresponding to the 30 different categories. 

**Null hypothesis:** the average word length in characters is the same across all 30 categories of news articles.

**Alternative hypothesis:** the average word length in characters is not the same across all 30 categories; at least one category average is significantly different.

#### Post-hoc tests
For post-hoc testing, my first instinct was to use many Student's t-tests. However, since I am testing the means of 10 different samples against each other, there would be a very high chance of a false positive. So, the post-hoc test method I used for this project is Tukey's test, which is specifically designed to be a follow-up to ANOVA. 

**Null hypotheses:**
**Alternative hypotheses:**

### Part 2: Comparison with a standard
Earlier in my planning process for this project, I wanted to look at the data from news headlines in comparison to other forms of prose. However, it ultimately was too wide of a scope and a little too ambitious for the scale of this project. I still wanted to do similar testing, so I decided to stay within-genre and compare a population standard to the samples.

#### Finding the standard

##### Determining outliers
- formula = Q1 - 3\*IQR, Q3 - 3\*IQR 
    - the increased threshold for outliers is due to the very small IQR found from the data

Rough average word count per CLEAN headline: 6.351774071917449

# Results
*A practice I follow is to have a separate "results" and "analysis" section. For results, you should describe the outcomes of your statistical without any "editorializing". I.e. describe the results as objectively as possible, without saying what you think those results mean. This is where you should state p-values and other direct results of your statistical tests. This is also where you should say if the Null hypothesis is rejected or maintained.*

## Part 1 results

## Part 2 results

# Analysis
*This is where you can go into more detail about what the results mean, and what significance they hold in relation to the subject area and the question you set out to answer.*

### **Potential sources of error / things that could be improved**
During the cleaning process, there were many different items that I felt I needed to account for. One of these seemed particularly pressing: names. Because of the nature of news articles, proper nouns are much more likely to appear. In fact, the words 'Trump' and 'Donald' are #1 and #3 in the top 10 most common words, with 10,585 and 4,835 instances respectively. Although it could just be reflective of when these headlines were written, it still seems reasonable to assume that the appearance of proper nouns is influencing the average word count and character lengths. 

# Conclusion
*This can be fairly short. Briefly re-state the high-level takeaways from your project, as well as a few ideas of how the research direction could be continued/improved in future work.*