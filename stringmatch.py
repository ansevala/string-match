#!/usr/bin/env python
# coding: utf-8
#
# Author and maintainer: Anselmi Valasmo
# Copyright (c) 2017 ansevala
# https://github.com/ansevala/string-match
# MIT License
#
# String-match
#
# version 1.0.0.0
# 2017-03-06
#
# Python functions for evaluating how well two strings match each other
#

all_to_lower_case = True # "True" or "False" up to you

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 
    'v', 'w', 'x', 'y', 'z', 'å', 'ä', 
    'ö'
    ] # The alphabet looks like this where I live; feel free to change it

# This function triples the length of a string by adding
# whitespaces to both ends
def add_space_to_both_ends(s):
    return ' ' * len(s) + s + ' ' * len(s)

# This function adds 50% to the combined length of two strings by adding
# whitespaces to the middle
def add_space_to_the_middle(s1, s2):
    return s1 + ' ' * (len(s1+s2)/2) + s2

# This function returns the number of characters both strings have allowing
# multiple occurances
def same_char_count(str1, str2):
    if (len(str1) == 0 or len(str2) == 0):
        return 0
    if (str1 == str2):
        return len(str1)
    str1 = str1.lower() # these have to be transformed
    str2 = str2.lower() # other way it would be silly
    if (len(str1) > len(str2)): 
        longer_str = str1
        shorter_str = str2
    else:
        longer_str = str2
        shorter_str = str1
    same_char_count = 0
    for char in alphabet:
        if (char in str1 and char in str2):
            same_char_count += min(str1.count(char), str2.count(char))
    return same_char_count

# This function returns the number of individual characters both strings have
def same_unique_char_count(str1, str2):
    if (len(str1) == 0 or len(str2) == 0):
        return 0
    if (str1 == str2):
        return len(str1)
    str1 = str1.lower()
    str2 = str2.lower()
    if (len(str1) > len(str2)): 
        longer_str = str1
        shorter_str = str2
    else:
        longer_str = str2
        shorter_str = str1
    same_char_count = 0
    for char in alphabet:
        if (char in str1 and char in str2): 
            same_char_count += 1
    return same_char_count

# This function returns the longest sequence of characters
# the strings have in common without string manipulation
def longest_same_char_sequence_uncut(str1, str2):
    if (len(str1) == 0 or len(str2) == 0):
        return 0
    if (str1 == str2):
        return len(str1)
    if all_to_lower_case: 
        str1 = str1.lower()
        str2 = str2.lower()
    if (same_unique_char_count(str1, str2) == 0):
        return 0
    if (len(str1) > len(str2)): 
        longer_str = str1
        shorter_str = str2
    else:
        longer_str = str2
        shorter_str = str1
    longer_str = add_space_to_both_ends(longer_str)
    longest_same_char_sequence = 0
    for index in range(len(longer_str) - len(shorter_str)):
        same_char_count = 0
        i = 0
        for x in range(index, index + len(shorter_str)):
            if (longer_str[x] == shorter_str[i]):
                same_char_count += 1
                if (same_char_count > longest_same_char_sequence):
                    longest_same_char_sequence = same_char_count
            else:
                same_char_count = 0
            i += 1
    return longest_same_char_sequence

# This function returns the maximum number of characters 
# strings can have at the same indexes just by moving the
# shorter string along the longer one
def same_chars_at_indexes_uncut(str1, str2):
    if (len(str1) == 0 or len(str2) == 0):
        return 0
    if (str1 == str2):
        return len(str1)
    if all_to_lower_case: 
        str1 = str1.lower()
        str2 = str2.lower()
    if (same_unique_char_count(str1, str2) == 0):
        return 0
    if (len(str1) > len(str2)): 
        longer_str = str1
        shorter_str = str2
    else:
        longer_str = str2
        shorter_str = str1
    longer_str = add_space_to_both_ends(longer_str)
    highest_same_char_count = 0
    for index in range(len(longer_str) - len(shorter_str)):
        same_char_count = 0
        i = 0
        for x in range(index, index + len(shorter_str)):
            if (longer_str[x] == shorter_str[i]):
                same_char_count += 1
            i += 1
        if (same_char_count > highest_same_char_count):
            highest_same_char_count = same_char_count
    return highest_same_char_count

