from services.ai_config import NiftyBridgeAI
from fastapi import FastAPI

# Create FastAPI instance.
app = FastAPI()


# Define a route for handling incoming POST requests with a parameter called "message".
@app.post("/{question}")
async def setup_chat(question: str) -> dict[str, str]:
    """
    Handles incoming POST requests with a parameter called "message" and returns a response.

    Args:
        message (str): The message to be sent to the NiftyBridgeAI class.

    Returns:
        dict[str, str]: A dictionary containing the answer from NiftyBridgeAI as the response to the request.
                        If an error occurs, it will return a dictionary containing an "error" key with
                        the error message as the value.
    """
    try:
        # Create an instance of NiftyBridgeAI class.
        nifty_ai = NiftyBridgeAI()

        # Get the answer from the query using the get_answer method of NiftyBridgeAI instance.
        answer = nifty_ai.get_answer(query=question)

        # If the answer contains "I'm sorry", return appropriate response.
        if "I'm sorry" in answer["result"]:
            return "I don't know please contact with support by email support@nifty-bridge.com"

        # Return the answer as the response to the request.
        return answer

    except Exception as e:
        # If any exception occurs, return the error message as the response.
        return {"error": str(e)}
