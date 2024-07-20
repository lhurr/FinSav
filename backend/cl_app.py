from langchain.schema.runnable.config import RunnableConfig
import chainlit as cl
from schema import Message
import io
from matplotlib import pyplot as plt
from src.runner import clarify_query_topics, get_companies_from_query, download_data, default_chat_chain, \
    synthesise_query_result_chain
from starlette.responses import StreamingResponse
from database import get_db
from pydantic import BaseModel
from typing import Optional

# class MessageRequest(BaseModel):
#     user_id: int
#     session_id: Optional[int] = None
#     message: str

# class AIResponse(BaseModel):
#     ai_response: Optional[str]
#     image_url: Optional[str]
#     session_id: Optional[int]

# db = get_db()



@cl.step
async def _clarify_query_topics(question):
    topics = clarify_query_topics(question)
    return list(topics)


@cl.step
async def _get_companies_from_query(question):
    return list(get_companies_from_query(question))


@cl.step
async def _download_data(topics, companies) -> list:
    return list(download_data(topics, companies))

def create_img(fig):
    img_buf = io.BytesIO()
    fig.savefig(img_buf, format='png')
    img_buf.seek(0)
    # plt.close(fig)
    return img_buf


@cl.on_message
async def on_message(message: cl.Message):

    question = message.content

    topics = await _clarify_query_topics(question) # SQL Query
    print(topics)
    data = list()
    if len(topics) == 0:
        chain = default_chat_chain()
    else:
        companies = await _get_companies_from_query(question)
        if len(companies) == 0:
            chain = default_chat_chain()
        else:
            data = await _download_data(topics, companies)
            chain = synthesise_query_result_chain(companies, [d[0] for d in data])

    msg = cl.Message(content="", author='FinSav')
    output_msg = ""
    await msg.send()


    async for chunk in chain.astream(
        {"question": question},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        # print(chunk)
        await msg.stream_token(chunk)
        output_msg += chunk

    for _, fig in data:
        if fig is not None:
            try:
                plot_fn = cl.Pyplot(figure=fig, display="inline", size='medium')
                msg.elements.append(plot_fn)
            except:
                plot_fn = cl.Plotly(figure=fig, display="inline", size='medium')
                msg.elements.append(plot_fn)

        else:
            print("No Graph")


    await msg.send()
    return msg


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="""**Welcome to FinSav** \n
Get real-time information about the realm of finance! \n
""", author='FinSav').send()
    # cl.user_session.set("id", 0)