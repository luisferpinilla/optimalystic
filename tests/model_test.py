import json
import pytest
from optimalystic.models import *


def test_json_model_valido():
    raw_json = """
    {
      "name": "Ejemplo_basico_MIP",
      "variables": [
        { "name": "x", "type": "integer", "lower_bound": 0 },
        { "name": "y", "type": "integer", "lower_bound": 0 },
        { "name": "z", "type": "binary" }
      ],
      "objective": {
        "sense": "max",
        "terms": [
          { "variable": "x", "coefficient": 5 },
          { "variable": "y", "coefficient": 3 },
          { "variable": "z", "coefficient": 8 }
        ]
      },
      "constraints": [
        {
          "name": "restriccion_1",
          "terms": [
            { "variable": "x", "coefficient": 2 },
            { "variable": "y", "coefficient": 1 }
          ],
          "operator": "<=",
          "rhs": 10
        },
        {
          "name": "restriccion_2",
          "terms": [
            { "variable": "x", "coefficient": 1 },
            { "variable": "z", "coefficient": 4 }
          ],
          "operator": ">=",
          "rhs": 3
        }
      ]
    }
    """
    problem_data = json.loads(raw_json)
    problem = Problem(**problem_data)
    assert problem.name == "Ejemplo_basico_MIP"
    assert len(problem.variables) == 3
    assert problem.objective.sense == "max"
    assert len(problem.constraints) == 2


def test_model_valido_simple():
    data = {
        "name": "modelo_simple",
        "variables": [
            {"name": "x", "type": "integer", "lower_bound": 0, "upper_bound": 10},
            {"name": "y", "type": "binary"},
            {"name": "z", "type": "continuous", "lower_bound": 1.5},
        ],
        "objective": {
            "sense": "max",
            "terms": [
                {"variable": "x", "coefficient": 5},
                {"variable": "y", "coefficient": 2},
            ],
        },
        "constraints": [
            {
                "name": "restriccion_1",
                "terms": [
                    {"variable": "x", "coefficient": 3},
                    {"variable": "y", "coefficient": 4},
                ],
                "operator": "<=",
                "rhs": 10,
            },
            {
                "name": "restriccion_2",
                "terms": [{"variable": "z", "coefficient": 1}],
                "operator": ">=",
                "rhs": 2,
            },
        ],
    }
    problem = Problem(**data)
    assert problem.name == "modelo_simple"
    assert len(problem.variables) == 3
    assert problem.objective.sense == "max"
    assert problem.constraints[1].rhs == 2


def test_model_invalido_tipo_variable():
    data = {
        "name": "modelo_tipo_invalido",
        "variables": [{"name": "x", "type": "entero"}],  # valor inválido
        "objective": {"sense": "max", "terms": [{"variable": "x", "coefficient": 5}]},
        "constraints": [],
    }
    with pytest.raises(Exception):
        Problem(**data)
