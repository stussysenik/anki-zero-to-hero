import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Tailwind_CSS"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "Layout":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Layout"),
    "Styling":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Styling"),
    "Responsive":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Responsive"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === TAILWIND FUNDAMENTALS ===

c("Fundamentals", "What is Tailwind CSS?",
  "A utility-first CSS framework. Instead of writing custom CSS, you compose designs using pre-built classes directly in HTML. Compiles to only the CSS you actually use via content scanning.",
  ["L0_primitives"])

c("Fundamentals", "How does Tailwind's tree-shaking work?",
  "At build time, Tailwind scans your content files (HTML, JSX, Vue, etc.) for class names. Only the classes found are included in the final CSS bundle. Unused utilities are purged — results in tiny CSS files.",
  ["L0_primitives"])

c("Fundamentals", "What is the Tailwind configuration file?",
  "<code>tailwind.config.js</code> (or <code>.ts</code>) — defines the design system: colors, spacing, fonts, breakpoints, plugins, and content paths. <code>theme.extend</code> adds custom values without losing defaults.",
  ["L0_primitives"])

c("Fundamentals", "What is the Tailwind spacing scale?",
  "A 4px-based scale: <code>p-1</code> = 4px, <code>p-4</code> = 16px, <code>p-8</code> = 32px. Values: 0, 0.5 (2px), 1-12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96. Also supports arbitrary values: <code>p-[13px]</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is a Tailwind utility class?",
  "A single-purpose CSS class: <code>flex</code> → <code>display: flex</code>. <code>text-red-500</code> → <code>color: #ef4444</code>. Composing many utilities replaces writing custom CSS. Classes are self-explanatory.",
  ["L0_primitives"])

c("Fundamentals", "What are Tailwind's layer directives?",
  "<code>@layer base</code>: base styles (reset, HTML elements). <code>@layer components</code>: reusable component classes (cards, buttons). <code>@layer utilities</code>: custom utilities. Order determines specificity priority.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>@apply</code> directive?",
  "Extracts repeated utility patterns into a custom CSS class: <code>.btn { @apply px-4 py-2 rounded bg-blue-500 text-white; }</code>. Use sparingly — prefer component abstraction (React/Vue components) over <code>@apply</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>@tailwind</code> directive?",
  "Injects Tailwind's layers into your CSS: <code>@tailwind base;</code>, <code>@tailwind components;</code>, <code>@tailwind utilities;</code>. Required in your main CSS file. With v4 (if using), these are handled by the new engine.",
  ["L0_primitives"])

c("Fundamentals", "What is arbitrary value syntax in Tailwind?",
  "Square bracket notation for one-off values: <code>w-[300px]</code>, <code>text-[#bada55]</code>, <code>top-[calc(100%+10px)]</code>, <code>grid-cols-[auto,1fr]</code>. Escape whitespace with underscore: <code>before:content-['hello_world']</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is Tailwind's dark mode support?",
  "Two strategies: <code>media</code> — follows OS preference via <code>prefers-color-scheme</code>. <code>class</code> — toggled by adding <code>dark</code> class to HTML. Prefix utilities with <code>dark:</code>: <code>dark:bg-gray-900</code>.",
  ["L0_primitives"])

# === TAILWIND LAYOUT ===

c("Layout", "What class makes an element a flex container?",
  "<code>flex</code> — sets <code>display: flex</code>. For inline flex: <code>inline-flex</code>.",
  ["L1_mechanics"])

c("Layout", "What class centers items horizontally in flexbox?",
  "<code>justify-center</code> — sets <code>justify-content: center</code>. Also: <code>justify-start</code>, <code>justify-end</code>, <code>justify-between</code>, <code>justify-around</code>, <code>justify-evenly</code>.",
  ["L1_mechanics"])

c("Layout", "What class centers items vertically in flexbox?",
  "<code>items-center</code> — sets <code>align-items: center</code>. Also: <code>items-start</code>, <code>items-end</code>, <code>items-baseline</code>, <code>items-stretch</code>.",
  ["L1_mechanics"])

c("Layout", "What class makes a grid container?",
  "<code>grid</code> — sets <code>display: grid</code>. Use with <code>grid-cols-*</code> for column count, <code>gap-*</code> for spacing.",
  ["L1_mechanics"])

c("Layout", "What class defines a 3-column grid?",
  "<code>grid-cols-3</code>. Also: <code>grid-cols-1</code> through <code>grid-cols-12</code>. <code>grid-cols-none</code> for no explicit grid.",
  ["L1_mechanics"])

