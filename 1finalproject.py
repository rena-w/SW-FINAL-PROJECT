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
        chars = str.maketrans({'{':'', '}':'', ',':'', '\"':'','\"':'','?':'', '\'':'', '-':' ', '!':'', '.':''})
        cleaned = [item.translate(chars) for item in joined_lines] # gets rid of punctuation/non alphanumeric characters
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
            print('Successfully created file! -> 'f'{file}.txt')
        if f'{format}' == 'strings':
            for item in list_data:
                outfile.write(str(item)+'\n')
            print('Successfully created file! -> 'f'{file}.txt') 
        if f'{format}' == 'single string':
            outfile.write(str(list_data))
            print ('Successfully created file! -> 'f'{file}.txt')   

def combine(list_of_lists): # combines lists into one list
    merged = []
    for lst in list_of_lists:
        merged += lst
    return merged

def clean(entry, paired=True): # cleans headlines — removes numbers, punctuation, and stop words
    stop_words = set(stopwords.words('english'))
    if paired:
        cleaned_p = []
        headline = entry[0]
        for word in headline: 
            w = word.lower()
            if w.isalpha() and w not in stop_words and len(w)>1:
                cleaned_p.append(word)
        results = (cleaned_p, entry[1])
        return results
    if not paired:
        cleaned_np = []
        hl = entry    
        for wor in hl:
            wo = wor.lower()
            if wo.isalpha() and wo not in stop_words and len(wo)>1:
                cleaned_np.append(wor)
        return cleaned_np

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

def make_entry(pairs, both=True): # INPUT UNCLEAN PAIRS PLEASE — makes entries of each headline with category, WC, CL — this is used for R!
    if both: # want entries with both UNCLEAN and CLEAN data   
        entries = []
        for pair in pairs: 
            category = pair[1]
            UChl = pair[0]
            clean_pair = clean(pair)
            Chl = clean_pair[0]
            if len(Chl) > 1:
                UCword_count = findWC(pair) # word count of UNCLEAN headline
                UCchara_length = findCL(pair) # character length of UNCLEAN headline
                UChl_joined = ' '.join(UChl) # joined UNCLEAN headline
                Cword_count = findWC(clean_pair) # word count of CLEAN headline
                Cchara_length = findCL(clean_pair) # character length of CLEAN headline
                Chl_joined = ' '.join(Chl) # joined CLEAN headline
                entry = (category, UChl_joined, Chl_joined, UCword_count, Cword_count, UCchara_length, Cchara_length)
                entries.append(entry)
            else: 
                continue
        return entries
    if not both: 
        print('CLEAN or UNCLEAN?')
        inpt = input('Enter type of data: ')
        if f'{inpt}'=='clean':     
            en = []
            for pair in pairs:
                cat = pair[1]
                cleaned = clean(pair)
                chl = cleaned[0]
                if len(chl) > 1:
                    chl_join = ' '.join(cleaned[0])
                    wc = findWC(cleaned)
                    cl = findCL(cleaned)
                    e = (cat, chl_join, wc, cl)
                    en.append(e)
                else:
                    continue
            return en
        if f'{inpt}'=='unclean':
            entri = []
            for pair in pairs:
                cat_ = pair[1]
                uchl = ' '.join(pair[0])
                wc_ = findWC(pair)
                cl_ = findCL(pair)
                e_ = (cat_, uchl, wc_, cl_)
                entri.append(e_)
            return entri

