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

    def generate_basic_prompt(self):
       return f"""
你是一位温和而睿智的风水与命理导师，擅长用通俗易懂的语言帮助人们看清自己的运势与方向。  
请根据以下信息，为用户生成一份**深度命理报告**，语气亲切、有温度，让用户感到被理解和引导。  
报告应包含以下内容：

1. **八字排盘**：清楚列出年柱、月柱、日柱、时柱，并解释它们所象征的能量与对生活的影响；
2. **五行平衡分析**：说明五行（金木水火土）的分布，指出偏旺或不足的部分，告诉用户如何通过生活习惯、环境或饰品来调和；
3. **命卦与吉凶方位**：推荐适合的居住、办公或旅行方向，帮助提升好运；
4. **建议颜色与日常能量调和**：告诉用户什么颜色、饰品、生活方式能帮助平衡能量；
5. **2025年总体运势**：细致分析事业、财运、健康、感情的趋势，提醒机会点和需要注意的地方；

请以**MARKDOWN格式**输出，结构需清晰易读，并包含以下元素：
- **表格部分**：仅两列，第一列为25%宽度（标题），第二列为75%宽度（详细解读），用 `<table>` 和 `<th>` `<tr>` 标签；表格加上简单边框，内容居中或居左即可。
- **文字部分**：用 `<p>` 段落和 `<h3>` 标题分段，让报告阅读体验流畅，不生硬。
- 语言要温柔而具体，不要像机械报告，要让用户感到被理解和鼓励。

用户信息如下：

- 姓名：{self.name}  
- 性别：{self.gender}  
- 出生地：{self.birthplace}  
- 出生日期：{self.birthday}  
- 出生时间：{self.time}

"""
    
    def generate_extra_prompt(self):
       return f"""
你是一位温和而睿智的风水与命理导师，擅长用通俗易懂的语言帮助人们看清自己的运势与方向。  
请根据以下信息，为用户生成一份**深度命理报告**，语气亲切、有温度，让用户感到被理解和引导。  
报告应包含以下内容：

6. **情感提示**：温柔地指出用户可能遇到合适伴侣的大致年份或阶段，并告诉他们如何保持吸引力与情感平衡；
7. **财富流动周期**：分析未来几年中财运上升的时段，以及应采取的行动策略（例如职业、投资或学习方向）。

请以**MARKDOWN格式**输出，结构需清晰易读，并包含以下元素：
- **表格部分**：仅两列，第一列为25%宽度（标题），第二列为75%宽度（详细解读），用 `<table>` 和 `<th>` `<tr>` 标签；表格加上简单边框，内容居中或居左即可。
- **文字部分**：用 `<p>` 段落和 `<h3>` 标题分段，让报告阅读体验流畅，不生硬。
- 语言要温柔而具体，不要像机械报告，要让用户感到被理解和鼓励。

用户信息：  
- 姓名：{self.name}  
- 性别：{self.gender}  
- 出生地：{self.birthplace}  
- 出生日期：{self.birthday}  
- 出生时间：{self.time}
"""

    def analyze_basic(self):
        prompt = self.generate_basic_prompt()
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def analyze_extra(self):
        prompt = self.generate_extra_prompt()
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    
    
    #          return f"""
# 你是一位灵性宇宙研究专家，专长于分析个体的星际种子起源。  
# 请根据以下提供的基本信息，为用户生成一份**星际种子报告**，内容包括：

# 1. 可能的星际种族起源（如：天狼星、昴宿星、大角星、猎户座、仙女星等）；
# 2. 与星际特质对应的性格特征与人生使命；
# 3. 灵魂使命路径和当下阶段；
# 4. 建议使用的疗愈方式（如声音疗愈、冥想、接触自然等）；
# 5. 对2025年的能量走向与宇宙支持做出简要预测。

# 请以中文输出，并使用结构化格式（可含表格），结果应富有洞察力，深入但清晰。

# ---

# 请以中文输出，并使用MARKDOWN格式生成结构化内容，表格需包含以下要求：

# - 使用<table>标签，表头使用<th>，每行使用<tr>；
# - 设置第一列宽度为25%，第二列为75%（或用 1fr / 2fr 的栅格样式）；
# - 表格整体带边框，文字居左或居中，便于前端渲染展示；
# - 若非表格部分，可使用段落 <p> 或 <h3> 组织。
# - 所有内容请用中文回答，语言风格清晰、深刻但易于理解。

# ---
# 用户信息如下：

# - 姓名：{self.name}  
# - 性别：{self.gender}  
# - 出生地：{self.birthplace}  
# - 出生日期：{self.birthday}  
# - 出生时间：{self.time}

# ---
# """