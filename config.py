username = "AtCoderのユーザ名を入れる"
password = "AtCoderのパスワードを入れる"

# 保存したいファイルのルートディレクトリ
root_dir = "~/"

# 保存したい問題, 保存先ディレクトリ, 保存ファイル名
target = [['_a', root_dir + "a/tests/", "sample_inputs.rs"],
          ['_b', root_dir + "b/tests/", "sample_inputs.rs"],
          ['_c', root_dir + "c/tests/", "sample_inputs.rs"],
          ['_d', root_dir + "d/tests/", "sample_inputs.rs"],
          ['_e', root_dir + "e/tests/", "sample_inputs.rs"]]

# 出力フォーマットを指定
## ファイル最初に書く宣言等
initial = '''use cli_test_dir::*;
const BIN: &'static str = \"./main\";
'''

## テストケースごとの出力形式
sample_format = '''
#[test]
fn sample{sample_number}() {{
    let testdir = TestDir::new(BIN, \"\");
    let output = testdir
        .cmd()
        .output_with_stdin(r#\"{input}
\"#)
        .tee_output()
        .expect_success();
    assert_eq!(output.stdout_str(), \"{output}\\n\");
    assert!(output.stderr_str().is_empty());
}}
'''

## ファイル終わりに書く宣言等
last = '''
// FIN
'''
