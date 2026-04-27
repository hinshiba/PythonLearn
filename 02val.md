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

`price` には `input()` が返した値が保存されるため，何度でも使い回せる．
税率が変わっても `tax_rate = 1.08` と一箇所だけ直せばよい．
変数には「値を一箇所にまとめる」「意味を伝える」という二つの役割がある．

---

## 変数への代入と評価

Python 公式ドキュメント: https://docs.python.org/ja/3/reference/simple_stmts.html#assignment-statements

### 代入

```python
x = 42
```

`=` は**代入演算子**と呼ぶ．数学の「等しい」ではなく，「右辺の値を左辺の名前に結びつける」という操作だ．  
右辺が先に評価され，その結果が左辺の名前に結びつけられる．

```python
x = 10
x = x + 1   # 右辺の x + 1 (= 11) が先に評価され，結果が x に結びつく
print(x)    # 11
```

### 評価

変数名を式の中に書くと，その時点で結びついているオブジェクトが取り出される．これを**評価**という．

```python
a = 5
b = 3
c = a + b   # a が 5，b が 3 として評価され，c に 8 が結びつく
print(c)    # 8
```

### 複合代入演算子

`x = x + 1` のように「自分自身を使って更新する」パターンは頻出するため，短縮形がある．

| 書き方   | 意味        |
| -------- | ----------- |
| `x += 1` | `x = x + 1` |
| `x -= 2` | `x = x - 2` |
| `x *= 3` | `x = x * 3` |
| `x /= 2` | `x = x / 2` |

---

## 変数とメモリのイメージ

Python 公式ドキュメント: https://docs.python.org/ja/3/reference/datamodel.html#objects-values-and-types

Python の変数は，C 言語などとは異なる仕組みで動く．

Python では，`42` や `"hello"` などの値そのものを**オブジェクト**と呼ぶ．  
オブジェクトはメモリ上のどこかに確保される．変数はそのオブジェクトを指す**名札（参照）**だ．

```
x = 42

  名前空間          メモリ上
┌──────────┐      ┌──────────────┐
│  x  ────────→   │  int: 42     │
└──────────┘      └──────────────┘
```

名札を別の名前にコピーすると，同じオブジェクトを二つの名前で指すことになる．

```python
x = 42
y = x

print(x)   # 42
print(y)   # 42
```

```
┌──────────┐      ┌──────────────┐
│  x  ────────→   │  int: 42     │
│  y  ────────→   │              │
└──────────┘      └──────────────┘
```

組み込み関数 `id()` を使うと，オブジェクトのメモリ上の位置（識別値）を確認できる．

```python
x = 42
y = x
print(id(x))           # たとえば 140234567890
print(id(y))           # 同じ値
print(id(x) == id(y))  # True
```

### 演習 1

次のコードを実行する前に，出力を予想してから確認しよう．

```python
a = 100
b = a
a = 200
print(b)
```

<details>
<summary>解答</summary>

`100`

`b = a` の時点で `b` は `100` というオブジェクトを指す．その後 `a` を `200` に変えても，`b` の指し先は変わらない．

</details>

---

## 基本的なデータ型

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html

オブジェクトにはそれぞれ**型（type）**がある．型は「どんな値か」「どんな操作ができるか」を決める．  
組み込み関数 `type()` で型を確認できる．

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type(True))     # <class 'bool'>
print(type("hello"))  # <class 'str'>
print(type(None))     # <class 'NoneType'>
```

### `int` — 整数

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#numeric-types-int-float-complex

```python
age = 25
year = 2024
negative = -10
big = 1_000_000   # アンダースコアで桁区切りができる（値は変わらない）
```

### `float` — 浮動小数点数

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#numeric-types-int-float-complex

小数点を含む数値を表す．コンピュータの内部では 2 進数で近似的に表現されるため，厳密な等価比較には注意が必要だ．

```python
pi = 3.14159
rate = 1.08
print(0.1 + 0.2)          # 0.30000000000000004（近似誤差）
print(0.1 + 0.2 == 0.3)   # False
```

### `bool` — 真偽値

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#boolean-type-bool

`True` または `False` の二値だけを持つ．`int` のサブクラスであり，`True == 1`，`False == 0` が成り立つ．

```python
is_open = True
has_error = False
print(True + True)   # 2（int として扱われる）
```

条件式の結果は `bool` になる．

```python
x = 10
print(x < 5)    # False
print(x == 3)   # False
print(x != 3)   # True
```

### `str` — 文字列

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#text-sequence-type-str

文字の並び（シーケンス）を表す．シングルクォート `'` またはダブルクォート `"` で囲む．どちらを使っても意味は同じだ．

