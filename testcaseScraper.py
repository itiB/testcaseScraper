#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import re

import requests

import config


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
            'username': config.username,
            'password': config.password,
            'csrf_token': token,
        }

        r = s.post("https://atcoder.jp/login", postdata)
        # print('login_status:'+str(r.status_code))
        # TODO: Error check for Access forbidden etc...

        for target in config.target:
            target_url = "https://atcoder.jp/contests/" + opt.contest_id + "/tasks/" + opt.contest_id + target[0]
            task = s.get(target_url)
            save_file(target[1], target[2], task.text)

# 新しいディレクトリにファイルを作成、保存する
# @param dir_path: 保存先ディレクトリ名, filename: ファイル名, content: 内容
def save_file(dir_path, filename, content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(content)

if __name__ == "__main__":
    main()
