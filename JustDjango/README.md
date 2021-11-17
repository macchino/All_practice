PostgreSQLのPeer認証と他の認証方法への変更

http://www.utsushiiro.jp/blog/archives/327

Peer 認証からパスワード認証に変更
パスワード認証に変更するには auth-method を peer から md5 にすればよい.

local   all             postgres                              peer ← ここが auth-method
ただし, これを最初にやってしまうと postgresユーザ(データベース側)のパスワードは設定されていないため, ログインできない(パスワードがNULLなのでパスワード認証が必ず失敗する). このパスワードを設定するには以下の２つの方法がある.

一つ目は Peer 認証で postgresql に接続してpostgres ユーザ(データベース側)のパスワードを設定する方法. まず, Peer 認証で接続するために postgres ユーザ(OS側)でログインできる必要があるが, postgresql インストール時に作成される postgres ユーザ(OS側)はパスワードが設定されていないのでまずこれを設定する.

[utsushiiro@ubuntu_server ]$ sudo passwd postgres
その後, postgres になって postgresql に接続する.

[utsushiiro@ubuntu_server ]$ su - postgres
[postgres@ubuntu_server ]$ psql
psql (9.5.9)
Type "help" for help.

postgres=#
そして, 以下の SQL でパスワードを設定する.

ALTER USER postgres with encrypted password 'ここにパスワード';


次に
CREATE DATABASE hello_app（DB名）;
CREATE USER admin WITH PASSWORD 'password'(←パスワード入力);
GRANT ALL PRIVILEGES ON DATABASE hello_app TO admin;