```python
name = "Alice"
greeting = 'Hello'
```

この資料では引用でない限りは，ダブルクォートを用いるものとする．

複数行の文字列はトリプルクォート `"""` または `'''` で囲む．

```python
message = """
これは
複数行の
文字列です．
"""
```

文字列同士の `+` は**連結**，`*` は**繰り返し**を行う（後述の「演算とオブジェクト」参照）．

```python
s = "Hello" + ", " + "World"
print(s)          # Hello, World
print("abc" * 3)  # abcabcabc
```

**f-string（フォーマット済み文字列リテラル）**: 文字列の中に式の評価値を埋め込める．

```python
name = "Alice"
age = 30
print(f"{name} は {age} 歳です．")  # Alice は 30 歳です．
```

### `None` — 値がないことを表す

Python 公式ドキュメント: https://docs.python.org/ja/3/library/constants.html#None

「値が存在しない」「まだ決まっていない」ことを示す唯一の型．型は `NoneType`．

```python
result = None
print(result)         # None
print(type(result))   # <class 'NoneType'>
```

### 演習 2

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

## 演算とオブジェクト

Python 公式ドキュメント: https://docs.python.org/ja/3/reference/expressions.html#operator-precedence

### 算術演算子

| 演算子 | 意味                       | 例               |
| ------ | -------------------------- | ---------------- |
| `+`    | 加算                       | `3 + 2` → `5`    |
| `-`    | 減算                       | `3 - 2` → `1`    |
| `*`    | 乗算                       | `3 * 2` → `6`    |
| `/`    | 除算（結果は常に `float`） | `7 / 2` → `3.5`  |
| `//`   | 切り捨て除算               | `7 // 2` → `3`   |
| `%`    | 剰余                       | `7 % 2` → `1`    |
| `**`   | 累乗                       | `2 ** 8` → `256` |

### 演算はオブジェクトを新たに生成する

`a + b` を計算すると，**新しいオブジェクトが生成**される．元の `a` や `b` は変化しない．

```python
a = 10
b = 3
c = a + b   # 新しい int オブジェクト 13 が生成され，c に結びつく

print(a)   # 10（変化なし）
print(b)   # 3（変化なし）
print(c)   # 13
```

```
演算前:
  a ──→ [int: 10]
  b ──→ [int:  3]

a + b を評価:
           +演算
  [int: 10] ＋ [int: 3] → [int: 13] ← 新しいオブジェクト
                              ↑
  c ─────────────────────────┘
```

これは `str` でも同様だ．

```python
s1 = "Hello"
s2 = "World"
s3 = s1 + s2   # "HelloWorld" という新しい str オブジェクトが生成される

print(s1)   # "Hello"（変化なし）
print(s2)   # "World"（変化なし）
print(s3)   # "HelloWorld"
```

### 演算子の優先順位

数学と同様，`*` や `/` は `+` や `-` より先に評価される．  
明示的に順序を指定したいときは括弧 `()` を使う．

```python
print(2 + 3 * 4)    # 14（3 * 4 が先）
print((2 + 3) * 4)  # 20
```

### 演習 4

次の式の結果を予想してから確認しよう．

```python
print(10 // 3)
print(10 % 3)
print(2 ** 10)
print(9 / 3)
```

### 演習 5

半径 `r = 5` の円の面積と円周を計算して出力するコードを書こう（`pi = 3.14159` を使う）．

<details>
<summary>解答</summary>

```python
r = 5
pi = 3.14159
area = pi * r ** 2
circumference = 2 * pi * r
print(f"面積: {area}")
print(f"円周: {circumference}")
```

</details>

---

## 型ヒント

Python 公式ドキュメント: https://docs.python.org/ja/3/library/typing.html

Python は変数に型を書かなくても動く（**動的型付け**）が，型を明示的に書くことで  
コードの意図が伝わりやすくなり，エディタによる補完・検査を活用できる．

```python
age: int = 25
name: str = "Alice"
rate: float = 1.08
is_valid: bool = True
```

型ヒントはあくまでヒントであり，Python インタプリタは実行時に型を強制しない．  
型の検査をしたい場合は `ty` などの外部ツールを使う．

関数の引数と戻り値にも型ヒントを書ける（関数は後述の章で扱う）．

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## オブジェクトとメソッド

