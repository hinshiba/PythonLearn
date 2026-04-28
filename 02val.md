## 変数と演算

---

## なぜ変数が必要か

プログラムは「データを受け取り，処理し，結果を返す」ことを繰り返す．
たとえば，ユーザーが入力した価格に消費税を加えた金額を計算したいとする．

```python
print(float(input("価格を入力: ")) * 1.1)
```

このコードには問題がある．同じ入力値を別の場所でも使いたいとき，再度`input()`を呼ぶしかない．また，税率が10%から8%に変わったとき，`1.1`という数値をすべて書き換えなければならない．

変数を使うと，値に**名前をつけて再利用**できる．

```python
price = float(input("価格を入力: "))
tax_rate = 1.1

print(price * tax_rate)
```

`price`には`input()`が返した値が保存されるため，何度でも使い回せる．
税率が変わっても`tax_rate = 1.08`と一箇所だけ直せばよい．
変数には「値を一箇所にまとめる」，「意味を伝える」という二つの役割がある．

---

## 式の評価

言語リファレンス: https://docs.python.org/ja/3/reference/expressions.html#

後の説明を簡単にするため，形式的な構文について軽く説明する．**式 (expression)** とは，値を生み出す構文要素のことだ．リテラル，変数，関数呼び出し，演算子の組み合わせはすべて式である．

```python
42                # リテラル(**プログラム中に直接書かれた定数**)
"hello"           # これもリテラル
x                 # 変数
3 + 4             # 演算 2つの式(3と4)を演算子でつなげたもの <- これも式
x * 12            # これも式
print("hello")    # 関数呼び出し
```

式を計算して値を求める操作を**評価 (evaluation)** という．Pythonは式を評価すると，必ず一つのオブジェクトを返す．

この記号`>>>`は対話モードを意味する．`python`と単にタイプすると対話モードに入ることができる．
対話モードを抜ける場合は`quit()`と入力する．

```python
>>> 3 + 4
7
>>> 2 * (3 + 4)
14
>>> "Hello" + ", " + "World"
'Hello, World'
```

複合的な式は，左から順に評価していく．`2 * (3 + 4)`は次の手順で評価される．

1. リテラルである`2`を評価して，整数オブジェクトの`Int(2)`を得る
2. `(3 + 4)`を評価する
   1. リテラルである`3`を評価して，整数オブジェクトの`Int(3)`を得る
   2. 同様に`Int(4)`を得る
   3. `+`演算子を評価して，新しい整数オブジェクトの`Int(7)`を得る
3. 掛け算を意味する`*`演算子を評価する．(`Int(2) * Int(7)`)これによって`Int(14)`を得る

あまり考えなくても良い場面も多いため，以降は暗黙的にオブジェクトを指すものとする．

### 式と文

Python の構文要素は**式 (expression)** と**文 (statement)** に大別される．

- **式**は評価されて値を返す．`3 + 4`，`print("hi")`，`x` など．
- **文**は何らかの動作を実行する単位．これから後述する代入文`x = 1`，`if`文，`for`文などが該当する．

`x = 1` のような代入文自体は値を返さないが，右辺の `1` は式として評価される．

---

## 変数への代入と評価

ドキュメントチュートリアル: https://docs.python.org/ja/3/tutorial/introduction.html#using-python-as-a-calculator

言語リファレンス: https://docs.python.org/ja/3/reference/simple_stmts.html#assignment-statements

変数への代入について説明する．前述のとおり変数を使うと，値に**名前をつけて再利用**できる．
Pythonにおいては，変数は代入によってのみ作成することができる．

### 代入

簡易的な定義を示す．
```
識別子 = 式
```

例
```python
x = 42
```

`=` は**代入演算子**と呼ぶ．数学の「等しい」ではなく，「右辺の値を左辺の名前(識別子)に結びつける」という操作だ．
右辺の**式を評価**し，その結果が左辺の名前に結びつけられる．

