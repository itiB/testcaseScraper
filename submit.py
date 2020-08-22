#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import re
import sys
import os
import requests

sys.path.append(os.path.abspath(".."))

import setting

def main():
    usage = "usage: %(prog)s problem_id"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('contest_id')
    opt = parser.parse_args()

    # Session Start
    with requests.Session() as s:
        # get csrf_token
        html = s.get('https://atcoder.jp/login').text

        pattern = re.compile('<input type="hidden" name="csrf_token" value="(.+)" />')
        result = pattern.findall(html)
        token = result[0].replace('&#43;', '+')

        postdata = {
            'username': setting.username,
            'password': setting.password,
            'csrf_token': token,
        }

        r = s.post("https://atcoder.jp/login", postdata)
        r.raise_for_status()
        # print('login_status:'+str(r.status_code))
        # TODO: Error check for Access forbidden etc...
        print("Connected...")

        with open("./src/main.rs", mode="r") as f:
            source_code = f.read()+'\n'  # ファイル終端まで全て読んだデータを返す
            target_url = "https://atcoder.jp/contests/{contest}/submit".format(
                contest = opt.contest_id
            )
            submit_info = {
                "data.TaskScreenName": opt.contest_id + "_b",
                "csrf_token": token,
                "data.LanguageId": 4050, # Rust (1.42.0),
                "sourceCode": source_code
            }
            result = s.post(target_url, data=submit_info)

            if result.status_code == 200:
                print("Submitted!")
            else:
                result.raise_for_status()

if __name__ == "__main__":
    main()