Python 公式ドキュメント: https://docs.python.org/ja/3/reference/datamodel.html#objects-values-and-types

Python のすべての値はオブジェクトだ．  
オブジェクトは**データ（属性）**と**操作（メソッド）**をひとまとめにしたものだ．

メソッドは `オブジェクト.メソッド名()` の形で呼び出す．  
「`str` 型のオブジェクトに対して，この操作を行う」という意味になる．

```python
s = "Hello, World"

print(s.upper())       # HELLO, WORLD  （大文字にした新しい str を返す）
print(s.lower())       # hello, world
print(s.replace("World", "Python"))  # Hello, Python
print(s.startswith("Hello"))         # True
print(s.count("l"))    # 3
print(s)               # Hello, World（元の s は変化しない）
```

> `str` のメソッドはすべて元の文字列を変更せず，新しいオブジェクトを返す（`str` は**イミュータブル**，後述）．

`split()` は文字列を区切り文字で分割して，**リスト**（後述）を返す．

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
メソッドが `None` を返す場合はチェーンできない（後述の `list` を参照）．

### 演習 6

```python
sentence = "the quick brown fox"
```

このとき，次の出力を得るにはどうすればよいか考えよう．

1. `"THE QUICK BROWN FOX"`
2. 単語の数を出力する（ヒント：`split()` を使う）
3. `"the quick brown fox jumps"` （末尾に `" jumps"` を追加する）

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

## コンストラクタとキャスト

Python 公式ドキュメント: https://docs.python.org/ja/3/library/functions.html#built-in-functions

型名を関数のように呼び出すと，その型の新しいオブジェクトを生成する．  
この呼び出しを**コンストラクタ呼び出し**という（厳密にはクラスの呼び出し）．

```python
x = int(42)      # int オブジェクト 42 を生成
s = str("hi")    # str オブジェクト "hi" を生成
```

別の型のオブジェクトを渡すと，**型変換（キャスト）**として使える．

```python
print(int("123"))     # 123（str → int）
print(float("3.14"))  # 3.14（str → float）
print(str(42))        # "42"（int → str）
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False（空文字列は偽）
print(bool("hi"))     # True
```

変換できない値を渡すとエラーになる．

```python
int("3.14")   # ValueError: invalid literal for int() ...
int("abc")    # ValueError: invalid literal for int() ...
```

`float` 経由ならば変換できる場合もある．

```python
int(float("3.14"))   # 3（小数点以下は切り捨て）
```

### `bool` の真偽

Python では多くのオブジェクトが `bool` として解釈できる．
主な**偽（falsy）**な値:

- `False`
- `0`，`0.0`
- 空の文字列 `""`
- 後述するコンテナが空 `[]`，`()`，`{}`
- `None`

上記以外は**真（truthy）**として扱われる．

### 演習 7

`input()` はすべての入力を `str` として返す．次のコードを完成させよう．

```python
user_input_a = input("整数を入力: ")
user_input_b = input("小数を入力: ")
```

1. `user_input_a` を `int` に変換して 2 倍にする
2. `user_input_b` を `float` に変換して切り捨て整数を求める

<details>
<summary>解答</summary>

```python
user_input_a = input("整数を入力: ")
user_input_b = input("小数を入力: ")

print(int(user_input_a) * 2)
print(int(float(user_input_b)))
```

</details>

---

## コンテナ型

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#sequence-types-list-tuple-range

複数のオブジェクトをまとめて保持するオブジェクトを**コンテナ**という．

### `list` — リスト

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#list

順序を持ち，**変更可能（ミュータブル）**なコンテナ．角括弧 `[]` で作る．

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]   # 異なる型を混在できる
empty = []
```

**インデックスアクセス**: 0 から始まる位置番号で要素を取得する．

```python
print(fruits[0])    # "apple"
print(fruits[1])    # "banana"
print(fruits[-1])   # "cherry"（末尾から -1）
```

**スライス**: `[start:stop]` で部分リストを取得する（新しいリストが返る）．

```python
print(fruits[0:2])   # ['apple', 'banana']
print(fruits[1:])    # ['banana', 'cherry']
print(fruits[:2])    # ['apple', 'banana']
```

**主なメソッド**:

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("date")         # 末尾に追加（元のリストを変更）
print(fruits)                 # ['apple', 'banana', 'cherry', 'date']

fruits.insert(1, "avocado")   # 位置 1 に挿入
print(fruits)                 # ['apple', 'avocado', 'banana', 'cherry', 'date']

fruits.remove("banana")       # 最初に見つかった "banana" を削除
print(fruits)                 # ['apple', 'avocado', 'cherry', 'date']

popped = fruits.pop()         # 末尾を取り出して返す
print(popped)                 # 'date'
print(fruits)                 # ['apple', 'avocado', 'cherry']

print(len(fruits))            # 3（要素数）
print(fruits.index("cherry")) # 2（位置を返す）
print("apple" in fruits)      # True（含まれるか確認）
```

