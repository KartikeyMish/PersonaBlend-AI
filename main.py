import textbase
from textbase.message import Message
from textbase import models
from textbase import prompts
from textbase import voice
import os
from typing import List

# Load your OpenAI API key
# models.OpenAI.api_key = "YOUR_API_KEY"
# models.HuggingFace.api_key = "YOUR_API_KEY"
# or from environment variable:

models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")
models.HuggingFace.api_key = os.getenv("HUGGING_API_KEY")
voice.distress.iam_user_access_key_id = os.getenv("IAM_ACCESS_KEY")
voice.distress.iam_user_secret_access_key = os.getenv("IAM_SECRET_ACCESS_KEY")
voice.distress.bucket_name = os.getenv("BUCKET_NAME")
voice.distress.object = os.getenv("OBJECT_NAME")


# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like. The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a pleasant chat!
"""


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    #Creating a model variable to store the model to be used
    
    model = models.HuggingFace #Default model
    
    # Tried to send distress audio to Responsible organizat (via AWS S3 & towilie) - but not able to finsih it due to wifi cut in my college :
    # Do check the code in textbase\voice.py for half implementation of the same
    # for promt in prompts.distress:
    #     if promt in message_history[-1].content:
    #         voice.distress.record()
    #         link = voice.distress.generate()
    #         voice.transcribe(link)

    # Using ChatGPT model if the last message contains any of the promts in promptsGPT
    for promt in prompts.gpt:
        if promt in message_history[-1].content:
            model = models.OpenAI

    # calling the generate function of the respective model  
    bot_response = model.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history
    )

    return bot_response, state