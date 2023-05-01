# Import necessary classes and functions from different packages.
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import TokenTextSplitter
from langchain.document_loaders import PyPDFLoader
import os
from dotenv import load_dotenv

# Load environment variables from .env file.
load_dotenv()

# Set the OpenAI API key.
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def load_document(path: str) -> list[str]:
    """
    Load and split a PDF document into chunks using LangChain.
    Returns a list of chunks (strings).
    """
    # Create a PyPDFLoader object with the path.
    pdf_loader = PyPDFLoader(path)
    
    # Create a TokenTextSplitter object with chunk_size=500 and chunk_overlap=50.
    chunker = TokenTextSplitter(chunk_size=500, chunk_overlap=50)
    
    # Use the pi_pdf loader to load and split the pdf document and return the result.
    return chunker.split_documents(pdf_loader.load_and_split())

# Get the path of the current directory.
dir_path = os.path.dirname(os.path.realpath(__file__))

# Join the path of langchain.pdf to the dir_path.
pdf_path = os.path.join(dir_path, "langchain.pdf")

# Create an instance of OpenAIEmbedding class.
embeddings = OpenAIEmbeddings()

# Create a vector store using Chroma.from_documents() method with loaded and splitted document and the created embeddings object.
vectordb = Chroma.from_documents(load_document(pdf_path), embeddings)
