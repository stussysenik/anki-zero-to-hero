import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "View_Transitions_API"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "MPA":          genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-MPA-Transitions"),
    "SPA":          genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-SPA-Transitions"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === FUNDAMENTALS ===

c("Fundamentals", "What is the View Transitions API?",
  "A browser API for creating smooth animated transitions between DOM states (page navigations or SPA state changes). The browser captures before/after snapshots and crossfades between them by default.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>document.startViewTransition()</code> method?",
  "Initiates a view transition for SPA state changes. Takes a callback that updates the DOM: <code>document.startViewTransition(() =&gt; updateDOM())</code>. Returns a promise that resolves when the transition completes.",
  ["L0_primitives"])

c("Fundamentals", "What are the phases of a view transition?",
  "1: Capture old state (snapshot). 2: DOM updates (callback). 3: Capture new state (snapshot). 4: Animate — old snapshot fades out, new snapshot fades in (default crossfade). 5: Clean up pseudo-elements.",
  ["L0_primitives"])

c("Fundamentals", "What pseudo-elements does the View Transitions API create?",
  "<code>::view-transition</code> — root container (fixed, full viewport). <code>::view-transition-group(root)</code> — groups old/new. <code>::view-transition-image-pair(root)</code> — holds both images. <code>::view-transition-old(root)</code> — outgoing. <code>::view-transition-new(root)</code> — incoming.",
  ["L0_primitives"])

c("Fundamentals", "What is a <code>view-transition-name</code>?",
  "A CSS property that tags an element for the transition: <code>view-transition-name: hero-image</code>. The browser tracks elements with matching names across old/new states and animates them independently from the root crossfade.",
  ["L0_primitives"])

c("Fundamentals", "What is the Cross-document (MPA) View Transitions?",
  "Transitions between same-origin page navigations (multi-page apps). No JavaScript needed. Triggered by navigation (link click, form submit). Both pages must opt in: <code>&lt;meta name=\"view-transition\" content=\"same-origin\"&gt;</code> or CSS <code>@view-transition { navigation: auto; }</code>.",
  ["L0_primitives"])

c("Fundamentals", "What CSS rule enables MPA view transitions?",
  "<code>@view-transition { navigation: auto; }</code> — enables same-origin cross-document view transitions. Or the meta tag equivalent. Can scope with <code>same-origin</code> keyword.",
  ["L0_primitives"])

c("Fundamentals", "What is the transition object returned by <code>startViewTransition()</code>?",
  "Has three properties: <code>updateCallbackDone</code> (promise), <code>ready</code> (promise, resolves when pseudo-elements are created), <code>finished</code> (promise, resolves when animation completes). Use <code>.ready</code> to animate between capture and play.",
  ["L1_mechanics"])

c("Fundamentals", "Which browsers support View Transitions API?",
  "Chromium-based (Chrome, Edge, Opera, Arc) since Chrome 111+ (March 2023). Cross-document (MPA) since Chrome 126+ (2024). Not supported in Firefox or Safari (as of 2025) — use as progressive enhancement.",
  ["L0_primitives"])

# === CORE OPERATIONS ===

c("CoreOps", "How do you trigger a basic SPA view transition?",
  "<code>document.startViewTransition(() =&gt; { /* update DOM */ });</code> — the callback receives no arguments. Update the DOM synchronously inside the callback.",
  ["L1_mechanics"])

c("CoreOps", "How do you give an element a <code>view-transition-name</code>?",
  "CSS: <code>.hero { view-transition-name: hero-image; }</code>. The name must be unique per page — two elements with the same name cause the transition to be skipped for those elements.",
  ["L1_mechanics"])

c("CoreOps", "How do you customize the default animation?",
  "Target pseudo-elements in CSS: <code>::view-transition-old(root) { animation: slide-out 0.3s; }</code> <code>::view-transition-new(root) { animation: slide-in 0.3s; }</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you target a specific named element's transition?",
  "<code>::view-transition-old(hero-image) { animation: 0.5s ease-out fade-slide; }</code>. Use the <code>view-transition-name</code> value inside the pseudo-element parentheses.",
  ["L1_mechanics"])

