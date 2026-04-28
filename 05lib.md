## モジュールとライブラリ

### モジュールの必要性

この章ではモジュールについて学ぶ．
いままで変数，関数という単位で名前を付けて再利用することを可能にしてきた．
モジュールも同様に，複数の関数や変数，まだ明確には登場していないクラスといった定義をひとまとまりにした単位であり，名前を付けて他のプログラムから再利用できるようにする仕組みである．

モジュールを作成するもっとも典型的な方法は `.py` ファイルを作成することである．そして複数のモジュールをまとめてさらに大きな単位にしたものが**パッケージ**であり，世界中の人が再利用できるよう公開されているパッケージのことを，本資料では便宜的に**ライブラリ**と呼ぶ．

Pythonドキュメント: https://docs.python.org/ja/3/reference/import.html#importlib

---

### ライブラリの利用

正直にいうと，多くの場合モジュールの分割より圧倒的によく使われるのがライブラリの利用である．
プログラミングを学び始めて「目的の処理をすべて自分で書きたい」と思っている人には残念かもしれないが，(またはもうプログラムなんて書きたくないと思っている人には朗報かもしれないが)多くの場合，他人の作成したライブラリを呼び出すことで素早く実装することがほとんどである．代表的な領域と，よく使われるライブラリを以下に挙げる．

- 数値計算: `numpy`
- 機械学習: `pytorch`，`tensorflow`，`scikit-learn`
- 図の作成: `matplotlib`，`seaborn`，`plotly`
- データ分析: `polars`，`pandas`
- Webアプリ: `fastapi`，`flask`，`django`
- HTTPアクセス: `requests`，`httpx`

これらをはじめとするPythonのライブラリは，**PyPI** (Python Package Index) と呼ばれる中央のリポジトリで公開されている．

PyPI: https://pypi.org/

2026-04-28現在，PyPIには **797,203** ものプロジェクトが登録されている．大抵のことはすでに誰かが実装しているため，車輪の再発明をせずに呼び出すだけでよい場合が多い．

#### 備考: ライブラリのセキュリティ

PyPIには誰でもパッケージを公開できるため，悪意のあるコードを含むパッケージが紛れ込んでいることがある．特に有名ライブラリと類似した名前を使った**タイポスクワッティング**と呼ばれる攻撃 (`requests` に似せた `requsts` など) は度々問題となっている．導入するライブラリは以下の点を確認したい．

- 公式ドキュメントやGitHubリポジトリへのリンクが正規のものか
- 直近のリリース履歴があり保守されているか
- ダウンロード数や依存元プロジェクトの規模

---

### モジュールの分割

実装が大きくなってくると，すべてを1つのファイルに書くのは現実的でなくなる．Pythonでは別の `.py` ファイルを作成し，それを `import` することで複数ファイルへ分割できる．

#### 別ファイルの作成と import

たとえば次のような2ファイル構成を考える．

```python
# greet.py
def hello(name: str) -> str:
    return f"Hello, {name}!"

def bye(name: str) -> str:
    return f"Bye, {name}!"
```

```python
# main.py
import greet

print(greet.hello("World"))   # Hello, World!
print(greet.bye("World"))     # Bye, World!
```

`import モジュール名` と書くと，同じディレクトリにある `モジュール名.py` が読み込まれ，そのモジュール内の名前は `モジュール名.識別子` の形でアクセスできるようになる．

#### from import

モジュール内の特定の名前だけを取り込みたいときは `from モジュール名 import 識別子` と書く．こうするとモジュール名のプレフィクスなしで使えるようになる．

```python
# main.py
from greet import hello, bye

print(hello("World"))   # Hello, World!
print(bye("World"))     # Bye, World!
```

別名をつけたいときは `as` を使う．

```python
import numpy as np
from greet import hello as say_hello
```

なお `from モジュール名 import *` という書き方もあるが，どの名前が取り込まれたかが分からなくなり可読性を著しく損なうため，原則として使うべきではない．

#### `__name__` について

`uv` によって生成されたコードには次のようなものが含まれていた．

```python
if __name__ == "__main__":
    main()
```

