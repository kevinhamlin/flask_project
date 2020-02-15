import os
import secrets
from PIL import Image
from flask_mail import Message
from flask import url_for, current_app
from main import mail


def save_profile_picture(form_picture):
    random_hex_value = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    profile_picture_filename = random_hex_value + file_ext
    profile_pic_path = os.path.join(current_app.root_path, 'static/profile_pictures', profile_picture_filename)

    picture_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(picture_size)
    img.save(profile_pic_path)
    return profile_picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    message = Message('Password Reset Request', sender='kevin.hamlin@gmail.com', recipients=[user.email])
    message.body = f'''To reset your password, please click the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not request this password reset, please ignore this email.
'''
    mail.send(message)