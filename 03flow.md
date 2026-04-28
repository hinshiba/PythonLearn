## 制御構文

ここまで面白くもない文法について学んできた．
この章の制御構造をある程度理解すれば，小さなプログラムであれば十分記述可能であるはずである．

### プログラムの制御構造

Pythonチュートリアル: https://docs.python.org/ja/3/tutorial/controlflow.html

ある程度昔には`goto`を用いたジャンプ命令によってフロー分岐やループ表現を実現していた．
いまでもアセンブリはジャンプ命令によって実装することとなるが，非常に読みずらく理解しずらいという問題がある．

これをどうにかする手法として提案されたのが**構造化プログラミング**という概念で，標準的な制御構造として3つが提唱されている．

- 順次
- 分岐: `if`，`elif`，`else`
- 反復: `for`，`while`

---

### if文

Pythonドキュメント: https://docs.python.org/ja/3/reference/compound_stmts.html#the-if-statement

条件によって処理を分岐させるための構文である．簡易的な定義を以下に示す．

```
"if" 式 ":" ブロック
         ("elif" 式 ":" ブロック)*
         ["else" ":" ブロック]
```

`if` の直後に書かれた式が真と評価された場合，対応するブロックが実行される．前述のとおり，Pythonではブロックをインデント (通常は半角スペース4つ) によって表現することに注意してほしい．

```python
x = 10

if 0 < x:               # x > 0
    print("positive")
```

ここで条件式に書ける「真と評価される値」について整理しておく．Pythonでは任意のオブジェクトが真偽値としての文脈で評価可能で，`bool()`を呼んだときの結果がそのまま条件判定に使われる．

- 偽と評価されるもの: `False`，`None`，数値の `0`，空のコンテナ (`""`，`[]`，`{}`，`()`)
- 真と評価されるもの: それ以外すべて

条件式では**比較演算子**と**論理演算子**を有効に活用できる．

| 演算子               | 意味                 |
| -------------------- | -------------------- |
| `==`，`!=`           | 等しい，等しくない   |
| `<`，`<=`，`>`，`>=` | 大小比較             |
| `in`，`not in`       | 含まれる，含まれない |
| `is`，`is not`       | 同一オブジェクトか   |
| `and`，`or`，`not`   | 論理積，論理和，否定 |

```python
score = 75

if 60 <= score and score <= 100:
    print("pass")
```

Pythonでは`60 <= score <= 100`のように比較演算子を連鎖させて書ける．これは `60 <= score and score <= 100` と等価であるが，他のプログラミング言語の多くはこの記法をサポートしていない．

`and` と `or` は**短絡評価**を行う．`a and b` は `a` が偽なら `b` を評価せず `a` を返し，`a or b` は `a` が真なら `b` を評価せず `a` を返す．

```python
name = ""
display = name or "anonymous"   # name が空文字なので "anonymous"
```

#### elifとelse

複数の条件を順に評価したい場合は `elif` を使う．どの条件にも当てはまらない場合の処理は `else` に書く．

```python
score = 72

if 90 <= score:
    grade = "A"
elif 80 <= score:
    grade = "B"
elif 60 <= score:
    grade = "C"
else:
    grade = "F"

print(grade)   # C
```

`elif` は上から順に評価され，最初に真となった分岐だけが実行される．`else` 節は省略可能で，どの条件にも一致しなかったときに何もしないなら書かなくてよい．

なお，Pythonには他言語にあるような `switch` / `case` 文は長らく存在しなかったが，3.10以降は構造的パターンマッチング (`match` 文) が導入されている．本資料では扱わない．

#### 条件演算子

値を条件によって切り替えたいだけのとき，`if` 文で書くと冗長になることがある．Pythonでは式としての分岐を**条件式** (三項演算子に相当) で書ける．

```
真のときの値 "if" 条件 "else" 偽のときの値
```

```python
n = 7
parity = "even" if n % 2 == 0 else "odd"
print(parity)   # odd
```

C系言語の `条件 ? 真 : 偽` と語順が異なる点に注意せよ．Pythonでは値が先に来る．

条件式は式なので，関数の引数や内包表記の中など，文を書けない場所でも使える．

