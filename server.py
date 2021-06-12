
from aiohttp import web
import requests

from scanner import scan_port


async def health(request):
    return web.Response(text="<h1> Async Rest API using aiohttp : Health OK </h1>",
                        content_type='text/html')


async def get_crypto_info(request):
    url = "https://api.coingecko.com/api/v3/coins/bitcoin?localization=false&tickers=false&market_data=false&community_data=false&developer_data=false&sparkline=false"
    response = requests.get(url)
    if response.status_code in [200, 201]:
        return web.Response(text=response.text, content_type='application/json')
    else:
        return web.Response(text=str({"status": "failure", "status_code": response.status_code}))


async def scaner(request):
    ip = request.match_info.get('ip')
    start_port = int(request.match_info.get('begin_port'))
    finish_port = int(request.match_info.get('end_port'))
    result = []
    for i in range(start_port, finish_port):
        if scan_port(ip, i):
            result.append({"port": i, "state": "open"})
        else:
            result.append({"port": i, "state": "close"})

    return web.json_response(result)


async def init():
    app = web.Application()
    app.router.add_get("/", health)
    app.router.add_post("/v1/crypto/info", get_crypto_info)
    app.router.add_get("/scan/{ip}/{begin_port}/{end_port}", scaner)
    return app


if __name__ == "__main__":
    application = init()
    web.run_app(application, host='127.0.0.1', port=8000)