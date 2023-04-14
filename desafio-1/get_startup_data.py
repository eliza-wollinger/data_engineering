import json
from typing import List, Dict
from psycopg2.extensions import AsIs


def read_startup_data(file_path: str) -> List[Dict]:
    with open(file_path) as json_file:
        data = json.load(json_file)
        return [
            {
                "id": startup["id"],
                "name": startup["company_name"],
                "description": startup["headline"],
                "location": startup["location"],
                "industry": startup["industries"][0]["industry_name"] if startup["industries"] else None,
                "employee_count": startup["employees"] if startup["employees"] else None,
                "website": startup["website"] if startup["website"] else None,
                "tags": startup["tags"] if startup["tags"] else None
            } for startup in data
        ]

    
def create_startup_table(cur):
    cur.execute('''
        CREATE TABLE IF NOT EXISTS startups (
            id SERIAL PRIMARY KEY,
            name TEXT,
            industry TEXT,
            location TEXT,
            employee_count INT,
            website TEXT,
            tags TEXT[],
            description TEXT,
            date_created TIMESTAMP DEFAULT NOW()
        );
    ''')


def insert_startup_data(cur, data):
    for startup in data:
        cur.execute('''
            INSERT INTO startups (
                id,
                name,
                industry,
                location,
                employee_count,
                website,
                tags,
                description
            ) VALUES (
                %(id)s,
                %(name)s,
                %(industry)s,
                %(location)s,
                %(employee_count)s,
                %(website)s,
                %(tags)s,
                %(description)s
            )
        ''', startup)