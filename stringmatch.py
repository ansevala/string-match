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
# version 1.0.1.0
# 2017-03-16
#
# Python functions for evaluating how well two strings match each other
#

all_to_lower_case = True # "True" or "False" up to you

import sys

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 
    'v', 'w', 'x', 'y', 'z', 'å', 'ä', 
    'ö'
    ] # The alphabet looks like this where I live; feel free to change it

# This function prints the rows of a matrix
def print_matrix(matrix):
    for row in matrix:
        print row

# This function returns a character sequence length matrix
def char_sequence_length_matrix(l_str, s_str):
    csl_matrix = []
    char_comparison = []
    i = 0
    for j in range(len(s_str)):
        if (l_str[0] == s_str[i]):
            char_comparison.append(1)
        else:
            char_comparison.append(0)
        i += 1
    csl_matrix.append(char_comparison)
    for index in range(1, len(l_str)):
        char_comparison = []
        i = 0
        for j in range(len(s_str)):
            if (l_str[index] == s_str[i]):
                if (i != 0):
                    current_length = csl_matrix[index - 1][i - 1]
                    char_comparison.append(current_length + 1)
                else:
                    char_comparison.append(1)
            else:
                char_comparison.append(0)
            i += 1
        csl_matrix.append(char_comparison)
    return csl_matrix

# This function returns the greatest value of a list
def greatest_of_a_list(lst):
    if (lst == None):
        return 0
    if (len(lst) == 0):
        return 0
    greatest = -sys.maxint
    for value in lst:
        if (value > greatest):
            greatest = value
    return greatest

# This function returns the greatest value of a matrix
def greatest_of_a_matrix(matrix):
    if (matrix == None):
        return 0
    if (len(matrix) == 0):
        return 0
    greatest = -sys.maxint
    i = 0
    for row in matrix:
        if(greatest_of_a_list(row) > greatest):
            greatest = greatest_of_a_list(row) 
        i += 1
    return greatest

# This function returns the number of characters both strings have allowing
# multiple occurances
def same_char_count(str1, str2):
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
def longest_same_char_sequence(str1, str2):
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
    longest_same_char_sequence = 0
    matrix = char_sequence_length_matrix(longer_str, shorter_str)
    # print_matrix(matrix)
    longest_same_char_sequence = greatest_of_a_matrix(matrix)
    return longest_same_char_sequence

# This function returns the maximum number of characters 
# strings can have at the same indexes just by moving the
# shorter string along the longer one
def same_chars_at_indexes(str1, str2):
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
    highest_same_char_count = 0
    matrix = char_sequence_length_matrix(longer_str, shorter_str)
    # print_matrix(matrix)
    i = 0
    for element in matrix[0]:
        j = 0
        count = 0
        while (i < len(matrix[0])):
            if (matrix[i][j] != 0):
                count += 1
            if (count > highest_same_char_count):
                highest_same_char_count = count
            i += 1
            j += 1
    j = 0
    for element in matrix:
        i = 0
        count = 0
        while (j < len(matrix)):
            if (matrix[i][j] != 0):
                count += 1
            if (count > highest_same_char_count):
                highest_same_char_count = count
            i += 1
            j += 1
    return highest_same_char_count

# This function returns the information of preceding function
# as a proportional value
def same_chars_at_indexes_proportion(str1, str2):
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
    sum_of_sequences = 0
    matrix = char_sequence_length_matrix(longer_str, shorter_str)
    # print_matrix(matrix)
    if (seq_min_length <= 0 or seq_min_length == ""):
        seq_min_length = 1
    longest_same_char_sequence = greatest_of_a_matrix(matrix)
    while (longest_same_char_sequence > seq_min_length):
        longest_same_char_sequence = greatest_of_a_matrix(matrix)
        for index in range(longest_same_char_sequence - 1, len(matrix)):
            if longest_same_char_sequence in matrix[index]:
                if (longest_same_char_sequence >= seq_min_length):
                    sum_of_sequences += longest_same_char_sequence
                matrix = matrix[:index-longest_same_char_sequence + 1] + matrix[index + 1:]
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