c("CoreOps", "How do you wait for a view transition to complete?",
  "<code>const transition = document.startViewTransition(updateDom);<br>await transition.finished;<br>console.log('Transition done');</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you run code after the capture phase but before animation?",
  "<code>const t = document.startViewTransition(updateDom);<br>await t.ready; // pseudo-elements exist now<br>// Custom Web Animations API on pseudo-elements<br>document.documentElement.animate(...)</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you skip the animation for a specific element?",
  "Either don't assign a <code>view-transition-name</code> (it follows the root crossfade by default), or set <code>view-transition-name: none</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you enable MPA cross-document transitions?",
  "On both pages (source and destination): <code>@view-transition { navigation: auto; }</code> in CSS, OR <code>&lt;meta name=\"view-transition\" content=\"same-origin\"&gt;</code> in <code>&lt;head&gt;</code>.",
  ["L1_mechanics"])

# === MPA TRANSITIONS ===

c("MPA", "How do you name elements for MPA transitions across pages?",
  "Give elements the same <code>view-transition-name</code> on both pages. The browser matches them and animates between the two positions. Example: header with <code>view-transition-name: site-header</code> on both pages.",
  ["L1_mechanics"])

c("MPA", "How do you create custom MPA transition animations?",
  "Define <code>@keyframes</code> and apply to pseudo-elements in the destination page's CSS. The animation runs when the page loads: <code>::view-transition-new(root) { animation: slide-in 0.4s; }</code>",
  ["L1_mechanics"])

c("MPA", "What is the <code>pageswap</code> event?",
  "Fires on the outgoing page when a cross-document navigation starts. <code>window.addEventListener('pageswap', e =&gt; { ... })</code>. Gives a <code>viewTransition</code> object for last-moment modifications before snapshot.",
  ["L1_mechanics"])

c("MPA", "What is the <code>pagereveal</code> event?",
  "Fires on the incoming page when the view transition begins. <code>window.addEventListener('pagereveal', e =&gt; { ... })</code>. Access <code>e.viewTransition</code> for animation customization.",
  ["L1_mechanics"])

c("MPA", "How do you control which navigations trigger transitions?",
  "CSS: <code>@view-transition { navigation: auto; }</code> for all same-origin. JavaScript: check <code>e.viewTransition</code> in <code>pageswap</code>/<code>pagereveal</code> events. Can skip based on URL or user preference.",
  ["L2_composition"])

# === SPA TRANSITIONS ===

c("SPA", "How do you integrate view transitions with a router (React Router, etc.)?",
  "In the router's navigation callback, wrap the state update: <code>router.navigate = (to) =&gt; document.startViewTransition(() =&gt; oldNavigate(to))</code>. Libraries like <code>react-view-transitions</code> or <code>svelte-view-transitions</code> abstract this.",
  ["L2_composition"])

c("SPA", "How do you handle view transitions with React?",
  "Wrap state updates: <code>const [page, setPage] = useState('/home');<br>function navigate(to) { document.startViewTransition(() =&gt; setPage(to)) }</code>. Use <code>useLayoutEffect</code> to ensure DOM is ready before transition starts.",
  ["L2_composition"])

c("SPA", "How do you use view transitions with Astro?",
  "Astro 3.0+ has built-in support: add <code>&lt;ViewTransitions /&gt;</code> component to your layout. Automatically wraps page navigations. Supports named transitions via <code>transition:name</code> directive.",
  ["L2_composition"])

# === PATTERNS ===

c("Patterns", "What is the crossfade pattern?",
  "Default behavior, no custom code needed. Old page fades out, new page fades in. Use <code>::view-transition-old(root), ::view-transition-new(root) { animation-duration: 300ms; }</code> to adjust timing.",
  ["L2_composition"])

c("Patterns", "What is the morphing hero image pattern?",
  "Give the hero image <code>view-transition-name: hero</code> on both pages. The browser animates position and size between the two states. Works across MPA and SPA navigations.",
  ["L2_composition"])

c("Patterns", "What is the shared element transition pattern?",
  "Multiple elements with matching names across old/new: thumbnail gallery where each image has <code>view-transition-name: photo-{id}</code>. The browser animates each independently.",
  ["L2_composition"])

