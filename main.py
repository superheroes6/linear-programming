from pulp import LpMaximize, LpProblem, LpVariable, value
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de SQLAlchemy
Base = declarative_base()
engine = create_engine('sqlite:///army_resources.db')
Session = sessionmaker(bind=engine)
session = Session()

# Modelo de base de datos
class ArmyResources(Base):
    __tablename__ = 'army_resources'
    id = Column(Integer, primary_key=True)
    swordsmen = Column(Integer)
    bowmen = Column(Integer)
    horsemen = Column(Integer)
    total_power = Column(Float)

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Crear el problema de maximización
model = LpProblem(name="maximize-army-power", sense=LpMaximize)

# Declarar variables
swordsmen = LpVariable(name="swordsmen", lowBound=0, cat="Integer")
bowmen = LpVariable(name="bowmen", lowBound=0, cat="Integer")
horsemen = LpVariable(name="horsemen", lowBound=0, cat="Integer")

# Agregar restricciones
model += (60 * swordsmen + 80 * bowmen + 140 * horsemen <= 1200, "Resource constraint 1")
model += (20 * swordsmen + 10 * bowmen <= 800, "Resource constraint 2")
model += (40 * bowmen + 100 * horsemen <= 600, "Resource constraint 3")

# Definir la función objetivo
model += (70 * swordsmen + 95 * bowmen + 230 * horsemen, "Total power")

# Resolver el problema
status = model.solve()

# Mostrar resultados y guardar en la base de datos
if model.status == 1:  # 1 significa que se encontró una solución óptima
    total_power = value(model.objective)
    swordsmen_value = swordsmen.varValue
    bowmen_value = bowmen.varValue
    horsemen_value = horsemen.varValue

    print('================= Solution =================')
    print(f'Optimal power = {total_power} 💪power')
    print('Army:')
    print(f' - 🗡️Swordsmen = {swordsmen_value}')
    print(f' - 🏹Bowmen = {bowmen_value}')
    print(f' - 🐎Horsemen = {horsemen_value}')

    # Guardar en la base de datos
    resources = ArmyResources(
        swordsmen=swordsmen_value,
        bowmen=bowmen_value,
        horsemen=horsemen_value,
        total_power=total_power
    )
    session.add(resources)
    session.commit()
else:
    print('The solver could not find an optimal solution.')