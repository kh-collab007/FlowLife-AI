Markdown
# FlowLife AI
## AIと、より良い毎日へ。
FlowLife AIは、日々の生活の中で「何から始めるべきか」を考える時間を減らし、AIがユーザーの予定や行動に優先順位を付け、その日にやるべきことを提案する生活支援サービスです。
## Vision
人は毎日、「何から始めるべきか」という小さな意思決定を何度も繰り返して生活しています。
FlowLife AIは、その迷う時間を減らし、一人ひとりがより充実した毎日を送れることを目指して開発しています。
## Planned Features
- タスク登録
- タスク一覧表示
- AIによる優先順位提案
## Roadmap
### Version 0.1
- タスク登録
- タスク一覧表示
### Version 0.2
- AI優先順位提案
### Version 0.3
- 行動分析
## Future Ideas
- カレンダーアプリとの連携
- 音声AIとの連携
- ポイントシステム
- 習慣分析
## Tech stack
- Python
- Git
- Git Hub
## Status
現在開発中です。このアイデアが本当に人の生活を良くするかは、まだ分かりません。だからこそ、小さく公開し、ユーザーのフィードバックを受けながら改善を重ねていきたいと考えています。
## Project Status
current Version: v0.1.0(Development)
## Development Log
### 2026/07/13
- Created FlowLife AI project
- Set up GitHub repository and development environment
- Implemented the first Python backend program
- Verified local execution
- Learned and established the Git workflow:
  - git status
  - git add
  - git commit
  - git push

### 2026/07/14
- FlowLife AIの初めてのWebページを作成
- FastAPIでJSONを返すだけでなく、HTMLを表示する仕組みを実装
- Jinja2を利用したHTMLテンプレート表示を追加
- `templates/index.html` を作成
- FastAPI（バックエンド）とHTML（フロントエンド）の役割分担を理解
- ローカル環境でWebページの表示に成功

###　2026/07/15
- ホームページに入力フォームを追加
- 木曜入力用のテキストボックスを作成
- 登録するボタンを追加
- 入力欄の説明として<label>を使用し、for属性とid属性の関連について学習

### 2026/07/16
- 目標入力フォームの作成
- inputタグによる入力欄の作成
- labelタグによる入力項目の説明
- formによるデータ送信処理
- FastAPIによるデータ受信
- POST/submitでフォームデータを受信
- Form()を利用して入力内容を取得
- 受け取ったデータをpython側で処理
- 入力データの管理
- Pythonのリストを利用して、入力された目標を一時的に保存する機能を実装
- 入力された目標を追加することで、複数の目標を管理できる
- Jinja2によるHTMLへのデータ表示
- FastAPIからHTMLへデータを渡し、Jinja2のテンプレート機能を利用して一覧表示を実装。これにより、入力した複数の目標を画面上に表示できる。

### 2026/07/17
- 目標を辞書形式で管理するように変更
- 各目標に一意のIDを付与
- 目標の達成状態を管理するため、doneフラグを追加
- Jinja2のfor文を用いて登録した目標を一覧表示
- 達成ボタンを押すと、対応する目標のdoneをTrueに変更する機能を実装
- Jinja2のif文を用いて、達成状態に応じて達成済み、未達成を表示し分ける機能を実装
### 学んだこと
- Pythonの辞書とリストを組み合わせたデータ管理
- IDを利用して特定のデータのみを更新する方法
- Jinja2のfor文による繰り返し表示
- Jinja2のif文による条件分岐
- FastAPIでフォームから受け取ったデータを画面に反映する流れ

### 2026/07/18
- 達成済みの目標では達成ボタンを表示しない機能を実装
- 目標を削除する機能を実装
- 各目標に削除ボタンを追加
- 削除後に目標一覧を再表示するように変更
### 学んだこと
- Jinja2のnotを使った条件分岐
- removeを用いたリストからの要素削除
- URLパラメータを利用して特定のデータを削除する方法