def search(entries_paired): # data search function — can look for particular words, categories, WCs, or CLs 
    print('search function activated!')
    print('What are you looking for? --> WORD    CATEGORY      WC     CL')
    variable = input('Enter search: ')
    def word_search(entries_lista, both=True):
        print('What word(s) are you looking for?')
        target = str(input('Enter target word(s): '))    
        if both:   
            print('Searching ORIGINAL or CLEAN data?')
            inp = input('Enter data type: ')
            if f'{inp}'=='original':
                captured_Owords = []
                for ee in entries_lista:
                    if target in ee[1]: captured_Owords.append(ee)
                return captured_Owords
            if f'{inp}'=='clean':
                captured_Owords = []
                for nn in entries_lista:
                    if target in nn[2]: captured_Owords.append(nn)
                return captured_Owords
        if not both:   
            captured_words = []
            for ww in entries_lista:
                if target in ww[1]: captured_words.append(ww)
            return captured_words
    def category_search(entries_listb):
        print('What category are you looking for?')
        inpt = input('Enter category: ')
        category = inpt.upper()
        captured_cat = []
        for eee in entries_listb:
            if f'{category}' in eee[0]:
                captured_cat.append(eee)
        return captured_cat
    def WC_search(entries_listc, both=True):
        condition = input('WC is (greater than > / less than < / equal to =) ')
        wc_limit = int(input('Enter number: '))
        if both:
            print('Searching ORIGINAL or CLEAN data?')
            inpt = input('Enter data type: ')
            if f'{inpt}'=='original':
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
            if f'{inpt}'=='clean':
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
        if not both:
            captured_WC = []
            if f'{condition}'=='>':    
                for rrrrr in entries_listc:    
                    if rrrrr[2] > wc_limit:
                        captured_WC.append(rrrrr)
            if f'{condition}'=='<':
                for iiiii in entries_listc:
                    if iiiii[2] < wc_limit:
                        captured_WC.append(iiiii)
            if f'{condition}'=='=':
                for eeeee in entries_listc:    
                    if eeeee[2] == wc_limit:
                        captured_WC.append(eeeee)
            return captured_WC
    def CL_search(entries_listd, both=True):
        condition = input('CL is (greater than > / less than < / equal to =) ')
        cl_limit = int(input('Enter number: '))
        if both:    
            print('Searching ORIGINAL or CLEAN data?')
            inpt = input('Enter data type: ')
            if f'{inpt}'=='original':
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
            if f'{inpt}'=='clean':
                captured_cleanCL = []
                if f'{condition}'=='>':    
                    for r in entries_listd:
                        if r[6] > cl_limit:
                            captured_cleanCL.append(r)
                if f'{condition}'=='<':
                    for i in entries_listd:
                        if i[6] < cl_limit:
                            captured_cleanCL.append(i)
                if f'{condition}'=='=':
                    for s in entries_listd:
                        if s[6] == cl_limit:
                            captured_cleanCL.append(s)
                return captured_cleanCL
        if not both:
                captured_CL = []
                if f'{condition}'=='>':    
                    for aaaaa in entries_listd:
                        if aaaaa[6] > cl_limit:
                            captured_CL.append(aaaaa)
                if f'{condition}'=='<':
                    for bbbb in entries_listd:
                        if bbbb[6] < cl_limit:
                            captured_CL.append(bbbb)
                if f'{condition}'=='=':
                    for cccc in entries_listd:
                        if cccc[6] == cl_limit:
                            captured_CL.append(cccc)
                return captured_CL
    def result_finding(results):
        if len(results) != 0:
            print('Found! Would you like to write to a file?')
            answer = input('Y/N: ') 
            if f'{answer}'=='y':
                filename = input('Enter .txt file name: ')
                write_file(f'{filename}', results, 'strings')
                return results
            if f'{answer}'=='n': 
                print('Done :)')
                return results
        else: print('Nothing found!')
    if f'{variable}'=='word':       
        loc = input('Does this dataset contain more than one kind of data? Y/N: ')
        if f'{loc}'=='y':
            both_word_search = word_search(entries_paired, both=True)
            results_a = result_finding(both_word_search)
            return results_a
        if f'{loc}'=='n':
            single_word_search = word_search(entries_paired, both=False)
            results_b = result_finding(single_word_search)
            return results_b
    if f'{variable}'=='category':
        category_search_ = category_search(entries_paired)
        results_c = result_finding(category_search_)
        return results_c
    if f'{variable}' == 'WC':
        lo = input('Does this dataset contain more than one kind of data? Y/N: ')
        if f'{lo}'=='y':
            both_wc_search = WC_search(entries_paired, both=True)
            results_d = result_finding(both_wc_search)
            return results_d
        if f'{lo}'=='n':
            single_wc_search = WC_search(entries_paired, both=False)
            results_e = result_finding(single_wc_search)
            return results_e
    if f'{variable}'=='CL':
        l = input('Does this dataset contain more than one kind of data? Y/N: ')
        if f'{l}'=='y':
           both_cl_search = CL_search(entries_paired, both=True)
           results_f = result_finding(both_cl_search)
           return results_f
        if f'{l}'=='n':
           single_cl_search = CL_search(entries_paired, both=False)
           results_g = result_finding(single_cl_search)
           return results_g

### RAW DATA ###
raw_data = get_lines('/Users/rena/Desktop/COURSES/LING 250/FINAL PROJECT/ALL_DATA.txt')
#write_file('RAW_DATA', raw_data, 'strings')
headlines = find_type(raw_data, '$B') # only the headlines, split into individual words — doesn't have punctuation but DOES have hashtags
#print('number of raw headlines TOTAL: ', len(headlines))

