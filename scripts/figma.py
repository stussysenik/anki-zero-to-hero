import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Figma"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Components":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Components"),
    "Systems":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Design-Systems"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === FIGMA FUNDAMENTALS ===

c("Fundamentals", "What is Figma?",
  "A cloud-based, collaborative interface design tool running in the browser. Used for UI/UX design, prototyping, design systems, and developer handoff. Real-time multiplayer — like Google Docs for design.",
  ["L0_primitives"])

c("Fundamentals", "What is a Frame in Figma?",
  "The primary container for design. Think of it as an artboard or div. Has a fixed width/height, can clip content, supports auto layout, and represents a screen/section/component. Created with <code>F</code> key.",
  ["L0_primitives"])

c("Fundamentals", "What is Auto Layout?",
  "Figma's flexbox-like system. Frames with auto layout (<code>Shift+A</code>) automatically arrange children horizontally/vertically, with spacing, padding, alignment. Resizes to fit content. Drives responsive design. Replaces manual positioning in most cases.",
  ["L0_primitives"])

c("Fundamentals", "What is a Component in Figma?",
  "A reusable design element with a master definition and instances. Change the master, all instances update. Override instance properties with variants. The foundation of design systems. Keyboard: <code>Ctrl+Alt+K</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is a Variant?",
  "Different states of a component grouped together: button states (default, hover, disabled, active). <code>Add variant</code> creates a component set. Developers see variant props as code-friendly tokens. <code>Button / Primary / Hover</code>.",
  ["L0_primitives"])

c("Fundamentals", "What are Component Properties?",
  "Exposed knobs for component instances: text overrides, boolean visibility toggles, instance swaps, variant selection. Makes components truly reusable without detaching. Defines the component's API for designers.",
  ["L0_primitives"])

c("Fundamentals", "What is a Style in Figma?",
  "Reusable design tokens: colors (fill, stroke), text (font, size, weight), effects (shadows, blur), grids. Defined in the right sidebar. Any change to a style cascades to all elements using it. <code>Ctrl+Alt+</code> to create.",
  ["L0_primitives"])

c("Fundamentals", "What is a Variable in Figma?",
  "Design token v2: a named value that can reference other variables, support modes (light/dark themes), and be scoped. Replaces styles for primitive values. Variables can drive prototype interactions. Boolean/Number/String/Color types.",
  ["L0_primitives"])

c("Fundamentals", "What is Vector Networks in Figma?",
  "Figma's pen tool creates vector networks (not paths). A vector point can have multiple connected edges — like a graph. No direction requirement. Enables complex shapes with fewer points and cleaner geometry.",
  ["L0_primitives"])

c("Fundamentals", "What is the difference between Groups and Frames?",
  "Group: just a selection wrapper, no layout logic, grows to content bounds. Frame: has explicit dimensions, auto layout, clipping, constraints. Use Frames for everything — groups are barely needed in modern Figma.",
  ["L0_primitives"])

# === FIGMA CORE OPERATIONS ===

c("CoreOps", "How do you create a frame?",
  "Press <code>F</code>, then click and drag. Or select an element and use the Frame dropdown in the toolbar. Preset sizes in the right panel. <code>Ctrl+Alt+G</code> to frame an existing selection.",
  ["L1_mechanics"])

c("CoreOps", "How do you toggle Auto Layout?",
  "<code>Shift+A</code> adds/removes auto layout on a frame. Direction, gap, padding, alignment, and resizing options appear in the right sidebar. Nest auto layout frames for complex responsive layouts.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a component?",
  "Select elements, press <code>Ctrl+Alt+K</code> (Windows) or <code>Cmd+Opt+K</code> (Mac). Purple outline indicates a component. Instance from Assets panel or <code>Alt+drag</code>. Detach: <code>Ctrl+Alt+B</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you add variants to a component?",
  "Select component, click <code>Add variant</code> in the Properties section. Name properties: <code>Type=Primary</code>, <code>State=Default</code>. Props become dropdowns on instances. Override by selecting different variant.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a color style?",
  "Select an element with the color, click the four-dot icon next to Fill in the right sidebar, click <code>+</code>. Name it: <code>primary/500</code>. Apply: select element, open Fill, click the four-dot icon, select style.",
  ["L1_mechanics"])

