# 専門家LLMアシスタント

LangChainとOpenAI GPTを使用した専門分野別のアシスタントアプリケーション

## 🚀 機能

- **税務専門家モード**: 税理士として税務に関する質問に回答
- **経理専門家モード**: 経理エキスパートとして会計・簿記に関する質問に回答
- LangChainを使用したLLMとの連携
- Streamlitによる直感的なWebインターフェース

## 📋 必要な環境

- Python 3.11+
- OpenAI API キー

## 🔧 セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/YOUR_USERNAME/streamlit-llm-app.git
cd streamlit-llm-app
```

### 2. 仮想環境の作成・有効化

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定

1. `.env` ファイルを作成
2. OpenAI APIキーを設定

```env
OPENAI_API_KEY=sk-proj-your-actual-api-key-here
```

### 5. アプリケーションの実行

```bash
streamlit run app.py
```

ブラウザで http://localhost:8501 にアクセス

## 📁 プロジェクト構造

```
streamlit-llm-app/
├── app.py              # メインアプリケーション
├── requirements.txt    # 依存パッケージ一覧
├── .env               # 環境変数（要設定、.gitignoreに含まれる）
├── .gitignore         # Git除外設定
├── README.md          # このファイル
└── backup/            # プロジェクトバックアップ
```

## 💡 使用方法

1. アプリケーション起動後、左側で専門分野を選択
2. 右側のテキストエリアに質問を入力
3. 「🚀 質問する」ボタンをクリック
4. 選択した専門分野の専門家として回答が生成されます

## 🔧 技術スタック

- **Frontend**: Streamlit
- **LLM Framework**: LangChain
- **AI Model**: OpenAI GPT-3.5-turbo
- **Environment**: Python 3.11+

## 📝 ライセンス

MIT License

## 🤝 貢献

プルリクエストや課題報告を歓迎します。

## 📞 サポート

質問や問題がある場合は、Issuesページで報告してください。