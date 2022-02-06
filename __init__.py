# -*- coding: utf-8 -*-

from mindmeld import Application
from .text_preparation_pipeline import get_text_preparation_pipeline
app = Application(__name__, text_preparation_pipeline=get_text_preparation_pipeline())


@app.handle(default=True)
def default(request, responder):
    """This is a default handler."""
    responder.reply('I did not understand your request, please try again.')

@app.handle(intent="destination_information")
def information(request, responder):
    responder.reply("Look up info")

@app.handle(intent="directions")
def directions(request, responder):
    responder.reply("Use google maps for directions")

@app.handle(intent="obstacles")
def obstacles(request, responder):
    responder.reply("Don't worry about it. There are no obstacles near you")

@app.handle(intent="pathfinding")
def pathfinding(request, responder):
    responder.reply("You are on the right path")

@app.handle(intent="surroundings")
def surroundings(request, responder):
    responder.reply("There are 3 people in front of you")