```python
x = 10      # 右辺の 10 が評価され，結果が x に結びつく
x = x + 1   # 右辺の x + 1 (= 11) が評価され，結果が x に結びつく
print(x)    # 後述
```

### 評価

変数名を式の中に書くと，その時点で結びついているオブジェクトが取り出される．これを**評価**という．

```python
a = 5       # 5 が 5 と評価され a に 5 が結びつく
b = 3       # 以降はリテラルの評価は省略する
c = a + b   # a が 5，b が 3 として評価され，5 + 3 が評価され 8 となり， c に 8 が結びつく
print(c)    # 引数の c が評価され， 8 が `print()`に渡される
```

### 演習

#### 演習1

`input()`で整数を受け取り，その値の2倍，3倍，4倍を順に表示するコードを書こう．
掛け算には`*`演算子を用いよう．

<details>
<summary>解答</summary>

```python
n = int(input("整数を入力: "))
print(n * 2)
print(n * 3)
print(n * 4)
```

</details>

---

## 演算

言語リファレンス: https://docs.python.org/ja/3/reference/expressions.html#operator-precedence

変数への代入と，そのための式についてこれまで説明してきた．
ここではより多様な式を作成するため，演算子について説明する．

### 算術演算子

Pythonによるよく使われる算術演算子を示す．

| 演算子 | 意味                      | 例               |
| ------ | ------------------------- | ---------------- |
| `+`    | 加算                      | `3 + 2` → `5`    |
| `-`    | 減算                      | `3 - 2` → `1`    |
| `*`    | 乗算                      | `3 * 2` → `6`    |
| `/`    | 除算 (結果は常に `float`) | `7 / 2` → `3.5`  |
| `//`   | 切り捨て除算              | `7 // 2` → `3`   |
| `%`    | 剰余                      | `7 % 2` → `1`    |
| `**`   | 累乗                      | `2 ** 8` → `256` |

### 比較演算子

これらは後述する`bool`型の値を返す．`bool`型は真であることを意味する`True`と偽であることを意味する`False`の2つの値のみをとる．

| 演算子 | 意味       | 例                 |
| ------ | ---------- | ------------------ |
| `<`    | より小さい | `1 < 2`   `# True` |
| `<=`   | 以下       | `1 <= 1`  `# True` |
| `>`    | より大きい | `2 > 1`   `# True` |
| `>=`   | 以上       | `1 >= 1`  `# True` |
| `!=`   | 等しくない | `1 != 2`  `# True` |
| `==`   | 等しい     | `1 == 1`  `# True` |

> スタイルとして，変数を常に左側に書く人と，数直線になるように右側が大になる演算子のみを使う人がいる

`bool`型は極めて重要である．
具体的には後述する`if`文や`filter`等を用いることで，評価が`True`となる場合のみ実行するといった制御が可能となる．

### 論理演算子

`bool`型の値どうしを組み合わせて，`bool`型の値を得ることができる．

| 演算子 | 意味                               | 例                          |
| ------ | ---------------------------------- | --------------------------- |
| `and`  | 両方が`True`のとき`True`           | `True and False`  `# False` |
| `or`   | 少なくとも一方が`True`のとき`True` | `True or False`   `# True`  |
| `not`  | `True`と`False`を反転する          | `not True`        `# False` |

これらを用いることで，複雑な判断が可能となる．

### 演算子の優先順位

数学と同様，`*` や `/` は `+` や `-` より先に評価される．  
明示的に順序を指定したいときは括弧 `()` を使う．

```python
print(2 + 3 * 4)    # 14 (3 * 4 が先) 
print((2 + 3) * 4)  # 20
```

### 演習

#### 演習1

`input()` で半径 `r` を受け取り，円の円周と面積を計算して出力するコードを書こう (`pi = 3.14159` を使う) ．

<details>
<summary>解答</summary>

```python
r = float(input("半径を入力: "))
pi = 3.14159
area = pi * r ** 2
circumference = 2 * pi * r
print(f"円周: {circumference}")
print(f"面積: {area}")
```

