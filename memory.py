# memory.py
# Stage 2 - Nova V2 Memory System

import sqlite3
from datetime import datetime

DB_PATH = "nova_memory.db"


# ─────────────────────────────
# DATABASE SETUP
# ─────────────────────────────

def init():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        content TEXT,
        confidence REAL DEFAULT 1.0,
        created TEXT
    )
    """)

    conn.commit()
    conn.close()


init()


# ─────────────────────────────
# ADD MEMORY
# ─────────────────────────────

def add_memory(mem_type, content, confidence=1.0):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    INSERT INTO memory (type, content, confidence, created)
    VALUES (?, ?, ?, ?)
    """, (mem_type, content, confidence, datetime.now().isoformat()))

    conn.commit()
    conn.close()


# ─────────────────────────────
# GET MEMORIES
# ─────────────────────────────

def get_all():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT type, content, confidence, created FROM memory")
    rows = c.fetchall()

    conn.close()
    return rows


def get_by_type(mem_type):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    SELECT type, content, confidence, created
    FROM memory
    WHERE type = ?
    """, (mem_type,))

    rows = c.fetchall()
    conn.close()
    return rows


# ─────────────────────────────
# SEARCH MEMORY
# ─────────────────────────────

def search(query):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    SELECT type, content, confidence, created
    FROM memory
    WHERE content LIKE ?
    """, (f"%{query}%",))

    rows = c.fetchall()
    conn.close()
    return rows


# ─────────────────────────────
# SIMPLE HELPER
# ─────────────────────────────

def format_memories(rows):
    """Convert DB rows into readable text for AI context"""
    return "\n".join([
        f"[{r[0]}] {r[1]} (conf: {r[2]})"
        for r in rows
    ])