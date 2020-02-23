from flask import Flask
import numpy

oldorph = Flask(__name__)
from oldorph import script

text_in = '''
[Сегодня:14:26] Марригорн: Ненавижу окуней
[Сегодня:14:26] Марригорн: Нет, спасибо
[Сегодня:14:26] Марригорн: К тому моменту как она до меня дойдет - она станет вяленой рыбой
[Сегодня:14:26] Марригорн: …
[Сегодня:14:26] Артеус: Марри, хочешь тебе подарю?
[Сегодня:14:25] Сандер: Я люблю только копченую рыбу
[Сегодня:14:25] Марригорн: Очень даже
[Сегодня:14:25] Марригорн: Зря, я вот недавно делал треску в кляре
[Сегодня:14:25] Марригорн: Если окунь недостаточно большой, все ухищрения все равно не окупятся
[Сегодня:14:24] Сандер: Но все равно я не люблю рыбу
[Сегодня:14:24] Артеус: И где-то через пол года - совсем
[Сегодня:14:24] Сандер: Не, там как то делают насечки на ребрах и запекают в духовке
[Сегодня:14:24] Артеус: Поэтому я выкину ее в морозилку
[Сегодня:14:24] Марригорн: Поэтому лучше кому-то впарить
[Сегодня:14:24] Марригорн: Но так делать зашквар
[Сегодня:14:24] Марригорн: Это та рыба, которую проще выкинуть обратно в реку, чем самому жрать
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
