from ortools.linear_solver import pywraplp
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
swordsmen = solver.IntVar(0, solver.infinity(), 'swordsmen')
bowmen = solver.IntVar(0, solver.infinity(), 'bowmen')
horsemen = solver.IntVar(0, solver.infinity(), 'horsemen')
solver.Add(swordsmen*60 + bowmen*80 + horsemen*140 <= 1200)
solver.Add(swordsmen*20 + bowmen*10 <= 800)                 
solver.Add(bowmen*40 + horsemen*100 <= 600)
solver.Maximize(swordsmen*70 + bowmen*95 + horsemen*230)
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
  print('================= Solution =================')
  print(f'Solved in {solver.wall_time():.2f} milliseconds in {solver.iterations()} iterations')
  print()
  print(f'Optimal power = {solver.Objective().Value()} 💪power')
  print('Army:')
  print(f' - 🗡️Swordsmen = {swordsmen.solution_value()}')
  print(f' - 🏹Bowmen = {bowmen.solution_value()}')
  print(f' - 🐎Horsemen = {horsemen.solution_value()}')
else:
  print('The solver could not find an optimal solution.')