def empty_stats():
    return {
        "shots": 0,
        "shots_on_target": 0,
        "corners": 0
    }


def parse_statistics(data):
    stats = empty_stats()

    try:
        groups = data["statistics"][0]["groups"]

        for group in groups:
            for item in group.get("statisticsItems", []):

                name = item.get("name")
                home = item.get("home")
                
                if name == "Total shots":
                    stats["shots"] = int(home)

                elif name == "Shots on target":
                    stats["shots_on_target"] = int(home)

                elif name == "Corner kicks":
                    stats["corners"] = int(home)

    except Exception:
        pass

    return stats
