import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# 環境変数を読み込み
load_dotenv()

# ページ設定
st.set_page_config(
    page_title="専門家LLMアシスタント",
    page_icon="👨‍💼",
    layout="wide"
)

def initialize_llm():
    """LangChain ChatOpenAI の初期化"""
    # 環境変数からAPIキーを取得
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        st.error("⚠️ OpenAI APIキーが設定されていません。")
        st.info("""
        APIキーを設定するには：
        1. `.env` ファイルを作成
        2. `OPENAI_API_KEY=your_api_key_here` を追加
        3. `your_api_key_here` を実際のAPIキーに置き換え
        """)
        return None
    
    # LangChain ChatOpenAIの初期化
    llm = ChatOpenAI(
        api_key=api_key,
        model="gpt-3.5-turbo",
        temperature=0.7
    )
    return llm

def get_system_message(expert_type):
    """専門家の種類に応じてシステムメッセージを生成"""
    system_messages = {
        "税務": """
あなたは税務の専門家です。以下の特徴を持って回答してください：

- 日本の税法に精通した税理士として振る舞ってください
- 所得税、法人税、消費税、相続税などの税務に関する質問に詳しく答えてください
- 税制改正や最新の税務情報についても言及してください
- 専門用語を使いつつも、分かりやすい説明を心がけてください
- 必要に応じて具体的な計算例や事例を示してください
- 税務申告や節税対策についてのアドバイスも提供してください
""",
        "経理": """
あなたは経理の専門家です。以下の特徴を持って回答してください：

- 簿記や会計の専門知識を持った経理のエキスパートとして振る舞ってください
- 仕訳、財務諸表作成、原価計算、予算管理などの経理業務に詳しく答えてください
- 会計基準（日本基準、IFRS等）についても説明してください
- 経理システムや会計ソフトの活用方法についてもアドバイスしてください
- 月次決算、年次決算の流れや注意点について説明してください
- 内部統制や経理業務の効率化についても言及してください
"""
    }
    return system_messages.get(expert_type, "あなたは親切で知識豊富なアシスタントです。")

def generate_response(llm, expert_type, user_input):
    """LLMからの応答を生成"""
    try:
        # システムメッセージを取得
        system_message_content = get_system_message(expert_type)
        
        # メッセージを構築
        messages = [
            SystemMessage(content=system_message_content),
            HumanMessage(content=user_input)
        ]
        
        # LLMから応答を生成
        response = llm(messages)
        return response.content
        
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

def main():
    st.title("👨‍💼 専門家LLMアシスタント")
    st.markdown("専門分野を選択して、その領域の専門家として回答するLLMアシスタント")
    
    # LLMの初期化
    llm = initialize_llm()
    
    if llm is None:
        st.stop()
    
    # メインコンテンツを2列に分割
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.header("🔧 設定")
        
        # 専門家の種類を選択するラジオボタン
        expert_type = st.radio(
            "専門家の種類を選択してください:",
            ["税務", "経理"],
            index=0,
            help="選択した専門分野の専門家として回答します"
        )
        
        # 選択された専門家の説明を表示
        if expert_type == "税務":
            st.info("🧾 **税務専門家モード**\n\n税理士として、所得税、法人税、消費税、相続税などの税務に関する質問にお答えします。")
        elif expert_type == "経理":
            st.info("📊 **経理専門家モード**\n\n経理のエキスパートとして、簿記、会計、財務諸表、原価計算などの経理業務に関する質問にお答えします。")
    
    with col2:
        st.header("💬 質問・相談")
        
        # 入力フォーム
        with st.form("query_form"):
            user_input = st.text_area(
                "質問や相談内容を入力してください:",
                height=150,
                placeholder=f"{expert_type}に関する質問をどうぞ..."
            )
            
            submitted = st.form_submit_button("🚀 質問する", use_container_width=True)
        
        # 回答の表示エリア
        if submitted and user_input.strip():
            with st.spinner(f"{expert_type}専門家として回答を生成中..."):
                # LLMから応答を生成
                response = generate_response(llm, expert_type, user_input)
                
                # 結果を表示
                st.success("✅ 回答が生成されました")
                
                # 回答を表示するコンテナ
                with st.container():
                    st.markdown("### 📝 専門家からの回答")
                    st.markdown("---")
                    st.write(response)
                    st.markdown("---")
        
        elif submitted and not user_input.strip():
            st.warning("⚠️ 質問内容を入力してください。")
    
    # フッター
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: gray; font-size: 0.8em;'>
        💡 ヒント: 具体的な状況や詳細を含めて質問すると、より精度の高い回答が得られます
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()