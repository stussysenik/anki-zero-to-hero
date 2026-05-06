import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Rive"

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

# === RIVE FUNDAMENTALS ===

c("Fundamentals", "What is Rive?",
  "A real-time interactive design and animation tool. Creates state-machine-driven, vector-based animations that run natively on web, mobile, and desktop via a lightweight runtime.",
  ["L0_primitives"])

c("Fundamentals", "What is a Rive State Machine?",
  "A visual graph defining transitions between animation states based on inputs (boolean, number, trigger). Powers interactive animations without writing imperative code — declare inputs, define transitions, the runtime handles the rest.",
  ["L0_primitives"])

c("Fundamentals", "What is a Rive Artboard?",
  "The canvas where you design vector graphics and animations. Each file can contain multiple artboards. The runtime loads a specific artboard by name or index.",
  ["L0_primitives"])

c("Fundamentals", "What is the difference between Rive and Lottie?",
  "Lottie: After Effects export, static playback. Rive: purpose-built tool, state machines for interactivity, smaller file size, real-time blending, runtime manipulation of bones/shapes/inputs. Rive is interactive by design.",
  ["L0_primitives"])

c("Fundamentals", "What is a Rive Input?",
  "A variable exposed by a state machine: <code>bool</code>, <code>number</code>, or <code>trigger</code>. External code sets these values to drive animation transitions. E.g., <code>artboard.stateMachineInput(\"isHovered\").value = true</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is a Rive Listener?",
  "A Rive-native event handler attached to a state machine or specific artboard element. Listeners fire on pointer events (<code>pointerDown</code>, <code>pointerEnter</code>) or timeline events. They change inputs, firing state transitions.",
  ["L0_primitives"])

c("Fundamentals", "What is the Rive bone system?",
  "An IK (inverse kinematics) rigging system. Control a skeleton with bones that deform vector shapes. Animators animate bones; the runtime interpolates bone positions and the mesh deforms accordingly.",
  ["L0_primitives"])

c("Fundamentals", "What is a Rive Timeline animation?",
  "Keyframe-based animation on a timeline. Unlike state machines, these are for linear playback: entrance animations, looping idles, or one-off effects. State machines reference timelines as animation states.",
  ["L0_primitives"])

c("Fundamentals", "What is Rive's mesh deformation?",
  "Vector shapes can be subdivided into a mesh grid, then bones control grid vertices. Enables smooth bending/stretching beyond simple rotation. Think Puppet Warp but real-time.",
  ["L0_primitives"])

c("Fundamentals", "What runtime platforms does Rive support?",
  "Web (WASM/JS), iOS, Android, Flutter, React Native, Unity, Unreal Engine, WebGL/Canvas. The <code>.riv</code> file is platform-agnostic; runtimes render it natively on each platform.",
  ["L0_primitives"])

# === RIVE CORE OPERATIONS ===

c("CoreOps", "How do you load a Rive file on the web?",
  "<code>const rive = new rive.Rive({ src: \"animation.riv\", canvas: canvasElement, autoplay: true, stateMachines: \"StateMachine1\" });</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you set a state machine input value?",
  "<code>const inputs = rive.stateMachineInputs(\"StateMachine1\");<br>const hoverInput = inputs.find(i =&gt; i.name === \"isHovered\");<br>hoverInput.value = true;</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you fire a trigger input?",
  "<code>const trigger = inputs.find(i =&gt; i.name === \"explode\");<br>trigger.fire();</code> — triggers are momentary (fire once, auto-reset). Unlike bools which hold state.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a state machine transition?",
  "In Rive Editor: Select a state, drag a transition arrow to another state. Set condition: <code>isHovered == true</code> OR <code>state Value &gt; 0.5</code>. Can mix multiple conditions with AND/OR.",
  ["L1_mechanics"])

c("CoreOps", "How do you blend between animations in Rive?",
  "State machines handle cross-fading automatically. Configure blend duration on each transition edge. Mixer layers can blend multiple animations simultaneously (e.g., running legs + waving arms).",
  ["L1_mechanics"])

c("CoreOps", "How do you nest artboards in Rive?",
  "Drag one artboard onto another to create a nested artboard instance. Changes to the source artboard propagate to all instances. Use for reusable components (buttons, icons, characters).",
  ["L1_mechanics"])

c("CoreOps", "How do you use constraints in Rive?",
  "IK constraints: bone follows a target. Distance constraints: limit how far bones can stretch. Transform constraints: copy position/rotation from another bone. Used for limbs, mechanical rigs.",
  ["L1_mechanics"])

c("CoreOps", "How do you export a Rive file?",
  "File -&gt; Export -&gt; .riv file. The file contains all artboards and state machines. No additional asset files needed — vectors are embedded, not rasterized.",
  ["L1_mechanics"])

c("CoreOps", "How do you listen for Rive events in code?",
  "<code>rive.on(\"statechange\", (event) =&gt; { console.log(event.data) })</code>. Available events: <code>load</code>, <code>play</code>, <code>pause</code>, <code>stop</code>, <code>loop</code>, <code>statechange</code>. State machine events carry state name and data.",
  ["L1_mechanics"])

