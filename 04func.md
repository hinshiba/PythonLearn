## 関数

### 関数の必要性

ここまでは関数を定義することなく実装を行ってきた．
しかし関数を実装することで，処理のかたまりに名前を付け，再利用することができるようになる．
これは変数のような利点をもたらす．

|                  | 変数                     | 関数                     |
| ---------------- | ------------------------ | ------------------------ |
| 名前を付けるもの | 値                       | 手続き                   |
| 利点1            | 名前によって理解を助ける | 名前によって理解を助ける |
| 利点2            | ほかの場所で再利用できる | ほかの場所で再利用できる |

関数を定義すること自体も十分理解してほしいが，呼び出しという操作についても知識を深めてほしい．

### 関数の宣言と定義

Pythonドキュメント: https://docs.python.org/ja/3/reference/compound_stmts.html#function-definitions

関数は `def` キーワードを用いて定義する．これまでで一番省略の多い定義であるが，本資料では次の形を覚えておけば十分である．

```
"def" 識別子 "(" 仮引数名1 ":" 型ヒント1 "," ...... ")" ["->" 型ヒント] ":" ブロック
```

`識別子` が関数の名前，`仮引数` が呼び出し時に値を受け取るための変数，`->` の後ろが返り値の型ヒントである．型ヒントは省略できるが，読み手のためにつける習慣をつけたい．ブロック内に処理を書き，`return` 文で値を返す．

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 5))   # 8
```

#### 仮引数と実引数

関数まわりでは似た用語が登場するため整理しておく．

- **仮引数 (parameter)**: 関数定義の側で書かれる変数．上の例では `a`，`b`．
- **実引数 (argument)**: 関数を呼び出すときに実際に渡される値．上の例では `3`，`5`．

仮引数はあくまで関数の中で使うための「箱」であり，呼び出すたびに新しい値が入る．これに対して実引数は呼び出し側で実際に評価された値そのものである．

#### return

`return`文は関数の処理を終了し，呼び出し元へ値を返す．`return`を書かなかった場合や`return`の後ろに値を書かなかった場合は `None` が返る．

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def shout(name: str) -> None:
    print(f"HELLO, {name.upper()}!")
    # return を書かなくてもよい (None が返る)

s = greet("World")     # "Hello, World!"
r = shout("World")     # 標準出力に表示，r は None
```

`return`は関数の途中でも書けて，そこで処理が打ち切られる．条件によって早期に値を返す書き方を**早期リターン**と呼ぶ．

```python
def abs_value(n: int) -> int:
    if n < 0:
        return -n
    return n
```

これはブロックのネストを小さくする有効な手法である．

#### 引数の種類

Pythonの関数引数にはいくつかの種類があり，それぞれ呼び出し方や宣言の仕方が異なる．

##### 位置引数

仮引数の宣言順に，呼び出し側でも順番通りに値を渡す．最も基本的な形である．

```python
def power(base: int, exp: int) -> int:
    return base ** exp

print(power(2, 10))   # 1024
```

##### キーワード引数

呼び出し側で `仮引数名=値` と書くことで，順序によらず明示的に対応関係を指定できる．

```python
print(power(base=2, exp=10))   # 1024
print(power(exp=10, base=2))   # 順序を入れ替えてもよい
```

引数の意図を呼び出し側に明示できるため，引数が多い関数では可読性が上がる．

##### デフォルト引数

仮引数に `=` でデフォルト値を指定すると，呼び出し時にその引数を省略できる．

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

print(greet("World"))                  # Hello, World!
print(greet("World", "こんにちは"))    # こんにちは, World!
```

注意点として，**デフォルト値はミュータブル (リストや辞書など) にしてはならない**．デフォルト値は関数定義時に1度だけ評価され，呼び出し間で共有されるため，思わぬバグの原因になる．

```python
def append_to(item, target: list = []):   # 危険
    target.append(item)
    return target

print(append_to(1))   # [1]
print(append_to(2))   # [1, 2] ← 前回の呼び出しの結果が残っている
```

ミュータブルなデフォルト値が必要な場合は `None` をデフォルトとし，関数内で生成するのが定石である．

```python
def append_to(item, target: list | None = None):
    if target is None:
        target = []
    target.append(item)
    return target
```

##### 可変長引数 (位置)

仮引数名の前に `*` をつけると，余った位置引数を `tuple` としてまとめて受け取れる．慣習的に名前は `args` とすることが多い．

```python
def total(*args: int) -> int:
    return sum(args)

print(total(1, 2, 3))         # 6
print(total(1, 2, 3, 4, 5))   # 15
```

##### 可変長引数 (キー)

仮引数名の前に `**` をつけると，余ったキーワード引数を `dict` としてまとめて受け取れる．慣習的に名前は `kwargs` とすることが多い．

```python
def show(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}={value}")