リストは**ミュータブル**なので，メソッドが元のリストを変更することに注意する（新しいオブジェクトを返すわけではない）．  
ただし `+` 演算は新しいリストを返す．

```python
a = [1, 2]
b = [3, 4]
c = a + b       # 新しいリストが生成される
print(c)        # [1, 2, 3, 4]
print(a)        # [1, 2]（変化なし）
```

**`append()` の戻り値は `None`**

`append()` は元のリストを直接変更する操作で，戻り値は `None` だ．  
`str` のメソッドとは異なり，戻り値を使ったメソッドチェーンはできない．

```python
fruits = ["apple"]
result = fruits.append("banana")
print(result)   # None（append は None を返す）
print(fruits)   # ['apple', 'banana']（リスト自体は変更されている）

# 誤り: None に .append() は存在しないため AttributeError になる
# fruits.append("cherry").append("date")
```

破壊的なメソッド（元のオブジェクトを変更するもの）は `None` を返すのが Python の慣例だ．

### `tuple` — タプル

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#tuple

順序を持ち，**変更不可（イミュータブル）**なコンテナ．丸括弧 `()` で作る（括弧は省略できる）．

```python
point = (10, 20)
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

- 変更する予定がないデータ（座標，RGB 値など）→ `tuple`
- 追加・削除・変更を行うデータ → `list`

**アンパック**: 複数の変数にまとめて代入できる．

```python
x, y = (10, 20)
print(x)   # 10
print(y)   # 20

# list でも同様に使える
a, b, c = [1, 2, 3]
```

### `dict` — 辞書

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#mapping-types-dict

**キー**と**値**のペアを保持するコンテナ．波括弧 `{}` で作る．  
キーには変更不可なオブジェクト（`str`，`int`，`tuple` など）が使える．

```python
person = {"name": "Alice", "age": 30, "city": "Tokyo"}
```

**アクセスと変更**:

```python
print(person["name"])      # "Alice"
print(person["age"])       # 30

person["age"] = 31         # 値を変更
person["email"] = "a@b.c"  # 新しいキーを追加
del person["city"]         # キーと値を削除

print(person)
# {'name': 'Alice', 'age': 31, 'email': 'a@b.c'}
```

存在しないキーにアクセスすると `KeyError` という**例外**が発生する．  
例外とはプログラムの実行中に発生するエラーで，発生すると通常は実行が中断される（例外処理については後の章で扱う）．

```python
print(person["city"])   # KeyError: 'city'
```

`get()` を使うと，キーが存在しなくても例外を発生させずに安全にアクセスできる．

```python
print(person.get("city"))          # None（キーがない場合）
print(person.get("city", "N/A"))   # "N/A"（デフォルト値を指定）
```

**主なメソッド**:

```python
d = {"a": 1, "b": 2, "c": 3}

print(d.keys())    # dict_keys(['a', 'b', 'c'])
print(d.values())  # dict_values([1, 2, 3])
print(d.items())   # dict_items([('a', 1), ('b', 2), ('c', 3)])
print("a" in d)    # True（キーが含まれるか）
print(len(d))      # 3
```

### `set` — 集合

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#set-types-set-frozenset

**重複を持たず，順序がない**コンテナ．波括弧 `{}` で作る（ただし空集合は `set()` を使う）．

```python
s = {1, 2, 3, 2, 1}
print(s)       # {1, 2, 3}（重複が除かれる）

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

重複の除去や，含まれるかの高速な確認（`list` より速い）に使う．

```python
tags = ["python", "web", "python", "api", "web"]
unique_tags = set(tags)
print(unique_tags)   # {'python', 'web', 'api'}（順序は不定）
```

### 演習 8

次のコードで何が出力されるか予想してから確認しよう．

```python
data = [10, 20, 30, 40, 50]
print(data[2])
print(data[-2])
print(data[1:4])
data.append(60)
print(len(data))
```

