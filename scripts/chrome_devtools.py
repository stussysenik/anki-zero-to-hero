import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Chrome_DevTools"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals":          genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "ElementsStyles":        genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Elements-Styles"),
    "Console":               genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Console"),
    "Network":               genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Network"),
    "SourcesDebugging":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Sources-Debugging"),
    "Performance":           genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Performance"),
    "MemoryApplication":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Memory-Application"),
    "SecuritySensors":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Security-Sensors"),
    "AdvancedWorkflows":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::09-Advanced-Workflows"),
    "Extending":             genanki.Deck(R(), f"{TOPIC}::Zero2Hero::10-Extending-DevTools"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ============================================================
# 01 — FUNDAMENTALS (L0 Primitives + L1 Mechanics)
# ============================================================

c("Fundamentals",
  "What is Chrome DevTools?",
  "A set of web developer tools built directly into the Google Chrome browser. It lets you inspect, debug, and profile web applications in real time — edit pages on the fly, diagnose network issues, profile performance, audit accessibility, and debug JavaScript all from within the browser.",
  ["fundamentals", "L0"])

c("Fundamentals",
  "How do you open Chrome DevTools?",
  "<code>F12</code> (Windows/Linux) or <code>Cmd+Opt+I</code> (Mac) — opens the last-used panel. Alternatively: right-click any element and select <b>Inspect</b>, or use Chrome menu → More Tools → Developer Tools.",
  ["fundamentals", "L0", "keybinding"])

c("Fundamentals",
  "What does <code>Ctrl+Shift+I</code> / <code>Cmd+Opt+I</code> do?",
  "Opens Chrome DevTools — the last-used panel appears by default.",
  ["fundamentals", "L0", "keybinding"])

c("Fundamentals",
  "What does <code>Ctrl+Shift+J</code> / <code>Cmd+Opt+J</code> do?",
  "Opens DevTools directly to the <b>Console</b> panel.",
  ["fundamentals", "L0", "keybinding"])

c("Fundamentals",
  "What does <code>Ctrl+Shift+C</code> / <code>Cmd+Opt+C</code> do when DevTools is open?",
  "Toggles <b>Inspect Element</b> mode — the cursor becomes a crosshair; click any element on the page to select it in the Elements panel.",
  ["fundamentals", "L0", "keybinding"])

c("Fundamentals",
  "What are the main panels in Chrome DevTools?",
  "<b>Elements</b> — DOM + CSS<br><b>Console</b> — JS output, CLI<br><b>Sources</b> — Debugger, file system<br><b>Network</b> — HTTP requests, WebSockets<br><b>Performance</b> — runtime profiling<br><b>Memory</b> — heap, allocation timelines<br><b>Application</b> — storage, service workers<br><b>Security</b> — HTTPS, certificates<br><b>Lighthouse</b> — audits<br><b>Recorder</b> — user flow recording<br><b>Animations</b> — CSS animation inspector<br><b>Sensors</b> — geolocation, orientation override",
  ["fundamentals", "L0"])

c("Fundamentals",
  "What is the Command Menu and how do you open it?",
  "<code>Ctrl+Shift+P</code> / <code>Cmd+Shift+P</code> — the Command Menu is a fuzzy-search command palette that lets you run any DevTools action (switch panels, run snippets, change settings, simulate features) without using the mouse.",
  ["fundamentals", "L0", "keybinding"])

c("Fundamentals",
  "What are the three DevTools dock positions?",
  "<b>Bottom</b> (default) — below the viewport<br><b>Right</b> — to the right of the viewport (good for wide screens)<br><b>Undocked</b> — separate window (good for multi-monitor)<br>Toggle with <code>Ctrl+Shift+D</code> / <code>Cmd+Shift+D</code> or via the ⋮ menu → Dock side.",
  ["fundamentals", "L0"])

c("Fundamentals",
  "How do you open DevTools Settings?",
  "<code>F1</code> while DevTools is focused, or click the gear icon ⚙︎ in the top-right corner, or <code>Cmd+Shift+P</code> → 'Settings'.",
  ["fundamentals", "L0", "keybinding"])

c("Fundamentals",
  "How do you search across all loaded sources in DevTools?",
  "<code>Ctrl+Shift+F</code> / <code>Cmd+Opt+F</code> — opens the <b>Search</b> panel, which searches across all loaded scripts, stylesheets, and source files. Unlike <code>Ctrl+F</code> which searches only the current file.",
  ["fundamentals", "L1", "keybinding"])

c("Fundamentals",
  "What does <code>Ctrl+O</code> / <code>Cmd+O</code> do in DevTools?",
  "Opens the <b>Open File</b> dialog — fuzzy-search to quickly jump to any source file loaded by the page (JS, CSS, HTML, WASM, source maps).",
  ["fundamentals", "L1", "keybinding"])

c("Fundamentals",
  "How do you toggle the Device Toolbar (responsive design mode)?",
  "<code>Ctrl+Shift+M</code> / <code>Cmd+Shift+M</code> — toggles the device toolbar at the top of the viewport, letting you emulate different screen sizes, device pixel ratios, and touch input.",
  ["fundamentals", "L1", "keybinding"])

c("Fundamentals",
  "What does the 'Disable cache' checkbox do in DevTools?",
  "When checked (Network panel), Chrome bypasses the HTTP cache for all requests while DevTools is open. This ensures you always see the freshest resources during development — equivalent to a hard reload.",
  ["fundamentals", "L1"])

c("Fundamentals",
  "How do you do a hard reload (bypass cache)?",
  "<b>Right-click the refresh button</b> → Empty Cache and Hard Reload, or hold <code>Shift</code> while clicking refresh, or <code>Ctrl+Shift+R</code> / <code>Cmd+Shift+R</code>. In DevTools, right-click the refresh button for all three reload options.",
  ["fundamentals", "L1", "keybinding"])

c("Fundamentals",
  "What are the three reload options when you right-click the Chrome refresh button?",
  "<b>Normal Reload</b> — Cmd+R / Ctrl+R<br><b>Hard Reload</b> — Shift+Cmd+R / Ctrl+Shift+R (bypasses cache)<br><b>Empty Cache & Hard Reload</b> — Clears the cache entirely, then does a hard reload. The most thorough refresh.",
  ["fundamentals", "L1"])

c("Fundamentals",
  "What is a 'Live Expression' in the Console?",
  "Click the eye icon 👁 in the Console to pin a JavaScript expression that evaluates in real time as you interact with the page. Uses include watching <code>document.activeElement</code>, tracking scroll position, or monitoring any variable.",
  ["fundamentals", "L1"])

c("Fundamentals",
  "How do you emulate a different user-agent in DevTools?",
  "Network panel → Network conditions tab → uncheck 'Use browser default' under User agent, or Command Menu → 'Show Network conditions'. Alternatively, Sensors panel has UA override. The page sees the spoofed UA string.",
  ["fundamentals", "L1"])

c("Fundamentals",
  "How do you emulate different network conditions (throttling)?",
  "Network panel → 'No throttling' dropdown → select preset (Slow 3G, Fast 3G, Slow 4G) or add a custom profile. Also available in Performance panel's capture settings. Throttling applies to all network requests from the tab.",
  ["fundamentals", "L1"])

c("Fundamentals",
  "What is the 'Rendering' panel and how do you open it?",
  "Command Menu → 'Show Rendering'. It provides checkboxes for: <b>Paint flashing</b> (green flash on repaints), <b>Layout Shift Regions</b> (blue flash on CLS), <b>Layer borders</b> (orange borders), <b>FPS meter</b>, <b>Scrolling performance issues</b>, <b>Core Web Vitals overlay</b>, and <b>Emulate CSS media</b> (prefers-color-scheme, prefers-reduced-motion).",
  ["fundamentals", "L1"])

c("Fundamentals",
  "What is the 'Changes' panel and how do you open it?",
  "Command Menu → 'Show Changes'. It shows a diff of all CSS and DOM modifications you've made in DevTools since page load — like <code>git diff</code> for the current page. Green = additions, Red = deletions. Extremely useful for copying your DevTools tweaks back into source code.",
  ["fundamentals", "L1"])

c("Fundamentals",
  "What are the three dot menus in the top-right of each DevTools panel?",
  "The vertical ⋮ (kebab) menu on a <b>panel tab</b> lets you move/hide panels. The horizontal ⋯ (meatball) menu inside a panel (e.g., in the Elements sidebar) has panel-specific actions. The gear ⚙ icon opens Settings.",
  ["fundamentals", "L1"])

c("Fundamentals",
  "How do you take a screenshot of a specific DOM node?",
  "Select the node in Elements → press <code>Cmd+Shift+P</code> → 'Capture node screenshot'. For full-page: 'Capture full size screenshot'. For a selection area: 'Capture area screenshot' → drag to select region.",
  ["fundamentals", "L1"])

c("Fundamentals",
  "What is the difference between <code>console.log</code> and <code>console.dir</code>?",
  "<code>console.log(obj)</code> prints the object in a tree representation (useful for DOM elements — shows HTML tree). <code>console.dir(obj)</code> prints a JSON-style interactive property list of the JavaScript object — use this when you need to inspect a DOM element's JS properties rather than its HTML structure.",
  ["fundamentals", "L1"])

c("Fundamentals",
  "How do you preserve the Console log across page navigations?",
  "Console panel → click the gear ⚙ → check <b>'Preserve log'</b>. This prevents the console from clearing when the page navigates or reloads. Same option exists in the Network panel for preserving HTTP request logs across page loads.",
  ["fundamentals", "L1"])

c("Fundamentals",
  "What is Autofill in DevTools and how do you test it?",
  "Application panel → Storage → Autofill. You can view, add, and delete autofill entries (addresses, credit cards). Command Menu → 'Show Autofill' opens it directly. Useful for testing form autofill behavior.",
  ["fundamentals", "L1"])

# ============================================================
# 02 — ELEMENTS & STYLES (L1 Mechanics + L2 Composition)
# ============================================================

c("ElementsStyles",
  "What do you press to inspect an element on the page?",
  "<code>Ctrl+Shift+C</code> / <code>Cmd+Opt+C</code> toggles Inspect Element mode, then click the element. Alternatively, right-click any element → <b>Inspect</b>.",
  ["elements", "L1", "keybinding"])

c("ElementsStyles",
  "How do you edit HTML content of an element in DevTools?",
  "Double-click the text content in the DOM tree, type, and press Enter. OR right-click the element → <b>Edit as HTML</b> for full HTML editing in a text field. OR press <code>F2</code> to edit an element's outerHTML inline.",
  ["elements", "L1"])

c("ElementsStyles",
  "How do you edit an element's attributes in DevTools?",
  "Double-click the attribute name or value in the DOM tree, or right-click → <b>Add attribute</b>. Press <code>Enter</code> to confirm, <code>Tab</code> to move to the next attribute, <code>Esc</code> to cancel.",
  ["elements", "L1"])

c("ElementsStyles",
  "How do you delete a DOM node in DevTools?",
  "Select the node and press <code>Delete</code> / <code>Backspace</code>, or right-click → <b>Delete element</b>.",
  ["elements", "L1", "keybinding"])

c("ElementsStyles",
  "How do you move a DOM node to a different parent?",
  "Drag and drop the node in the DOM tree to its new position, or right-click → <b>Cut</b> then right-click target → <b>Paste</b>.",
  ["elements", "L1"])

c("ElementsStyles",
  "How do you force an element state (:hover, :active, :focus, :focus-visible, :visited)?",
  "Right-click the element in the DOM tree → <b>Force state</b> → choose <code>:hover</code>, <code>:active</code>, <code>:focus</code>, <code>:focus-visible</code>, or <code>:visited</code>. Or use the <code>:hov</code> button in the Styles pane to toggle states and see applied CSS.",
  ["elements", "L1"])

c("ElementsStyles",
  "Where are the CSS Styles computed for an element displayed?",
  "The <b>Styles</b> pane (right sidebar) shows the cascaded rules matching the selected element, ordered by specificity. The <b>Computed</b> tab shows the final resolved values for every CSS property on that element — click any property to see which rule set it and the cascade chain.",
  ["elements", "L1"])

c("ElementsStyles",
  "How do you add a new CSS rule or property in the Styles pane?",
  "Click the <code>+</code> (New Style Rule) button in the Styles pane to create a new selector targeting the selected element. To add a property inside an existing rule block, click between the braces <code>{}</code> and start typing.",
  ["elements", "L1"])

c("ElementsStyles",
  "How do you toggle a CSS property on/off without deleting it?",
  "Uncheck/check the checkbox next to the property name in the Styles pane. This lets you test the effect of a property without losing the value.",
  ["elements", "L1"])

c("ElementsStyles",
  "How do you increment/decrement numeric CSS values with the keyboard?",
  "Click the numeric value in the Styles pane and press:<br><code>Up</code> / <code>Down</code> — increment/decrement by 1<br><code>Shift+Up</code> / <code>Shift+Down</code> — by 10<br><code>Alt+Up</code> / <code>Alt+Down</code> — by 0.1 (Mac: Opt+Up/Down)<br><code>Page Up</code> / <code>Page Down</code> — by 100",
  ["elements", "L1", "keybinding"])

c("ElementsStyles",
  "What is the Color Picker in DevTools?",
  "Click any color swatch (small colored square) next to a CSS color value. Opens a full color picker with: eyedropper (pick color from page), hue/opacity sliders, format switcher (hex, rgb, hsl, hwb), color palette history, and contrast ratio display.",
  ["elements", "L1"])

c("ElementsStyles",
  "How do you use the Eyedropper tool?",
  "Open the Color Picker by clicking a color swatch in the Styles pane, then click the eyedropper icon 🎨 → hover over any pixel on the page → click to pick that exact color. Or Command Menu → 'Show Eyedropper'.",
  ["elements", "L1"])

c("ElementsStyles",
  "What CSS color format shortcuts does the Color Picker support?",
  "Hold <code>Shift</code> and click the color swatch to cycle through color formats: <code>hex</code> → <code>rgb()</code> → <code>hsl()</code> → <code>hwb()</code>. The contrast ratio display shows AA/AAA compliance against the background color.",
  ["elements", "L1", "keybinding"])

c("ElementsStyles",
  "What is the Box Model diagram in the Computed pane?",
  "A visual representation showing <b>content</b> (blue), <b>padding</b> (green), <b>border</b> (yellow-orange), and <b>margin</b> (brown) for the selected element. Hover over any region to highlight it on the page. Double-click any value to edit it inline.",
  ["elements", "L1"])

c("ElementsStyles",
  "How do you inspect and debug CSS Flexbox layouts?",
  "Click the <code>flex</code> badge next to a <code>display: flex</code> element in the Elements panel (purple badge), or open the <b>Layout</b> pane. Shows flex-direction, alignment, gaps, and highlights the flex container and items on the page with colored overlays. Check 'Show flexbox overlays' in Layout pane.",
  ["elements", "L2"])

c("ElementsStyles",
  "How do you inspect and debug CSS Grid layouts?",
  "Click the <code>grid</code> badge next to a <code>display: grid</code> element (teal badge), or open the <b>Layout</b> pane. Toggle grid overlays (line numbers, track sizes, area names) for any grid on the page. You can view multiple grids simultaneously. The Layout pane shows every grid container on the page.",
  ["elements", "L2"])

c("ElementsStyles",
  "What information does the Layout pane show for a Grid container?",
  "The <b>Layout</b> pane (in the Elements sidebar) lists every grid container on the page with checkboxes to toggle overlays. For the selected grid: shows <b>track sizes</b> (each column/row width/height), <b>line numbers</b>, <b>area names</b>, and <b>grid gap</b>. The overlay renders on the page with colored dashed lines and labels.",
  ["elements", "L2"])

c("ElementsStyles",
  "What does the 'Layout Shift Regions' checkbox in the Rendering panel do?",
  "Highlights <b>CLS (Cumulative Layout Shift)</b> regions with a blue flash whenever the layout shifts unexpectedly. Critical for debugging layout stability issues that hurt Core Web Vitals scores. Use alongside the Performance panel's 'Web Vitals' lane.",
  ["elements", "L2"])

c("ElementsStyles",
  "What is the CSS Overview panel?",
  "Command Menu → 'Show CSS Overview' → Capture overview. Analyzes the entire page and reports: <b>Colors</b> (palette, contrast issues), <b>Fonts</b> (families, sizes, weights used), declarations not used anywhere, <b>Media queries</b>, and selectors. A health-check tool for CSS codebase hygiene.",
  ["elements", "L2"])

c("ElementsStyles",
  "How do you copy an element's CSS styles, selector, or JS path?",
  "Right-click the element in the DOM tree → <b>Copy</b> → choose from: <b>Copy selector</b> (CSS selector), <b>Copy JS path</b> (JavaScript document.querySelector path), <b>Copy styles</b> (all computed CSS), <b>Copy element</b> (HTML), <b>Copy outerHTML</b>.",
  ["elements", "L1"])

c("ElementsStyles",
  "How do you break on DOM subtree modifications or attribute changes?",
  "Right-click the element → <b>Break on</b> → <b>Subtree modifications</b> (when any child is added/removed), <b>Attribute modifications</b> (when attributes change), or <b>Node removal</b> (when the element itself is removed). This sets a DOM breakpoint — execution pauses in the Sources panel showing the JS that triggered the change.",
  ["elements", "L2"])

c("ElementsStyles",
  "What are DOM breakpoints and where do you manage them?",
  "DOM breakpoints pause JavaScript execution when a DOM node or its subtree is modified. Set via Elements panel → right-click → Break on. Manage all DOM breakpoints in the <b>Sources panel → DOM Breakpoints</b> pane (in the debugger sidebar). You can disable, remove, or see what triggered each.",
  ["elements", "L2"])

c("ElementsStyles",
  "How do you scroll an element into view from the Elements panel?",
  "Right-click the element → <b>Scroll into view</b>. The page scrolls to make the element visible. Use this when an element is off-screen or in a scrollable container.",
  ["elements", "L1"])

c("ElementsStyles",
  "What are 'Badges' in the Elements panel?",
  "Small colored labels that appear next to elements in the DOM tree. A <code>flex</code> badge (purple) indicates <code>display: flex</code>. A <code>grid</code> badge (teal) indicates <code>display: grid</code>. A <code>scroll</code> badge (yellow badge with arrow) shows scrollable elements and highlights scroll overflow. Click any badge to toggle the corresponding overlay.",
  ["elements", "L1"])

c("ElementsStyles",
  "How do you view and edit CSS custom properties (variables) in DevTools?",
  "In the Styles pane, custom properties (<code>--my-var</code>) appear with their resolved values. Hover a <code>var(--name)</code> usage to see its value. The <b>Computed</b> tab shows all registered custom properties and their computed values at the bottom in a special 'Registered Properties' section.",
  ["elements", "L1"])

c("ElementsStyles",
  "How do you view all event listeners attached to an element?",
  "In the Elements panel, next to the element in the DOM tree, you'll see a <code>event</code> badge (or expand the <b>Event Listeners</b> tab in the sidebar). It shows all listeners grouped by event type (click, keydown, etc.), their source file location (clickable to jump to Sources), and whether they use passive/capture/once.",
  ["elements", "L2"])

c("ElementsStyles",
  "How do you inspect Shadow DOM in DevTools?",
  "Shadow DOM trees appear in the Elements panel indented under the host element with a <code>#shadow-root (open)</code> label. You can expand and interact with them just like regular DOM. Settings → Preferences → 'Show user agent shadow DOM' reveals browser-internal shadow trees (e.g., video controls, input internals).",
  ["elements", "L2"])

c("ElementsStyles",
  "How do you edit a CSS pseudo-element (::before, ::after) style?",
  "Expand the element in the DOM tree — pseudo-elements appear as child nodes labeled <code>::before</code> and <code>::after</code>. Click one to see and edit its styles in the Styles pane. Pseudo-elements are only visible in the DOM tree if they have <code>content</code> set.",
  ["elements", "L2"])

c("ElementsStyles",
  "What is the Animations panel and what does it show?",
  "Command Menu → 'Show Animations'. Shows a timeline of all CSS animations and transitions on the page. Each animation appears as a colored bar — drag to scrub, adjust timing, or replay. You can modify <code>animation-duration</code>, <code>animation-delay</code>, <code>animation-timing-function</code> (with a cubic-bezier editor), and <code>animation-iteration-count</code>.",
  ["elements", "L2"])

c("ElementsStyles",
  "How do you edit a CSS animation's easing curve in DevTools?",
  "Click the easing function value (e.g., <code>cubic-bezier(0.4, 0.0, 0.2, 1)</code>) in the Styles pane to open the <b>cubic-bezier editor</b>. Drag the control points to visually adjust the curve. The Animations panel's easing editor also shows a preview dot that animates with the curve.",
  ["elements", "L2"])

c("ElementsStyles",
  "How do you view accessibility information for an element?",
  "Select the element in Elements → open the <b>Accessibility</b> pane in the sidebar. Shows: computed ARIA role, ARIA name, ARIA properties, keyboard-focusable status, color contrast ratio (with AA/AAA compliance), and the full accessibility tree starting from that node.",
  ["elements", "L2"])

# ============================================================
# 03 — CONSOLE (L1 Mechanics + L2 Composition)
# ============================================================

c("Console",
  "What are Console Utilities ($_, $0, $1-$4, $(selector), $$(selector), $x(xpath))?",
  "<code>$0</code> — currently selected element in Elements.<br><code>$1</code>–<code>$4</code> — previously selected elements (history stack).<br><code>$_</code> — result of the last evaluated expression.<br><code>$(selector)</code> — alias for <code>document.querySelector()</code><br><code>$$(selector)</code> — alias for <code>document.querySelectorAll()</code>, returns array.<br><code>$x(xpath)</code> — evaluate XPath expression, returns array of matching nodes.",
  ["console", "L1", "utilities"])

c("Console",
  "What does <code>$0</code> refer to in the Console?",
  "The element currently selected in the <b>Elements</b> panel. <code>$1</code> is the previously selected element, <code>$2</code> the one before that, up to <code>$4</code>. These are live references — if the DOM changes, <code>$0</code> reflects the current state.",
  ["console", "L1"])

c("Console",
  "What is <code>copy()</code> in the Console and how is it used?",
  "<code>copy($0)</code> copies the string representation of the argument to the clipboard. Works with strings, objects (JSON.stringified), and DOM nodes (outerHTML). Extremely useful for grabbing data from the page. <code>copy($$('a').map(a => a.href).join('\\n'))</code> copies all links.",
  ["console", "L1", "utilities"])

c("Console",
  "What does <code>monitor()</code> and <code>unmonitor()</code> do?",
  "<code>monitor(fn)</code> makes the Console log every call to <code>fn</code> with arguments. <code>unmonitor(fn)</code> stops monitoring. Example: <code>monitor(window.scrollTo)</code> logs every scroll call. Useful for debugging which code is calling a function and with what args.",
  ["console", "L1"])

c("Console",
  "What does <code>monitorEvents()</code> do?",
  "<code>monitorEvents($0, ['click', 'keydown'])</code> logs every event of the specified types fired on the target element. <code>monitorEvents($0, 'mouse')</code> monitors all mouse events. <code>unmonitorEvents($0)</code> stops. This is a live event spy — see every event with its properties.",
  ["console", "L1", "utilities"])

c("Console",
  "What does <code>getEventListeners($0)</code> return?",
  "Returns an object mapping event types to arrays of registered listener functions on the element. Each listener entry shows: the callback function (source-able), <code>useCapture</code>, <code>passive</code>, <code>once</code> flags, and the <code>listener</code> reference. Unlike the Elements panel sidebar, this works in the Console for scripting.",
  ["console", "L1"])

c("Console",
  "What is <code>queryObjects(Constructor)</code>?",
  "<code>queryObjects(Promise)</code> returns an array of all live objects created with the given constructor that haven't been garbage collected. Useful for finding leaked objects. Example: <code>queryObjects(AbortController)</code> to find controllers that were never aborted.",
  ["console", "L1"])

c("Console",
  "What are the key console methods beyond <code>console.log</code>?",
  "<code>console.warn()</code> — yellow warning message with stack trace.<br><code>console.error()</code> — red error with stack trace.<br><code>console.info()</code> — info-level message.<br><code>console.debug()</code> — only shown at verbose log level.<br><code>console.table(data)</code> — renders an array/object as a sortable table.<br><code>console.group(label)</code> / <code>console.groupEnd()</code> — collapsible group.<br><code>console.assert(cond, msg)</code> — logs error if condition is falsy.<br><code>console.time(label)</code> / <code>console.timeEnd(label)</code> — measure duration.<br><code>console.count(label)</code> — count how many times a line executes.<br><code>console.trace()</code> — print stack trace.<br><code>console.dir(obj)</code> — interactive JS object inspector.<br><code>console.clear()</code> — clear console.",
  ["console", "L1"])

c("Console",
  "What is <code>console.table()</code> and when should you use it?",
  "<code>console.table(data)</code> renders an array of objects or a 2D array as a sortable, filterable table in the Console. Click column headers to sort. Use it for:<br>1. Viewing API response arrays<br>2. Inspecting event listener lists<br>3. Debugging data transformations<br>4. Comparing object properties at a glance",
  ["console", "L1"])

c("Console",
  "How do you use <code>console.group()</code> effectively?",
  "<code>console.group('User API Call')</code> starts a collapsible group; <code>console.groupEnd()</code> closes it. Use <code>console.groupCollapsed()</code> for initially collapsed. Nest groups for hierarchical output. Example pattern for an API call:<br><code>console.group('GET /users'); console.log('headers', headers); console.table(data); console.groupEnd();</code>",
  ["console", "L1"])

c("Console",
  "What does <code>console.time()</code> / <code>console.timeEnd()</code> do?",
  "Creates a named timer: <code>console.time('render')</code> starts it, <code>console.timeEnd('render')</code> prints the elapsed ms. Multiple timers can run simultaneously with different labels. <code>console.timeLog('render')</code> prints the current elapsed time without stopping. More precise than <code>Date.now()</code> wrapping for quick performance checks.",
  ["console", "L1"])

c("Console",
  "What does <code>console.trace()</code> output?",
  "Prints a full call stack trace in the Console — showing the exact function call chain that led to that line. Each stack frame is a clickable link to the source file. Use it to answer the question 'who called this function?' without setting a breakpoint.",
  ["console", "L1"])

c("Console",
  "What is the difference between <code>console.assert()</code> and a manual <code>if</code> check?",
  "<code>console.assert(condition, 'message')</code> only logs to the console if the condition is <b>falsy</b>. Unlike throw, it doesn't halt execution or affect program flow — it's a non-invasive assertion for development. Use it to verify invariants without breaking the user experience.",
  ["console", "L1"])

c("Console",
  "How do you filter console output by log level or keywords?",
  "The Console sidebar has checkboxes: <b>Errors</b>, <b>Warnings</b>, <b>Info</b>, <b>Verbose</b>. The filter bar at the top accepts text to filter messages. Enter a <b>regex</b> pattern by wrapping in <code>/</code> slashes: <code>/fetch|axios/</code>. Enter a <b>negative filter</b> with <code>-</code> prefix: <code>-node_modules</code> to exclude noise.",
  ["console", "L1"])

c("Console",
  "How do you write multi-line expressions in the Console?",
  "<code>Shift+Enter</code> inserts a newline without executing the expression. <code>Enter</code> alone executes. For snippets, click the <code>{}</code> (multi-line editor) button at the bottom-left of the Console to expand a code editor area. The Console auto-indents within brackets/parens.",
  ["console", "L1", "keybinding"])

c("Console",
  "What is the <code>{}</code> button (multi-line editor) in the Console?",
  "Click the <code>{ }</code> icon at the bottom-left of the Console (or <code>Ctrl+[</code> / <code>Cmd+[</code>) to expand a dedicated code editor area at the bottom. You can write multi-line JavaScript, then press <code>Ctrl+Enter</code> / <code>Cmd+Enter</code> to execute. <code>Ctrl+Enter</code> in the single-line input also creates a newline.",
  ["console", "L1", "keybinding"])

c("Console",
  "How do you log variables with automatic labels using shorthand?",
  "Use object shorthand: <code>console.log({x, y, z})</code> instead of <code>console.log('x:', x, 'y:', y)</code>. The Console displays <code>{x: 42, y: 'hello', z: true}</code> — automatically labeled, less typing, and expandable as an object tree. ES6 shorthand is self-documenting.",
  ["console", "L2"])

c("Console",
  "What is <code>console.log()</code> styling with <code>%c</code>?",
  "<code>console.log('%c Big Red Text', 'color: red; font-size: 24px;')</code> — the <code>%c</code> specifier applies CSS to subsequent text until the next <code>%c</code>. Use for debug banners, visual markers, or making critical logs stand out. Multiple <code>%c</code> specifiers work in sequence.",
  ["console", "L2"])

c("Console",
  "What live expressions should you commonly pin in the Console?",
  "<code>document.activeElement</code> — which element has focus<br><code>document.querySelectorAll('img').length</code> — image count<br><code>JSON.parse(document.querySelector('#__NEXT_DATA__')?.textContent || '{}')</code> — server state (Next.js)<br><code>window.scrollY</code> — scroll position<br><code>window.___someGlobal</code> — any global state you're debugging",
  ["console", "L2"])

c("Console",
  "How do you use the Command Menu to access Console features?",
  "<code>Cmd+Shift+P</code>:<br>- 'Show Console' — switch to Console panel<br>- 'Create live expression' — pin a new live expression<br>- 'Show changes' — view CSS/JS modifications<br>- 'Clear console' — equivalent to <code>console.clear()</code> or <code>Ctrl+L</code><br>- 'Show network console' — filter to network-only messages",
  ["console", "L2"])

# ============================================================
# 04 — NETWORK (L1 Mechanics + L2 Composition + L3 Design)
# ============================================================

c("Network",
  "What does the Network panel show?",
  "Every HTTP request and response made by the page — including XHR/fetch, JS, CSS, images, fonts, WebSockets, Server-Sent Events, and WebTransport. For each request: URL, method, status code, type, size, timing, waterfall. The cascade (waterfall) visualizes request dependencies and duration.",
  ["network", "L1"])

c("Network",
  "How do you filter network requests by type?",
  "Click the filter buttons at the top: <b>XHR/Fetch</b>, <b>JS</b>, <b>CSS</b>, <b>Img</b>, <b>Media</b>, <b>Font</b>, <b>Doc</b>, <b>WS</b> (WebSocket), <b>Wasm</b>, <b>Manifest</b>, <b>Other</b>. Hold <code>Cmd/Ctrl</code> to select multiple types. The search/filter input also supports filtering by URL, headers, or response body content.",
  ["network", "L1", "keybinding"])

c("Network",
  "How do you block specific requests in the Network panel?",
  "Right-click a request → <b>Block request URL</b> or <b>Block request domain</b>. All future requests matching the pattern are blocked (no network fetch). Manage blocked patterns in the <b>Network request blocking</b> tab (Command Menu → 'Show Network request blocking'). Useful for testing offline behavior for specific resources.",
  ["network", "L2"])

c("Network",
  "What does 'Preserve log' do in the Network panel?",
  "Checking <b>'Preserve log'</b> prevents the network log from being cleared on page navigation. Without it, the log resets every time you navigate. Essential when debugging redirect chains, form submissions that navigate, or multi-page auth flows.",
  ["network", "L2"])

c("Network",
  "What is the difference between 'Disable cache' in the Network panel and a Hard Reload?",
  "<b>Disable cache</b> — bypasses the HTTP cache for ALL subsequent requests while DevTools is open. Persistent setting.<br><b>Hard Reload</b> — bypasses cache for one page load only.<br>Use 'Disable cache' during sustained development; use Hard Reload for one-off testing.",
  ["network", "L2"])

c("Network",
  "What HTTP request information can you inspect in the Headers tab?",
  "<b>General</b>: Request URL, Method, Status Code, Remote Address, Referrer Policy<br><b>Response Headers</b>: server, content-type, cache-control, set-cookie, CORS headers<br><b>Request Headers</b>: authority, method, path, cookie, user-agent, accept, content-type<br><b>Query String Parameters</b>: parsed URL parameters<br>The 'Raw' toggle shows the literal header text.",
  ["network", "L1"])

c("Network",
  "What is shown in the Preview tab of a network request?",
  "A <b>rendered preview</b> of the response body based on content-type: JSON is shown as an expandable tree, images are shown inline, HTML/CSS/JS show a syntax-highlighted preview, fonts show a preview of glyphs. The <b>Response</b> tab shows the raw response body text.",
  ["network", "L1"])

c("Network",
  "What is shown in the Timing tab of a network request?",
  "A granular breakdown of where time was spent: <b>Queueing</b> (browser queued the request), <b>Stalled</b> (waiting for a connection), <b>DNS Lookup</b>, <b>Initial Connection</b> (TCP handshake + TLS), <b>Request sent</b>, <b>Waiting (TTFB)</b> — time until first byte from server, <b>Content Download</b>. This pinpoints latency issues: slow DNS, slow TLS, slow server, slow network.",
  ["network", "L2"])

c("Network",
  "What is TTFB and why does it matter?",
  "<b>Time To First Byte</b> — the time from sending the HTTP request to receiving the first byte of the response. High TTFB means the server is slow to respond (database queries, server-side rendering, uncached computation). Low TTFB means CDN cache hit or fast server. Visible in the Network Timing tab as the 'Waiting' segment.",
  ["network", "L2"])

c("Network",
  "What are the key columns in the Network waterfall view?",
  "<b>Name</b> — resource path<br><b>Status</b> — HTTP status code<br><b>Type</b> — resource MIME type<br><b>Initiator</b> — what triggered the request (script, parser, CSS)<br><b>Size</b> — transferred size (compressed) / actual size (decompressed)<br><b>Time</b> — total request duration<br><b>Waterfall</b> — visual bar showing timing breakdown<br>Right-click headers to add more columns: Domain, Method, Connection ID, Protocol (h2, h3, http/1.1).",
  ["network", "L1"])

c("Network",
  "How do you sort network requests by size or duration?",
  "Click the <b>Size</b> or <b>Time</b> column header to sort ascending. Click again to reverse. Sort by <b>Time</b> descending to find your slowest requests. Sort by <b>Size</b> to find the largest payloads (images, JS bundles). Use the filter bar combined with sorting to drill down.",
  ["network", "L1"])

c("Network",
  "How do you inspect WebSocket frames in DevTools?",
  "In the Network panel, filter by <b>WS</b> (WebSocket) type. Click the WebSocket connection. The <b>Messages</b> tab shows every frame sent and received (green = sent, white = received) with timestamps. Data can be viewed as text, JSON, hex, or binary. The <b>Frames</b> tab is the older label for the same thing.",
  ["network", "L2"])

c("Network",
  "How do you inspect Server-Sent Events (SSE) in DevTools?",
  "In the Network panel, the SSE connection appears as type <code>eventsource</code>. Click it and go to the <b>EventStream</b> tab to see each <code>event:</code>, <code>data:</code>, and <code>id:</code> field as they are received in real time. Unlike WebSocket, SSE is unidirectional (server → client).",
  ["network", "L2"])

c("Network",
  "What are 'Network overrides' and how do they work?",
  "Network panel → <b>Overrides</b> tab (or Command Menu → 'Show Overrides'). Select a local folder to save resources to. When you edit a file in Sources, the override serves that local copy instead of the network resource — persisting across page reloads. Use for testing fixes without deploying, mocking API responses (stub JSON files), or hacking on production sites locally.",
  ["network", "L3"])

c("Network",
  "How do you export a HAR file from the Network panel?",
  "Right-click any request → <b>Save all as HAR with content</b>, or click the download arrow ⬇ in the Network toolbar. HAR (HTTP Archive) is a JSON format containing all request/response data. Share HAR files with backend engineers for debugging — they contain headers, timings, and response bodies.",
  ["network", "L2"])

c("Network",
  "What does the Initiator column in the Network panel show?",
  "What triggered the request. Shows:<br><b>Parser</b> — HTML parser found a <code>&lt;script&gt;</code>, <code>&lt;link&gt;</code>, <code>&lt;img&gt;</code><br><b>Script</b> — JavaScript XHR/fetch call with file:line link<br><b>Redirect</b> — HTTP redirect from another request<br><b>CSS</b> — CSS <code>url()</code> reference<br><b>Other</b> — user navigation, form submission<br>Click the initiator link to jump to the exact line of JS that made the fetch.",
  ["network", "L2"])

c("Network",
  "How do you replay an XHR/fetch request?",
  "Right-click the request → <b>Replay XHR</b>. Re-sends the identical request with the same method, headers, and body. Useful for testing idempotent API calls. To modify parameters, right-click → <b>Copy</b> → <b>Copy as fetch</b>, paste into Console, edit, and execute.",
  ["network", "L2"])

c("Network",
  "How do you copy a network request as a fetch/curl command?",
  "Right-click the request → <b>Copy</b> →<br><code>Copy as fetch</code>: <code>fetch(\"url\", {\"headers\":{...}})</code> — paste in Console.<br><code>Copy as cURL</code>: <code>curl 'url' -H 'header: value'</code> — paste in terminal.<br><code>Copy as Node.js fetch</code>: same for Node.<br><code>Copy as PowerShell</code>: for Windows users.<br>This is the fastest way to reproduce an API call from the browser to a test environment.",
  ["network", "L2"])

c("Network",
  "What is the difference between the Size column values 'x kB transferred' and 'x kB resource'?",
  "The top value is the <b>transferred size</b> (compressed, over-the-wire bytes). The bottom value is the <b>resource size</b> (decompressed, actual bytes parsed). For a 500 KB JS file served with gzip: '60 kB transferred / 500 kB resource'. A large gap indicates good compression. '0 kB transferred' with a size shown = served from cache. '(memory cache)' / '(disk cache)' = cached.",
  ["network", "L2"])

c("Network",
  "How do you filter out requests by domain or pattern?",
  "In the filter/search bar:<br><code>domain:api.example.com</code> — show only requests to that domain<br><code>domain:*.example.com</code> — wildcard domain filtering<br><code>-domain:google-analytics.com</code> — hide matching domain (leading minus)<br><code>method:POST</code> — filter by HTTP method<br><code>status-code:200</code> — filter by response code<br><code>status-code:>400</code> — all error responses<br><code>larger-than:100K</code> — responses over 100KB<br><code>mime-type:application/json</code> — filter by MIME type",
  ["network", "L2"])

c("Network",
  "What does the 'Connection ID' column (when enabled) tell you?",
  "Right-click the header row → check <b>Connection ID</b>. Each TCP/QUIC connection gets a numeric ID. Requests sharing the same ID are multiplexed over the same connection (HTTP/2, HTTP/3). Seeing many different IDs may indicate poor connection reuse. Useful for debugging HTTP/2 multiplexing and connection pooling.",
  ["network", "L3"])

c("Network",
  "What is the Protocol column and what values can it show?",
  "Right-click header → <b>Protocol</b>. Shows the HTTP version for each request:<br><code>h2</code> — HTTP/2 (multiplexed, binary)<br><code>h3</code> — HTTP/3 / QUIC (UDP-based)<br><code>http/1.1</code> — classic HTTP<br><code>data</code> — data: URI<br>Blank — request failed or protocol unknown. Use to verify your site is serving over HTTP/2+ for performance.",
  ["network", "L3"])

c("Network",
  "What are the three throttling profiles built into DevTools?",
  "<b>Slow 3G</b>: 400ms RTT, 400 Kbps down, 400 Kbps up<br><b>Fast 3G</b>: 150ms RTT, 1.6 Mbps down, 750 Kbps up<br><b>Slow 4G</b>: 70ms RTT, 4 Mbps down, 3 Mbps up<br>Add custom profiles in the throttling dropdown → <b>Add</b>. Network throttling simulates real-world mobile conditions for testing loading performance.",
  ["network", "L2"])

c("Network",
  "How do you simulate offline mode in DevTools?",
  "Network panel → throttling dropdown → select <b>Offline</b>. All network requests will fail immediately, as if the device has no network connection. Alternatively, Command Menu → 'Go offline'. This is essential for testing offline-first apps, service worker caching, and error state UIs.",
  ["network", "L2"])

c("Network",
  "How do you view the response headers that triggered a cache hit/miss?",
  "In the Headers tab of a request, check the <b>Response Headers</b> section for caching directives: <code>cache-control: max-age=...</code>, <code>etag: \"...\"</code>, <code>last-modified: ...</code>, <code>expires: ...</code>, <code>age: ...</code>, <code>x-cache: HIT/MISS</code> (CDN). The 'Size' column shows '(disk cache)' or '(memory cache)' for cache hits.",
  ["network", "L2"])

c("Network",
  "What is the Network conditions tab and what can you override?",
  "Opened via the Network panel panel menu or Command Menu → 'Show Network conditions'. Override: <b>Network throttling</b>, <b>User agent</b> (spoof browser/device), and <b>Accepted Content-Encodings</b> (e.g., disable gzip to test raw transfer sizes). Useful for testing without changing actual network or browser settings.",
  ["network", "L2"])

c("Network",
  "What is the Dependency/Waterfall view and how do you read it?",
  "The waterfall shows each request as a colored bar on a timeline. The bars are staggered — a request that starts after another's bar begins is a <b>dependent request</b> (e.g., CSS loaded, then fonts inside CSS). Right-click → <b>Reveal in Elements panel</b> to find the DOM node that triggered it. Hover a bar to see timing breakdown.",
  ["network", "L2"])

# ============================================================
# 05 — SOURCES & DEBUGGING (L2 Composition + L3 Design + L4 Diagnosis)
# ============================================================

c("SourcesDebugging",
  "What are the key panes in the Sources panel?",
  "<b>Left</b>: File Navigator — page sources, filesystem (Workspaces), overrides, content scripts, and snippets.<br><b>Center</b>: Code Editor — view and edit source files with syntax highlighting.<br><b>Right</b>: Debugger sidebar — Threads, Call Stack, Breakpoints, Scope, Watch, XHR/fetch breakpoints, DOM breakpoints, Event Listener breakpoints, CSP Violation breakpoints.",
  ["sources", "L1"])

c("SourcesDebugging",
  "How do you set a line-of-code breakpoint?",
  "Click the line number gutter (left margin) in the Sources editor. A blue marker appears. Alternatively, right-click a line → <b>Add breakpoint</b>. Execution pauses before that line executes. The breakpoint list in the right sidebar lets you enable/disable/remove breakpoints.",
  ["sources", "L2"])

c("SourcesDebugging",
  "What is a conditional breakpoint?",
  "Right-click a line → <b>Add conditional breakpoint</b> → enter a JavaScript expression. The breakpoint only pauses when the expression is <b>truthy</b>. Example: <code>user.id === 1234</code> pauses only for that user. The condition runs every time the line is hit — keep it cheap (O(1), no side effects).",
  ["sources", "L2"])

c("SourcesDebugging",
  "What is a Logpoint?",
  "Right-click a line → <b>Add logpoint</b> → enter a message using <code>$var</code> or <code>{var}</code> placeholders. Instead of pausing, it <b>logs</b> the message to the Console every time the line executes. Essentially a non-blocking <code>console.log</code> injected without modifying source code. Format: <code>'User {user.id} clicked at', $timestamp</code>.",
  ["sources", "L2"])

c("SourcesDebugging",
  "What are the step-over, step-into, and step-out controls?",
  "<code>F9</code> / <code>Ctrl+\\</code> — <b>Resume</b> (continue execution)<br><code>F10</code> / <code>Ctrl+'</code> — <b>Step over</b> (execute current line, don't enter functions)<br><code>F11</code> / <code>Ctrl+;</code> — <b>Step into</b> (enter function call on current line)<br><code>Shift+F11</code> / <code>Ctrl+Shift+;</code> — <b>Step out</b> (finish current function, return to caller)<br><code>F8</code> — <b>Step</b> (like step-over but for async). Use step-over for your code, step-into for library code you need to understand.",
  ["sources", "L2", "keybinding"])

c("SourcesDebugging",
  "How do you use Watch expressions?",
  "In the <b>Watch</b> pane (right sidebar of Sources), click <code>+</code> and enter any JavaScript expression. The expression evaluates in the current stack frame's scope and updates live as you step through code. Watch complex property paths: <code>this.props.user.preferences.theme</code>. Watch conditions: <code>items.filter(i => i.price > 100)</code>.",
  ["sources", "L2"])

c("SourcesDebugging",
  "What is the Call Stack pane and what does it show?",
  "Shows the chain of function calls that led to the current execution point. The top frame is the current function; the bottom is the entry point. Click any frame to jump to that location and inspect its local variables. Async call stacks (enabled in Settings) show the full async chain crossing await/Promise boundaries.",
  ["sources", "L2"])

c("SourcesDebugging",
  "What is the Scope pane and what variables does it show?",
  "Shows all in-scope variables at the current execution point: <b>Local</b> (function-scoped), <b>Closure</b> (captured variables from outer functions), <b>Module</b> (ES module scope), and <b>Global</b> (window/globalThis). Double-click a value to edit it live — change variable values while debugging without restarting.",
  ["sources", "L2"])

c("SourcesDebugging",
  "How do you blackbox a script?",
  "Right-click a source file in the File Navigator → <b>Blackbox script</b>, or right-click in the Call Stack → <b>Blackbox script</b>. Blackboxed scripts are hidden from the Call Stack and are skipped when stepping through code. Essential for hiding framework internals (React, Vue, Angular, lodash) and only debugging your application code.",
  ["sources", "L3"])

c("SourcesDebugging",
  "What are XHR/fetch breakpoints?",
  "In the <b>XHR/fetch Breakpoints</b> pane (right sidebar), click <code>+</code> and enter a URL substring. Execution pauses whenever a fetch/XHR request is made to a URL containing that string. Example: break on <code>/api/user</code> to catch all user API calls. Use <code>*</code> to break on every XHR request (noisy but comprehensive).",
  ["sources", "L3"])

c("SourcesDebugging",
  "What are Event Listener breakpoints?",
  "In the Event Listener Breakpoints pane, expand event categories (Mouse, Keyboard, Touch, Timer, etc.) and check specific events. Execution pauses when that event listener fires — <b>before</b> the handler runs. Use <b>Ctrl+F</b> in the pane to search for events by name. Categories include: Animation, Canvas, Clipboard, Control, Device, Drag/Drop, Keyboard, Load, Mouse, Notification, Parse, Pointer, Promise, Timer, Touch, WebAudio, Window, Worker. Essential for finding the JS that handles a click/keypress without manually searching the codebase.",
  ["sources", "L3"])

c("SourcesDebugging",
  "What are CSP Violation breakpoints?",
  "Enabled via the CSP Violation Breakpoints pane. Pauses execution whenever a <b>Content Security Policy</b> violation occurs. Useful for debugging CSP issues (blocked scripts, styles, images). Shows the violated directive and the resource that triggered the violation.",
  ["sources", "L3"])

c("SourcesDebugging",
  "How do you use Workspaces to edit files and persist changes to disk?",
  "Sources panel → <b>Filesystem</b> tab → <b>Add folder to workspace</b>. Chrome prompts for write permissions. Once granted, editing a file in Sources edits the local file on disk. Changes are saved immediately. Green = workspace file (synced), Red = unsaved changes. CSS changes in Elements auto-map to workspace files. This enables full in-browser IDE-like editing.",
  ["sources", "L2"])

c("SourcesDebugging",
  "What are Snippets and how do you create one?",
  "Sources panel → <b>Snippets</b> tab in the left sidebar → <b>New snippet</b>. Write any JavaScript and run with <code>Ctrl+Enter</code> / <code>Cmd+Enter</code>. Snippets persist across sessions (stored in DevTools local storage). Access via Command Menu: type the snippet name to run it. Use for debugging utilities, test fixtures, DOM manipulation scripts, or bookmarklets.",
  ["sources", "L2"])

c("SourcesDebugging",
  "What are common useful Snippets?",
  "1. <b>Enable design mode</b>: <code>document.designMode = 'on'</code> — make any page editable.<br>2. <b>Log all event listeners</b>: <code>getEventListeners(window)</code>.<br>3. <b>Remove all cookies</b>: loop and delete.<br>4. <b>Extract all links</b>: <code>copy($$('a').map(a => a.href).join('\\n'))</code>.<br>5. <b>Debug React Fiber</b>: <code>document.querySelector('#root')._reactRootContainer</code>.<br>6. <b>Toggle CSS outlines</b>: <code>$$('*').forEach(el => el.style.outline = el.style.outline ? '' : '1px solid red')</code>.",
  ["sources", "L2"])

c("SourcesDebugging",
  "What is 'Pretty print' and how do you use it?",
  "Click the <code>{ }</code> icon at the bottom of the Sources editor (or right-click → <b>Format</b>) to prettify a minified JS/CSS file. Appends <code>:formatted</code> to the filename. Breakpoints set in the formatted file map back to the minified source. Essential for debugging production bundles.",
  ["sources", "L2"])

c("SourcesDebugging",
  "How do you search within a source file?",
  "<code>Ctrl+F</code> / <code>Cmd+F</code> — search within the current file. <code>Ctrl+Shift+F</code> / <code>Cmd+Opt+F</code> — search across <b>all</b> loaded source files. The global search supports regex (check the <code>.*</code> toggle) and case sensitivity. Results are grouped by file with clickable line numbers.",
  ["sources", "L1", "keybinding"])

c("SourcesDebugging",
  "How do you navigate to a specific function or CSS rule within a file?",
  "<code>Ctrl+Shift+O</code> / <code>Cmd+Shift+O</code> in the Sources editor opens the <b>function/selector picker</b> — a fuzzy-search outline of all functions, classes, and CSS rules in the current file. Type to filter and press Enter to jump.",
  ["sources", "L1", "keybinding"])

c("SourcesDebugging",
  "What does the 'Pause on exceptions' button do?",
  "The octagonal stop-sign button in the Sources panel (top-right of the debugger sidebar) toggles <b>Pause on caught exceptions</b> and <b>Pause on uncaught exceptions</b>. When enabled, Chrome will break on the exact line that throws the exception — even if it's inside a try/catch. Essential for debugging swallowed errors.",
  ["sources", "L3"])

c("SourcesDebugging",
  "How do you debug async/await code across await boundaries?",
  "Enable <b>Async</b> call stacks in Settings → Sources → 'Use async call stacks'. This shows the full call chain across <code>await</code> boundaries in the Call Stack pane. Without this, stepping over an <code>await</code> loses the caller context. Experimental: 'Respect 'pause' statements in async functions'.",
  ["sources", "L3"])

c("SourcesDebugging",
  "How do you use conditional breakpoints for debugging specific data conditions?",
  "Right-click a line → Add conditional breakpoint → expression like:<br><code>data.items.length > 100</code> — break only on large datasets<br><code>user.role === 'admin'</code> — break for admin users<br><code>n > 5 && console.table(items), n > 5</code> — log table when condition met (comma operator: log + condition)<br><code>event.key === 'Escape'</code> — break on Escape key<br>Use <code>console.trace()</code> inside conditions for non-breaking stack traces.",
  ["sources", "L3"])

c("SourcesDebugging",
  "What are Source Maps and how do they work in DevTools?",
  "Source maps (<code>.map</code> files) map minified/compiled code back to original source code. They enable debugging TypeScript, JSX, SCSS, and minified JS in DevTools as if you're debugging the original source. Must be enabled in Settings → Sources → 'Enable JavaScript source maps'. The <code>sourceMappingURL</code> comment at the end of the compiled file points to the map.",
  ["sources", "L3"])

c("SourcesDebugging",
  "How do you debug source map issues?",
  "If sources don't map correctly: 1) Check Settings → Sources → 'Enable JavaScript source maps' is on. 2) Look for the <code>sourceMappingURL</code> at the bottom of the compiled file. 3) Open the <b>Developer Resources</b> tab (bottom of Sources left panel) — it shows source map load errors. 4) Verify the <code>sources</code> array in the <code>.map</code> file lists the correct source files. 5) Check the Network panel to ensure the .map file is being loaded (200 OK).",
  ["sources", "L4"])

c("SourcesDebugging",
  "What are Overrides and when should you use them over Workspaces?",
  "<b>Overrides</b>: Override any network resource with a local copy. Simpler — just pick a folder, and DevTools automatically intercepts matching requests. Best for quick production debugging or mocking API responses.<br><b>Workspaces</b>: Maps local files to network resources bidirectionally. Changes save to disk, and disk changes reload in DevTools. Best for active development where you want the changes to persist to your project files. Overrides create copies; Workspaces edit the real files.",
  ["sources", "L3"])

c("SourcesDebugging",
  "How do you set a breakpoint on a DOM node's subtree/attribute modifications?",
  "Right-click element in Elements panel → <b>Break on</b> → <b>Subtree modifications</b>, <b>Attribute modifications</b>, or <b>Node removal</b>. These <b>DOM breakpoints</b> appear in the Sources panel's DOM Breakpoints pane. When triggered, the debugger pauses on the line of JavaScript that caused the modification. A powerful tool for answering 'what JavaScript is changing my DOM?'",
  ["sources", "L3"])

c("SourcesDebugging",
  "What is the 'Threads' pane and when do you need it?",
  "The Threads pane at the top of the debugger sidebar shows all active JavaScript execution contexts: the main thread, Web Workers, Service Workers, and Worklets. Click any thread to switch debugging context. When a Worker hits a breakpoint, its thread highlights — click it to inspect that Worker's scope, call stack, and variables.",
  ["sources", "L3"])

c("SourcesDebugging",
  "How do you debug a Web Worker?",
  "Open Sources → Threads pane → the Worker script appears as a separate thread. Set breakpoints directly in the Worker's source file. You can debug Workers with the same breakpoints, watch expressions, and step controls as the main thread. Use <code>console.log</code> in the Worker and it appears in the Console with a <code>[Worker]</code> prefix.",
  ["sources", "L4"])

c("SourcesDebugging",
  "What is 'Break on debugger statements' and when is it useful?",
  "When a <code>debugger;</code> statement executes, DevTools pauses by default. Settings → Sources → you can disable <b>'Pause on debugger statement'</b>. Useful when a third-party script has <code>debugger;</code> statements that interrupt your workflow (looking at you, analytics scripts). Also: right-click the line gutter → 'Never pause here' to ignore specific lines.",
  ["sources", "L3"])

# ============================================================
# 06 — PERFORMANCE (L3 Design + L4 Diagnosis + L5 Opinion)
# ============================================================

c("Performance",
  "What does the Performance panel do?",
  "Records a timeline of everything happening in the page: JavaScript execution, style recalculation, layout, paint, compositing, network requests, frames per second, and Core Web Vitals. It's a runtime profiler — you hit Record, interact with the page, stop recording, and analyze the flame chart.",
  ["performance", "L3"])

c("Performance",
  "What keyboard shortcut starts/stops a Performance recording?",
  "<code>Ctrl+E</code> / <code>Cmd+E</code> — starts and stops a Performance recording when the Performance panel is open.",
  ["performance", "L3", "keybinding"])

c("Performance",
  "What is the difference between the Performance panel and the Performance Insights panel?",
  "<b>Performance panel</b>: Detailed timeline, flame chart, raw event data. Full control — best for deep analysis by experienced devs. Shows everything (network, frames, interactions, main thread, GPU, raster).<br><b>Performance Insights</b> (newer): Highlights only important insights (long tasks, layout shifts, INP interactions). Less data, more actionable. Better for quick triage and non-specialists. Shows 'what to fix' rather than 'here's every event'.",
  ["performance", "L4"])

c("Performance",
  "What is a flame chart and how do you read it?",
  "The flame chart visualizes the call stack over time in the Main thread track. Each bar represents a function call. <b>Width</b> = duration. <b>Stack depth</b> = call hierarchy (caller above, callee below). <b>Color</b> = type: yellow (scripting), purple (rendering), green (painting). Click to zoom into a function; double-click to zoom to its full duration. The top-down and bottom-up tabs present the same data differently.",
  ["performance", "L4"])

c("Performance",
  "What are the three Core Web Vitals and what are their thresholds?",
  "<b>LCP (Largest Contentful Paint)</b>: Loading performance. Good ≤ 2.5s, needs improvement ≤ 4s, poor > 4s.<br><b>INP (Interaction to Next Paint)</b>: Responsiveness (replaced FID in March 2024). Good ≤ 200ms, needs improvement ≤ 500ms, poor > 500ms.<br><b>CLS (Cumulative Layout Shift)</b>: Visual stability. Good ≤ 0.1, needs improvement ≤ 0.25, poor > 0.25.<br>All three are visible in the Performance panel's 'Web Vitals' lane or the 'Timings' track.",
  ["performance", "L4"])

c("Performance",
  "What is the difference between LCP and FCP?",
  "<b>FCP (First Contentful Paint)</b>: Time until the first text/image/painted content appears. The initial visual feedback to the user.<br><b>LCP (Largest Contentful Paint)</b>: Time until the largest content element (hero image, heading, video) is rendered — when the page's primary content is visible. LCP is a better indicator of perceived load completion. LCP ≥ FCP always (LCP is later or equal).",
  ["performance", "L4"])

c("Performance",
  "What does INP measure and how is it different from FID?",
  "<b>FID (First Input Delay)</b>: Only measured the <b>first</b> interaction's input delay (time from user click to event handler start).<br><b>INP (Interaction to Next Paint)</b>: Measures the <b>worst</b> interaction's full latency (input delay + processing time + presentation delay) across the entire page lifecycle. A more comprehensive responsiveness metric. INP is measured when the user leaves the page.",
  ["performance", "L4"])

c("Performance",
  "What are Long Tasks and how do you identify them?",
  "A <b>Long Task</b> is any task that blocks the main thread for ≥ 50ms. They appear as red triangles in the top-left corner of the Main thread track (or a red 'Long Tasks' lane in newer layouts). Click a long task to see the functions responsible. Long tasks kill responsiveness — they delay INP and cause jank. The Total Blocking Time (TBT) metric sums all long task time beyond 50ms.",
  ["performance", "L4"])

c("Performance",
  "What are the key colors to understand in the flame chart?",
  "<b>Yellow</b> — JavaScript execution (scripting, event handlers, timers)<br><b>Purple</b> — Recalculate Style & Layout (style recalc + layout/paint)<br><b>Green</b> — Paint & Composite (rasterization, layer compositing)<br><b>Gray</b> — System & Idle (garbage collection, parsing, etc.)<br><b>Blue</b> — Parse HTML & CSS<br>If you see lots of purple/green during interactions, your JS is triggering forced synchronous layouts — a performance anti-pattern.",
  ["performance", "L4"])

c("Performance",
  "What is 'forced synchronous layout' (layout thrashing) and how does it appear in DevTools?",
  "Forced sync layout occurs when you <b>write</b> a style property, then immediately <b>read</b> a layout property (like <code>offsetHeight</code>) without batching. The browser must synchronously recalculate layout before returning the read. In the flame chart: alternating purple (layout) bars tightly interleaved with yellow (scripting) — each read forces a re-layout. Fix: batch reads first, then writes (FastDOM pattern).",
  ["performance", "L4"])

c("Performance",
  "What is the FPS meter and how do you enable it?",
  "Rendering panel → check <b>FPS Meter</b>. Shows a real-time frames-per-second counter in the top-left of the viewport. A line at 60 FPS = smooth. Drops below 60 = jank. The histogram shows frame distribution. Use while interacting with the page to spot janky interactions. Or Command Menu → 'Show FPS Meter'.",
  ["performance", "L3"])

c("Performance",
  "What does Paint Flashing show?",
  "Rendering panel → check <b>Paint flashing</b>. Every time the browser repaints a region of the screen, that region flashes <b>green</b>. Use to find unnecessary repaints — CSS animations on <code>top</code>/<code>left</code> (which repaint every frame) vs <code>transform</code> (which only composites). If the whole screen flashes green continuously, you have a paint storm.",
  ["performance", "L4"])

c("Performance",
  "What are Layer Borders and how do they help?",
  "Rendering panel → <b>Layer borders</b>. Shows orange borders around composited layers and blue grid tiles. Every orange-bordered region is a GPU texture. Too many layers = excessive GPU memory. Large layers = slower compositing. Use to see what's being promoted to its own layer (e.g., via <code>will-change</code>, <code>transform: translateZ(0)</code>).",
  ["performance", "L4"])

c("Performance",
  "What is the Layers panel and what does it show?",
  "Command Menu → 'Show Layers'. Shows a 3D exploded view of every composited layer on the page. Rotate, zoom, and pan to see layer stacking. Click a layer to see: dimensions, memory usage, compositing reasons (why it was promoted), and a paint count. Essential for debugging <code>will-change</code> overuse and GPU memory issues.",
  ["performance", "L4"])

c("Performance",
  "How do you record and analyze user interactions with the Performance panel?",
  "Set up: Performance panel → record settings (gear) → enable <b>'Enable advanced paint instrumentation'</b> and <b>'Screenshots'</b>. Record a short interaction (click, scroll, type). Stop. The <b>Interactions</b> track shows each interaction with a label. Click an interaction to zoom to it. The flame chart shows exactly what executed during that click. Use this to find the JavaScript causing a 500ms INP.",
  ["performance", "L4"])

c("Performance",
  "What does the Summary tab show when you select a range in the Performance panel?",
  "A pie chart breakdown of the selected time range: <b>Scripting</b> (%), <b>Rendering</b> (%), <b>Painting</b> (%). The bottom-up table shows individual function calls sorted by total/self time. The call tree view shows the nested call hierarchy. Use to identify the single function responsible for most of the time in a janky interaction.",
  ["performance", "L4"])

c("Performance",
  "How do you force garbage collection in the Performance panel?",
  "Click the trash can icon 🗑 in the Performance panel (or Console panel, or Memory panel). This triggers a synchronous Garbage Collection cycle. Useful before recording to start with a clean memory baseline. Note: GC is non-deterministic — forced GC doesn't guarantee all objects are collected.",
  ["performance", "L4"])

c("Performance",
  "What is the Coverage panel and what does it tell you?",
  "Command Menu → 'Show Coverage' → click the Record button (reload or interact). Shows per-file percentages of <b>unused bytes</b> (red bar) vs <b>used bytes</b> (blue bar). JavaScript and CSS files often ship 70-80% unused code. Use coverage data to inform code splitting and dead-code elimination. The source tree shows individual lines highlighted green (used) and red (unused).",
  ["performance", "L4"])

c("Performance",
  "How do you emulate a slow CPU for performance testing?",
  "Performance panel → Capture Settings (gear icon) → <b>CPU throttling</b>:<br><b>4x slowdown</b> — simulates a mid-range mobile device<br><b>6x slowdown</b> — simulates a low-end device<br>Or add a custom multiplier. This artificially slows JavaScript execution to make performance issues easier to spot and reproduce. The frame budget shrinks proportionally (60 FPS → 10-15 FPS at 4x). Always test on real devices too.",
  ["performance", "L4"])

c("Performance",
  "What is the difference between the Performance panel and the Lighthouse audit?",
  "<b>Performance panel</b>: You manually record, analyze raw data, and diagnose specific code paths. Deep, interactive, requires expertise.<br><b>Lighthouse</b>: Automated audit that simulates a mid-tier mobile device on Slow 4G. Gives a 0-100 score, identifies opportunities (render-blocking resources, oversized images, unused CSS), and provides specific suggestions. Best for: getting a baseline score, tracking regressions in CI, and getting actionable recommendations without deep profiling knowledge.",
  ["performance", "L5"])

c("Performance",
  "What is  <code>requestAnimationFrame</code> and how can you debug its callbacks?",
  "<code>requestAnimationFrame(callback)</code> schedules a callback to run before the next frame. In the Performance panel's flame chart, rAF callbacks appear as yellow bars in the Main thread track labeled 'Animation Frame Fired'. Look for rAF callbacks that take >10ms — they risk missing the frame deadline. Use the Animation lane to see frame timing.",
  ["performance", "L4"])

c("Performance",
  "What is <code>requestIdleCallback</code> and when should you use it based on Performance analysis?",
  "<code>requestIdleCallback(cb, {timeout})</code> schedules work during browser idle periods (when no frames need to be painted). In the Performance flame chart, idle callbacks appear as yellow bars labeled 'Run Microtasks' or 'Fire Idle Callback'. Use for non-critical work: analytics, prefetching, cleanup. If idle callbacks are running during frame time (not actually idle), you're over-scheduling work.",
  ["performance", "L5"])

c("Performance",
  "How do you get a Performance trace from a production user?",
  "The Performance panel works on any website. Navigate to the production URL, open DevTools, record interactions. For user-reported jank: have the user take a Performance recording (they record → reproduce the issue → stop → export as JSON via the download button). Or use the <code>PerformanceObserver</code> API to collect RUM (Real User Monitoring) data: <code>new PerformanceObserver(list => {...}).observe({entryTypes: ['longtask', 'largest-contentful-paint', 'layout-shift']})</code>.",
  ["performance", "L5"])

c("Performance",
  "What is the 'Renderer' section in the Performance panel summary?",
  "When you select a paint event in the flame chart, the summary shows <b>Renderer</b>: which compositing layers were used, the paint commands executed, and the draw calls. This is advanced GPU-level debugging. Useful when paint is the bottleneck (green dominates the flame chart) — you can see exactly what's being rasterized.",
  ["performance", "L6"])

c("Performance",
  "What does the 'Experiments' section under Settings offer for Performance?",
  "Settings → Experiments → search for performance experiments like:<br><b>Timeline: event initiators</b> — shows what triggered each event<br><b>Timeline: show all events</b> — even micro-tasks<br><b>Override default line-level CPU profile</b> — more granular flame chart<br><b>Web Vitals overlay</b> — shows LCP, INP, CLS on the page in real-time<br><b>Performance Insights</b> panel — newer simplified perf panel<br>Enable cautiously; experiments may cause instability.",
  ["performance", "L6"])

# ============================================================
# 07 — MEMORY & APPLICATION (L3 Design + L4 Diagnosis)
# ============================================================

c("MemoryApplication",
  "What are the three memory profiler types in the Memory panel?",
  "<b>Heap Snapshot</b> — point-in-time snapshot of all JS objects in the heap. Shows object count, size, retaining paths.<br><b>Allocation instrumentation on timeline</b> — records heap allocations over time with call stacks. Identifies which functions allocate the most objects.<br><b>Allocation sampling</b> — lightweight statistical sampling of allocations (like CPU profiling for memory). Lower overhead than instrumentation, good for finding allocation hotspots in long-running apps.",
  ["memory", "L4"])

c("MemoryApplication",
  "How do you take and analyze a Heap Snapshot?",
  "Memory panel → Heap snapshot → <b>Take snapshot</b>. After it loads:<br>1. <b>Summary view</b>: Objects grouped by constructor. Sort by 'Shallow Size' or 'Retained Size'.<br>2. <b>Comparison view</b>: Take two snapshots, compare to find objects added between them.<br>3. <b>Containment view</b>: Objects grouped by their GC root — see the hierarchy of references.<br>4. Use the <b>Retainers</b> pane (click an object) to see what's holding a reference to it — the key to finding leaks.",
  ["memory", "L4"])

c("MemoryApplication",
  "What is the difference between Shallow Size and Retained Size in a heap snapshot?",
  "<b>Shallow Size</b>: The memory directly held by the object itself (its own properties). Small for most objects (strings are the exception).<br><b>Retained Size</b>: The total memory that would be freed if this object were deleted — including all objects it exclusively references. This is the real 'leak cost'. A closure retaining a large array has small shallow size but huge retained size. Sort by retained size to find leak candidates.",
  ["memory", "L4"])

c("MemoryApplication",
  "What are the three snapshot views (Summary, Comparison, Containment) and when do you use each?",
  "<b>Summary</b>: Constructors grouped by type. Start here — check for unexpected object counts (e.g., 5000 detached DOM nodes, 1000 closures).<br><b>Comparison</b>: Diff two snapshots. Used for leak hunting: take snapshot A, perform action, take snapshot B, compare — objects that increased are suspects.<br><b>Containment</b>: GC root hierarchy (window → document → ...). Use when you know a specific object exists and you need to find its retaining path back to a root.",
  ["memory", "L4"])

c("MemoryApplication",
  "What are 'Detached DOM nodes' and how do you find them in a heap snapshot?",
  "Filter the snapshot summary by 'Detached' — these are DOM nodes removed from the document tree but still referenced by JavaScript (e.g., stored in a variable, closure, or event handler). They're a memory leak because they can't be garbage collected. The filter shows <code>Detached HTMLDivElement</code>, etc. Check their <b>Retainers</b> to find the JavaScript holding the reference.",
  ["memory", "L4"])

c("MemoryApplication",
  "How do you use the Allocation timeline to find memory leaks?",
  "Memory panel → <b>Allocation instrumentation on timeline</b> → <b>Start</b> recording. Interact with the page. <b>Stop</b>. The timeline shows:<br>- <b>Blue bars</b>: memory allocated (not yet freed)<br>- <b>Gray bars</b>: memory allocated and since freed<br>Growing blue bars over repeated interactions = leak. Click a bar to see the call stack of allocations at that point. The constructor list shows which types of objects are being allocated most.",
  ["memory", "L4"])

c("MemoryApplication",
  "What is the 'Allocation sampling' profiler?",
  "A lightweight alternative to allocation instrumentation. It samples allocations at a fixed rate (instead of recording every allocation). Lower overhead — suitable for long-running profiling sessions. Use when the full instrumentation timeline causes too much slowdown. It shows a flame chart of allocation call stacks, weighted by allocated bytes.",
  ["memory", "L4"])

c("MemoryApplication",
  "What is the Performance Monitor and what does it show?",
  "Command Menu → 'Show Performance Monitor'. A real-time dashboard showing: <b>CPU usage</b> (%), <b>JS heap size</b> (MB), <b>DOM Nodes</b> (count), <b>JS event listeners</b> (count), <b>Documents</b> (count), <b>Document Frames</b> (count), <b>Layouts/sec</b>, and <b>Style recalcs/sec</b>. A rising JS heap size line that never drops = likely memory leak. Rising DOM node count when it should be stable = leaking nodes.",
  ["memory", "L4"])

c("MemoryApplication",
  "What storage types can you inspect and manage in the Application panel?",
  "<b>Local Storage</b> — per-origin key-value strings (5-10 MB limit)<br><b>Session Storage</b> — per-tab key-value (cleared on tab close)<br><b>IndexedDB</b> — structured data, async API, unlimited (with permission)<br><b>Cookies</b> — per-domain, sent with every request, small (4 KB each)<br><b>Cache Storage</b> — Service Worker Cache API entries<br><b>Web SQL</b> — deprecated but still inspectable<br><b>Trust Tokens</b>, <b>Interest Groups</b>, <b>Shared Storage</b>, <b>Bounce Tracking Mitigations</b> — newer privacy/ads APIs",
  ["application", "L3"])

c("MemoryApplication",
  "How do you view and edit localStorage/sessionStorage in DevTools?",
  "Application panel → <b>Storage</b> → <b>Local Storage</b> or <b>Session Storage</b> → select origin. Shows a table of key-value pairs. <b>Double-click</b> to edit values. Right-click → <b>Delete</b> to remove. The <b>Clear All</b> button (⌀) removes all entries for that origin. Console shortcut: <code>localStorage</code> / <code>sessionStorage</code> to interact programmatically.",
  ["application", "L3"])

c("MemoryApplication",
  "How do you inspect and delete cookies in DevTools?",
  "Application panel → <b>Storage</b> → <b>Cookies</b> → select domain. Shows: Name, Value, Domain, Path, Expires, Size, HttpOnly, Secure, SameSite, SameParty, Priority. Double-click to edit. Right-click → <b>Delete</b>. Use <b>Clear All</b> to wipe all cookies for the domain. Also accessible in the Console via <code>document.cookie</code> (but HttpOnly cookies won't show there).",
  ["application", "L3"])

c("MemoryApplication",
  "What is the Application panel's 'Background Services' section?",
  "Shows events from background fetch, background sync, notifications, payment handler, periodic background sync, push messaging, and speculative loading. Each section shows a timeline of events recording when they were triggered. Click 'Record' to start logging events. Useful for debugging Service Worker background sync flows and push notification delivery.",
  ["application", "L3"])

c("MemoryApplication",
  "How do you inspect IndexedDB databases?",
  "Application panel → <b>Storage</b> → <b>IndexedDB</b> → expand database → expand object store. Shows stored records in a paginated table. You can: view/edit values (double-click), delete entries, refresh to see live data, and view the IndexedDB schema (object store names, key paths, indexes). Console access: <code>indexedDB.open('dbName')</code> for programmatic inspection.",
  ["application", "L3"])

c("MemoryApplication",
  "How do you inspect and debug Service Workers?",
  "Application panel → <b>Service Workers</b>. Shows: the current service worker's status (activated, installing, waiting), source URL, last update time. Actions: <b>Update</b> (force re-fetch from server), <b>Unregister</b>, <b>Stop</b> (terminate the worker), <b>Inspect</b> (opens the SW's own DevTools window — separate from the page), <b>Bypass for network</b> (skip the SW for requests). Check 'Update on reload' to force SW refresh on page reload (crucial for development, or SW changes won't be reflected).",
  ["application", "L4"])

c("MemoryApplication",
  "How do you inspect Cache Storage (Service Worker caches)?",
  "Application panel → <b>Cache Storage</b> → expand cache name. Shows all cached Request/Response pairs with URLs, sizes, and response headers. Click an entry to view the response body (Preview tab). Use to verify your SW is caching the right assets. Delete individual entries or clear the entire cache. The <b>Cache</b> section also shows quota usage.",
  ["application", "L3"])

c("MemoryApplication",
  "What is the Application panel's 'Frame' section and how do you use it?",
  "Application panel → <b>Frames</b> → expand the top frame (main page) and any nested iframes. Shows per-frame resource tree: all scripts, stylesheets, images, fonts loaded by that frame. Click any resource to see its content. Useful for: inspecting what scripts an iframe loaded, finding dynamically injected resources, and understanding multi-frame applications.",
  ["application", "L3"])

c("MemoryApplication",
  "How do you clear all site data from DevTools?",
  "Application panel → <b>Storage</b> → <b>Clear site data</b> button in the top section. This clears: Local Storage, Session Storage, IndexedDB, Web SQL, Cookies, Cache Storage, Service Workers, and more for the current origin. Equivalent to Chrome settings → 'Clear browsing data' but scoped to the current site. Useful for resetting state during development.",
  ["application", "L3"])

c("MemoryApplication",
  "What is the 'Manifest' pane in the Application panel?",
  "Shows the parsed <code>manifest.json</code> for the web app (PWA). Displays: app name, short name, start URL, icons (with sizes), display mode, theme color, background color, and scope. The <b>Identity</b> section shows icons. The <b>Presentation</b> section shows display-related settings. Use to verify your PWA manifest is valid and all icon sizes are provided.",
  ["application", "L3"])

c("MemoryApplication",
  "How do you simulate different storage quota behaviors?",
  "In the Application panel → <b>Storage</b>, the top section shows quota usage for the current origin. Click the <b>Simulate custom storage quota</b> checkbox and enter a limit (in MB) to test how your app behaves under storage pressure — IndexedDB writes will fail, Cache Storage may evict entries. Essential for offline-first app testing.",
  ["application", "L4"])

# ============================================================
# 08 — SECURITY & SENSORS (L2 Composition + L3 Design + L4 Diagnosis)
# ============================================================

c("SecuritySensors",
  "What does the Security panel show?",
  "Displays the security state of the current page: a summary card showing whether the connection is <b>secure</b> (valid HTTPS), <b>neutral</b> (HTTP), or <b>insecure</b> (broken HTTPS, mixed content). Shows: certificate details (issuer, validity dates, subject, fingerprint, transparency), TLS version and cipher suite, mixed content status (passive/active), and subresource security origins.",
  ["security", "L3"])

c("SecuritySensors",
  "How do you view the TLS certificate details in DevTools?",
  "Security panel → click <b>View certificate</b>. Shows: Issued to (CN, O, OU), Issued by (CA), Validity period, Fingerprints (SHA-1, SHA-256), Subject Public Key Info (algorithm, key size), Subject Alternative Names, Extensions (basic constraints, key usage, CRL, CT, etc.). Also accessible by clicking the lock icon in the URL bar → Certificate is valid → Details.",
  ["security", "L3"])

c("SecuritySensors",
  "What is Mixed Content and how does DevTools flag it?",
  "<b>Mixed Content</b>: An HTTPS page loads resources over HTTP. Two types:<br><b>Passive (display)</b>: Images, audio, video — visible in Security panel as a warning. The page shows 'Not secure' with the info ⓘ icon.<br><b>Active (script)</b>: Scripts, stylesheets, iframes — <b>blocked by default</b>. The Security panel shows these as errors. The Console logs detailed mixed content warnings with the exact resource URL. Fix: upgrade HTTP resources to HTTPS, or use <code>upgrade-insecure-requests</code> CSP directive.",
  ["security", "L3"])

c("SecuritySensors",
  "What is the Security panel's origin list at the bottom?",
  "Shows every origin that the page loads resources from (scripts, styles, images, iframes, etc.), grouped by security type: <b>Secure</b> (green, HTTPS), <b>Neutral</b> (yellow, HTTP/data/blob), and <b>Unknown/Canceled</b>. Click any origin to see detailed info. Use to find which third-party scripts are served over HTTP (mixed content).",
  ["security", "L3"])

c("SecuritySensors",
  "How do you inspect Content Security Policy (CSP) violations?",
  "Security panel → <b>...</b> menu → <b>Show console</b> (or look in the Console). Regex filter: <code>/violates the following Content Security Policy/</code>. CSP violations show: the blocked resource URL, the directive that blocked it, and the source file. For deeper debugging: Sources panel → CSP Violation Breakpoints — pauses execution on violations, showing the exact script that triggered the violation in the call stack.",
  ["security", "L3"])

c("SecuritySensors",
  "What sensors can you emulate in the Sensors panel?",
  "Command Menu → 'Show Sensors':<br><b>Geolocation</b>: Override <code>navigator.geolocation</code> with custom lat/lng coordinates or select from presets (London, Tokyo, Mumbai, etc.).<br><b>Orientation</b>: Emulate device orientation (alpha, beta, gamma) and absolute/integrated accelerometer readings.<br><b>Touch</b> (in older versions; now in Device Toolbar).<br><b>Idle</b>: Emulate user idle/locked state.<br><b>User Agent Client Hints</b>: Override UA brands, platform, architecture, and bitness.<br>Use for testing location-aware apps, device motion games, and responsive behaviors.",
  ["sensors", "L3"])

c("SecuritySensors",
  "How do you override Geolocation for testing?",
  "Sensors panel → <b>Location</b> → select preset (e.g., 'Tokyo') or enter custom latitude/longitude. All calls to <code>navigator.geolocation.getCurrentPosition()</code> will return the spoofed coordinates. This persists until you clear the override. Use for testing map features, local search results, store locators, and region-specific pricing.",
  ["sensors", "L3"])

c("SecuritySensors",
  "How do you emulate dark mode (prefers-color-scheme) in DevTools?",
  "Rendering panel → <b>Emulate CSS media feature prefers-color-scheme</b> → select <code>prefers-color-scheme: dark</code> or <code>prefers-color-scheme: light</code>. Use to test both color schemes without changing your OS theme. Also access via Command Menu → 'Emulate CSS prefers-color-scheme: dark'. Works alongside <code>prefers-reduced-motion</code> and <code>prefers-contrast</code> toggles.",
  ["sensors", "L2"])

c("SecuritySensors",
  "How do you emulate prefers-reduced-motion?",
  "Rendering panel → <b>Emulate CSS media feature prefers-reduced-motion</b> → select <code>reduce</code>. All CSS inside <code>@media (prefers-reduced-motion: reduce)</code> will be applied, and JavaScript can query <code>window.matchMedia('(prefers-reduced-motion: reduce)')</code>. Use to test accessibility for users with vestibular motion disorders.",
  ["sensors", "L2"])

c("SecuritySensors",
  "How do you emulate forced-colors mode (Windows High Contrast)?",
  "Rendering panel → <b>Emulate CSS media feature forced-colors</b> → select <code>active</code>. Simulates Windows High Contrast Mode. CSS system colors (<code>CanvasText</code>, <code>ButtonFace</code>, etc.) are used instead of author-defined colors. Use <code>@media (forced-colors: active)</code> to customize. Essential for accessibility compliance (WCAG).",
  ["sensors", "L3"])

c("SecuritySensors",
  "How do you emulate a different timezone in DevTools?",
  "Sensors panel → <b>Location</b> sets the timezone to match the selected location's timezone. This affects <code>Intl.DateTimeFormat().resolvedOptions().timeZone</code>. Use to test timezone-sensitive features: scheduling, date displays, countdown timers. Combine with geolocation override for full location simulation.",
  ["sensors", "L3"])

c("SecuritySensors",
  "How do you simulate print mode in DevTools?",
  "Rendering panel → <b>Emulate CSS media type</b> → select <code>print</code>. Applies <code>@media print</code> styles. Alternatively, Command Menu → 'Emulate CSS print media'. The page renders with print styles applied (hides navigation, adjusts font sizes, shows/hides print-specific elements) without actually printing. Use <code>Cmd+P</code> → 'Save as PDF' to see actual print output.",
  ["sensors", "L2"])

c("SecuritySensors",
  "How do you emulate different display pixel ratios (DPR)?",
  "Device Toolbar (toggle with <code>Cmd+Shift+M</code>) → ⋮ menu → <b>Add device pixel ratio</b>. Enter a custom DPR (1, 2, 3). This affects <code>window.devicePixelRatio</code> and CSS media queries like <code>@media (-webkit-min-device-pixel-ratio: 2)</code>. Use to test high-DPI (Retina) rendered output, canvas resolution, and responsive images (<code>srcset</code>).",
  ["sensors", "L3"])

c("SecuritySensors",
  "How do you test how your page behaves when fonts fail to load?",
  "Rendering panel → check <b>Disable local fonts</b>. Prevents local font files from being used — only web fonts loaded via <code>@font-face</code> will render (if they're loaded). Combine with Network throttling → 'Offline' to simulate font download failure. Use to test fallback font stacks and <code>font-display</code> strategies.",
  ["sensors", "L3"])

c("SecuritySensors",
  "How do you test accessible focus order with DevTools?",
  "Sources panel → <b>Accessibility</b> pane (in the sidebar when in Elements panel) shows the <b>Source Order Viewer</b> option (if enabled via experiments). Or use the <code>document.querySelectorAll(':focus-visible')</code> in Console. The Accessibility tree shows computed roles, names, and properties. Use the Elements panel → Accessibility pane to see the computed ARIA attributes for any element.",
  ["sensors", "L3"])

# ============================================================
# 09 — ADVANCED WORKFLOWS (L5 Opinion + L6 Innovation)
# ============================================================

c("AdvancedWorkflows",
  "What is Lighthouse and how do you run it?",
  "Lighthouse is an automated auditing tool for web pages. Run it from the Lighthouse panel in DevTools, or via Chrome extension, CLI (<code>npm i -g lighthouse</code>), or PageSpeed Insights. Audits: <b>Performance</b>, <b>Accessibility</b>, <b>Best Practices</b>, <b>SEO</b>, and optionally <b>Progressive Web App</b>. Generates a scored report (0-100) with specific actionable recommendations. Modes: Navigation (full page load), Timespan (interactive), Snapshot (current state).",
  ["advanced", "L5"])

c("AdvancedWorkflows",
  "When should you run Lighthouse in DevTools vs Lighthouse CI vs PageSpeed Insights?",
  "<b>DevTools Lighthouse</b>: During local development. Fast feedback loop. Runs on your machine with your network.<br><b>Lighthouse CI</b>: In CI/CD pipeline. Prevents performance regressions. Can set score budgets and block PRs that degrade scores.<br><b>PageSpeed Insights (PSI)</b>: For production analysis. Uses real-world Chrome UX Report (CrUX) field data + lab simulation. Shows both real-user data and a Lighthouse simulation. Best for understanding what real users experience.",
  ["advanced", "L6"])

c("AdvancedWorkflows",
  "What is the Recorder panel and what does it do?",
  "Opened via the Recorder tab (or Command Menu → 'Show Recorder'). Records user flows (clicks, inputs, navigations) and <b>replays</b> them for testing. Exports recordings to: <b>Puppeteer script</b> (Node.js), <b>Puppeteer replay</b> (library), <b>@puppeteer/replay</b> JSON, or <b>Chrome DevTools</b> format. Use for: creating E2E test scaffolds, reproducing bugs with deterministic steps, and performance testing (can measure with Performance panel).",
  ["advanced", "L6"])

c("AdvancedWorkflows",
  "How do you export a Recorder flow as a Puppeteer script?",
  "Recorder panel → record your flow → stop → click the <b>Export</b> button → select <b>Export as a Puppeteer script</b>. Saves a <code>.js</code> file with the full Puppeteer automation code. Run with <code>node script.js</code> (requires <code>puppeteer</code> package). The generated script includes: selectors, waitForSelector, click, type, and navigation commands. A great way to bootstrap E2E tests from manual testing.",
  ["advanced", "L6"])

c("AdvancedWorkflows",
  "What is the Chrome DevTools Protocol (CDP)?",
  "CDP is the low-level protocol that powers all of DevTools. It's a WebSocket-based RPC protocol that allows external tools to instrument, inspect, debug, and profile Chrome. Everything you do in DevTools GUI is a CDP command under the hood. Domains include: <code>DOM</code>, <code>CSS</code>, <code>Network</code>, <code>Debugger</code>, <code>Runtime</code>, <code>Page</code>, <code>Performance</code>, <code>Profiler</code>, <code>HeapProfiler</code>, etc. Puppeteer and Playwright are high-level wrappers around CDP.",
  ["advanced", "L6"])

c("AdvancedWorkflows",
  "What is the Protocol monitor and how do you open it?",
  "Command Menu → 'Show Protocol monitor'. Shows a live stream of all CDP commands and events sent between the DevTools frontend and the Chrome backend. Each entry shows: direction (sent ➡ received ⬅), method name (e.g., <code>Runtime.evaluate</code>), parameters, and response. Use to: understand what CDP commands DevTools uses for a specific action, debug CDP-based automation scripts, and learn the protocol internals.",
  ["advanced", "L6", "extending"])

c("AdvancedWorkflows",
  "How do you connect DevTools to a remote Chrome instance (e.g., headless Chrome, Android browser)?",
  "Start Chrome with remote debugging enabled: <code>chrome --remote-debugging-port=9222</code>. Then open <code>chrome://inspect</code> in your local Chrome. The remote targets appear under 'Remote Target'. Click <b>inspect</b> to open a DevTools window connected to the remote instance. Or navigate to <code>http://localhost:9222</code> for a JSON API of all debuggable pages. For Android: enable USB debugging → <code>chrome://inspect</code> detects connected devices.",
  ["advanced", "L6", "remote", "extending"])

c("AdvancedWorkflows",
  "How do you debug a Node.js application with Chrome DevTools?",
  "Start Node with: <code>node --inspect app.js</code> (break immediately) or <code>node --inspect-brk app.js</code> (break on first line). Open <code>chrome://inspect</code> in Chrome → click 'inspect' under Remote Target. You get the full DevTools Sources, Console, Performance, and Memory panels — but for your Node.js process. <code>node --inspect=0.0.0.0:9229</code> to expose on all interfaces (Docker, remote servers). Use <code>ndb</code> (npm i -g ndb) for an enhanced Node debugging experience built on DevTools.",
  ["advanced", "L6", "nodejs"])

c("AdvancedWorkflows",
  "What is the difference between <code>--inspect</code> and <code>--inspect-brk</code> in Node.js?",
  "<code>node --inspect app.js</code> starts the inspector on port 9229 and runs the script normally. You must manually set breakpoints or pause execution from DevTools.<br><code>node --inspect-brk app.js</code> starts the inspector and <b>pauses on the first line</b> of user code. This lets you set breakpoints before the script executes — essential for debugging startup code, initialization, and top-level statements.<br><code>node --inspect-wait app.js</code> (Node 22+) waits for the debugger to attach before executing.",
  ["advanced", "L6", "nodejs"])

c("AdvancedWorkflows",
  "How do you debug Node.js with Chrome DevTools inside Docker?",
  "1. Expose the inspector port: <code>docker run -p 9229:9229 ...</code><br>2. Start Node with: <code>node --inspect=0.0.0.0:9229 app.js</code> (bind to 0.0.0.0, not localhost)<br>3. Open <code>chrome://inspect</code> → <b>Configure</b> → add <code>localhost:9229</code><br>4. If on a remote host: use SSH tunneling: <code>ssh -L 9229:localhost:9229 user@remote</code><br>5. For production debugging: always use <code>--inspect</code> (not <code>--inspect-brk</code>) and ensure port is not publicly exposed.",
  ["advanced", "L6", "nodejs", "docker"])

c("AdvancedWorkflows",
  "How do you debug a Service Worker with DevTools?",
  "1. Application panel → Service Workers → click <b>inspect</b> next to the active SW. A separate DevTools window opens for the SW.<br>2. In that window: use Console to log from the SW, Sources to set breakpoints in SW code, Network to see SW-initiated fetches.<br>3. Check 'Update on reload' to force SW updates on page reload (otherwise the installed SW is used for 24h or until update propagates).<br>4. Use <b>Bypass for network</b> to ignore the SW entirely for one-off testing.",
  ["advanced", "L6", "service-worker"])

c("AdvancedWorkflows",
  "How do you use DevTools as a CSS design tool (not just debugging)?",
  "1. <b>Edit CSS directly in the Styles pane</b> — autocompletes values, shows all valid options for properties like <code>display</code>, <code>position</code>.<br>2. <b>Box-shadow editor</b> — click the shadow value for a visual editor with x/y offset, blur, spread, and color picker.<br>3. <b>Cubic-bezier editor</b> — click any <code>cubic-bezier()</code> or CSS transition timing function for a drag-to-edit curve.<br>4. <b>Easing editor</b> in the Animations panel — visualize and tweak animation curves.<br>5. <b>Flexbox/Grid editors</b> — click the <code>flex</code>/<code>grid</code> badges to toggle visual overlays showing alignment, gaps, and track sizes.<br>6. <b>Copy all changes</b> from the Changes panel back to your source code. DevTools is a live WYSIWYG CSS editor.",
  ["advanced", "L5"])

c("AdvancedWorkflows",
  "What is the difference between the Console, the Console panel, and the Console drawer?",
  "<b>Console</b>: The JavaScript REPL and log viewer, available as a full panel or as a drawer.<br><b>Console panel</b>: The full-height Console panel (opened via <code>Cmd+Opt+J</code>).<br><b>Console drawer</b>: A split-pane Console that opens at the bottom of any other panel. Toggle with <code>Esc</code>. The drawer lets you run JS and see logs while simultaneously viewing Elements, Network, or Sources. Most staff-level devs keep the drawer open constantly.",
  ["advanced", "L5"])

c("AdvancedWorkflows",
  "What does pressing <code>Esc</code> do in DevTools?",
  "Toggles the <b>drawer</b> at the bottom — a split-pane that can hold the <b>Console</b>, <b>Search</b>, <b>Changes</b>, <b>Animations</b>, <b>Rendering</b>, <b>Sensors</b>, <b>Coverage</b>, <b>Network conditions</b>, <b>Performance Monitor</b>, <b>Quick source</b>, <b>Issues</b>, or <b>What's New</b>. Switch drawer tabs via the ⋮ menu in the drawer. The drawer is the power-user's multi-tool — keep Console in the drawer while working in any other panel.",
  ["advanced", "L5", "keybinding"])

c("AdvancedWorkflows",
  "How do you emulate focus on a specific page element for debugging?",
  "Elements panel → right-click the element → <b>Focus</b>. The element receives focus as if the user clicked/tabbed to it. All <code>:focus</code> styles apply, and keyboard events route to it. Alternatively, select the element in Elements, then in Console: <code>$0.focus()</code>. Use with force element state (<code>:focus-visible</code>) for complete focus testing.",
  ["advanced", "L5"])

c("AdvancedWorkflows",
  "What is the Issues panel and what does it show?",
  "The Issues panel (available in the drawer or as a tab) aggregates warnings and errors from multiple sources: <b>Cookie issues</b> (SameSite, Secure), <b>Mixed content</b>, <b>CORS errors</b>, <b>CSP violations</b>, <b>Deprecated features</b>, <b>COOP/COEP issues</b> (cross-origin isolation), <b>Permissions policy</b> violations, <b>Trusted Types</b> violations, and <b>Quirks Mode</b> detection. Each issue links to detailed documentation. Use as a first-stop for triaging browser-level problems.",
  ["advanced", "L5"])

c("AdvancedWorkflows",
  "How do you debug CORS errors efficiently?",
  "1. The Console shows CORS errors in red with details about the missing header.<br>2. The <b>Issues</b> panel aggregates CORS issues with suggested fixes.<br>3. Network panel → the failed preflight (OPTIONS) request → Headers tab → check <code>Access-Control-Request-*</code> and <code>Access-Control-Allow-*</code> headers.<br>4. Check the <b>Timing</b> tab — a failed CORS request shows as 'CORS error'.<br>5. Use <code>curl -X OPTIONS</code> to test the preflight response manually. CORS errors are server-side; DevTools only diagnoses the symptoms.",
  ["advanced", "L5"])

c("AdvancedWorkflows",
  "How do you emulate a different language/locale in Chrome DevTools?",
  "Settings → <b>Preferences</b> → <b>Languages</b> → add the desired language and drag to reorder. Refresh the page. This affects the <code>Accept-Language</code> header and <code>navigator.language</code>. To also change timezone and locale-dependent formatting, use the Sensors panel → set the location (which also sets the timezone). For full locale testing: combine with a VPN or location override.",
  ["advanced", "L5"])

c("AdvancedWorkflows",
  "What are the three modes of the JavaScript debugger when paused?",
  "<b>Normal pause</b>: After a breakpoint, <code>debugger;</code> statement, or exception — you can step through code, inspect variables, and evaluate Console expressions in the current scope.<br><b>Logpoint pause</b>: Breaks silently in the background (doesn't stop execution), only logs the message. Set via right-click → Add logpoint.<br><b>Never pause here</b>: Right-click a line number → 'Never pause here' — the debugger skips this line even if a breakpoint or <code>debugger;</code> is set. Use to suppress noise from hot paths or third-party scripts without blackboxing the whole file.",
  ["advanced", "L5"])

c("AdvancedWorkflows",
  "What is the 'Ad privacy' tab in the Application panel?",
  "Shows information about the <b>Protected Audience API</b> (formerly FLEDGE), <b>Attribution Reporting</b>, and <b>Private Aggregation</b> — the Privacy Sandbox APIs replacing third-party cookies. Use to inspect interest groups, debug ad auction flows, view attribution source/trigger registrations, and monitor private aggregation reports. Essential for ad-tech engineers testing post-third-party-cookie implementations.",
  ["advanced", "L6"])

c("AdvancedWorkflows",
  "How do you record a user flow that spans multiple pages?",
  "Recorder panel → start recording → navigate between pages (the Recorder follows) → continue interacting → stop. The recording captures full-page navigations with <code>setViewport</code>, <code>navigate</code>, <code>click</code>, <code>change</code>, and <code>keyDown</code>/<code>keyUp</code> steps. Replay works across page boundaries. Export to Puppeteer generates a script that opens each page and replays the interactions on each.",
  ["advanced", "L6"])

c("AdvancedWorkflows",
  "What are the Developer Resources tab and the 'Authored/Deployed' tree in Sources?",
  "Sources panel → left sidebar: Under the <b>Page</b> tab, there are two views toggled at the bottom:<br><b>Authored</b>: Shows files grouped by the source directory structure (from source maps). Shows original TypeScript/JSX/SCSS files as the developer wrote them.<br><b>Deployed</b>: Shows files grouped by the deployed URL structure. Shows the actual JS/CSS files served to the browser.<br>Toggle between them to see the mapping between source and deployed code.",
  ["advanced", "L5"])

c("AdvancedWorkflows",
  "How do you use the Command Menu for keyboard-driven DevTools workflows?",
  "<code>Cmd+Shift+P</code> opens the Command Menu. Type-less workflows:<br>- 'Dock to right' / 'Dock to bottom' / 'Undock' — reposition DevTools<br>- 'Capture full size screenshot' — one-click full page capture<br>- 'Show Coverage' — find dead code<br>- 'Show Rendering' — visual debugging toolbox<br>- 'Run snippet' — execute saved snippets by name<br>- 'Emulate CSS prefers-color-scheme: dark' — toggle dark mode<br>- 'Show Performance Monitor' — real-time perf dashboard<br>Power users use Command Menu more than the mouse.",
  ["advanced", "L5"])

c("AdvancedWorkflows",
  "What are the key Experiments you should enable for staff-level workflows?",
  "Settings → <b>Experiments</b> → useful ones include:<br><b>Timeline: event initiators</b> — shows what triggered each Performance event<br><b>Resolve variable names in breakpoint-selectable locations</b> — easier conditional breakpoints<br><b>Allow extensions to load custom formatters</b> — for framework-specific object formatting<br><b>Override default line-level CPU profile</b> — high-resolution flame charts<br><b>Live heap profile</b> — continuous memory profiling<br><b>WebAuthn debugging</b> — test WebAuthn/Passkey flows<br><b>Source order viewer</b> — visualize DOM order for accessibility<br>Experimental features may change or be removed — test before relying on them.",
  ["advanced", "L6"])

# ============================================================
# 10 — EXTENDING DEVTOOLS (L6 Innovation)
# ============================================================

c("Extending",
  "How do Chrome extensions add panels to DevTools?",
  "Extensions use the <code>devtools_page</code> manifest entry to specify an HTML page. Inside it, <code>chrome.devtools.panels.create()</code> adds a custom panel. The panel has access to <code>chrome.devtools.inspectedWindow</code> (eval in page context, get resources) and <code>chrome.devtools.network</code> (HAR data). Example panels: React DevTools, Vue DevTools, Redux DevTools, Apollo Client DevTools.",
  ["extending", "L6"])

c("Extending",
  "What is <code>chrome.devtools.inspectedWindow.eval()</code>?",
  "An extension API that evaluates JavaScript in the context of the inspected page. The expression runs with full access to the page's JavaScript objects and DOM. Example: <code>chrome.devtools.inspectedWindow.eval('document.title', callback)</code>. Use to build extension panels that interact with the page's runtime state — this is how React DevTools reads the component tree from the page.",
  ["extending", "L6"])

c("Extending",
  "What are custom object formatters and how do you enable them?",
  "Custom formatters allow libraries to control how their objects are displayed in the Console. Enabled via Settings → Preferences → Console → <b>'Enable custom formatters'</b>, or a library registers via <code>window.devtoolsFormatters</code>. Once enabled, framework-specific objects (Immutable.js records, Moment.js dates, MobX observables) display with rich formatting instead of raw JSON. React DevTools uses this for component formatting.",
  ["extending", "L6"])

c("Extending",
  "How does Puppeteer interact with Chrome DevTools Protocol?",
  "Puppeteer launches Chrome with <code>--remote-debugging-port=0</code> and connects via CDP over WebSocket. Every Puppeteer API call (<code>page.click()</code>, <code>page.evaluate()</code>, <code>page.screenshot()</code>, <code>page.tracing.start()</code>) is translated to one or more CDP commands. You can send raw CDP commands via <code>page.createCDPSession()</code> for protocol features not yet wrapped by Puppeteer. Playwright works the same way but also supports Firefox and WebKit via protocol adapters.",
  ["extending", "L6"])

c("Extending",
  "How do you use raw CDP commands from JavaScript in a page?",
  "You don't — the page can't directly access CDP. CDP is an external protocol for debugging tools. However, extensions can use <code>chrome.debugger.attach()</code> and <code>chrome.debugger.sendCommand()</code> from a DevTools extension. Libraries like <code>puppeteer-core</code> and <code>playwright</code> connect to the CDP WebSocket endpoint. For ad-hoc CDP: open <code>http://localhost:9222/json</code> to find the WebSocket URL, then connect with a WebSocket client.",
  ["extending", "L6"])

c("Extending",
  "How do you run Lighthouse from the command line in CI?",
  "Install: <code>npm i -g lighthouse</code>. Run: <code>lighthouse https://example.com --output html --output-path report.html</code>. Key CI flags: <code>--chrome-flags=\"--headless --no-sandbox\"</code>, <code>--preset=desktop</code> (desktop simulation), <code>--only-categories=performance,accessibility</code>. Set <b>performance budgets</b>: <code>lighthouse --budget-path=budget.json</code>. Lighthouse CI server (<code>lhci</code>) can track scores over time and block regressions via GitHub status checks.",
  ["extending", "L6"])

c("Extending",
  "What is the difference between Puppeteer and Puppeteer-core?",
  "<b>Puppeteer</b>: Downloads a bundled Chromium binary. Self-contained, heavier.<br><b>Puppeteer-core</b>: No bundled browser — connects to an existing Chrome/Chromium instance. Lighter, used when you already have Chrome installed (Docker, CI, or connecting to your own Chrome). Always use <code>puppeteer-core</code> in production/CI where Chrome is managed separately.",
  ["extending", "L6"])

c("Extending",
  "How do you capture a Performance trace programmatically with Puppeteer/CDP?",
  "<code>await page.tracing.start({categories: ['devtools.timeline']})</code> — starts recording. <code>await page.tracing.stop()</code> — returns a trace buffer. Save to file: <code>fs.writeFileSync('trace.json', traceData)</code>. Load the trace in DevTools: Performance panel → load profile (⬆ button) → select the trace file. Categories: <code>'devtools.timeline'</code> (general), <code>'disabled-by-default-devtools.timeline.frame'</code> (frames), <code>'v8.execute'</code> (JS execution).",
  ["extending", "L6"])

c("Extending",
  "How do you use <code>queryObjects()</code> to debug memory leaks in extensions?",
  "In the Console of a DevTools extension's inspection context (not the page), <code>queryObjects(MyConstructor)</code> returns all live instances. Use to: find leaked extension objects attached to pages, verify cleanup logic, and debug extension memory issues. Works in the <code>chrome://inspect</code> → inspect an extension's background page Console.",
  ["extending", "L6"])

c("Extending",
  "How do you debug a Chrome extension's DevTools page itself?",
  "1. Open <code>chrome://extensions</code> and enable <b>Developer mode</b>.<br>2. Find your extension → click <b>background page</b> (or service worker) to inspect the extension's main context.<br>3. For the DevTools panel: right-click the panel and select <b>Inspect</b> — this opens a second DevTools window debugging the first DevTools panel. Or in the first DevTools, press <code>Ctrl+Shift+I</code> again to open a third-level DevTools for the second one (Inception-level debugging).<br>4. Use <code>chrome.devtools.inspectedWindow.eval()</code> to run code in the debugged page.",
  ["extending", "L6"])

c("Extending",
  "What is the 'About DevTools' panel and what does <code>chrome://devtools</code> show?",
  "<code>chrome://devtools</code> shows the DevTools build information: Chrome version, V8 version, DevTools version, User Agent, and supported experiments. Useful for: verifying you're on the latest version, checking if an experimental feature is available in your Chrome build, and reporting bugs with accurate version info.",
  ["extending", "L6"])

c("Extending",
  "How do you use DevTools to inspect and debug WebAssembly?",
  "Network panel → filter by <b>Wasm</b>. Click a .wasm file to view it. If the module was compiled with debugging enabled (<code>-g</code> in Emscripten), Sources panel shows the original C/C++/Rust source. The Call Stack shows wasm frames mixed with JS frames. Performance panel shows wasm execution in the flame chart. Memory panel heap snapshots show wasm memory. DevTools has first-class WASM support since Chrome 71.",
  ["extending", "L6", "wasm"])

c("Extending",
  "How do you use DevTools to inspect SharedArrayBuffer and cross-origin isolation?",
  "Application panel → <b>Frames</b> → select the top frame → check the <b>Cross-Origin Isolation</b> section. Shows: <b>Cross-Origin-Opener-Policy</b> (COOP), <b>Cross-Origin-Embedder-Policy</b> (COEP), and whether <code>SharedArrayBuffer</code> is available. The Console shows errors when COOP/COEP headers are missing. Use <code>self.crossOriginIsolated</code> in Console to check. Required for <code>SharedArrayBuffer</code>, high-resolution timers, and <code>performance.measureUserAgentSpecificMemory()</code>.",
  ["extending", "L6"])

c("Extending",
  "How do you capture a Node.js CPU profile from the command line?",
  "Run: <code>node --cpu-prof app.js</code>. Generates a <code>CPU.${isoTime}.${pid}.cpuprofile</code> file. Load it in DevTools: Performance panel → 'Load profile' (⬆ icon) → select the file. Or use the <code>inspector</code> module: <code>session.connect()</code>, <code>Profiler.start()</code>, <code>Profiler.stop()</code>. For heap snapshots: <code>node --heap-prof app.js</code> or <code>require('v8').writeHeapSnapshot()</code>. Load in Memory panel.",
  ["extending", "L6", "nodejs"])

c("Extending",
  "What is Puppeteer's page.evaluateOnNewDocument() and how does it relate to DevTools?",
  "<code>page.evaluateOnNewDocument(fn)</code> injects a JavaScript function that runs in every page context <b>before</b> any scripts execute. This is the programmatic equivalent of Sources → Overrides/Workspaces to inject debugging code. Use cases: monkey-patch browser APIs for testing, install global error handlers, override <code>navigator</code> properties, or inject mock implementations. Shared with how DevTools itself injects its console utilities ($, $$, $x, etc.) before page scripts run.",
  ["extending", "L6"])

c("Extending",
  "How do you set up a headless Chrome + DevTools development workflow?",
  "1. Start headless Chrome: <code>google-chrome --headless --remote-debugging-port=9222</code><br>2. Open <code>http://localhost:9222</code> to list all debuggable targets (tabs)<br>3. Connect Puppeteer: <code>puppeteer.connect({browserURL: 'http://localhost:9222'})</code><br>4. Open <code>chrome://inspect</code> in your visual Chrome → inspect any headless tab<br>5. Use <code>page.screenshot({fullPage: true})</code> for visual regression testing<br>6. Combine with <code>page.tracing</code> for automated performance regression detection in CI<br>This is the production debugging stack: headless Chrome for automation, DevTools for manual inspection when needed.",
  ["extending", "L6"])

# Build & write
for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = "Chrome_DevTools_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(C)} cards across {len(decks)} decks -> {filename}")

# VERIFICATION (run this block after build):
# import zipfile, sqlite3, json
# with zipfile.ZipFile(filename) as z: z.extract("collection.anki2", "/tmp/")
# db = sqlite3.connect("/tmp/collection.anki2")
# n, c = db.execute("SELECT count(*) FROM notes").fetchone()[0], db.execute("SELECT count(*) FROM cards").fetchone()[0]
# decks_json = json.loads(db.execute("SELECT decks FROM col").fetchone()[0])
# print(f"Notes: {n}, Cards: {c}")
# for v in decks_json.values():
#     if v["name"] != "Default": print(f"  {v['name']}")
# assert n == c == len(C), f"Mismatch: {n} notes, {c} cards, {len(C)} defined"
