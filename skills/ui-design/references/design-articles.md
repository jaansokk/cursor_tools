# Design foundations and source differences

The core skill is a synthesis of these six articles and the owner's preferences. Tonal separation, explicit project choices, function-first expression, purposeful brand-true departures, the general accent-hue limit, and avoidance of decorative counters are owner guidance; they are not presented as unanimous rules from the authors.

The accent policy is explicit: prefer one hue for general interface elements, with two as the maximum, using saturation and brightness variations as needed. Separate informational roles such as utility, labels, status, and dashboard data may require additional colors. Source palette examples illustrate concepts within this policy; they do not replace it.

Read the relevant source for its explanations and visual examples. Use the principles within the approved project direction, not as a reason to import a source site's aesthetic.

## Refactoring UI: practical adjustments

[7 Practical Tips for Cheating at Design — Adam Wathan & Steve Schoger](https://medium.com/refactoring-ui/7-practical-tips-for-cheating-at-design-40c736799886)

Useful for balancing text weight and tonal emphasis, reducing unnecessary borders, and distinguishing action importance. Sections 1, 4, and 7 connect closely to the core hierarchy and separation guidance.

The title of section 1 contrasts weight/color with size; its explanation cautions against relying on size alone. Section 4 offers shadows, background differences, and spacing as alternative separators, not a required combination. Section 6 proposes colored borders for flair: use such additions only within the user's chosen role for brand expression, with a clear purpose.

## Nielsen Norman Group: perceptual grouping

[Proximity Principle in Visual Design — Aurora Harley](https://www.nngroup.com/articles/gestalt-proximity/)

Useful for making spacing communicate relationships, keeping instructions and controls near their subjects, and preserving groups across responsive changes. Proximity can be stronger than shared color or shape. Common-region and similarity cues should support the same organization rather than contradict it.

The form examples show that the structure of the gaps matters more than empty space in isolation. Excessive distance can hide relevant actions by making them appear unrelated. Gestalt grouping is part of the information structure, not a final decorative pass.

## Erik Kennedy: structure, light, and whitespace

[7 Rules for Creating Gorgeous UI, Part 1](https://www.learnui.design/blog/7-rules-for-creating-gorgeous-ui-part-1.html)

Useful for understanding simple interfaces with subtle depth cues, building layout before adding color, and spotting cramped composition. Rule 1 explains the brighter-raised-surface model; Rule 2 uses grayscale as a design constraint; Rule 3 demonstrates generous spacing.

Kennedy favors flatty styling. The skill keeps flat/flatty, gradients, and shadows as separate project choices. Apply the lighting model when the interface depicts depth. Grayscale is a diagnostic technique, with exceptions for color-dependent tasks and strongly expressive work. Generous spacing addresses cramped layouts; it does not mean doubling every gap in a comparison tool.

## Anthony Hobday: a practical visual system

[Quick Start Guide: Visual Design](https://anthonyhobday.com/sideprojects/quickstart/visualdesign)

Useful for coherent type and spacing relationships, shared alignment edges, baselines, nested groups, and selective emphasis. It explains how reducing secondary emphasis can simplify hierarchy.

Hobday explicitly frames the advice as starting guidelines. For example, three or four type sizes, a 12-column grid, a 60/30/10 palette, and body text around 16–20 pixels illustrate possible systems. They are not requirements for every product. Choose readable text and purposeful roles rather than reproducing these numbers. The advice to avoid pure black and white is a comfort-oriented preference, not a prohibition on readable endpoint colors.

## Nielsen Norman Group: decisions in finished designs

[Good Visual Design, Explained — Kelley Gordon](https://www.nngroup.com/articles/good-visual-design/)

Useful for studying real layouts with annotated grids, deliberate type hierarchy, limited palettes, and imagery that contributes information. It demonstrates that size can establish hierarchy even with little variation in text color or weight.

The three-size and two-main-color examples are illustrative starting points. They differ from Hobday's recipes without invalidating the shared principles. A grid organizes related elements; a successful example does not make its column count or density universal. Meaningful photography may deserve attention while the surrounding UI stays restrained.

## Mark Boulton: space as an active tool

[Whitespace — A List Apart](https://alistapart.com/article/whitespace/)

Useful for distinguishing small typographic spaces from larger compositional gaps and seeing how space itself can create emphasis. Its dense-content example improves readability without reducing the amount of information.

The brand-positioning examples show why spacing depends on purpose. They do not establish that every spacious interface is better or that a dense interface is cheap. Preserve grouping and comfortable reading while choosing density for the user's task.

## Reconcile recommendations by purpose

| Apparent disagreement | How to apply the sources |
| --- | --- |
| Size versus weight and tonal contrast | Judge the cues together. Size may be reduced with appropriate weight and contrast adjustments, provided the result remains comfortably readable and preserves hierarchy. |
| Generous whitespace versus compact information | Preserve legibility and relative grouping; choose density for reading, scanning, or comparison. |
| Three type sizes versus three or four; two colors versus 60/30/10 | Source numbers illustrate coherent systems rather than required counts or proportions. The owner's separate policy limits general accents to one preferred hue, two at most; informational colors have distinct roles. |
| Flatty versus flat styling | Ask for the project's surface treatment. Use simulated lighting only when it supports the approved choice. |
| Accent borders for flair versus function-first composition | Ask what role brand expression may play in this use case. Do not introduce ornament merely because an article suggests it. |
| Spacing, surface tone, borders, or shadows for separation | Start with correct relationships. Prefer tone to an extra enclosing border when a visible region helps; use a border or approved shadow when it communicates the needed boundary more clearly. This ordering is the owner's synthesis. |

If the use case and recorded choices do not resolve a material disagreement, describe the alternatives and ask. Avoid asking the user to resolve differences that are simply techniques for different contexts.

## Accessibility is a separate quality requirement

A visual example in an article is not proof of accessibility. Measure actual color pairs and inspect meaningful control cues and focus states, including over gradients or tinted surfaces. Low-contrast placeholder text is not exempt simply because it is secondary.

For projects targeting WCAG 2.2 AA, consult [text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), and the project's applicable accessibility requirements. Aesthetic numerical examples do not relax these requirements.
