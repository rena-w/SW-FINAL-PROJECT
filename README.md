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
In the first half of this section, I will cover the process of cleaning the data, processing it, and my reasoning for each decision. I will also briefly describe the code used to format, organize, and sort the data for usage. In the second half, I will discuss the different statistical tests I used and the purpose of each test and what it intends to find out about the data. 

## Part 1: Cleaning and sorting the data
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
4. **Stopwords**
    Stopwords are used so often in English, and it was heavily skewing my data due to the frequency of them showing up. These are words like 'the', 'you', 'a', 'to', 'is', etc. Using the nltk module, I used list iteration to comb through every headline and remove the words that were in the list of English stopwords.

For all of these changes, there is corresponding code in [1finalproject.py](). `clean()` is the function I wrote specifically to get rid of numbers and stopwords and `get_lines()`, the function I mentioned was the first step of the whole process every time I ran the script, was created to be responsible for getting rid of all abnormal non-alphanumeric characters. 

### Working with the numbers
However, once I had finished cleaning the headlines and the lexical data, I had to consider the conditions I'd need to set for my quantitative variables. Because this entire project relies on these values, especially the character length, I needed to ensure that the data in those columns were satisfactory as well. While the textual data did directly affect the numerical data, there were some oddities that looked fine on the lexical side, but proved to be troublesome in the numerical data. For example, there is an entry with the headline "From Here to There" in the category 'PARENTING'. I kept getting zeros when importing my CL data into R, and I couldn't figure out where they were coming from, since I couldn't find these zeros in the `categorized_headlines.txt` file or in any of my other data files. Eventually, I figured out the step where things were going wrong. The data was fine after going through `find_type()` and `make_pair()`, but once it went through `clean()` as part of the `make_entry()` step, the zeros appeared. The issue was I hadn't realized that there were quite a few entries where all the words were stopwords, and so that would return values of zero after all the items were removed. 

To combat the issue of having 1s and zeros in my dataset, I first created a search function `search()` to help me easily locate all entries where WC or CL was greater than, less than, or equal to a particular value. However, I decided that simply changing `findWC()` and `findCL()` would be easier, and `search()` was repurposed and expanded so that I could use it to find specific words, categories, WCs, and CLs across both cleaned and uncleaned data. This proved very useful when I needed to access entries of specific categories quickly. 

In summary, on the numbers side, I excluded all entries that ended up with a WC of less than 2, which effectively also made sure that all CLs of less than 2 would be removed as well. The smallest values that were used in my statistical analysis were WC=2, CL=2. My hope with these conditions was to minimize the pull of smaller numbers on the overall distributions, both population-wise and category-wise.

---

## Part 2: **Testing**
All of my statistic work was done with R, though the actual R script where I did my scratch work was not included in this repository (though it absolutely can be if requested!!). Under each test, I provide the code used to perform it, or an example if there were multiple tests, as is the case for several of them. To address the guiding questions I had for this project, I conducted my statistical testing for two specific questions:

1. tests comparing **each category** (between samples).

2. tests comparing between **the standard** (made from population data) and **sample data** (from each category).

### Comparing categories: ANOVA & post-hoc followups
The independent variable for this part was `category`. The samples from each category were guaranteed to be independent — each article can only be assigned to one category. Although I did do follow-up testing with Welch's ANOVA just to double-check, it probably wasn't necessary.

#### ANOVA
With ANOVA, the aim was to look at the average character lengths of each category in comparison to each other. The one-way ANOVA was conducted using `formula = CL ~ CATEGORY`, with `category` as the distributing variable. There were 30 levels of the independent variable corresponding to the 30 different categories, which was a lot of groups. The number of levels made it pretty difficult to conduct analysis between specific groups, even when the number of groups was lowered.

**Null hypothesis:** the average word length in characters is the same across all 30 categories of news articles.

H0: `average_CL('POLITICS') = average_CL('ENTERTAINMENT & MEDIA') = average_CL('ENVIRONMENT') = ... = average_CL('PARENTING')`

**Alternative hypothesis:** the average word length in characters is not the same across all 30 categories; at least one category average is significantly different.

HA: `*NOT*(average_CL('POLITICS') = average_CL('ENTERTAINMENT & MEDIA') = average_CL('ENVIRONMENT') = ... = average_CL('PARENTING'))`

**Code used for testing:** `cl_aov=aov(formula=cl~category, data=entries)`

