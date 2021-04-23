"""
Contains models for validating incoming data.
"""

from typing import List

from pydantic import BaseModel, Field, validator


class Coordinates(BaseModel):
    lat: float = Field(..., alias="latitude")
    lon: float = Field(..., alias="longitude")

    class Config:
        allow_population_by_field_name = True

    # TODO: validate coordinates in range


# TODO: These 3 are not currently being used in app
class Person(BaseModel):
    name: str


class Craft(BaseModel):
    name: str
    people: List[Person]


class InSpace(BaseModel):
    crafts: List[Craft]