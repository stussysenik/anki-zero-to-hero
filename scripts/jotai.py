import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Jotai"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Derived":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Derived-Atoms"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === JOTAI FUNDAMENTALS ===

c("Fundamentals", "What is Jotai?",
  "A primitive and flexible state management library for React. Based on 'atoms' — the smallest units of state. Atoms can be composed, derived, and shared. Bottom-up approach: state lives close to where it's used.",
  ["L0_primitives"])

c("Fundamentals", "What is an atom in Jotai?",
  "The fundamental unit of state. Created with <code>atom(initialValue)</code>. A writable primitive. Read/write with hooks: <code>const [value, setValue] = useAtom(myAtom)</code>. Atoms are independent — updating one doesn't affect others.",
  ["L0_primitives"])

c("Fundamentals", "How is Jotai different from Zustand?",
  "Jotai: atomic, bottom-up — each piece of state is its own atom. Zustand: store-based, top-down — one or a few stores. Jotai atoms auto-depend on each other (Reactive). Zustand uses explicit selectors. Jotai feels like a reactive spreadsheet; Zustand feels like a Redux store.",
  ["L0_primitives"])

c("Fundamentals", "How is Jotai different from Recoil?",
  "Jotai is inspired by Recoil but smaller, simpler, and maintained. Both use atoms. Jotai: ~3KB, no string keys, atoms that derive async state natively, no <code>RecoilRoot</code> setup complexity. Recoil is effectively unmaintained (Meta abandoned it).",
  ["L0_primitives"])

c("Fundamentals", "What is <code>useAtom</code>?",
  "<code>const [value, setValue] = useAtom(myAtom)</code>. Like <code>useState</code> but with atoms. <code>value</code> is the current state. <code>setValue</code> updates it (can pass a value or updater function). Component re-renders when the atom changes.",
  ["L0_primitives"])

c("Fundamentals", "What is a derived atom?",
  "An atom whose value depends on other atoms. <code>const doubledAtom = atom((get) =&gt; get(countAtom) * 2)</code>. Read-only by default. When <code>countAtom</code> changes, <code>doubledAtom</code> automatically recomputes. Reactive dependency tracking.",
  ["L0_primitives"])

c("Fundamentals", "What is a writable derived atom?",
  "A derived atom that can also be written to: <code>const priceAtom = atom((get) =&gt; get(baseAtom) * 2, (get, set, newPrice) =&gt; set(baseAtom, newPrice / 2))</code>. Read and write are separate functions. Write can set other atoms.",
  ["L0_primitives"])

c("Fundamentals", "What is <code>useAtomValue</code> vs <code>useSetAtom</code>?",
  "<code>useAtomValue(atom)</code>: read only — doesn't need <code>setValue</code>. <code>useSetAtom(atom)</code>: write only — doesn't subscribe to value changes (no re-render on value change, only exposes the setter). Optimize re-renders by reading only what you need.",
  ["L0_primitives"])

c("Fundamentals", "Does Jotai need a Provider?",
  "No Provider required. Atoms work without any wrapping. However, <code>Provider</code> component scopes atom state to a subtree. Without Provider, atoms share a default store. With Provider, child atoms get isolated state.",
  ["L0_primitives"])

# === JOTAI CORE OPERATIONS ===

c("CoreOps", "How do you create a simple atom?",
  "<code>import { atom } from 'jotai';<br>const countAtom = atom(0);</code>. Use: <code>const [count, setCount] = useAtom(countAtom);</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you update an atom value?",
  "<code>setCount(5)</code> — direct value. <code>setCount((prev) =&gt; prev + 1)</code> — updater function. <code>setCount((prev) =&gt; { ...; return newValue; })</code> — complex logic.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a read-only derived atom?",
  "<code>const totalAtom = atom((get) =&gt; {<br>  const items = get(itemsAtom);<br>  return items.reduce((sum, i) =&gt; sum + i.price, 0);<br>});</code>. Read: <code>const total = useAtomValue(totalAtom);</code>. Auto-recomputed when <code>itemsAtom</code> changes.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a writable derived atom?",
  "<code>const proxyAtom = atom(<br>  (get) =&gt; get(baseAtom),<br>  (get, set, newValue) =&gt; { set(baseAtom, transform(newValue)); }<br>);</code>",
  ["L1_mechanics"])

