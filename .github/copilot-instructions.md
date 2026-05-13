# Copilot Instructions for Agents Repository

## Repository Purpose

This repository contains skills, agents, and prompts for AI coding assistants. Agent Skills follow the [Agent Skills Specification](https://agentskills.io/specification). Each skill is a self-contained directory with instructions that help AI agents perform specific tasks.

## Architecture

### Skills Structure

Every skill must follow this directory structure:

```sh
skills/skill-name/
├── SKILL.md          # Required: YAML frontmatter + Markdown instructions
├── scripts/          # Optional: Executable code (Python, Bash, JavaScript)
├── references/       # Optional: Additional documentation loaded on-demand
└── assets/           # Optional: Templates, images, data files
```

### Progressive Disclosure Pattern

Skills are designed for efficient context usage:

1. **Metadata** (~100 tokens): `name` and `description` fields loaded at startup for all skills
2. **Instructions** (<5000 tokens): Full `SKILL.md` body loaded when skill is activated
3. **Resources** (as needed): Files in `scripts/`, `references/`, or `assets/` loaded only when required

Keep main `SKILL.md` under 500 lines. Move detailed reference material to separate files.

## SKILL.md Format

### Required Frontmatter

```yaml
---
name: skill-name
description: What this skill does and when to use it (max 1024 chars)
---
```

### Optional Frontmatter Fields

```yaml
license: Apache-2.0
compatibility: Environment requirements (product, packages, network access)
metadata:
  author: example-org
  version: "1.0"
allowed-tools: Bash(git:*) Read  # Experimental: space-delimited pre-approved tools
```

### Body Content

After frontmatter, write Markdown instructions. Recommended sections:
- Step-by-step instructions
- Examples of inputs and outputs
- Common edge cases

## Key Conventions

### Naming Rules (`name` field)

- 1-64 characters
- Lowercase alphanumeric and hyphens only (`a-z`, `-`)
- Must not start or end with `-`
- Must not contain consecutive hyphens (`--`)
- Must match the parent directory name

✅ Valid: `pdf-processing`, `data-analysis`, `code-review`
❌ Invalid: `PDF-Processing`, `-pdf`, `pdf--processing`

### Description Best Practices

Write descriptions that help agents identify relevant tasks:

✅ Good: "Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction."

❌ Poor: "Helps with PDFs."

### File References

Use relative paths from skill root, one level deep:

```markdown
See [the reference guide](references/REFERENCE.md) for details.

Run: scripts/extract.py
```

Avoid deeply nested reference chains.

## Template

Use `.tmpl/SKILLS.md` as the starting template for new skills.

## Validation

Validate skills using the [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) library:

```bash
skills-ref validate ./my-skill
```

This checks frontmatter validity and naming conventions.