```python
numbers = [1, -2, 3, -4]
abs_values = [n if n >= 0 else -n for n in numbers]
print(abs_values)   # [1, 2, 3, 4]
```

ただし条件が複雑になったり分岐が3つ以上になったりする場合は，無理に条件式に詰め込まず通常の `if` / `elif` / `else` で書いた方が読みやすい．

#### 宣言的手法

> この節は余裕がある人だけで良い．

ここまでは「どう処理するか」を順に書き下す**手続き的**な書き方を紹介してきた．一方，Pythonには「何を求めるか」を記述する**宣言的**なスタイルもある．コレクションに対する条件分岐は，`if` 文で書くよりも高階関数や内包表記を使った方が意図が明確になることが多い．

ここでは代表的な高階関数として `filter()` と `map()` を紹介する．

**`filter(関数, イテラブル)`**: 関数が真を返す要素だけを残す．

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)   # [2, 4, 6]
```

`lambda` は無名関数を作る式で，`lambda 引数: 式` という形をとる．関数定義については後の章で改めて扱う．

**`map(関数, イテラブル)`**: 各要素に関数を適用した結果を返す．

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda n: n ** 2, numbers))
print(squares)   # [1, 4, 9, 16]
```

このように，「条件で要素を選ぶ」「全要素を変換する」といった処理は，`for` 文と `if` 文で組み立てるよりも高階関数や値の生成であれば後述する内包表記で表現した方が，コード量が減り意図も伝わりやすい．分岐をすべて `if` 文で書く必要はない，ということを覚えておきたい．

#### 演習

##### 演習1

整数 `n` を受け取り，その符号に応じて以下のように出力するコードを書け．

- `n` が正なら `"positive"`
- `n` が負なら `"negative"`
- `n` が `0` なら `"zero"`

<details>
<summary>解答</summary>

```python
n = int(input("> "))

if 0 < n:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")
```

`elif` を `else` で結ぶことで，「正でも負でもないなら `0` である」という事実をそのまま記述できる．`elif n == 0:` と書いても動作は同じだが，`else` の方が「残りすべて」を表現しているという意図が伝わりやすい．

</details>

##### 演習2

入力された西暦 `year` がうるう年であるかを判定するコードを書け．グレゴリオ暦のうるう年の規則は次の通りである．

- 4で割り切れる年はうるう年である
- ただし，100で割り切れる年はうるう年でない
- ただし，400で割り切れる年はうるう年である

たとえば，`2000` はうるう年だが `1900` はうるう年でない．`2024` はうるう年だが `2023` はうるう年でない．

<details>
<summary>解答</summary>

```python
year = int(input("西暦を入力> "))

if year % 400 == 0:
    print("leap")
elif year % 100 == 0:
    print("not leap")
elif year % 4 == 0:
    print("leap")
else:
    print("not leap")
```

ここで重要なのは `elif` の**評価順序**である．規則を上から順にそのまま書くと次のようになりがちだが，これは誤りである．

```python
# 誤った例
if year % 4 == 0:
    print("leap")
elif year % 100 == 0:
    print("not leap")
elif year % 400 == 0:
    print("leap")
else:
    print("not leap")
```

`2000` は `4` でも割り切れるため，最初の `if year % 4 == 0:` で `"leap"` と出力される．これはたまたま正解だが，`1900` を入力しても同じく最初の分岐で `"leap"` となってしまい，**誤った結果**になる．`if` / `elif` は上から順に評価され，最初に真となった分岐だけが実行されるため，**より特殊な条件 (= 範囲が狭い条件) を先に書く**必要がある．

論理演算子を組み合わせて1つの式で書くこともできる．

```python
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("leap")
else:
    print("not leap")
```

さらに，(読みやすいかは別として)条件演算子を使えば1行で書ける．

```python
print("leap" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "not leap")
```

</details>


---

### for文

Pythonドキュメント: https://docs.python.org/ja/3/reference/compound_stmts.html#the-for-statement

イテラブルの全要素に対して同じ処理を繰り返したいとき，`for`文を使う．簡易的な定義を以下に示す．

