# 📦 Optimalystic Modeling Language

**Lenguaje de modelado matemático basado en JSON para problemas de Programación Lineal Entera Mixta (MIP), validado con Pydantic y compatible con solvers como PuLP, OR-Tools, GLPK y SCIP.**

---

## 🚀 ¿Qué es este proyecto?

Este proyecto define un lenguaje declarativo en formato JSON para modelar y resolver problemas de optimización lineal y entera. Los modelos son validados estructuralmente mediante [Pydantic](https://docs.pydantic.dev/) en Python, y pueden convertirse a objetos ejecutables por distintos solucionadores (solvers) como:

- [PuLP](https://coin-or.github.io/pulp/)
- [Google OR-Tools](https://developers.google.com/optimization)
- [GLPK](https://www.gnu.org/software/glpk/)
- [SCIP](https://scipopt.org/) *(en desarrollo)*

Además, este lenguaje puede integrarse en aplicaciones empresariales como capa intermedia entre lógica de negocio y soluciones de optimización, con soporte para ejecución remota vía AWS Lambda.

---

## 🧠 Características principales

- ✅ Validación formal de modelos MIP con Pydantic
- 📤 Exportación e importación en formato JSON
- 🔄 Conversión a múltiples solvers (PuLP, OR-Tools, etc.)
- 🔒 Soporte para validación de licencias
- ☁️ Preparado para despliegue en AWS (Lambda, S3)
- 🧪 Pruebas unitarias incluidas con `pytest`

---

## 📁 Estructura del proyecto

```
mip_modeling_language/
├── mip_modeling_language/
│   ├── models.py             # Definición del lenguaje MIP con Pydantic
│   ├── parser.py             # Carga y validación de JSON
│   ├── converters/           # Convertidores a distintos solvers
│   ├── solvers/              # Ejecución de modelos en cada solver
│   └── utils/                # Funciones auxiliares como control de licencias
├── tests/                    # Pruebas unitarias
├── examples/                 # Modelos de ejemplo en JSON
├── docs/                     # Documentación técnica del lenguaje
├── scripts/                  # Ejecución de modelos desde línea de comandos
├── README.md
├── requirements.txt
└── pyproject.toml
```

---

## ✅ Ejemplo mínimo

```json
{
  "name": "Ejemplo_basico",
  "variables": [
    { "name": "x", "type": "integer", "lower_bound": 0 },
    { "name": "y", "type": "binary" }
  ],
  "objective": {
    "sense": "max",
    "terms": [
      { "variable": "x", "coefficient": 10 },
      { "variable": "y", "coefficient": 6 }
    ]
  },
  "constraints": [
    {
      "name": "capacidad",
      "terms": [
        { "variable": "x", "coefficient": 2 },
        { "variable": "y", "coefficient": 4 }
      ],
      "operator": "<=",
      "rhs": 8
    }
  ]
}
```

---

## 🛠 Instalación

```bash
git clone https://github.com/tu_usuario/mip_modeling_language.git
cd mip_modeling_language
pip install -r requirements.txt
```

---

## 📦 Uso

```bash
python scripts/run_from_json.py examples/ejemplo_basico.json --solver pulp
```

---

## 📜 Licencia

Este proyecto está en desarrollo. Su distribución como herramienta open-source o privativa está sujeta a decisión futura.

---

## 🤝 Contacto

Proyecto desarrollado por **Grupo Zenith**.
Consultas: [consultor@grupozenith.com](mailto:consultor@grupozenith.com)
