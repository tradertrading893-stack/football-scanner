def calculate_average(matches_stats):
    if not matches_stats:
        return {
            "shots": 0,
            "shots_on_target": 0,
            "corners": 0
        }

    total = {
        "shots": 0,
        "shots_on_target": 0,
        "corners": 0
    }

    for match in matches_stats:
        for key in total:
            total[key] += match.get(key, 0)

    count = len(matches_stats)

    return {
        "shots": total["shots"] / count,
        "shots_on_target": total["shots_on_target"] / count,
        "corners": total["corners"] / count
    }
