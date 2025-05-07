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
        
        #alphabetized_entries = sort_alph(split_entries)
        return split_entries

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

def get_category(list, category): # find all (split HL, CAT) pairs and return list of only the split HL
    collected = []
    for tup in list:
        if f'{category}' in tup[1]:
            hl = tup[0]
            collected.append(hl)
    return collected

def findWC(list, paired=True): # find how many words in a string in a list; takes/returns list of pairs by default or just a list of lengths
    if paired:
        paired = []
        for entry in list:
            first = entry[0] 
            second = entry[1]
            wc = len(first)
            pair = (wc, second)
            paired.append(pair)
        return paired # returns something like [(7, POLITICS), (8, WELLNESS), (11, ENTERTAINMENT)]
    else: 
        length_list_s = [len(entry) for entry in list]
        return length_list_s # returns something like [7, 8, 11]
        
def findCL(list, paired=True): # find average character length of words in an entry; takes/returns list of pairs by default or just list of averages
    if paired:
        paired = []
        for ent in list:
            first = ent[0]
            second = ent[1]
            chara_lengths = [len(w) for w in first] # this is [5, 10, 13, 4, 6, 8, 7, 4]
            avg_chara = average(chara_lengths)
            pair = (avg_chara, second)
            paired.append(pair)
        return paired
    else:
        chara_avg = [[len(word) for word in entry] for entry in list] # find average character length of each word in a string
        avg = [average(entry) for entry in chara_avg] # find average of averages of words in each entry
        return avg

def write_file(file, list_data, format): # writes data to another file
    with open(f'{file}', 'w') as outfile:
        if f'{format}' == 'tuples':
            for tup in list_data:
                for item in tup:
                    outfile.write(str(item[0]) + '\n')   
            print("Successfully created file :)")
        if f'{format}' == 'strings':
            for item in list_data:
                outfile.write(str(item)+'\n')
            print("Successfully created file :)")    

def combine(list_of_lists): # combines lists into one list
    merged = []
    for lst in list_of_lists:
        merged += lst
    return merged

def stats(num_list): # takes a list of numbers and does statistics calculations
    mean = np.mean(num_list)
    median = np.median(num_list)
    variance = np.var(num_list)
    std_dev = np.std(num_list)
    range_val = np.max(num_list) - np.min(num_list)
    stats_listed = [('mean:', mean), ('median:', median), ('variance:', variance), ('std dev:', std_dev), ('range:', range_val)]
    return stats_listed

def get_gen_summary(list_of_HL):
    hl_WC = findWC(list_of_HL, paired=False) # list of word counts of every headline
    write_file('headlines_WC.txt', hl_WC, 'strings')
    hl_CL = findCL(list_of_HL, paired=False) # list of character length averages of every headline
    write_file('headlines_CL.txt', hl_CL, 'strings')
    stats_WC = average(hl_WC)
    stats_CL = average(hl_CL)
    results = [('General WC:', [hl_WC, stats_WC]), ('General CL:', [hl_CL, stats_CL])]
    #print(results[0])
    #print(results[1])
    return results

def get_cat_summary(list_of_entries, category):
    data = get_category(list_of_entries, f'{category}') # list of lists of strings (split HLs)
    write_file(f'{category}_headlines.txt', data, 'strings') # writes new file
    data_WC = findWC(data, paired=False) # returns list of just values
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
    #print(result[0])
    #print(result[1])
    return result

def loop_cat_summary(list_of_entries, categories):
    categories = category_list

### LISTS OF THINGS:
entries = get_lines('/Users/rena/Desktop/COURSES/LING 250/FINAL PROJECT/DATA.txt')

#### SETS OF VARIABLES ####
links = find_type(entries, '$A')

headlines = find_type(entries, '$B')
write_file('HL.txt', headlines, 'strings')
HLwords = combine(headlines) # all words in all headlines
writtenHL = find_type(entries, '$B', split=False)
write_file('headlines_clean.txt', writtenHL, 'strings')

categories = set(find_type(entries, '$C', split=False))
write_file('categories_real.txt', categories, 'strings')
#category_list = nltk.FreqDist(categories)
#print(category_list.most_common(5))

descriptions = find_type(entries, '$D')
authors = find_type(entries, '$E')
dates = find_type(entries, '$F')
                
#### PAIRS ####
categorized_headlines = make_pair(entries, '$B', '$C')
write_file('cat_HL.txt', categorized_headlines, 'strings')
test_cat_HLs = make_pair(entries, '$B', '$C', split=True)  
print('test:', test_cat_HLs[0][0])

#### GENERAL DESC STATS ####
general_stats = get_gen_summary(headlines)
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


def looky_look(entries_paired, target):
    captured = []
    for entry in entries_paired:
        if f'{target}' in entry[1]:
            captured.append(entry)
            print(f'"{target}" found!')
    return captured

test = looky_look(test_cat_HLs, 'Great')
print(test)

def find_all(entries_paired, target):
    captured = []
    for entry in entries_paired:
        if f'{target}' in entry[1]:
            captured.append(entry)
    if len(captured) == 0:
        print('None found :(')
    else:
        return captured
    
politics_test = find_all(categorized_headlines, 'POLITICS')