import sys
import re
import nltk 
from nltk.tag import pos_tag
import numpy as np

#### LIST OF FUNCTIONS TO USE ####
def get_lines(file): # get data in form of lines
    def extract_lines(input_file):# extract lines from file
        with open(input_file, 'r') as input:
            lines = input.readlines()
        lines_raw = [line.split() for line in lines] # this gets us each article entry in a separate string
        joined_lines = [' '.join(lin) for lin in lines_raw]
        chars = str.maketrans({'{': '', '}': '', ',': '', '\"':'','\"':'', '\'':'', '-':' '})
        cleaned = [item.translate(chars) for item in joined_lines] # gets rid of punctuation like {} brackets and double quotes ""
        return cleaned
    
    clean = extract_lines(file)  
    
    def replace_cats(list): # replace category labels
        a = [i.replace('link: ', '$A') for i in list]
        b = [al.replace('headline: ', '::: $B') for al in a]
        c = [bl.replace('category: ', '::: $C') for bl in b]
        d = [cl.replace('short_description: ', '::: $D') for cl in c]
        e = [dl.replace('authors: ', '::: $E') for dl in d]
        f = [el.replace('date: ', '::: $F') for el in e]
        return f
    
    alph = replace_cats(clean)
    
    def split_n_sort(input): # split by item in entry
        def split_on_cat(input_string):
            split = re.split(':::', input_string)
            stripped = [i.strip() for i in split]
            rep_quotes = [re.sub('\\\\u201[8|9]', '', a) for a in stripped]
            rep_emdash = [re.sub('\\\\u201[3|4|5]', '', b) for b in rep_quotes]
            rep_e_aigu = [re.sub('\\\\u0301', 'é', c) for c in rep_emdash]
            rep_e_grave = [re.sub('\\\\u200e[8|9]', 'è', d) for d in rep_e_aigu]
            rep_a_grave = [re.sub('\\\\u00e1', 'á', e) for e in rep_e_grave]
            rep_a_aigu = [re.sub('\\\\u00e1', 'á', f) for f in rep_a_grave]
            rep_space = [re.sub('\\\\u00a0', ' ', g) for g in rep_a_aigu]
            rep_ellipsis = [re.sub('\\\\u2026', '', h) for h in rep_space]
            rep_o_grave = [re.sub('\\\\u00f3', 'ò', i) for i in rep_ellipsis]
            rep_a_diaeresis = [re.sub('\\\\u00e4', 'ä', j) for j in rep_o_grave]
            rep_u_diaeresis = [re.sub('\\\\u00fc', 'ü', k) for k in rep_a_diaeresis]
            return rep_u_diaeresis    
            
        split_entries = [split_on_cat(string) for string in input]
  
        def sort_alph(input_list): # sort alphabetically
            sorted_input_list = []
            for sublist in input_list:    
                sort_sublist = sorted(sublist)
                sorted_input_list.append(sort_sublist)
            return sorted_input_list
        
        alphabetized_entries = sort_alph(split_entries)
        return alphabetized_entries

    lines = split_n_sort(alph)
    return lines

def find_type(input_list, type_var, split=True): # collect items from entries that have the same variable
    if split:
        types = []
        for entry in input_list:
            for string in entry:
                if f'{type_var}' in string:
                    replace = string.replace(f'{type_var}','')
                    strip = replace.strip()
                    splits = strip.split()
                    types.append(splits)
        return types
    else:
        types = []
        for entry in input_list:
            for string in entry:
                if f'{type_var}' in string:
                    replaced = string.replace(f'{type_var}','')
                    stripped = replaced.strip()
                    types.append(stripped)
        return types