```
"for" 変数名 "in" イテラブルなオブジェクト ":" ブロック
          ["else" ":" ブロック]
```

`in`の右に書かれたイテラブルから要素を1つずつ取り出して変数に代入し，対応するブロックを実行する．これをすべての要素について繰り返す．`if`文と同様に，ブロックはインデントで表現する．

```python
fruits: list[str] = ["apple", "banana", "cherry"]

for fruit in fruits:
    # fruit str型の新しい変数
    print(fruit)
# apple
# banana
# cherry
```

文字列も前述のとおりイテラブルであるので次のようなこともできる．

```python
for c in "abc":
    print(c)
# a
# b
# c
```

`dict` に対しては，デフォルトでキーが取り出される．キーと値の両方が欲しいときは `.items()` を使ってアンパックするとよい．

```python
scores = {"Alice": 85, "Bob": 92}

for key in scores:
    print(key, scores[key])
# Alice 85
# Bob 92

for key, value in scores.items():
    print(f"{key}: {value}")
```

#### range()

`range()` は整数の連番を生成するイテラブルを返す．特定の回数だけ処理を繰り返したいときに便利である．

```python
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):      # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 3):  # 0, 3, 6, 9
    print(i)
```

`range(stop)`，`range(start, stop)`，`range(start, stop, step)` の3形式があり，いずれも `stop` の値は**含まない**ことに注意 (半開区間)．

ループ変数を使わず単に処理を `n` 回繰り返したいだけのときは，慣習として変数名に `_` (アンダースコア) を使う．「この変数を使う意図はありません」という意思表示になる．

```python
for _ in range(3):
    print("hello")
# hello
# hello
# hello
```

#### イテレータによる同等表現

`for` 文は，内部的には**イテレータ**という仕組みを使って要素を1つずつ取り出している．具体的には次の手順で動作する．

1. `iter(イテラブル)`を呼び，イテレータを得る
2. `next(イテレータ)`を繰り返し呼んで要素を取り出す
3. `StopIteration`例外が発生したらループを終了する

つまり次の `for` 文と `while` 文を使った書き方は等価である．

```python
fruits: list[str] = ["apple", "banana", "cherry"]

# for 文
for fruit in fruits:
    print(fruit)
    # ほかの処理

# 同等の処理 (イテレータを直接操作)
it: Iterator[str] = iter(fruits)    # イテレータを得る
while True:                         # 無限ループ
    try:
        fruit: str = next(it)       # nextで一つ次を得る
    except StopIteration:           # もし`StopIteration`が発生したら`while`を抜ける
        break

    print(fruit)
    # ほかの処理
```

普段は `for` 文を使えば十分であり，このような書き下しを自分で書く必要はほぼない．ただし「`for` 文は魔法ではなくイテレーターの上に成り立っている」ということを知っておくと，エラーの修正や後々ジェネレータや独自のイテラブルを扱うときに理解しやすい．

#### enumerate()

イテラブルの要素と一緒に，それが何番目の要素なのか(インデックス)を取得したいことがある．素朴に書くと次のようになる．

```python
fruits: list[str] = ["apple", "banana", "cherry"]

i: int = 0
for fruit in fruits:
    print(i, fruit)
    i += 1
```

しかしPythonには `enumerate()` という組み込み関数があり，インデックスと要素のペアを返してくれる．こちらを使った方が簡潔である．

```python
fruits: list[str] = ["apple", "banana", "cherry"]

# 複数の変数を配置できる
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry
```

開始番号を変えたいときは第2引数で指定できる (例: `enumerate(fruits, 1)`で`1`から始まる)．

#### breakとcontinue

Pythonドキュメント: https://docs.python.org/ja/3/reference/simple_stmts.html#the-break-statement

ループの途中で抜けたり，残りの処理を飛ばして次の反復に進みたいことがある．このために`break`と `continue`という文が用意されている．

- `break`: 現在のループを直ちに終了する
- `continue`: 現在の反復の残りをスキップし，次の反復に進む

```python
# 最初に見つかった負の数で打ち切る
numbers: list[int] = [3, 1, 4, -1, 5, 9]

for n in numbers:
    if n < 0:
        print("found negative")
        break
    print(n)
# 3
# 1
# 4
# found negative
```

