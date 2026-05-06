import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "GSAP"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === GSAP FUNDAMENTALS ===

c("Fundamentals", "What is GSAP?",
  "GreenSock Animation Platform — a high-performance JavaScript animation library for the web. Animates CSS properties, SVGs, Canvas, WebGL objects, and DOM elements with precise control.",
  ["L0_primitives"])

c("Fundamentals", "What is a GSAP tween?",
  "The basic animation unit. A tween changes properties of a target from current value to a specified value over a duration. Created with <code>gsap.to()</code>, <code>gsap.from()</code>, <code>gsap.fromTo()</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is a GSAP timeline?",
  "A container for sequencing multiple tweens in order. Created with <code>gsap.timeline()</code>. Provides precise control over timing, overlapping animations, and orchestration.",
  ["L0_primitives"])

c("Fundamentals", "What are GSAP's three core tween methods?",
  "<code>gsap.to()</code> — animate TO values. <code>gsap.from()</code> — animate FROM values to current state. <code>gsap.fromTo()</code> — animate FROM specified values TO specified values.",
  ["L0_primitives"])

c("Fundamentals", "What is GSAP ScrollTrigger?",
  "A plugin that links animations to scroll position. Creates scroll-driven animations, pinning, parallax, and reveal effects. <code>gsap.registerPlugin(ScrollTrigger)</code> — must be registered before use.",
  ["L0_primitives"])

c("Fundamentals", "What is GSAP Flip?",
  "First-Last-Invert-Play — a plugin for animating layout changes. Records an element's position (First), captures new position after a state change (Last), calculates the difference (Invert), then animates (Play).",
  ["L0_primitives"])

c("Fundamentals", "What is GSAP Observer?",
  "A plugin for normalizing mouse/touch/pointer events across devices. Provides delta-based scroll observation. Useful for custom scroll experiences, carousels, and gesture-based interactions.",
  ["L0_primitives"])

c("Fundamentals", "What is GSAP Draggable?",
  "A plugin for making elements draggable, spinnable, throwable. Supports snapping, bounds, and inertia. <code>Draggable.create(\".box\", {type: \"x,y\"})</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is GSAP MotionPath?",
  "A plugin for animating elements along SVG paths or curves. <code>motionPath: { path: \"#myPath\", align: \"#myPath\" }</code>. Elements can auto-rotate to follow the path direction.",
  ["L0_primitives"])

c("Fundamentals", "What easing does GSAP use by default?",
  "<code>\"power1.out\"</code> — a gentle deceleration. Not linear. GSAP provides <code>power1-4</code>, <code>back</code>, <code>elastic</code>, <code>bounce</code>, <code>circ</code>, <code>expo</code>, <code>sine</code>, <code>steps</code>, and custom easing via <code>CustomEase</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is GSAP's stagger property?",
  "Staggers the start times of animation across a <code>NodeList</code> / <code>Array</code>. <code>stagger: 0.1</code> offsets each element by 0.1s. Can also use object syntax: <code>stagger: { each: 0.1, from: \"center\" }</code>.",
  ["L0_primitives"])

c("Fundamentals", "Is GSAP free?",
  "Core GSAP (all tweening, timelines, basic utils) is free. Plugins (ScrollTrigger, Flip, Observer, Draggable, MotionPath, SplitText, MorphSVG, CustomEase) require a Club GreenSock membership for commercial use.",
  ["L0_primitives"])

# === GSAP CORE OPERATIONS ===

c("CoreOps", "How do you create a basic <code>to</code> tween?",
  "<code>gsap.to(\".box\", { x: 200, duration: 1, opacity: 0.5 })</code> — animates to the specified values over 1 second.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a <code>from</code> tween?",
  "<code>gsap.from(\".box\", { x: -200, opacity: 0, duration: 1 })</code> — starts from these values and animates to the element's current/natural state.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a <code>fromTo</code> tween?",
  "<code>gsap.fromTo(\".box\", { x: -100 }, { x: 200, duration: 1 })</code> — animates from the first object to the second object values.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a timeline and add tweens?",
  "<code>const tl = gsap.timeline();<br>tl.to(\".box\", { x: 200, duration: 0.5 })<br>  .to(\".box\", { y: 100, duration: 0.3 })<br>  .to(\".box\", { rotation: 360, duration: 0.5 });</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you position tweens on a timeline?",
  "Use the position parameter: <code>tl.to(\".a\", { x: 100 }, \"+=0.5\")</code> (0.5s after previous), <code>\"-=0.2\"</code> (overlap), <code>\"&lt;\"</code> (same time as last start), <code>\"&gt;+0.2\"</code>, or absolute <code>2</code> (at 2s).",
  ["L1_mechanics"])