c("Layout", "What class makes an element span 2 columns in a grid?",
  "<code>col-span-2</code>. Range: <code>col-span-1</code> through <code>col-span-12</code>. <code>col-span-full</code> for all columns.",
  ["L1_mechanics"])

c("Layout", "What class sets position to relative?",
  "<code>relative</code>. Also: <code>absolute</code>, <code>fixed</code>, <code>sticky</code>, <code>static</code>.",
  ["L1_mechanics"])

c("Layout", "What class hides an element?",
  "<code>hidden</code> — <code>display: none</code>. <code>invisible</code> — <code>visibility: hidden</code> (still occupies space). <code>sr-only</code> — visually hidden but accessible to screen readers.",
  ["L1_mechanics"])

c("Layout", "What class sets width to full?",
  "<code>w-full</code> = <code>width: 100%</code>. <code>w-screen</code> = <code>100vw</code>. <code>w-auto</code>. <code>w-1/2</code> = 50%. Fractions: <code>w-1/3</code>, <code>w-2/3</code>, <code>w-1/4</code>, <code>w-3/4</code>, etc.",
  ["L1_mechanics"])

c("Layout", "What class sets maximum width?",
  "<code>max-w-lg</code> (512px), <code>max-w-xl</code> (576px), <code>max-w-2xl</code> (672px), <code>max-w-7xl</code> (1280px). Also: <code>max-w-sm</code>, <code>max-w-md</code>, <code>max-w-full</code>, <code>max-w-screen-xl</code>.",
  ["L1_mechanics"])

c("Layout", "What class adds padding on all sides?",
  "<code>p-4</code> = 16px all around. Directional: <code>pt-4</code> (top), <code>pr-4</code> (right), <code>pb-4</code> (bottom), <code>pl-4</code> (left). Horizontal: <code>px-4</code>. Vertical: <code>py-4</code>.",
  ["L1_mechanics"])

c("Layout", "What class adds margin auto (centering a block)?",
  "<code>mx-auto</code> — auto margin on left and right, centers the element. Also: <code>my-auto</code> for vertical centering in flex/grid.",
  ["L1_mechanics"])

c("Layout", "What class sets gap in flex/grid?",
  "<code>gap-4</code> — 16px gap. <code>gap-x-4</code> (column gap), <code>gap-y-2</code> (row gap). Values from 0 to 96 following the spacing scale.",
  ["L1_mechanics"])

# === TAILWIND STYLING ===

c("Styling", "What class sets text color?",
  "<code>text-{color}-{shade}</code>: <code>text-red-500</code>, <code>text-blue-700</code>, <code>text-white</code>, <code>text-black</code>. Shades: 50-950 in increments. <code>text-current</code> inherits from parent <code>color</code>.",
  ["L1_mechanics"])

c("Styling", "What class sets background color?",
  "<code>bg-{color}-{shade}</code>: <code>bg-gray-100</code>, <code>bg-indigo-600</code>. <code>bg-white</code>, <code>bg-transparent</code>. <code>bg-gradient-to-r from-blue-500 to-purple-500</code> for gradients.",
  ["L1_mechanics"])

c("Styling", "What class sets border?",
  "<code>border</code> (1px solid), <code>border-2</code> (2px), <code>border-4</code> (4px). Color: <code>border-gray-300</code>. Style: <code>border-solid</code>, <code>border-dashed</code>, <code>border-none</code>.",
  ["L1_mechanics"])

c("Styling", "What class makes border radius (rounded corners)?",
  "<code>rounded</code> (4px), <code>rounded-md</code> (6px), <code>rounded-lg</code> (8px), <code>rounded-xl</code> (12px), <code>rounded-2xl</code> (16px), <code>rounded-full</code> (circle), <code>rounded-none</code>.",
  ["L1_mechanics"])

c("Styling", "What class sets text size?",
  "<code>text-xs</code> (12px), <code>text-sm</code> (14px), <code>text-base</code> (16px), <code>text-lg</code> (18px), <code>text-xl</code> (20px), <code>text-2xl</code> (24px) ... <code>text-9xl</code> (128px).",
  ["L1_mechanics"])

c("Styling", "What class sets font weight?",
  "<code>font-thin</code> (100), <code>font-light</code> (300), <code>font-normal</code> (400), <code>font-medium</code> (500), <code>font-semibold</code> (600), <code>font-bold</code> (700), <code>font-extrabold</code> (800), <code>font-black</code> (900).",
  ["L1_mechanics"])

