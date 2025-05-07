import sys
import re
import nltk 
from nltk.tag import pos_tag
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
import numpy as np

#### LIST OF FUNCTIONS TO USE ####
def get_lines(file): # get data in form of lines
    def extract_lines(input_file):# extract lines from file
        with open(input_file, 'r') as input:
            lines = input.readlines()
        lines_raw = [line.split() for line in lines] # this gets us each article entry in a separate string
        joined_lines = [' '.join(lin) for lin in lines_raw]
        chars = str.maketrans({'{':'', '}':'', ',':'', '\"':'','\"':'','?':'', '\'':'', '-':' '})
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
        def split_delete_unicode(input_string):
            split = re.split(':::', input_string)
            stripped = [i.strip() for i in split]
            delete = [re.sub('\\\\u201[345890]|\\\\u200[abef]|\\\\u00ae|\\\\u00a[39b]|\\\\u2032|\\\\u02bc|\\\\u00b[047]|\\\\u2122|\\\\u202[68]|\\\\ufeff|\\\\u02bb', '', a) for a in stripped]
            rep_e = [re.sub('\\\\u0301|\\\\uffc3\\\\uffab|\\\\uffc3\\\\uffa9|\\\\u200e[89]|\\\\u00e[89ab]|\\\\u1ec5', 'e', b) for b in delete]
            rep_E = [re.sub('\\\\u00c9', 'E', c) for c in rep_e]
            rep_a = [re.sub('\\\\u00e[01245]|\\\\u1ea[15]|\\\\u0101', 'a', d) for d in rep_E]
            rep_i = [re.sub('\\\\u00e[cdef]', 'i', e) for e in rep_a]
            rep_o = [re.sub('\\\\u00f[3486]|\\\\u01d2', 'o', f) for f in rep_i]
            rep_u = [re.sub('\\\\u00f[abc9]', 'u', g) for g in rep_o]
            rep_n = [re.sub('\\\\u00f1', 'n', h) for h in rep_u]
            rep_c = [re.sub('\\\\u00e7', 'c', i) for i in rep_n]
            rep_s = [re.sub('\\\\u015b|\\\\u0219', 's', j) for j in rep_c]
            rep_oe = [re.sub('\\\\u0153','oe',k) for k in rep_s]
            rep_z = [re.sub('\\\\u017e', 'z', l) for l in rep_oe]
            rep_U = [re.sub('\\\\u00dc','U',m) for m in rep_z]
            rep_C = [re.sub('\\\\u00c7|\\\\u010c','C', n) for n in rep_U]
            space = [re.sub('\\\\u00a0', ' ', o) for o in rep_C]
            rep_doublequotes = [re.sub('\\\\u201[cd]|\\\\', '"', p) for p in space]
            rep_doublespaces = [re.sub(r'\s{2,}', ' ', q) for q in rep_doublequotes]
            return rep_doublespaces    
            
        split_entries = [split_delete_unicode(string) for string in input]
  
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
            paired_unsplit.append(clean_pair_b)
        return paired_unsplit

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

def findWC(entry): # find how many words in a string in a list; takes/returns list of pairs by default or just a list of lengths
    headline = entry[0]
    WC_value = len(headline)
    return WC_value # returns an integer
        
def findCL(entry): # find average character length of words in an entry; takes/returns list of pairs by default or just list of averages   
    first = entry[0]
    entry_count = []
    for word in first:
        count = 0
        for char in word: 
            if char.isalpha():
                count += 1 
        entry_count.append(count)
    avg = average(entry_count) # finds the average for that headline; returns one integer
    return avg

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

def make_entry(paired_HLs):
    summaries_clean = []
    for pair in paired_HLs:    
        hl_joined = ' '.join(pair[0])
        category = pair[1]
        word_count = findWC(pair) # word count of headline
        chara_length = findCL(pair) # character length average of one headline
        clean_entry = (hl_joined, category, word_count, chara_length)
        summaries_clean.append(clean_entry)
    write_file('entry_data.txt', summaries_clean, 'strings')
    return summaries_clean

