import json

def load_workouts():
    with open('workouts-all.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_sport(sport: str):
    if sport == 0:
        return "running"
    if sport == 21:
        return "indoor cycling"
    if sport == 2:
        return "cycling"
    if sport == 18:
        return "walking"
    if sport == 14:
        return "fitness walking"
    return sport

workouts = load_workouts()
with open('workouts-converted.txt', 'w') as f:
    for workout in workouts:
        if workout["readable_type"] == "WORKOUT" and workout["author"]["last_name"] == "Yanzin":
            w = workout["workout"]
            sport = get_sport(w["sport"])
            start_time = w["start_time"]
            start_time = "{} {}".format(start_time[:10], start_time[11:19]).replace('-', '.')
            distance = str(w["distance"]).replace('.', ',')
            duration = str(w["duration"]).replace('.', ',')
            calories = str(w["calories"]).replace('.', ',')
            f.write("{};{};{};{};{}\n".format(sport, start_time, distance, duration, calories))