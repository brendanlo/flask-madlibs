from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def load_silly_story_form():
    """return the madlibs homepage with the story form"""
    breakpoint()
    prompts = silly_story.prompts
# define prompts here, pass in render_template
    return render_template("questions.html", prompts=silly_story.prompts)
