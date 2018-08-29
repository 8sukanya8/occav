import os
from load import read_file


def author_dictionary (corpus_token_path, correct_author_path):
    token_files = os.listdir(corpus_token_path)
    correct_author = read_file(correct_author_path).split("\n")
    author_name_token_dict = {}
    for i in range(0, correct_author.__len__()):
        if correct_author[i] not in author_name_token_dict.keys():
            author_name_token_dict[correct_author[i]] = [token_files[i]]
            #print(author_name_token_dict[french_correct_author[i]])
        else:
            existing_token_files = author_name_token_dict[correct_author[i]]
            if existing_token_files is not None:
                author_name_token_dict[correct_author[i]].append(token_files[i])
    return author_name_token_dict

