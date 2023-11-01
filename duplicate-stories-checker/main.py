# -*- coding: utf-8 -*-
import os
import json
import time
import traceback
from difflib import SequenceMatcher

similarities = []


def similarity_ratio(string1, string2):
    return SequenceMatcher(None, string1, string2).ratio()


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
        tamilsurangam_directory = path + "/tamilsurangam"
        tamilsurangam_directories = os.listdir(tamilsurangam_directory)
        siruvarmalar_contents = load_json(path + "/siruvarmalar.json")
        for index, siruvarmalar_story in enumerate(siruvarmalar_contents):
            print(
                f"--- Siruvarmalar Story: {siruvarmalar_story['story_title']} --")
            for index, tamilsurangam_file in enumerate(tamilsurangam_directories):
                print(
                    f"Checking Tamilsurangam Stories: {tamilsurangam_file}...")
                tamilsurangam_contents = load_json(
                    tamilsurangam_directory + f"/{tamilsurangam_file}")
                for index, tamilsurangam_story in enumerate(tamilsurangam_contents):
                    ratio = similarity_ratio(
                        siruvarmalar_story["story"], tamilsurangam_story["story"])
                    if (ratio > 0.5):
                        print(siruvarmalar_story["story_title"], siruvarmalar_story["story_id"],
                              tamilsurangam_story["story_title"], tamilsurangam_story["story_id"])
                        similarities.append({
                            "siruvarmalar_story":  siruvarmalar_story["story_title"],
                            "siruvarmalar_id": siruvarmalar_story["story_id"],
                            "tamilsurangam_story": tamilsurangam_story["story_title"],
                            "tamilsurangam_id": tamilsurangam_story["story_id"],
                            "ratio": ratio
                        })
                    time.sleep(0.5)
        save_as_json(path + "/similarities.json", similarities)
    except Exception:
        dump_error()


runner()
