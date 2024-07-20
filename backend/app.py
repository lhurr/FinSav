from fastapi import FastAPI, HTTPException, WebSocket
from starlette.middleware.cors import CORSMiddleware
from langchain_community.llms import Ollama
from chainlit.utils import mount_chainlit
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from chainlit.auth import create_jwt
from chainlit.user import User
# import database

app = FastAPI()
# db = database.get_db()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.on_event("startup")
# async def startup():
#     await db.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await db.disconnect()


@app.get("/messages")
async def get_initial_message():
    return {"message": "Hello!"}

@app.get("/custom-auth")
async def custom_auth():
    token = create_jwt(User(identifier="Test User"))
    return JSONResponse({"token": token})

mount_chainlit(app=app, target="cl_app.py", path="/chainlit")


# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await manager.connect()
#     try:
#         while True:
#             text_data = await websocket.receive_text()
#             question = text_data
#             await manager.send_personal_message(f"Received:{question}",websocket)
#             topics = await _clarify_query_topics(question) # SQL Query
#             data = list()
#             if len(topics) == 0:
#                 chain = default_chat_chain()
#             else:
#                 companies = await _get_companies_from_query(question)
#                 if len(companies) == 0:
#                     chain = default_chat_chain()
#                 else:
#                     data = await _download_data(topics, companies)
#                     chain = synthesise_query_result_chain(companies, [d[0] for d in data])

#             for chunks in llm.stream(query):
#                 await websocket.send_text(chunks)
#             await websocket.send_text('**|||END|||**')
#     except Exception as e:
#         print(f'WebSocket error: {str(e)}')
#         websocket.close()
#     # finally:

#     #     await websocket.close()

