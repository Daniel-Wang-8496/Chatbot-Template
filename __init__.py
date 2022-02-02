# -*- coding: utf-8 -*-
"""This module contains a template MindMeld application"""
from mindmeld import Application

app = Application(__name__)

__all__ = ['app']


@app.handle(default=True)
def default(request, responder):
    """This is a default handler."""
    responder.reply('I did not understand your request, please try again.')

@app.handle(intent="destination_information")
def information(request, responder):
    responder.reply("It's currently raining at your location")

@app.handle(intent="directions")
def directions(request, responder):
    responder.reply("There are 3 minutes left until then")

@app.handle(intent="obstacles")
def obstacles(request, responder):
    responder.reply("There are no trees in front of you")

@app.handle(intent="pathfinding")
def pathfinding(request, responder):
    responder.reply("There is a sidewalk 3 feet to your right")

@app.handle(intent="surroundings")
def surroundings(request, responder):
    responder.reply("There are 3 people in front of you")
