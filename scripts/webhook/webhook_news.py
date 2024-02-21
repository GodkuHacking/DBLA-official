import aiohttp
import discord
from discord import Webhook, Embed
from bs4 import BeautifulSoup
import asyncio

# Define the webhook URL
WEBHOOK_URL = 'webhook_url'

# Function to fetch data from the URL and create an embed
async def fetch_and_send():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://dblegends.net/news') as response:
            if response.status == 200:
                # Parsing HTML content
                soup = BeautifulSoup(await response.text(), 'html.parser')
                # Finding the desired elements (news items)
                news_items = soup.find_all('div', class_='news-item newzooms')
                for news_item in news_items[:4]:  # Limit to the latest 4 news items
                    # Extracting data from the news item
                    news_title = news_item.find('h2').text.strip()
                    news_link = 'https://dblegends.net' + news_item.find('a')['href']
                    news_image = news_item.find('img')['src']
                    news_start_time = news_item.find('p').text.strip().split('Start Time: ')[1].split('～')[0]
                    news_end_time = news_item.find('p').text.strip().split('End Time: ')[1]
                    
                    # Creating an embed
                    embed = Embed(title=news_title, url=news_link, description=f"Start Time: {news_start_time}\nEnd Time: {news_end_time}")
                    embed.set_image(url=news_image)
                    
                    # Sending the embed to Discord using webhook
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(WEBHOOK_URL, session=session)
                        await webhook.send(embed=embed)
            else:
                print("Failed to fetch website content.")

# Run the async function
asyncio.run(fetch_and_send())
