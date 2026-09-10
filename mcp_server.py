import sys
import json
from client import RobinsonUnifier

unifier = RobinsonUnifier()

def handle_call(name, arguments):
    if name == "unify":
        t1 = tuple(arguments["t1"])
        t2 = tuple(arguments["t2"])
        subst = unifier.unify(t1, t2)
        return {"substitution": subst if subst is not False else None, "success": subst is not False}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
