import genanki, random
R = lambda: random.randrange(1 << 30, 1 << 31)

model = genanki.Model(R(), "React Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}\n<hr id=answer>\n{{Back}}"}],
    css=""".card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px;
                text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; }
           .front { font-weight: bold; margin-top: 60px; }
           .back  { font-size: 20px; text-align: left; padding: 10px 30px; }
           code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244;
                       padding: 2px 6px; border-radius: 4px; font-size: 18px; }
           hr { border-color: #45475a; }""")

decks = {
    "Fundamentals": genanki.Deck(R(), "React::Zero2Hero::01-Fundamentals"),
    "Hooks": genanki.Deck(R(), "React::Zero2Hero::02-Hooks"),
    "HooksInternals": genanki.Deck(R(), "React::Zero2Hero::03-Hooks-Internals"),
    "Patterns": genanki.Deck(R(), "React::Zero2Hero::04-Component-Patterns"),
    "Fiber": genanki.Deck(R(), "React::Zero2Hero::05-Fiber-Reconciliation"),
    "Concurrent": genanki.Deck(R(), "React::Zero2Hero::06-Concurrent-React"),
    "ServerComponents": genanki.Deck(R(), "React::Zero2Hero::07-Server-Components"),
    "Performance": genanki.Deck(R(), "React::Zero2Hero::08-Performance"),
    "Routing": genanki.Deck(R(), "React::Zero2Hero::09-Routing-NextJS"),
    "Testing": genanki.Deck(R(), "React::Zero2Hero::10-Testing"),
    "Gotchas": genanki.Deck(R(), "React::Zero2Hero::11-Gotchas"),
    "Expert": genanki.Deck(R(), "React::Zero2Hero::12-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ===== 01-FUNDAMENTALS =====
c("Fundamentals", "What is the Virtual DOM?",
  "A lightweight JS representation of the real DOM. React creates a tree of plain objects describing what the UI should look like, diffs against the previous tree, and applies minimal DOM updates.",
  ["L0_primitives"])

c("Fundamentals", "What is JSX?",
  "A syntax extension that compiles to <code>React.createElement</code> calls. With React 17+ jsx-runtime, compiles to <code>_jsx(type, props)</code>. Not HTML — JavaScript with XML-like syntax.",
  ["L0_primitives"])

c("Fundamentals", "What is the difference between a component and an element?",
  "Component: a function or class that returns React elements. Element: a plain object describing a DOM node or component instance — <code>{ type, props, key, ref }</code>. Elements are immutable; components can have state.",
  ["L0_primitives"])

c("Fundamentals", "What are props?",
  "Read-only inputs passed from parent to child. <code>&lt;Child name={value} /&gt;</code>. In function components: <code>function Child({ name })</code>. Never mutate props — they are frozen in dev mode.",
  ["L0_primitives"])

c("Fundamentals", "What is state in React?",
  "Mutable data managed by a component that persists across renders. Changed via <code>useState</code> / <code>useReducer</code> / <code>this.setState</code>. State changes trigger re-renders. Unlike props, state is private to the component.",
  ["L0_primitives"])

c("Fundamentals", "Why does React use <code>className</code> instead of <code>class</code>?",
  "<code>class</code> is a reserved JS keyword. JSX compiles to JS function calls where <code>class</code> would be a syntax error. <code>htmlFor</code> (not <code>for</code>) for the same reason.",
  ["L0_primitives"])

c("Fundamentals", "What is the difference between controlled and uncontrolled components?",
  "Controlled: form data handled by React state — <code>&lt;input value={val} onChange={setVal} /&gt;</code>. Uncontrolled: DOM itself holds the value — <code>&lt;input ref={inputRef} /&gt;</code>. Controlled = single source of truth.",
  ["L1_mechanics"])

c("Fundamentals", "What does <code>ReactDOM.createRoot</code> do?",
  "Creates a concurrent root (React 18+). <code>const root = createRoot(domNode); root.render(&lt;App /&gt;)</code>. Enables automatic batching, Suspense, transitions. Replaces the legacy <code>ReactDOM.render</code>.",
  ["L1_mechanics"])

c("Fundamentals", "What is the component lifecycle?",
  "Mount: component created and inserted into DOM. Update: re-render due to props/state/context change. Unmount: removed from DOM. In hooks: <code>useEffect(() => {}, [])</code> for mount; cleanup function for unmount.",
  ["L1_mechanics"])

c("Fundamentals", "What is reconciliation?",
  "React's O(n) diffing algorithm comparing old and new element trees. Decides which DOM nodes to create, update, or delete. Keys help preserve identity across reorders. Different element types destroy the old subtree.",
  ["L1_mechanics"])

c("Fundamentals", "What is the <code>key</code> prop and why does it matter?",
  "A stable identifier for list elements. Without keys, React uses index-based matching — reordering causes unnecessary DOM mutations. With keys, React matches by identity. Must be unique among siblings, not globally.",
  ["L1_mechanics"])

c("Fundamentals", "What is <code>React.StrictMode</code>?",
  "A dev-only wrapper that double-invokes renders, state updaters, and effect cleanups to detect impure code. Does NOT affect production. Wraps: <code>&lt;StrictMode&gt;&lt;App /&gt;&lt;/StrictMode&gt;</code>.",
  ["L1_mechanics"])

c("Fundamentals", "How does React's synthetic event system work?",
  "React wraps native events in <code>SyntheticEvent</code> — cross-browser wrapper. Uses event delegation: a single listener at the root captures all events. React then dispatches to the appropriate fiber based on the target. Events pool in React 16 (reused); removed in 17.",
  ["L1_mechanics"])

# ===== 02-HOOKS =====
c("Hooks", "What are the two rules of hooks?",
  "1) Only call hooks at the TOP LEVEL — never inside conditions, loops, or nested functions. 2) Only call hooks from React function components or custom hooks — never from regular JS functions.",
  ["L0_primitives"])

c("Hooks", "What does <code>useState</code> return?",
  "A tuple: <code>[currentState, setStateFunction]</code>. <code>setState(newValue)</code> triggers re-render. <code>setState(prev =&gt; next)</code> for updates based on previous value. The initial value is only used on the FIRST render.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useEffect</code> do and what are its cleanup and deps?",
  "<code>useEffect(fn, deps)</code>: runs <code>fn</code> AFTER render and paint. Returns cleanup function that runs BEFORE next effect or unmount. <code>deps</code>: effect re-runs when any dep changes. <code>[]</code>: runs once on mount. No deps arg: runs every render.",
  ["L1_mechanics"])

c("Hooks", "When should you use <code>useLayoutEffect</code> instead of <code>useEffect</code>?",
  "<code>useLayoutEffect</code> fires synchronously AFTER DOM mutations but BEFORE browser paint. Use when you need to measure DOM and apply changes before paint (avoid flicker). <code>useEffect</code> fires AFTER paint — user sees initial render first.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useRef</code> do and when should you use it vs state?",
  "Returns a mutable <code>{ current: initialValue }</code> object that persists across renders. Mutating <code>ref.current</code> does NOT trigger re-render. Use for: DOM references, mutable instance variables, previous value tracking. Use state for values that affect UI.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useMemo</code> do?",
  "<code>useMemo(factory, deps)</code> — returns cached result of <code>factory()</code>. Recomputes only when deps change. For expensive computations. Not a guarantee — React may recompute for memory reasons.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useCallback</code> do?",
  "<code>useCallback(fn, deps)</code> — returns a memoized version of <code>fn</code>. Actually calls <code>useMemo(() =&gt; fn, deps)</code> internally. Use when passing callbacks to memoized children to prevent unnecessary re-renders.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useReducer</code> do and when is it better than <code>useState</code>?",
  "<code>const [state, dispatch] = useReducer(reducer, initialState)</code>. Better for complex state logic with multiple sub-values or when next state depends on previous. Enables predictable state transitions. <code>useState</code> is actually implemented as <code>useReducer</code> internally.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useContext</code> do?",
  "<code>const value = useContext(MyContext)</code> — reads the current context value from the nearest <code>&lt;MyContext.Provider&gt;</code> ancestor. Component re-renders when context value changes. Context value is compared via <code>Object.is</code>.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useImperativeHandle</code> do?",
  "<code>useImperativeHandle(ref, () =&gt; ({ focus, reset }), deps)</code> — customizes the instance value exposed to parent when using <code>ref</code>. Used with <code>forwardRef</code>. Lets parent call child methods without exposing the entire DOM node.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useDebugValue</code> do?",
  "<code>useDebugValue(value, formatter)</code> — displays a label for a custom hook in React DevTools. Only runs in development. Useful for complex hooks to show their current state in DevTools.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useId</code> do?",
  "<code>const id = useId()</code> — generates a unique, stable ID string. For accessibility (linking label+input), ARIA attributes. Stable across server and client rendering (hydration). NOT for keys in lists.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useDeferredValue</code> do?",
  "<code>const deferred = useDeferredValue(value)</code> — returns a deferred version of <code>value</code> that lags behind urgent updates. React renders with old value first, then re-renders with new value at lower priority. Use to keep UI responsive during expensive updates.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useTransition</code> do?",
  "<code>const [isPending, startTransition] = useTransition()</code>. Wraps a state update in <code>startTransition(() =&gt; setState(x))</code> to mark it as non-urgent. <code>isPending</code> is true while transition runs. Urgent updates interrupt transitions.",
  ["L1_mechanics"])

c("Hooks", "What does <code>useSyncExternalStore</code> do?",
  "<code>useSyncExternalStore(subscribe, getSnapshot)</code> — subscribes to an external store with tear prevention. Added in React 18 to solve concurrent rendering tearing (inconsistent state). Forces synchronous re-render when store changes during concurrent render.",
  ["L1_mechanics"])

# ===== 03-HOOKS-INTERNALS =====
c("HooksInternals", "How are hooks stored internally in React?",
  "As a SINGLY LINKED LIST on <code>fiber.memoizedState</code>. Each hook node has: <code>memoizedState</code>, <code>baseState</code>, <code>queue</code>, <code>next</code>. During render, React walks the list in order — this is WHY hook call order must be consistent.",
  ["L2_composition"])

c("HooksInternals", "Why can't hooks be called inside conditions or loops?",
  "Because hooks are identified by their POSITION in the linked list on <code>fiber.memoizedState</code>. If order changes between renders, the wrong hook's state is read — e.g., <code>useState</code> reads from <code>useEffect</code>'s slot. Causes corrupted state and crashes.",
  ["L3_design"])

c("HooksInternals", "Why does React 18 batch multiple <code>setState</code> calls automatically?",
  "<code>dispatchSetState</code> calls <code>enqueueUpdate</code> (queues to fiber's update queue) + <code>scheduleUpdateOnFiber</code>. <code>ensureRootIsScheduled</code> debounces: first call creates a task; subsequent calls see a task already scheduled and just merge lanes. All queued updates processed in one render.",
  ["L3_design"])

c("HooksInternals", "How does <code>useEffect</code> timing work at the fiber level?",
  "During <code>commitBeforeMutationEffects</code>: React schedules passive effects via <code>scheduleCallback(NormalPriority, flushPassiveEffects)</code>. <code>flushPassiveEffects</code> runs ALL destroy (cleanup) then ALL create — after browser paint. Guarantees useEffect does NOT block paint.",
  ["L3_design"])

c("HooksInternals", "How does <code>useLayoutEffect</code> differ from <code>useEffect</code> internally?",
  "Both create effect nodes with the same <code>pushEffect</code> mechanism. Difference: <code>tag</code> is <code>HookLayout</code> vs <code>HookPassive</code>. <code>commitLayoutEffects</code> processes Layout effects sync during commit (before paint). <code>flushPassiveEffects</code> processes Passive effects async (after paint).",
  ["L3_design"])

c("HooksInternals", "What is the eager bailout optimization in <code>useState</code>?",
  "If no other updates are pending and the new value is <code>Object.is</code> equal to the current value, React skips scheduling a re-render entirely. The <code>eagerState</code> field on the update object stores the pre-computed next state; compared before enqueueing.",
  ["L3_design"])

c("HooksInternals", "How does context propagation work under the hood?",
  "When Provider value changes (<code>!Object.is(prev, next)</code>), <code>propagateContextChange</code> walks the fiber subtree marking fibers with the changed context lane. <code>readContext</code> (called by <code>useContext</code>) walks UP <code>fiber.return</code> to find nearest Provider. Context is compared, not deeply diffed.",
  ["L3_design"])

# ===== 04-COMPONENT-PATTERNS =====
c("Patterns", "What is a Higher-Order Component (HOC)?",
  "A function that takes a component and returns a new component. <code>const Enhanced = withAuth(MyComponent)</code>. Used for cross-cutting concerns (auth, logging, theming). Hooks have largely replaced HOCs for new code.",
  ["L2_composition"])

c("Patterns", "What is a render prop?",
  "A prop whose value is a function that returns React elements. <code>&lt;Mouse render={({x,y}) =&gt; &lt;Cursor x={x} y={y} /&gt;} /&gt;</code>. Shares logic between components. Hooks also replace most render prop use cases.",
  ["L2_composition"])

c("Patterns", "What is the compound components pattern?",
  "Multiple components that share implicit state via context. <code>&lt;Select&gt;&lt;Select.Option value='a' /&gt;&lt;/Select&gt;</code>. <code>Select</code> provides context; <code>Option</code> consumes it. No prop drilling. Used by Radix UI, Mantine, React Aria.",
  ["L2_composition"])

c("Patterns", "What is the custom hook pattern?",
  "A function starting with <code>use</code> that calls other hooks. <code>function useWindowSize() { const [size, setSize] = useState(); useEffect(() =&gt; { ... }, []); return size; }</code>. Extracts reusable stateful logic without changing component hierarchy.",
  ["L2_composition"])

c("Patterns", "How does <code>forwardRef</code> work?",
  "<code>const FancyInput = forwardRef((props, ref) =&gt; &lt;input ref={ref} /&gt;)</code>. Passes the ref from parent to a child DOM node or component. Necessary because <code>ref</code> is not a prop — React handles it specially.",
  ["L1_mechanics"])

c("Patterns", "How do you implement a generic list component (render prop vs HOC vs hooks)?",
  "Modern: custom hook <code>usePagination(data, pageSize)</code> returns <code>{ items, hasNext, nextPage }</code>. Component consumes the hook. Older: <code>&lt;PaginatedList data={x} renderItem={(item) =&gt; &lt;Item /&gt;} /&gt;</code> (render prop). Hooks = cleaner.",
  ["L2_composition"])

# ===== 05-FIBER-RECONCILIATION =====
c("Fiber", "What is a React Fiber?",
  "A JS object representing a unit of work. Properties: <code>tag</code> (FunctionComponent=0, HostComponent=5, etc.), <code>child</code>/<code>return</code>/<code>sibling</code> (tree pointers), <code>alternate</code> (work-in-progress counterpart), <code>memoizedState</code>/<code>memoizedProps</code>, <code>flags</code> (side effects bitfield).",
  ["L0_primitives"])

c("Fiber", "What do the <code>child</code>, <code>return</code>, and <code>sibling</code> fiber pointers form?",
  "A left-child right-sibling tree — NOT a binary tree. <code>child</code> = first child. <code>return</code> = parent. <code>sibling</code> = next sibling (linked list). This enables depth-first traversal during reconciliation.",
  ["L2_composition"])

c("Fiber", "What is the <code>alternate</code> fiber?",
  "React uses double-buffering: each fiber has an <code>alternate</code> pointing to its counterpart in the other tree. The current tree (on-screen) and work-in-progress tree swap on commit. This allows React to work on a new tree while the old one is still displayed.",
  ["L2_composition"])

c("Fiber", "What are the two phases of the work loop?",
  "Phase 1 — <code>beginWork</code>: depth-first. Determines if fiber needs updating, calls <code>renderWithHooks</code> for functions, diffProps for HostComponents. Returns next child or null.<br>Phase 2 — <code>completeWork</code>: bubbles up when subtree exhausted. Creates/updates DOM nodes, bubbles <code>subtreeFlags</code> up.",
  ["L2_composition"])

c("Fiber", "What are React lanes?",
  "A 31-bit bitfield encoding priority. <code>SyncLane</code> (1, highest), <code>InputContinuousLane</code> (user events), <code>DefaultLane</code> (normal setState), transition lanes (lower priority), <code>IdleLane</code>. <code>getHighestPriorityLane(lanes) = lanes &amp; -lanes</code> extracts the lowest set bit.",
  ["L2_composition"])

c("Fiber", "What are the three sub-phases of the commit phase?",
  "1) <code>commitBeforeMutationEffects</code>: runs <code>getSnapshotBeforeUpdate</code>, schedules passive effects.<br>2) <code>commitMutationEffects</code>: performs DOM insert/update/delete, runs layout effect cleanups, <code>componentWillUnmount</code>.<br>3) <code>commitLayoutEffects</code>: runs layout effect setups, <code>componentDidMount/Update</code>.",
  ["L2_composition"])

c("Fiber", "How does React's diffing algorithm handle list reconciliation?",
  "First pass: iterate both old and new arrays, match by keys at same position. On mismatch: build Map from old fiber keys → old fibers. For each new child, lookup in Map. Matched = reuse fiber with updated props. Unmatched new = Placement. Remaining old = Deletion. <code>lastPlacedIndex</code> tracks position to minimize reorders.",
  ["L2_composition"])

c("Fiber", "What triggers a subtree bailout?",
  "<code>bailoutOnAlreadyFinishedWork</code>: checks <code>oldProps === newProps</code>, no child lanes matching current priority, and no <code>ForceClientRender</code> flag. If all true, clones child fibers and returns null — entire subtree skipped. <code>React.memo</code> adds shallow prop comparison check.",
  ["L3_design"])

c("Fiber", "Why are the render and commit phases separate?",
  "Render phase is pure computation — can be interrupted, paused, aborted. If React wrote to DOM during render and then got interrupted, the DOM would be left in an incomplete state. Commit phase is non-interruptible and atomically flips the <code>.current</code> pointer.",
  ["L3_design"])

c("Fiber", "What is the <code>flags</code> (formerly effectTag) bitfield on a fiber?",
  "Encodes side effects via bitwise OR: <code>Placement</code>=2 (insert DOM), <code>Update</code>=4 (update props), <code>Deletion</code>=8 (remove DOM), <code>ContentReset</code>=16. <code>subtreeFlags</code> accumulates all descendant flags — lets commit phase skip subtrees with no work.",
  ["L2_composition"])

# ===== 06-CONCURRENT-REACT =====
c("Concurrent", "What is time slicing in React?",
  "React yields to the browser after each fiber's work if the 5ms frame budget is exceeded. <code>shouldYield()</code> checks <code>performance.now() &gt;= deadline</code>. Uses <code>MessageChannel</code> for scheduling — fires sooner than <code>setTimeout</code> and doesn't interfere with <code>requestAnimationFrame</code>.",
  ["L2_composition"])

c("Concurrent", "How does Suspense work internally?",
  "A component throws a PROMISE during render. React catches it in <code>renderWithHooks</code>, walks up fiber tree to nearest <code>Suspense</code> fiber, attaches <code>.then(retry)</code> on the promise, and renders the fallback UI instead. When promise resolves, <code>retryTimedOutBoundary</code> triggers re-render with primary children.",
  ["L3_design"])

c("Concurrent", "How do transitions interact with urgent updates?",
  "Transition updates use low-priority lanes. If an urgent update (click, input, SyncLane) arrives during a transition render: React discards the work-in-progress tree (<code>prepareFreshStack</code>), re-renders at higher priority, commits it. Then the transition restarts from scratch with the new state.",
  ["L3_design"])

c("Concurrent", "What is tearing in concurrent rendering?",
  "React yields mid-render. If an external store updates during the yield, component A could see Store v1 while component B (rendered after yield) sees Store v2 — inconsistent UI. <code>useSyncExternalStore</code> prevents tearing by forcing a synchronous re-render when snapshot differs between render phases.",
  ["L4_diagnosis"])

c("Concurrent", "How does the React Scheduler prevent starvation?",
  "Each task has an <code>expirationTime = now + timeout</code>. Timeout varies by priority: ImmediatePriority=-1ms (always expired), UserBlocking=250ms, Normal=5000ms, Low=10000ms, Idle=max. When a task expires, it upgrades to synchronous priority and runs without yielding.",
  ["L3_design"])

c("Concurrent", "What is selective hydration? (React 18 SSR)",
  "React can hydrate parts of the page out of order. When a user clicks a not-yet-hydrated component: React pauses current hydration, hydrates the clicked component first (high priority), replays the event, then resumes hydrating the rest. <code>Suspense</code> boundaries define hydration boundaries.",
  ["L2_composition"])

c("Concurrent", "What does <code>useTransition</code> return and how does <code>isPending</code> work?",
  "Returns <code>[isPending, startTransition]</code>. <code>startTransition</code> wraps a state update at transition priority. <code>isPending</code> becomes <code>true</code> when a transition is in progress and returns <code>false</code> when the transition commit completes. React may render the old UI + loading indicator simultaneously.",
  ["L1_mechanics"])

# ===== 07-SERVER-COMPONENTS =====
c("ServerComponents", "What are React Server Components (RSC)?",
  "Components that render ONLY on the server — never sent as JS to the client. Can directly access databases, file systems, backend services. Cannot use hooks, state, effects, or browser APIs. Can be <code>async</code>. Client receives a serialized UI description.",
  ["L0_primitives"])

c("ServerComponents", 'What does the <code>"use client"</code> directive do?',
  "Marks a file as client-side code. Everything imported by it becomes client code. Placed at top before imports. Signals the bundler to create a client bundle entry point. Without it, the file is a server component by default (in Next.js App Router).",
  ["L1_mechanics"])

c("ServerComponents", 'What does the <code>"use server"</code> directive do?',
  "File-level: every export becomes a Server Action. Function-level: <code>async function submit() { 'use server'; ... }</code>. Creates an API endpoint — client calls it, function runs on server. Arguments serialized via React Flight protocol.",
  ["L1_mechanics"])

c("ServerComponents", "What is the RSC payload format?",
  "A streaming line-delimited format with chunk types: <code>M</code> (Module reference: client component), <code>J</code> (JSON tree with placeholders), <code>S</code> (Suspense boundary), <code>E</code> (Error). Placeholders like <code>$1</code> and <code>@1</code> reference previously parsed chunks. Serialized via <code>renderToReadableStream</code>.",
  ["L2_composition"])

c("ServerComponents", "Can you import a Server Component into a Client Component?",
  "NO. Importing a Server Component into a <code>'use client'</code> file would bundle its code (including secrets) into the client bundle. BUT you can PASS server components as CHILDREN to client components: <code>&lt;ClientComp&gt;&lt;ServerChild /&gt;&lt;/ClientComp&gt;</code>. Children rendered on server, passed as opaque elements.",
  ["L1_mechanics"])

c("ServerComponents", "How does RSC work with Suspense for streaming?",
  "<code>renderToPipeableStream</code>: sends shell (initial HTML + RSC payload), Suspense boundaries with pending data send fallback first. When data resolves: inline <code>&lt;script&gt;</code> tag updates the DOM with new content. Client uses <code>createFromFetch</code> to parse stream and Suspense retries show resolved content.",
  ["L2_composition"])

# ===== 08-PERFORMANCE =====
c("Performance", "What does <code>React.memo</code> do and when does it help?",
  "Wraps component: <code>const Memoized = React.memo(Component, areEqual?)</code>. Does shallow prop comparison before re-rendering. If props equal and no state/context changes, bails out. Helps when parent re-renders frequently but child props are referentially stable. Does NOT block context-triggered re-renders.",
  ["L1_mechanics"])

c("Performance", "What is code splitting and how do you implement it?",
  "<code>const LazyComp = React.lazy(() =&gt; import('./Heavy')); &lt;Suspense fallback={&lt;Spinner /&gt;}&gt;&lt;LazyComp /&gt;&lt;/Suspense&gt;</code>. Bundler splits at <code>import()</code> boundary. Component only loaded when rendered. Reduce initial bundle size.",
  ["L1_mechanics"])

c("Performance", "What causes an infinite re-render loop in React?",
  "1) <code>useEffect(() =&gt; setState(x+1), [x])</code> — effect changes its own dep. 2) <code>useEffect(() =&gt; setState(x+1))</code> — no deps = runs every render. 3) setState in render body (not in handler/effect). 4) Object/array in deps created inline: <code>[{ a: 1 }]</code> — new ref every render. 5) Context value is new object every render.",
  ["L4_diagnosis"])

c("Performance", "How does the Profiler API work?",
  "<code>&lt;Profiler id='Nav' onRender={callback}&gt;</code>. <code>callback(id, phase, actualDuration, baseDuration, startTime, commitTime, interactions)</code>. <code>actualDuration</code>: time spent rendering the committed update. <code>baseDuration</code>: worst-case estimate without memoization. Stripped in production.",
  ["L1_mechanics"])

c("Performance", "What are the most common memory leaks in React?",
  "1) Event listeners not removed in useEffect cleanup. 2) Intervals/timeouts not cleared. 3) Subscriptions/WebSockets not unsubscribed. 4) Stale refs holding large objects after unmount. 5) Detached DOM trees referenced by closures. Always return cleanup function from <code>useEffect</code> when setting up listeners.",
  ["L4_diagnosis"])

c("Performance", "When does <code>useMemo</code> actually harm performance?",
  "When the computation is cheaper than the comparison cost + memory overhead. Simple operations like <code>a + b</code> or accessing a property — <code>useMemo</code> adds overhead of storing/caching + <code>Object.is</code> on each dep. Only use for genuinely expensive computations (sorting large arrays, complex derivations).",
  ["L5_opinion"])

# ===== 09-ROUTING-NEXTJS =====
c("Routing", "What are the key differences between Next.js App Router and Pages Router?",
  "App Router (Next.js 13+): Server Components by default, file-based routing in <code>app/</code> dir, layouts that persist across navigations, streaming, React Suspense boundaries. Pages Router: <code>pages/</code> dir, getServerSideProps/getStaticProps, Client Components by default.",
  ["L0_primitives"])

c("Routing", "What rendering strategies does Next.js support?",
  "SSR (Server-Side Rendering): fresh data each request, <code>cache: 'no-store'</code>. SSG (Static Site Generation): built at build time, <code>generateStaticParams</code>. ISR (Incremental Static Regeneration): SSG with periodic revalidation via <code>next.revalidate</code>. CSR: client-only rendering with <code>'use client'</code>.",
  ["L1_mechanics"])

c("Routing", "How does server-side data fetching work in the App Router?",
  "Async Server Components: <code>async function Page() { const data = await fetch(url); return &lt;div&gt;{data}&lt;/div&gt;; }</code>. Next.js extends <code>fetch</code> with caching: <code>fetch(url, { cache: 'force-cache' })</code> (static), <code>cache: 'no-store'</code> (dynamic). <code>next: { revalidate: 60 }</code> for ISR.",
  ["L1_mechanics"])

c("Routing", "What are layouts in Next.js App Router?",
  "<code>layout.tsx</code> wraps child pages and persists across navigations. State is preserved. Nested layouts: each segment can have its own layout. <code>RootLayout</code> is required. Layouts receive <code>children</code> as a prop. Cannot access <code>searchParams</code> directly.",
  ["L1_mechanics"])

c("Routing", "What are loading and error boundaries in App Router?",
  "<code>loading.tsx</code>: shown while page/segment loads (Suspense fallback). <code>error.tsx</code>: error boundary — catches errors in child segments. Must be a Client Component. Receives <code>error</code> and <code>reset</code> props. <code>global-error.tsx</code> catches root layout errors.",
  ["L1_mechanics"])

c("Routing", "What are Server Actions in Next.js?",
  "Functions that run on the server, callable from Client Components. <code>async function create() { 'use server'; ... }</code>. Used for form submissions, data mutations. Can be called as <code>action</code> prop on <code>&lt;form&gt;</code> or programmatically via <code>startTransition</code>. Eliminates need for API routes in many cases.",
  ["L1_mechanics"])

c("Routing", "How does React Router v6 handle data loading?",
  "<code>loader</code> functions run BEFORE navigation, data available via <code>useLoaderData()</code>. <code>action</code> for form submissions (similar to loaders). <code>defer()</code> for streaming with <code>&lt;Await&gt;</code> + <code>Suspense</code>. <code>useFetcher()</code> for non-navigation data loading. Replaces <code>useEffect</code> + <code>useState</code> pattern.",
  ["L2_composition"])

c("Routing", "What is partial prerendering (PPR)?",
  "Next.js experimental: combines static and dynamic content in the same page. Static shell is prerendered at build time; dynamic holes stream in at request time. Configured via <code>experimental.ppr: true</code>. Uses <code>&lt;Suspense&gt;</code> boundaries to define dynamic holes.",
  ["L2_composition"])

# ===== 10-TESTING =====
c("Testing", "How do you test a component with React Testing Library?",
  "<code>render(&lt;MyComponent /&gt;); const el = screen.getByText('Submit'); fireEvent.click(el); expect(screen.getByText('Done')).toBeInTheDocument()</code>. Query from user perspective. Avoid testing implementation details (state, internal methods).",
  ["L1_mechanics"])

c("Testing", "How do you test a custom hook?",
  "<code>import { renderHook, act } from '@testing-library/react'; const { result } = renderHook(() =&gt; useCounter()); act(() =&gt; result.current.increment()); expect(result.current.count).toBe(1)</code>. <code>act()</code> wraps state updates to flush effects and ensure React has processed the update.",
  ["L1_mechanics"])

c("Testing", "How do you mock a module with a custom implementation?",
  "<code>jest.mock('./api', () =&gt; ({ fetchData: jest.fn().mockResolvedValue({ data: 'test' }) }))</code>. For dynamic mocks: <code>jest.mock('./api', () =&gt; ({ __esModule: true, default: jest.fn() }))</code>. Use <code>jest.requireActual</code> to partially mock.",
  ["L1_mechanics"])

c("Testing", "What are the query priority guidelines in Testing Library?",
  "1) <code>getByRole</code> (accessible, user-facing). 2) <code>getByLabelText</code> (form fields). 3) <code>getByPlaceholderText</code>. 4) <code>getByText</code>. 5) <code>getByDisplayValue</code>. LAST RESORT: <code>getByTestId</code>. This order mirrors how users find elements.",
  ["L2_composition"])

c("Testing", "How do you test async operations?",
  "<code>await screen.findByText('Loaded')</code> — waits for element to appear. <code>waitFor(() =&gt; expect(mockFn).toHaveBeenCalled())</code> — waits for assertion. <code>waitForElementToBeRemoved</code> — waits for element to disappear. All have default timeout of 1000ms (configurable).",
  ["L1_mechanics"])

# ===== 11-GOTCHAS =====
c("Gotchas", 'What is a stale closure in React hooks?',
  "An effect or callback captures a variable value from a specific render's scope and never updates. <code>useEffect(() =&gt; { const id = setInterval(() =&gt; console.log(count), 1000) }, [])</code> — <code>count</code> is always 0. Fix: use functional updater <code>setCount(c =&gt; c + 1)</code> or add count to deps.",
  ["L4_diagnosis"])

c("Gotchas", "Why do context consumers re-render more than expected?",
  "When context value changes, ALL consumers and ALL their children re-render (unless memoized). If you pass <code>value={{ x: 1 }}</code>, a NEW object is created every render, changing the context every time. Fix: <code>useMemo(() =&gt; ({ x: 1 }), [])</code> for the value, or split into multiple contexts.",
  ["L4_diagnosis"])

c("Gotchas", "Why can using array index as key cause bugs?",
  "If list order changes (add/remove/sort), indices shift. Items' identity is lost — React may update the wrong item's state. Delete item 0: item 1 becomes the new index 0, but keeps its old state. Always use stable, unique identifiers from your data as keys.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>useEffect</code> run twice in development?",
  "React 18 StrictMode double-invokes effects: setup → cleanup → setup. Detects missing cleanup functions. The cleanup runs between the two invocations — if your effect has side effects without cleanup, the double-invoke exposes the bug. Only in development.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>setState</code> not update the value immediately?",
  "<code>setCount(c + 1); console.log(count)</code> — <code>count</code> is still the old value. setState schedules a re-render; the current render's <code>count</code> variable doesn't change. Use <code>setCount(c =&gt; c + 1)</code> for dependent updates. The new value is available on the NEXT render.",
  ["L4_diagnosis"])

c("Gotchas", "Why are inline object/array/function props bad for <code>React.memo</code>?",
  "<code>&lt;MemoChild style={{ color: 'red' }} /&gt;</code> — a new object every render, so <code>React.memo</code>'s shallow comparison always fails. Child re-renders every time. Fix: extract to stable reference (<code>useMemo</code>, const outside component) or use <code>useCallback</code> for functions.",
  ["L4_diagnosis"])

c("Gotchas", "What causes the 'Can't perform a React state update on an unmounted component' warning?",
  "An async operation (fetch, timeout, promise) resolves after a component has unmounted. The callback calls <code>setState</code> on an unmounted component. Fix: use <code>AbortController</code> for fetch, or a ref-based <code>isMounted</code> check. React 18 mostly eliminates this warning for async updates.",
  ["L4_diagnosis"])

c("Gotchas", 'Why does <code>dangerouslySetInnerHTML</code> have that name?',
  "It bypasses React's XSS protection. <code>&lt;div dangerouslySetInnerHTML={{ __html: html }} /&gt;</code>. If <code>html</code> contains user input, it enables XSS attacks. The name and verbose API are INTENTIONAL — they make you think twice before using it. Always sanitize HTML with DOMPurify.",
  ["L4_diagnosis"])

# ===== 12-EXPERT =====
c("Expert", "How does React's Scheduler use MessageChannel?",
  "Creates a <code>MessageChannel</code>. Calls <code>port.postMessage(null)</code> to schedule a macrotask. The <code>port.onmessage</code> handler flushes the scheduler queue. Chosen over <code>setTimeout</code> because MessageChannel fires before setTimeout (no 4ms minimum delay) and doesn't interfere with rAF.",
  ["L6_innovation"])

c("Expert", "What is the React Forget compiler?",
  "An experimental auto-memoizing compiler. Statically analyzes components to determine what values they read, then automatically inserts <code>useMemo</code>/<code>useCallback</code> equivalents at compile time. Eliminates manual memoization. React 19+ adopted the compiler (React Compiler).",
  ["L6_innovation"])

c("Expert", "How do you build a custom React reconciler?",
  "Use the <code>react-reconciler</code> package: <code>const reconciler = ReactReconciler(hostConfig)</code>. <code>hostConfig</code> defines platform-specific operations: <code>createInstance</code>, <code>appendChild</code>, <code>commitUpdate</code>, <code>prepareUpdate</code>, etc. React DOM, React Native, Ink, React Three Fiber all use this API.",
  ["L6_innovation"])

c("Expert", "What is the <code>react-reconciler</code> host config?",
  "An object defining how React interacts with a host environment. Key methods: <code>createInstance(type, props)</code> — create a node. <code>createTextInstance(text)</code>. <code>appendChild/insertBefore/removeChild</code>. <code>prepareUpdate</code> — diff props. <code>commitUpdate</code> — apply diff. <code>supportsMutation</code>/<code>supportsPersistence</code> flags.",
  ["L6_innovation"])

c("Expert", "How does the Fast Refresh (HMR) mechanism work?",
  "React maintains a module-level signature. When a file changes, React hot-swaps the component implementation WITHOUT unmounting. Preserves state, hooks, and DOM. If the component's signature changed (different hooks order), falls back to full remount. Babel plugin injects signatures at compile time.",
  ["L6_innovation"])

c("Expert", "What is the event delegation architecture in React 17+?",
  "React 17+: attaches event listeners to the ROOT DOM node (not document). This allows multiple React versions on the same page. Events still bubble through the React fiber tree (not DOM tree) — especially important for Portals where the DOM position differs from the React tree position.",
  ["L6_innovation"])

c("Expert", "How do Portals work with React's event system?",
  "Portals render children into a different DOM container. BUT events bubble through the REACT TREE (fiber hierarchy), not the DOM tree. A click on a portal-rendered button bubbles to the portal's React parent, not the DOM parent. React's synthetic event system handles this routing.",
  ["L6_innovation"])

# ===== BUILD =====
for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

fn = "React_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(fn)
print(f"Built {len(decks)} decks with {len(C)} cards -> {fn}")

# VERIFICATION:
# import zipfile, sqlite3, json
# with zipfile.ZipFile("React_Zero_to_Hero.apkg") as z: z.extract("collection.anki2", "/tmp/")
# db = sqlite3.connect("/tmp/collection.anki2")
# n, c = db.execute("SELECT count(*) FROM notes").fetchone()[0], db.execute("SELECT count(*) FROM cards").fetchone()[0]
# print(f"Notes: {n}, Cards: {c}")
# assert n == c == len(C), f"Mismatch: {n} notes, {c} cards, {len(C)} defined"
