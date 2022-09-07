import aiohttp
import asyncio
from bs4 import BeautifulSoup
from config import METEOPROG_URL, METEO_URL


async def fetch_to_meteoprog():
    async with aiohttp.ClientSession() as session:
        async with session.get(METEOPROG_URL) as response:
            text = await response.read()
            result = BeautifulSoup(text, 'lxml').find('section',
                                                      class_="main-top")

            head_1 = result.find('span').text

            head_2 = result.find('h2').text
            current_temp = result.find('div', class_="today-temperature").text
            desc = result.find('h3').text

            params = result.findAll('th')

            params_value = result.findAll('td')

            return params, params_value, head_1, head_2, current_temp, desc


async def fetch_to_meteo():

    async with aiohttp.ClientSession() as session:
        async with session.get(METEO_URL) as response:
            text = await response.read()
            result = BeautifulSoup(text, "lxml").find('div', class_="weather-detail__main")
            head_1 = 'Погода в Києві на сьогодні'
            head_2 = result.find('div', class_="weather-detail__main-title").text.replace('\n', '')
            current_temp = result.find('div', class_="weather-detail__main-temp").text
            desc = result.find('div', class_="weather-detail__main-specification").text
            params = result.findAll('div', class_="weather-detail__extra-caption")
            params_value = result.findAll('div', class_="weather-detail__extra-data")

            return head_1, head_2, current_temp, desc, params, params_value


async def main():
    sites = asyncio.gather(fetch_to_meteoprog(), fetch_to_meteo())
    return await sites


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
responses = asyncio.run(main())
meteoprog_response = responses[0]
meteo_response = responses[1]