c("CoreOps", "How do you add labels to a timeline?",
  "<code>tl.add(\"startLabel\")</code> or <code>tl.to(\".box\", { x: 100 }, \"myLabel\")</code>. Then reference: <code>tl.to(\".circle\", { y: 50 }, \"myLabel+=0.5\")</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you control playback of a tween/timeline?",
  "<code>tl.play()</code>, <code>tl.pause()</code>, <code>tl.reverse()</code>, <code>tl.restart()</code>, <code>tl.seek(0.5)</code> (jump to 0.5s), <code>tl.progress(0.75)</code> (jump to 75%).",
  ["L1_mechanics"])

c("CoreOps", "How do you set up ScrollTrigger?",
  "<code>gsap.registerPlugin(ScrollTrigger);<br>gsap.to(\".box\", {<br>  scrollTrigger: \".box\",<br>  x: 500<br>});</code> — animates x as the element scrolls into view.",
  ["L1_mechanics"])

c("CoreOps", "What are the key ScrollTrigger config properties?",
  "<code>scrollTrigger: { trigger: \".el\", start: \"top 80%\", end: \"bottom 20%\", scrub: true, pin: true, markers: true }</code> — trigger element, scroll positions, scrubbing, pinning, debug markers.",
  ["L1_mechanics"])

c("CoreOps", "How do you kill a tween/timeline?",
  "<code>tween.kill()</code> or <code>timeline.kill()</code> — stops immediately and releases for GC. <code>gsap.killTweensOf(\".box\")</code> kills all tweens targeting that element.",
  ["L1_mechanics"])

c("CoreOps", "How do you set defaults for a timeline?",
  "<code>gsap.timeline({ defaults: { duration: 0.5, ease: \"power2.out\" } })</code> — all child tweens inherit these defaults unless overridden.",
  ["L1_mechanics"])

c("CoreOps", "How do you use stagger with an object config?",
  "<code>gsap.to(\".box\", { y: -50, stagger: { each: 0.1, from: \"center\", grid: \"auto\", axis: \"x\" } })</code> — stagger from center outward, with grid awareness.",
  ["L1_mechanics"])

c("CoreOps", "How do you add callbacks to a tween/timeline?",
  "<code>gsap.to(\".box\", { x: 100, onStart: () =&gt; console.log(\"start\"), onComplete: () =&gt; console.log(\"done\"), onUpdate: () =&gt; {}, onRepeat: () =&gt; {} })</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you animate an SVG attribute?",
  "Use <code>attr</code> property: <code>gsap.to(\"circle\", { attr: { cx: 200, cy: 100, r: 50 }, duration: 1 })</code>. For transform, use the shorthand: <code>gsap.to(\"rect\", { x: 100, rotation: 45 })</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you repeat a tween?",
  "<code>gsap.to(\".box\", { x: 100, repeat: 3, yoyo: true, repeatDelay: 0.5 })</code> — repeats 3 times (4 plays total), yoyos back and forth, with 0.5s delay between repeats.",
  ["L1_mechanics"])

c("CoreOps", "How do you animate CSS variables with GSAP?",
  "<code>gsap.to(\".box\", { \"--myColor\": \"#ff0000\", duration: 1 })</code> — animates custom property values. Element must use <code>var(--myColor)</code> in its CSS.",
  ["L1_mechanics"])

c("CoreOps", "How do you get all tweens on an element?",
  "<code>gsap.getTweensOf(\".box\")</code> — returns an array of active tweens targeting the element. Useful for inspection or conditional killing.",
  ["L1_mechanics"])

