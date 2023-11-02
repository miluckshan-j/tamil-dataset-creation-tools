import os
import json
import time
import traceback


def load_json(file):
    with open(file, "r", encoding="utf-8") as infile:
        file_contents = json.load(infile)
        return file_contents


def save_as_json(file, content):
    with open(file, "w", encoding="utf-8") as outfile:
        json.dump(content, outfile, ensure_ascii=False, indent=2)


def dump_error():
    with open("error.log", "a") as log:
        log.write(f"{time.ctime()}\n")
        log.write(traceback.format_exc())


def is_in_list(key, value, list):
    for index, list_item in enumerate(list):
        if list_item[key] == value:
            return True
    return False


def runner():
    try:
        path = os.getcwd()
        siruvarmalar_contents = load_json(path + "/siruvarmalar-input.json")
        similarities_contents = load_json(path + "/similarities.json")
        # output = siruvarmalar_contents
        for index, siruvarmalar_story in enumerate(siruvarmalar_contents):
            if (is_in_list('siruvarmalar_id', siruvarmalar_story["story_id"], similarities_contents)):
                siruvarmalar_contents.remove(siruvarmalar_story)
        save_as_json(path + "/siruvarmalar.json", siruvarmalar_contents)
    except Exception:
        dump_error()


runner()
