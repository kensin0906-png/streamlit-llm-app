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

### 1. 仮想環境の作成・有効化

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 2. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 3. 環境変数の設定

1. `.env.template` を `.env` にコピー
2. `.env` ファイル内の `your_openai_api_key_here` を実際のOpenAI APIキーに置き換え

```env
OPENAI_API_KEY=sk-proj-your-actual-api-key-here
```

### 4. アプリケーションの実行

```bash
streamlit run app.py
```

ブラウザで http://localhost:8501 にアクセス

## 📁 プロジェクト構造

```
streamlit-llm-app/
├── app.py              # メインアプリケーション
├── requirements.txt    # 依存パッケージ一覧
├── .env.template      # 環境変数テンプレート
├── .env               # 環境変数（要設定）
├── .gitignore         # Git除外設定
└── README.md          # このファイル
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