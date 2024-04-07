import aiohttp
import asyncio

async def fetch_data(prompt):
    url = "http://localhost:3000/user_prompt"
    params = {'user_prompt': prompt}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                return await response.json()  # Asynchronously get JSON response
            else:
                return {'error': 'Failed to fetch data', 'status_code': response.status}

async def main():
    result = await fetch_data("soccer")
    print(result)

# [{'brxId': '2f2f590e-4c12-4d11-9c4e-fc30a033ffbf', 'brxName': 'Summaraize', 'topLevelBrx': True, 'brxRes': {'output': '{"url":"https://firebasestorage.googleapis.com/v0/b/brx-frontend.appspot.com/o/imgGen%2FdalleGen%2F2f2f590e-4c12-4d11-9c4e-fc30a033ffbf%2F234f8caf-9e6f-4095-a0a7-70dad6d7fbf8%2Fcd42214f-1e05-47a3-ac91-00218fb411f9?alt=media&token=7b7fe302-258e-4749-b39f-943ce8ee39fc","revised_prompt":"An action-packed scene on a soccer field. A Middle-Eastern female player, in a blue and white uniform, is skillfully dribbling the ball, avoiding her opponents: a Caucasian male player in red and a South Asian female player in green. The audience in the stands are a mix of different descents, all cheering enthusiastically. Clear blue skies overhead and a lush, green field underfoot. The goal post is visible in the distance with black and a Hispanic female goalkeeper ready to defend."}'}}]


asyncio.run(main())