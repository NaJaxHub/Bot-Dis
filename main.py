import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import requests
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# โหลด .env และดึง Token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# กำหนด PORT (Render ใช้ตัวแปร PORT)
PORT = int(os.environ.get("PORT", 8000))

# สร้าง FastAPI app
app = FastAPI()

messages = []

class Message(BaseModel):
    user: str
    user_id: int
    message: str

@app.get("/messages")
async def get_messages():
    return {"messages": messages}

@app.post("/save_message")
async def save_message(data: Message):
    messages.append(data.dict())
    return {"status": "success", "message": "Message saved successfully"}

# กำหนด intents
intents = discord.Intents.default()
intents.messages = True  
intents.members = True   

prefix = "s!"
client = commands.Bot(command_prefix=prefix, intents=intents)

@client.event
async def on_ready():
    print(f"✅ Login : {client.user}")  
    await asyncio.sleep(1)

@client.command()
async def red(ctx, *, message=None):
    allowed_user_ids = {1119509280480038972, 893294010762928149}
    if ctx.guild is None and ctx.author.id in allowed_user_ids:
        if message:
            await ctx.send(f"Code_Red : {message}")
            try:
                response = requests.post(f"https://your-render-url.com/save_message", json={
                    "user": ctx.author.name,
                    "user_id": ctx.author.id,
                    "message": message
                })
                if response.status_code == 200:
                    print("✅ ข้อความถูกบันทึกในเว็บเซิร์ฟเวอร์")
            except Exception as e:
                print(f"❌ เกิดข้อผิดพลาดในการส่งข้อมูลไปยังเว็บ: {e}")

# เรียกใช้บอทและ FastAPI
async def run_discord_bot():
    await client.start(TOKEN)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(run_discord_bot())
    uvicorn.run(app, host="0.0.0.0", port=PORT)
