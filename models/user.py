#!/usr/bin/python3
"""Creating User Class"""
from .base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