</details>

---

## 基本的なデータ型

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html

オブジェクトにはそれぞれ**型 (type)**がある．型は「どんな値か」，「どんな操作ができるか」を決める．  
組み込み関数 `type()` で型を確認できる．

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type(True))     # <class 'bool'>
print(type("hello"))  # <class 'str'>
print(type(None))     # <class 'NoneType'>
```

### `int`: 整数

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#numeric-types-int-float-complex

```python
age = 25
year = 2024
negative = -10
big = 1_000_000   # アンダースコアで桁区切りができる (値は変わらない) 
```

### `float`: 浮動小数点数

小数点を含む数値を表す．コンピュータの内部では 2 進数で近似的に表現されるため，厳密な等価比較には注意が必要だ．

```python
pi = 3.14159
rate = 1.08
print(0.1 + 0.2)          # 0.30000000000000004 (近似誤差) 
print(0.1 + 0.2 == 0.3)   # False
```

### `bool`: 真偽値

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#boolean-type-bool

前述のとおり`True`または`False`の二値だけを持つ．`int`のサブクラスであり，`True == 1`，`False == 0`が成り立つ．

```python
is_open = True
has_error = False
print(True + True)   # 2 (int として扱われる) 
```

条件式の結果は `bool` になり，`if`文等の制御に用いられる．

```python
x = 10
print(x < 5)    # False
print(x == 3)   # False
print(x != 3)   # True
```

Python では多くのオブジェクトが `bool` として解釈できる．
主な**偽 (falsy) **な値:

- `False`
- `0`，`0.0`
- 空の文字列 `""`
- 後述するコンテナが空 `[]`，`()`，`{}`
- `None`

上記以外は**真 (truthy) **として扱われる．

### `str`: 文字列

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#text-sequence-type-str

文字の並び (シーケンス) を表す．
リテラルを記述する場合はシングルクォート `'` またはダブルクォート `"` で囲む．どちらを使っても意味は同じだ．

```python
name = "Alice"      
greeting = 'Hello' # 
```

> 表記ゆれが同一プログラムにあると，プログラムの品質を疑われることとなる．
> 環境構築の時に導入したフォーマッタである`ruff`は初期状態では`"`に自動的に統一するはずである．

この資料では引用でない限りは，ダブルクォートを用いることとする．
また，文字列中に`"`が出てくる場合は`'`を用いることとする．

```python
# hoge = "ダブルクォートはこれ"です"
#                             ^ ここで文字列が終わると判定してしまう
hoge = 'ダブルクォートはこれ"です'  # 良い例
```

複数行の文字列はトリプルクォート `"""` または `'''` で囲む．

```python
message = """
これは
複数行の
文字列です．
"""
```

文字列同士の `+` は**連結**，`*` は**繰り返し**を行う．

```python
s = "Hello" + ", " + "World"
print(s)          # Hello, World
print("abc" * 3)  # abcabcabc
```

**f-string (フォーマット済み文字列リテラル) **: 文字列の中に式の評価値を埋め込める．

```python
name = "Alice"
age = 30
print(f"{name} は {age} 歳です．")  # Alice は 30 歳です．
```

### `None`: 値がないことを表す

Python 公式ドキュメント: https://docs.python.org/ja/3/library/constants.html#None

「値が存在しない」「まだ決まっていない」ことを示す唯一の型．型は `NoneType`．

```python
result = None
print(result)         # None
print(type(result))   # <class 'NoneType'>
```

### 演習1

次の各値の型を `type()` で確認してから，何型になるか予想しよう．

```python
type(100)
type(100.0)
type("100")
type(True)
type(1 == 1)
type(None)
```

### 演習 3

以下の変数を使って，f-string で「〇〇の身長は△△cmです．」という文を出力しよう．

```python
person = "田中"
height = 172.5
```

<details>
<summary>解答</summary>

```python
print(f"{person}の身長は{height}cmです．")
# 田中の身長は172.5cmです．
```

