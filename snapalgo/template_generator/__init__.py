import pyperclip
import os

def load_template(template_name):
    curr_path = os.path.dirname(__file__)
    file_path = os.path.join(curr_path, './' + template_name + '.py')
    template_code = ""
    with open(file_path, 'r') as f:
        template_code = f.read()

    f.close()
    pyperclip.copy(template_code)
    return template_code

def list_available_templates():
    arr = []
    arr.append('union_find')
    arr.append('trie')
    arr.append('segment_tree')
    arr.append('radix_sort')
    arr.append('preorder')
    arr.append('postorder')
    arr.append('inorder')
    print(arr)
    return arr