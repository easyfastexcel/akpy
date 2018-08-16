import os
import yaml
import subprocess

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from akpy.str_mgmt import *


def clear_dir(dir_path):
    for f in os.listdir(dir_path):
        os.remove(os.path.join(dir_path, f))


def set_empty_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        clear_dir(dir_path)


def get_yaml_data(yaml_dir_path):
    with open(yaml_dir_path) as f:
        data = yaml.safe_load(f)
    return data


def confirm_manual_file_selection(file_name='report', source='the web', step_numb=''):
    root = Tk()
    root.withdraw()

    title = '' + step_numb + 'Manual file selection?'
    message = '' + step_numb + 'Do you have have a recently downloaded ' + file_name + ' from ' + source + '?\n\n\n' + \
              'YES, I will select the file from my PC\n\n' \
              'NO, I don\'t have a recently downloaded ' + file_name + ' from ' + source
    return messagebox.askquestion(title, message)


def confirm_file_requirement(file_name='report', submsg='', step_numb=''):
    root = Tk()
    root.withdraw()

    title = '' + step_numb + 'File Requirement: ' + file_name
    if len(submsg) > 0:
        submsg = '\n           ' + submsg
    message = '' + step_numb + 'The following file is required to complete the next step in the automated process: ' + \
              '\n\n          ' + file_name + submsg + '\n\n\n' + \
              'YES, I have it and will select the file from my PC\n\n' \
              'NO, I don\'t have the required file (exit process)'
    return messagebox.askquestion(title, message)


def get_user_selected_file_path(initial_dir="/",
                                title="Select file"):
    root = Tk()
    root.withdraw()

    # messagebox.showinfo(title, intro_msg)

    response_yn = False
    while not response_yn:
        root.filename = filedialog.askopenfilename(initialdir=initial_dir,
                                                   title=title)
        # ,filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

        if not root.filename:
            sys.exit("User invoked cancel")

        msg = "You selected the file at the following file path.  Is this correct?"
        response_yn = messagebox.askyesno("Selected file path",
                                          msg+"\n\n"+root.filename)

    return root.filename


def ensure_output_dir(dir_name='output'):
    output_dirpath = os.path.join(os.path.expanduser('~'),'Desktop', dir_name)
    if not os.path.exists(output_dirpath):
        os.mkdir(output_dirpath)
        

def verify_file_extension(target_dirpath, acceptable_extensions):
    extension_start = last_substring_position('.', target_dirpath)
    if target_dirpath[extension_start:] in acceptable_extensions:
        return True
    else:
        return False


def open_explorer(path):
    str_filebrowser_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([str_filebrowser_path, path])
    elif os.path.isfile(path):
        subprocess.run([str_filebrowser_path, '/select,', os.path.normpath(path)])


if __name__ == "__main__":
    pass
