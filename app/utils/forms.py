from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Email
from passlib.hash import bcrypt_sha256
from app.services.user_manager import find_user_by_email
from ..models.user import User


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

    def validate_email(self, email):
        user = find_user_by_email(email=email.data)
        if not user:
            raise ValidationError(message="Email veya şifrenizi kontrol ediniz.")

    def validate_password(self, password):
        user = find_user_by_email(email=self.email.data)
        if not bcrypt_sha256.verify(password.data, user.password_hash):
            raise ValidationError(message="Email veya şifrenizi kontrol ediniz.")
