import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("nba_elo_latest.csv")


def create_total_ratings_bar_plot(data):
    """
    Create a bar plot to compare the total ratings of different teams or games.

    Args:
        data (DataFrame): Pandas DataFrame containing the dataset.

    Returns:
        None
    """
    # Group the data by team1 and calculate the mean total_rating for each team
    team_ratings = data.groupby('team1')['total_rating'].mean()

    # Sort the teams by their mean total_rating
    team_ratings = team_ratings.sort_values(ascending=False)

    plt.figure(figsize=(15, 10))
    team_ratings.plot(kind='bar', color='skyblue')
    plt.xlabel('Teams')
    plt.ylabel('Mean Total Rating')
    plt.title('Mean Total Ratings for Different Teams')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


create_total_ratings_bar_plot(df)


def create_game_quality_histogram(data):
    """
    Create a histogram to visualize the distribution of games based on quality.

    Args:
        data (DataFrame): Pandas DataFrame containing the dataset.

    Returns:
        None
    """
    # Count the number of games in each quality category
    quality_counts = data['quality'].value_counts()

    plt.figure(figsize=(10, 6))
    plt.hist(data['quality'], bins=len(quality_counts),
             rwidth=0.9, color='lightblue', edgecolor='black')
    plt.xlabel('Game Quality')
    plt.ylabel('Number of Games')
    plt.title('Distribution of Games by Quality (Histogram)')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


create_game_quality_histogram(df)


def create_team_elo_ratings_line_plot(data, team_name):
    """
    Create a line plot to visualize the Elo ratings of a specific team over time.

    Args:
        data (DataFrame): Pandas DataFrame containing the dataset.
        team_name (str): Name of the team to plot Elo ratings for.

    Returns:
        None
    """
    # Filter the data for the specified team
    team_data = data[(data['team1'] == team_name) |
                     (data['team2'] == team_name)]

    # Combine Elo ratings for both home and away matches
    team_data['elo_rating'] = team_data.apply(
        lambda row: row['elo1_pre'] if row['team1'] == team_name else row['elo2_pre'], axis=1
    )

    # Sort the data by date
    team_data = team_data.sort_values(by='date')

    plt.figure(figsize=(15, 8))
    plt.plot(team_data['date'], team_data['elo_rating'],
             label=f'{team_name} Elo Rating', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Elo Rating')
    plt.title(f'{team_name} Elo Ratings Over Time')
    plt.xticks(rotation=90)
    plt.legend()
    plt.grid(True)
    plt.show()


# Replace 'BOS' with the team abbreviation you want to visualize.
create_team_elo_ratings_line_plot(df, 'BOS')
