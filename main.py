import ollama
import streamlit as st

USER_NAME = "USER"
ASSISTANT_NAME = "assistant"

if not "chat_log" in st.session_state:
    st.session_state.chat_log = []

def create_stream(input_message: str):
    stream = ollama.chat(
        model='hf.co/bluepen5805/DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf', 
        messages=[
        {
            'role': 'user',
            'content': input_message,
        }
        ],
        stream=True,

    )
    return stream

def main():
    st.title("DeepSeek日本語版")

    input_message = st.chat_input()

    # リセットボタン作成
    if st.button("チャットリセット"):
        # セッションステートのchat_logを空に
        st.session_state.chat_log = []

    if input_message:
        for chat in st.session_state.chat_log:
            with st.chat_message(chat["name"]):
                st.write(chat["msg"])

        # 最新のメッセージを表示
        with st.chat_message(USER_NAME):
            st.write(input_message)

        stream = create_stream(input_message)

        with st.chat_message(ASSISTANT_NAME):
            assistant_message = ""
            assistant_response_area = st.empty()
            for chunk in stream:
                # 回答を逐次表示
                assistant_message += chunk["message"]["content"]
                assistant_response_area.write(assistant_message)

        # セッションにチャットログを追加
        st.session_state.chat_log.append({"name": USER_NAME, "message": input_message})
        st.session_state.chat_log.append({"name": ASSISTANT_NAME, "msg": assistant_message})

if __name__ == "__main__":
    main()