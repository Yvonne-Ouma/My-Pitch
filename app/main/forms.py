from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('pitch review', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please, tell us something about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    title = StringField('Comment title',validators=[Required()])
    review = TextAreaField('comment review', validators=[Required()])
    submit = SubmitField('Submit')
