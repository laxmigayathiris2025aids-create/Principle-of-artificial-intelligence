
def unify(pred1, pred2):

    # Remove spaces
    pred1 = pred1.replace(" ", "")
    pred2 = pred2.replace(" ", "")

    # Extract predicate names
    name1 = pred1[:pred1.index("(")]
    name2 = pred2[:pred2.index("(")]

    if name1 != name2:
        return "Unification Failed"

    # Extract arguments
    args1 = pred1[pred1.index("(") + 1:pred1.rindex(")")].split(",")
    args2 = pred2[pred2.index("(") + 1:pred2.rindex(")")].split(",")

    if len(args1) != len(args2):
        return "Unification Failed"

    substitution = {}

    def is_variable(term):
        return len(term) == 1 and term.isupper()

    def resolve(term):
        while term in substitution:
            term = substitution[term]
        return term

    # Unify arguments
    for a, b in zip(args1, args2):

        a = resolve(a)
        b = resolve(b)

        if a == b:
            continue

        if is_variable(a):
            substitution[a] = b

        elif is_variable(b):
            substitution[b] = a

        else:
            return "Unification Failed"

    if not substitution:
        return "Predicates are already unified"

    # Resolve final substitutions
    result = {}

    for variable in substitution:
        result[variable] = resolve(substitution[variable])

    return result


# Main program
pred1 = input("Enter Predicate 1: ")
pred2 = input("Enter Predicate 2: ")

result = unify(pred1, pred2)

print("\nResult:")

if isinstance(result, dict):
    for variable, value in result.items():
        print(variable, "=", value)
else:
    print(result)
