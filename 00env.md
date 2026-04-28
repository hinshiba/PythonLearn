## 開発環境の構築

この章では，Pythonでプログラミングを始めるための環境をWindows11上に整える．
やることは大きく4つ:

1. エクスプローラーの設定
2. ターミナルの設定
3. 開発ツールのインストール
4. 開発フォルダの作成

順番に進めていこう．

---

### エクスプローラーの設定

Windows のエクスプローラー(ファイルを管理するアプリ)は，初期設定だといくつかの情報が隠されている．
プログラミングではファイルの **拡張子**(`.py`，`.txt` など)や，**隠しフォルダ**(`.git` など)を日常的に扱うので，最初に表示設定を変えておく．

まずエクスプローラーを開き(`Win + E`)，上部メニューの **「...」** > **「オプション」** > **「表示」**と進む．
以降の設定はすべてこの画面で行う．

#### 拡張子を表示する

Windows はデフォルトで拡張子を非表示にしている．
拡張子が見えないと `main.py` と `main.txt` の区別がつかず，トラブルの原因になる．

**「登録されている拡張子は表示しない」** のチェックを**外す**．

これでファイル名の末尾に `.txt` や `.py` などの拡張子が表示されるようになる．

#### 隠しフォルダを表示する

Git などの開発ツールは `.git` のようにドット (`.`) で始まるフォルダを作る．
Windows はデフォルトでこれらを非表示にしているため，表示設定を変更する．

**「隠しファイル、隠しフォルダー、および隠しドライブを表示する」** にチェックを入れる．

#### エクスプローラーを別プロセスで開くようにする

エクスプローラーは通常，すべてのウィンドウが1つのプロセスとして動作している．
この設定だと，1つのウィンドウがフリーズすると他のウィンドウも巻き添えになる．
ウィンドウごとに独立したプロセスにしておくと安定する．

**「別のプロセスでフォルダー ウィンドウを開く」** にチェックを入れる．

---

### ターミナルの設定

ターミナルとは，コマンド(文字の命令)を入力してコンピュータを操作するアプリのこと．
プログラミングではターミナルを頻繁に使うので，すぐ起動できるようにしておく．

#### ターミナルをタスクバーにピン留めする

1. スタートメニューを開き，「ターミナル」と検索する
2. タスクバーの **「ターミナル」** アプリを右クリック > **「タスク バーにピン留めする」** を選択

これでタスクバーからワンクリックで起動できるようになる．

#### PowerShell 7.x をインストールする

Windows に最初から入っている「Windows PowerShell」はバージョン5.1で，やや古い．
最新の **PowerShell 7.x** をインストールするとよい．

1. タスクバーからターミナルを起動する
2. 以下のコマンドを入力して Enter を押す:

```powershell
winget install Microsoft.PowerShell
```

3. インストールが完了したら，ターミナルを閉じて再度開く
4. ターミナル上部のタブ横にある **「˅」**(下矢印)> **「設定」** を開く
5. **「既定のプロファイル」** を **「PowerShell」**(アイコンが黒いほう)に変更する
6. **「保存」** をクリックし，ターミナルを再起動する

以降，ターミナルを開くと PowerShell 7.x が起動するようになる．

---

### 開発ツールのインストール

ここでは3つのツールを順にインストールする:

| ツール     | 役割                                                                   |
| ---------- | ---------------------------------------------------------------------- |
| **Scoop**  | Windows 用のパッケージマネージャ．コマンドでソフトをインストールできる |
| **VSCode** | コードを書くためのエディタ                                             |
| **uv**     | Python のインストールやパッケージ管理を行うツール                      |

#### Scoop のインストール

Scoop は Windows 向けのパッケージマネージャで，ターミナルからコマンド一つでソフトウェアをインストール・管理できる．

ターミナルで以下のコマンドを実行する:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

1行目はスクリプトの実行を許可する設定，2行目が Scoop 本体のインストールである．

インストールが終わったら，動作確認:

```powershell
scoop --version
```

バージョン番号が表示されれば成功．

```powershell
scoop install 名前
```
によってある名前のプログラムをダウンロードし，インストールすることができる．
インストール後に出てきた内容は必ず読もう．
機能のためにその行をシェルで実行する必要がある．

#### git のインストール

git自体は開発に必須のツールであるが，今回は立ち入らない．
ここでは，Scoopの前提としてインストールする．

```powershell
scoop install git
```

これを実行すると次のようなメッセージが出るはずだ．

