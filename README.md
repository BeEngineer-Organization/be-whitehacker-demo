# be-whitehacker-demo

10分程度の時間ということで、CSRF攻撃だけでは時間的に足りないような気がしたので、パスワードリスト攻撃のコードも載せておきます。

## 必要な準備

### クローン

任意のディレクトリ直下で、ターミナルで以下のコマンドを実行します。

    $ git clone https://github.com/BeEngineer-Organization/be-whitehacker-demo.git

これでクローンが完了しました。任意のディレクトリ直下にbe-whitehacker-demoディレクトリが作成されます。

### 攻撃用アプリの準備

be-whitehacker-demoディレクトリ直下で、ターミナルで以下のコマンドを実行します。

    $ git clone https://github.com/BeEngineer-Organization/be-whitehacker-target-app.git

これでbe-whitehacker-demo直下にbe-whitehacker-target-appディレクトリが作成されます。そこから以下の手順を進めます。

まず、be-whitehacker-target-appディレクトリ直下に.envファイルを作成し、以下のように記述します。

    SUPERUSER_NAME=admin
    SUPERUSER_EMAIL=admin@admin.com
    SUPERUSER_PASSWORD=test

次に、be-whitehacker-target-app/config/settings.pyに移動します。以下のようになっている部分があります。

    DEBUG = FALSE
    # DEBUG = TRUE

この部分を以下のように変更します。

    # DEBUG = FALSE
    DEBUG = TRUE

また、ターミナルで以下のコマンドを実行します。

    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip3 install -r requirements.txt

be-whitehacker-target-appディレクトリ直下で以下のコマンドを実行すると、ローカルサーバが立ち上がります。

    $ python3 manage.py runserver

ローカルサーバは CTRL + C で終了します

### コードの移し替え

be-whitehacker-demo/views.pyのコードをコピーし、be-whitehacker-target-app/csrf-attack/views.pyに貼り付けます。これによって、CSRF攻撃ができるようになります。

### パスワードリストのダウンロード

[このサイト](https://download.openwall.net/pub/wordlists/passwords/)のpassword.gzをダウンロードします。

password.gzのパスをコピーし、解凍するために以下のコマンドを実行します。

    $ gunzip {password.gzのパス}

password.gzが解凍されると、passwordファイルが現れます。また、be-whitehacker-demo/password_attack.pyの以下の部分に、passwordファイルのパスを記述します。

    WORDLIST = ""    # passwordのパスを記述

## 紹介のやり方
### CSRF攻撃

be-whitehacker-target-appディレクトリ直下で以下のコマンドを実行して、ローカルサーバを立ち上げます。

    $ python3 manage.py runserver

サインアップでユーザを複数作り（ここでは便宜上A、Bとします。）、Aでログインします。

AとBのトークルームを作って、そこで「http://127.0.0.1:8000/beengineer.fake/teacher-list/」というメッセージをBに送信します。このリンクはCSRF攻撃が可能な罠サイトのものです。

マイページからログアウトし、Bとしてログインし直します。その後、トークルームに移動し、リンク先にアクセスすると、「CSRF ATTACK」という送ったはずのないメッセージが勝手に送信されています。

### パスワードリスト攻撃

be-whitehacker-target-appディレクトリ直下で以下のコマンドを実行して、ローカルサーバを立ち上げます。

    $ python3 manage.py runserver

be-whitehacker-demoディレクトリ直下に移動します。別のターミナルを立ち上げて、以下のコマンドでpassword_attack.pyを起動させます。

    $ sudo python3 password_attack.py

ターミナルに攻撃の履歴が表示され、成功した場合には特定のメッセージが表示されます。