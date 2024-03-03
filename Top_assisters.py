# Count the number of assists by each assister
assist_counts = ds['Goal_assist'].value_counts()

for assister, count in assist_counts.items():
    print(f"{assister}: {count} assists")