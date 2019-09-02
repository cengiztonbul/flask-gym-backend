from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, FileField
from wtforms.validators import DataRequired, EqualTo, Email
from passlib.hash import bcrypt_sha256
from app.services.user_manager import find_user_by_email
from ..models.user import User
from flask_login import current_user


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


class NewPasswordForm(FlaskForm):
    password = PasswordField("Eski Şifre", validators=[DataRequired()], )
    new_password = PasswordField("Yeni Şifre", validators=[DataRequired(), EqualTo("new_password_confirm",
                                                                                   message="Passwords must match")])
    new_password_confirm = PasswordField("Yeni Şifre (tekrar)", validators=[DataRequired()])

    def validate_password(self, password):
        user = find_user_by_email(current_user.email)
        if not bcrypt_sha256.verify(password.data, user.password_hash):
            raise ValidationError(message="Eski şifreniz yanlış girildi.")

            
class ExerciseForm(FlaskForm):
    name = StringField("Hareket Adı", validators=[DataRequired()])
    image = FileField("hareket fotoğrafı")
    video_url = StringField("Video Linki")
    desc = StringField("description", validators=[DataRequired()])
    steps = StringField("steps", validators=[DataRequired()])

    # parts #
    back = BooleanField("back")
    leg = BooleanField("leg")
    chest = BooleanField("chest")
    shoulder = BooleanField("shoulder")
    abs = BooleanField("abs")
    biceps = BooleanField("biceps")
    triceps = BooleanField("triceps")
    # ----- #

    @property
    def body_parts(self):
        parts = []

        if self.back.data:
            parts.append("Sırt")

        if self.leg.data:
            parts.append("Bacak")

        if self.chest.data:
            parts.append("Göğüs")

        if self.shoulder.data:
            parts.append("Omuz")

        if self.abs.data:
            parts.append("Karın")

        if self.biceps.data:
            parts.append("Ön Kol")

        if self.triceps.data:
            parts.append("Arka Kol")

        return parts
