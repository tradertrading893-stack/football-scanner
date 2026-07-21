from sofascore import get_team_last_matches, get_match_statistics
from stats import parse_statistics
from team_stats import calculate_average


def get_team_statistics(team_id):

    matches = get_team_last_matches(team_id)

    stats_list = []

    for match in matches:

        match_id = match["id"]

        data = get_match_statistics(match_id)

        if data:
            stats = parse_statistics(data)
            stats_list.append(stats)

    return calculate_average(stats_list)