c("Styling", "What class adds shadow?",
  "<code>shadow</code> (small), <code>shadow-sm</code>, <code>shadow-md</code>, <code>shadow-lg</code>, <code>shadow-xl</code>, <code>shadow-2xl</code>, <code>shadow-none</code>, <code>shadow-inner</code>. Color: <code>shadow-red-500/50</code> (with opacity).",
  ["L1_mechanics"])

c("Styling", "What class sets opacity?",
  "<code>opacity-0</code> through <code>opacity-100</code> in increments of 5. <code>opacity-50</code> = 50% opacity. Also: <code>bg-red-500/50</code> for color-specific opacity (the slash syntax).",
  ["L1_mechanics"])

c("Styling", "What class truncates text with ellipsis?",
  "<code>truncate</code> — applies <code>overflow: hidden; text-overflow: ellipsis; white-space: nowrap</code>. For multi-line truncation: <code>line-clamp-3</code> (3 lines, then ellipsis).",
  ["L1_mechanics"])

c("Styling", "What class sets cursor style?",
  "<code>cursor-pointer</code>, <code>cursor-not-allowed</code>, <code>cursor-wait</code>, <code>cursor-text</code>, <code>cursor-move</code>, <code>cursor-grab</code>, <code>cursor-default</code>.",
  ["L1_mechanics"])

# === RESPONSIVE DESIGN ===

c("Responsive", "How do you apply styles at specific breakpoints?",
  "Prefix with breakpoint: <code>sm:flex</code>, <code>md:grid-cols-2</code>, <code>lg:px-8</code>, <code>xl:text-xl</code>, <code>2xl:max-w-7xl</code>. Styles apply at that breakpoint AND up (mobile-first).",
  ["L1_mechanics"])

c("Responsive", "What are Tailwind's default breakpoints?",
  "<code>sm</code>: 640px, <code>md</code>: 768px, <code>lg</code>: 1024px, <code>xl</code>: 1280px, <code>2xl</code>: 1536px. Mobile-first: unprefixed classes apply to all sizes (base = mobile).",
  ["L0_primitives"])

c("Responsive", "What is the mobile-first approach in Tailwind?",
  "Write styles for mobile first (no prefix), then layer larger sizes: <code>class=\"text-sm md:text-base lg:text-lg\"</code>. Small screen gets <code>text-sm</code>, medium gets <code>text-base</code>, large gets <code>text-lg</code>.",
  ["L2_composition"])

c("Responsive", "How do you hide elements responsively?",
  "<code>hidden md:block</code> — hidden on mobile, visible on <code>md</code> and up. <code>block md:hidden</code> — visible on mobile, hidden on larger.",
  ["L1_mechanics"])

# === TAILWIND PATTERNS ===

c("Patterns", "What is the container pattern?",
  "<code>container mx-auto px-4</code> — centers content with responsive max-width and horizontal padding. <code>container</code> sets width, <code>mx-auto</code> centers, <code>px-4</code> adds breathing room.",
  ["L2_composition"])

c("Patterns", "What is the group hover pattern?",
  "Parent gets <code>group</code>, children use <code>group-hover:</code> prefix: <code>&lt;div class=\"group\"&gt;&lt;p class=\"group-hover:text-blue-500\"&gt;Hover me&lt;/p&gt;&lt;/div&gt;</code>. Works with any state: <code>group-focus</code>, <code>group-active</code>.",
  ["L2_composition"])

c("Patterns", "What is the peer pattern?",
  "Sibling-based styling: <code>&lt;input class=\"peer\"&gt;&lt;p class=\"peer-invalid:visible invisible\"&gt;Error&lt;/p&gt;</code>. When peer input is invalid, the error text becomes visible.",
  ["L2_composition"])

c("Patterns", "What is the CVA (Class Variance Authority) pattern?",
  "Define component variants using <code>cva</code> (or <code>class-variance-authority</code> lib): <code>const button = cva('px-4 py-2 rounded', { variants: { intent: { primary: 'bg-blue-500', secondary: 'bg-gray-500' } } })</code>. Used heavily with React/Shadcn.",
  ["L2_composition"])

c("Patterns", "What is the arbitrary variant pattern?",
  "<code>[&amp;:nth-child(3)]:underline</code> — targeting specific child. <code>[@media(hover:hover)]:opacity-100</code> — custom media queries. Square bracket variants for anything not built-in.",
  ["L6_innovation"])

