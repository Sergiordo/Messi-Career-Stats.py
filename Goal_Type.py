# Initialize counters for different types of shots
Left_Foot = 0
Right_foot = 0
Header = 0
Penalty = 0
Chest = 0
Direct_Free_kick = 0
Tap_in = 0


# Iterate over the 'Type' column and count occurrences of each type of shot
for shot_type in ds['Type']:
    if shot_type == 'Left-footed shot':
        Left_Foot += 1
    elif shot_type == 'Right-footed shot':
        Right_foot += 1
    elif shot_type == 'Header':
        Header += 1
    elif shot_type == 'Penalty':
        Penalty += 1
    elif shot_type == 'Chest':
        Chest += 1
    elif shot_type == 'Direct free kick':
        Direct_Free_kick += 1
    elif shot_type == 'Tap-in':
        Tap_in += 1

# Print the counts of different types of shots
print('Left Footed Shots:', Left_Foot)
print('Right Footed Shots:', Right_foot)
print('Header Shots:', Header)
print('Penalty Shots:', Penalty)
print('Chest Shots:', Chest)
print('Direct free Kick Shots:', Direct_Free_kick)
print('Tap in:', Tap_in)
