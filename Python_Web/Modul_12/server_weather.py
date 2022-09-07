import jinja2
import aiohttp_jinja2
from aiohttp import web

from clien_weather import meteoprog_response, meteo_response



@aiohttp_jinja2.template('index.html')
async def get_temp(request):
    context = {
        'head_1': meteoprog_response[2],
        'head_2': meteoprog_response[3],
        'cur_temp': meteoprog_response[4],
        'desc_weather': meteoprog_response[5],
        'param': meteoprog_response[0],
        'param_val': meteoprog_response[1],
        'head_1_2': meteo_response[0],
        'head_2_2': meteo_response[1],
        'cur_temp_2': meteo_response[2],
        'desc_weather_2': meteo_response[3],
        'param_2': meteo_response[4],
        'param_val_2': meteo_response[5],
    }

    return context


if __name__ == "__main__":
    # run on http://127.0.0.1:8080/

    app = web.Application()

    # setup jinja2

    aiohttp_jinja2.setup(app,
                         loader=jinja2.FileSystemLoader(
                             './static/templates'
                         ))

    app.router.add_get('/', get_temp)
    app.router.add_static('/', 'static/', name="static", follow_symlinks=True)

    web.run_app(app)