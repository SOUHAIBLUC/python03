#!/usr/bin/env python3



def main() -> None:
    
    
    print("=== Achievement Tracker System ===")
    

    
    alice_achievements = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    }
    
    bob_achievements = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    }
    
    charlie_achievements = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }
    

    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")
    
    print()
    print("=== Achievement Analytics ===")
    

    all_unique = alice_achievements.union(bob_achievements, charlie_achievements)
    

    
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")
    

    common_to_all = alice_achievements.intersection(bob_achievements, charlie_achievements)
    

    
    print(f"Common to all players: {common_to_all}")
    
    
    rare_achievements = set()
    
    for achievement in all_unique:

        count = 0
        if achievement in alice_achievements:
            count += 1
        if achievement in bob_achievements:
            count += 1
        if achievement in charlie_achievements:
            count += 1
        

        if count == 1:
            rare_achievements.add(achievement)
    
    print(f"Rare achievements (1 player): {rare_achievements}")
    

    print()
    

    alice_bob_common = alice_achievements.intersection(bob_achievements)

    
    print(f"Alice vs Bob common: {alice_bob_common}")
    

    alice_unique = alice_achievements.difference(bob_achievements)

    
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob_achievements.difference(alice_achievements)
    
    print(f"Bob unique: {bob_unique}")



if __name__ == "__main__":
    main()