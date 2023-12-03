import base64
import json
import logging
import os

if os.getenv('API_ENV') != 'production':
    from dotenv import load_dotenv

    load_dotenv()


from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from lotify.client import Client


import uvicorn

logging.basicConfig(level=os.getenv('LOG', 'WARNING'))
logger = logging.getLogger(__file__)

app = FastAPI()

# TODO: check CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


client = Client()


@app.post('/sub')
async def publisher(request: Request):
    # pub: {"order_id": 22, "name":"居西批全家優惠碼"}
    body = await request.body()
    body = json.loads(body.decode())
    logger.info(f"Publisher original data is: {str(body)}")
    data = body.get('message').get('data')
    logger.info(f"Publisher content data is: {str(data)}")
    if data is None:
        return None
    else:
        data = json.loads(base64.b64decode(data))
        logger.info(f"Publisher data format struct: {str(data)}")

    if data.get('order_id') != None:
        response = client.send_message(
            access_token=os.environ.get('LOTIFY_ACCESS_TOKEN', 'xxx'),
            message=f"\n[NAME]\n訂單編號: {data.get('order_id')}\n訂單內容: {data.get('name')}")
        print(response)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', default=8000))
    debug = True if os.environ.get(
        'API_ENV', default='develop') == 'develop' else False
    logging.info('Application will start...')
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=debug)
