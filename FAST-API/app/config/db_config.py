import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="ep-billowing-smoke-ai5rf94d-pooler.c-4.us-east-1.aws.neon.tech",
        port="5432",
        user="neondb_owner",
        password="npg_IBaq6Q3cgJvl",
        dbname="neondb"
    )