#### Post-hoc tests
For post-hoc testing, my first instinct was to use many Student's t-tests. However, as mentioned above, there are many, many levels. False positives are essentially guaranteed, even if I lowered the number of tests to 10 different samples against each other. I did manually conduct individual t-tests with the top 10 categories, but like I said, the results are likely not accurate. 

The post-hoc test method I decided to use for this project is Tukey's test, which is specifically designed to be a follow-up to ANOVA. It compares the means of every possible combination of two groups while accomodating for any familywise errors. With 30 levels, that would mean a ridiculous number of comparisons (1,073,741,823), but it also means that a test like Tukey's test is the only option, since a t-test would result in an unimaginable amount of false positives. I conducted my Tukey test with the top 10 categories.

**Null hypothesis:** There is no significant difference between any of the groups; all the means are equal.

H0: `average_CL('POLITICS') = average_CL('ENTERTAINMENT & MEDIA') = average_CL('ENVIRONMENT') = ... = average_CL('PARENTING')`

**Alternative hypotheses:** For all combinations, the alternative hypothesis is that the means of the two groups being compared is significantly different.

HA: `average_CL('POLITICS') - average_CL('ENTERTAINMENT & MEDIA') != 0` (for example)

**Code used for testing:** `post_test <- TukeyHSD(topten_aov, conf.level = 0.95)`

---

### Comparison with a standard: one-sample t-tests and chi-square tests
Earlier in my planning process for this project, I wanted to look at the data from news headlines in comparison to other forms of prose. However, it ultimately was too wide of a scope and a little too ambitious for the scale of this project. I still wanted to do similar testing, so I decided to stay within-genre and compare a population standard to the samples. 

The first group of tests compare the sample averages to a population average: these are the one-sample t-tests. The second tests assess if the probability of a particular outcome is equal to the population probability across all categories — chi-square goodness-of-fit tests. 

#### Defining the standard
There are two groups of words that were collected from the cleaned headlines: the *set* of **UNIQUE** words and the *list* of **ALL** words. As reported by the summary statistics above, there are 1,343,496 total words and 57,116 unique words in this dataset. The average CL calculated from each of those groups is significantly different: the average CL of unique words is 7.379 letters, and the average CL of all words is nearly 1.5 characters shorter, at 5.975 letters. 

I chose to define the population standard using the list of **all** words, referred to from now on as `all_words`, since it clearly is the better demonstration of the distribution of word lengths across the entire population. Therefore, for Part 2 of testing, the established standard is **an average CL of 5.975 letters**.

The five number summary of `all_words` is as follows:
**MIN** 2 **Q1** 4 **MED** 6 **Q3** 7 **MAX** 30
with an IQR of 3. Using the typical formula of 1.5\*IQR, that puts the upper and lower bounds at 11 and -0.5 letters respectively. Since we are only interested in long words, the upper bound is the relevant value. Finally, we arrive at the section where the words 'Long Word' appear — the calculated upper bound of the population CL gives us our definition. A 'long word', therefore, is **any word that has a CL > 11**. With these population values set, we now move on to explaining the tests.

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

**Code used for testing:** `t.test(x=pol_cl, mu=5.975, alternative="two.sided")`

#### Testing goodness-of-fit
In order to see if the standards of long words are equal across the board, I chose to use the chi-square goodness-of-fit test to compare the distributions of the population to each category's sample. Because CL is a quantitative variable, I converted it into a categorical one by binning the data in R: `pop_CL$len <- cut(pop_CL$V1, breaks=c(0.5, 4, 11, Inf), labels=c('short', 'med', 'long'))`. This gave me the expected proportions of: 27.7% short words, 70.7% medium words, and 1.5% long words.

**Null hypothesis:** for each chi-square test, the frequency distribution of CLs of each category is the same as that of the population. In otherwords, CLs occur in the same proportions in both the population and the sample.

H0: `proportion(words(population)) = proportion(words(insert_category))`

**Alternative hypothesis:** for each chi-square test, the proportions of CLs is not the same between the population distribution and the sample distribution. 

HA: `proportion(words(population)) != proportion(words(insert_category))`

**Code used for testing:** `chisq.test(expected_proportions, sample_proportions)`

# RESULTS

## Part 1 results
For all tests, I used the typical significance level of 0.05.

### ANOVA 

Using `formula = CL ~ CATEGORY`, the results of ANOVA are statistically significant. 
F-value: 162.6
p-value: 0.0000000000000002
Since p-value is much smaller than our significance level of 0.05, we **reject** the null hypothesis and conclude that there is significant evidence to suggest that average word length in characters is not the same across all 30 categories.

