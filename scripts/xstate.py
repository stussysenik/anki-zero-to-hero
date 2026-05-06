import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "XState"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Advanced":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Advanced-Concepts"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === XSTATE FUNDAMENTALS ===

c("Fundamentals", "What is XState?",
  "A JavaScript/TypeScript library for creating, interpreting, and executing finite state machines and statecharts. Based on the W3C SCXML specification. Brings explicit, visualizable state management to applications.",
  ["L0_primitives"])

c("Fundamentals", "What is a finite state machine?",
  "A mathematical model describing a system that can be in exactly one state at a time, with defined transitions between states triggered by events. <code>{ states, events, transitions, initial }</code>. No impossible states.",
  ["L0_primitives"])

c("Fundamentals", "What is a statechart?",
  "An extension of finite state machines by David Harel. Adds: hierarchy (nested states), orthogonality (parallel states), history (remembering previous state), guards (conditions), and actions (entry/exit/transition effects). XState implements statecharts.",
  ["L0_primitives"])

c("Fundamentals", "What are the 5 parts of an XState machine definition?",
  "<code>id</code>: machine identifier. <code>initial</code>: starting state. <code>states</code>: object of state definitions. <code>context</code>: extended state (data). <code>on</code>: top-level event handlers. Each state can have its own <code>on</code>, <code>entry</code>, <code>exit</code> actions.",
  ["L0_primitives"])

c("Fundamentals", "What is context in XState?",
  "Extended state — data that the machine holds beyond its current state node. <code>context: { count: 0, items: [] }</code>. Updated via <code>assign</code> actions. Distinct from finite state — context can be any value while finite state is one of a defined set.",
  ["L0_primitives"])

c("Fundamentals", "What is an event in XState?",
  "A named message sent to the machine that triggers transitions. <code>send('TOGGLE')</code> or <code>send({ type: 'UPDATE', value: 42 })</code>. Events can carry data. The machine evaluates which transition matches the event.",
  ["L0_primitives"])

c("Fundamentals", "What is a guard in XState?",
  "A condition that must be true for a transition to occur: <code>on: { CLICK: [{ target: 'loading', guard: 'isValid' }, { target: 'error' }] }</code>. Guards are pure functions returning boolean. Multiple transitions for the same event — first matching guard wins.",
  ["L0_primitives"])

c("Fundamentals", "What are actions in XState?",
  "Side effects that happen on state entry, exit, or during transitions. Three types: <code>entry</code> (on entering state), <code>exit</code> (on leaving state), and transition actions. <code>assign</code> is the most common action — it updates <code>context</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is <code>useMachine</code> in @xstate/react?",
  "<code>const [state, send] = useMachine(machine)</code>. <code>state</code>: current snapshot (<code>.value</code>, <code>.context</code>, <code>.matches()</code>). <code>send</code>: dispatches events to the machine. Component re-renders when state changes.",
  ["L0_primitives"])

c("Fundamentals", "How does the XState visualizer help?",
  "XState's visualizer (stately.ai/viz) renders machine definitions as interactive diagrams. You can click states, follow transitions, see which states are reachable. Helps verify 'are any impossible states reachable?' before writing code.",
  ["L0_primitives"])

# === XSTATE CORE OPERATIONS ===

c("CoreOps", "How do you define a simple toggle machine?",
  "<code>import { createMachine } from 'xstate';<br>const toggleMachine = createMachine({<br>  id: 'toggle',<br>  initial: 'inactive',<br>  states: {<br>    inactive: { on: { TOGGLE: 'active' } },<br>    active: { on: { TOGGLE: 'inactive' } }<br>  }<br>});</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you use <code>assign</code> to update context?",
  "<code>import { assign } from 'xstate';<br>const counterMachine = createMachine({<br>  context: { count: 0 },<br>  on: {<br>    INCREMENT: { actions: assign({ count: (ctx) =&gt; ctx.count + 1 }) }<br>  }<br>});</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you add entry and exit actions?",
  "<code>active: {<br>  entry: 'startTimer',<br>  exit: 'stopTimer',<br>  on: { PAUSE: 'paused' }<br>}</code>. Actions are referenced by string name and implemented with <code>actions</code> config.",
  ["L1_mechanics"])

