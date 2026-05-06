import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Zustand"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Middleware":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Middleware"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === ZUSTAND FUNDAMENTALS ===

c("Fundamentals", "What is Zustand?",
  "A small, fast, scalable state management library for React. Based on hooks and simplified flux principles. No boilerplate, no providers, no context. Stores are plain hooks created with <code>create()</code>.",
  ["L0_primitives"])

c("Fundamentals", "How is Zustand different from Redux?",
  "Zustand: no providers, no reducers, no actions/dispatch, no middleware boilerplate. Just a store hook. Much less code (~1KB vs Redux's larger bundle). Better for simpler to medium-complexity apps. Redux: better for large teams with established patterns.",
  ["L0_primitives"])

c("Fundamentals", "How is Zustand different from React Context?",
  "Zustand: no provider wrapping, no unnecessary re-renders on any state change (selective subscriptions). Context: requires provider in the tree, re-renders all consumers when any part of context changes (unless using split contexts). Zustand scales better for high-frequency updates.",
  ["L0_primitives"])

c("Fundamentals", "What is the basic structure of a Zustand store?",
  "<code>import { create } from 'zustand';<br>const useStore = create((set) =&gt; ({<br>  count: 0,<br>  increment: () =&gt; set((state) =&gt; ({ count: state.count + 1 })),<br>  reset: () =&gt; set({ count: 0 })<br>}));</code>",
  ["L0_primitives"])

c("Fundamentals", "What are selectors in Zustand?",
  "Functions that pick specific slices of state: <code>const count = useStore((state) =&gt; state.count)</code>. The component ONLY re-renders when <code>count</code> changes — not when other state fields change. Enables fine-grained subscriptions.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>set</code> function in Zustand?",
  "The function passed to <code>create</code>'s callback. Mutates state: <code>set({ count: 10 })</code> (replaces). <code>set((state) =&gt; ({ count: state.count + 1 }))</code> (updates based on previous state). Can shallow-merge or replace entirely.",
  ["L0_primitives"])

c("Fundamentals", "What is <code>get</code> in Zustand?",
  "The second argument to create's callback. Retrieves current state without subscribing: <code>const state = get()</code>. Use inside actions to read state without triggering re-renders. Not a hook — direct state access.",
  ["L0_primitives"])

c("Fundamentals", "Can Zustand be used outside React?",
  "Yes. Subscribe directly: <code>const unsub = useStore.subscribe((state) =&gt; console.log(state))</code>. Get state: <code>useStore.getState()</code>. Set state: <code>useStore.setState({ key: val })</code>. Zustand stores are vanilla JS objects — React integration is just the subscribe hook.",
  ["L0_primitives"])

# === ZUSTAND CORE OPERATIONS ===

c("CoreOps", "How do you create a store?",
  "<code>import { create } from 'zustand';<br>const useStore = create((set, get) =&gt; ({<br>  bears: 0,<br>  increase: () =&gt; set((state) =&gt; ({ bears: state.bears + 1 })),<br>  removeAll: () =&gt; set({ bears: 0 }),<br>}));</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you use a store in a React component?",
  "<code>const bears = useStore((state) =&gt; state.bears);</code> — subscribe to <code>bears</code> only. <code>const { bears, increase } = useStore();</code> — subscribe to everything (re-renders on any change, usually avoid).",
  ["L1_mechanics"])

c("CoreOps", "How do you update nested state?",
  "<code>set((state) =&gt; ({<br>  user: { ...state.user, name: 'Alice' }<br>}))</code>. Or use <code>immer</code> middleware: <code>set((state) =&gt; { state.user.name = 'Alice' })</code> — mutable syntax, immutable result.",
  ["L1_mechanics"])

