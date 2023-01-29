import csv
import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.csrf import generate_csrf
from wtforms import StringField, URLField, TimeField, SelectField, SubmitField, \
    HiddenField
from wtforms.validators import DataRequired, URL


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
    Bootstrap(app)

    return app


app = create_app()



# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------

def get_cafe_data():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return list_of_rows

def write_to_cafe_data(data_set):
    with open('cafe-data.csv', mode='a') as csv_file:
        csv_file.write(data_set)



class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    opening_time = TimeField('Opening Time e.g 8:30am', validators=[DataRequired()])
    closing_time = TimeField('Closing Time e.g 5:30pm', validators=[DataRequired()])
    coffee_rating = SelectField(choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'], validators=[DataRequired()])
    wifi_strength_rating = SelectField(choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], validators=[DataRequired()])
    power_socket_availability = SelectField(choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')
    csrf_token = HiddenField()

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    form.csrf_token.data = generate_csrf()
    if form.validate_on_submit():
        data_set = f"\n{form.cafe_name.data},{form.cafe_location.data},{form.opening_time.data},{form.closing_time.data},\
        {form.coffee_rating.data.strip()},{form.wifi_strength_rating.data},{form.power_socket_availability.data}"
        write_to_cafe_data(data_set)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    return render_template('cafes.html', cafes=get_cafe_data())


if __name__ == '__main__':
    app.run(debug=True)
