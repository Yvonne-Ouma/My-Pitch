from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class MinutePitchForm(FlaskForm):

    title = StringField('MinutePitch title',validators=[Required()])
    review = TextAreaField('pitch review', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please, tell us something about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    title = StringField('Comment title',validators=[Required()])
    review = TextAreaField('comment review', validators=[Required()])
    submit = SubmitField('Submit')
