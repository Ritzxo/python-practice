# Read input for the three matches
match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

# 1. Find players who participated in all three matches
find_players = match1.intersection(match2, match3)

# 2. Find players who participated in exactly two matches
two_matches1 = match1.intersection(match2) - match3
two_matches2 = match1.intersection(match3) - match2
two_matches3 = match2.intersection(match3) - match1
exactly_two = two_matches1.union(two_matches2, two_matches3)
# 3. Find players who participated in only one match
one_player = match1.difference(match2, match3)
one_player2 = match2.difference(match1, match3)
one_player3 = match3.difference(match1, match2)

exactly_one = one_player.union(one_player2, one_player3)
# 4. Count total unique players
all_players = match1.union(match2, match3)

total_players = len(all_players)


# 5. Find players in Match 1 only
one_match = match1.difference(match2, match3)

# Print results in the specified format
print(f"Players in all matches: {sorted(list(find_players))}")
print(f"Players in exactly two matches: {sorted(list(exactly_two))}")
print(f"Players in only one match: {sorted(list(exactly_one))}")
print(f"Total unique players: {total_players}")
print(f"Players in Match 1 only: {sorted(list(one_match))}")