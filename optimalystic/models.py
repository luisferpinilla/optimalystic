from pydantic import BaseModel, Field
from typing import List, Literal, Union, Optional, Dict

# Tipo de variable: continua, entera, binaria
VarType = Literal["continuous", "integer", "binary"]

# Dirección de optimización
SenseType = Literal["min", "max"]

# Dirección de las restricciones
OperatorType = Literal["<=", ">=", "=="]


class Variable(BaseModel):
    name: str
    type: VarType
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None


class LinearTerm(BaseModel):
    variable: str
    coefficient: float


class Objective(BaseModel):
    sense: SenseType
    terms: List[LinearTerm]


class Constraint(BaseModel):
    name: str
    terms: List[LinearTerm]
    operator: OperatorType
    rhs: float


class Problem(BaseModel):
    name: str
    licence: Optional[str] = None
    variables: List[Variable]
    objective: Objective
    constraints: List[Constraint]
