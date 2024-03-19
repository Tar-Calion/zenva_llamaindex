from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import dotenv
import os

dotenv.load_dotenv(override=True)

documents = SimpleDirectoryReader('data').load_data()

index = VectorStoreIndex.from_documents(documents)

# store the index
index.storage_context.persist()

chat_engine = index.as_chat_engine(verbose=True, chat_mode='react')

chat_engine.chat_repl()
