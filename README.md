# NiftyBridge LangChain project
The NiftyBridge LangChain project is an example of how to use multiple packages to create a vector store from text data. The packages used in this project are langchain.vectorstore, langchain.embeddings.openai, langchain.text_splitter, and langchain.document_loaders.

## Installation
Clone the repository by running the following command:

Once cloned, navigate to the project root directory:
cd langchain
Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
Set up your .env file with necessary API keys. You can copy the sample .env file by running the following command:
```bash
cp .env.sample .env
```

Then, replace the API keys with your own in the .env file.

Usage
Once the installation process has been completed successfully,
    you can now run FastAPI app localy by  *uvicorn main:app*
    or run Dockerfile to create image

    Uvicorn running on http://127.0.0.1:8000 

```
That API wait request in Method "POST"
curl -X 'POST' \
  'http://127.0.0.1:8000/Who%20is%20Nifty' \
  -H 'accept: application/json' \
  -d ''
```
response example

Response body
Download
```json
{
  "query": "Who is Nifty",
  "result": "Nifty Bridge LLC is a company that offers various products and services to help merchants manage NFT minting, experiences, and sales online through their platform."
}
```

This code loads a PDF document called 'langchain.pdf' and creates an instance of OpenAIEmbeddings class. It then calls the load_document function to split the loaded PDF document into chunks of 500 tokens with an overlap of 50 tokens. The load_document function returns a list of these chunks.

Finally, the code uses Chroma's from_documents method to create a vector store from the loaded and splitted documents using the previously created OpenAIEmbeddings object.
