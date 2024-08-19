import psycopg2
from connect import connect_database


def main():
    connect_database()

if __name__ == "__main__":
    main()