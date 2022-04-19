from enum import Enum

from uuid import UUID


class GameStatus(Enum):
    NOT_STARTED = 3
    RUNNING = 0
    DRAW = 1
    DONE = 2


class Game:
    def __init__(self, team1, team2, status=GameStatus.NOT_STARTED):
        self._id = UUID()  # unique
        self._team1 = team1
        self._team2 = team2
        self.status = status
        self.score = None
        # self.current_playing_team = None

    # def _current_playing_team(self, team):
    #     self.current_playing_team = team


class Score:
    def __init__(self, game_id, team_id):
        self.game_id = game_id
        self.team_id = team_id
        self.id = UUID()
        self.current_score = 0
        self.scores = []

    def add_scores(self, score):
        self.scores.append(score)

    def update_score(self, val):
        self.current_score += val

    def get_score(self):
        return self.current_score


class Player:
    def __init__(self, name, email, phone, global_ranking, total_score):
        self.id = UUID()  # unique
        self._name = name
        self._email = email
        self._phone = phone
        self._global_ranking = global_ranking
        self._total_score = total_score

    def get_total_score(self):
        return self._total_score

    def get_global_ranking(self):
        return self._global_ranking

    def update_global_ranking(self, current_ranking):
        self._global_ranking = current_ranking

    def update_total_score(self, val):
        self._total_score += val


class Team:
    def __init__(self, name, players):
        self._id = UUID()  # unique
        self._name = name
        self._players = players

    def add_players(self, player):
        pass

    def remove_player(self, player):
        pass


class GameHistory:
    def __init__(self, game_id, start_date, end_date, winning_team):
        self.id = UUID()
        self._game_id = game_id
        self._start_date = start_date
        self._end_sate = end_date
        self._winning_team = winning_team

    def _update_winning_team(self, team_id):
        self._winning_team = team_id

    def _update_end_date(self, end_date):
        pass


class GameService:
    def __init__(self):
        self.current_game = None
        self.games = []

    def create_game(self, team1, team2):
        game = Game(team1, team2)
        self.games.append(game)
        return game

    def start_game(self, game):
        while True:
            current_playing_team = 1
            self.current_game = game
            self.current_game.score = Score(self.current_game.id, current_playing_team)

            # Update current_playing_Team and scores here and break the loop once game finishes
            # condition to end game
            self.end_game(self.current_game)

    def end_game(self, game):
        # Add entry to the game history class
        pass


