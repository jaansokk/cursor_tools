---
name: ui-design
description: >
  Design, implement, or improve user interfaces using framework-independent
  principles of hierarchy, Gestalt grouping, spacing, typography, color,
  and interaction. Use for visual UI work on applications, websites, and
  components while preserving the project's implementation stack.
---

# UI Design

Make the user's task clear and comfortable to complete. Build visual character through deliberate choices that serve the use case. Avoid ornament added merely to make an interface look designed. Confidently depart from conventions when doing so serves the use case or is true to the approved brand. Make the departure intentional, subtle in execution, and easy to understand; preserve usability.

This skill describes design decisions. Use the project's existing stack, components, and tokens to implement them; do not introduce a styling framework or replace a design system just to follow this skill.

## Establish the task and visual direction

Read the relevant interface, content, and existing design guidance. Identify the person, primary task, important information, and intended order of attention. Understand whether they need to read, scan, compare, enter information, or act repeatedly.

For a new visual direction, ask about unresolved choices together and wait for the answers before applying those treatments:

- **Flat or flatty:** simple surfaces without simulated depth, or simple shapes with subtle cues of elevation?
- **Gradients:** none, subtle lighting, or expressive use; where are they appropriate?
- **Shadows:** none, restrained functional elevation, or more expressive depth; where are they appropriate?
- **Brand expression:** should visual treatments serve direct content and interaction purposes only, or may some also communicate identity? If identity is a goal, should it live within useful elements or include restrained decoration?

These are separate choices. Flatty does not automatically imply shadows or gradients, and an expressive brand does not authorize arbitrary ornament. Do not choose a default aesthetic. Reuse approved answers and established project guidance; do not restart discovery for a small edit within an approved direction. Clarify only material gaps that affect the requested work.

Continue work that does not depend on unanswered choices, such as correcting grouping or readability. Removing a redundant effect does not require choosing a replacement; ask before introducing an unresolved treatment.

## Gestalt grouping is structural

Decide what belongs together before styling individual elements. Make perceptual groups match actual relationships.

- **Proximity:** related elements belong closer together than unrelated elements. Keep a heading with its content, a label with its field, and an action with the object it affects. Preserve nested grouping relationships.
- **Similarity:** similar appearance should indicate a shared role or behavior. Do not give unrelated actions the same prominent treatment, or make equivalent items look unrelated without a reason.
- **Common region:** a shared surface or enclosure makes its contents appear related. Use this deliberately; a container can create a misleading group even when the spacing inside looks tidy.
- **Figure and ground:** the active content and relevant controls should be distinguishable from supporting structure. Let backgrounds support understanding without competing for attention.
- **Continuity:** aligned edges and repeated structure give the eye a clear path through related information.
- **Closure:** people can infer a whole from partial cues. Use that to keep groups recognizable without tracing every edge; retain any boundary essential to understanding or operation.

Check the grouping before reading the words. If the perceived structure is wrong, fix the relationships; adding color or another box will not repair the underlying organization. Recheck grouping when content wraps or moves at a different viewport size.

## Spacing and alignment express relationships

Spacing has a hierarchy of its own. Use smaller distances inside close relationships, larger gaps between groups, and stronger separation between major sections. For example, label-to-field, field-to-field, and section-to-section gaps express different levels of relatedness. Equal spacing everywhere flattens that hierarchy. Repeated relationships should have consistent spacing, with nested groups remaining visibly connected to their parent group.

Use space to communicate importance as well as grouping. Giving an important element or group more breathing room can establish emphasis without enlarging the text or adding another color. Build a coherent rhythm whose gap relationships make the content hierarchy apparent; a consistent spacing scale alone does not guarantee this.

Measure from the visible content or surface edges that people perceive. Align related text edges and adjacent text baselines; allow small optical corrections when mathematical alignment looks wrong.

Choose density for the task. Long-form reading benefits from comfortable line length and leading. Comparison tools may need compact rows with clear alignment. Increase space where it clarifies a relationship or focus; do not make every interface sparse or disconnect controls from their content.

Establish separation through proximity and alignment first. When a visible region is useful, prefer a restrained difference in surface tone over an additional enclosing border. Add borders when they clarify a necessary boundary, affordance, or compact division more effectively. Avoid redundant combinations of a border, tint, and shadow that all communicate the same separation. Differentiate functional control boundaries from decorative container edges.

## Hierarchy allocates attention

Make the visual order reflect the task's importance. Distinguish primary information, supporting content, and incidental metadata with the smallest effective set of cues: position, space, size, weight, and tonal contrast.

Quiet secondary elements before increasing every primary element. Maintain readability while reducing emphasis; supporting information still needs to be usable. A page title does not automatically deserve more attention than the information needed for the current task.

Action emphasis follows importance in the current context. Primary, secondary, and less frequent actions should be distinguishable. Destructive meaning and visual prominence are separate decisions: a deletion action can be quiet in a list and prominent in its confirmation.

Use counters only when order has meaning, such as actual steps, rank, or an explicit ordered reference. Do not prefix unordered cards, benefits, navigation items, or sections with decorative counters such as “01” and “02”.

