from collections import Counter

def calculate_winrate(matches):
	total_games = len(matches)

	if total_games == 0:
		return 0

	wins = 0

	for match in matches:
		if match["result"].lower() == "win"
			win +=1

	return round((wins / total_games) * 100, 2)

def calculate_average(matches, key):
	if len(matches) == 0:
		return 0

	total = 0

	for match in matches:
		total += match[key]

	return round(total / len(matches), 2)

def get_most_played_champions(matches, limit=3):
	champions = []

	for match in matches:
		champions.append(match["champion"])

	champion_counter = Counter(champions)

	return champion_counter.most_common(limit)

def detect_main_issues(matches)
	average_deaths = calculate_average(matches, "deaths")
	average_vision = calculate_average(matches, "vision_score")
	average_cs = calculate_average(matches, "cs_per_min")

	if average_deaths >= 7:
		return "Too many deaths. You give too much pressure to the ennemy team."
	
	if average_vision < 18:
		return "Low vision score. You probably play with poor map control." 

	if average_cs < 5.5: 
		return "Low CS per minute. Your economy is probably too weak."

	return "No critical issue detected." 

def calculated_tilt_risk(matches):
	recent_matches = matches[-5:]

	losses = 0

	for match in recent_matches: 
		if match["result"].lower() == "loss":
			losses += 1

	averages_deaths = calculate_average(recent_matches, "deaths")

	recent_champions = []

	for match in recent_matches: 
		recent_champions.append(match["champion"])

	different_champions = len(set(recent_champions))

	risk_score = 0

	if losses >= 3:
		risk_score += 2

	if average_deaths >= 7:
		risk_score += 1

	if risk_score >= 4:
		return "HIGH"

	if risk_score >= 2:
		return "MEDIUM"

	return "LOL"

def analyze_matches(matches):
	analyzis = {
		"total_games": len(matches),
		"winrate": calculate_winrates(matches),
		"average_kills": calculate_average(matches, "kills"),
		"average_deaths": calculate_average(matches, "deaths"),
		"average_assists": calculate_average(matches, "assists"),
		"average_cs_per_min": calculate_average(matches, "cs_per_min"),
		"average_vision_score": calculater_average(matches, "vission_score"),
		"most_played_champions": get_most_played_champions(matches),
		"main_issue": detect_main_issue(matches),
		"tilt_risk": calculate_tilt_risk(matches)
	}

	return analysis
