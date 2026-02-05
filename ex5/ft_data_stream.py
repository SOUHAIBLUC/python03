#!/usr/bin/env python3

import time


def game_event_stream(count: int):

    import random
    

    players = ['alice', 'bob', 'charlie', 'diana', 'evan']
    actions = ['killed monster', 'found treasure', 'leveled up', 'completed quest']
    

    for i in range(1, count + 1):

        event = {
            'id': i,
            'player': random.choice(players),
            'level': random.randint(1, 20),
            'action': random.choice(actions)
        }
        yield event


def analyze_event_stream(event_generator) -> dict:

    total_events = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    for event in event_generator:

        total_events += 1
        

        if event['level'] >= 10:
            high_level_count += 1
        
        if event['action'] == 'found treasure':
            treasure_count += 1
        
        if event['action'] == 'leveled up':
            levelup_count += 1
        
        if total_events <= 3:
            print(f"Event {event['id']}: Player {event['player']} (level {event['level']}) {event['action']}")
    
    if total_events > 3:
        print("...")
    
    return {
        'total': total_events,
        'high_level': high_level_count,
        'treasure': treasure_count,
        'levelup': levelup_count
    }


def fibonacci_generator(limit: int):

    a, b = 0, 1
    
    for _ in range(limit):

        yield a
        

        a, b = b, a + b


def prime_generator(limit: int):

    def is_prime(n: int) -> bool:
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    count = 0
    num = 2 
    
    while count < limit:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def main() -> None:
    """
    Main function demonstrating generator usage.
    """
    print("=== Game Data Stream Processor ===")
    

    event_count = 1000
    print(f"Processing {event_count} game events...")
    

    events = game_event_stream(event_count)
    

    start_time = time.time()
    

    stats = analyze_event_stream(events)
    

    end_time = time.time()
    
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {stats['total']}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['levelup']}")
    print(f"Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")
    
    print()
    print("=== Generator Demonstration ===")
    

    print("Fibonacci sequence (first 10): ", end="")
    fib_gen = fibonacci_generator(10)

    print(", ".join(str(num) for num in fib_gen))
    

    print("Prime numbers (first 5): ", end="")
    prime_gen = prime_generator(5)
    print(", ".join(str(num) for num in prime_gen))



if __name__ == "__main__":
    main()