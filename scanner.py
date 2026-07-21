from sofascore import get_team_last_matches, get_match_statistics
from stats import parse_statistics
from team_stats import calculate_average


def get_team_statistics(team_id):

    matches = get_team_last_matches(team_id)

    stats_list = []

    for match in matches:

        data = get_match_statistics(match["id"])

        if data:
            stats = parse_statistics(data)
            stats_list.append(stats)

    return calculate_average(stats_list)


def check_match(match):

    home_team = match["homeTeam"]
    away_team = match["awayTeam"]

    home_id = home_team["id"]
    away_id = away_team["id"]

    home_stats = get_team_statistics(home_id)
    away_stats = get_team_statistics(away_id)

    return {
        "home": home_team["name"],
        "away": away_team["name"],
        "home_stats": home_stats,
        "away_stats": away_stats
    }
