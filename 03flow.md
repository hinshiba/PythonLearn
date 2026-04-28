## 制御構文

ここまで面白くもない文法について学んできた．
この章の制御構造をある程度理解すれば，小さなプログラムであれば十分記述可能であるはずである．

### プログラムの制御構造

ある程度昔には`goto`を用いたジャンプ命令によってフロー分岐やループ表現を実現していた．
いまでもアセンブリはジャンプ命令によって実装することとなるが，非常に読みずらく理解しずらいという問題がある．

これをどうにかする手法として提案されたのが**構造化プログラミング**という概念で，標準的な制御構造として3つが提唱されている．

- 順次
- 分岐
- 反復




---

## `__name__` について

Python のスクリプトを実行したことがある人は，次のコードを見たことがあるかもしれない．

```python
if __name__ == "__main__":
    main()
```

これは「おまじない」ではなく，仕組みを理解すると自然なコードだ．

Python では，スクリプトファイル（モジュール）を実行するとき，インタプリタはそのモジュールにいくつかの**特殊な属性**を自動的に設定する．そのひとつが `__name__` だ．

- そのファイルを**直接 `python ファイル名.py` として実行した場合**: `__name__` には文字列 `"__main__"` が代入される．
- そのファイルを**別のファイルから `import` した場合**: `__name__` にはそのモジュール名（ファイル名から `.py` を除いたもの）が代入される．

```python
# greet.py
print(f"このモジュールの __name__ は: {__name__}")

def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    # ここは直接実行されたときだけ動く
    print(greet("World"))
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

この仕組みにより，「ライブラリとしても，スクリプトとしても使えるファイル」を書くことができる．

---

## 反復: `for` 文

コンテナ型やイテラブルの全要素に対して同じ処理を行うとき，`for` 文を使う．

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry
```

`dict` に対しては，デフォルトでキーを反復する．

```python
scores = {"Alice": 85, "Bob": 92}

for key in scores:
    print(key, scores[key])
# Alice 85
# Bob 92

for key, value in scores.items():   # アンパックを使うと両方取れる
    print(f"{key}: {value}")
```

`for` 文は内部でイテレータプロトコルを使って動いている:

1. `iter(iterable)` を呼び，イテレータを得る
2. `next(iterator)` を繰り返し呼ぶ
3. `StopIteration` が発生したらループを終了する

`range()` を使うと整数の連番を手軽に反復できる．

```python
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):      # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 3):  # 0, 3, 6, 9
    print(i)
```

**`enumerate()`**: インデックスと要素をペアで返す．

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry
```

**`zip()`**: 複数のイテラブルを並行して反復する．

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78
```

### リスト内包表記

イテラブルから新しいリストを作る簡潔な書き方．

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

### 演習: range と for

`range()` を使って 1 から 10 までの奇数だけを出力するコードを書こう．

<details>
<summary>解答</summary>

```python
for i in range(1, 11, 2):
    print(i)

# またはリスト内包表記
print([i for i in range(1, 11) if i % 2 != 0])
```

</details>

### 演習: 合計

次のリストに含まれる数値のうち，3 の倍数だけを合計するコードを書こう．

```python
numbers = [1, 3, 5, 6, 9, 10, 12, 15, 17]
```

<details>
<summary>解答</summary>

```python
numbers = [1, 3, 5, 6, 9, 10, 12, 15, 17]

total = 0
for n in numbers:
    if n % 3 == 0:
        total += n
print(total)   # 45

# リスト内包表記 + sum()
print(sum(n for n in numbers if n % 3 == 0))   # 45
```

</details>

### 演習: 辞書のリスト

次の辞書のリストから，スコアが 80 以上の人の名前だけを `list` で取得するコードを書こう．

```python
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 91},
    {"name": "Diana", "score": 68},
]
```

<details>
<summary>解答</summary>

```python
passed = [s["name"] for s in students if s["score"] >= 80]
print(passed)   # ['Alice', 'Charlie']
```

</details>