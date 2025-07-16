import os
from openai import OpenAI
from fastapi import FastAPI, Request
import json
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from models.fortune_engine import FortuneEngine

load_dotenv()  # 载入.env文件

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# 允许跨域请求（Vue 用在 localhost:5173 时必须要加）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://beaintech.github.io"],  # 实际部署时改成前端的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "MINGEN backend is running"}

@app.post("/submit")
async def submit(data: dict):
    # 1. 保存用户输入
    try:
        with open("submissions.json", "a", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
            f.write("\n")
    except Exception as e:
        return {"error": f"无法保存输入：{str(e)}"}

    # 2. 使用 FortuneEngine 分析
    try:
        engine = FortuneEngine(
            name=data.get("name"),
            birthday=data.get("birthday"),
            time=data.get("time"),
            birthplace=data.get("birthplace"),
            gender=data.get("gender", "未提供")
        )
        result = engine.analyze()
        return {"result": result}
    except Exception as e:
        return {"error": f"分析失败：{str(e)}"}

# @app.post("/submit")
# async def submit(data: dict):
#     name = data.get("name")
#     birthday = data.get("birthday")
#     time = data.get("time")
#     birthplace = data.get("birthplace")

#     prompt = f"""
# 你是一位风水大师，请根据以下信息生成用户的命理分析，包括八字排盘、五行平衡分析、命卦、吉凶方位、建议颜色和2025年的运势预测。尽量使用表格或结构化格式输出。

# 姓名：{name}
# 出生地：{birthplace}
# 出生日期：{birthday}
# 出生时间：{time}

# 请用中文回答，结果精炼但全面。
#     """

#     try:
#         response = client.chat.completions.create(
#             model="gpt-4.1", 
#             messages=[{"role": "user", "content": prompt}]
#         )
#         result = response.choices[0].message.content

#         return {"result": result}
#     except Exception as e:
#         return {"error": str(e)}