c("CoreOps", "How do you use ScrollTrigger with scrub?",
  "<code>gsap.to(\".box\", {<br>  scrollTrigger: { trigger: \".box\", start: \"top center\", end: \"bottom center\", scrub: true },<br>  x: 500<br>});</code> — animation progress is tied to scroll position. <code>scrub: 0.5</code> adds 0.5s smooth lag.",
  ["L1_mechanics"])

# === GSAP PATTERNS ===

c("Patterns", "What is the reveal animation pattern?",
  "Use <code>gsap.from()</code> with <code>opacity: 0, y: 50</code>. Common for scroll-triggered content reveals. Each element animates in from below with a stagger.",
  ["L2_composition"])

c("Patterns", "What is the parallax scrolling pattern?",
  "Multiple layers moving at different speeds: <code>gsap.to(\".bg\", { yPercent: 20, ease: \"none\", scrollTrigger: { scrub: true } })</code>. Each layer has a different <code>yPercent</code> value.",
  ["L2_composition"])

c("Patterns", "What is the pinning pattern with ScrollTrigger?",
  "<code>scrollTrigger: { trigger: \".section\", pin: true, scrub: true }</code>. The section stays fixed while internal animations play. Useful for storytelling, product showcases.",
  ["L2_composition"])

c("Patterns", "What is the staggered list animation pattern?",
  "Animate list items sequentially: <code>gsap.from(\"li\", { opacity: 0, x: -20, stagger: 0.08, duration: 0.3 })</code>. Each item fades in slightly after the previous.",
  ["L2_composition"])

c("Patterns", "What is the Flip animation pattern?",
  "<code>const state = Flip.getState(\".cards\"); /* change layout */;<br>Flip.from(state, { duration: 0.5, stagger: 0.05, ease: \"power2.inOut\" });</code> — animates from old to new positions smoothly.",
  ["L2_composition"])

c("Patterns", "What is the matchMedia pattern in GSAP?",
  "<code>ScrollTrigger.matchMedia({<br>  \"(min-width: 800px)\": () =&gt; { /* desktop animations */ },<br>  \"(max-width: 799px)\": () =&gt; { /* mobile animations */ }<br>});</code> — responsive animations that rebuild on breakpoint change.",
  ["L2_composition"])

c("Patterns", "What is the counter animation pattern?",
  "Animate a number display: <code>gsap.from(counter, { textContent: 0, duration: 2, snap: { textContent: 1 }, scrollTrigger: ... })</code>. <code>snap</code> rounds to whole numbers.",
  ["L2_composition"])

c("Patterns", "What is the hover micro-interaction pattern?",
  "<code>element.addEventListener(\"mouseenter\", () =&gt; gsap.to(el, { scale: 1.1, duration: 0.2 }))<br>element.addEventListener(\"mouseleave\", () =&gt; gsap.to(el, { scale: 1, duration: 0.2 }))</code>",
  ["L2_composition"])

# === GSAP GOTCHAS ===

c("Gotchas", "Why doesn't my ScrollTrigger animation update on resize?",
  "ScrollTrigger refreshes automatically but you may need <code>ScrollTrigger.refresh()</code> after dynamic content changes. Set <code>invalidateOnRefresh: true</code> on tweens that depend on viewport calculations.",
  ["L4_diagnosis"])

c("Gotchas", "Why is GSAP animating transform values but they jump at the end?",
  "GSAP sets inline <code>transform</code> on the element. If CSS also has transform rules with <code>!important</code> or conflicting values, they compete. Use GSAP for ALL transform animations on that element.",
  ["L4_diagnosis"])

c("Gotchas", "What causes flickering with <code>from</code> tweens?",
  "<code>from()</code> immediately sets the FROM values, potentially causing a flash before JS executes. Use <code>gsap.set()</code> to pre-set the initial state before the tween, or use <code>autoAlpha: 0</code> (sets visibility as well as opacity).",
  ["L4_diagnosis"])

