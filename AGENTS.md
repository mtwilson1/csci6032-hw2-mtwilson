# Agent Directives & Operational Boundaries

1. **Isolation Boundary:**
   - Operate exclusively within `/Users/[REDACTED]/Desktop/csci6032-hw2-mtwilson`.
   - Never inspect, modify, or read parent directories, system configs, or user credential stores.

2. **Secrets Protection:**
   - Do not request, print, or record API keys, personal tokens, or system credentials.

3. **Change Transparency:**
   - Explain file edit intentions before executing changes.
   - Run `git status` or show `git diff` after making modifications.