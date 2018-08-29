from load import read_file
from printFormat import printList
import os
import re
import lzma
import math
from CorpusProcessor import author_dictionary


def CBC(character_seq_x, character_seq_y):
    character_seq_xy = character_seq_x + character_seq_y
    compressed_seq_x = lzma.compress(character_seq_x)
    c_x = compressed_seq_x.__sizeof__()
    compressed_seq_y = lzma.compress(character_seq_y)
    c_y = compressed_seq_y.__sizeof__()
    compressed_seq_xy = lzma.compress(character_seq_xy)
    c_xy = compressed_seq_xy.__sizeof__()
    numerator = c_x + c_y - c_xy
    denominator = math.sqrt(c_x * c_y)
    cos_xy = 1 - (numerator/denominator)
    return cos_xy


def occav(true_author, candidate_author, unknown_author_file_path, known_author_files, token_path):
    unknown_author_doc_contents = read_file(token_path + "/"+ unknown_author_file_path, 'rb')
    s_min = 1
    s_min_file_path = ""
    for file in known_author_files:
        known_author_doc_path = token_path + "/" + file
        known_author_doc_contents = read_file(known_author_doc_path, 'rb')
        cbc = CBC(unknown_author_doc_contents, known_author_doc_contents)
        print("cbc = %f s_min = %f" % (cbc, s_min))
        if s_min > cbc:
            s_min = cbc
            s_min_file_path = file
    y_min_doc_contents = read_file(token_path + "/" + s_min_file_path, 'rb')
    cbc_sum_known_authors = 0
    other_token_files = [file for file in known_author_files if file!= s_min_file_path]
    for file in other_token_files:
        known_author_doc_contents = read_file(token_path + "/" + file, 'rb')
        # print(file3)
        cbc_y = CBC(y_min_doc_contents, known_author_doc_contents)
        print("file= ", file, "cbc_y =",cbc_y)
        cbc_sum_known_authors = cbc_sum_known_authors + cbc_y
    s_avg = cbc_sum_known_authors / (other_token_files.__len__())
    result = ""
    if s_min < s_avg:
        result = "accepted"
        # print("Authorship is accepted")
    else:
        result = "rejected"
        # print("Authorship is rejected")
    print("File = ", unknown_author_file_path, ", s_avg = %f, s_min = %f" % (s_avg, s_min), ", True Author = ", true_author,
          ", Candidate Author = ", candidate_author, ", Authorship ", result)


def evaluate_occav(author_dict, token_path):
    for true_author in author_dict.keys():
        unknown_token_files = author_dict[true_author]
        # candidate_authors = [key for key, value in french_author_dict.items() if key !=true_author]
        for unknown_token_file in unknown_token_files:
            for candidate_author in author_dict.keys():
                known_token_files = []
                if (candidate_author == true_author):
                    known_token_files = [file for file in author_dict[candidate_author] if
                                         file != unknown_token_file]
                else:
                    known_token_files = author_dict[candidate_author]
                occav(true_author, candidate_author, unknown_token_file, known_token_files, token_path)

#french_corpus_token_path = '/Users/sukanyanath/Documents/PhD/Datasets/French/Token'
#french_correct_author_path = '/Users/sukanyanath/Documents/PhD/Datasets/French/Author.txt'
#french_author_dict = author_dictionary(french_corpus_token_path, french_correct_author_path)
#evaluate_occav(french_author_dict, french_corpus_token_path)

english_corpus_token_path = '/Users/sukanyanath/Documents/PhD/Datasets/English/Token'
english_correct_author_path = '/Users/sukanyanath/Documents/PhD/Datasets/English/Author.txt'
english_author_dict = author_dictionary(english_corpus_token_path, english_correct_author_path)

evaluate_occav(english_author_dict, english_corpus_token_path)


