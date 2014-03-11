from random import choice

from flask import Flask, render_template
from werkzeug.datastructures import ImmutableDict


class FlaskWithHamlish(Flask):
    jinja_options = ImmutableDict(
        extensions=['jinja2.ext.autoescape', 'jinja2.ext.with_', 'hamlish_jinja.HamlishExtension'])


app = FlaskWithHamlish(__name__)
app.jinja_env.hamlish_enable_div_shortcut = True
app.jinja_env.hamlish_mode = 'indented'

prefix = ['beautiful', 'cute', 'brave', 'fascinating', 'radical', 'cheerful', 'thankful', 'fabulous', 'grateful',
          'joyful', 'caring', 'funny', 'generous', 'thrilling', 'giving', 'suave', 'creative', 'witty', 'confident',
          'amazing', 'wonderful', 'amusing', 'gorgeous', 'cool', 'intelligent', 'friendly', 'smart', 'nice', 'outgoing',
          'clever', 'intriguing', 'sweet', 'smart', 'inspiring', 'debonair', 'charming', 'pleasant', 'compassionate',
          'high-strung', 'exciting', 'gracious', 'kind', 'lovely', 'helpful', 'awesome', 'honest', 'trustworthy',
          'stunning', 'stylish', 'entertaining', 'loving', 'musical', "lovely", "sweet", "cute", "perfect", "baby"]

suffix = ['love', 'cutie-pie', 'compatriot', 'sugar', 'honey', 'baby', 'thinker', 'wifey', 'girl', 'eyes', 'sweetie',
          'sir', 'sweety', 'buddy', 'getleman', 'stud', 'darling', 'cutie', 'pal', 'friend', 'boo', 'sweetheart',
          'woman', 'babe', 'babes', 'hun', 'sunshine', 'kisser', 'gal', 'cuteness', 'cupcake', 'lady', 'princess',
          'kid', 'boy', 'cowboy', 'lips', 'madame', 'pudding', 'man', 'lover', 'yours']


def random_compliment(prefix, suffix):
    return choice(prefix).capitalize() + " " + choice(suffix).capitalize()

@app.route('/')
def hello_world():
    compliment = random_compliment(prefix, suffix)
    return render_template("index.haml", **locals())


if __name__ == '__main__':
    app.run()
