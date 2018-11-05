#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns


def plot_all_players(whr_rating):
    player_name_list = list()
    player_rating_list = list()

    for player_item in whr_rating:
        player_name = player_item[0]
        player_last_rating = player_item[1][-1]

        player_name_list.append(player_name)
        player_rating_list.append(player_last_rating)

    ax = sns.barplot(player_name_list, player_rating_list)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")

    plt.title('all players rating at 2018-11-05')
    plt.tight_layout()
    plt.savefig('pics/all_players.jpg')


def plot_one_player(whr_rating):
    for player_item in whr_rating:
        player_name = player_item[0]
        player_rating = player_item[1]

        length = len(player_rating)
        plt.figure()
        sns.barplot(x=list(range(length)), y=player_rating)
        plt.title('{} rating'.format(player_name))
        plt.savefig('pics/{}_rating.jpg'.format(player_name))
