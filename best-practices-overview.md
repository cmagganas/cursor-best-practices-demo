# Best Practices — Overview

- [x] Use templates as a foundation to build on
- [x] Planning ahead — Measure twice cut once
- [ ] Context is King — No uneducated guesses
- [ ] Prompt Engineering — Clear, Simple, Well Defined
- [ ] Structure Outputs — Use Pydantic Validation to maximize determinism

- Break down project into small tasks
- Use cursor for functions & v0 for UI
- git commit every task

Workflow:
- Describe task.
- Ask model how it’d solve it.
- Tell model to write instruction prompt to reproduce.
- Have model explain its solution with reasoning for assurance.
- Use cursor to ‘apply’ solution directly into your script (if applicable).