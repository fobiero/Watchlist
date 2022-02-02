from flask_wtf import FlaskForm
# from setuptools import Require
from wtforms import StringField,TextAreaField,SubmitField
# from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title')
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')