c("CoreOps", "How do you use constraints?",
  "In the right sidebar (no auto layout), set horizontal/vertical constraints: Left, Right, Left &amp; Right, Center, Scale. Determines how the element behaves when its parent frame resizes. Essential for responsive designs.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a prototype connection?",
  "Switch to Prototype tab (top right). Select an element, drag the <code>○</code> node to a target frame. Set interaction: On Click, Navigate To, Smart Animate, etc. Press <code>▶</code> to preview.",
  ["L1_mechanics"])

c("CoreOps", "How do you use Smart Animate?",
  "Select <code>Smart Animate</code> as the animation type in prototype connections. Figma animates matching layer names between frames — position, scale, opacity, rotation. A mini animation engine for micro-interactions.",
  ["L1_mechanics"])

c("CoreOps", "How do you export assets?",
  "Select element, go to Export section in right sidebar. Add export: PNG, SVG, JPG, PDF. Set scale (1x, 2x, 3x). <code>Ctrl+Shift+E</code> to export. <code>Export all</code> for multiple. Dev Mode exports CSS/iOS/Android tokens.",
  ["L1_mechanics"])

c("CoreOps", "What is Dev Mode in Figma?",
  "Toggle with <code>Shift+D</code>. Shows code snippets (CSS, SwiftUI, Compose), spacing measurements, style values, and component documentation. Designed for developer handoff. Separate from the design view.",
  ["L1_mechanics"])

c("CoreOps", "How do you use boolean operations?",
  "Select two shapes, use toolbar: Union, Subtract, Intersect, Exclude. Creates complex shapes from primitives. Non-destructive — select the boolean group to modify original shapes. Found in the top toolbar.",
  ["L1_mechanics"])

c("CoreOps", "How do you use masks?",
  "Place an image above a shape, select both, <code>Ctrl+Alt+M</code> — the shape clips the image. Masks use the bottom-most shape's contour. Edit the mask shape and the clipped content independently.",
  ["L1_mechanics"])

# === COMPONENTS & SYSTEMS ===

c("Components", "What is component-override management?",
  "Instances can override: text content, visibility, swap nested instances, toggle boolean props, select variant props. Overrides are preserved even when the master changes (diff-based). Reset: right-click → Reset Instance.",
  ["L2_composition"])

c("Components", "What is slot components?",
  "Use boolean props and instance swap to create 'slot' areas: a card component with <code>showIcon: boolean</code> and <code>icon: InstanceSwap</code>. Designers can pick which icon to show without detaching.",
  ["L2_composition"])

c("Systems", "What is a Design System in Figma?",
  "A centralized library of components, styles, and variables. Team library: publish components to a shared library. Other files <code>Enable library</code> to use them. Updates push to all consuming files. Layers: Foundation → Components → Patterns → Pages.",
  ["L3_design"])

c("Systems", "How do you organize component naming?",
  "Use <code>/</code> for hierarchy: <code>Button/Primary/Default</code>, <code>Button/Primary/Hover</code>. Figma auto-groups into nested folders in the Assets panel. Consistent naming = discoverable components. Follow atomic design: Atoms/Molecules/Organisms.",
  ["L3_design"])

c("Systems", "What are Variables vs Styles?",
  "Variables (newer): support modes (themes), aliasing (referencing other variables), scoping, and prototype values. Styles: only for visual properties, no modes, no aliasing. Migrate from styles to variables for design tokens; keep styles for typography/effects.",
  ["L3_design"])

# === PATTERNS ===

c("Patterns", "What is the 8pt grid system?",
  "All spacing, sizing, and padding are multiples of 8px (or 4px for dense UIs). In auto layout: gap=24, padding=16, height=48. Ensures visual rhythm and consistency. Use nudge amount <code>8</code> in Figma preferences.",
  ["L2_composition"])

