import sys
import re
import nltk 
from nltk.tag import pos_tag
from nltk.corpus import stopwords
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

def make_pair(list_of_entries, first_term, second_term): # make pairs of two variables
    cleaned = []
    paired = []
    keywords = [f'{first_term}', f'{second_term}']
    for entry in list_of_entries:
        paired_items_list = [s for s in entry if any(keyword in s for keyword in keywords)]
        clean_pair_a = [item.replace(f'{first_term}','') for item in paired_items_list]
        clean_pair_b = [e.replace(f'{second_term}','') for e in clean_pair_a]
        cleaned.append(tuple(clean_pair_b))
    for tup in cleaned:
        split_first = tup[0].split(' ')
        combo = (split_first, tup[1])
        paired.append(combo)
    return paired

def write_file(file, list_data, format): # writes data to another file
    with open(f'{file}.txt', 'w') as outfile:
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

def clean(entry, paired=True): # cleans headlines — removes numbers and stop words
    stop_words = set(stopwords.words('english'))
    if paired:
        cleaned_p = []
        headline = entry[0]
        for word in headline: 
            w = word.lower()
            if w.isalpha() and w not in stop_words:
                cleaned_p.append(word)
        results = (cleaned_p, entry[1])
        return results
    if not paired:
        cleaned_np = []
        hl = entry    
        for wor in hl:
            wo = wor.lower()
            if wo.isalpha() and wo not in stop_words:
                cleaned_np.append(wor)
        return cleaned_np

def findWC(entry): # find how many words in a string in a list
    headline = entry[0]
    WC_value = len(headline)
    return WC_value # returns an integer
        
def findCL(entry): # find average character length of words in an entry
    headline = entry[0]
    entry_count = []
    for word in headline:
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

def make_entry(UCpairs): # INPUT UNCLEAN PAIRS PLEASE — makes entries of each headline with category, WC, CL — this is used for R!
    entries = []
    for pair in UCpairs: 
        category = pair[1]
        UChl = pair[0]
        clean_pair = clean(pair)
        Chl = clean_pair[0]
        UCword_count = findWC(pair) # word count of UNCLEAN headline
        UCchara_length = findCL(pair) # character length of UNCLEAN headline
        UChl_joined = ' '.join(UChl) # joined UNCLEAN headline
        Cword_count = findWC(clean_pair) # word count of CLEAN headline
        Cchara_length = findCL(clean_pair) # character length of CLEAN headline
        Chl_joined = ' '.join(Chl) # joined CLEAN headline
        entry = (category, UChl_joined, Chl_joined, UCword_count, Cword_count, UCchara_length, Cchara_length)
        entries.append(entry)
    return entries

