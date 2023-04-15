import csv
from typing import List, Dict


def read_playroll_data(file_path: str) -> List[Dict]:
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [
            {
                "id": int(row["id"]),
                "team": row["team"],
                "season_smart_year": int(row["seasonStartYear"]),
                "payroll": int(row["payroll"]),
                "inflation_adj_payroll": int(row["inflationAdjPayroll"]),
            }
            for row in csv_reader
        ]


def read_player_stats_data(file_path: str) -> List[Dict]:
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [
            {
                "id": int(row["Unnamed: 0 "]),
                "season": int(row["Season"]),
                "player": row["Player"],
                "age": int(row["Age"]),
            }
            for row in csv_reader
        ]


def read_salaries_data(file_path: str) -> List[Dict]:
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [
            {
                "id": int(row[""]),
                "name": row["playerName"],
                "season": int(row["seasonStartYear"]),
                "salary": int(row["salary"]),
                "inflation_adj_salary": int(row["inflationAdjSalary"]),
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