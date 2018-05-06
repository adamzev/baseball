''' file manager handles loading and saving files
    loads and saves json data
    saves csv data
'''
import glob
import json
import os
import errno

from libs.query import Query as q

import libs.func as func


def save_file(this_file):
    file_name = this_file['file_name']
    save_json(this_file, file_name)


def select_and_load_json_file(files):
    n = 1
    for this_file in files:
        file_data = load_json(this_file)
        print("{}) {}".format(n, file_data["friendly_name"]))
        n += 1
    file_num = q.query_int("Select a file number: ", None, 1, n - 1)
    data = load_json(files[file_num - 1])
    return data


def get_json_file_data(folder, name, creation_function):
    ''' lists and allows selection of all json files in a folder
    name is the type of save file this is (spec, engine, etc)
    if no file are available or if the user chooses, executes creation_function
    to create a new save file '''
    files = glob.glob("{}/*.json".format(folder))
    if len(files) < 1:  # if there are no spec files, you need to create one
        data = creation_function()
    else:
        create_new = q.query_yes_no("Do you want to create a new {} file? ".format(name), "no")
        if create_new:
            data = creation_function()
        else:
            data = select_and_load_json_file(files)

    func.pretty_json(data)
    return data


def create_csv(data, fileName):
    ''' creates a csv file '''
    with open(fileName, 'w') as outfile:
        outfile.write(data)


def update_csv(data, fileName):
    ''' appends data to a csv file '''
    with open(fileName, 'a') as outfile:
        outfile.write(data)


def make_dir(fileName):
    ''' make a directory '''
    if not os.path.exists(os.path.dirname(fileName)):
        try:
            os.makedirs(os.path.dirname(fileName))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def ask_to_save(data, question="Would you like to save? "):
    ''' queries if the user wants to save a file
        "data" is a dictionary with the key "file_name" which is
        the name and location to save the data
    '''
    save_this_data = q.query_yes_no(question, "yes")
    if save_this_data:
        save_file(data)


def save_json(data, fileName):
    ''' creates a json file (overwriting any prior files) '''
    make_dir(fileName)
    with open(fileName + ".json", "w") as outfile:
        json.dump(data, outfile)


def load_json(fileName):
    ''' loads the file with the given file name and returns the json data '''
    with open(fileName) as data_file:
        return json.load(data_file)