show(name="Alice", role="admin")
# name=Alice
# role=admin
```

##### 備考: 位置専用引数とキーワード専用引数

> この節は余裕がある人だけで良い．

仮引数並びの中に特殊なマーカーである `/` と `*` を入れることで，呼び出し側に「位置引数として渡せ」「キーワード引数として渡せ」と強制できる．

- `/` より**前**の仮引数は**位置専用** (positional-only) となり，キーワードでは渡せない．
- `*` より**後**の仮引数は**キーワード専用** (keyword-only) となり，位置では渡せない．
- `/` と `*` の**間**の仮引数はどちらの方法でも渡せる (通常の仮引数)．

```python
def f(pos_only, /, normal, *, kw_only) -> None:
    print(pos_only, normal, kw_only)

f(1, 2, kw_only=3)            # OK
f(1, normal=2, kw_only=3)     # OK
f(pos_only=1, normal=2, kw_only=3)   # NG (pos_only はキーワード不可)
f(1, 2, 3)                    # NG (kw_only は位置不可)
```

可変長引数 `*args` 自体も「これより後ろはキーワード専用」を意味するため，`*args` を伴う関数のあとに書いた仮引数はキーワード専用となる．

```python
def g(a, *args, key) -> None:
    print(a, args, key)

g(1, 2, 3, key=4)   # a=1, args=(2,3), key=4
```

これによって`input`の定義に含まれていたスラッシュの意味が分かったはずである．

```python
input(prompt, /)
```

引数の意図を明確にしたいAPI設計で有用である．

#### 引数は変数への代入

仮引数に実引数の値が渡されるという操作は，本質的には**代入**である．つまり次の2つは似た振る舞いをする．

```python
def f(x: int) -> None:
    print(x)

f(10)
# ↓ ほぼ同等
x = 10
print(x)
```

このことから，Pythonの「変数は値そのものではなくオブジェクトへの参照を保持する」という性質がそのまま関数引数にも当てはまる．たとえばリストを渡して関数内で書き換えると，呼び出し側のリストも変化する．

```python
def push_one(target: list[int]) -> None:
    target.append(1)

xs = [10, 20]
push_one(xs)
print(xs)   # [10, 20, 1]
```

---

### 関数の呼び出し

#### 呼び出し時の評価

関数を呼び出す `f(args)` という式を評価するとき，Pythonはまず**実引数を左から順に評価**し，その結果を仮引数に束縛してからブロックを実行する．

```python
def f(a: int, b: int) -> int:
    return a + b

x = 3
y = 5
print(f(x + 1, y * 2))   # 4 と 10 が先に計算され，f(4, 10) が呼ばれる
```

この「先に評価する」という挙動を**正格評価**と呼ぶ．Pythonでは `if` の条件式や論理演算子の短絡評価を除いて，基本的にすべて正格評価である．

> 対義語は「遅延評価」．必要になってから評価する．

#### 呼び出し方

引数の種類に応じて，呼び出し側の書き方も組み合わせられる．

```python
def describe(name: str, age: int = 0, *hobbies: str, **info: str) -> None:
    print(name, age, hobbies, info)

describe("Alice")
# Alice 0 () {}

describe("Alice", 30)
# Alice 30 () {}

describe("Alice", 30, "music", "go")
# Alice 30 ('music', 'go') {}

describe("Alice", age=30, role="admin")
# Alice 30 () {'role': 'admin'}
```

また，`list` や `dict` の前に `*` / `**` をつけて呼び出すと，それぞれを位置引数 / キーワード引数として展開できる (アンパック)．

```python
args = [2, 10]
print(power(*args))   # power(2, 10) と等価

kwargs = {"base": 2, "exp": 10}
print(power(**kwargs))   # power(base=2, exp=10) と等価
```

#### スコープ

関数の中で `=` で代入された変数は，その関数の中だけで有効な**ローカル変数**となる．関数の外で定義された変数は**グローバル変数**と呼び，関数内から参照することはできるが，再代入は別物として扱われる．

グローバル変数はよほどのことがなければ使うべきでない．最後の手段である．

```python
x = 10                # グローバル変数

def f() -> None:
    print(x)          # 参照はできる → 10

def g() -> None:
    x = 20            # これはローカル変数 (グローバルとは別物)
    print(x)          # 20

f()
g()
print(x)              # 10 (グローバルは変わっていない)
```

関数内からグローバル変数を本当に書き換えたいときは`global`宣言を使うが，これは本当に意図せぬ副作用を生みやすいため最後の手段の最後の手段である．

Pythonの名前解決はおおむね **LEGB** の順で行われる．

- **L** (Local): 関数内のローカル
- **E** (Enclosing): 外側の関数 (ネストした関数の場合)
- **G** (Global): モジュールのトップレベル
- **B** (Built-in): `print` や `len` のような組み込み

---

### 良い関数とは

短く定義された関数は読みやすく，再利用しやすい．特に次の2点を意識するとよい．

- **1つの関数は1つのことだけを行う**: 名前で表現できる単位に処理をまとめる．
- **入力と出力を明確にする**: 引数で受け取り，`return` で返す．グローバル変数を読み書きしたり，外の状態に依存したりしない方が望ましい．

#### 副作用と参照透過性

> この節は余裕がある人だけで良い．

関数が引数の値を返す以外に，外部の状態を変化させることを**副作用**と呼ぶ．たとえば，グローバル変数の書き換え，ファイルの書き出し，画面への出力，引数として渡されたリストの破壊的変更，これらはすべて副作用である．

同じ引数で呼べば常に同じ結果を返すという性質を**参照透過性**という．参照透過な関数は，呼び出し結果でその場所を置き換えてもプログラム全体の意味が変わらないため，テストしやすく，並行処理にも強い．

```python
# 副作用がなく参照透過な関数
def add(a: int, b: int) -> int:
    return a + b

