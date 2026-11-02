import sqlite3
import psycopg2
DB_PATH = 'postgresql://neondb_owner:npg_scTmqO3PWr9F@ep-bitter-bar-bbh8p46f-pooler.c-15.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require'

def get_connection():
    return psycopg2.connect(DB_PATH)