</details>

---

## 型ヒント

Python 公式ドキュメント: https://docs.python.org/ja/3/library/typing.html

Python は変数に型を書かなくても動く (**動的型付け**) が，型を明示的に書くことで  
コードの意図が伝わりやすくなり，エディタによる補完・検査を活用できる．

```python
age: int = 25
name: str = "Alice"
rate: float = 1.08
is_valid: bool = True
```

**型ヒントはあくまでヒント**であり，Pythonインタプリタは実行時に型を強制しない．  
型の検査をしたい場合は開発中に`ty`などの外部ツールで確認する．

関数の引数と戻り値にも型ヒントを書ける(関数は後述の章で扱う)．

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## オブジェクトとメソッド

Python 公式ドキュメント: https://docs.python.org/ja/3/reference/datamodel.html#objects-values-and-types

Python のすべての値はオブジェクトだ．  
オブジェクトは**データ (属性) **と**操作 (メソッド) **をひとまとめにしたものだ．

> (備考) 少なくともこの文書ではオブジェクトを何かしらのクラスのインスタンスとして定義する

メソッドは `オブジェクト.メソッド名()` の形で呼び出す．  
「`str` 型のオブジェクトに対して，この操作を行う」という意味になる．

```python
s: str = "Hello, World"

print(s.upper())       # HELLO, WORLD   (大文字にした新しい str を返す) 
print(s.lower())       # hello, world
print(s.replace("World", "Python"))  # Hello, Python
print(s.startswith("Hello"))         # True
print(s.count("l"))    # 3
print(s)               # Hello, World (元の s は変化しない) 
```

> `str` のメソッドはすべて元の文字列を変更せず，新しいオブジェクトを返す (`str` は**イミュータブル**，後述) ．

`split()` は文字列を区切り文字で分割して，**リスト** (後述) を返す．

```python
s = "apple,banana,cherry"
parts = s.split(",")
print(parts)   # ['apple', 'banana', 'cherry']
```

`strip()` は前後の空白文字を取り除く．

```python
s = "  hello  "
print(s.strip())   # "hello"
```

### メソッドチェーン

`str` のメソッドはすべて新しい `str` を返すため，続けて呼び出すことができる．これを**メソッドチェーン**という．

```python
s = "  Hello, World  "
result = s.strip().lower().replace(",", "")
print(result)   # "hello world"
```

各メソッドが新しいオブジェクトを返すので，`.` でつなぐことができる．  
メソッドが `None` を返す場合はチェーンできない (後述の `list` を参照) ．

### 演習

#### 演習1

```python
sentence = "the quick brown fox"
```

このとき，次の出力を得るにはどうすればよいか考えよう．

1. `"THE QUICK BROWN FOX"`
2. 単語の数を出力する (ヒント：`split()` を使う) 
3. `"the quick brown fox jumps"`  (末尾に `" jumps"` を追加する) 

<details>
<summary>解答</summary>

```python
sentence = "the quick brown fox"

# 1
print(sentence.upper())

# 2
words = sentence.split(" ")
print(len(words))   # 4

# 3
print(sentence + " jumps")
```

</details>

---

## コンテナ型

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#sequence-types-list-tuple-range

複数のオブジェクトをまとめて保持するオブジェクトを**コンテナ**という．

> この文書では定義として考える場合は`__contains__()`を実装したクラスとする

### `list`: リスト

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#list

順序を持ち，**変更可能 (ミュータブル) **なコンテナ．角括弧 `[]` で作る．

```python
fruits: list[str] = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]   # 異なる型を混在できる
empty = []
```

**インデックスアクセス**: 0 から始まる位置番号で要素を取得する．
このように，番号を指定して操作のできる型を**シーケンス型**という．

```python
print(fruits[0])    # "apple"
print(fruits[1])    # "banana"
print(fruits[-1])   # "cherry" (末尾から -1) 
```

**スライス**: `[start:stop]` で部分リストを取得する (新しいリストが返る) ．