c("CoreOps", "How do you use state.matches()?",
  "<code>if (state.matches('loading')) return &lt;Spinner /&gt;;<br>if (state.matches({ active: 'editing' })) return &lt;Editor /&gt;;</code>. <code>.matches()</code> checks if the machine is in a state or nested state path.",
  ["L1_mechanics"])

c("CoreOps", "How do you nest states (hierarchy)?",
  "<code>states: {<br>  idle: {<br>    initial: 'still',<br>    states: {<br>      still: { on: { MOVE: 'walking' } },<br>      walking: { on: { STOP: 'still' } }<br>    }<br>  }<br>}</code>. <code>state.matches({ idle: 'walking' })</code>. Nested states inherit parent transitions.",
  ["L1_mechanics"])

c("CoreOps", "How do you create parallel states?",
  "<code>states: {<br>  active: {<br>    type: 'parallel',<br>    states: {<br>      audio: { initial: 'muted', states: { ... } },<br>      display: { initial: 'dark', states: { ... } }<br>    }<br>  }<br>}</code>. Both <code>audio</code> and <code>display</code> are active simultaneously.",
  ["L1_mechanics"])

c("CoreOps", "How do you invoke a promise/service?",
  "<code>loading: {<br>  invoke: {<br>    src: (ctx, event) =&gt; fetch('/api'),<br>    onDone: { target: 'success', actions: assign({ data: (_, e) =&gt; e.data }) },<br>    onError: 'failure'<br>  }<br>}</code>. The machine waits for the promise resolution/error.",
  ["L1_mechanics"])

c("CoreOps", "How do you use spawn to create actors?",
  "<code>spawn(someMachine, 'child1')</code> creates a child actor. Communicate via <code>sendParent</code>. Used for managing subtasks, parallel workers, or child machines. The parent can <code>send</code> to spawned actors.",
  ["L2_composition"])

c("CoreOps", "How do you create a guard condition?",
  "<code>on: {<br>  SUBMIT: [<br>    { target: 'processing', guard: 'isFormValid' },<br>    { target: 'error' }<br>  ]<br>},<br>guards: { isFormValid: (ctx) =&gt; ctx.name.length &gt; 0 }</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you use XState with React?",
  "<code>import { useMachine } from '@xstate/react';<br>const [state, send] = useMachine(myMachine);<br>return &lt;button onClick={() =&gt; send('CLICK')}&gt;{state.context.count}&lt;/button&gt;;</code>",
  ["L1_mechanics"])

# === ADVANCED CONCEPTS ===

c("Advanced", "What is an actor in XState v5?",
  "Everything is an actor: machines, promises, callbacks, observables. Actors have their own lifecycle, can receive/send messages. <code>createActor(machine).start()</code>. The actor model unifies state machines, services, and effects into one concept.",
  ["L3_design"])

c("Advanced", "What is the difference between XState v4 and v5?",
  "v5: everything is an actor. No more <code>interpret()</code> — use <code>createActor()</code>. Actor logic (machine, promise, transition function) is separate from running instances. Better TypeScript inference. <code>setup()</code> for configuration instead of <code>createMachine()</code>.",
  ["L3_design"])

c("Advanced", "What is <code>setup()</code> in XState v5?",
  "Configures a machine with typed actions, guards, actors: <code>setup({ types: ..., actions: { ... }, guards: { ... }, actors: { ... } }).createMachine({ ... })</code>. Separates implementation from machine definition. Better TypeScript inference.",
  ["L3_design"])

c("Advanced", "What is history state?",
  "<code>hist: { type: 'history' }</code> — remembers the last active child state. <code>deep: { type: 'history', history: 'deep' }</code> — remembers deeply nested state. Useful for 'restore previous state' patterns like tabs or wizards.",
  ["L3_design"])

c("Advanced", "What is delayed transitions (<code>after</code>)?",
  "<code>idle: { after: { 5000: 'timeout' } }</code> — transitions after 5 seconds of inactivity. Cancelled when leaving the state. Can use variables: <code>after: { someDelay: 'timedOut' }</code> with contextual delay values.",
  ["L2_composition"])