## Typography must be comfortably readable

Choose typefaces for legibility, language coverage, task fit, and approved character. Preserve established project typography. There are no named-font bans or mandatory display/body pairings.

Start with comfortably sized text at the actual viewing distance and viewport. Text size can be reduced when it suits the task and hierarchy; adjust weight and tonal contrast accordingly to preserve readability. Judge size, weight, and contrast together rather than making smaller text automatically lighter or fainter. Increased weight or contrast cannot rescue text that remains too small to read comfortably.

For crowded layouts, consider grouping, reflow, disclosure, and content priorities alongside any size reduction. Small body text, labels, captions, and data still need enough visual presence to read comfortably; do not simply shrink everything to fit.

Use consistent typographic roles, readable line lengths, and leading suited to text size. The role distinctions matter more than a fixed number of font sizes. Use alignment and suitable numeral forms for comparison; monospace is useful for code and some identifiers, not compulsory for every number.

## Color communicates purpose

Build the organization and emphasis without depending on hue. A grayscale review can reveal weak hierarchy; inspect the full-color version as well, especially when color carries status or selection.

Use color where it communicates action, state, selection, category, or approved identity. Keep its meaning consistent. Ordinary metadata and decorative structure should not consume the same emphasis as important controls. Let meaningful imagery take attention when it is the content.

For general interface elements, prefer one accent hue and use at most two. Build variations through saturation and brightness changes within those hues, alongside neutral surfaces and text. Give each accent a consistent role instead of adding hues for variety.

This accent limit does not constrain utility colors, meaningful labels, status indicators, or dashboard and chart categories where color has a separate informational role. Define those colors by that role and use them consistently. Always reinforce meaningful color with another cue such as text, shape, position, or an icon.

Measure text contrast against the actual rendered background, including tinted surfaces and gradients. Muted labels, captions, placeholders, and chart annotations are not excuses for unreadable text. Follow the project's accessibility requirements for text, required control/state cues, and focus indicators; decorative surface edges do not all need the same contrast as controls.

## Surfaces and depth follow the chosen model

Use flat or flatty treatment according to the approved project direction. Flat interfaces can establish structure through space, alignment, and surface tone without simulated elevation.

When depicting elevation, keep the lighting and layer relationships consistent. A lighter raised surface on a darker or tinted canvas, including a white card, is a valid technique. Shadows should explain an approved depth relationship; gradients should serve an approved lighting, emphasis, or identity purpose. Avoid stacking effects to compensate for weak hierarchy.

Make purposeful, brand-true departures when they improve the result. Keep their execution controlled and subtle, with clear behavior and coherent relationships to the rest of the system. Familiar conventions are useful starting points, not reasons to suppress an intentional choice.

## Preserve usability as the interface changes

Keep controls recognizable, labels clear, focus visible, and states distinguishable. Prefer native semantics and established accessible components when they meet the interaction need. Design for relevant loading, empty, error, selected, and disabled states without inventing extra UI for states the feature does not have.

Test long labels, realistic data, and narrow layouts. Preserve relationships and readable type when space is constrained. Reflow or change presentation before shrinking everything. Use motion only when it helps explain a transition or response, and respect reduced-motion preferences.

## Review the rendered result

Inspect the actual interface when a preview is available. If visual verification is unavailable, say what was reviewed and what remains unverified.

- Does the first thing noticed match the task's priority? Does a squint or blur reveal the intended hierarchy?
- Does spacing reinforce that hierarchy, with clear differences between close relationships, groups, and major sections? Does extra breathing room emphasize the right content?
- Do groups remain clear without reading every label? Are labels, controls, and supporting actions attached to the right content?
- Is body and supporting text comfortably readable at normal size? Where size is reduced, do weight and contrast compensate appropriately without flattening the hierarchy? Verify contrast separately; a screenshot or squint test cannot establish accessibility compliance.
- Does general styling use one accent hue, or at most two, with saturation and brightness variations? Are additional utility, label, and dashboard colors serving distinct informational roles?
- Could a border, accent, shadow, icon, or number be removed without losing meaning or approved identity? Remove redundant treatments.
- Are flat/flatty, gradient, shadow, and brand-expression choices respected across components and states?
- Do realistic content, keyboard use, zoom, and narrow layouts preserve understanding and operation?

Explain meaningful choices in terms of the user's task. Record durable project decisions in existing design documentation; use the [compact template](templates/design-system.md) when a new record is useful. Avoid creating a design-system document for every small task.

## Sources and judgment

The [six annotated articles](references/design-articles.md) explain the foundation and where their advice differs. Consult the relevant article when a decision needs deeper explanation. Numerical examples in those sources illustrate relationships; they do not override this skill's explicit preferences, including its general accent-hue limit, or substitute for reviewing the result. Accessibility requirements remain requirements, not aesthetic suggestions.

When source advice conflicts in a way the task and approved project choices do not resolve, explain the competing recommendations and ask the user about the material tradeoff. Do not silently turn a source's preferred aesthetic into project policy.