c("CoreOps", "How do you play a specific timeline from code?",
  "<code>rive.play(\"timelineName\")</code> or <code>rive.play([\"timeline1\", \"timeline2\"])</code>. Without state machine, you control timelines directly.",
  ["L1_mechanics"])

c("CoreOps", "How do you set number input values programmatically?",
  "<code>input.value = 0.75;</code> — normalized values (0 to 1) are typical. Can be mapped to scroll progress, mouse position, slider values, or any continuous input.",
  ["L1_mechanics"])

# === RIVE PATTERNS ===

c("Patterns", "What is the hover/interactive button pattern?",
  "Create idle and hover animation states. Use a boolean input <code>isHovered</code>. Add transition from idle to hover when <code>isHovered == true</code>, and back when false. Wire JS <code>mouseenter/mouseleave</code> to set the input.",
  ["L2_composition"])

c("Patterns", "What is the scroll-driven animation pattern?",
  "Use a number input (e.g., <code>scrollProgress</code>). In the timeline animation, set keys at 0% and 100%. Map JS scroll position to 0-1: <code>scrollInput.value = window.scrollY / maxScroll</code>.",
  ["L2_composition"])

c("Patterns", "What is the character animation mixing pattern?",
  "Use multiple timeline layers: base idle on one layer, arm wave on another. The Rive Mixer blends them. State machines control which layers are active. Enables dynamic character behaviors without creating separate animations for every combination.",
  ["L2_composition"])

c("Patterns", "What is the data-binding pattern for Rive?",
  "Expose number inputs for all data-driven properties. In code, whenever your data changes, set the corresponding inputs. Rive interpolates to new animation states smoothly. Think reactive animation.",
  ["L2_composition"])

c("Patterns", "What is the nested component pattern?",
  "Build small, reusable Rive components (button, toggle, loader) as separate artboards. Nest them into larger compositions. Each nested instance can have its own state machine running independently.",
  ["L2_composition"])

c("Patterns", "What is the multi-state toggle pattern?",
  "Three+ states: off -&gt; mid -&gt; on. Transitions based on a number input (0, 0.5, 1) or sequential trigger presses. State machine with conditions for each threshold.",
  ["L2_composition"])

# === RIVE GOTCHAS ===

c("Gotchas", "Why isn't my state machine transition triggering?",
  "Check that the input type matches (bool/number/trigger). Triggers must be <code>.fire()</code>'d, not set to true. Boolean conditions use <code>==</code>, not assignment. Check transition direction (one-way arrows).",
  ["L4_diagnosis"])

c("Gotchas", "Why does my Rive animation look blurry?",
  "Rive renders at the canvas resolution. Ensure the canvas size matches its display size (device pixel ratio): <code>canvas.width = canvas.clientWidth * devicePixelRatio</code>. Rive is vector-based and should be crisp at any scale.",
  ["L4_diagnosis"])

c("Gotchas", "What causes Rive WASM loading failures?",
  "The <code>.wasm</code> file must be served with the correct MIME type (<code>application/wasm</code>). Configure your server/CDN. The JS runtime throws a descriptive error if WASM fails to instantiate.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my listener not fire on a nested element?",
  "Listeners must be attached at the correct hierarchy level. A listener on a group fires for all children. A listener on a specific shape only fires for that shape. Check the listener's target in the Rive Editor.",
  ["L4_diagnosis"])

c("Gotchas", "How do you handle Rive memory in long-running SPAs?",
  "Call <code>rive.cleanup()</code> or <code>rive.destroy()</code> before removing the canvas. Rive allocates WASM memory that must be explicitly freed. Orphaned runtimes cause memory leaks.",
  ["L4_diagnosis"])

# === RIVE EXPERT ===

c("Expert", "How do you optimize Rive file size?",
  "Minimize keyframe count (remove redundant keys), consolidate shapes, use looping state machines instead of long linear timelines, and enable <code>compress</code> in export. A complex interactive character can be under 50KB.",
  ["L3_design"])

c("Expert", "When should you use Rive vs a CSS/JS animation?",
  "Rive: complex vector animations with interactivity, character animation, state machines. CSS/JS: simple transitions, layout animations, accessibility-critical UI. Rive excels at illustration-quality interactivity.",
  ["L5_opinion"])

c("Expert", "What is the Rive Text feature?",
  "Text runs (strings with shared styling) that can be animated and driven by state machines. Text content can be changed at runtime. Use for animated typography, dynamic labels.",
  ["L6_innovation"])

c("Expert", "How do you integrate Rive with React?",
  "Use <code>@rive-app/react-canvas</code> or <code>@rive-app/canvas</code>: <code>&lt;RiveComponent src=\"file.riv\" stateMachines=\"SM\" /&gt;</code>. Pass a ref to call <code>riveComponent.rive</code> for programmatic input control.",
  ["L3_design"])

c("Expert", "What is the Rive runtime architecture?",
  "Core loop: load <code>.riv</code> -&gt; decode binary format -&gt; build scene graph -&gt; advance state machines -&gt; evaluate animations -&gt; generate vertex data -&gt; render via GPU (WebGL/Metal/Vulkan). The <code>.riv</code> format is a custom binary with embedded vector paths and keyframe data.",
  ["L6_innovation"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
