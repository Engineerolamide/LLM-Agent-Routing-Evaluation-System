# LLM Agent Routing & Evaluation System

## Overview
This project explores how to design, route, and evaluate Large Language Model (LLM) responses in a multi-agent system.

The goal is to move beyond simple prompt usage and instead treat LLMs as systems that require structure, testing, and iteration to behave reliably.

---

## Problem

When using LLMs in real-world workflows, several issues arise:
- Inconsistent tone across responses
- Hallucinated or fabricated information
- Poor handling of ambiguous inputs
- Lack of control over output structure

This project investigates how to design systems that improve reliability and consistency.

---

## Approach

### 1. Multi-Agent Routing
User inputs are classified and routed to specialized "agents" implemented through structured prompts.

Example agents:
- Motivational Agent
- Advisory Agent
- Informational Agent

Each agent has:
- Defined tone and role
- Output constraints
- Structured response expectations

---

### 2. Prompt Architecture
Prompts were designed to:
- Enforce consistent tone and identity
- Control response length and format
- Reduce ambiguity in outputs

Example:
"You are a motivational coach. Respond in 2-3 sentences. Be direct, encouraging, and avoid generic advice."

---

### 3. System Design

Tools used:
- OpenAI API (LLM responses)
- Make (Integromat) for orchestration
- Google Sheets for logging inputs/outputs

Workflow:
1. User submits input
2. Input is classified
3. Routed to appropriate agent prompt
4. Response generated
5. Logged for evaluation

---

## Evaluation Method

To understand model behavior, outputs were evaluated across several dimensions:

### Consistency
- Does the same input produce similar responses?
- Is agent tone preserved?

### Instruction Adherence
- Does the model follow constraints (length, format, tone)?

### Failure Modes
Tracked common issues:
- Hallucination
- Ambiguity
- Tone drift
- Ignoring instructions

---

## Experiments

### Experiment 1: Prompt Tightening
- Compared loose vs structured prompts
- Result: Structured prompts improved consistency and reduced variation

### Experiment 2: Edge Case Testing
Tested inputs like:
- Contradictory instructions
- Ambiguous phrasing
- Emotionally complex requests

Result:
- Model struggled with ambiguity without clear constraints
- Improved with better prompt framing

---

## Key Findings

- Small prompt changes significantly impact output behavior
- LLMs require structured constraints for reliability
- Multi-agent routing improves contextual relevance
- Evaluation is critical for improving system performance

---

## Future Improvements

- Automated evaluation scoring (ranking outputs)
- Adding feedback loops for continuous improvement
- Expanding agent roles and specialization
- Integrating lightweight UI for user interaction

---

## Why This Matters

LLMs are powerful but unpredictable. Treating them as systems that require design, evaluation, and iteration is key to building reliable AI applications.

This project reflects a shift from "using AI" to understanding and improving how AI behaves in real-world scenarios.
