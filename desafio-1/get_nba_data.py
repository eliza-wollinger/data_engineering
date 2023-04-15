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
                "payroll": int(row["payroll"]).str.replace('$','').str.replace(',',''),
                "inflation_adj_payroll": int(row["inflationAdjPayroll"]).str.replace('$','').str.replace(',',''),
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
                "salary": int(row["salary"]).str.replace('$','').str.replace(',',''),
                "inflation_adj_salary": int(row["inflationAdjSalary"]).str.replace('$','').str.replace(',',''),
            }
            for row in csv_reader
        ]


def create_nba_table(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS playroll (
                id SERIAL PRIMARY KEY,
                team VARCHAR(255) NOT NULL,
                season_smart_year INTEGER NOT NULL,
                payroll MONEY NOT NULL,
                inflation_adj_payroll MONEY NOT NULL
            );

            CREATE TABLE IF NOT EXISTS "player_stats" (
                "id" SERIAL PRIMARY KEY,
                "season" INTEGER NOT NULL,
                "player" varchar,
                "age" INTEGER NOT NULL
            );

                CREATE TABLE IF NOT EXISTS "salaries" (
                "id" SERIAL PRIMARY KEY,
                "name" VARCHAR(255) NOT NULL,
                "season" INTEGER NOT NULL,
                "salary" MONEY NOT NULL,
                "inflation_adj_salary" MONEY NOT NULL
            );

            """
        )
        conn.commit()


def insert_nba_data(conn, playroll_data, player_stats_data, salaries_data: List[Dict]):
    with conn.cursor() as cur:
        for data in playroll_data:
            cur.execute(
                """
                INSERT INTO playroll
                (id, team, season_smart_year, payroll, inflation_adj_payroll)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    data["id"],
                    data["team"],
                    data["season_smart_year"],
                    data["payroll"],
                    data["inflation_adj_payroll"],
                ),
            )
        
        for data in player_stats_data:
            cur.execute(
                """
                INSERT INTO player_stats
                (id, season, player, age)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    data["id"],
                    data["season"],
                    data["player"],
                    data["age"],
                ),
            )

        for data in salaries_data:
            cur.execute(
                """
                INSERT INTO salaries
                (id, name, season, salary, inflation_adj_salary)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    data["id"],
                    data["name"],
                    data["season"],
                    data["salary"],
                    data["inflation_adj_salary"],
                ),
            )

        conn.commit()