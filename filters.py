def match_passes_filter(team_a, team_b):

    team_a_ok = (
        team_a["shots"] >= 34 and
        team_a["shots_on_target"] >= 15 and
        team_a["corners"] >= 10
    )

    team_b_ok = (
        team_b["shots"] >= 31 and
        team_b["shots_on_target"] >= 14 and
        team_b["corners"] >= 10
    )

    return team_a_ok and team_b_ok
