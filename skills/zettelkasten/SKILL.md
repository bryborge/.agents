---
name: zettelkasten
description: Create structured atomic notes, maps of content and sources for a zettelkasten-style note-taking system. Use this skill when the user wants to take or update notes.
license: apache-2.0
metadata:
  author: bryborge
  version: "1.0"
---

# Zettelkasten Skill

## Overview

Zettelkasten is a personal knowledge management and note-taking system. Zettels are "atomic" notes that represent a single, self-contained idea or concept, and are linked to one-another in an organic and ever-evolving relational way (like gardening in an ecosystem of ideas).

### Dependencies

The `pdf-processing` skill may be needed to generate a document based on the content from a PDF.

## Objectives

At a high level, your primary job is to capture concepts from source materials (lecture slides, textbooks, and assignments in pdf and potentially other text formats) as Zettels, and to relate them to each other--sometimes in unique and surprising ways.

### General Tasks

#### 1. Create "Maps of Content" (or MOC) documents.

These serve as central nodes for related Zettel AND Source documents. Follow the `moc.md` template file found in `templates/`.

#### 2. Create "Source" documents.

These represent *where* ideas came from. Follow the `source.md` template file found in `templates/`.

> [!IMPORTANT]
> Source documents should always be created from other documents that are provided by the user, such as lecture slides, digital textbooks, and scientific articles in PDF format.
> If the user does NOT provide these to you, ask the user for them.

#### 3. Create Zettel documents.

These are notes that capture a single, atomic idea or concept. Follow the `zettel.md` template file found in `templates/`.

### General Rules

> [!IMPORTANT]
> 1.  **Never invent information:** Only use the context provided from source material.
> 2.  **Maintain Atomicity:** If asked to draft a Zettel, ensure it covers only one, discrete concept.
> 3.  **Preserve formatting:** Always output notes using the exact relevant document structure.

-   The *title* of a generated document should use `Capitalization` inside the document, and `kebab-case` in the document name. For example, "Discrete Structures" is the title used inside the document, and "discrete-structures"is the title part of the file name of that document.
-   A complete file name should look like the following example: `<unique-identifier>-<title>.md` and the file should be placed in the relevant folder inside the working project (`src/<mocs|sources|zettels>`).

> [!NOTE]
> Links between documents are generated using "Wikilink" syntax.
>   -   Basic Link: [[file-name]]
>   -   Alias Link: [[file-name|Display Name]]
>   -   Header Link: [[file-name#Header]]
>
> Favor Alias Links, especially when linking in the context of a block of text so that the text reads clearly.

## Procedure

### Document Generation

#### 1.  Generate the requested document.

If the user asks something like "generate a source for 'ECE171 - Lecture 3' based on this file: ...", "capture the following concept: ...", "make a moc for 'DC Circuits'", then create the relevant document making sure to follow the correct document structure.

#### 2.  Fill out the document metadata.

-   If the user specifies a unique identifier, use it. Fall back to Unix timestamp.
-   For Sources, specify a source-type like "textbook", "literature-book", "lecture", "presentation", "website"

#### 3.  Fill out the remaining sections of the document.

As a general rule, try to keep Zettel document length to 1000 words or less.  Sources and MOCs are not word-heavy documents and do not have a length cutoff like Zettels do.

#### 4.  Ask for feedback.

Loop in the user by asking for feedback before generating the document.

#### 5.  Update and Fix backlinks.

After a new document is generated, ensure that the related MOCs, Sources, and Zettels backlinks are correct. Fix any link errors that you find.