c("Patterns", "What is the responsive resize pattern?",
  "Combine auto layout + constraints: cards with auto layout for internal spacing, constraints to stretch/center in parent frames. Use <code>Resizing: Fill container</code> + <code>Hug</code> for intrinsic sizing. Preview with different frame sizes.",
  ["L2_composition"])

c("Patterns", "What is the design tokens pattern?",
  "Define primitives as variables: <code>color/primary/500</code>, <code>spacing/4</code>, <code>radius/md</code>. Apply to styles and components. When branding changes, edit one variable — entire design system updates. Export tokens to code via Figma API or plugins.",
  ["L3_design"])

c("Patterns", "What is the Base Component pattern?",
  "Create a <code>_Base/Button</code> component with all structure/behavior. Create variant sets (<code>Button/Primary</code>, <code>Button/Secondary</code>) that use Base as a nested instance. Changes to Base cascade everywhere. Inception pattern for component architecture.",
  ["L3_design"])

# === GOTCHAS ===

c("Gotchas", "Why does my component instance not resize with auto layout?",
  "Instance dimensions may be fixed (not <code>Hug</code> or <code>Fill</code>). Check the resizing settings on the component's frames. Instance text that wraps might not propagate height changes — use <code>Hug contents</code> on text layers.",
  ["L4_diagnosis"])

c("Gotchas", "Why are my constraints not working?",
  "Constraints apply to direct children of frames WITHOUT auto layout. If auto layout is ON, constraints are hidden — auto layout handles positioning. Choose: auto layout (preferred) OR constraints, not both on the same frame.",
  ["L4_diagnosis"])

c("Gotchas", "Why does Smart Animate not work?",
  "Requirements: 1) Layers must have matching names (case-sensitive). 2) Layers must exist in both frames. 3) Should be within the same top-level frame structure. 4) Animation properties must be different between states. Add <code>#</code> suffix to duplicate layer names.",
  ["L4_diagnosis"])

c("Gotchas", "Why do absolute positioned elements in auto layout misbehave?",
  "Absolute position (<code>Ctrl+Shift+A</code>) removes element from auto layout flow. It positions relative to the parent frame edges. Used for badges, floating buttons. Check constraints on the absolute element — they control which corner it sticks to.",
  ["L4_diagnosis"])

c("Gotchas", "Why is my text inconsistent across instances?",
  "Text styles override font-family, size, weight, line-height. If an instance's text looks different, check that it's using the same style. Component text properties can be bound to a text variable for consistent content across instances.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "What is the Figma Plugin API?",
  "JavaScript-based API for extending Figma. Create plugins with <code>figma.showUI()</code>. Access document nodes, styles, variables. Distribute on Figma Community. Written in TypeScript with <code>@figma/plugin-typings</code>. Local dev: <code>Plugins → Development → New Plugin</code>.",
  ["L6_innovation"])

c("Expert", "What is the Figma REST API?",
  "Programmatic access to files, components, styles, comments. <code>GET /v1/files/:key</code> returns the full document JSON. <code>GET /v1/files/:key/components</code> for components. Used for design token extraction, automated asset export, documentation generation, CI integration.",
  ["L6_innovation"])

c("Expert", "What is Figma Branching and Merging?",
  "Like git for design: create a branch, make changes, review, merge. File must be in a Professional/Organization plan. Branch protects the main design while experimenting. Merge resolves conflicts. Enables design reviews and parallel work.",
  ["L6_innovation"])

c("Expert", "What are Figma Modes (Theme Switching)?",
  "Variables can have multiple modes: <code>Light</code>, <code>Dark</code>, <code>High Contrast</code>. Each mode stores different values for the same variable. Apply a mode to a frame — all variables resolve to that mode. Prototype: <code>Set variable mode</code> interaction to toggle themes.",
  ["L3_design"])

c("Expert", "How do you set up a Dev Handoff workflow?",
  "Use Dev Mode (<code>Shift+D</code>). Annotate components with descriptions and links (right panel). Use section statuses (Ready for dev, In progress). Export variables as design tokens (JSON). Integrate with tooling: Figma → Tokens Studio → Style Dictionary → Code.",
  ["L5_opinion"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
