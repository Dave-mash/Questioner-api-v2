"""
This module contains all the database configurations
"""
import os 
import psycopg2


config_name = os.getenv('APP_SETTINGS')
development_url = os.getenv('Dev_URL')
testing_url = os.getenv('Test_URL')
production_url = os.getenv('DATABASE_URL')
conn = psycopg2.connect(development_url)

try:
    """Putting the connection in try """
    if config_name == 'development':
        conn = psycopg2.connect(development_url)
    if config_name == 'testing':
        conn = psycopg2.connect(testing_url)
    if config_name == 'production':
        conn = psycopg2.connect(production_url)
except BaseException:
    print("Database not connected!")

cur = conn.cursor()

def create_tables():
    """
    A fucntion to create all the tables
    """
    queries = tables()
    for q in queries:
        cur.execute(q)
    conn.commit()

def tables():
    users_table = """
                    CREATE TABLE IF NOT EXISTS Users (
                    id serial PRIMARY KEY NOT NULL,
                    first_name text NOT NULL,
                    last_name text NOT NULL,
                    othername text NOT NULL,
                    email text NOT NULL,
                    phoneNumber integer NOT NULL,
                    username text UNIQUE NOT NULL,
                    password text NOT NULL,
                    isAdmin text NOT NULL,
                    date_registered integer NOT NULL
                    )
                """
    meetups_table = """
                    CREATE TABLE IF NOT EXISTS meetups (
                    id serial PRIMARY KEY NOT NULL,
                    admin_id serial PRIMARY KEY NOT NULL,
                    location text NOT NULL,
                    topic text NOT NULL,
                    created_on integer NOT NULL,
                    description text NOT NULL,
                    schedule interger NOT NULL,
                    tags varChar NOT NULL
                    )
                """
    questions_table = """
                    CREATE TABLE IF NOT EXISTS users (
                    id serial PRIMARY KEY NOT NULL,
                    meetup_id serial PRIMARY KEY NOT NULL,
                    created_on integer NOT NULL,
                    created_by integer NOT NULL,
                    title text NOT NULL,
                    body text NOT NULL,
                    votes integer NOT NULL
                    )
                """

    queries = [users_table, questions_table,
               meetups_table]

    return queries