from db_connection import connect_to_db, close_db_connection
from get_nba_data import read_nba_data, create_nba_table, insert_nba_data
from get_startup_data import read_startup_data, create_startup_table, insert_startup_data


def main():
    # Connect to the database
    conn, cur = connect_to_db()
    
    # Read and insert NBA data
    nba_data = read_nba_data('nba_data.csv')
    create_nba_table(cur)
    insert_nba_data(cur, nba_data)
    
    # Read and insert Startup data
    startup_data = read_startup_data('startup_data.json')
    create_startup_table(cur)
    insert_startup_data(cur, startup_data)
    
    # Close the database connection
    close_db_connection(conn, cur)


if __name__ == '__main__':
    main()
