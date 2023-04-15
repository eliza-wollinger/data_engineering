import csv
from typing import List, Dict
from datetime import datetime
from psycopg2.extensions import AsIs


def read_playroll_data(file_path: str) -> List[Dict]:
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [
            {
                "id": int(row["Id"]),
                "name": row["Player"],
                "height": int(row["height (in)"]),
                "weight": int(row["weight (lbs)"]),
                "college": row["college"],
                "birthdate": datetime.strptime(row["birth_date"], "%Y-%m-%d"),
            }
            for row in csv_reader
        ]


def read_player_box_score_stats_data(file_path: str) -> List[Dict]:
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [
            {
                "id": int(row["Id"]),
                "name": row["Player"],
                "height": int(row["height (in)"]),
                "weight": int(row["weight (lbs)"]),
                "college": row["college"],
                "birthdate": datetime.strptime(row["birth_date"], "%Y-%m-%d"),
            }
            for row in csv_reader
        ]


def read_player_stats_data(file_path: str) -> List[Dict]:
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [
            {
                "id": int(row["Id"]),
                "name": row["Player"],
                "height": int(row["height (in)"]),
                "weight": int(row["weight (lbs)"]),
                "college": row["college"],
                "birthdate": datetime.strptime(row["birth_date"], "%Y-%m-%d"),
            }
            for row in csv_reader
        ]


def read_salaries_data(file_path: str) -> List[Dict]:
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [
            {
                "id": int(row["Id"]),
                "name": row["Player"],
                "height": int(row["height (in)"]),
                "weight": int(row["weight (lbs)"]),
                "college": row["college"],
                "birthdate": datetime.strptime(row["birth_date"], "%Y-%m-%d"),
            }
            for row in csv_reader
        ]


def create_nba_table(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                height INTEGER NOT NULL,
                weight INTEGER NOT NULL,
                college VARCHAR(255),
                birthdate DATE NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()


def insert_nba_data(conn, players_data: List[Dict]):
    with conn.cursor() as cur:
        for player in players_data:
            cur.execute(
                """
                INSERT INTO players
                (name, height, weight, college, birthdate)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    player["name"],
                    player["height"],
                    player["weight"],
                    player["college"],
                    player["birthdate"],
                ),
            )
        conn.commit()