```python
# 偶数だけを処理し，奇数はスキップする
for n in range(1, 6):
    if n % 2 != 0:
        continue
    print(n)
# 2
# 4
```

`break`と`continue` は，最も内側のループにのみ作用する．多重ループで外側のループを抜けたいときは，フラグ変数を用意するか，後述の関数として切り出して `return` で抜けるなどの工夫が必要になる．

なお，`for` 文には `else` 節を書くこともでき，これは**ループが `break` で中断されずに最後まで回りきった**ときにだけ実行される．「探索したが見つからなかった場合」を素直に書ける．

```python
numbers: list[int] = [3, 1, 4, 1, 5, 9]

for n in numbers:
    if n < 0:
        print("found negative")
        break
else:
    print("all non-negative")
# all non-negative
```

他言語にあまり見られない構文であるため，初見では`if`の`else`と混同しやすい．無理に使う必要はないが，こういう書き方ができるということは知っておくとよい．

#### リスト内包表記

> この節は余裕がある人だけで良い．

`for` 文と `if` 文を組み合わせて新しいリストを作る処理は頻出するため，Pythonには**リスト内包表記**という専用の記法がある．

```python
numbers = [1, 2, 3, 4, 5]

# for 文で書く場合
squares = []
for n in numbers:
    squares.append(n ** 2)

# リスト内包表記
squares = [n ** 2 for n in numbers]
print(squares)   # [1, 4, 9, 16, 25]
```

条件でフィルタすることもできる．

```python
evens = [n for n in numbers if n % 2 == 0]
print(evens)   # [2, 4]
```

前述の宣言的手法の節と同様，「リストを生成する」という意図がそのままコードに表れるため，慣れると `for` 文よりも読みやすい．

#### while文について

Pythonには `for` 文以外にもう一つの反復構文として `while` 文がある．条件が真である間ブロックを繰り返し実行するもので，回数が事前に決まらないループに向いている．本資料では扱わないが，興味があればPythonチュートリアルの該当箇所を読んでほしい．

Pythonチュートリアル: https://docs.python.org/ja/3/tutorial/controlflow.html#while-statements

#### 演習

##### 演習1

いわゆる**FizzBuzz**問題である．1から30までの整数について，次のルールに従って出力するコードを書け．

- 15の倍数なら `"FizzBuzz"`
- 3の倍数なら `"Fizz"`
- 5の倍数なら `"Buzz"`
- それ以外はその数自体

<details>
<summary>解答</summary>

```python
for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

うるう年判定の演習と同様に `elif` の評価順序がポイントで，`15` の倍数は `3` の倍数でも `5` の倍数でもあるため，最も特殊な条件である `i % 15 == 0` を先に書く必要がある．

</details>

##### 演習2

簡単な電卓を作成せよ．次の形式で入力を受け取り，演算結果を出力するプログラムを書け．

```
> 3 + 5
8
> 10 - 4
6
> 6 * 7
42
> 20 / 4
5.0
```

入力は `input()` で1行として受け取り，半角スペースで区切られているとしてよい．`+`，`-`，`*`，`/` の4種類の演算子に対応すること．それ以外の演算子が来たときは `"unknown operator"` と出力せよ．

ヒント: 入力文字列は `str.split()` で空白区切りの `list` に分けられる．数値への変換は `int()` や `float()` を使う．

<details>
<summary>解答</summary>

```python
line = input("> ")
a, op, b = line.split()
a = float(a)
b = float(b)

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("unknown operator")
```

`a, op, b = line.split()` のように複数の変数へ一度に代入する書き方を**アンパック代入**と呼ぶ．`split()` は半角空白で区切ったリストを返すため，要素数が3でないとエラーになる点に注意．

複数回連続して計算したい場合は `for` 文と `range()` を組み合わせるとよい．たとえば3回繰り返すなら以下のようになる．

```python
for _ in range(3):
    line = input("> ")
    a, op, b = line.split()
    a = float(a)
    b = float(b)

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("unknown operator")
```

ループ変数自体は使わないため，`_` を変数名に用いている．

</details>
