---
skill_id: context7-docs-fetcher
name: "Real-Time documentation (Context7)"
description: "Allows the agent to fetch the latest documentation for any library or framework to prevent hallucinations and outdated API usage."
mcp_servers: ["context7-docs"]
---

# Context7 Documentation Skill

- **Purpose**: Ensure that all code generated for the SSD-Framework uses the latest, version-specific APIs, bypassing LLM training data cut-offs.
- **Workflow**:
    1. **Identify Needed Tech**: Check `specs/techstack.md` for the current project's libraries.
    2. **Resolve Library**: Use `resolve-library-id` if the ID for a library is unknown.
    3. **Fetch Docs**: Use `query-docs` to retrieve the relevant API sections (e.g., "Next.js 15 Middleware" or "Supabase Auth Helpers").
    4. **Implementation**: Reference the fetched documentation directly while writing code to `app/`.
- **Standard**: Always invoke Context7 when:
    - Implementing a new library for the first time.
    - Upgrading a major version of a tech stack component.
    - Encountering unclear error messages from modern libraries that suggest an API change.
