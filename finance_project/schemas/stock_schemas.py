"""Schemas for Stock API."""

from pydantic import BaseModel, Field

class StockShema(BaseModel):
    name: str = Field(max_length=20)
    price: int = Field(gt=0)
    code: str = Field(max_length=7)