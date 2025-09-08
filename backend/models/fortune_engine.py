import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class FortuneEngine:
    def __init__(
        self,
        name: str = "Unknown",
        birthday: str = None,
        time: str = "00:00",
        birthplace: str = None,
        gender: str = "Not Provided"
    ):
        self.name = name
        self.birthday = birthday
        self.time = time
        self.birthplace = birthplace
        self.gender = gender

    def generate_basic_prompt(self):
        return f"""
        You are a gentle and professional destiny & astrology advisor.

        Person A:
        - Name: {self.name}
        - Gender: {self.gender}
        - Birthday: {self.birthday}
        - Time: {self.time}
        - Birthplace: {self.birthplace}
        """

    def generate_extra_prompt(self):
        return f"""
        You are an astrology advisor focusing on love & wealth.

        Person A:
        - Name: {self.name}
        - Gender: {self.gender}
        - Birthday: {self.birthday}
        - Time: {self.time}
        - Birthplace: {self.birthplace}
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


    # 1. Helper: birthday → zodiac sign
    def get_zodiac_sign(self, date_str: str) -> str:
        if not date_str:
            return "Unknown"

        date = datetime.strptime(date_str, "%Y-%m-%d")
        day, month = date.day, date.month

        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "Aries"
        if (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "Taurus"
        if (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "Gemini"
        if (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "Cancer"
        if (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "Leo"
        if (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "Virgo"
        if (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "Libra"
        if (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "Scorpio"
        if (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "Sagittarius"
        if (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "Capricorn"
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "Aquarius"
        if (month == 2 and day >= 19) or (month == 3 and day <= 20):
            return "Pisces"

    # 2. Helper: zodiac → compatibility score
    def calc_score(self, sign1: str, sign2: str) -> int:
        zodiac_elements = {
            "Aries": "Fire", "Leo": "Fire", "Sagittarius": "Fire",
            "Taurus": "Earth", "Virgo": "Earth", "Capricorn": "Earth",
            "Gemini": "Air", "Libra": "Air", "Aquarius": "Air",
            "Cancer": "Water", "Scorpio": "Water", "Pisces": "Water"
        }

        e1, e2 = zodiac_elements.get(sign1), zodiac_elements.get(sign2)
        if not e1 or not e2:
            return 75  # fallback neutral

        if e1 == e2:
            return 92  # same element → strong match
        if (e1, e2) in [("Fire", "Air"), ("Air", "Fire"),
                        ("Earth", "Water"), ("Water", "Earth")]:
            return 85  # complementary elements
        return 72  # conflicting elements

    # 3. Inside your class
    def analyze_compatibility(self, other: "FortuneEngine"):
        sign1 = self.get_zodiac_sign(self.birthday)
        sign2 = self.get_zodiac_sign(other.birthday)
        score = self.calc_score(sign1, sign2)

        prompt = f"""
        You are a gentle and professional astrology advisor.

        Person A: {self.name}, {self.birthday}, {self.time}, {self.birthplace}, {self.gender}, Sun sign: {sign1}  
        Person B: {other.name}, {other.birthday}, {other.time}, {other.birthplace}, {other.gender}, Sun sign: {sign2}  

        IMPORTANT RULES (must follow exactly):
        1. The overall compatibility score has already been calculated = {score}%.
        - You MUST use this exact score.
        - Do NOT invent or change the percentage.
        2. Output format must be HTML only. 
        - Use <h3> for section headings.
        - Use <p> for normal text.
        - Use <table>, <tr>, <th>, <td> for structured data.
        - Each <tr> must be on a new line.
        3. Do NOT use Markdown tables (|---|). 
        4. Do NOT wrap the result in ``` or backticks.
        5. Do NOT bold numbers with ** or __.

        The report must follow this exact structure:

        <h3>Overall Compatibility</h3>
        <p>Overall compatibility score: {score}%</p>

        <h3>Detailed Breakdown</h3>
        <table>
        <tr><th>Aspect</th><th>Score (0–100)</th><th>Explanation</th></tr>
        <tr><td>Stability</td><td>...</td><td>Explain here</td></tr>
        <tr><td>Career</td><td>...</td><td>Explain here</td></tr>
        <tr><td>Security</td><td>...</td><td>Explain here</td></tr>
        <tr><td>Functionality</td><td>...</td><td>Explain here</td></tr>
        <tr><td>Romance</td><td>...</td><td>Explain here</td></tr>
        </table>

        <h3>Summary</h3>
        <p>Write exactly 5 warm and professional sentences summarizing the relationship.</p>

        End of instructions. Do not add any extra formatting.
        """

        response = client.chat.completions.create(
            model="gpt-4.1",
            temperature=0.2,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content


# class FortuneEngine:
#     def __init__(
#             self,
#             name: str = "Unknown",
#             birthday: str = None,
#             time: str = "00:00",
#             birthplace: str = None,
#             gender: str = "Not Provided"
#         ):
#             self.name = name
#             self.birthday = birthday
#             self.time = time
#             self.birthplace = birthplace
#             self.gender = gender

#     # def generate_basic_prompt(self):
# #        return f"""
# # 你是一位温和且专业的风水与命理导师，熟悉中国传统命理学与农历（阴历）排盘体系。  
# # 请严格依据以下步骤，为用户生成一份**准确的深度命理报告**，同时保持语气亲切，让用户感到被理解与引导：  

# # 1. **时间校准**：先将用户提供的公历出生日期（阳历）准确转换为农历日期（阴历），并标明转换结果；  
# # 2. **四柱排盘（年柱、月柱、日柱、时柱）**：基于农历日期及时辰，严格使用天干地支推算四柱，并明确说明每柱的五行属性及含义；  
# # 3. **五行平衡分析**：详细统计五行（金、木、水、火、土）分布，指出偏旺或不足的部分，并提出补救建议（生活习惯、环境、饰品）；  
# # 4. **命卦与吉凶方位**：基于出生年份和性别，确定命卦，给出适合的居住、办公、旅行方位；  
# # 5. **建议颜色与能量调和**：给出颜色、饰品、生活方式建议，帮助平衡个人能量；  
# # 6. **2025年总体运势**：细致分析事业、财运、健康、感情趋势，给出机会与提醒。

# # 请用 **MARKDOWN格式** 输出，且必须包含以下要求：
# # - 所有四柱结果明确标明**农历日期**、天干地支与五行属性；
# # - 使用 `<table>` 生成排版精美的两列表格，第一列宽度25%，第二列75%，表格带简单边框，文字居中或居左；
# # - 文字段落部分用 `<p>` 和 `<h3>` 标签组织，让内容流畅、温柔、有亲和力；
# # - 避免机械化语气，让用户有被理解、被安抚的感觉。

# # 用户信息如下（请先进行公历到农历转换）：  

# # - 姓名：{self.name}  
# # - 性别：{self.gender}  
# # - 出生地：{self.birthplace}  
# # - 公历出生日期：{self.birthday}  
# # - 出生时间：{self.time}  

# # 请严格按照中国传统命理规则（农历 + 天干地支）推算结果, 英语输出。

# # """

#     def generate_basic_prompt(self):
#         base_prompt = f"""
#         You are a gentle and professional destiny & astrology advisor...
#         [your existing instructions here]
        
#         Person A:
#         - Name: {self.name}
#         - Gender: {self.gender}
#         - Birthday: {self.birthday}
#         - Time: {self.time}
#         - Birthplace: {self.birthplace}
#         """

#         if self.second_birthday and self.second_birthplace:
#             base_prompt += f"""
#         Person B:
#         - Name: {self.second_name}
#         - Birthday: {self.second_birthday}
#         - Gender: {self.second_gender}
#         - Birthplace: {self.second_birthplace}
#         - Time: {self.second_time}
#         """

#             base_prompt += """
#         Please generate not only the personal fortune for Person A, but also a **compatibility analysis**
#         between Person A and Person B, covering:
#         - Overall compatibility score (percentage)
#         - Stability / Career / Security / Functionality / Romance (0–100 each, with explanation)
#         - 5-sentence summary
#         """

#         return base_prompt

#     def generate_extra_prompt(self):
#        return f"""
# 你是一位温和且专业的风水与命理导师，熟悉中国传统命理学与农历（阴历）排盘体系，善于以亲切温暖的语言为人解读情感与财富运势。  
# 请严格依据以下步骤，为用户生成一份**附加命理报告**，帮助用户了解情感和财富流动趋势：  

# 1. **时间校准**：先将用户的公历出生日期（阳历）转换为农历（阴历），标明转换后的日期；  
# 2. **基础命盘确认**：基于农历日期及时辰，使用天干地支核对四柱，并确认其对情感和财富的主要能量作用；  
# 3. **情感提示**：结合命盘和大运流年，温柔地指出用户在未来哪些年份或阶段容易遇到合适伴侣或情感突破，并给予如何保持吸引力、稳定关系的具体建议；  
# 4. **财富流动周期**：分析未来数年中，哪些年份或周期财运较旺、资源流动明显，给出职业发展、理财投资和技能提升的策略建议。

# 请用 **MARKDOWN 格式** 输出，并遵循以下要求：
# - 在报告开头标明 **公历→农历转换结果**（如果日期已知）；  
# - 使用 `<table>` 制作两列表格，第一列为25%宽度（标题），第二列为75%宽度（详细解读），表格需带边框，文字居中或居左；  
# - 文字段落部分使用 `<p>` 和 `<h3>` 标签，让报告阅读体验自然温暖；  
# - 避免生硬或机械的语气，让用户感到被理解和鼓励。

# 用户信息如下（请先进行公历到农历的日期转换）：  
# - 姓名：{self.name}  
# - 性别：{self.gender}  
# - 出生地：{self.birthplace}  
# - 公历出生日期：{self.birthday}  
# - 出生时间：{self.time}  

# 请结合传统命理（农历 + 天干地支）推算结果，并以温柔、鼓励的语气撰写报告, 英语输出。。
# """

#     def analyze_basic(self):
#         prompt = self.generate_basic_prompt()
#         response = client.chat.completions.create(
#             model="gpt-4.1",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response.choices[0].message.content

#     def analyze_extra(self):
#         prompt = self.generate_extra_prompt()
#         response = client.chat.completions.create(
#             model="gpt-4.1",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response.choices[0].message.content
    
    
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