# === TAILWIND GOTCHAS ===

c("Gotchas", "Why aren't my custom colors working?",
  "Define them in <code>tailwind.config.js</code>: <code>theme: { extend: { colors: { brand: '#1e2e3e' } } }</code>. Then use <code>bg-brand</code>, <code>text-brand</code>. Without extending, you'll override ALL default colors.",
  ["L4_diagnosis"])

c("Gotchas", "Why are dynamically constructed classes not working?",
  "Tailwind scans source files at build time. <code>bg-${color}-500</code> is NOT detected because it's a dynamic string. Use full class names: <code>bg-red-500</code> or whitelist/safelist in config. Or use style props for truly dynamic values.",
  ["L4_diagnosis"])

c("Gotchas", "What causes 'The `hover:` class does not exist'?",
  "The hover variant doesn't exist in isolation — it must be combined with a utility: <code>hover:bg-blue-500</code>, not just <code>hover:</code>. Same for all variants.",
  ["L4_diagnosis"])

c("Gotchas", "Why is my <code>z-index</code> not working?",
  "Tailwind's <code>z-10</code> sets <code>z-index: 10</code>, but <code>z-index</code> only works on positioned elements (<code>relative</code>, <code>absolute</code>, <code>fixed</code>, <code>sticky</code>). Add positioning class alongside it.",
  ["L4_diagnosis"])

c("Gotchas", "Why is <code>!important</code> not working with <code>!text-red-500</code>?",
  "The <code>!</code> prefix adds <code>!important</code>: <code>!text-red-500</code> works. But you need to add it to the utility, not replace it. Also check specificity conflicts — <code>!important</code> doesn't fix specificity, it just forces the value.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>space-x-4</code> add margin to first child?",
  "It shouldn't — <code>space-x-*</code> uses the lobotomized owl selector (<code>* + *</code>). But if children are not direct descendants, the selector fails. Ensure children are direct children of the <code>space-x-4</code> element.",
  ["L4_diagnosis"])

# === TAILWIND EXPERT ===

c("Expert", "What is the Tailwind CSS IntelliSense plugin?",
  "VS Code extension providing autocomplete, linting, hover previews, and class sorting. Suggests relevant classes as you type. Also shows the generated CSS for each utility on hover.",
  ["L5_opinion"])

c("Expert", "What is Prettier plugin for Tailwind?",
  "<code>prettier-plugin-tailwindcss</code> — automatically sorts classes in the recommended order (layout → positioning → sizing → typography → visual → states). Ensures consistency across the team.",
  ["L3_design"])

c("Expert", "What are Tailwind plugins?",
  "Extend Tailwind with custom utilities, components, and variants via <code>plugin()</code> function in config. Example: <code>@tailwindcss/typography</code> (the Prose plugin), <code>@tailwindcss/forms</code> (form reset), <code>@tailwindcss/container-queries</code>.",
  ["L6_innovation"])

c("Expert", "How do you handle long, unreadable class strings in JSX?",
  "Use <code>clsx</code> or <code>cn()</code> utility: <code>cn('base-classes', condition &amp;&amp; 'conditional', className)</code>. Pair with <code>cva</code> for variants. Alternatively, use a <code>className</code> helper that splits into multiple lines.",
  ["L3_design"])

c("Expert", "What is the <code>@layer</code> strategy for organizing custom styles?",
  "Put element resets in <code>@layer base</code>, reusable component classes in <code>@layer components</code>, and one-off custom utilities in <code>@layer utilities</code>. This ensures Tailwind's specificity hierarchy is respected.",
  ["L3_design"])

c("Expert", "How do you build a design system with Tailwind?",
  "Define tokens in <code>tailwind.config.js</code>: colors, spacing, font sizes, border radius, shadows. Components use these tokens via utility classes. For React/Vue, wrap component patterns (button variants, card layouts) with <code>cva</code> or similar. Consistency comes from tokens, not custom CSS.",
  ["L3_design"])

c("Expert", "What is Tailwind v4 / Oxide engine?",
  "Tailwind v4 (in development) replaces the JavaScript configuration with CSS-first configuration using <code>@theme</code> directives. Built on Rust-based Oxide engine for faster builds. Configuration moves into CSS: <code>@theme { --color-primary: #1e2e3e; }</code>.",
  ["L6_innovation"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
