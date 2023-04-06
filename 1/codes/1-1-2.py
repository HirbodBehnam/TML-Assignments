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
    return second_index - first_index <= 1

def ok(a: str) -> bool:
    if a.count("a") < 2 and a.count("c") < 2:
        return False
    if char_ok(a, "a") or char_ok(a, "c"):
        return True
    return False

alphabet = ["a","b","c"]
ok_states = []
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                if ok(a + b + c + d):
                    ok_states.append(a + b + c + d)

print(ok_states)
print(len(ok_states))