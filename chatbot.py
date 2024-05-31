from langchain_openai import OpenAI
from langchain.chains import LLMChain
from prompts import cart_assistant_prompt_template
from langchain.memory.buffer import ConversationBufferMemory

from dotenv import load_dotenv

import chainlit as cl

load_dotenv()


@cl.on_chat_start
def setup_multiple_chains():
    llm = OpenAI(model='gpt-3.5-turbo-instruct',
                 temperature=0)
    conversation_memory = ConversationBufferMemory(memory_key="chat_history",
                                                   max_len=200,
                                                   return_messages=True,
                                                   )
    llm_chain = LLMChain(llm=llm, prompt=cart_assistant_prompt_template, memory=conversation_memory)
    cl.user_session.set("llm_chain", llm_chain)

@cl.on_message
async def handle_message(message: cl.Message):
    user_message = message.content.lower()
    llm_chain = cl.user_session.get("llm_chain")
    response = await llm_chain.acall(user_message,
                                        callbacks=[cl.AsyncLangchainCallbackHandler()])

    response_key = "output" if "output" in response else "text"
    await cl.Message(response.get(response_key, "")).send()
