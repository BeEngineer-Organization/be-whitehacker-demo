# be-whitehacker-demo

10分程度の時間ということで、CSRF攻撃だけでは時間的に足りないような気がしたので、パスワードリスト攻撃のコードも載せておきます。

## 必要な準備

### クローン

be_whitehacker_demoディレクトリを作成し、be_whitehacker_demoディレクトリ直下に移動してからターミナルで以下のコマンドを実行します。

`$ git clone https://github.com/BeEngineer-Organization/be-whitehacker-demo.git`

これでクローンが完了しました。

### 攻撃用アプリの準備

target_appディレクトリを作成し、そこで、ターミナルで以下のコマンドを実行します。

`$ git clone https://github.com/BeEngineer-Organization/be-whitehacker-target-app.git`

次に、target_app/config/settings.pyに移動します。以下のようになっている部分があります。

    DEBUG = FALSE
    # DEBUG = TRUE

この部分を以下のように変更します。

    # DEBUG = FALSE
    DEBUG = TRUE

また、ターミナルで以下のコマンドを実行します。

    $ python3 -m venv venv
    $ source myvenv/bin/activate
    $ pip3 install -r requirements.txt

target_appディレクトリ直下で以下のコマンドを実行すると、ローカルサーバが立ち上がります。

`$ python3 manage.py runserver`

ローカルサーバは CTRL + C で終了します

### コードの移し替え

be_whitehacker_demo/views.pyのコードをコピーし、target_app/csrf-attack/views.pyに貼り付けます。これによって、CSRF攻撃ができるようになります。

### パスワードリストのダウンロード

[このサイト](https://download.openwall.net/pub/wordlists/passwords/)のpassword.gzをダウンロードします。

password.gzのパスをコピーし、解凍するために以下のコマンドを実行します。

`$ gunzip {password.gzのパス}`

password.gz解凍されると、passwordファイルが現れます。また、be_whitehacker_demo/password_attack.pyの以下の部分に、passwordファイルのパスを記述します。

`WORDLIST = ""    # passwordのパスを記述`