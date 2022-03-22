from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import  StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PropertyForm(FlaskForm):
    choices = [("Apartment", "Apartment"), ("House","House")]
    proptitle = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    beds = StringField('No. of Rooms', validators=[DataRequired()])
    baths = StringField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    proptype = SelectField('Property Type', choices=choices)
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])