```python
print(fruits[0:2])   # 0番目から2番目   ['apple', 'banana']
print(fruits[1:])    # 1番目から最後    ['banana', 'cherry'] 
print(fruits[:2])    # 最初から2番目    ['apple', 'banana']
```

**主なメソッド**:

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("date")         # 末尾に追加 (元のリストを変更) 
print(fruits)                 # ['apple', 'banana', 'cherry', 'date']

fruits.insert(1, "avocado")   # 位置 1 に挿入
print(fruits)                 # ['apple', 'avocado', 'banana', 'cherry', 'date']

fruits.remove("banana")       # 最初に見つかった "banana" を削除
print(fruits)                 # ['apple', 'avocado', 'cherry', 'date']

popped = fruits.pop()         # 末尾を取り出して返す
print(popped)                 # 'date'
print(fruits)                 # ['apple', 'avocado', 'cherry']

print(len(fruits))            # 3 (要素数) 
print(fruits.index("cherry")) # 2 (位置を返す) 
print("apple" in fruits)      # True (含まれるか確認) 
```

リストは**ミュータブル**なので，メソッドが元のリストを変更することに注意する (新しいオブジェクトを返すわけではない) ．  
ただし `+` 演算は新しいリストを返す．

```python
a: list[int] = [1, 2]
b = [3, 4]
c = a + b       # 新しいリストが生成される
print(c)        # [1, 2, 3, 4]
print(a)        # [1, 2] (変化なし) 
```

**`append()` の戻り値は `None`**

`append()` は元のリストを直接変更する操作で，戻り値は `None` だ．  
`str` のメソッドとは異なり，戻り値を使ったメソッドチェーンはできない．

```python
fruits: list[str] = ["apple"]
result = fruits.append("banana")
print(result)   # None (append は None を返す) 
print(fruits)   # ['apple', 'banana'] (リスト自体が変更されている) 

# 誤り: None に .append() は存在しないため AttributeError になる
# fruits.append("cherry").append("date")
```

破壊的なメソッド (元のオブジェクトを変更するもの) は `None` を返すのが Python の慣例だ．

### `tuple`: タプル

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#tuple

順序を持ち，**変更不可 (イミュータブル)**なコンテナ．丸括弧 `()` で作る．

```python
point: tuple[int, int] = (10, 20)
rgb = (255, 128, 0)
single = (42,)    # 要素が 1 つのときはカンマが必要
```

インデックスアクセスやスライスは `list` と同様だが，要素の変更はできない．

```python
point = (10, 20)
print(point[0])    # 10
point[0] = 99      # TypeError: 'tuple' object does not support item assignment
```

`list` と `tuple` の使い分け:
- 一般的には`list`を用いる
- 関数の戻り値は`tuple`で定義する

**アンパック**: 複数の変数にまとめて代入できる．

```python
x, y = (10, 20)
print(x)   # 10
print(y)   # 20

# list でも同様に使える
a, b, c = [1, 2, 3]
```

### `dict`: 辞書

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#mapping-types-dict

**キー**と**値**のペアを保持するコンテナ．波括弧 `{key: value, ......}` で作る．  
キーには変更不可なオブジェクト (`str`，`int`，`tuple` など) が使える．

```python
person: dict[str, str | int] = {"name": "Alice", "age": 30, "city": "Tokyo"}
```

**アクセスと変更**:

```python
print(person["name"])      # キーによるアクセス "Alice"
print(person["age"])       # 30

person["age"] = 31         # 値を変更
person["email"] = "a@example.com"  # そのキーが登録されていない場合は，新しいペアが挿入される

print(person)
# {'name': 'Alice', 'age': 31, 'email': 'a@example.com'}
```

存在しないキーにアクセスすると `KeyError` という**例外**が発生する．  
例外とはプログラムの実行中に発生するエラーで，発生すると通常は実行が中断される．

```python
print(person["city"])   # KeyError: 'city'
```

`get()`を使うと，キーが存在しなくても例外を発生させずに安全にアクセスできる．

```python
print(person.get("city"))          # None (キーがない場合)
print(person.get("city", "N/A"))   # "N/A" (デフォルト値を指定)
```

**主なメソッド**:

```python
d: dict[str | int] = {"a": 1, "b": 2, "c": 3}

