import re
import lzma


def read_file(filepath, mode = 'r'): # rb for raw binary
    f = open(filepath, mode)# encoding = encoding)
    file_content = ""
    try:
        file_content = f.read()
    finally:
        f.close()
    return file_content


def tokenize(character_seq, delimiter, remove_chars = None):
    if remove_chars.len is not None:
        for i in remove_chars:
            re.sub(i, "", character_seq)
    tokens = character_seq.split(delimiter)
    return tokens

def read_compressed_lzma_file(character_seq, output_file_path= None):
    lzma.open(character_seq, mode="rb")
    lzma.LZMAFile(filename=character_seq, mode="r")