def find(entries_paired):
    def choose_search():    
        print('search function activated!')
        print('What are you looking for? --> WORD    CATEGORY      WC     CL')
        variable = input('Enter search: ')
        return variable
    search = choose_search() 
    def searching(search_choice):   
        if f'{search_choice}'=='word':    
            print('What word(s) are you looking for?')
            target = str(input('Enter target word(s): '))
            captured_words = []
            for entry in entries_paired:
                if target in entry[0]: captured_words.append(entry)
            return captured_words
        if f'{search_choice}'=='category':
            print('What category are you looking for?')
            inpt = input('Enter category: ')
            category = inpt.upper()
            captured_cat = []
            for entry in entries_paired:
                if f'{category}' in entry[1]:
                    captured_cat.append(entry)
            return captured_cat
        if f'{search_choice}' == 'WC':
            captured_WC = []
            condition = input('WC is (greater than > / less than < / equal to =) ')
            if condition=='>':    
                wc_limit = int(input('Enter number: '))
                for entry in entries_paired:    
                    if entry[2] > wc_limit:
                        captured_WC.append(entry)
            if condition=='<':
                wc_lim = int(input('Enter number: '))
                for entry in entries_paired:
                    if entry[2] < wc_lim:
                        captured_WC.append(entry)
            if condition=='=':
                wc_li = int(input('Enter number: '))
                for entry in entries_paired:    
                    if entry[2] == wc_li:
                        captured_WC.append(entry)
            return captured_WC
        if f'{search_choice}'=='CL':
            captured_CL = []
            cond = input('CL is (greater than > / less than < / equal to =) ')
            if cond=='>':    
                cl_limit = int(input('Enter number: '))
                for entry in entries_paired:
                    if entry[3] > cl_limit:
                        captured_CL.append(entry)
            if cond=='<':
                cl_lim = int(input('Enter number: '))
                for entry in entries_paired:
                    if entry[3] < cl_lim:
                        captured_CL.append(entry)
            if cond=='=':
                cl_li = int(input('Enter number: '))
                for entry in entries_paired:
                    if entry[3] == cl_li:
                        captured_CL.append(entry)
            return captured_CL
    results = searching(search)
    if len(results) != 0:
        print('Found! Would you like to write to a file?')
        answer = input('Y/N: ') 
        if f'{answer}'=='y':
            filename = input('Enter .txt file name: ')
            write_file(f'{filename}.txt', results, 'strings')
            return results
        if f'{answer}'=='n': 
            print('Done :)')
            return results
    else: print('Nothing found!')

### LISTS ###
raw_data = get_lines('/Users/rena/Desktop/COURSES/LING 250/FINAL PROJECT/ALL_DATA.txt')

links = find_type(raw_data, '$A')

headlines = find_type(raw_data, '$B')
#write_file('HL.txt', headlines, 'strings')
HLwords = combine(headlines) # all words in all headlines
total_word_count = len(HLwords)
writtenHL = find_type(raw_data, '$B', split=False)
#write_file('headlines_clean.txt', writtenHL, 'strings')

categories_all = find_type(raw_data, '$C', split=False)
categories = sorted(set(categories_all))
#write_file('categories.txt', categories, 'strings')
#category_list = nltk.FreqDist(categories)
#print(category_list.most_common(5))

descriptions = find_type(raw_data, '$D')
authors = find_type(raw_data, '$E')
dates = find_type(raw_data, '$F')
                
#### PAIRS ####
categorized_headlines = make_pair(raw_data, '$B', '$C') #### USE THIS!!!! ####
categorized_HLs_clean = make_pair(raw_data, '$B', '$C', split=False)  
#write_file('categorized_clean.txt', categorized_HLs_clean, 'strings')

entries = make_entry(categorized_headlines)
#correct_entries = find(all_entries, 'WC')
test = find(entries)

## entries has: (headline, category, word count, character count)
### REGEX 
# for removing () and ': \('|\)$|'
# for hashtags: #[0-9]*[A-Za-z]+[0-9a-zA-Z]+(?=\s)
# for any all caps terms in parentheses: \([A-Z]+\)
# for numbers: (?<!\$|:)(?<=\s|^)[0-9]+(?=\s|,|:|\?)(?!:\d)