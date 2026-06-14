def build_report(analysis):
    lines = []

    lines.append("RIFT SENTINEL REPORT")
    lines.append("====================")
    lines.append("")
    lines.append(f"Games analyzed: {analysis['total_games']}")
    lines.append(f"Winrate: {analysis['winrate']}%")
    lines.append("")
    lines.append("Average stats")
    lines.append("-------------")
    lines.append(f"Kills: {analysis['average_kills']}")
    lines.append(f"Deaths: {analysis['average_deaths']}")
    lines.append(f"Assists: {analysis['average_assists']}")
    lines.append(f"CS/min: {analysis['average_cs_per_min']}")
    lines.append(f"Vision score: {analysis['average_vision_score']}")
    lines.append("")
    lines.append("Most played champions")
    lines.append("---------------------")

    for champion, count in analysis["most_played_champions"]:
        lines.append(f"- {champion}: {count} games")

    lines.append("")
    lines.append("Diagnosis")
    lines.append("---------")
    lines.append(f"Main issue: {analysis['main_issue']}")
    lines.append(f"Tilt risk: {analysis['tilt_risk']}")
    lines.append("")
    lines.append("Verdict")
    lines.append("-------")

    if analysis["tilt_risk"] == "HIGH":
        lines.append("Stop queueing. You are probably tilted.")
    elif analysis["tilt_risk"] == "MEDIUM":
        lines.append("Be careful. Your recent games show warning signs.")
    else:
        lines.append("Mental state looks stable enough.")

    return "\n".join(lines)