### CATEGORIES ###
categories_all = find_type(raw_data, '$C', split=False)
cat_dist = nltk.FreqDist(categories_all)
cat_list = sorted(cat_dist.most_common(10), key=lambda x: x[1], reverse=True)
category_counts = sorted(cat_dist.most_common(30))
#write_file('category_counts', category_counts, 'strings')
categories = sorted(set(categories_all))

### PAIRS ###
categorized_headlines = make_pair(raw_data, '$B', '$C') #### USE THIS TO MAKE ENTRIES ####
written_catHLs = [(' '.join(entry[0]), entry[1]) for entry in categorized_headlines]
#write_file('categorized_headlines', written_catHLs, 'strings')
cleaned_headlines = [clean(h) for h in categorized_headlines]
written_cleanedHLs = [(' '.join(entry[0]), entry[1]) for entry in cleaned_headlines]
#write_file('cleaned_headlines', written_cleanedHLs, 'strings')

### ENTRIES ###
full_entry = make_entry(categorized_headlines) # ORIG / CLEAN COMBINED ENTRIES 
#write_file('full_entries', full_entry, 'strings')
#print('making CLEAN entries!!!')
entries = make_entry(categorized_headlines, both=False) # USEABLE ENTRIES
#write_file('entries', entries, 'strings')
#print('number of USEABLE entries: ', len(entries))
## entries has: (category, original HL, cleaned HL, original WC, cleaned WC, original CL, cleaned CL)

#print('TEST: making UNCLEAN ENTRIES')
#unclean_entries = make_entry(categorized_headlines, both=False)
#print('total number of entries: ', len(unclean_entries))

### WORDS / DATA & NUMBERS ###
UC_HL_words = combine(headlines) # all words in headlines
#print('number of words BEFORE cleaning): ', len(UC_HL_words))
C_HLwords = clean(UC_HL_words, paired=False) # list of words remaining AFTER CLEAN
#write_file('all_HLwords', sorted(C_HLwords), 'strings')
#print('number of words AFTER cleaning: ', len(C_HLwords))
lower_all_HLwords = [word.lower() for word in C_HLwords]
HLwords = sorted(set(lower_all_HLwords))
#write_file('HLwords', HLwords, 'strings')
#print('number of unique words: ', len(HLwords))
words_dist = nltk.FreqDist(lower_all_HLwords)
#print('10 most common words: ', sorted(words_dist.most_common(10)))

rough_avg_WC = len(UC_HL_words)/len(headlines) # rough estimate of average word count from all words divided by number of headlines
#print('rough average word count per UNCLEAN headline: ', rough_avg_WC)
ucWC_data = [len(item[0]) for item in categorized_headlines] # list of word counts from UNCLEAN headlines 
#write_file('c_uncleanWC_data', ucWC_data, 'strings')
UCcount_dist = nltk.FreqDist(ucWC_data)
#print('10 most common UNCLEAN WCs: ', UCcount_dist.most_common(10))
rough_avg_cleanWC = len(C_HLwords)/len(cleaned_headlines) # rough estimate of average word count from clean words divided by number of clean headlines
#print('rough average word count per CLEAN headline: ', rough_avg_cleanWC)
cWC_data = [len(item[0]) for item in cleaned_headlines] # list of word counts from CLEAN headlines
#write_file('cleanWC_data', cWC_data, 'strings')
Ccount_dist = nltk.FreqDist(cWC_data)
#print('10 most common CLEAN WCs: ', Ccount_dist.most_common(10))

char_length_set = [len(w) for w in HLwords] # list of CLs of SET OF ALL WORDS found in headlines
#print('average length of all UNIQUE words in headlines: ', average(char_length_set))
CL_data = [len(s) for s in C_HLwords] # list of CLs from ALL WORDS in headlines
#write_file('CL_data', CL_data, 'strings')
#print('average length of ALL WORDS in headlines: ', average(CL_data))
lengths_dist = nltk.FreqDist(CL_data)
#print('10 most common lengths: ', sorted(lengths_dist.most_common(10)))


search(entries)








### REGEX 
# for removing parentheses and apostrophes: \('|\)$|']
# for hashtags: #[0-9]*[A-Za-z]+[0-9a-zA-Z]+(?=\s)
# for any all caps terms in parentheses: \([A-Z]+\)
# for numbers: (?<!\$|:)(?<=\s|^)[0-9]+(?=\s|,|:|\?)(?!:\d)

# EXTRA DATA #
links = find_type(raw_data, '$A')
descriptions = find_type(raw_data, '$D')
authors = find_type(raw_data, '$E')
dates = find_type(raw_data, '$F')