# === PATTERNS ===

c("Patterns", "What is the 'make impossible states impossible' pattern?",
  "Use state machines to prevent invalid states. Instead of <code>{ isLoading, data, error }</code> (8 possible combos, many invalid), define states: <code>idle | loading | success | error</code>. Only valid states exist. No more 'loading AND error' bugs.",
  ["L3_design"])

c("Patterns", "What is the wizard/flow pattern?",
  "Linear state progression with optional steps: <code>states: { step1, step2, step3, confirm }</code>. <code>on: { NEXT: 'step2', BACK: 'step1' }</code>. Each step can validate before allowing <code>NEXT</code>. Perfect for onboarding, checkout, forms.",
  ["L2_composition"])

c("Patterns", "What is the actor-based data fetching pattern?",
  "Spawn a child 'fetcher' machine for each data request. Parent sends <code>FETCH</code>, child handles loading/error/success, sends result back via <code>sendParent</code>. Encapsulates fetch lifecycle in a reusable machine.",
  ["L3_design"])

c("Patterns", "What is the parent-child machine communication pattern?",
  "Parent spawns child: <code>spawn(childMachine)</code>. Child communicates via <code>sendParent({ type: 'DONE', data })</code>. Parent receives as event and handles. Clean separation — child machines don't know about parents; parents don't know child internals.",
  ["L3_design"])

# === GOTCHAS ===

c("Gotchas", "Why does my machine not transition on an event?",
  "Check: 1) Is the event name exactly matching (case-sensitive)? 2) Is the event being sent (<code>send('EVENT')</code>)? 3) Is the transition defined in the CURRENT state or parent? 4) Is the guard blocking it? Add console logging to guard functions.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>assign</code> not work in transition actions?",
  "In v4, <code>actions</code> on transitions can include <code>assign</code>. But entry/exit actions can't use <code>assign</code> in v4 — use <code>invoke</code> or <code>always</code> instead. In v5, <code>assign</code> is more flexible.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my context type widen or become <code>any</code>?",
  "XState uses the context type from <code>createMachine</code>'s initial context. If you don't type the context explicitly, it infers from the initial value. Always type your context: <code>createMachine&lt;Context, Event&gt;(...)</code> or use <code>setup()</code>.",
  ["L4_diagnosis"])

c("Gotchas", "What happens to event listeners when a machine stops?",
  "When you stop a machine (<code>actor.stop()</code>), spawned children are stopped automatically. But external subscriptions (DOM listeners, timers) are NOT cleaned up automatically. Use <code>exit</code> actions or <code>onDone</code> handlers to clean up.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>state.context</code> reference not update?",
  "State objects are immutable snapshots. Each <code>.context</code> is a new reference on change. Don't mutate <code>state.context</code> directly — use <code>assign</code>. If using React, ensure you're destructuring <code>state</code> from the hook, not storing a stale reference.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "How do you test an XState machine?",
  "<code>import { createTestModel } from '@xstate/test';<br>const testModel = createTestModel(machine);<br>testModel.getPaths().forEach((path) =&gt; { path.test({ states, events }); });</code>. Generates test paths covering all states and transitions automatically. Statechart-based testing.",
  ["L6_innovation"])

c("Expert", "What is SCXML compliance in XState?",
  "XState v5 aims for full SCXML (W3C State Chart XML) compliance. This means XState machines can serialize to/from SCXML, enabling interoperability with other statechart tools and specifications.",
  ["L6_innovation"])

c("Expert", "How do you use XState for backend workflows?",
  "XState runs in Node.js without React. Define machines for order processing, user onboarding, CI/CD pipelines. Persist state to a database: <code>actor.getPersistedState()</code> and <code>createActor(machine, { state: restoredState })</code>. Long-running state machines.",
  ["L6_innovation"])

c("Expert", "When should you use XState vs simpler state management?",
  "XState: complex workflows, many possible states, need explicit visual model, safety-critical UI (forms, payments, auth). Simpler (useState, useReducer, Zustand): simple boolean toggles, basic counters, CRUD lists. XState shines when you're asking 'wait, can the user be in state X while Y is happening?'",
  ["L5_opinion"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
