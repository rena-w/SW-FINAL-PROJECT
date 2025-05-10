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
>This repository contains the main files I used for my final project, representative of where I did the most work. This includes the original data downloaded from the corpus in a pristine, untouched state, the cleaned data that I used for statistical testing and analysis, and other data files that were created to help me work with the data. I also included the Python script containing the code used during this project and the functions I wrote for the purpose of exploring the data further. Finally, there is also the edit history that shows my progress on this project, as well as the different directions I took along the way.

---
---

# DATA
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

This is an entry from my final, *fully cleaned* dataset as an example:

    ('US NEWS', 'Million Americans Roll Sleeves Omicron Targeted COVID Boosters', 8, 6.875)

Some fun statistics I found along the way:

**Most common words**: 'Trump', 'new', 'Donald', 'says', 'day', 'best', 'Trumps'/'Trump's', 'make', 'one', 'us'/'U.S.'

**Most common WCs** (before cleaning): 10 words, 11 words, 9 words, 12 words, 8 words, 7 words, 13 words, 6 words, 14 words, 5 words

**Most common WCs** (after cleaning): 7 words, 8 words, 6 words, 5 words, 4 words, 9 words, 3 words, 10 words, 2 words, 11 words

**Most common CLs**: 5 letters, 4 letters, 6 letters, 7 letters, 8 letters, 3 letters, 9 letters, 10 letters, 11 letters, 2 letters

**The longest word:** 'selenofriggatriskaidekaphobics' (30 letters, appears one time)

---
---

# METHODOLOGY 
*This is one of the most important sections. A scientific paper should provide enough information that another scientist would be able to replicate the results. You don't have to cover every single detail of how your code is implemented, etc, but you should minimally describe any processing you apply to the data, as well as the specific statistical tests you use. This section should also formalize your hypotheses. If you decide to create a Github repository (see extra-credit section), you may cite portions of the code where appropriate.*

In this section, I will cover the process of cleaning the data, processing it, and my reasoning for each decision. I will also briefly describe the code used to format, organize, and sort the data for usage. Finally, I will discuss the different statistical tests I used and the purpose of each test. 

Unfortunately, something was wrong with the formatting of the original data, so I had to convert it into text and reformat the dataset before I could do anything else. Each entry was already on its own line, so the initial challenge was separating the items within each individual entry. I also had to make sure they were all in the same order, since the original dataset seemed to be inconsistent with the order of their variables. I really underestimated the amount of issues I would run into as I continued to work with the headlines — especially because I just had so much of them to account for — so the code I wrote kept getting longer and more complicated.

### **Working with the text**
Once I got the entries separated, my focus then turned to the lexical content of each headline. The other variables were less important — for example, other than the recategorization I mentioned earlier, the `category` column didn't need to be changed very much. 

Predictably, getting an accurate measure of CL was what drove the vast majority of these changes. My plan for character length was to calculate it by counting the number of alphabetic characters in each word, then finding the overall average of all the words in the entire headline. This would then repeat for every entry. The function `findCL()`, the partner to `findWC()`, used `len()` at first, but in order to safeguard against any symbols or non-alphabetic letters that my `clean()` function failed to catch, was altered to use repeated list iterations instead.

    for word in headline:
        count = 0
        for char in word: 
            if char.isalpha():
                count += 1
            entry_count.append(count)
        avg = average(entry_count)

**Items I removed and why they were problematic:**
1. **Punctuation** and other **non-alphanumeric characters**

    This includes things like commas, periods, ellipses, apostrophes, and any other character that isn't an alphabetic letter. These would have interfered with the counting of CL, incorrectly yielding a higher count. 
    
    The function `get_lines()` retrieves data from an original *.txt* data file and iterates through its contents to return a list of all entries without unwanted characters. Punctuation, other symbols, and unicode were removed in the first step of the whole process using RegEx patterns to identify and replace them.