c("CoreOps", "How do you read an atom value without subscribing?",
  "In event handlers/callbacks, use <code>const get = useStore().get;</code>: <code>get(countAtom)</code>. Or outside React: <code>import { getDefaultStore } from 'jotai'; const val = getDefaultStore().get(myAtom);</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you set an atom outside React?",
  "<code>import { getDefaultStore } from 'jotai';<br>const store = getDefaultStore();<br>store.set(countAtom, 42);</code>. Works in event handlers, WebSocket callbacks, timers.",
  ["L1_mechanics"])

c("CoreOps", "How do you create an async atom?",
  "<code>const userAtom = atom(async () =&gt; {<br>  const response = await fetch('/api/user');<br>  return response.json();<br>});</code>. Use with <code>React.Suspense</code> for loading states. Or use <code>loadable</code> utility.",
  ["L1_mechanics"])

c("CoreOps", "How do you handle pending/error states for async atoms?",
  "Use <code>jotai/utils</code>'s <code>loadable</code>: <code>const loadableAtom = loadable(asyncAtom);<br>const value = useAtomValue(loadableAtom);<br>if (value.state === 'loading') return &lt;Spinner /&gt;;<br>if (value.state === 'hasError') return &lt;Error /&gt;;<br>return &lt;Data data={value.data} /&gt;;</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you subscribe to atom changes?",
  "<code>const store = getDefaultStore();<br>const unsub = store.sub(countAtom, () =&gt; console.log('changed'));</code>. <code>unsub()</code> to stop. Programmatic subscription outside React components.",
  ["L1_mechanics"])

c("CoreOps", "How do you create an atom family?",
  "<code>import { atomFamily } from 'jotai/utils';<br>const userAtom = atomFamily((id) =&gt; atom(async () =&gt; fetchUser(id)));</code>. Each <code>userAtom(1)</code> creates a unique memoized atom. Great for per-item state (tabs, items, users).",
  ["L1_mechanics"])

# === DERIVED ATOMS ===

c("Derived", "What is the <code>get</code> function in derived atoms?",
  "Reads the current value of another atom and subscribes to its changes. <code>atom((get) =&gt; get(countAtom) * 2)</code>. This creates a reactive dependency — when <code>countAtom</code> changes, this atom recomputes.",
  ["L1_mechanics"])

c("Derived", "How do you combine multiple atoms?",
  "<code>const fullNameAtom = atom((get) =&gt; `${get(firstNameAtom)} ${get(lastNameAtom)}`)</code>. Or: <code>const combinedAtom = atom((get) =&gt; ({ a: get(atomA), b: get(atomB) }))</code>. Only recomputes when depended atoms change.",
  ["L2_composition"])

c("Derived", "What is the <code>splitAtom</code> utility?",
  "Splits a list atom into individual atoms per item: <code>const itemAtomsAtom = splitAtom(itemsAtom)</code>. Each <code>itemAtomsAtom[i]</code> is a writable atom representing that item. Update individually without re-rendering the whole list.",
  ["L2_composition"])

c("Derived", "What is the <code>selectAtom</code> utility?",
  "Creates a derived atom that only re-renders when a selected subset changes: <code>const nameAtom = selectAtom(userAtom, (user) =&gt; user.name)</code>. Even if <code>userAtom</code> changes, <code>nameAtom</code> only re-renders when <code>name</code> actually differs.",
  ["L2_composition"])

c("Derived", "How do on-mount and lifecycle work for atoms?",
  "Use <code>atom.onMount</code>: <code>const websocketAtom = atom(null);<br>websocketAtom.onMount = (setAtom) =&gt; {<br>  const ws = new WebSocket(...);<br>  ws.onmessage = (e) =&gt; setAtom(JSON.parse(e.data));<br>  return () =&gt; ws.close(); // cleanup on unmount<br>};</code>. Side effects tied to atom lifecycle.",
  ["L2_composition"])

# === PATTERNS ===

c("Patterns", "What is the atomic state pattern?",
  "Keep state in the smallest possible atoms. Instead of <code>atom({ name, email, preferences })</code>, use three atoms: <code>nameAtom</code>, <code>emailAtom</code>, <code>preferencesAtom</code>. Components reading <code>nameAtom</code> don't re-render on email changes.",
  ["L3_design"])

c("Patterns", "What is the derived form state pattern?",
  "Form fields as atoms, derived computed state: <code>const isFormValidAtom = atom((get) =&gt; get(nameAtom).length &gt; 0 &amp;&amp; get(emailAtom).includes('@'))</code>. Submit button subscribes to <code>isFormValidAtom</code> only.",
  ["L2_composition"])

c("Patterns", "What is the <code>atomWithStorage</code> pattern?",
  "Sync atom to localStorage: <code>import { atomWithStorage } from 'jotai/utils';<br>const darkModeAtom = atomWithStorage('darkMode', false);</code>. Automatically persists and restores. Works with sessionStorage, AsyncStorage, custom stores.",
  ["L2_composition"])