c("CoreOps", "How do you reset a store to initial state?",
  "Store the initial state separately: <code>const initialState = { bears: 0 }</code>. Then <code>reset: () =&gt; set(initialState)</code>. Or use <code>get()</code> to reset individual fields.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a store with TypeScript?",
  "<code>interface BearState { bears: number; increase: () =&gt; void; }<br>const useStore = create&lt;BearState&gt;((set) =&gt; ({ ... }));</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you subscribe to state changes outside React?",
  "<code>const unsub = useStore.subscribe(<br>  (state) =&gt; state.bears,<br>  (bears, prevBears) =&gt; console.log(bears, prevBears)<br>);</code>. Returns an unsubscribe function.",
  ["L1_mechanics"])

c("CoreOps", "How do you access state outside React without subscribing?",
  "<code>const bears = useStore.getState().bears;</code> — snapshots current state. Use in event handlers, callbacks, or non-React code where you don't want re-renders.",
  ["L1_mechanics"])

c("CoreOps", "How do you use <code>setState</code> directly (outside hooks)?",
  "<code>useStore.setState({ bears: 5 })</code> — equivalent to calling <code>set</code> inside the store. <code>useStore.setState((state) =&gt; ({ bears: state.bears + 1 }))</code>. Useful in non-React code, tests, or utils.",
  ["L1_mechanics"])

# === MIDDLEWARE ===

c("Middleware", "What is the <code>immer</code> middleware in Zustand?",
  "Enables writing mutable update logic: <code>import { immer } from 'zustand/middleware/immer';<br>const useStore = create(immer((set) =&gt; ({<br>  nested: { deep: { count: 0 } },<br>  increment: () =&gt; set((state) =&gt; { state.nested.deep.count += 1 })<br>})));</code> — no manual spread needed.",
  ["L2_composition"])

c("Middleware", "What is the <code>persist</code> middleware?",
  "Persists state to <code>localStorage</code> (or other storage): <code>import { persist } from 'zustand/middleware';<br>const useStore = create(persist((set) =&gt; ({ ... }), { name: 'my-store' }));</code>. State survives page reloads.",
  ["L2_composition"])

c("Middleware", "What is the <code>devtools</code> middleware?",
  "Connects to Redux DevTools browser extension: <code>import { devtools } from 'zustand/middleware';<br>const useStore = create(devtools((set) =&gt; ({ ... }), { name: 'MyStore' }));</code>. Time-travel debugging for Zustand stores.",
  ["L2_composition"])

c("Middleware", "How do you compose multiple middleware?",
  "Nest them: <code>create(devtools(persist(immer((set) =&gt; ({ ... })), { name: 'store' })))</code>. Order: innermost is applied first (usually immer first, then persist/devtools around it).",
  ["L2_composition"])

c("Middleware", "What is <code>subscribeWithSelector</code> middleware?",
  "Allows subscribing with a selector: <code>useStore.subscribe((s) =&gt; s.bears, callback)</code>. Without it, <code>.subscribe</code> fires on any change. With it, fires only when the selected value changes.",
  ["L2_composition"])

# === PATTERNS ===

c("Patterns", "What is the slice pattern?",
  "Organize store logic into separate functions: <code>const createBearSlice = (set) =&gt; ({ bears: 0, addBear: () =&gt; set(s =&gt; ({ bears: s.bears + 1 })) });<br>const createFishSlice = (set) =&gt; ({ fishes: 0, addFish: () =&gt; ... });<br>const useStore = create((...args) =&gt; ({ ...createBearSlice(...args), ...createFishSlice(...args) }));</code>= Keep stores modular and testable.",
  ["L3_design"])

c("Patterns", "What is the action-in-store pattern?",
  "Define actions inside the store closure: <code>create((set, get) =&gt; ({ ... }))</code>. Actions can <code>get()</code> other state and <code>set()</code> updates. Functions alongside state — no separate action files. This is the idiomatic Zustand pattern.",
  ["L2_composition"])

c("Patterns", "What is the transient update pattern (no re-render)?",
  "Use <code>get()</code> inside an action instead of the hook: <code>doSomething: () =&gt; { const { count } = get(); fetch('/api', { body: count }) }</code>. Reads state without subscribing the component.",
  ["L3_design"])

