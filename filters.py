def check_team_a(stats):
    return (
        stats["shots"] >= 34 and
        stats["shots_on_target"] >= 15 and
        stats["corners"] >= 10
    )


def check_team_b(stats):
    return (
        stats["shots"] >= 31 and
        stats["shots_on_target"] >= 14 and
        stats["corners"] >= 10
    )


def match_passes_filter(team_a, team_b):
    return check_team_a(team_a) and check_team_b(team_b)