c("Patterns", "What is the <code>atomWithReset</code> pattern?",
  "Atom with a reset method: <code>import { atomWithReset } from 'jotai/utils';<br>const formAtom = atomWithReset({ name: '', email: '' });</code>. <code>setForm(useResetAtom())</code> resets to initial value. Great for forms that need clearing.",
  ["L2_composition"])

c("Patterns", "What is the scope/Provider pattern?",
  "Wrap parts of tree with <code>&lt;Provider&gt;</code> to isolate atom state: <code>&lt;Provider&gt;&lt;Editor /&gt;&lt;/Provider&gt;</code>. Editor gets its own atom instances. Two Editors in different Providers have independent state. Default store is global.",
  ["L3_design"])

# === GOTCHAS ===

c("Gotchas", "Why does my derived atom recompute unnecessarily?",
  "Derived atoms recompute when any depended atom changes. If you read a large object atom just to access one field, the derived recomputes on any change to that object. Use <code>selectAtom</code> or split into smaller atoms.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>useAtomValue</code> still re-render?",
  "<code>useAtomValue</code> subscribes to the atom. If the atom's value changes (even to the same value by reference), the component re-renders. To prevent re-renders on same-value updates, use <code>useAtomValue(atom, { delay: 0 })</code> or ensure stable references.",
  ["L4_diagnosis"])

c("Gotchas", "Why do atoms inside <code>atomFamily</code> not get garbage collected?",
  "By default, <code>atomFamily</code> caches all created atoms indefinitely. For cleanup, pass a <code>shouldRemove</code> function: <code>atomFamily(param, null, (createdAt, param) =&gt; Date.now() - createdAt &gt; 60000)</code> removes atoms older than 1 minute.",
  ["L4_diagnosis"])

c("Gotchas", "What's the difference between <code>atom()</code> and <code>atom(null)</code>?",
  "<code>atom(null)</code> creates an atom with initial value <code>null</code>. <code>atom()</code> with no argument requires an initial value to be provided at first write — reading before the first write returns undefined. Usually provide an initial value.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my async atom not retry on error?",
  "Async atoms cache errors. After an error, the atom stays in error state until dependencies change. To retry, write to a dependency (e.g., touch a <code>requestIdAtom</code>) to trigger recomputation. Or use <code>atomWithRefresh</code> for manual retry.",
  ["L4_diagnosis"])

c("Gotchas", "Can I call <code>useAtom</code> conditionally?",
  "No — hooks cannot be called conditionally. But you can create atoms conditionally: <code>const priceAtom = useMemo(() =&gt; isUSD ? atom(get(...)) : atom(get(...)), [isUSD])</code>. Atoms created at render time are fine; hooks placed conditionally are not.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "How do you debug Jotai atoms?",
  "Use <code>jotai-devtools</code> (npm package). Shows atom dependency graph, current values, change history. Or use <code>useReducerAtom</code> for Redux DevTools integration. <code>debugLabel</code>: <code>atom(0).debugLabel = 'count'</code> for readable names.",
  ["L6_innovation"])

c("Expert", "How does Jotai handle batching of updates?",
  "Jotai batches atom writes automatically. Multiple <code>set()</code> calls in a synchronous block result in a single re-render. In React 18 with automatic batching, even async updates are batched. Use <code>unstable_batchedUpdates</code> for manual batching if needed.",
  ["L3_design"])

c("Expert", "What is the Jotai store API for external state management?",
  "<code>import { createStore } from 'jotai';<br>const myStore = createStore();<br>myStore.get(atom); myStore.set(atom, value); myStore.sub(atom, callback);</code>. Support for multiple isolated stores, testing, and non-React usage.",
  ["L6_innovation"])

c("Expert", "How do you integrate Jotai with React Query or tRPC?",
  "Create atoms that wrap query results: <code>atomWithQuery</code> from <code>jotai-tanstack-query</code> or manually: <code>atom(async () =&gt; queryClient.fetchQuery(...))</code>. Benefits: Query cache still manages dedup/staleness; atoms provide reactive access.",
  ["L5_opinion"])

c("Expert", "When should you choose Jotai over Zustand or Redux?",
  "Jotai: granular, reactive dependencies, many independent pieces of state, derived/computed state is central, React-only. Zustand: simpler global store, works outside React. Redux: large teams, normalization, middleware-heavy. Jotai shines with interdependent atomic state.",
  ["L5_opinion"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
