# DeepSeek日本語版チャットアプリ

## 実行環境

Mac mini, M2 Pro, 16GB

## 環境構築

1. ollamaのインストールし、ollamaコマンドでDeepSeek-R1日本語学習済みモデルをpullし、起動する。

'''
brew install ollama

ollama serve

# 別タブで
ollama run hf.co/bluepen5805/DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf
'''

2. 必要なpythonライブラリをインストールし、streamlitを起動する

'''
uv sync

uv run streamlit run main.py
'''

### 参考資料

- https://huggingface.co/bluepen5805/DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf/tree/main
- https://zenn.dev/nishijima13/articles/3b1a50b8728261
- https://note.com/masayuki_abe/n/nac1dc2dd0e3f
- https://zenn.dev/ml_bear/books/d1f060a3f166a5/viewer/cca68d