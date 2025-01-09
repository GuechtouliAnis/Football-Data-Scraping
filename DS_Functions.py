from bs4 import BeautifulSoup
import time
import requests

def scrap_clubs_links(league):
    """
    Scrapes the links to club pages from a given league page.

    Args:
        league (dict): A dictionary containing the league information. 
                       It should have the keys 'link' (URL of the league page) 
                       and 'main_table' (ID of the main table containing club links).

    Returns:
        dict: A dictionary where the keys are club names and the values are URLs to the club pages.

    Example:
        league = {
            'link': 'https://fbref.com/en/comps/9/Premier-League-Stats',
            'main_table': 'results2020-2021'
        }
        clubs = scrap_clubs_links(league)
    """
    Clubs = {}
    # Send a GET request to the league page URL
    response = requests.get(league['link'])
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Select the main table containing club links
        table = soup.select(f'#{league["main_table"]} tbody')
        if table:
            # Convert the table to a BeautifulSoup object
            table_html = str(table[0])
            table_soup = BeautifulSoup(table_html, 'html.parser')
            # Find all rows in the table
            clubs = table_soup.find_all('tr')
            for row in clubs:
                # Extract the club name and link
                Club = row.find('td', {'data-stat': 'team'}).text.strip()
                link = 'https://fbref.com/' + row.find('a')['href']
                # Add the club name and link to the dictionary
                Clubs[Club] = link
        else:
            print("Table not found on the page.")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
    return Clubs

def Scrap(table, club, keys, league):
    """
    Scrapes player data from a given table.

    Args:
        table (BeautifulSoup object): The HTML table containing player data.
        club (str): The name of the club.
        keys (list): A list of keys to extract from the table. 
                     Possible values include 'club', 'league', 'player', etc.
        league (str): The name of the league.

    Returns:
        list: A list of dictionaries, each containing player data.

    Example:
        table = BeautifulSoup(table_html, 'html.parser').select('table tbody')
        club = 'Manchester United'
        keys = ['club', 'league', 'player', 'goals']
        league = 'Premier League'
        players = Scrap(table, club, keys, league)
    """
    if table:
        # Convert the table to a BeautifulSoup object
        table_html = str(table[0])
        table_soup = BeautifulSoup(table_html, 'html.parser')
        # Find all rows in the table
        player_rows = table_soup.find_all('tr')
        player_data = []
        for row in player_rows:
            player_dict = {}
            for key in keys:
                if key == 'club':
                    # Add the club name to the player dictionary
                    player_dict[key] = club
                elif key == 'league':
                    # Add the league name to the player dictionary
                    player_dict[key] = league
                elif key == 'player':
                    # Add logic to extract player data
                    pass
                # Add more conditions for other keys
            # Append the player dictionary to the player data list
            player_data.append(player_dict)
        return player_data
    else:
        print("Table not found.")
        return []

def Scrap_ds(response, j):
    """
    Extracts data-stat values from a given table in the HTML response.

    Args:
        response (requests.Response): The HTTP response object containing the HTML page.
        j (str): The ID of the table to be scraped.

    Returns:
        list: A list of data-stat values extracted from the table, with 'club' and 'league' added.

    Example:
        response = requests.get('https://example.com')
        data_stat_values = Scrap_ds(response, 'table_id')
    """
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')
    # Select the table with the given ID
    table = soup.select(f'table#{j} tbody')
    # Convert the table to a BeautifulSoup object
    table_html = str(table[0])
    table_soup = BeautifulSoup(table_html, 'html.parser')
    # Find all rows in the table
    ds = table_soup.find_all('tr')
    # Extract data-stat values from the first row
    data_stat_values = [tag.get('data-stat') for tag in ds[0].find_all(['td', 'th'])]
    # Insert 'club' and 'league' into the list of data-stat values
    data_stat_values.insert(4, 'club')
    data_stat_values.insert(5, 'league')
    # Remove the last element from the list
    data_stat_values.pop()
    return data_stat_values

def Scrap_data(league, attr):
    """
    Scrapes player data from multiple clubs in a given league.

    Args:
        league (dict): A dictionary containing the league information. 
                       It should have the keys 'link' (URL of the league page), 
                       'main_table' (ID of the main table containing club links), 
                       and 'id' (unique identifier for the league).
        attr (dict): A dictionary where keys are attribute names and values are table IDs to be scraped.

    Returns:
        dict: A dictionary where keys are attribute names and values are lists of player data.

    Example:
        league = {
            'link': 'https://fbref.com/en/comps/9/Premier-League-Stats',
            'main_table': 'results2020-2021',
            'id': '9'
        }
        attr = {
            'goals': 'stats_goals',
            'assists': 'stats_assists'
        }
        data = Scrap_data(league, attr)
    """
    # Scrape the links to club pages
    Clubs = scrap_clubs_links(league)
    # Initialize the data dictionary with empty lists for each attribute
    data = {i: [] for i in attr.keys()}
    # Initialize the ds dictionary with None values
    ds = {att: None for att in attr.keys()}
    
    # Initialize ds outside the main loop
    for att, st_id in attr.items():
        # Scrape the data-stat values for the first club to initialize ds
        ds[att] = Scrap_ds(requests.get(list(Clubs.values())[0]), st_id + str(league['id']))
    
    cpt = 1
    for club, link in Clubs.items():
        # Send a GET request to the club page URL
        response = requests.get(link)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            for att, st_id in attr.items():
                # Select the table with the given ID
                table = soup.select(f'table#{st_id+str(league["id"])} tbody')
                # Scrape the player data from the table and append it to the data dictionary
                data[att].append(Scrap(table, club, ds[att], league['league']))
            print(f'{cpt} - {club} data scraped successfully')
            cpt += 1
            # Sleep for 7 seconds to avoid overwhelming the server
            time.sleep(7)
        else:
            print('status code : ', response.status_code)
            break
    return data