def make_pair(list_of_entries, first_term, second_term, split=True): # make pairs of two variables, can be whole thing or split into words
    if split:    
        paired_unsplit = []
        keywords = [f'{first_term}', f'{second_term}']
        for entry in list_of_entries:
            paired_items_list = [s for s in entry if any(keyword in s for keyword in keywords)]
            clean_pair_a = [item.replace(f'{first_term}','') for item in paired_items_list]
            clean_pair_b = [e.replace(f'{second_term}','') for e in clean_pair_a]
            paired_unsplit.append(tuple(clean_pair_b))
        paired_split = []
        for tup in paired_unsplit:
            first = tup[0]
            second = tup[1]
            split_first = first.split(' ')
            combo = (split_first, second)
            paired_split.append(combo)
        return paired_split
    else: 
        paired_unsplit = []
        keywords = [f'{first_term}', f'{second_term}']
        for entry in list_of_entries:
            paired_items_list = [s for s in entry if any(keyword in s for keyword in keywords)]
            clean_pair_a = [item.replace(f'{first_term}','') for item in paired_items_list]
            clean_pair_b = [e.replace(f'{second_term}','') for e in clean_pair_a]
            paired_unsplit.append(tuple(clean_pair_b))
        return paired_unsplit

def get_category(list, category): # find all (split HL, CAT) pairs and return list of only the split HL
    collected = []
    for tup in list:
        if f'{category}' in tup[1]:
            hl = tup[0]
            collected.append(hl)
    return collected

def write_file(file, list_data, format): # writes data to another file
    with open(f'{file}', 'w') as outfile:
        if f'{format}' == 'tuples':
            for tup in list_data:
                for item in tup:
                    outfile.write(str(item[0]) + '\n')   
            print('Successfully created file! -> 'f'{file}')
        if f'{format}' == 'strings':
            for item in list_data:
                outfile.write(str(item)+'\n')
            print('Successfully created file! -> 'f'{file}') 
        if f'{format}' == 'single string':
            outfile.write(str(list_data))
            print ('Successfully created file! -> 'f'{file}')   

def combine(list_of_lists): # combines lists into one list
    merged = []
    for lst in list_of_lists:
        merged += lst
    return merged

#def clean(list, target, regex=True):
    #if regex:
        #re.sub'(?=, \d)|(?<=, )'
    #if not regex:
        #text = str(list)
        #for item in list:
            #[i.replace(f'{target}', '') for i in item]

def findWC(entry, paired=True, return_single=True): # find how many words in a string in a list; takes/returns list of pairs by default or just a list of lengths
    if paired:
        if not return_single:
            first = entry[0] 
            second = entry[1]
            wc = len(first)
            pair = (wc, second)
            return pair # returns something like (7, POLITICS), (8, WELLNESS), (11, ENTERTAINMENT)
        if return_single: # returns a single value 
            headline = entry[0]
            WC_value = len(headline)
            return WC_value # returns an integer
    if not paired:
        word_count = len(entry)
        return word_count
        
def findCL(entry, paired=True, return_single=True): # find average character length of words in an entry; takes/returns list of pairs by default or just list of averages
    if paired:    
        if not return_single:
            first = entry[0]
            second = entry[1]
            chara_lengths = [len(w) for w in first] # this is [5, 10, 13, 4, 6, 8, 7, 4]
            avg_chara = average(chara_lengths) # average character length for a word in this entry
            pair = (avg_chara, second)
            return pair # returns something like (7.137647, POLITICS)
        if return_single:
            first = entry[0]
            chara_count = [len(word) for word in first] # returns list of character counts like [3, 6, 2, 4, 6, 5]
            avg = average(chara_count) # finds the average for that headline; returns one integer
            return avg
    if not paired:
        chara = [len(word) for word in entry]
        avg_char = average(chara)
        return avg_char

def average(num_list): # find the mean of a list of numbers
    total = 0
    count = 0
    for num in num_list:
        total += num
        count += 1
    if count == 0:
        return 0
    average = total / count
    return average

def stats(num_list): # takes a list of numbers and does statistics calculations
    mean = np.mean(num_list)
    median = np.median(num_list)
    variance = np.var(num_list)
    std_dev = np.std(num_list)
    range_val = np.max(num_list) - np.min(num_list)
    stats_listed = [('mean:', mean), ('median:', median), ('variance:', variance), ('std dev:', std_dev), ('range:', range_val)]
    return stats_listed

