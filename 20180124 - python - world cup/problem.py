
def world_cup_draws_calc(matches, teams):
    return (matches * 3) - sum(teams.values())
