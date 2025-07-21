from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from submissions import save_submission
from models.fortune_engine import FortuneEngine

app = FastAPI()

# CORS（Render 或本地前端访问时）
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],  # 部署时可以换成具体域名
    allow_origins=["https://beaintech.github.io"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 基础报告接口
@app.post("/generate-basic-report")
async def generate_basic(data: dict):
    try:
        engine = FortuneEngine(
            name=data.get("name"),
            birthday=data.get("birthday"),
            time=data.get("time"),
            birthplace=data.get("birthplace"),
            gender=data.get("gender", "未提供")
        )
# save submit data to SQLite and generate fortune report

        result = engine.analyze_basic()
        save_submission(data, result, report_type="basic")  # 确保保存数据
        return {"result": result}
    except Exception as e:
        return {"error": f"生成报告失败：{str(e)}"}


# 高级报告接口（付费）

@app.post("/generate-extra-report")
async def generate_extra(data: dict):
    try:
        engine = FortuneEngine(
            name=data.get("name"),
            birthday=data.get("birthday"),
            time=data.get("time"),
            birthplace=data.get("birthplace"),
            gender=data.get("gender", "未提供")
        )
        result = engine.analyze_extra()
        save_submission(data, result, report_type="extra")  # 确保保存数据
        return {"result": result}
    except Exception as e:
        return {"error": f"高级报告生成失败：{str(e)}"}
    
@app.get("/")
async def root():
    return {"message": "MINGEN backend is running"}


# @app.post("/submit")
# async def submit(data: dict):
#     try:
#         # 保存到 SQLite 数据库
#         save_submission(data)
#     except Exception as e:
#         return {"error": f"无法保存输入：{str(e)}"}

#     # 使用 FortuneEngine 生成报告
#     try:
#         engine = FortuneEngine(
#             name=data.get("name"),
#             birthday=data.get("birthday"),
#             time=data.get("time"),
#             birthplace=data.get("birthplace"),
#             gender=data.get("gender", "未提供")
#         )
#         result = engine.analyze()
#         return {"result": result}
#     except Exception as e:
#         return {"error": f"分析失败：{str(e)}"}
    



# save submit data to submission json file

# import os
# from openai import OpenAI
# from fastapi import FastAPI, Request
# import json
# from fastapi.middleware.cors import CORSMiddleware
# from dotenv import load_dotenv
# from models.fortune_engine import FortuneEngine

# load_dotenv()  # 载入.env文件

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# app = FastAPI()

# # 允许跨域请求（Vue 用在 localhost:5173 时必须要加）
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # 实际部署时改成前端的域名
#     # allow_origins=["https://beaintech.github.io"], 
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# async def root():
#     return {"message": "MINGEN backend is running"}

# @app.post("/submit")
# async def submit(data: dict):
#     # 1. 保存用户输入
#     try:
#         with open("submissions.json", "a", encoding="utf-8") as f:
#             json.dump(data, f, ensure_ascii=False)
#             f.write("\n")
#     except Exception as e:
#         return {"error": f"无法保存输入：{str(e)}"}

#     # 2. 使用 FortuneEngine 分析
#     try:
#         engine = FortuneEngine(
#             name=data.get("name"),
#             birthday=data.get("birthday"),
#             time=data.get("time"),
#             birthplace=data.get("birthplace"),
#             gender=data.get("gender", "未提供")
#         )
#         result = engine.analyze()
#         return {"result": result}
#     except Exception as e:
#         return {"error": f"分析失败：{str(e)}"}
