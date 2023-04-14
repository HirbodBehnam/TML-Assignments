def nth_index(a: str, char: str, b: int):
    indexes = [i for i, n in enumerate(a) if n == char]
    if len(indexes) <= b:
        return None
    return indexes[b]

def char_ok(a: str, char: str) -> bool:
    first_index = nth_index(a, char, 0)
    second_index = nth_index(a, char, 1)
    if first_index == None or second_index == None:
        return False
    return second_index - first_index <= 2

def ok(a: str) -> bool:
    if a.count("a") < 2 and a.count("c") < 2:
        return False
    if char_ok(a, "a") or char_ok(a, "c"):
        return True
    return False

print(ok("caca"))

alphabet = ["a","b","c"]
ok_states = []
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                if ok(a + b + c + d):
                    ok_states.append(a + b + c + d)

def state_name(state: str) -> str:
    return "$q_{" + state + "}$"

print(ok_states)
print(len(ok_states))
for state in ok_states:
    next_a = state[1:] + "a"
    next_b = state[1:] + "b"
    next_c = state[1:] + "c"
    next_a = state_name(next_a) if next_a in ok_states else ""
    next_b = state_name(next_b) if next_b in ok_states else ""
    next_c = state_name(next_c) if next_c in ok_states else ""
    print(f"{state_name(state)} & {next_a} & {next_b} & {next_c} \\\\")
