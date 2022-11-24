from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField
from wtforms.validators import NumberRange, DataRequired


class Choice_of_direction(FlaskForm):
    way = SelectField("Выберете сторону света, в которую желаете отправиться!", coerce=int,
                      choices=[(0, "Север"), (1, "Восток"), (2, "Юг"), (3, "Запад")],
                      render_kw={'class': 'form-select'})


class Number_steps(FlaskForm):
    steps = IntegerField("Как далеко планируешь продвинуться?", validators=[NumberRange(min=1), DataRequired()],
                         default=1, render_kw={"class": "form-control"})
    submit = SubmitField("В путь!")
