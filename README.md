# testcaseScraper

AtCoderのテストケースを手打ちで作ってるのに激しく時間の無駄を感じたからスクレイピングして勝手に作ってもらうことにした

## できあがるもの

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

## Usage

```bash
$ ./testcaseScraper.py <コンテスト名>
```

```bash
$ ./testcaseScaner.py abc175
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
