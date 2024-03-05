from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain import OpenAI
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import InMemoryByteStore
from langchain_community.document_loaders import TextLoader
import os

DATA_PATH = os.path.join(os.getcwd(),'animalgpt','All data_2.txt')

STORE = InMemoryByteStore()

class Prediction:

    def __init__(self) -> None:
        self.underlying_embeddings = OpenAIEmbeddings()
        self.cached_embedder = CacheBackedEmbeddings.from_bytes_store(
        self.underlying_embeddings, STORE, namespace=self.underlying_embeddings.model
        )
        self.raw_documents = TextLoader(DATA_PATH).load()
        
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=0)
        self.texts = self.text_splitter.split_documents(self.raw_documents)
        self.db = FAISS.from_documents(self.texts, self.cached_embedder)

    
    def predict(self,query):
        retrieval_qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=self.db.as_retriever())
        result = retrieval_qa({"query": query})
        return result["result"]
        
        