### 演習 9

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
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# 1
print(scores["Bob"])           # 92

# 2
scores["Diana"] = 95
print(scores)

# 3
print(scores.keys())
```

</details>

### 演習 10

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

### 演習 11

次のコードを実行する前に，出力を予想してから確認しよう．

```python
nums = [1, 2, 3]
result = nums.append(4)
print(result)
print(nums)
```

また，`tuple` で同じことを試みるとどうなるか確認しよう．

```python
t = (1, 2, 3)
t[0] = 99
```

<details>
<summary>解答</summary>

```python
nums = [1, 2, 3]
result = nums.append(4)
print(result)   # None（append は None を返す）
print(nums)     # [1, 2, 3, 4]（元のリストが変更されている）
```

`tuple` への代入は `TypeError: 'tuple' object does not support item assignment` が発生する．  
`list` はミュータブル（変更可能），`tuple` はイミュータブル（変更不可）というちがいを実感できる．

</details>

### 演習 12

次のコードを実行するとどうなるか予想してから確認しよう．

```python
scores = {"Alice": 85, "Bob": 92}
print(scores["Charlie"])
```

エラーを発生させずに同じアクセスをするにはどうすればよいか考えよう．

<details>
<summary>解答</summary>

`KeyError: 'Charlie'` が発生する．  
`get()` を使うと安全にアクセスできる:

```python
print(scores.get("Charlie"))       # None
print(scores.get("Charlie", 0))    # 0（デフォルト値）
```

</details>

---

## イテレータ

Python 公式ドキュメント: https://docs.python.org/ja/3/library/stdtypes.html#iterator-types

コンテナ型（`list`，`tuple`，`str`，`dict`，`set`）はすべて**イテラブル（iterable）**だ．  
イテラブルとは，`__iter__()` メソッドを持つオブジェクトで，要素を順番に一つずつ取り出せる．

### なぜイテレータが必要か

コンテナ型はすべての要素をメモリ上に保持している．  
たとえば `list` に 100 万件のデータを入れると，その分だけメモリを消費する．

イテレータはデータを**一度に一つだけ**取り出す仕組みだ．  
「次の要素を要求されたときに初めて取り出す」ため，大量のデータを扱っても一度にメモリに全部読み込む必要がない．

また，後述する `for` ループはイテレータの仕組みを利用して動いている．  
コンテナから `iter()` でイテレータを作り，`next()` を繰り返すのが `for` ループの正体だ．

### イテレータの仕組み

**イテレータ（iterator）**: イテラブルから生成される，「次の要素を一つ返す」ことだけを担うオブジェクト．  
`__next__()` メソッドを持ち，要素がなくなると `StopIteration` 例外を送出する．

> **例外**とはプログラムの実行中に発生するエラーのことで，発生すると通常は実行が中断される．`StopIteration` は「次の要素がない」ことを知らせるための例外であり，`for` ループが終了するときに内部で使われる（例外処理については後の章で扱う）．

組み込み関数 `iter()` でイテラブルからイテレータを取得し，`next()` で要素を一つずつ取り出せる．

```python
fruits = ["apple", "banana", "cherry"]

it = iter(fruits)
print(next(it))   # "apple"
print(next(it))   # "banana"
print(next(it))   # "cherry"
print(next(it))   # StopIteration 例外が発生
```

イテレータは「どこまで読んだか」という状態を保持する．一度使い切ると再利用できない．

```python
it = iter([1, 2, 3])
print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
# これ以上 next() を呼ぶと StopIteration が送出される
```

**[`range()`](https://docs.python.org/ja/3/library/stdtypes.html#range)**: 整数の連番を表すイテラブル．実際には `range` オブジェクトであり，要素はアクセスされるまで生成されない（**遅延評価**）．

```python
r = range(5)                  # 0〜4 を表す range オブジェクト（値はまだ生成されない）
it = iter(r)
print(next(it))               # 0
print(next(it))               # 1
print(list(range(2, 8)))      # [2, 3, 4, 5, 6, 7]
print(list(range(0, 10, 3)))  # [0, 3, 6, 9]
```

### 演習 13

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

### 演習 14

同様に2番目と4番目の要素だけ取り出すコードを書こう．

<details>
<summary>解答</summary>

```python
data = [10, 20, 30, 40, 50]
it = iter(data)
next(it)
print(next(it))   # 20
next(it)
print(next(it))   # 40
```

</details>
