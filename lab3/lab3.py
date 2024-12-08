import itertools

# Разбирает формулу в КНФ на множество дизъюнктов
def parse_formula_to_clauses(formula_str):
    formula_str = formula_str.replace(" ", "")
    clauses = formula_str.split("&")
    parsed_clauses = []
    for clause in clauses:
        literals = clause.strip("()").split("V")
        parsed_clauses.append(set(literals))
    return parsed_clauses

# Выполняет резолюцию двух дизъюнктов и упрощает
def resolve(clause1, clause2):
    for literal in clause1:
        complement = literal[1:] if literal.startswith('!') else f'!{literal}'
        if complement in clause2:
            resolvent = (clause1 | clause2) - {literal, complement}
            simplified_resolvent = set()
            for lit in resolvent:
                complement_lit = lit[1:] if lit.startswith('!') else f'!{lit}'
                if complement_lit not in resolvent:
                    simplified_resolvent.add(lit)
            return simplified_resolvent
    return None

# Проверяет, является ли дизъюнкт пустым
def is_empty_clause(clause):
    return len(clause) == 0

# Форматирует дизъюнкт в читаемый строковый вид
def format_clause(clause):
    return " V ".join(sorted(clause)) if clause else "пустая резольвента"

# Реализует метод резолюций для проверки доказуемости следствия из посылок
def resolution_method(clauses, goal):
    clauses.extend(goal)
    
    all_clauses = set(map(frozenset, clauses))
    steps = []

    print("Исходное множество дизъюнктов:")
    for clause in clauses:
        print(f"  {format_clause(clause)}")

    while True:
        new_resolvents = set()
        pairs = list(itertools.combinations(all_clauses, 2))
        for clause1, clause2 in pairs:
            resolvent = resolve(clause1, clause2)
            if resolvent is not None:
                resolvent = frozenset(resolvent)
                steps.append(f"{format_clause(clause1)} & {format_clause(clause2)} => {format_clause(resolvent)}")

                if is_empty_clause(resolvent):
                    return True, steps
                if resolvent not in all_clauses:
                    new_resolvents.add(resolvent)

        if not new_resolvents:
            return False, steps

        all_clauses.update(new_resolvents)

def main():
    premises_str = input("Введите посылки в формате (A V B V C) & (B V !C) & (!A V B) & (!B V C):\n")
    goal_str = input("Введите следствие в формате (A V B V C) & (!A V B):\n")

    try:
        clauses = parse_formula_to_clauses(premises_str)
        goal_clauses = parse_formula_to_clauses(goal_str)

        if not clauses or not goal_clauses:
            print("Ошибка: неверный формат посылок или следствия.")
            return

        is_proved, steps = resolution_method(clauses, goal_clauses)

        print("\nШаги резолюции:")
        for step in steps:
            print(step)

        if is_proved:
            print("\nТеорема доказана.")
        else:
            print("\nТеорема опровергнута.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()