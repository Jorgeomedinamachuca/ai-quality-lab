# AI Testing Notes

Testing AI is not only about checking whether an application works. It is also about evaluating whether the system behaves reliably, safely and usefully under different user inputs.

## Key QA Questions

- Does the AI answer the actual question?
- Does it invent unsupported facts?
- Does it handle ambiguity appropriately?
- Does it refuse unsafe requests correctly?
- Does it expose sensitive or confidential data?
- Does it remain consistent across repeated prompts?
- Does it provide a good user experience?
- Does it explain limitations transparently?

## Important Difference from Traditional Testing

Traditional automation often checks deterministic outcomes: given input A, expect output B.

AI systems often require behavioural evaluation: given input A, the output may vary, but it must remain accurate, safe, useful and aligned with the intended product behaviour.

This means AI Quality Engineering needs:

- acceptance criteria for response behaviour;
- evaluation rubrics;
- prompt datasets;
- repeat execution;
- risk classification;
- human review for high-impact outputs;
- automated checks where behaviour can be reliably measured.
