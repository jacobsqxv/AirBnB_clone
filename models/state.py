#!/usr/bin/python3
"""holds class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """Representation of state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes of state"""
        super().__init__(*args, **kwargs)
