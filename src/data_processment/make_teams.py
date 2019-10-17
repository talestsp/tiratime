from src.entity.team import Team

TEAM_NAMES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "H", "I"]


def traditional(players, n_teams, n_player_team):
    players.sort(key=lambda player : player.mean(), reverse=False)

    teams = []

    for i in range(n_teams):
        teams.append(Team(name=TEAM_NAMES[i]))

    while not all_teams_complete(teams, n_player_team) and len(players) > 0:
        teams.sort(key=lambda team : team.rating()["total"], reverse=False) #priority for the lower rating team

        player = players.pop()
        teams[0].add_player(player) #priority team applied here

    return teams


def all_teams_complete(teams, n_player_team):
    for team in teams:
        if team.size() < n_player_team:
            return False
    return True






