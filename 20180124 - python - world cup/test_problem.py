import unittest
from problem import world_cup_draws_calc

class TestWorldCup(unittest.TestCase):

    def test_has_no_draws_when_no_game_was_played(self):
        matches = 0
        teams = {
            'Brasil': 0,
            'Australia': 0
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 0, 'has no draws when no game was played')

    def test_has_one_draws_when_everebody_has_one_point_and_one_game_was_played(self):
        matches = 1
        teams = {
            'Brasil': 1,
            'Australia': 1
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 1, 'has one draws when everebody has one point and one game was played')

    def test_has_0_draws_when_1_matches_was_played_and_1_team_has_3_points(self):
        matches = 1
        teams = {
            'Brasil': 3,
            'Australia': 0
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 0, 'has 0 draws when 1 matches was played and 1 team has 3 points')

    def test_has_0_draws_when_1_matches_was_played_and_1_team_has_3_points_inverted(self):
        matches = 1
        teams = {
            'Brasil': 0,
            'Australia': 3
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 0, 'has 0 draws when 1 matches was played and 1 team has 3 points inverted')

    def test_has_0_draws_when_2_matches_was_played_and_2_teams_has_3_points(self):
        matches = 2
        teams = {
            'Brasil': 3,
            'Australia': 3
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 0, 'has 0 draws when 2 matches was played and 2 teams has 3 points')

    def test_has_1_draws_when_2_matches_was_played_and_one_team_has_4_points(self):
        matches = 2
        teams = {
            'Brasil': 4,
            'Australia': 1
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 1, 'has 1 draws when 2 matches was played and one team has 4 points')

    def test_has_2_draws_when_2_matches_was_played_and_both_teams_has_2_points(self):
        matches = 2
        teams = {
            'Brasil': 2,
            'Australia': 2
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 2, 'has 2 draws when 2 matches was played and both teams has 2 points')

    def test_has_0_draws_when_2_matches_was_played_and_one_team_has_6_points(self):
        matches = 2
        teams = {
            'Brasil': 6,
            'Australia': 0
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 0, 'has 0 draws when 2 matches was played and one team has 6 points')

    def test_has_3_draws_when_3_matches_was_played_and_both_teams_have_3_points(self):
        matches = 3
        teams = {
            'Brasil': 3,
            'Australia': 3
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 3, 'has 3 draws when 3 matches was played and both teams have 3 points')

    def test_has_0_draws_when_3_matches_was_played_and_one_team_has_9_points(self):
        matches = 3
        teams = {
            'Brasil': 9,
            'Australia': 0
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 0, 'has 0 draws when 3 matches was played and one team has 9 points')

    def test_has_4_draws_when_4_matches_was_played_and_both_team_has_4_points(self):
        matches = 4
        teams = {
            'Brasil': 4,
            'Australia': 4
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 4, 'has 4 draws when 4 matches was played and both team has 4 points')

    def test_has_5_draws_when_5_matches_was_played_and_both_team_has_5_points(self):
        matches = 5
        teams = {
            'Brasil': 5,
            'Australia': 5
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 5, 'has 5 draws when 5 matches was played and both team has 5 points')

    def test_has_1_draws_when_2_matches_was_played_and_one_team_has_4_points_v2(self):
        matches = 2
        teams = {
            'Brasil': 4,
            'Australia': 1
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 1, 'has 1 draws when 2 matches was played and one team has 4 points v2')

    def test_has_1_draws_when_2_matches_was_played_and_3_team_has_3_points(self):
        matches = 2
        teams = {
            'Brasil': 3,
            'Croacia': 1,
            'Australia': 1
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 1, 'has 1 draws when 2 matches was played and 3 team has 3 points')

    def test_has_2_draws_when_2_matches_was_played_and_3_team_has_2_points(self):
        matches = 2
        teams = {
            'Brasil': 2,
            'Croacia': 1,
            'Australia': 1
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 2, 'has 2 draws when 2 matches was played and 3 team has 2 points')

    def test_has_2_draws_when_2_matches_was_played_and_3_team_has_2_points_inverted(self):
        matches = 2
        teams = {
            'Brasil': 1,
            'Croacia': 2,
            'Australia': 1
        }
        self.assertEqual(world_cup_draws_calc(matches, teams), 2, 'has 2 draws when 2 matches was played and 3 team has 2 points inverted')



unittest.main()
