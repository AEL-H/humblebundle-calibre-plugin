#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import httpretty
from humble_api.humble_api import HumbleApi
from actions import Action


@httpretty.activate
def test_httpbin():
    hapi = HumbleApi("AAAAAAA")
    httpretty.register_uri(
        httpretty.GET,
        hapi.ORDER_LIST_URL,
        body=(
                '[\n{\n"gamekey":"HHHHHHHHHHHHHHH"\n},'
                '\n{\n"gamekey":"KKKKKKKKKKKKKK"\n}\n]'
                )
    )
    game_keys = hapi.get_gamekeys()
    assert game_keys == ['HHHHHHHHHHHHHHH', 'KKKKKKKKKKKKKK'], (
            "Game keys incorrectly retrieved")
    prepare_fake_answers(hapi, game_keys)
    Action.list_downloads(hapi, game_keys)  # TODO: capture and check STDOUT
    # TODO: also check Action.batch_download(hapi, game_keys)


def prepare_fake_answers(hapi, game_keys):
    for key in game_keys:
        httpretty.register_uri(
            httpretty.GET,
            hapi.ORDER_URL.format(order_id=key),
            body=get_fake_answer(key)
            )


def get_fake_answer(key):
    path = "test/fake_library/" + key
    file = open(path, "r")
    response = file.read()
    file.close()
    return response
