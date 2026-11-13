import copy

def is_variable(term):
    """Variables start with '?' (e.g., '?s', '?c1')."""
    return isinstance(term, str) and term.startswith("?")

def unify(x, y, theta=None):
    """Standard First-Order Logic Unification Algorithm."""
    if theta is None:
        theta = {}
    if theta is False:
        return False
    if x == y:
        return theta
    if is_variable(x):
        return unify_var(x, y, theta)
    if is_variable(y):
        return unify_var(y, x, theta)
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    return False

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    if x in theta:
        return unify(var, theta[x], theta)
    new_theta = copy.deepcopy(theta)
    new_theta[var] = x
    return new_theta

def substitute(atom, theta):
    """Replaces variables in a predicate using substitution theta."""
    return tuple(theta.get(term, term) for term in atom)

class FOLReasoner:
    def __init__(self, facts, rules):
        self.facts = set(facts)
        self.rules = rules

    def forward_chain(self, target_query=None):
        """Data-driven forward chaining inference with tracing."""
        inferred = set(self.facts)
        trace = []
        inferences_count = 0

        while True:
            new_facts_added = False
            for rule in self.rules:
                substitutions = self._match_premises(rule["premises"], inferred, {})
                for theta in substitutions:
                    inferences_count += 1
                    new_fact = substitute(rule["conclusion"], theta)
                    if new_fact not in inferred:
                        inferred.add(new_fact)
                        new_facts_added = True
                        trace.append({
                            "rule": rule["name"],
                            "substitutions": theta,
                            "inferred_fact": new_fact
                        })
                        if target_query and new_fact == target_query:
                            return True, trace, inferences_count
            if not new_facts_added:
                break

        found = (target_query in inferred) if target_query else True
        return found, trace, inferences_count

    def _match_premises(self, premises, facts_set, theta):
        if not premises:
            return [theta]
        first, rest = premises[0], premises[1:]
        results = []
        for fact in facts_set:
            new_theta = unify(first, fact, theta)
            if new_theta is not False:
                results.extend(self._match_premises(rest, facts_set, new_theta))
        return results

    def backward_chain(self, goal, visited=None):
        """Goal-driven backward chaining inference with proof tracing."""
        if visited is None:
            visited = set()
        if goal in visited:
            return False, [], 1
        visited.add(goal)

        steps = 1
        if goal in self.facts:
            return True, [{"step": "Fact Match", "goal": goal, "substitutions": {}}], steps

        for rule in self.rules:
            theta = unify(rule["conclusion"], goal, {})
            if theta is not False:
                subgoals = [substitute(p, theta) for p in rule["premises"]]
                all_subgoals_proven = True
                combined_trace = []

                for sg in subgoals:
                    proven, sub_trace, sub_steps = self.backward_chain(sg, visited.copy())
                    steps += sub_steps
                    if not proven:
                        all_subgoals_proven = False
                        break
                    combined_trace.extend(sub_trace)

                if all_subgoals_proven:
                    combined_trace.append({
                        "step": f"Rule Applied: {rule['name']}",
                        "goal": goal,
                        "substitutions": theta
                    })
                    return True, combined_trace, steps

        return False, [], steps