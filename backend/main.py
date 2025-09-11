import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from openai import OpenAI
from models.fortune_engine import FortuneEngine

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],
    allow_origins=["https://beaintech.github.io"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "MINGEN backend is running"}

@app.post("/submit")
async def submit(data: dict):
    try:
        with open("submissions.json", "a", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
            f.write("\n")
    except Exception as e:
        return {"error": f"无法保存输入：{str(e)}"}
    try:
        try:
            engine = FortuneEngine(
                name=data.get("name"),
                birthday=data.get("birthday"),
                time=data.get("time"),
                birthplace=data.get("birthplace"),
                gender=data.get("gender", "未提供"),
                client=client
            )
        except TypeError:
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

@app.post("/generate-basic-report")
async def generate_basic(data: dict):
    try:
        try:
            engine = FortuneEngine(
                name=data.get("name"),
                birthday=data.get("birthday"),
                time=data.get("time"),
                birthplace=data.get("birthplace"),
                gender=data.get("gender", "Not Provided"),
                client=client
            )
        except TypeError:
            engine = FortuneEngine(
                name=data.get("name"),
                birthday=data.get("birthday"),
                time=data.get("time"),
                birthplace=data.get("birthplace"),
                gender=data.get("gender", "Not Provided")
            )
        if hasattr(engine, "analyze_basic"):
            result = engine.analyze_basic()
        else:
            result = engine.analyze()
        with open("submissions.json", "a", encoding="utf-8") as f:
            json.dump({"type": "basic", "payload": data, "result": result}, f, ensure_ascii=False)
            f.write("\n")
        return {"result": result}
    except Exception as e:
        return {"error": f"生成报告失败：{str(e)}"}

@app.post("/generate-extra-report")
async def generate_extra(data: dict):
    try:
        try:
            engine = FortuneEngine(
                name=data.get("name"),
                birthday=data.get("birthday"),
                time=data.get("time"),
                birthplace=data.get("birthplace"),
                gender=data.get("gender", "Not Provided"),
                client=client
            )
        except TypeError:
            engine = FortuneEngine(
                name=data.get("name"),
                birthday=data.get("birthday"),
                time=data.get("time"),
                birthplace=data.get("birthplace"),
                gender=data.get("gender", "Not Provided")
            )
        if hasattr(engine, "analyze_extra"):
            result = engine.analyze_extra()
        else:
            result = engine.analyze()
        with open("submissions.json", "a", encoding="utf-8") as f:
            json.dump({"type": "extra", "payload": data, "result": result}, f, ensure_ascii=False)
            f.write("\n")
        return {"result": result}
    except Exception as e:
        return {"error": f"高级报告生成失败：{str(e)}"}

@app.post("/generate-compatibility-report")
async def generate_compatibility(data: dict):
    try:
        try:
            person1 = FortuneEngine(
                name=data.get("name"),
                birthday=data.get("birthday"),
                time=data.get("time"),
                birthplace=data.get("birthplace"),
                gender=data.get("gender", "Not Provided"),
                client=client
            )
        except TypeError:
            person1 = FortuneEngine(
                name=data.get("name"),
                birthday=data.get("birthday"),
                time=data.get("time"),
                birthplace=data.get("birthplace"),
                gender=data.get("gender", "Not Provided")
            )
        try:
            person2 = FortuneEngine(
                name=data.get("second_name"),
                birthday=data.get("second_birthday"),
                time=data.get("second_time"),
                birthplace=data.get("second_birthplace"),
                gender=data.get("second_gender", "Not Provided"),
                client=client
            )
        except TypeError:
            person2 = FortuneEngine(
                name=data.get("second_name"),
                birthday=data.get("second_birthday"),
                time=data.get("second_time"),
                birthplace=data.get("second_birthplace"),
                gender=data.get("second_gender", "Not Provided")
            )
        if hasattr(person1, "analyze_compatibility"):
            result = person1.analyze_compatibility(person2)
        else:
            a = person1.analyze()
            b = person2.analyze()
            result = f"<h3>Compatibility</h3><p>Person A:</p>{a}<p>Person B:</p>{b}"
        with open("submissions.json", "a", encoding="utf-8") as f:
            json.dump({"type": "compatibility", "payload": data, "result": result}, f, ensure_ascii=False)
            f.write("\n")
        return {"result": result}
    except Exception as e:
        return {"error": f"生成兼容性报告失败：{str(e)}"}


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
