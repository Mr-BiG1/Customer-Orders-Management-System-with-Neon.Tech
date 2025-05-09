# Darsan Sabu George 
# 2025-04-16
# PROG2390 
# 8959922
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        sslmode=os.getenv("DB_SSLMODE")
    )
