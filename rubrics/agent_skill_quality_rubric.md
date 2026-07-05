# Agent Skill Quality Rubric

This rubric evaluates the quality, safety and testability of reusable AI agent skills, including Claude-style skills.

## Evaluation Criteria

| Criterion | Description | Score 1 | Score 3 | Score 5 |
|---|---|---|---|---|
| Purpose Clarity | The skill clearly explains what it is for. | Purpose is missing or vague. | Purpose is present but broad. | Purpose is specific, clear and useful. |
| Trigger Clarity | The skill explains when it should be used. | No usage context. | Some usage examples. | Clear conditions for when to use the skill. |
| Input Definition | The skill defines expected input. | Input is not defined. | Input is partially defined. | Input is clearly defined with examples. |
| Output Definition | The skill defines expected output. | Output is unclear. | Output is partially described. | Output format is clear and structured. |
| QA Value | The skill supports quality-related work. | QA value is unclear. | Some QA value is present. | Strong QA relevance and practical utility. |
| Reusability | The skill can be reused across similar tasks. | Highly task-specific. | Some reuse possible. | Clearly reusable and adaptable. |
| Safety Boundaries | The skill defines what it should not do. | No safety limits. | Some limits included. | Clear safety, privacy and reliability limits. |
| Ambiguity Handling | The skill handles incomplete or unclear inputs. | Ignores ambiguity. | Mentions ambiguity. | States assumptions and asks clarification questions. |
| Testability | The skill can be evaluated with tests or rubrics. | Not testable. | Partially testable. | Has clear structure suitable for automated checks. |
| Human Oversight | The skill recognises the role of human review. | Implies full automation. | Mentions review generally. | Clearly positions AI output as reviewable support. |

## Scoring

- 45–50: Strong skill
- 35–44: Good skill with minor improvements needed
- 25–34: Usable but requires refinement
- Below 25: Weak or unsafe skill design

## QA Interpretation

A high-quality agent skill should be clear, bounded, reusable, safe and testable.

From a Quality Engineering perspective, the skill itself is a testable artefact. Its structure, instructions, examples and safety boundaries can all be reviewed and validated before the skill is used in a real workflow.