2. **Hashtags**

    Hashtags such as #MeToo or #BlackLivesMatter were also common occurrences. Although hashtags are often made up of several words in sequence, since there are deliberately no spaces used, it is meant to be read and treated as one single word (+=1 in word count). Like punctuation, these items would result in an incorrect CL. This comes at the risk of having a lower WC. 
    
    I really wanted to try and keep them in the data, so I attempted to work around them at first. Even though they aren't technically *words*, they do still convey a lot of information. I was also concerned that removing hashtags would change the structure of shorter headlines (WC-wise) too much. Although I had some ideas and I tried a few already, it turned out to be harder to keep the hashtags than to take them out. 

3. Items that consisted of only **numeric digits**
    
    To find the number of words in each headline, the first version of the `findWC()` function used the construction `wc = len(headline)`, just phrased in a way that allowed for different types of inputs to be processed successfully. `findWC()` returned a single value: a count of all the items within a list. 
    
    However, if you look at news headlines, you will find that numbers or values are never written out as words, but these items will be counted as words regardless. This would affect both the WC and the CL values, meaning that the easiest solution was to just remove them.

---

## **Testing**
To address the guiding questions I had for this project I conducted my statistical testing in two parts:

**Part 1**: tests comparing **each category** (between samples).

**Part 2**: tests comparing between **the standard** (made from population data) and **sample data** (from each category).

### Part 1: ANOVA & POST-HOC
The independent variable for this part was `category`. The samples from each category were guaranteed to be independent — each article can only be assigned to one category. Although I did do follow-up testing with Welch's ANOVA just to double-check, it probably wasn't necessary.

#### ANOVA

With ANOVA, the aim was to look at the average character lengths of each category in comparison to each other. The one-way ANOVA was conducted using `formula = CL ~ CATEGORY`, with `category` as the distributing variable. There were 30 levels of the independent variable corresponding to the 30 different categories, which was a lot of groups. The number of levels made it pretty difficult to conduct analysis between specific groups, even when the number of groups was lowered.

**Null hypothesis:** the average word length in characters is the same across all 30 categories of news articles.

H0: `average_CL('POLITICS') = average_CL('ENTERTAINMENT & MEDIA') = average_CL('ENVIRONMENT') = ... = average_CL('PARENTING')`

**Alternative hypothesis:** the average word length in characters is not the same across all 30 categories; at least one category average is significantly different.

HA: `*NOT*(average_CL('POLITICS') = average_CL('ENTERTAINMENT & MEDIA') = average_CL('ENVIRONMENT') = ... = average_CL('PARENTING'))`

#### Post-hoc tests
For post-hoc testing, my first instinct was to use many Student's t-tests. However, as mentioned above, there are many, many levels. False positives are essentially guaranteed, even if I lowered the number of tests to 10 different samples against each other. I did manually conduct individual t-tests with the top 10 categories, but like I said, the results are likely not accurate. 

The post-hoc test method I decided to use for this project is Tukey's test, which is specifically designed to be a follow-up to ANOVA. It compares the means of every possible combination of two groups while accomodating for any familywise errors. With 30 levels, that would mean a ridiculous number of comparisons (1,073,741,823), but it also means that a test like Tukey's test is the only option, since a t-test would result in an unimaginable amount of false positives. I conducted my Tukey test with the top 10 categories.

**Null hypothesis:** There is no significant difference between any of the groups; all the means are equal.

H0: `average_CL('POLITICS') = average_CL('ENTERTAINMENT & MEDIA') = average_CL('ENVIRONMENT') = ... = average_CL('PARENTING')`

**Alternative hypotheses:** For all combinations, the alternative hypothesis is that the means of the two groups being compared is significantly different.

HA: `average_CL('POLITICS') - average_CL('ENTERTAINMENT & MEDIA') != 0` (for example)

### Part 2: Comparison with a standard
Earlier in my planning process for this project, I wanted to look at the data from news headlines in comparison to other forms of prose. However, it ultimately was too wide of a scope and a little too ambitious for the scale of this project. I still wanted to do similar testing, so I decided to stay within-genre and compare a population standard to the samples. 