c("Patterns", "What is the async action pattern?",
  "<code>fetchUsers: async () =&gt; {<br>  set({ loading: true });<br>  const users = await api.getUsers();<br>  set({ users, loading: false });<br>}</code>. Actions can be async — just <code>set</code> before and after the await.",
  ["L2_composition"])

c("Patterns", "What is the derived state pattern (computed values)?",
  "Create selectors that compute values: <code>const total = useStore((s) =&gt; s.items.reduce((sum, i) =&gt; sum + i.price, 0))</code>. Re-computed whenever items change. For expensive derivations, memoize with <code>useMemo</code> or <code>shallow</code>.",
  ["L2_composition"])

# === GOTCHAS ===

c("Gotchas", "Why does my component re-render when unrelated state changes?",
  "You're subscribing to the whole store: <code>const state = useStore()</code>. Use selectors: <code>const bears = useStore((s) =&gt; s.bears)</code>. The component only re-renders when <code>bears</code> changes.",
  ["L4_diagnosis"])

c("Gotchas", "Why does Zustand's <code>set</code> merge shallowly?",
  "<code>set({ count: 5 })</code> replaces <code>count</code> but keeps other top-level keys. <code>set({ nested: { ...nested, key: val } })</code> manual deep merge is required. Or use immer middleware for automatic deep updates.",
  ["L4_diagnosis"])

c("Gotchas", "Why do selectors cause infinite loops or stale values?",
  "If a selector returns a new object/array every time (by reference), Zustand thinks state changed and re-renders infinitely. Use <code>shallow</code> comparison: <code>useStore(selector, shallow)</code>. Or return primitives from selectors.",
  ["L4_diagnosis"])

c("Gotchas", "How do you test a Zustand store?",
  "Reset store between tests: <code>useStore.setState(initialState)</code>. Test actions by calling them and checking <code>useStore.getState()</code>. No provider wrapping needed — stores are just functions.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>useStore.getState()</code> return stale data inside a closure?",
  "<code>getState()</code> always returns the latest state. But if you destructure: <code>const { count } = useStore.getState();</code> — <code>count</code> is a snapshot. Call <code>getState()</code> again to get the latest value.",
  ["L4_diagnosis"])

c("Gotchas", "What is the 'store is not a function' error?",
  "<code>create</code> returns a hook. Hooks can only be called inside React components or other hooks. Outside React, use <code>store.getState()</code> and <code>store.setState()</code>.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "How do you share state between multiple stores?",
  "Store A can call <code>useStoreB.getState()</code> or <code>useStoreB.subscribe()</code>. Or use a root store that composes slices (slice pattern). Or create a <code>syncedStore</code> that subscribes to another store and mirrors its state.",
  ["L6_innovation"])

c("Expert", "What is Zustand v5's new API?",
  "v5 (in development): <code>create</code> replaced with <code>createStore</code> (vanilla) and <code>useStore</code> (React hook). Cleaner separation. React Server Components support. No breaking changes for most users — <code>create</code> is still supported.",
  ["L6_innovation"])

c("Expert", "How do you use Zustand with React Server Components?",
  "Server Components can't use hooks. Use Zustand stores on the client boundary (<code>'use client'</code>). Fetch data in server components, pass as initial props to client components, hydrate Zustand stores in <code>useEffect</code> or during initialization.",
  ["L3_design"])

c("Expert", "What is <code>useShallow</code> in Zustand?",
  "A comparison function: <code>import { useShallow } from 'zustand/react/shallow'</code>. <code>const { bears, fishes } = useStore(useShallow((s) =&gt; ({ bears: s.bears, fishes: s.fishes })));</code>. Only re-renders when values actually change (shallow comparison), unlike object reference comparison.",
  ["L3_design"])

c("Expert", "When should you use Zustand vs Context vs Jotai?",
  "Zustand: external, centralized store for app-wide state, outside React tree. Jotai: atomic, bottom-up, component-level state with derived atoms. Context: simple values that change rarely (theme, locale). Zustand for global, Jotai for granular, Context for simple.",
  ["L5_opinion"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
