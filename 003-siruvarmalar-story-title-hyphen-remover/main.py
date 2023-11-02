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


def runner():
    try:
        path = os.getcwd()
        siruvarmalar_contents = load_json(path + "/siruvarmalar-input.json")
        for index, siruvarmalar_story in enumerate(siruvarmalar_contents):
            title = siruvarmalar_story["story_title"].split("-")
            if (len(title) == 1):
                title = title[0].strip()
            elif (len(title) > 1):
                del title[0]
                formatted_title = []
                for index, title_item in enumerate(title):
                    formatted_title.append(title_item.strip())
                title = ' '.join(formatted_title)
            siruvarmalar_story["story_title"] = title
        save_as_json(path + "/siruvarmalar.json", siruvarmalar_contents)
    except Exception:
        dump_error()


runner()
