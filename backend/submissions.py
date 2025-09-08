import sqlite3
from pathlib import Path

# 数据库文件路径
DB_PATH = Path(__file__).parent / "submissions.db"

# 初始化数据库（如果不存在就创建）
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            gender TEXT,
            birthday TEXT,
            time TEXT,
            birthplace TEXT,
            second_birthday TEXT,     -- 新增
            second_birthplace TEXT,   -- 新增
            second_gender TEXT,       -- 新增
            report_type TEXT,          -- 新增字段，用于区分 basic / extra
            full_report TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# 插入一条用户提交
def save_submission(data: dict, report: str = "", report_type: str = "basic"):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO submissions (name, gender, birthday, time, birthplace, report_type, full_report)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("name"),
        data.get("gender", "未提供"),
        data.get("birthday"),
        data.get("time"),
        data.get("birthplace"),
        report_type,
        report
    ))
    conn.commit()
    conn.close()

# 查询所有记录（调试用）
def get_all_submissions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM submissions ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

# 确保启动时初始化数据库
init_db()
