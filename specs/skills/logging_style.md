# Skill: Logging Protocol
When implementing logs in the `app/` folder, follow these rules:
- **Format:** Use JSON-like structures for console logs: `[TIMESTAMP] [LEVEL] [FEATURE] - Message`.
- **Levels:** >   - `DEBUG`: For state transitions (e.g., Hunger 50 -> 45).
  - `INFO`: For user actions (e.g., Pet fed).
  - `ERROR`: For failed validations or state inconsistencies.
- **Privacy:** Never log sensitive metadata or entire raw objects if they are large.