def find(entries_paired): # data search function — can look for particular words, categories, WCs, or CLs 
    print('search function activated!')
    print('What are you looking for? --> WORD    CATEGORY      WC     CL')
    variable = input('Enter search: ')
    def word_search(entries_lista, original=True):
        print('What word(s) are you looking for?')
        target = str(input('Enter target word(s): '))    
        if original:   
            captured_Owords = []
            for ee in entries_lista:
                if target in ee[1]: captured_Owords.append(ee)
            return captured_Owords
        if not original:   
            captured_Cwords = []
            for rr in entries_lista:
                if target in rr[2]: captured_Cwords.append(rr)
            return captured_Cwords
    def category_search(entries_listb):
        print('What category are you looking for?')
        inpt = input('Enter category: ')
        category = inpt.upper()
        captured_cat = []
        for eee in entries_listb:
            if f'{category}' in eee[0]:
                captured_cat.append(eee)
        return captured_cat
    def WC_search(entries_listc, original=True):
        condition = input('WC is (greater than > / less than < / equal to =) ')
        wc_limit = int(input('Enter number: '))
        if original:
            captured_origWC = []
            if f'{condition}'=='>':    
                for e in entries_listc:    
                    if e[3] > wc_limit:
                        captured_origWC.append(e)
            if f'{condition}'=='<':
                for n in entries_listc:
                    if n[3] < wc_limit:
                        captured_origWC.append(n)
            if f'{condition}'=='=':
                for t in entries_listc:    
                    if t[3] == wc_limit:
                        captured_origWC.append(t)
            return captured_origWC
        if not original:
            captured_cleanWC = []
            if f'{condition}'=='>':    
                for r in entries_listc:    
                    if r[4] > wc_limit:
                        captured_cleanWC.append(r)
            if f'{condition}'=='<':
                for i in entries_listc:
                    if i[4] < wc_limit:
                        captured_cleanWC.append(i)
            if f'{condition}'=='=':
                for eeee in entries_listc:    
                    if eeee[4] == wc_limit:
                        captured_cleanWC.append(eeee)
            return captured_cleanWC
    def CL_search(entries_listd, original=True):
        condition = input('CL is (greater than > / less than < / equal to =) ')
        cl_limit = int(input('Enter number: '))
        if original:    
            captured_origCL = []
            if f'{condition}'=='>':    
                for e in entries_listd:
                    if e[5] > cl_limit:
                        captured_origCL.append(e)
            if f'{condition}'=='<':
                for n in entries_listd:
                    if n[5] < cl_limit:
                        captured_origCL.append(n)
            if f'{condition}'=='=':
                for t in entries_listd:
                    if t[5] == cl_limit:
                        captured_origCL.append(t)
            return captured_origCL
        if not original:
            captured_cleanCL = []
            if f'{condition}'=='>':    
                for r in entries_listd:
                    if r[6] > cl_limit:
                        captured_cleanCL.append(r)
            if f'{condition}'=='<':
                for i in entries_listd:
                    if y[6] < cl_limit:
                        captured_cleanCL.append(i)
            if f'{condition}'=='=':
                for s in entries_listd:
                    if s[6] == cl_limit:
                        captured_cleanCL.append(s)
            return captured_cleanCL
    def result_finding(results):
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
    if f'{variable}'=='word':       
        loc = input('Searching ORIGINAL or CLEAN? Enter: ')
        if f'{loc}'=='original':
            orig_word_search = word_search(entries_paired, original=True)
            results_a = result_finding(orig_word_search)
            return results_a
        if f'{loc}'=='clean':
            clean_word_search = word_search(entries_paired, original=False)
            results_b = result_finding(clean_word_search)
            return results_b
    if f'{variable}'=='category':
        category_search_ = category_search(entries_paired)
        results_c = result_finding(category_search_)
        return results_c
    if f'{variable}' == 'WC':
        lo = input('Searching ORIGINAL or CLEAN? Enter: ')
        if f'{lo}'=='original':
            orig_wc_search = WC_search(entries_paired, original=True)
            results_d = result_finding(orig_wc_search)
            return results_d
        if f'{lo}'=='clean':
            clean_wc_search = WC_search(entries_paired, original=False)
            results_e = result_finding(clean_wc_search)
            return results_e
    if f'{variable}'=='CL':
        l = input('Searching ORIGINAL or CLEAN? Enter: ')
        if f'{l}'=='original':
           orig_cl_search = CL_search(entries_paired, original=True)
           results_f = result_finding(orig_cl_search)
           return results_f
        if f'{l}'=='clean':
           clean_cl_search = CL_search(entries_paired, original=False)
           results_g = result_finding(clean_cl_search)
           return results_g
        
### DATA ###
raw_data = get_lines('/Users/rena/Desktop/COURSES/LING 250/FINAL PROJECT/ALL_DATA.txt')

headlines = find_type(raw_data, '$B')
UC_HL_words = combine(headlines) # all words in headlines
total_word_count = len(UC_HL_words)
#print('Total word count: ', total_word_count)
rough_avg_WC = total_word_count/len(headlines) # rough estimate of average word count from all words
#print('Rough average word count per UNCLEAN headline: ', rough_avg_WC)

clean_loose_HLs = [clean(hl, paired=False) for hl in headlines]
HLwords = combine(clean_loose_HLs) # words remaining AFTER CLEAN
cleaned_word_count = len(HLwords)
#print('Cleaned word count: ', cleaned_word_count)
clean_avg_WC = cleaned_word_count/len(clean_loose_HLs)
#print('Rough average word count per CLEAN headline: ', clean_avg_WC)

categories_all = find_type(raw_data, '$C', split=False)
categories = sorted(set(categories_all))
                
#### PAIRS ####
categorized_headlines = make_pair(raw_data, '$B', '$C') #### USE THIS!!!! ####
#write_file('categorized_headlines', categorized_headlines, 'strings')
cleaned_headlines = [clean(h) for h in categorized_headlines]
entries = make_entry(categorized_headlines)
#write_file('entry_data', entries, 'strings')
search = find(entries)

## entries has: (category, original HL, cleaned HL, original WC, cleaned WC, original CL, cleaned CL)

### REGEX 
# for removing parentheses and apostrophes: \('|\)$|']
# for hashtags: #[0-9]*[A-Za-z]+[0-9a-zA-Z]+(?=\s)
# for any all caps terms in parentheses: \([A-Z]+\)
# for numbers: (?<!\$|:)(?<=\s|^)[0-9]+(?=\s|,|:|\?)(?!:\d)

##### EXTRA DATA #####
links = find_type(raw_data, '$A')
descriptions = find_type(raw_data, '$D')
authors = find_type(raw_data, '$E')
dates = find_type(raw_data, '$F')