```
To register file associations, please execute the following command:
reg import "C:\Users\<username>\scoop\apps\git\current\install-associations.reg"

To register the context menu entry, please execute the following command:
reg import "C:\Users\<username>\scoop\apps\git\current\install-context.reg"

To set Git Credential Manager Core for portable Git, please execute the following command:
git config --system credential.helper manager
```

これらは忘れずに実行しよう．

```
reg import "C:\Users\<username>\scoop\apps\git\current\install-associations.reg"
```

のように選択して一行ずつ実行する．

#### VSCode のインストール

VSCode(Visual Studio Code)は，Microsoft 製の無料コードエディタ．
拡張機能が豊富で，Python 開発にも広く使われている．

このように複数行のコマンドがある場合は，一行ずつ実行する必要があることに注意せよ．

```powershell
scoop bucket add extras
scoop install extras/vscode
```

1行目は Scoop に `extras` リポジトリを追加するコマンド．VSCode は `extras` に含まれている．
2行目で VSCode をインストールする．

#### uv のインストール

uv は Python のインストールやライブラリ管理を高速に行えるツール．
この教材では Python のインストールからプロジェクト管理まで uv を使う．

```powershell
scoop install main/uv
```

動作確認:

```powershell
uv --version
```

#### uv で Python をインストールする

uv を使えば Python 本体のインストールもコマンド一つで済む．

```powershell
uv python install
```

これで最新の安定版 Python がインストールされる．

インストールされた Python のバージョンを確認:

```powershell
uv python list --only-installed
```

Python のバージョン番号(例: `cpython-3.13.x-...`)が表示されれば完了．

---

### 開発フォルダの作成

プログラミング用のフォルダを作っておく．
ここでのポイントは，**OneDrive の管理下にないフォルダ** を選ぶこと．

#### なぜ OneDrive 外に作るのか

Windows11では `デスクトップ` や `ドキュメント` フォルダが OneDrive に同期されている場合が多い．
OneDrive フォルダ内に開発プロジェクトを置くと，以下のような問題が起こる:

- `.venv` など大量の小さなファイルが同期対象になり，動作が重くなる
- ファイルのロックや同期競合でビルドが失敗することがある

そのため，OneDrive とは無関係な場所にフォルダを作るのが安全．

#### 作成手順

`C:`ドライブ下などに`dev`フォルダを作成する．
大事なのは `C:\<日本語等のパス>\...` 配下でないこと．

フォルダを作ったら，VSCode でそのフォルダを開いてみよう:

フォルダを選択した状態で右クリックを行い，**「Code で開く」** を選択しよう．

VSCode が起動してフォルダが開けば，開発環境の構築は完了．

他にもフォルダを開く方法として，
```
code path/to/dir
```
でフォルダを開くことができる．

## VSCode拡張機能のインストール

VSCode では拡張機能(Extension)を追加することで，Python 開発に必要な機能を揃えられる．
ここでは3つの拡張機能をインストールする．

| 拡張機能   | 役割                                  |
| ---------- | ------------------------------------- |
| **Python** | Python ファイルの認識，補完，デバッグ |
| **Ruff**   | コードのスタイルチェックと自動整形    |
| **Ty**     | 型チェック                            |

拡張機能のインストールは，VSCode のサイドバーにある拡張機能アイコン(`Ctrl+Shift+X`)から行う．

#### Python

検索バーに `ms-python.python` と入力し，**Python** (Microsoft) をインストールする．

`.py` ファイルを開いたときの補完・構文ハイライト・デバッグ機能はこの拡張機能が提供している．

#### Ruff

検索バーに `charliermarsh.ruff` と入力し，**Ruff** をインストールする．

Ruff は Python のリンター(コードの問題を検出するツール)とフォーマッター(コードを自動整形するツール)を兼ねる．
コードを保存するたびに自動で整形されるよう，VSCode の設定を追加しておく．

`Ctrl+Shift+P` でコマンドパレットを開き，「Open User Settings (JSON)」を選択する．
以下の設定を追加する:

```json
"editor.formatOnSave": true,
"[python]": {
    "editor.codeActionsOnSave": {
        "source.fixAll.ruff": "explicit"
    }
}
```

これでファイル保存時に Ruff が自動で整形・修正を行う．

#### Ty

検索バーに `astral-sh.ty` と入力し，**Ty** をインストールする．

Ty は Python の型チェッカーで，変数や関数の型が正しく使われているかをリアルタイムで確認する．

---

次の章([01hello.md](01hello.md))では，この環境を使って最初の Python プログラムを書く．
