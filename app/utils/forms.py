from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email


class RegisterForm(FlaskForm):
    first_name = StringField("Ad", validators=[DataRequired()])
    last_name = StringField("Soyad", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Şifre",
                           validators=[DataRequired(), EqualTo("password_confirm", message="Passwords must match")])
    password_confirm = PasswordField("Şifre (tekrar)", validators=[DataRequired()])
    # submit = SubmitField("Giriş Yap")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Şifre", validators=[DataRequired()])
    remember_me = BooleanField("Beni Hatırla")
    # submit = SubmitField("Sign In")
