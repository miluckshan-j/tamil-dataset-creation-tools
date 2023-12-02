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
        tamilsurangam_input_directory = path + "/tamilsurangam-inputs"
        tamilsurangam_directories = os.listdir(tamilsurangam_input_directory)
        for index, tamilsurangam_file in enumerate(tamilsurangam_directories):
            similarities = []
            print(
                f"Tamilsurangam Story: {tamilsurangam_file}...")
            tamilsurangam_contents = load_json(
                tamilsurangam_input_directory + f"/{tamilsurangam_file}")
            for index, tamilsurangam_story in enumerate(tamilsurangam_contents):
                print(tamilsurangam_story["story_id"])
                for index, tamilsurangam_checking_file in enumerate(tamilsurangam_directories):
                    if (tamilsurangam_file != tamilsurangam_checking_file):
                        print(
                            f"Tamilsurangam Checking Story: {tamilsurangam_checking_file}...")
                        tamilsurangam_checking_contents = load_json(
                            tamilsurangam_input_directory + f"/{tamilsurangam_checking_file}")
                        for index, tamilsurangam_checking_story in enumerate(tamilsurangam_checking_contents):
                            ratio = similarity_ratio(
                                tamilsurangam_story["story"], tamilsurangam_checking_story["story"])
                            if (ratio > 0.5):
                                print(
                                    f"{tamilsurangam_file} | {tamilsurangam_checking_file} | {tamilsurangam_story['story_id']} | {tamilsurangam_checking_story['story_id']} | {tamilsurangam_story['story_title']} | {tamilsurangam_checking_story['story_title']}")
                                similarities.append({
                                    "tamilsurangam_file": tamilsurangam_file,
                                    "tamilsurangam_checking_file": tamilsurangam_checking_file,
                                    "tamilsurangam_story_id": tamilsurangam_story["story_id"],
                                    "tamilsurangam_story": tamilsurangam_story['story_title'],
                                    "tamilsurangam_checking_story_id": tamilsurangam_checking_story['story_id'],
                                    "tamilsurangam_checking_story": tamilsurangam_checking_story['story_title']

                                })
            file_name = tamilsurangam_file.split(".")
            save_as_json(
                path + f"/{file_name[0]}-similarities.json", similarities)
    except Exception:
        dump_error()


runner()
