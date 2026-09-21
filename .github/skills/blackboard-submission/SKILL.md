---
name: blackboard-submission
description: A workflow skill to preflight, package, and safely submit CSCI 6032 Homework 2 to Blackboard.
---

# Blackboard Submission Protocol

Follow this workflow strictly. Do NOT auto-approve terminal commands or browser actions.

## 1. Preflight and Validation
- Confirm you are operating in the expected homework repository (`csci6032-hw2-mtwilson`).
- Run a preflight check: check the current branch, run `git status`, check recent commits, and verify the expected remote URL using `git remote -v`.
- Stop immediately if the tree is not clean, required artifacts are missing, or unresolved secrets/private data are apparent.
- Confirm that the current reviewed branch has been pushed.

## 2. Packaging
- Prepare `csci6032-hw2-mtwilson.tar.gz` from the committed `HEAD`. 
- EXCLUDE `.git`, credentials, caches, or unrelated files.
- List the archive contents and show the exact notebook, archive, repository URL, and submission text you propose to use.

## 3. Dry Run Support
- Support a "dry run" mode. If the user requests a dry run, perform every possible check but STOP before opening Blackboard or submitting.

## 4. Browser Navigation and Authentication
- Ask the user before opening or controlling the Blackboard tab.
- Require the user to authenticate personally. NEVER request, read, store, type, or expose credentials.
- Navigate only to this homework's submission page and stage the required files and repository URL.

## 5. Final Irreversible Submission
- STOP IMMEDIATELY before the final, irreversible submission action (clicking submit).
- Show the user exactly what will be submitted.
- Require explicit confirmation at that point. A prior general approval is not sufficient.
- After confirmation, complete the submission, verify the confirmation page or receipt, and report the result.
- Do not commit Blackboard screenshots, receipts, browser data, or personal information to the public repository.