Pythonでは，スクリプトファイル (モジュール) を実行するとき，インタプリタはそのモジュールにいくつかの**特殊な属性**を自動的に設定する．そのひとつが `__name__` 変数である．

- そのファイルを**直接 `python ファイル名.py` として実行した場合**: `__name__` には文字列 `"__main__"` が代入される．
- そのファイルを**別のファイルから `import` した場合**: `__name__` にはそのモジュール名 (ファイル名から `.py` を除いたもの) が代入される．

```python
# greet.py
print(f"このモジュールの __name__ は: {__name__}")

def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    # ここは直接実行されたときだけ動く
    print(hello("World"))
```

```
$ python greet.py
このモジュールの __name__ は: __main__
Hello, World!
```

```python
# main.py
import greet
# → "このモジュールの __name__ は: greet" と表示される
# → if __name__ == "__main__": の中は実行されない
```

なぜこの仕組みが必要なのか．`import`文は，モジュールファイルに書かれたトップレベルのコードを**すべて実行する**というのが基本動作である．つまり関数定義の外側に書かれた処理は，他のファイルから `import` されただけで動いてしまう．これでは「ライブラリとしても，スクリプトとしても使えるファイル」を書こうとしたときに困る．

`if __name__ == "__main__":` ブロックは，「直接実行されたときだけ動かしたい処理」をそこに閉じ込めるための定型句である．これにより，`greet.py` を `import` する側は副作用なしで関数だけを使え，直接実行する側はテスト用のコードを動かせる．

#### 名前空間

> この節は余裕がある人だけで良い．

モジュールは**名前空間**としても機能する．同じ名前の関数や変数があっても，所属するモジュールが異なれば別物として扱える．

```python
# math_util.py
def add(a: int, b: int) -> int:
    return a + b

# string_util.py
def add(a: str, b: str) -> str:
    return a + b   # 文字列連結を意図した別の関数

# main.py
import math_util
import string_util

print(math_util.add(1, 2))        # 3
print(string_util.add("a", "b"))  # ab
```

名前の衝突を避けつつ意味のある名前を付けられるのが，名前空間としてのモジュールの利点である．Pythonの設計思想を集めた**The Zen of Python** にも次のような言葉がある．

> Namespaces are one honking great idea -- let's do more of those!

多くの比較的新しい言語には名前空間という概念があるため，ここで理解しておいて損はない．

---

### ライブラリの導入

PyPIで公開されているライブラリを実際に使うには，それを自分のプロジェクトに導入する必要がある．本資料では `uv` を使って管理する．

ここで紹介するコマンドは，すべて**シェル (PowerShell やターミナル) から実行する**ものであり，Pythonファイル (`.py`) の中に書くものではない．
Pythonの構文ではなく，`uv`というアプリケーションを呼び出すコマンドであることを忘れないでほしい．

PowerShellで実行する例を以下に示す．

#### uv add

ライブラリをプロジェクトに追加する．

```powershell
uv add matplotlib
```

これを実行すると，`matplotlib` がダウンロードされ，プロジェクトの依存関係に追加される．以降，`uv run main.py` で実行するときには自動的に利用可能になる．

バージョンを指定したい場合は次のように書く．

```powershell
uv add "matplotlib==3.8.0"      # ちょうど 3.8.0
uv add "matplotlib>=3.8"        # 3.8 以上
uv add "matplotlib>=3.8,<4.0"   # 3.8 以上かつ 4.0 未満
```

シェルによっては `>` や `<` をリダイレクト記号として解釈してしまうため，引用符で囲む必要がある．

#### uv remove

不要になったライブラリを削除する．

```powershell
uv remove matplotlib
```

環境からも`pyproject.toml`からも取り除かれる．

#### uv pip install

`uv pip install`は古い`pip`互換のインストールコマンドである．プロジェクトの依存関係には記録されず，環境にだけ入る点が`uv add`と異なる．**基本的には `uv add` を使うこと**を推奨する．`pip install ...` の例しか載っていないドキュメントを試す際の互換コマンドだと考えればよい．

```powershell
uv pip install requests   # ドキュメントにpipを用いるように書いてある場合
```

#### uv sync

`pyproject.toml` (および `uv.lock`) に書かれた依存関係を実際の環境に反映する．他人のリポジトリをクローンしてきて初期セットアップするときによく使う．

