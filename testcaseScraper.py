#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import re

import requests

import config


class test_file:
    sample_num = 0

    def __init__(self, file_path, file_name):
        os.makedirs(file_path, exist_ok=True)
        self.test_file = open(os.path.join(file_path, file_name), 'w')
        self.test_file.write(config.initial)

    def add_testcase(self, sample_input, sample_output):
        self.sample_num += 1
        self.test_file.write(config.sample_format.format(
            sample_number = str(self.sample_num),
            input = sample_input,
            output = sample_output
        ))

    def close(self):
        self.test_file.write(config.last)
        self.test_file.close()

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
        print("Connected...")

        for target in config.target:
            # open output file
            testfile = test_file(target[1], target[2])

            # get sample texts
            target_url = "https://atcoder.jp/contests/" + opt.contest_id + "/tasks/" + opt.contest_id + target[0]
            task = s.get(target_url).text
            samples = extract_samples(task)

            # save samples
            for (sample_input, sample_output) in samples:
                testfile.add_testcase(sample_input, sample_output[:-1])

            testfile.close()
            print("  Complete: " + opt.contest_id + target[0])


# HTMLから入出力を引っ張り出す
# @param html: HTMLを突っ込む
# @return [[sample_input, sample_output], [..], []..]
def extract_samples(html):
    pattern = re.compile('<h3>[入出]力例 \d</h3><pre>([ \-\+\w\r\n]+)[\n\r]</pre>')
    return make_n_row_list(pattern.findall(html), 2)


# 新しいディレクトリにファイルを作成、保存する
# @param dir_path: 保存先ディレクトリ名, filename: ファイル名, content: 内容
def save_file(dir_path, filename, content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(content)


# リストを多次元リスト化する
# @param in_list: 入力リスト, n: 1行当たりの列数
# @return ?xnリスト
def make_n_row_list(in_list, n):
    return [in_list[i : i + n] for i in range(0, len(in_list), n)]


if __name__ == "__main__":
    main()
