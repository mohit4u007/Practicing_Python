# Asynchronous example
# This works in a file

import time
from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()

async def get_delay1():
	r = await asession.get('https://httpbin.org/delay/1')
	return r

async def get_delay2():
	r = await asession.get('https://httpbin.org/delay/2')
	return r

async def get_delay3():
	r = await asession.get('https://httpbin.org/delay/3')
	return r

t1 = time.perf_counter()

results = asession.run(get_delay1, get_delay2, get_delay3)

# Each item in the result list is a response object and can be interacted as such

for result in results:
	response = result.html.url
	print(response)

t2 = time.perf_counter()

print(f'Asynchronous: {t2 - t1} seconds')