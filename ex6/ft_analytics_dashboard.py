#!/usr/bin/env python3

def main() -> None:

    print("=== Game Analytics Dashboard ===")

    player_scores = {
        'alice': 2300,
        'bob': 1800,
        'charlie': 2150,
        'diana': 2050,
        'evan': 1600,
        'frank': 1950
    }

    player_achievements = {
        'alice': ['first_kill', 'level_10', 'boss_slayer', 'speed_demon',
                  'treasure_hunter'],
        'bob': ['first_kill', 'level_10', 'collector'],
        'charlie': ['first_kill', 'level_10', 'boss_slayer', 'speed_demon',
                    'treasure_hunter', 'perfectionist', 'master_chef'],
        'diana': ['level_10', 'boss_slayer', 'collector', 'speed_demon'],
        'evan': ['first_kill', 'level_10']
    }

    player_status = {
        'alice': 'active',
        'bob': 'inactive',
        'charlie': 'active',
        'diana': 'active',
        'evan': 'inactive',
        'frank': 'active'
    }

    print()
    print("=== List Comprehension Examples ===")

    high_scorers = [player for player, score in
                    player_scores.items() if score > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [score * 2 for score in player_scores.values()]
    print(f"Scores doubled: {doubled_scores}")

    active_players = [player for player in player_status.keys()
                      if player_status[player] == 'active']
    print(f"Active players: {active_players}")

    elite_players_upper = [player.upper() for player, score in
                           player_scores.items() if score > 2000]
    print(f"Elite players (uppercase): {elite_players_upper}")

    print()
    print("=== Dict Comprehension Examples ===")

    high_score_dict = {player: score for player, score in player_scores.items()
                       if score > 1800}
    print(f"Player scores (>1800): {high_score_dict}")

    score_categories = {
        'high': sum(1 for score in player_scores.values() if score >= 2000),
        'medium': sum(1 for score in
                      player_scores.values() if 1800 <= score < 2000),
        'low': sum(1 for score in player_scores.values() if score < 1800)
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {player: len(achievements)
                          for player, achievements
                          in player_achievements.items()}
    print(f"Achievement counts: {achievement_counts}")

    print()
    print("=== Set Comprehension Examples ===")

    all_players = {player for player in list(player_scores.keys()) +
                   list(player_achievements.keys())}
    print(f"Unique players: {all_players}")

    all_achievements = {achievement
                        for achievements in player_achievements.values()
                        for achievement in achievements}
    print(f"Unique achievements: {all_achievements}")

    score_ranges = {score // 100 * 100 for score in player_scores.values()}
    print(f"Score ranges (100s): {score_ranges}")

    active_player_set = {player for player, status in player_status.items()
                         if status == 'active'}
    print(f"Active players (set): {active_player_set}")

    print()
    print("=== Combined Analysis ===")

    all_unique_players = (
        {player for player in player_scores.keys()} |
        {player for player in player_achievements.keys()} |
        {player for player in player_status.keys()}
    )
    print(f"Total players: {len(all_unique_players)}")

    print(f"Total unique achievements: {len(all_achievements)}")

    avg_score = sum(player_scores.values()) / len(player_scores)
    print(f"Average score: {avg_score:.1f}")

    def get_score(item):
        return item[1]

    top_scorer = max(player_scores.items(), key=get_score)

    print(f"Top performer: {top_scorer[0]} ({top_scorer[1]} points, "
          f"{len(player_achievements.get(top_scorer[0], []))} achievements)")

    print()
    print("=== Nested Comprehensions (Advanced) ===")

    player_achievement_pairs = [
        (player, achievement)
        for player, achievements in player_achievements.items()
        for achievement in achievements
    ]
    print(f"Total (player, achievement)"
          f"pairs: {len(player_achievement_pairs)}")

    players_by_category = {
        'high': [p for p, s in player_scores.items() if s >= 2000],
        'medium': [p for p, s in player_scores.items() if 1800 <= s < 2000],
        'low': [p for p, s in player_scores.items() if s < 1800]
    }
    print(f"Players by category: {players_by_category}")


if __name__ == "__main__":
    main()