# This function returns the information of preceding function
# as a proportional value
def same_chars_at_indexes_proportion_uncut(str1, str2):
    if (len(str1) == 0 or len(str2) == 0):
        return 0.0
    if (str1 == str2):
        return 1.0
    if all_to_lower_case: 
        str1 = str1.lower()
        str2 = str2.lower()
    if (same_unique_char_count(str1, str2) == 0):
        return 0.0
    if (len(str1) > len(str2)): 
        longer_str = str1
        shorter_str = str2
    else:
        longer_str = str2
        shorter_str = str1
    return float(same_char_count(str1, str2))/float(len(longer_str))

# This function returns the sum of limit exceeding sequences
# of characters the strings have in common
def sum_of_same_char_sequences(str1, str2, seq_min_length):
    if (len(str1) == 0 or len(str2) == 0):
        return 0
    if (str1 == str2):
        return len(str1)
    if all_to_lower_case: 
        str1 = str1.lower()
        str2 = str2.lower()
    if (same_unique_char_count(str1, str2) == 0):
        return 0
    if (len(str1) > len(str2)): 
        longer_str = str1
        shorter_str = str2
    else:
        longer_str = str2
        shorter_str = str1
    longer_str = add_space_to_both_ends(longer_str)
    sum_of_sequences = 0
    longest_same_char_sequence = 0
    if (seq_min_length <= 0 or seq_min_length == ""):
        seq_min_length = 1
    while(longest_same_char_sequence == 0 or longest_same_char_sequence > seq_min_length):
        longest_same_char_sequence = 0    
        for index in range(len(longer_str) - len(shorter_str)):
            same_char_count = 0
            i = 0
            for x in range(index, index + len(shorter_str)):
                if (longer_str[x] == shorter_str[i] and longer_str[x] != ' '):
                    same_char_count += 1
                    if (same_char_count > longest_same_char_sequence):
                        longest_same_char_sequence = same_char_count
                        lscs_index = x - longest_same_char_sequence + 1
                else:
                    same_char_count = 0
                i += 1
        if (longest_same_char_sequence > seq_min_length):
            sum_of_sequences += longest_same_char_sequence
        to_be_removed = longer_str[lscs_index:lscs_index + longest_same_char_sequence]
        start_part = longer_str[:lscs_index]
        end_part = longer_str[lscs_index + longest_same_char_sequence:]
        # print "Out:  |" + to_be_removed + '|'
        longer_str = add_space_to_the_middle(start_part, end_part)
        # print "Left: |" + longer_str + '|'
        short_part_lscs_index = shorter_str.find(to_be_removed)
        shorter_str = shorter_str[:short_part_lscs_index] + shorter_str[short_part_lscs_index + longest_same_char_sequence:]
        if (len(shorter_str) < seq_min_length):
            break
    return sum_of_sequences

# This function returns the information of preceding function
# as a proportional value
def sum_of_same_char_sequences_proportion(str1, str2, seq_min_length):
    if (len(str1) == 0 or len(str2) == 0):
        return 0.0
    if (str1 == str2):
        return 1.0
    if all_to_lower_case: 
        str1 = str1.lower()
        str2 = str2.lower()
    if (same_unique_char_count(str1, str2) == 0):
        return 0.0
    if (len(str1) > len(str2)): 
        longer_str = str1
        shorter_str = str2
    else:
        longer_str = str2
        shorter_str = str1
    return float(sum_of_same_char_sequences(str1, str2, seq_min_length))/float(len(longer_str))

