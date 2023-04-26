from typing import Union

START = "start"
END = "end"
Q = ["b1", "a1", "a2", "b2", "t", "0"]
DELTA = {
    (START, "0"): "e",
    ("0", "a1"): "a",
    ("a1", "0"): "b",
    ("0", "b1"): "b",
    ("b1", "0"): "a",
    ("a1", "a2"): "a",
    ("a2", "a1"): "b",
    ("b1", "b2"): "b",
    ("b2", "b1"): "a",
    ("b2", "t"): "b",
    ("a2", "t"): "a",
    ("a1", END): "e",
    ("a2", END): "e",
    ("b1", END): "e",
    ("b2", END): "e",
    ("t", END): "e",
    ("t", "t"): "(a \\cup b)"
}
print(len(DELTA))

def rip_transitions(r1: Union[str, None], r2: Union[str, None], r3: Union[str, None]) -> Union[str, None]:
    if r1 == None or r3 == None:
        return None
    if r2 == None or r2 == "e":
        if r1 == "e" and r3 == "e":
            return "e"
        if r1 == "e":
            return r3
        if r3 == "e":
            return r1
        return r1 + r3
    result = ""
    if r1 != "e":
        result += r1
    result += f"({r2})^*"
    if r3 != "e":
        result += r3
    return result

def union_transitions(a: Union[str, None], b: Union[str, None]) -> Union[str, None]:
    if a == None and b == None:
        return None
    if a == None:
        return b
    if b == None:
        return a
    return f"({a} \\cup {b})"

while len(Q) != 0:
    rip = Q.pop(0)
    delta: dict[tuple[str,str], str] = dict()
    for i in (Q + [START]):
        for j in (Q + [END]):
            r1 = DELTA.get((i, rip), None)
            r2 = DELTA.get((rip, rip), None)
            r3 = DELTA.get((rip, j), None)
            r4 = DELTA.get((i, j), None)
            delta[(i, j)] = union_transitions(rip_transitions(r1, r2, r3), r4)
    DELTA = delta
    print(DELTA)
print(DELTA[(START, END)])