The first group of tests compare the sample averages to a population average — these are one-sample t-tests. The second tests assess if the probability of a particular outcome is equal to the population probability across all categories, or chi-square goodness-of-fit tests. 

#### Defining the standard
There are two groups of words that were collected from the cleaned headlines: the *set* of **UNIQUE** words and the *list* of **ALL** words. As reported by the summary statistics above, there are 1,343,496 total words and 57,116 unique words in this dataset. The average CL calculated from each of those groups is significantly different: the average CL of unique words is 7.379 letters, and the average CL of all words is nearly 1.5 characters shorter, at 5.975 letters. 

I chose to define the population standard using the list of **all** words, referred to from now on as `all_words`, since it clearly is the better demonstration of the distribution of word lengths across the entire population. Therefore, for Part 2 of testing, the established standard is **an average CL of 5.975 letters**.

The five number summary of `all_words` is as follows:
**MIN** 2 **Q1** 4 **MED** 6 **Q3** 7 **MAX** 30
with an IQR of 3. Using the typical formula of 1.5\*IQR, that puts the upper and lower bounds at 11.5 and -0.5 letters respectively. Since we are only interested in long words, the upper bound is the relevant value. Finally, we arrive at the section where the words 'Long Word' appear — the calculated upper bound of the population CL gives us our definition. A 'long word', therefore, is **any word that has a CL > 11**. With these population values set, we now move on to explaining the tests.

#### Sample average vs. population average — one-sample t-testing
Using a one-sample t-test to compare each category against the population standard is the simplest way to do so. Unlike the previous part, however, since we are still using only the top 10 categories as our samples, there are only 10 tests to conduct.  

**Null hypothesis:** for all 10 t-tests, the null hypothesis states that the average CL is equal to the population average of 5.975.

H0: `average_CL('POLITICS') = average_CL(population)`

**Alternative hypothesis:** for all 10 t-tests, the alternative is a two tailed 'not equal' prediction, since we have no information about which way a test will go. That gives us information about *if* there's a difference or not, but not any information about which way it goes.

HA: `'average_CL('POLITICS') != average_CL(population)`

If we have a test yielding a p-value that allows us to reject the null hypothesis, we can then conduct a second t-test, where the alternative hypothesis is that the sample mean is either greater than or lesser than the population mean. 

HA 2.0: `'average_CL('POLITICS') > average_CL(population)`
    OR
     `'average_CL('POLITICS') < average_C(population)`

#### Testing goodness-of-fit
In order to see if the standards of long words are equal across the board, I chose to use the chi-square goodness-of-fit test to compare the distributions of the population to each category's sample. 

**Null hypothesis:**
**Alternative hypothesis:**

# RESULTS
*A practice I follow is to have a separate "results" and "analysis" section. For results, you should describe the outcomes of your statistical without any "editorializing". I.e. describe the results as objectively as possible, without saying what you think those results mean. This is where you should state p-values and other direct results of your statistical tests. This is also where you should say if the Null hypothesis is rejected or maintained.*

## Part 1 results
### ANOVA 

### Tukey's Test


## Part 2 results


# ANALYSIS
*This is where you can go into more detail about what the results mean, and what significance they hold in relation to the subject area and the question you set out to answer.*

### **Potential sources of error / things that could be improved**
During the cleaning process, there were many different items that I felt I needed to account for. One of these seemed particularly pressing: names. Because of the nature of news articles, proper nouns are much more likely to appear. In fact, the words 'Trump' and 'Donald' are #1 and #3 in the top 10 most common words, with 10,585 and 4,835 instances respectively. Although it could just be reflective of when these headlines were written, it still seems reasonable to assume that the appearance of proper nouns is influencing the average word count and character lengths. 

# CONCLUSION
*This can be fairly short. Briefly re-state the high-level takeaways from your project, as well as a few ideas of how the research direction could be continued/improved in future work.*