```powershell
uv sync
```

このコマンドにより，必要なライブラリがすべて揃った状態のPython環境が用意される．

#### pyproject.toml

プロジェクトのメタ情報 (名前，バージョン，Pythonの要求バージョン) と依存ライブラリを記述する設定ファイルである．`uv add` / `uv remove` を実行すると，このファイルの `dependencies` 欄が自動的に書き換わる．

```toml
[project]
name = "pythonlearn"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "matplotlib>=3.8",
]
```

通常は手で編集するよりも `uv add` / `uv remove` 経由で更新するのが安全である．

#### 備考: uv が作成している venv について

> この節は余裕がある人だけで良い．

`uv` は内部で **仮想環境** (virtual environment, それを操作するvenv) というものを作成して，プロジェクトごとに独立したPython環境を用意している．`uv sync` や `uv add` を実行すると `.venv/` というディレクトリがプロジェクト直下にできているはずである．

PC全体で1つのPython環境を共有していると，あるプロジェクトで `matplotlib==3.8` を使い，別のプロジェクトで `matplotlib==2.0` を使うといった「バージョンの両立」ができない．プロジェクトごとに独立した環境を持たせることで，互いに干渉せず開発できるようになる．

`uv run main.py` の `uv run` は，「この `.venv/` 内のPythonでスクリプトを実行する」という意味である．`python main.py` と直接書くと，OSのグローバルなPythonが起動してしまい，プロジェクトに入れたはずのライブラリが見つからない，ということになりやすい．

`venv`は`uv`とは独立した機能であり，

```powershell
.\.venv\Scripts\activate
```

を実行することで仮想環境を有効化し，

```powershell
python main.py
```

のようにすることも前述のとおり可能である．

---

### 演習

#### 演習1

`matplotlib` を使って，0 から 2π の範囲で `sin(x)` と `cos(x)` のグラフを1つの図に重ねて描画せよ．凡例 (`legend`) も表示すること．

事前に PowerShell で次のコマンドを実行し，必要なライブラリを導入しておくこと．

```powershell
uv add matplotlib numpy
```

<details>
<summary>解答</summary>

```python
# main.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label="sin(x)")
plt.plot(x, y_cos, label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
```

```powershell
uv run main.py
```

`np.linspace(0, 2 * np.pi, 200)` は 0 から `2π` までを 200点に等分した配列を生成する．`plt.plot()` を続けて呼ぶことで複数の曲線を同じ図に重ねられる．`plt.legend()` は各曲線に渡した `label` を凡例として表示する．

</details>

#### 演習2

自分で `calc.py` というモジュールを作り，次の関数を定義せよ．

- `add(a, b)`: `a + b` を返す
- `sub(a, b)`: `a - b` を返す
- `mul(a, b)`: `a * b` を返す
- `div(a, b)`: `a / b` を返す．ただし `b` が `0` のときは `None` を返す

そのうえで，別ファイル `main.py` から `calc` モジュールを `import` して，すべての関数を呼び出してみよ．`calc.py` を直接実行したときには簡単な動作確認のテストコードが動くようにし，`import` されただけのときは動かないようにせよ．

<details>
<summary>解答</summary>

```python
# calc.py
def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b

if __name__ == "__main__":
    # 直接実行されたときだけ動く動作確認コード
    print(add(3, 5))    # 8
    print(sub(3, 5))    # -2
    print(mul(3, 5))    # 15
    print(div(10, 4))   # 2.5
    print(div(10, 0))   # None
```

```python
# main.py
import calc

print(calc.add(1, 2))     # 3
print(calc.sub(1, 2))     # -1
print(calc.mul(3, 4))     # 12
print(calc.div(10, 0))    # None

# from import を使う書き方
from calc import add, div
print(add(100, 200))      # 300
print(div(7, 2))          # 3.5
```

`if __name__ == "__main__":` ブロックの中に動作確認コードを置くことで，`main.py` から `import calc` した際に動作確認コードが動かないようにできる．これにより，`calc.py` 単体でテストしたいときは `uv run calc.py`，本番で使うときは `uv run main.py` というように使い分けられる．

</details>
