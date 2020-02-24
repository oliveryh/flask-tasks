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

