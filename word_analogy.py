#!/usr/bin/python3
#
# Comp Ling PROJECT #5
# May 2019
# Author: Kelsey Broadfield kelseybroadfield@bennington.edu
#

import sys, os
import numpy


# dictionary[word] = numpy.array(list of #, dtype = float)

model_path = sys.argv[1]
test_set = sys.argv[2]
output_dir = sys.argv[3]
eval_file = sys.argv[4]
should_normalize = int(sys.argv[5])
similarity_type = int(sys.argv[6])

# creates dictionary and reads the vector into a dictionary
vec2dic = {}


def Vec2Dic(line):
    parts = line.split(' ')
    lengthy = len(parts)
    vec2dic[parts[0]] = numpy.array(parts[1:lengthy], dtype=float)


with open(model_path, 'r') as open_file:
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
    this_d_vec = vec2dic[C] + vec2dic[B] - vec2dic[A]
    trifecta = 'A' + ' ' + 'B' + ' ' + 'C'
    return this_d_vec, trifecta


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
    distance = sum(abs(d_vec-compare_vec))
    c = distance
    return c


def cosine_finder(d_vec, compare_vec):
    c = d_vec.dot(compare_vec)
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
for file in os.listdir(test_set):
    if file.startswith('.'):
        continue
    if not file.endswith('.txt'):
        continue
    filepath = os.path.join(test_set, file)
    output_path = os.path.join(output_dir, file)
    with open(filepath, 'r') as open_file:
        with open(output_path, 'w') as open_output:
            if should_normalize == 0:
                for line in open_file.readlines():
                        normalized = to_normalize(line)
                        print(normalized)
                        this_d_vec, trifecta = analogizer(normalized)
                        if similarity_type == 0:
                            D = comparer0(this_d_vec, vec2dic)
                        if similarity_type == 1:
                            D = comparer1(this_d_vec, vec2dic)
                        if similarity_type == 2:
                            D = comparer2(this_d_vec, vec2dic)
                            open_output.write(trifecta + ' ' + D)
                            correct_counter = 0
                            if D == this_d_vec:
                                correct_counter += 1
                            with open(eval_file, 'w') as this:
                                this.write(str(correct_counter))
                                this.close()
                if should_normalize == 1:
                    for line in open_file.readlines():
                        this_d_vec, trifecta = analogizer(line)
                        if similarity_type == 0:
                            D = comparer0(this_d_vec, vec2dic)
                        if similarity_type == 1:
                            D = comparer1(this_d_vec, vec2dic)
                        if similarity_type == 2:
                            D = comparer2(this_d_vec, vec2dic)
                            open_output.write(trifecta + ' ' + D)
                        correct_counter = 0
                        if D == this_d_vec:
                            correct_counter += 1
                        with open(eval_file, 'w') as this:
                            this.write(str(correct_counter))
                            this.close()



                # compare this D to original D
                # if the D's are the sme, increment correct counter
                #record file name and accuracy, correct divided by all for each file in the eval file
                #save to accuracy string or dictionary 



