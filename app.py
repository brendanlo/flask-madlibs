from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def load_silly_story_form():
    """return the madlibs homepage with the story form"""

    prompts = silly_story.prompts

    return render_template("questions.html", prompts=prompts)


@app.get('/results')
def load_story_results():
    """returns the completed story with prompts filled into template"""

    completed_story = silly_story.generate(request.args)
   
    return render_template("story.html", completed_story=completed_story)

   