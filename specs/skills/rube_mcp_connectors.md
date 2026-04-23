---
skill_id: rube-automation-bridge
name: "Rube Multi-App Connector"
description: "Unified interface to interact with external services (Slack, GitHub, Notion) via Rube MCP."
mcp_servers: ["rube-mcp"]
---
# Rube Integration Skill
- **Purpose**: Automate project notifications and external data syncing.
- **Workflow**: 
    1. Identify the target service (e.g., GitHub Issues).
    2. Use the Rube bridge to authenticate and execute the request.
- **Standard**: Always log the status of external automation in `ROADMAP.md`.