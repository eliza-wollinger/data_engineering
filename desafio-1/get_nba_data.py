import csv
from typing import List, Dict
from datetime import datetime
from psycopg2.extensions import AsIs


def read_players_data(file_path: str) -> List[Dict]:
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


def read_teams_data(file_path: str) -> List[Dict]:
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [
            {
                "id": int(row["TeamId"]),
                "abbreviation": row["abbreviation"],
                "team_name": row["Team"],
                "simple_name": row["Simple"],
                "location": row["Location"],
            }
            for row in csv_reader
        ]


def create_players_table(conn):
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


def create_teams_table(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS teams (
                id SERIAL PRIMARY KEY,
                abbreviation VARCHAR(255) NOT NULL,
                team_name VARCHAR(255) NOT NULL,
                simple_name VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()


def insert_players_data(conn, players_data: List[Dict]):
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


def insert_teams_data(conn, teams_data: List[Dict]):
    with conn.cursor() as cur:
        for team in teams_data:
            cur.execute(
                """
                INSERT INTO teams
                (abbreviation, team_name, simple_name, location)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    team["abbreviation"],
                    team["team_name"],
                    team["simple_name"],
                    team["location"],
                ),
            )
        conn.commit()
