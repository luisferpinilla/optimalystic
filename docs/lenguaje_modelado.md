# 🧮 Documentación del Lenguaje de Modelado MIP

Este archivo describe cómo utilizar el lenguaje JSON para modelar problemas de programación lineal entera mixta (MIP), incluyendo ejemplos y su formulación matemática correspondiente.

---

## ✅ Ejemplo 1: Modelo con todos los tipos de variables y restricciones

### 📊 Variables
- $x \in \mathbb{R}^+ $: variable continua
- $y \in \mathbb{Z}^+ $: variable entera
- $z \in \{0, 1\} $: variable binaria

### 🎯 Función objetivo

$$
\text{Maximizar:} \quad 2.5x + 4y + 7z
$$

### 📏 Restricciones

$$
x + 2y \leq 10
$$

$$
3y + 5z \geq 8
$$

$$
x + z = 4
$$

### 🔣 JSON

```json
{
  "name": "Ejemplo_todos_tipos",
  "variables": [
    { "name": "x", "type": "continuous", "lower_bound": 0 },
    { "name": "y", "type": "integer", "lower_bound": 0 },
    { "name": "z", "type": "binary" }
  ],
  "objective": {
    "sense": "max",
    "terms": [
      { "variable": "x", "coefficient": 2.5 },
      { "variable": "y", "coefficient": 4 },
      { "variable": "z", "coefficient": 7 }
    ]
  },
  "constraints": [
    {
      "name": "restriccion_leq",
      "terms": [
        { "variable": "x", "coefficient": 1 },
        { "variable": "y", "coefficient": 2 }
      ],
      "operator": "<=",
      "rhs": 10
    },
    {
      "name": "restriccion_geq",
      "terms": [
        { "variable": "y", "coefficient": 3 },
        { "variable": "z", "coefficient": 5 }
      ],
      "operator": ">=",
      "rhs": 8
    },
    {
      "name": "restriccion_eq",
      "terms": [
        { "variable": "x", "coefficient": 1 },
        { "variable": "z", "coefficient": 1 }
      ],
      "operator": "==",
      "rhs": 4
    }
  ]
}
```

---

## ✅ Ejemplo 2: Minimización con múltiples tipos de variables

### 📊 Variables
- $ a \in \mathbb{R}^+ $: variable continua
- $ b \in \mathbb{Z},\ b \geq 1 $: variable entera
- $ c \in \{0, 1\} $: variable binaria

### 🎯 Función objetivo

$$
\text{Minimizar:} \quad a + 2b + 3c
$$

### 📏 Restricciones

$$
a + b \geq 5
$$

$$
c = 1
$$

### 🔣 JSON

```json
{
  "name": "Ejemplo_minimizacion",
  "variables": [
    { "name": "a", "type": "continuous", "lower_bound": 0 },
    { "name": "b", "type": "integer", "lower_bound": 1 },
    { "name": "c", "type": "binary" }
  ],
  "objective": {
    "sense": "min",
    "terms": [
      { "variable": "a", "coefficient": 1 },
      { "variable": "b", "coefficient": 2 },
      { "variable": "c", "coefficient": 3 }
    ]
  },
  "constraints": [
    {
      "name": "demanda",
      "terms": [
        { "variable": "a", "coefficient": 1 },
        { "variable": "b", "coefficient": 1 }
      ],
      "operator": ">=",
      "rhs": 5
    },
    {
      "name": "activacion",
      "terms": [
        { "variable": "c", "coefficient": 1 }
      ],
      "operator": "==",
      "rhs": 1
    }
  ]
}
```
