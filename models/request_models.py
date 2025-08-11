from pydantic import BaseModel, Field


class PowRequest(BaseModel):
    base: float
    exponent: float


class FibonacciRequest(BaseModel):
    n: int = Field(..., gt=0, description="n trebuie să fie > 0")


class FactorialRequest(BaseModel):
    n: int = Field(..., ge=0, description="n trebuie să fie >= 0")