def get_gen_summary(paired_HLs):
    hl_WC = findWC(paired_HLs, return_single=True) # list of word counts of every headline
    write_file('headlines_WC.txt', hl_WC, 'strings')
    hl_CL = findCL(paired_HLs, return_single=True) # list of character length averages of every headline
    write_file('headlines_CL.txt', hl_CL, 'strings')
    stats_WC = average(hl_WC)
    stats_CL = average(hl_CL)
    results = [('General WC:', [hl_WC, stats_WC]), ('General CL:', [hl_CL, stats_CL])]
    return results

def make_entry(paired_HLs):
    summaries = []
    for pair in paired_HLs:    
        hl_joined = ' '.join(pair[0])
        category = pair[1]
        word_count = findWC(pair, paired=True, return_single=True) # word count of headline
        chara_length = findCL(pair, paired=True, return_single=True) # character length average of one headline
        entry = (hl_joined, category, word_count, chara_length)
        summaries.append(entry)
    write_file('entry_data.txt', summaries, 'strings')
    return summaries

def get_cat_summary(list_of_entries, category):
    data = get_category(list_of_entries, f'{category}') # list of lists of strings (split HLs)
    write_file(f'{category}_headlines.txt', data, 'strings') # writes new file
    data_WC = [[findWC(entry, paired=True) for word in data] for entry in data] # returns list of just values
    write_file(f'{category}_WC.txt', data_WC, format='strings')
    if len(data_WC) == 0:
        print('error! something went wrong:(')
    avgWC = average(data_WC)
    stats_WC = stats(data_WC)
    data_CL = findCL(data, paired=False)
    write_file(f'{category}_CL.txt', data_WC, 'strings')
    if len(data_CL) == 0:
        print('error! something went wrong:(')
    avgCL = average(data_WC)
    stats_CL = stats(data_CL)
    result = [('WC:', [avgWC, stats_WC]), ('CL:', [avgCL, stats_CL])]
    #print('WC:', result[0])
    #print('CL:', result[1])
    return result

def look_for(entries_paired, target):
    captured = []
    for entry in entries_paired:
        if f'{target}' in entry[1]:
            captured.append(entry)
    if len(captured) != 0:
        print(f'"{target}" found!')        
        return captured
    else: 
        print('Nothing found!')

### LISTS ###
entries = get_lines('/Users/rena/Desktop/COURSES/LING 250/FINAL PROJECT/ALL_DATA.txt')

links = find_type(entries, '$A')

headlines = find_type(entries, '$B')
write_file('HL.txt', headlines, 'strings')
HLwords = combine(headlines) # all words in all headlines
write_file('HL_words', HLwords, 'single string')
writtenHL = find_type(entries, '$B', split=False)
write_file('headlines_clean.txt', writtenHL, 'strings')

categories_all = find_type(entries, '$C', split=False)
categories = set(categories_all)
write_file('categories.txt', categories, 'strings')
write_file('categories_all.txt', categories_all, 'strings')
#category_list = nltk.FreqDist(categories)
#print(category_list.most_common(5))

descriptions = find_type(entries, '$D')
authors = find_type(entries, '$E')
dates = find_type(entries, '$F')
                
#### PAIRS ####
categorized_headlines = make_pair(entries, '$B', '$C')
write_file('categorized_HL.txt', categorized_headlines, 'strings')
categorized_HLs_clean = make_pair(entries, '$B', '$C', split=False)  
write_file('categorized_clean.txt', categorized_HLs_clean, 'strings')

#### GENERAL DESC STATS ####
#general_stats = get_gen_summary(headlines)
# WC
# mean: 9.699642528170594
# median: 10.0
# variance: 9.541723039156574
# std dev: 3.088967956965008
# range: 44

# CL
# mean: 5.111783666197601
# median: 5.0
# variance: 0.8486685158900964
# std dev: 0.9212320640805423
# range: 36.0

test_entry_data = make_entry(categorized_headlines)
politics_test = get_category(categorized_headlines, 'POLITICS')

## need a file that has:
#### headline, category, word count, character count