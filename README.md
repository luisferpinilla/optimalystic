# 📦 Optimalystic Modeling Language

[![Tests](https://github.com/luisferpinilla/optimalystic/actions/workflows/test.yml/badge.svg)](https://github.com/luisferpinilla/optimalystic/actions)
[![Coverage](https://img.shields.io/badge/coverage-auto-lightgrey)](https://github.com/luisferpinilla/optimalystic)


**Lenguaje de modelado matemático basado en JSON para describir problemas de Programación Lineal Entera Mixta (MIP), validado estructuralmente con Pydantic.**

---

## 🚀 ¿Qué es este proyecto?

Este proyecto define un lenguaje declarativo en formato JSON para modelar y resolver problemas de optimización lineal y entera. Los modelos son validados estructuralmente mediante [Pydantic](https://docs.pydantic.dev/) en Python y pueden ser utilizados como base para construir soluciones de optimización personalizadas.

Si deseas utilizar este lenguaje en un proyecto o integración propia, te invitamos a contactar a Grupo Zenith para coordinar el uso apropiado y contribuir a su evolución open source.

---

## 🧠 Características principales

- ✅ Validación formal de modelos MIP con Pydantic
- 📤 Exportación e importación en formato JSON
- 🧪 Pruebas unitarias incluidas con `pytest`

---

## 📁 Estructura del proyecto

```
mip_modeling_language/
├── mip_modeling_language/
│   ├── models.py             # Definición del lenguaje MIP con Pydantic
├── tests/                    # Pruebas unitarias
├── examples/                 # Modelos de ejemplo en JSON
├── docs/                     # Documentación técnica del lenguaje
├── README.md
└── requirements.txt
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

Para obtener una documentacíón más detallada, consulte la [documentación](docs/lenguaje_modelado.md) del proyecto

---

## 🛠 Instalación

```bash
git clone https://github.com/luisferpinilla/optimalystic.git
cd optimalystic
pip install -r requirements.txt
```

---

## 🧼 Pre-commit hooks

Este proyecto utiliza [`pre-commit`](https://pre-commit.com/) para aplicar automáticamente reglas de estilo y validación antes de cada `git commit`.

### 🔧 Instalación en Windows (PowerShell, CMD o Git Bash)

1. Instala `pre-commit`:
   ```bash
   pip install pre-commit
   ```

2. Instala los hooks definidos:
   ```bash
   pre-commit install
   ```

3. Ejecuta los hooks manualmente en todos los archivos:
   ```bash
   pre-commit run --all-files
   ```

### ✅ Hooks incluidos (ejemplo)

- `black`: formateador de código Python
- `flake8`: detección de errores de estilo
- `isort`: ordenamiento automático de imports
- `end-of-file-fixer`: asegura saltos de línea al final de archivos
- `check-yaml`, `check-json`: validación de sintaxis

> Asegúrate de tener el archivo `.pre-commit-config.yaml` en la raíz del repositorio.

---


---

## 🙌 Contribuciones

Este proyecto es open source y está en constante evolución. Si deseas contribuir, por favor:

1. Abre un issue para proponer una mejora o reportar un bug.
2. Crea un fork del repositorio y realiza los cambios en una rama nueva.
3. Ejecuta los tests con `pytest` y asegúrate de que el código pase los hooks de `pre-commit`.
4. Envía un Pull Request explicando claramente qué cambios realizaste.

Si planeas integrar este lenguaje en una solución comercial o académica, por favor abre un [issue](https://github.com/tu_usuario/tu_repositorio/issues) para compartir tu caso de uso.

¡Gracias por hacer parte del ecosistema de modelado con propósito!


## 📜 Licencia

Este proyecto está en desarrollo. Su distribución como herramienta open-source esta sujeto a [licenciamiento](LICENSE).

---

## 🤝 Contacto

Proyecto desarrollado por **Grupo Zenith**.

Para sugerencias, consultas o propuestas de colaboración, por favor abre un [issue](https://github.com/luisferpinilla/optimalystic/issues) en este repositorio.
