# Linear Programming

Este proyecto resuelve un problema de programación lineal para maximizar el poder de un ejército sujeto a restricciones de recursos. Utiliza `pulp` para resolver el problema y `SQLAlchemy` para guardar los resultados en una base de datos SQLite.

## Descripción del problema

Queremos reclutar un ejército con el mayor poder posible. Cada tipo de unidad tiene un poder asociado:

- 🗡️ **Swordsman**: 💪70
- 🏹 **Bowman**: 💪95
- 🐎 **Horseman**: 💪230

La función objetivo es maximizar el poder total del ejército:

```
max 70 × swordsmen + 95 × bowmen + 230 × horsemen
```

### Restricciones

1. **Recursos disponibles**:
   - Cada swordsman consume 60 recursos.
   - Cada bowman consume 80 recursos.
   - Cada horseman consume 140 recursos.
   - Total disponible: 1200 recursos.

   ```
   60 × swordsmen + 80 × bowmen + 140 × horsemen ≤ 1200
   ```

2. **Entrenamiento**:
   - Cada swordsman requiere 20 horas de entrenamiento.
   - Cada bowman requiere 10 horas de entrenamiento.
   - Total disponible: 800 horas.

   ```
   20 × swordsmen + 10 × bowmen ≤ 800
   ```

3. **Establos**:
   - Cada bowman requiere 40 unidades de espacio en establos.
   - Cada horseman requiere 100 unidades de espacio en establos.
   - Total disponible: 600 unidades.

   ```
   40 × bowmen + 100 × horsemen ≤ 600
   ```

## Cómo usar el programa

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecuta el programa:
   ```bash
   python main.py
   ```

3. Los resultados se guardarán en una base de datos SQLite llamada `army_resources.db`. Puedes inspeccionar los datos usando cualquier herramienta compatible con SQLite.

## Repositorio

[GitHub Repository](https://github.com/superheroes6/linear-programming.git)