print(d.keys())    # dict_keys(['a', 'b', 'c'])
print(d.values())  # dict_values([1, 2, 3])
print(d.items())   # dict_items([('a', 1), ('b', 2), ('c', 3)])
print("a" in d)    # True (キーが含まれるか) 
print(len(d))      # 3
```

### `set`: 集合

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#set-types-set-frozenset

**重複を持たず，順序がない**コンテナ．波括弧 `{}` で作る (ただし空集合は `set()` を使う) ．

> `dict`のキーのみの実装であると理論的には考えることができる

```python
s = {1, 2, 3, 2, 1}
print(s)       # {1, 2, 3} (重複が除かれる) 

empty_set = set()   # {} では dict になってしまう
```

**集合演算**:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # 和集合: {1, 2, 3, 4, 5, 6}
print(a & b)   # 積集合: {3, 4}
print(a - b)   # 差集合: {1, 2}
print(a ^ b)   # 対称差: {1, 2, 5, 6}
```

重複の除去や，含まれるかの高速な確認 (`list` より速い) に使う．

```python
tags = ["python", "web", "python", "api", "web"]
unique_tags = set(tags)
print(unique_tags)   # {'python', 'web', 'api'} (順序は不定) 
```

### `str`: 文字列

ここまでかなり登場してきた`str`もまたコンテナ型であり，その中でもシーケンス型である．

そのため番号を指定して要素を取り出したり，スライスを作成することができる．
また，イミュータブルであるため変更する操作を直接行うことができない．

```python
msg = "hello python"
print(msg[0])
print(msg[6:])
# Cannot assign to a subscript on an object of type
# a[0] = "Z" 
```

### `range`オブジェクト

まだ登場していないが，`for`文において指定回数だけ繰り返すときに頻出である．
これもまたシーケンス型であるため同様の操作を実施できる．

```python
obj = range(4)
print(type(obj))    # <class 'range'>
print(obj)          # range(0, 4)
print(obj[2])       # 2
```

### 演習

#### 演習1

次のコードで何が出力されるか予想してから確認しよう．

```python
data: list[int] = [10, 20, 30, 40, 50]
print(data[2])
print(data[-2])
print(data[1:])
data.append(60)
print(len(data))
```

#### 演習2

以下の辞書を使って，各問いに答えるコードを書こう．

```python
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
```

1. `"Bob"` のスコアを出力する
2. `"Diana"` のスコアを `95` として追加する
3. キーの一覧を出力する

<details>
<summary>解答</summary>

```python
scores: dict[str, int] = {"Alice": 85, "Bob": 92, "Charlie": 78}

# 1
print(scores["Bob"])           # 92

# 2
scores["Diana"] = 95
print(scores)

# 3
print(scores.keys())
```

</details>

#### 演習3

次のリストから重複を除いて，何種類の要素があるかを出力するコードを書こう．

```python
colors = ["red", "blue", "green", "red", "blue", "yellow"]
```

<details>
<summary>解答</summary>

```python
colors = ["red", "blue", "green", "red", "blue", "yellow"]
unique = set(colors)
print(len(unique))   # 4
```

</details>

### コンテナ型の性質のまとめ

ここまで登場したコンテナ型は次の6つだ．

- `list`
- `tuple`
- `str`
- `range`
- `dict`
- `set`

これらに共通して当てはまる性質を整理する．

`in`演算子の右辺に配置し，左辺の値が含まれるかを`bool`で返す．

```python
print(3 in [1, 2, 3])              # True
print("a" in ("a", "b"))           # True
print("py" in "python")            # True (str は部分文字列を検査する)
print(2 in range(5))               # True
print("name" in {"name": "Alice"}) # True (dict はキーを検査する)
print(1 in {1, 2, 3})              # True
```