c("Patterns", "What is the reduced-motion pattern?",
  "Respect <code>prefers-reduced-motion</code>: <code>@media (prefers-reduced-motion) { ::view-transition-old(root), ::view-transition-new(root) { animation: none; } }</code>. Or skip the transition entirely: <code>if (window.matchMedia('(prefers-reduced-motion)').matches) { updateDom(); return; }</code>.",
  ["L2_composition"])

c("Patterns", "What is the page-type transition pattern?",
  "Different transitions for different navigation types: apply a class to <code>html</code> element, then target with <code>html.gallery-page ::view-transition-old(root) { ... }</code>. Gives list→detail a different animation than page→page.",
  ["L3_design"])

# === GOTCHAS ===

c("Gotchas", "Why is my view transition not working?",
  "Common causes: 1) browser doesn't support it (needs Chrome 111+). 2) Multiple elements have the same <code>view-transition-name</code> (must be unique). 3) The DOM update callback doesn't actually change anything. 4) The element has <code>display: none</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why do elements with the same <code>view-transition-name</code> cause issues?",
  "Names must be unique per page. Two elements with the same name cause the transition to be skipped for those elements. If you have a list, use dynamic names: <code>view-transition-name: item-${id}</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why does the transition flash or glitch?",
  "The element's layout may change between capture and animation phases. Ensure the element has <code>view-transition-name</code> applied BEFORE the transition starts (in CSS, not added in JS during the callback). Use <code>contain: paint</code> or <code>contain: layout</code> for stability.",
  ["L4_diagnosis"])

c("Gotchas", "How do view transitions interact with <code>position: fixed</code> elements?",
  "The <code>::view-transition</code> pseudo-element creates a new stacking context over the entire viewport. Fixed elements inside captured snapshots are flattened. If you need a fixed nav during transition, exclude it with a unique <code>view-transition-name</code> and animate it separately.",
  ["L4_diagnosis"])

c("Gotchas", "Why do MPA transitions feel slow?",
  "MPA transitions must wait for the new page to load before animating. Use <code>prefetch</code>/<code>prerender</code> (Speculation Rules API) to preload destination pages. Or use SPA transitions for instant state changes.",
  ["L4_diagnosis"])

c("Gotchas", "Can I use view transitions with iframes?",
  "No. The pseudo-elements overlay the root document's viewport. Iframes are isolated. If the iframe is same-origin, you might access its <code>document.startViewTransition</code>, but cross-origin is blocked.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "What are the Speculation Rules API and how do they help view transitions?",
  "Prerenders/prefetches pages before the user clicks. Combine with view transitions for instant transitions: <code>&lt;script type=\"speculationrules\"&gt;{ prerender: [{ source: 'list', urls: ['/next-page'] }] }&lt;/script&gt;</code>. The destination page is ready before the transition starts.",
  ["L6_innovation"])

c("Expert", "How do you debug view transitions?",
  "In Chrome DevTools: 'Animations' panel shows all view transition animations. CSS overview shows pseudo-elements. <code>transition.ready</code> gives access to the Animation objects. Use <code>document.documentElement.getAnimations()</code> to inspect running transitions.",
  ["L6_innovation"])

c("Expert", "What is the <code>types</code> system for MPA transitions?",
  "Assign <code>view-transition-name</code> with CSS scoping: <code>html:active-view-transition-type(detail) { ... }</code> or JS: <code>pageswap</code> event sets <code>e.viewTransition.types.add('slide')</code>. Create different animations for different navigation types.",
  ["L6_innovation"])

c("Expert", "How do you chain multiple view transitions?",
  "Each <code>startViewTransition</code> returns a promise. Chain sequentially: <code>await t1.finished; await startViewTransition(step2); await startViewTransition(step3)</code>. Or use abort signals: <code>startViewTransition({ update: cb, signal: controller.signal })</code>.",
  ["L6_innovation"])

c("Expert", "How do view transitions work with the Navigation API?",
  "The Navigation API (<code>window.navigation</code>) fires <code>navigate</code> events. Intercept them: <code>navigation.addEventListener('navigate', e =&gt; { e.intercept({ handler: () =&gt; document.startViewTransition(() =&gt; loadPage(e.destination.url)) }) })</code>. Gives full control over SPA-like MPA transitions.",
  ["L6_innovation"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
