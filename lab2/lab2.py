import itertools
import re

# Парсит формулу, введенную пользователем
def parse_formula(formula_str):
    formula_str = formula_str.replace(" ", "")

    clauses = re.findall(r'\(([^()]*)\)', formula_str)
    
    if not clauses:
        raise ValueError("Некорректный формат формулы: скобки отсутствуют")

    dnf = []
    for clause in clauses:
        literals = clause.split('V')
        dnf.append([literal for literal in literals if literal])

    return dnf

# Извлекает переменные из списка дизъюнктов
def get_variables(dnf):
    variables = set()
    for clause in dnf:
        for literal in clause:
            if literal.startswith('!'):
                variables.add(literal[1:])
            else:
                variables.add(literal)
    return sorted(list(variables))

# Создает таблицу истинности
def create_truth_table(dnf, variables):
    num_vars = len(variables)
    rows = 2**num_vars
    truth_table = []
    for i in range(rows):
        assignment = {}
        for j in range(num_vars):
            assignment[variables[j]] = (i >> j) & 1
        row = list(assignment.values()) + [evaluate(dnf, assignment)]
        truth_table.append(row)
    return truth_table

# Вычисляет значение ДНФ
def evaluate(dnf, assignment):
    result = 1
    for clause in dnf:
        clause_result = 0
        for literal in clause:
            value = assignment.get(literal[1:], 0) if literal.startswith("!") else assignment.get(literal, 0)
            if (literal.startswith("!") and not value) or (not literal.startswith("!") and value):
                clause_result = 1
                break
        result = result and clause_result
    return result

# Форматирует дизъюнкт
def format_disjunct(disjunct):
    return " V ".join(disjunct)

# Извлекает дизъюнкты из таблицы истинности
def extract_disjuncts(truth_table, variables):
    disjuncts = []
    for i, row in enumerate(truth_table):
        if row[-1]:
            disjunct = []
            for j, val in enumerate(row[:-1]):
                if val:
                    disjunct.append(variables[j])
                else:
                    disjunct.append(f"!{variables[j]}")
            disjuncts.append(disjunct)
    return disjuncts

# Генерирует все уникальные комбинации дизъюнктов
def generate_and_format_consequences(formatted_disjuncts):
    consequences = set()
    num_disjuncts = len(formatted_disjuncts)

    consequences.update(formatted_disjuncts)

    for r in range(2, num_disjuncts + 1):
        for combination in itertools.combinations(formatted_disjuncts, r):
            combined = " & ".join(f"({d})" for d in combination)
            consequences.add(combined)

    return sorted(list(consequences))


def main():
    formula_str = input("Введите формулу в формате (A V B V C) & (!A V C) & (A V B): ")
    try:
        dnf = parse_formula(formula_str)
        variables = get_variables(dnf)
        print("\nПосылки:")
        for clause in dnf:
            print( " V ".join(clause)) 
    except ValueError as e:
        print(f"Ошибка: {e}")

    truth_table = create_truth_table(dnf, variables) 

    print("\nТаблица истинности:")
    header = variables + ["f"]
    print(" ".join(header))
    for row in truth_table:
        print(" ".join(map(str, row)))

    disjuncts = extract_disjuncts(truth_table, variables)
    formatted_disjuncts = [format_disjunct(d) for d in disjuncts]
    print("\nИзвлеченные дизъюнкты:", ", ".join(formatted_disjuncts))

    consequences = generate_and_format_consequences(formatted_disjuncts)
    print("\nСледствия:\n", ",\n".join(consequences))


if __name__ == "__main__":
    main()