# 副作用があり参照透過な関数
# print関数もこの分類である 
total = 0
def add_to_total(n: int) -> None:   # 戻り値は一定
    global total
    total += n                      # 外部の状態を変化させている

# 副作用がないが参照透過でない関数
# 乱数生成等

# 副作用があり参照透過でない関数
# いろいろ
```

すべての関数から副作用を取り除くことはできない(画面表示やファイル入出力には副作用が不可欠)が，「副作用のある関数や参照透過でない関数」と「副作用がなく参照透過な関数」を意識して分けて書くと，コードが格段に追いやすくなる．

---

### 関数は第一級オブジェクト

Pythonでは関数も他の値と同じく**オブジェクト**である．数値や文字列と同様に変数に代入したり，他の関数の引数として渡したり，戻り値として返したりできる．このような性質を**第一級オブジェクト**であると言う．

```python
def square(n: int) -> int:
    return n ** 2

f: Callable[[int], int] = square    # 関数を変数に代入
res: int = f(5)                     # res = square(5) と同じ
print(res)                          # 25

print(square)   # <function square at 0x...>
```

関数を引数として受け取る関数を**高階関数**と呼ぶ．制御構文の章で紹介した`filter()`や`map()`はその代表例である．

```python
def apply(func, x: int) -> int:
    return func(x)

print(apply(square, 5))   # 25
```

### 無名関数

その場限りでしか使わない単純な関数を，名前を付けずに定義したいことがある．Pythonでは `lambda` 式を使って**無名関数**を作成できる．

```
"lambda" 仮引数並び ":" 式
```

```python
square = lambda n: n ** 2   # 無名関数の用途と異なるのですべきでない
print(square(5))            # 25
```

`lambda` の本体には**式しか書けない** (文は書けない) という制限があり，`return` も不要 (式の値がそのまま返り値となる)．したがって複雑な処理は通常の `def` で関数を定義した方がよい．

`lambda` が真価を発揮するのは，高階関数の引数として渡す場面である．

```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda n: n ** 2, numbers))
print(squares)   # [1, 4, 9, 16, 25]

evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)     # [2, 4]

# sorted のキーとして使う典型例
words = ["banana", "pie", "apple"]
print(sorted(words, key=lambda s: len(s)))   # ['pie', 'apple', 'banana']
```

---

### 演習

#### 演習1

2つの整数 `a`，`b` を受け取り，それらの最大公約数 (GCD) を返す関数 `gcd(a, b)` を定義せよ．ユークリッドの互除法を使えば次のように書ける．

- `b` が `0` ならば `a` を返す
- そうでなければ `gcd(b, a % b)` を返す (再帰)

<details>
<summary>解答</summary>

```python
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(12, 18))   # 6
print(gcd(100, 75))  # 25
```

関数が自分自身を呼び出すことを**再帰呼び出し**といい，ループでは表現しにくい処理を自然に書ける場合がある．ただし呼び出しの深さに上限があるため，深い再帰には向かない．

ループで書くこともできる．

```python
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
```

</details>

#### 演習2

任意個の数値を受け取り，それらの平均を返す関数 `mean(*nums)` を定義せよ．ただし引数が1つも渡されなかった場合は `0.0` を返すこと．

<details>
<summary>解答</summary>

```python
def mean(*nums: float) -> float:
    if len(nums) == 0:
        return 0.0
    return sum(nums) / len(nums)

print(mean(1, 2, 3, 4, 5))   # 3.0
print(mean())                # 0.0

# アンパックでリストを渡すこともできる
scores = [80, 90, 100]
print(mean(*scores))         # 90.0
```

可変長引数 `*nums` によって `nums` は `tuple` として受け取られる．`sum()` と `len()` の組み合わせで平均を計算できる．

なお，引数が1つも渡されなかった場合に `sum(nums) / len(nums)` を実行するとゼロ除算エラーになるため，先に `len(nums) == 0` のケースを早期リターンで処理している．

</details>

#### 演習3

> この演習は余裕がある人だけで良い．

関数を引数として受け取り，その関数を2回適用した結果を返す関数 `twice(f, x)` を定義せよ．つまり `twice(f, x)` は `f(f(x))` と等価である．これを使って `5` に対して「2乗する」操作を2回適用した結果を求めよ．

<details>
<summary>解答</summary>

```python
def twice(f, x):
    return f(f(x))

print(twice(lambda n: n ** 2, 5))   # 625 (5の2乗の2乗)
```

`5` の2乗は `25`，さらにそれを2乗すると `625` になる．`lambda` を使うことで，「2乗する」という関数を定義することなくその場で渡せる．

通常の関数を渡してもよい．

```python
def square(n: int) -> int:
    return n ** 2

print(twice(square, 5))   # 625
```

</details>