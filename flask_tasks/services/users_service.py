from typing import Optional

from passlib.handlers.sha2_crypt import sha512_crypt as crypto

from flask import jsonify

import flask_tasks.data.db_session as db_session
from flask_tasks.data.user import User

def add_user(name: str, email: str, password: str) -> Optional[User]:


    user = User()
    user.name = name
    user.email = email
    user.hashed_password = hash_text(password)

    session = db_session.create_session()
    session.add(user)
    session.commit()

    return user

def hash_text(text: str) -> str:

    hashed_text = crypto.encrypt(text, rounds=123456)
    return hashed_text

def login_user(email: str, password: str) -> Optional[User]:

    session = db_session.create_session()

    user = session.query(User).filter(User.email == email).first()

    if not user or not crypto.verify(password, user.hashed_password):
        return None

    return user

def get_user_by_id(user_id: str) -> Optional[User]:

    session = db_session.create_session()

    user = session.query(User).filter(User.id == user_id).first()

    return user

def does_email_exist(email: str) -> bool:

    session = db_session.create_session()

    user = session.query(User).filter(User.email == email).first()

    if user:
        return True
    else:
        return False
