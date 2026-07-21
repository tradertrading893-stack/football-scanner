from scanner import get_today_matches, get_match_info


def run():
    matches = get_today_matches()

    print(f"ნაპოვნია მატჩები: {len(matches)}")

    for match in matches:
        info = get_match_info(match)

        print(
            info["home"],
            "-",
            info["away"]
        )


if __name__ == "__main__":
    run()
