# read_movies.py
# Reads all items from the DynamoDB Movies table and prints them.
# Part of Lab 09 — feature/read-dynamo branch

import boto3
from boto3.dynamodb.conditions import Key

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Video_Games"


def get_table():
    """Return a reference to the DynamoDB Games table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_games(game):
    title = game.get("Title", "Unknown Title")
    year = game.get("Year", "Unknown Year")
    developer = game.get("Developer", "Unknown Developer")
    genres = game.get("Genres", "Unknown Genres")

    print(f"  Title  : {title}")
    print(f"  Year   : {year}")
    print(f"  Developer: {developer}")
    print(f"  Genres  : {genres}")
    print()



def print_all_games():
    """Scan the entire Games table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No games found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} game(s):\n")
    for game in items:
        print_games(game)



def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_games()


if __name__ == "__main__":
    main()
