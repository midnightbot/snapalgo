import pyperclip
import os

def union_find():
    curr_path = os.path.dirname(__file__)
    file_path = os.path.join(curr_path, './union_find.py')
    union_find_code = ""
    with open(file_path, 'r') as f:
        union_find_code = f.read()

    f.close()
    pyperclip.copy(union_find_code)
    return union_find_code


def trie():
    curr_path = os.path.dirname(__file__)
    file_path = os.path.join(curr_path, './trie.py')
    trie_code = ""
    with open(file_path, 'r') as f:
        trie_code = f.read()

    f.close()
    pyperclip.copy(trie_code)
    return trie_code