また，厳密にコンテナ型の性質というわけではないが，`len()`によって保持している要素数を取得できる．

```python
print(len([1, 2, 3]))         # 3
print(len((1, 2)))            # 2
print(len("hello"))           # 5
print(len(range(10)))         # 10
print(len({"a": 1, "b": 2}))  # 2
print(len({1, 2, 3}))         # 3
```

#### シーケンス型のみに当てはまる性質

コンテナ型の中でも順序を持ち，番号でアクセスできるものを**シーケンス型**という．ここまで登場したシーケンス型は次の4つだ．

- `list`
- `tuple`
- `str`
- `range`

`dict`と`set`はシーケンス型ではないため，以下の操作はできない．

**インデックスアクセス**: `obj[i]`で`i`番目の要素を取り出せる．負のインデックスは末尾から数える．

```python
print([10, 20, 30][0])    # 10
print((10, 20, 30)[-1])   # 30
print("python"[2])        # 't'
print(range(10)[5])       # 5
```

**スライス**: `obj[start:stop]`や`obj[start:stop:step]`で部分シーケンスを取り出せる．

```python
print([1, 2, 3, 4, 5][1:4])   # [2, 3, 4]
print((1, 2, 3, 4, 5)[::2])   # (1, 3, 5)
print("python"[1:4])          # 'yth'
print(list(range(10)[2:8:2])) # [2, 4, 6]
```

---

## イテレータ

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#iterator-types

コンテナ型 (`list`，`tuple`，`str`，`dict`，`set`) は(一般的には)すべて**イテラブル (iterable)**だ．  
イテラブルとは，`__iter__()` メソッドを持つオブジェクトで，要素を順番に一つずつ取り出せる．

### なぜイテレータが必要か

イテレータを用いることで，`list`を`tuple`に変更しても動くようなコードを作成できる．
このような共通して持っている基本的な機能を組み合わせて設計することで，より変更に強い抽象的なコードを作成できる．

また，後述する `for` ループはイテレータの仕組みを利用して動いている．  
コンテナから `iter()` でイテレータを作り，`next()` を繰り返すのが `for` ループの正体だ．

### イテレータの仕組み

**イテレータ (iterator)**とはイテラブルなオブジェクトから生成される，「次の要素を一つ返す」ことだけを担うオブジェクトであある．  
`__next__()`メソッドを持ち，要素がなくなると `StopIteration` 例外を送出する．

> **例外**とはプログラムの実行中に発生するエラーのことで，発生すると通常は実行が中断される．`StopIteration` は「次の要素がない」ことを知らせるための例外であり，`for` ループが終了するときに内部で使われる (例外処理については後の章で扱う) ．

組み込み関数`iter()`でイテラブルからイテレータを取得し，`next()`で要素を一つずつ取り出せる．

```python
fruits = ["apple", "banana", "cherry"]

it: Iterator[str] = iter(fruits)
print(next(it))   # "apple"
print(next(it))   # "banana"
print(next(it))   # "cherry"
print(next(it))   # StopIteration 例外が発生
```

イテレータは「どこまで読んだか」という状態を保持する．一度使い切ると再利用できない．

### 演習

#### 演習1

次のリストからイテレータを作り，`next()` を使って最初の 2 要素だけを取り出すコードを書こう．

```python
data = [10, 20, 30, 40, 50]
```

<details>
<summary>解答</summary>

```python
data = [10, 20, 30, 40, 50]
it = iter(data)
print(next(it))   # 10
print(next(it))   # 20
```

</details>

#### 演習2

同様に2番目と4番目の要素だけ取り出すコードを書こう．

<details>
<summary>解答</summary>

```python
data = [10, 20, 30, 40, 50]
it = iter(data)
next(it)          # 読み捨てる
print(next(it))   # 20
next(it)
print(next(it))   # 40
```

</details>
