# Planning ahead
Before you write a single line of code or ask AI, first figure out…

- What you are going to build
- What it (kind of) looks like
-> sketch a system diagram for backend or wireframe for frontend
- Don’t assume LLM knows best … it is the copilot and YOU are the boss
1. **Know what packages you are going to use ahead of time**
* Project Overview: High-level overview of the project including req. packages
* Core Functionalities: List of Functionalities the application should include, as well as modules/components for each
* Doc: Document which packages you are going to use with specific code examples from actual documentation that are relevant
* Current File Structure:
  - Use a template as the base of the project
  - Grab top level file structure
    (e.g. `tree L -2 -I ‘node_modules|.git’`)
    - FastAPI for backend
    - Nodejs for frontend

### Draft a PRD (Product Requirement Document) outline 
*instructions.md*
```
# Project Overview
...
# Core Functionalities
...
# Doc
...
# Current File Structure
...
```

2. **Research for package: Grab code examples from package docs to add into Doc section of PRD and/or add to Docs using “@”**

3. **Design Project Structure: Ask AI to create a file structure based on the PRD, example template structure and with as few files as possible.**

4. **Write Final PRD with draft PRD, ask it add detailed implementation requirements and new suggested file structure into markdown file.**

Use this PRD to align the AI outputs to your project needs by adding it to Docs and referencing whenever you need to or by adding it to .cursorrules file.