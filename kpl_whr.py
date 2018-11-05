#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os
import re

import yaml
from whr import whole_history_rating
from plot import plot_all_players
from plot import plot_one_player

init_date = datetime.datetime.now().date()


def load_config(name):
    config_name = os.path.join('resources', '{}.yaml'.format(name))
    config = yaml.load(open(config_name))
    return config


def get_player(player):
    pattern = re.compile('([a-zA-Z]+)-([a-zA-Z]+)')
    match = pattern.match(player)

    black = match.group(1)
    white = match.group(2)

    return black, white


def get_result(result):
    pattern = re.compile('(\d+)-(\d+)')
    match = pattern.match(result)

    black_score = int(match.group(1))
    white_score = int(match.group(2))

    return black_score, white_score


def create_games(whr, games_config, handicap=1):
    for game_item in games_config:
        game_date = game_item['date']

        time_step = (init_date - game_date).days

        player = game_item['player']
        black, white = get_player(player)

        result = game_item['result']
        black_score, white_score = get_result(result)

        for _ in range(black_score):
            whr.create_game(black, white, winner='B', time_step=time_step, handicap=handicap)

        for _ in range(white_score):
            whr.create_game(black, white, winner='W', time_step=time_step, handicap=handicap)

    whr.auto_iterate(time_limit=50)

    return whr


def main():
    games_config = load_config(name='games')
    whr = whole_history_rating.Base()

    whr = create_games(whr, games_config)
    whr_rating = whr.get_ordered_ratings()
    plot_all_players(whr_rating)
    plot_one_player(whr_rating)
    return whr_rating


if __name__ == "__main__":
    main()
