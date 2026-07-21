from sofascore import get_match_statistics
from stats import parse_statistics
from filters import match_passes_filter


def analyze_match(match_id, team_a, team_b):

    data = get_match_statistics(match_id)

    if not data:
        return False

    team_a_stats = parse_statistics(data)
    team_b_stats = parse_statistics(data)

    return match_passes_filter(
        team_a_stats,
        team_b_stats
    )
