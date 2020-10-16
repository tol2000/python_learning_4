import logging
from aiohttp import web

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s [LINE:%(lineno)-10d] # %(levelname)-8s [%(asctime)s] %(message)s"
)

dict_of = {
    "/": ("welcome", "omq_welcome.sql", "text/html"),
    "/prometheus_metrics/sessions": ("sessions", "omq_sessions.sql", "text"),
    "/prometheus_metrics/kirill": ("kirill", "omq_kirill_metrics.sql", "text"),
    "/json": ("json_test", "omq_json.sql", "application/json")
}


async def handler(request):
    choice = dict_of[request.path]
    response = web.Response(text=f"<h3>Hello, mode {choice[0]} with sql file {choice[1]}!</h3>")
    response.content_type = choice[2]
    return response


app = web.Application()
app.add_routes(
    [
        web.get(path=x, handler=handler) for x in dict_of.keys()
    ]
)
web.run_app(app=app, host="localhost", port=3001)