c("Gotchas", "Why don't GSAP tweens work with React state-driven styles?",
  "React re-renders may overwrite inline styles GSAP sets. Use <code>useRef</code> for element references, animate in <code>useLayoutEffect</code>, or use GSAP's <code>context()</code> for cleanup. Don't let React set conflicting styles.",
  ["L4_diagnosis"])

c("Gotchas", "How do you prevent GSAP animation memory leaks in SPAs?",
  "Use <code>gsap.context()</code> to scope animations: <code>let ctx = gsap.context(() =&gt; { /* animations */ }, scopeRef); return () =&gt; ctx.revert();</code>. This kills all animations in the scope on cleanup.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>ScrollTrigger.refresh()</code> not fix my layout shift?",
  "<code>refresh()</code> recalculates start/end positions based on current DOM. If the DOM hasn't finished updating (e.g., images loaded), use <code>ScrollTrigger.refresh()</code> in a <code>window.load</code> callback or after a <code>requestAnimationFrame</code>.",
  ["L4_diagnosis"])

c("Gotchas", "What is the <code>immediateRender</code> gotcha with <code>from</code> tweens?",
  "<code>from()</code> tweens render their FROM values immediately by default. In a timeline, <code>from()</code> tweens after the first position may render at timeline start, not at their scheduled time. Set <code>immediateRender: false</code> to defer.",
  ["L4_diagnosis"])

# === GSAP EXPERT ===

c("Expert", "What is <code>gsap.context()</code> and why use it?",
  "Creates an isolated animation scope. All tweens/timelines created inside are tracked and can be reverted/killed at once. Essential for React/Vue/Svelte components to prevent leaks on unmount.",
  ["L3_design"])

c("Expert", "What is GSAP's <code>quickTo</code> method?",
  "Creates an optimized function for rapidly updating a single property. <code>const xTo = gsap.quickTo(\".box\", \"x\"); xTo(100);</code>. Much faster than creating new tweens for frequent updates (e.g., mouse-follow).",
  ["L6_innovation"])

c("Expert", "How do you batch multiple GSAP reads and writes?",
  "GSAP automatically batches reads (getting computed styles) then writes (setting inline styles) within a single tick. This prevents layout thrashing. Custom batching: use <code>gsap.ticker</code> or <code>ScrollTrigger.sort()</code>.",
  ["L3_design"])

c("Expert", "What is CustomEase and when do you need it?",
  "A Club GreenSock plugin for creating arbitrary easing curves. Define as string: <code>\"M0,0 C0.33,1 0.68,1 1,1\"</code> or visually in the GSAP Ease Visualizer. Use when built-in eases don't match your design.",
  ["L5_opinion"])

c("Expert", "How should you structure GSAP animations in a production codebase?",
  "Centralize animation logic, use <code>gsap.context()</code> per component, provide <code>ScrollTrigger.refresh()</code> after dynamic content loads, use <code>gsap.matchMedia()</code> for responsive behaviors, and animate CSS custom properties for theme-aware animations.",
  ["L5_opinion"])

c("Expert", "What is the performance hierarchy of GSAP animations?",
  "Fastest: <code>transform</code> (<code>x</code>, <code>y</code>, <code>scale</code>, <code>rotation</code>) and <code>opacity</code> (GPU-composited). Slower: layout-triggering properties (<code>width</code>, <code>height</code>, <code>top</code>, <code>left</code>). Avoid animating layout properties — use FLIP or transforms.",
  ["L3_design"])

c("Expert", "How do you coordinate GSAP with the browser's Intersection Observer?",
  "ScrollTrigger uses IntersectionObserver internally for initial detection, then switches to scroll-based. For advanced cases, use <code>ScrollTrigger.create({ trigger: \".el\", onEnter: () =&gt; animation.play() })</code> for observer-like behavior.",
  ["L3_design"])

c("Expert", "How does GSAP's render loop work?",
  "GSAP uses <code>requestAnimationFrame</code> with a single shared ticker. All tweens update on the same frame. Priority: tweens update before timelines. The ticker adapts its frequency based on active animations (lags when idle, full-speed when animating).",
  ["L6_innovation"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
