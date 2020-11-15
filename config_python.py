username = "AtCoderのユーザ名を入れる"
password = "AtCoderのパスワードを入れる"

# 保存したいファイルのルートディレクトリ
root_dir = "~/"

# 保存したい問題, 保存先ディレクトリ, 保存ファイル名
target = [['_a', root_dir + "a/", "sample_inputs.py"],
          ['_b', root_dir + "b/", "sample_inputs.py"],
          ['_c', root_dir + "c/", "sample_inputs.py"],
          ['_d', root_dir + "d/", "sample_inputs.py"],
          ['_e', root_dir + "e/", "sample_inputs.py"]]

# 出力フォーマットを指定
## ファイル最初に書く宣言等
initial = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main import main
import unittest
import sys
import io

class TestCases(unittest.TestCase):
'''

sample_format = '''
    def test_{sample_number}(self):
           stub_stdin(self, \'\'\'{input}
\'\'\')
           stub_stdouts(self)
           main()
           self.assertEqual(sys.stdout.getvalue(), \"{output}\\n\")
'''

## ファイル終わりに書く宣言等
last = """

class StringIO(io.StringIO):
    def __init__(self, value=''):
        value = value.encode('utf8', 'backslashreplace').decode('utf8')
        io.StringIO.__init__(self, value)

    def write(self, msg):
        io.StringIO.write(self, msg.encode(
            'utf8', 'backslashreplace').decode('utf8'))


def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = StringIO(inputs)

def stub_stdouts(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = StringIO()
    sys.stdout = StringIO()


if __name__ == '__main__':
    unittest.main()
"""