### Tukey's Test

I performed Tukey's Test as a response to the statistically significant results of ANOVA using `post_test <- TukeyHSD(topten_aov, conf.level = 0.95)`. This test compared the top 10 categories, with 45 unique pairings, looking to see if there was a significant difference between the means of each pair. 

The [results of the test](https://github.com/rena-w/SW-FINAL-PROJECT/blob/main/tukey_results.txt) showed that the majority of comparisons were statistically significant: 

- 37 out of 45 pairings had a **p-value of less than 0.05**, so the null hypothesis was successfully rejected in the majority of comparisons. 

The 8 pairings that had a **p-value greater than 0.05** and ***failed*** to reject the null hypothesis are listed below, in order from largest p-value to smallest:
|Category 1|Category 2|p-value|
|:---|:---|:---|
|PARENTING|ENTERTAINMENT & MEDIA|0.9966326|
|FOOD & DRINK|ENTERTAINMENT & MEDIA|0.9872468|
|TRAVEL|HEALTH & WELLNESS|0.9757120|
|POLITICS|BUSINESS & ECONOMY|0.9560016|
|PARENTING|FOOD & DRINK|0.7901254|
|QUEER VOICES|FOOD & DRINK|0.7172272|
|STYLE & BEAUTY|PARENTING|0.1024857|
|QUEER VOICES|ENTERTAINMENT & MEDIA|0.0644390|

## Part 2 results
### One-Sample t-tests
Each t-test was conducted using the same three lines of code: 
1. `t.test(x=insert_category_CL, mu=5.975, alternative="two.sided")` — this two-sided test returned whether or not the sample mean was equal to the population mean of **5.975**.
2. `t.test(x=polcl, mu=5.975, alternative="greater")` — the right-tailed test was conducted first, though there was no real reason for the order.
3. `t.test(x=polcl, mu=5.975, alternative="less")` — by the end of the third test, the results would show if the comparison was statistically significant or not.

The results of the two-sided tests on the top 10 categories confirmed the results of ANOVA, giving significant evidence: the sample means were not equal to the population mean, rejecting the null hypothesis in all 10 cases. Further testing with right- and left-tailed tests showed that there was a 50/50 split: 5 categories had an **average CL that was greater than the population mean** and 5 categories had an **average CL that was less than the population mean**. 
- They are listed here:
    
    **GREATER**: POLITICS, HEALTH & WELLNESS, TRAVEL,  WORLD NEWS, BUSINESS & ECONOMY
    
    **LESS**: ENTERTAINMENT & MEDIA, PARENTING, STYLE & BEAUTY, FOOD & DRINK, QUEER VOICES

Categories that were confirmed to be **greater** than the population mean had a **p-value of 1**, failing to reject the null hypothesis for the left-tailed test and a **p-value of 0.0000000000000002**, successfully rejecting the null hypothesis for the right-tailed test.

With the exception of **QUEER VOICES**, which had a **p-value of 0.0000007369**, rejecting the null hypothesis for the left-tailed test, categories that were confirmed to be **less** than the population mean had a **p-value of 0.0000000000000002**, rejecting the null hypothesis for the left-tailed test and a **p-value of 1**, failing to reject the null hypothesis for the right-tailed test.  

### Chi-Square Goodness-of-Fit
Using the population proportions of 0.277, 0.707, and 0.015, each sample was compared to the expected proportions using `chisq.test(expected_prop, sample_prop)`. The [results](https://github.com/rena-w/SW-FINAL-PROJECT/blob/main/chi_sq_results) of all 10 tests were insignificant, all yielding the same result.

X-Squared = 6, *df* = 4, **p-value = 0.1991**

Since the p-value of 0.1991 > significance level 0.05, fail to reject the null hypothesis in all 10 cases. There is *not enough strong statistical evidence* to conclude that the proportions of short, medium, and long words of each category are different from the proportion of the population.

# ANALYSIS
To discuss my findings and give some of my analysis, I am bringing back the guiding questions from the beginning of this writeup:

1. Is there a difference in average length of words (in characters) between different categories/genres of articles?
2. What is considered a 'long word' in the context of news headlines?
3. Do writers avoid using long words in their titles? 
4. Are long words more likely to appear in particular categories of articles? Why?
5. Does the word count of a headline have an impact on the length of words within it? (i.e., if a headline has more words, are those less likely to be long words because the headline itself is already long?) 

Pieces of information such as the summary statistics gathered during this project, the tests I've run, as well as observations about the nature of the data itself all contribute to my attempt at answering these questions. 

### Q1: average CL across categories
The statistical significance of the ANOVA results showed that there is definitely variability between the categories — the tiny p-value of 0.00....2 clearly states that there is strong evidence of different averages in different categories. After seeing that result, conducting the follow-up test between each pair in the top 10 categories revealed that some of the categories were very similar. 

Some of these pairs were unsurprising and made a lot of sense, like BUSINESS & ECONOMY and POLITICS. These two genres share a lot of vocabulary and often overlap in subject matter, so it makes sense that the style of headlines would share similarities as well. Other pairs were more surprising. For me, the most surprising pair was ***PARENTING*** and ***ENTERTAINMENT & MEDIA***. Those two genres feel like they should have drastically different energies, yet the data shows us that at least in this one aspect, they are the most similar pair, with a **p-value of 0.996** that asserts that the average word length is essentially identical between the two categories.

From the first two tests, it seems that we can conclude the majority of categories, at least in the top 10, have average word lengths that are consistently very different from each other. Overall, this answers my first question and confirms that yes, average CL of a headline may be impacted or dependent in some way on the genre and content of the article it titles. 

### Q2: the definition of a 'long word'
In the process of preparing for the latter two tests, I calculated the descriptive statistics for the combined list of all words in every headline, which I treated as the master list and the representative of the whole population. While I definitely think there are a lot of issues that I ignored or brushed over, which I will address later in this section, the statistics I found were useful for interpreting the data. 

Addressing Q2 in particular, I thought that using the formula used to find outliers would be a good way to identify words that seemed to be abnormally long. In the first iteration of my analysis (in my presentation), I had used a dataset consisting of uncleaned data for my statistics, and thus had found an IQR value that was very small. This was likely due to the abundance of very short words like "as", "it", "to", and other stopwords. These results were quite misleading, and so the summary statistics from the cleaned data were a little surprising at first. The value of 11 letters as the definition of a long word in the context of news article headlines does sound reasonable, though there are, again, many factors that I did not control for that are likely influencing my data.

Finally, another aspect of this project that I didn't get a chance to explore was comparing the frequency of a long word in the headlines dataset to the frequency of that word in other forms of prose. I would've liked to investigate if there were any patterns between different forms of writing. A guess I have would be that there is a strong association between frequency of usage in general prose and frequency of usage in headlines, since authors would want to make the most of the readers' familiarity with vocabulary and choose words that people are more likely to understand.

### Q3: avoidance of long words
Going off of our definition established from Q2, I found a potential answer to Q3 in the data for the chi-squared tests. Because I had sorted the quantitative CLs into three ranges to find the proportion of each length, it was also a really good way to observe how dramatic the difference was between each length and each category. As illustrated in [the results of the chi-squared tests](https://github.com/rena-w/SW-FINAL-PROJECT/blob/main/chi_sq_results), both through the bare counts and through the percentages, it is very clear that authors do avoid using long words, or at least use them very, very sparingly. This makes sense and also agrees with the other analysis from this project.  

### Q4: probability and frequency of long word occurrences
One thought I had while going about my initial research and data observations was about the content of each genre. I commented about this as part of the answer for Q1, but the frequency data from each category also gave some more strength to a potential argument. The category with the most long words was HEALTH & WELLNESS with 18 long words. HEALTH & WELLNESS is category that I would associate with more calm, informative writing that may be aimed at a different audience than something like ENTERTAINMENT & MEDIA; however, some of the other data looks like it could be contradictory, since the category with the second most long words is POLITICS, which I don't perceive as being very calm.

The chi-squared tests were specifically meant to answer Q4, which asked about the probability that long words would appear, and if there was any difference between category. The conditions for the tests were that tf the tests fail to reject H0 for all 10 categories being tested, meaning that the proportions of short, medium, and long words is the same across the board, then the results provide statistical evidence that the genre of an article has no bearing on the *amount* of long words in its headline. These results also suggests that long words are not more likely to be in any category, since the proportions are all essentially the same. 

As seen above, the results of my chi-squared tests were exactly this, and it pretty much answers Q4. For these 10 categories, there is no relation or pattern between category and likelihood of long words appearing. I wasn't expecting any specific results from this test, though it was a little surprising to see the exact same numbers for nearly all 10 categories.

### Q5: the relationship between word count and word length
Unfortunately, the question I didn't seem to find any traction on was question 5 regarding the relationship of word count and character length. Given more time, I think that the way I've organized this dataset and the code I've come up with would make it very easy to investigate this, but because I wanted to limit the scope of this project and also the length of this writeup, I decided not to pursue that topic at the moment. It would be very interesting to see if there's any evidence to suggest a kind of balance or compromise being made during the writing of a headline; in other words, do authors decide to sacrifice some of their already limited word count so they can use a long word?

### Analysis conclusion:
The results from the statistical testing were pretty uniform and fit together pretty well, without much contradiction. It was a little confusing, since the first two tests and the last two targeted a different aspect of word length, but the results for both types of tests not only didn't clash, but do seem to complement each other. In conclusion, while some of the statistical results weren't the most exciting, this project provided a good basis of information to build off of and form more hypotheses based on these more general calculations.

## **Potential sources of error / things that could be improved**
I've mentioned many times throughout this write-up that I would talk about potential sources of error or confounding factors that were likely influencing the data. In this section, I will list and talk about some of the things that were on my mind while I was working through the data and during statistical testing. I would like to try and give suggestions or explanations of how I might approach them if I were to conduct this study again or continue investigating this dataset, but some of these were quite tricky and I spent a while puzzling over the data, trying to figure them out.

During the cleaning process, there were many different items that I felt I needed to account for. One of these seemed particularly pressing: names. Because of the nature of news articles, proper nouns are much more likely to appear. In fact, the words 'Trump' and 'Donald' are #1 and #3 in the top 10 most common words, with 10,585 and 4,835 instances respectively. For names specifically, this frequency of proper nouns is probably most prevalent in categories like POLITICS and ENTERTAINMENT & MEDIA, where famous persons, celebrities, and other names are featured in nearly every headline. Regarding the example of 'Donald' and 'Trump'; although it could just be reflective of when these headlines were written, it still seems reasonable to assume that the appearance of proper nouns is influencing the average word count and character lengths. 

However, other proper nouns that were causing some concern and curiosity were place names — in particular, country names. In the top 10 most common words, the two-letter word 'us' appears with 3190 entries. When I first saw this, I was worried that my `clean ()` function or even my `get_lines()` function were messing up the data and converting terms like 'U.S.' into lowercase 'us', since I used them to remove punctuation and sort through stopwords, which requires tokenization first. This also brings up the problem of all-caps terms like USA or NASA. At the bottom of [1finalproject.py](), I have a few RegEx patterns that I used when scouring data after a cleaning attempt. At one point, I was hoping to be able to write a function that let me choose what non-standard terms I wanted to keep and which to remove. I have a mini version of that in `make_entry()`, since it gives you a choice of making full, combined entries, which have the original and cleaned versions of everything, clean entries, which are the entries I used for this analysis, or original entries that are the same as the original data, just without punctuation or problematic characters. 

Finally, I mentioned wanting to try POS-tagging if I had the time, and unfortunately I didn't have the opportunity to do any analysis of parts of speech or lexical categories. If I had access to these labels during my data analysis, it may have helped me clean the data a bit easier and ease my concerns about the interference of proper nouns. 

# CONCLUSION
During this project, I'd hoped to explore several aspects of this topic, which is reflected in the questions I've asked, but most of all I wanted to do cross-category comparisons. The biggest conclusions I would draw from my analysis is that there is strong variability of average word length between different genres of journalism; that result was statistically very strong and provides a good base to form deeper research questions. 

The clear main question I can see directly stemming from the results of this project is looking into the relationship between word count and character length, as I've emphasized many times in my writing. Another good research topic would be the location of long words within each headline; whether they tend to appear at the beginning, middle, or end of headlines. This topic can then be expanded to consider the role of word count and subject matter of the article, to name a few other interesting variables.

There are also other data that I didn't use at all. For example, variables that are completely untouched and unacknowledged by this writeup — there is a column with the publication date of each article, which you could use to look at patterns of word usage or headline structure throughout different times of the year, or at specific holidays and events. Since this dataset is from a single newspaper, it does limit the scope a bit. However, the data is from a pretty big range of years, with a lot of change that occurred during that timespan, so I think there is a good amount of diversity in this dataset to explore some other aspects of news and journalism as well.

I talked about improvements to the research questions and methods in the previous section during my discussion of sources of error. I also have some suggestions about how to approach research projects that deal with very large datasets. One big thing that I would emphasize for myself is to not over-complicate things, even if it's fun. I liked writing the code for this project and I'm really happy with how some of my functions are working (especially `search()`!!) but it was a bit time-consuming and took me away from actually working with the data.