# First-Order Logic Rules (Horn Clauses)
RULES = [
    {
        "name": "Transitive_Prerequisite",
        "premises": [("Prerequisite", "?c1", "?c2"), ("Prerequisite", "?c2", "?c3")],
        "conclusion": ("IndirectPrerequisite", "?c1", "?c3")
    },
    {
        "name": "Single_Prereq_Eligibility",
        "premises": [
            ("CourseRequiresOnePrereq", "?c"),
            ("Prerequisite", "?p", "?c"),
            ("Completed", "?s", "?p"),
            ("Standing", "?s", "?st"),
            ("MinStanding", "?c", "?st"),
            ("NotCompleted", "?s", "?c")
        ],
        "conclusion": ("Eligible", "?s", "?c")
    },
    {
        "name": "No_Prereq_Eligibility",
        "premises": [
            ("NoPrerequisite", "?c"),
            ("NotCompleted", "?s", "?c")
        ],
        "conclusion": ("Eligible", "?s", "?c")
    }
]

def get_dataset(size="small"):
    """Generates Small, Medium, or Large datasets for experimental comparison."""
    facts = [
        ("Completed", "Alice", "CS101"),
        ("NotCompleted", "Alice", "CS102"),
        ("NotCompleted", "Alice", "CS201"),
        ("Prerequisite", "CS101", "CS102"),
        ("Prerequisite", "CS102", "CS201"),
        ("CourseRequiresOnePrereq", "CS102"),
        ("CourseRequiresOnePrereq", "CS201"),
        ("Standing", "Alice", "Sophomore"),
        ("MinStanding", "CS102", "Sophomore"),
        ("MinStanding", "CS201", "Sophomore"),
        ("NoPrerequisite", "MATH101"),
        ("NotCompleted", "Alice", "MATH101")
    ]

    if size in ["medium", "large"]:
        for i in range(1, 21):
            facts.append(("Completed", f"Student_{i}", "MATH101"))
            facts.append(("NotCompleted", f"Student_{i}", "MATH102"))
            facts.append(("Standing", f"Student_{i}", "Freshman"))
            facts.append(("NoPrerequisite", "MATH102"))
        for c in range(1, 16):
            facts.append(("Prerequisite", f"DEPT{c}01", f"DEPT{c}02"))
            facts.append(("MinStanding", f"DEPT{c}02", "Freshman"))

    if size == "large":
        for i in range(21, 101):
            facts.append(("Completed", f"Student_{i}", "CS101"))
            facts.append(("NotCompleted", f"Student_{i}", "CS102"))
            facts.append(("Standing", f"Student_{i}", "Junior"))
        for c in range(16, 41):
            facts.append(("Prerequisite", f"ADV{c}01", f"ADV{c}02"))

    return facts, RULES