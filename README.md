# testcaseScraper

AtCoderのテストケースを手打ちで作ってるのに激しく時間の無駄を感じたからスクレイピングして勝手に作ってもらうことにした

## Usage

```bash
$ ./testcaseScraper.py <コンテスト名>
```

```bash
$ ./testcaseScaner.py abc175
```

## できあがるもの

### Python用

`config_python.py` を `config.py` に上書きするなりなんなりで使ってほしい  
PythonのUnittestを用いたサンプル実行ができるようになる

各問題のディレクトリに入って `main.py` にコードを書いたのちにテストを実行する  
`main.py` の中には `main()` 関数を作っておくこと

```
$ ./sample_inputs.py
```

### Rust用

Rustのproconioに対応したテストコードを作ってくれる。

```rust
use cli_test_dir::*;
const BIN: &'static str = "./main";

#[test]
fn sample1() {
    let testdir = TestDir::new(BIN, "");
    let output = testdir
        .cmd()
        .output_with_stdin(r#"RRS
"#)
        .tee_output()
        .expect_success();
    assert_eq!(output.stdout_str(), "2\n");
    assert!(output.stderr_str().is_empty());
}
// FIN
```

### Setting

`config.py` に設定を書いていく

- username
  - Atcoderのユーザ名
- password
  - Atcoderのパスワード
- root_dir
  - 保存先ディレクトリ
- target
  - 各問題の保存先やファイル名を設定する
