CREATE TABLE "playroll" (
  "id" integer PRIMARY KEY,
  "team" varchar,
  "season_smart_year" integer,
  "payroll" integer,
  "inflation_adj_payroll" integer
);

CREATE TABLE "player_stats" (
  "id" integer PRIMARY KEY,
  "season" integer,
  "player" varchar,
  "age" integer
);

CREATE TABLE "salaries" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "season" integer,
  "salary" integer,
  "inflation_adj_salary" integer
);
