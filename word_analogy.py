#!/usr/bin/python3
#
# Comp Ling PROJECT #5
# May 2019
# Author: Kelsey Broadfield kelseybroadfield@bennington.edu
#

import sys, os
import numpy


# dictionary[word] = numpy.array(list of #, dtype = float)

input_one = sys.argv[1]
input_two = sys.argv[2]
input_three = sys.argv[3]

# creates dictionary and reads the vector into a dictionary
vec2dic = {}


def Vec2Dic(line):
    parts = line.split(' ')
    lengthy = len(parts)
    vec2dic[parts[0]] = numpy.array(parts[1:lengthy], dtype=float)


with open(input_one, 'r') as open_file:
    lines = open_file.readlines()
    for x in lines:
        Vec2Dic(x)
open_file.close()


# function that does the A, B, C, D thing
# creates a d_vec for every file in the Google Test Set
def analogizer(line):
    word_list = line.split()
    A = word_list[0]
    B = word_list[1]
    C = word_list[2]
    d_vec = vec2dic[C] + vec2dic[B] - vec2dic[A]
    return d_vec


# Euclydian Distance
# d_vec and a vector from vec2dic: compare, save the smallest one
# for every line in every file, you find the best option for D based on
# a comparison between the created d_vec for the file and the actual vectors
# points are lists of numbers, sq root of A2 + B2 = C
# min
def euclidian_finder(d_vec, compare_vec):
    to_sqrt = (numpy.square(d_vec-compare_vec))
    c = numpy.sqrt(to_sqrt)
    return c


def manhattan_finder(d_vec, compare_vec):
    distance = abs(d_vec[1] - compare_vec[1]) + abs(d_vec[2] - compare_vec[2])
    c = distance
    return c


def cosine_finder(d_vec, compare_vec):
    return c


# comparison for Euclydian AND Manhattan (both care about largest C)
def comparer0(d_vec, vec2dic):
    closest_distance = 500
    closest_word = None
    for word in vec2dic:
        this_value = vec2dic.get(word)
        this_c = euclidian_finder(d_vec, this_value) # change our with manhattan finder
# euclydian function #compare word vector to dvec using euclydian
        if this_c < closest_distance:
            closest_distance = this_c
            closest_word = word
    return closest_word
# care about the word that is closest, closest distance (c). euclydian, smallest c, cosine largest c

# manhattan
def comparer1(d_vec, vec2dic):
    closest_distance = 500
    closest_word = None
    for word in vec2dic:
        this_value = vec2dic.get(word)
        this_c = manhattan_finder(d_vec, this_value)
        if this_c < closest_distance:
            closest_distance = this_c
            closest_word = word
    return closest_word

# comparison for cosine
def comparer2(d_vec, vec2dic):
    closest_distance = 500
    closest_word = None
    for word in vec2dic:
        this_value = vec2dic.get(word)
        this_c = cosine_finder(d_vec, this_value)
        if this_c > closest_distance:
            closest_distance = this_c
            closest_word = word
    return closest_word

# RANDOM NOTES: ignore
    #if you use numpy
    # this_d_vec = vec2dic[C] + vec2dic[B] - vec2dic[A]

        # D_vec[0]= C[0]+B[0]-A[0]
    # for every 300 numbers in vector, add to list to equal D_vec
    # access same index of all three vectors


def to_normalize(d_vec):
    to_square = 0
    for y in range(len(d_vec)):
        to_square += numpy.square(y)
    magnitude = numpy.sqrt(to_square)
    for vec in d_vec:
        new_vec = numpy.divide(vec, magnitude)
        vec = new_vec
        return vec


# reads directory files
for file in os.listdir(input_two):
    if file.startswith('.'):
        continue
    if not file.endswith('.txt'):
        continue
    filepath = os.path.join(input_two, file)
    with open(filepath, 'r') as open_file:
        for line in open_file.readlines():
            this_d_vec = analogizer(line)
            # if it needs to be normalized, add normalize function HERE before comparers, add vec to first parameter
            comparer0(this_d_vec, vec2dic)
            comparer1(this_d_vec, vec2dic)
            comparer2(this_d_vec, vec2dic)


# NOTES
#for filename in os.listdir(dir_name):
    # if file_name.startswith('.')
        #continue
    #if not filename.endswith('.txt'):
        #continue
    #filepath = os.path.join(dir_name, filename)
    #with open(filepath, 'r') as open_file
        #for line in open_file.readlines():
            #print(line)

