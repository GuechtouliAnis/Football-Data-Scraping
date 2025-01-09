import DS_Functions as dsf
import pandas as pd

# Define the season
season = "23_24"

# Define the attributes and their corresponding table IDs
attr = {'Goalkeeping': 'stats_keeper_', 'Goalkeeping_adv': 'stats_keeper_adv_','Defense': 'stats_defense_',
        'Shooting': 'stats_shooting_','Passing': 'stats_passing_','Pass_types': 'stats_passing_types_',
        'GCA': 'stats_gca_','Possession': 'stats_possession_','Playing_time': 'stats_playing_time_','Misc': 'stats_misc_'}

# Define the leagues and their corresponding information
Leagues = {
    'Premier League'  :{'id':9,'link':'https://fbref.com/en/comps/9/Premier-League-Stats','league':'Premier League',
                        'main_table':'results2023-202491_overall','season':'2023-2024','country':'England'},#Done
    
    'EFL'             :{'id':10,'link':'https://fbref.com/en/comps/10/Championship-Stats','league':'EFL',
                        'main_table':'results2023-2024101_overall','season':'2023-2024','country':'England'},#Done
    
    'Serie A'         :{'id':11,'link':'https://fbref.com/en/comps/11/Serie-A-Stats','league':'Serie A',
                        'main_table':'results2023-2024111_overall','season':'2023-2024','country':'Italy'},#Done
    
    'La Liga'         :{'id':12,'link':'https://fbref.com/en/comps/12/La-Liga-Stats','league':'La Liga',
                        'main_table':'results2023-2024121_overall','season':'2023-2024','country':'Spain'},#Done
    
    'Ligue 1'         :{'id':13,'link':'https://fbref.com/en/comps/13/Ligue-1-Stats','league':'Ligue 1',
                        'main_table':'results2023-2024131_overall','season':'2023-2024','country':'France'},#Done
    
    'Segunda Division':{'id':17,'link':'https://fbref.com/en/comps/17/Segunda-Division-Stats','league':'Segunda Division',
                        'main_table':'results2023-2024171_overall','season':'2023-2024','country':'Spain'},#Done
    
    'Serie B'         :{'id':18,'link':'https://fbref.com/en/comps/18/Serie-B-Stats','league':'Serie B',
                        'main_table':'results2023-2024181_overall','season':'2023-2024','country':'Italy'},#Done
    
    'Bundesliga'      :{'id':20,'link':'https://fbref.com/en/comps/20/Bundesliga-Stats','league':'Bundesliga',
                        'main_table':'results2023-2024201_overall','season':'2023-2024','country':'Germany'},#Done
    
    'Primera Division':{'id':21,'link':'https://fbref.com/en/comps/21/2023/2023-Primera-Division-Stats','league':'Primera Division',
                        'main_table':'results2023211_overall','season':'2023','country':'Argentina'},#Done
    
    'MLS_east'        :{'id':22,'link':'https://fbref.com/en/comps/22/2023/2023-Major-League-Soccer-Stats','league':'MLS',
                        'main_table':'results2023221Eastern-Conference_overall','season':'2023','country':'USA'},#Done
    
    'MLS_west'        :{'id':22,'link':'https://fbref.com/en/comps/22/2023/2023-Major-League-Soccer-Stats','league':'MLS',
                        'main_table':'results2023221Western-Conference_overall','season':'2023','country':'USA'},#Done
    
    'Eredivisie'      :{'id':23,'link':'https://fbref.com/en/comps/23/Eredivisie-Stats','league':'Eredivisie',
                        'main_table':'results2023-2024231_overall','season':'2023-2024','country':'Netherlands'},#Done
    
    'Brazilian League':{'id':24,'link':'https://fbref.com/en/comps/24/2023/2023-Serie-A-Stats','league':'Brazilian League',
                        'main_table':'results2023241_overall','season':'2023','country':'Brazil'},#Done
    
    'Liga MX'         :{'id':31,'link':'https://fbref.com/en/comps/31/Liga-MX-Stats','league':'Liga MX',
                        'main_table':'results2023-2024310_overall','season':'2023-2024','country':'Mexico'},#Done
    
    'Premeira Liga'   :{'id':32,'link':'https://fbref.com/en/comps/32/Primeira-Liga-Stats','league':'Primeira Liga',
                        'main_table':'results2023-2024321_overall','season':'2023-2024','country':'Portugal'},#Done
    
    '2. Bundesliga'   :{'id':33,'link':'https://fbref.com/en/comps/33/2-Bundesliga-Stats','league':'2. Bundesliga',
                        'main_table':'results2023-2024331_overall','season':'2023-2024','country':'Germany'},#Done
    
    'Pro League'      :{'id':37,'link':'https://fbref.com/en/comps/37/Belgian-Pro-League-Stats','league':'Pro League',
                        'main_table':'results2023-2024370_overall','season':'2023-2024','country':'Belgium'},#Done
    
    'Ligue 2'         :{'id':60,'link':'https://fbref.com/en/comps/60/Ligue-2-Stats','league':'Ligue 2',
                        'main_table':'results2023-2024601_overall','season':'2023-2024','country':'France'}#Done
}

def main(Leagues, attr):
    """
    Main function to scrape data from multiple leagues and export it to CSV files.

    Args:
        Leagues (dict): A dictionary containing information about various leagues.
        attr (dict): A dictionary where keys are attribute names and values are table IDs to be scraped.
    """
    # Choose a league
    league = Leagues['Premier League']
    # Scrape data for the chosen league
    Data = dsf.Scrap_data(league, attr)
    # Dictionary that will host the concatenated dataframes
    total_data = {}
    for i, j in Data.items():
        # Concatenate the dataframes for each attribute
        total_data[i] = pd.concat(j, ignore_index=True)
    # Export the scraped data into CSV files
    for attribute in total_data.keys():
        total_data[attribute].to_csv(attribute + f"_{league['league']}_{season}.csv", index=False)

if __name__ == '__main__':
    main(Leagues, attr)