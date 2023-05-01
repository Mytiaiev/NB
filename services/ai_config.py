# Import necessary classes and functions from different packages.
from langchain.llms import OpenAI
from langchain.chains import LLMChain, RetrievalQA
from langchain.prompts import PromptTemplate
from .document import vectordb


# Define a class called NiftyBridgeAI.
class NiftyBridgeAI:
    # Constructor for the class.
    def __init__(self):
        # Create an instance of OpenAI class with specific model name.
        self.llm = OpenAI(model_name="gpt-3.5-turbo")

        # Define a template string that includes input variable "text".
        self.template = """
        Hello im NiftyBridgeAI assistant. How could i help you
        Question: {context}
        Answer:
        """
        # Create a prompt template object using the defined template and input variables.
        self.prompt_template = PromptTemplate(
            template=self.template,
            input_variables=["context"],
        )
        self.chain_type_kwargs = {"prompt": self.prompt_template}
        # Create a LLMChain object with the created llm instance and prompt template.
        # self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

        # Convert the document in vectordb to retriever and use as a RetrivalQA object.
        retrieval = vectordb.as_retriever(
            search_type="similarity", search_kwargs={"k": 2}
        )
        self.qa = RetrievalQA.from_chain_type(
            llm=OpenAI(model_name="gpt-3.5-turbo"),
            chain_type="stuff",
            retriever=retrieval,
            return_source_documents=False,
            chain_type_kwargs=self.chain_type_kwargs,
        )

    # Define a method called get_answer which uses the qa attribute to get answer for the query.
    def get_answer(self, query):
        return self.qa(query)
