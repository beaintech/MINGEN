# fortune_engine.py

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class FortuneEngine:
    def __init__(self, name, birthday, time, birthplace, gender="未提供"):
        self.name = name
        self.birthday = birthday
        self.time = time
        self.birthplace = birthplace
        self.gender = gender

    def generate_prompt(self):
#         return f"""
# 你是一位风水大师，请根据以下信息生成用户的命理分析，包括八字排盘、五行平衡分析、命卦、吉凶方位、建议颜色和2025年的运势预测。尽量使用表格或结构化格式输出。

# 姓名：{self.name}
# 出生地：{self.birthplace}
# 出生日期：{self.birthday}
# 出生时间：{self.time}

# 请用中文回答，结果精炼但全面。
#         """

         return f"""
你是一位灵性宇宙研究专家，专长于分析个体的星际种子起源。  
请根据以下提供的基本信息，为用户生成一份**星际种子报告**，内容包括：

1. 可能的星际种族起源（如：天狼星、昴宿星、大角星、猎户座、仙女星等）；
2. 与星际特质对应的性格特征与人生使命；
3. 灵魂使命路径和当下阶段；
4. 建议使用的疗愈方式（如声音疗愈、冥想、接触自然等）；
5. 对2025年的能量走向与宇宙支持做出简要预测。

请以中文输出，并使用结构化格式（可含表格），结果应富有洞察力，深入但清晰。

---

请以中文输出，并使用MARKDOWN格式生成结构化内容，表格需包含以下要求：

- 使用<table>标签，表头使用<th>，每行使用<tr>；
- 设置第一列宽度为35%，第二列为65%（或用 1fr / 2fr 的栅格样式）；
- 表格整体带边框，文字居左或居中，便于前端渲染展示；
- 若非表格部分，可使用段落 <p> 或 <h3> 组织。
- 所有内容请用中文回答，语言风格清晰、深刻但易于理解。

---
用户信息如下：

- 姓名：{self.name}  
- 性别：{self.gender}  
- 出生地：{self.birthplace}  
- 出生日期：{self.birthday}  
- 出生时间：{self.time}

---
"""

    def analyze(self):
        prompt = self.generate_prompt()
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
