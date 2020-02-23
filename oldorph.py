from flask import Flask
import numpy

oldorph = Flask(__name__)
from oldorph import script

text_in = '''
Вудуист подмигнул деду, махнул рукой и , пропустив вперед ученицу рявкнул.

- Ну, что встали? БЕГОМ! - и шагнул в портал следом.

Легко заходить в него первым, если ты правильно и заранее выбрал позицию. Впрочем, пяти минут должно было более чем хватить, ибо о сроках в итоге все заинтересованные оказались предупреждены.
'''
try:
    replace_rules = numpy.array(script.read_text('oldorph/replace_rules.txt'))
except OSError:
    replace_rules = []


@oldorph.route('/')
@oldorph.route('/index')
def index():
    text = script.replace_text(text_in, replace_rules)

    return text

if __name__ == "__main__":
    oldorph.run()
