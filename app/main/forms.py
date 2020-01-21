from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField)
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField("Blog title:", validators=[Required()])
    post = TextAreaField("Type Away:", validators=[Required()])
    submit = SubmitField("Post")
    
class UpdateProfile(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")