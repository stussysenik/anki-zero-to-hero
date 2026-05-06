import genanki, random
R = lambda: random.randrange(1 << 30, 1 << 31)
model = genanki.Model(R(), "JS/TS Q&A",
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
    "CoreJS": genanki.Deck(R(), "JS_TS::Zero2Hero::01-Core-JavaScript"),
    "Prototypes": genanki.Deck(R(), "JS_TS::Zero2Hero::02-Prototypes-Objects"),
    "Async": genanki.Deck(R(), "JS_TS::Zero2Hero::03-Async-Execution"),
    "Engine": genanki.Deck(R(), "JS_TS::Zero2Hero::04-Engine-Internals"),
    "Modules": genanki.Deck(R(), "JS_TS::Zero2Hero::05-Modules"),
    "Iterables": genanki.Deck(R(), "JS_TS::Zero2Hero::06-Iterables-Generators"),
    "Proxies": genanki.Deck(R(), "JS_TS::Zero2Hero::07-Proxies-Reflect"),
    "TSCore": genanki.Deck(R(), "JS_TS::Zero2Hero::08-TypeScript-Core"),
    "TSAdvanced": genanki.Deck(R(), "JS_TS::Zero2Hero::09-TypeScript-Advanced"),
    "DOM": genanki.Deck(R(), "JS_TS::Zero2Hero::10-DOM-Web-APIs"),
    "Patterns": genanki.Deck(R(), "JS_TS::Zero2Hero::11-Patterns-Meta"),
    "Expert": genanki.Deck(R(), "JS_TS::Zero2Hero::12-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ===== 01-CORE-JAVASCRIPT =====
c("CoreJS", "What are the 7 primitive types in JavaScript?",
  "<code>undefined</code>, <code>null</code>, <code>boolean</code>, <code>number</code>, <code>bigint</code>, <code>string</code>, <code>symbol</code>. Everything else (objects, arrays, functions, classes, Map, Set) is an object. Primitives are immutable and compared by value; objects by reference.",
  ["L0_primitives"])

c("CoreJS", "What is the difference between <code>null</code> and <code>undefined</code>?",
  "<code>undefined</code>: variable declared but not assigned, missing function return, missing object property. <code>null</code>: intentional absence of any object value, must be explicitly assigned. <code>typeof null === 'object'</code> (historical bug). <code>null == undefined</code> is true; <code>null === undefined</code> is false.",
  ["L0_primitives"])

c("CoreJS", "What is type coercion?",
  "JavaScript's automatic conversion between types. <code>'5' + 3</code> → <code>'53'</code> (number → string, concatenation). <code>'5' - 3</code> → <code>2</code> (string → number, subtraction). <code>+</code> prefers strings; <code>-</code>, <code>*</code>, <code>/</code>, <code>%</code> prefer numbers.",
  ["L0_primitives"])

c("CoreJS", "What is <code>==</code> vs <code>===</code>?",
  "<code>==</code> allows coercion (Abstract Equality). <code>===</code> checks both type AND value (Strict Equality). <code>0 == false</code> is true (number vs boolean coerced). <code>0 === false</code> is false (number vs boolean). Always use <code>===</code> unless you specifically want coercion.",
  ["L0_primitives"])

c("CoreJS", "What are the 8 falsy values?",
  "<code>false</code>, <code>0</code>, <code>-0</code>, <code>0n</code> (BigInt zero), <code>''</code> (empty string), <code>null</code>, <code>undefined</code>, <code>NaN</code>. Everything else is truthy — including <code>[]</code>, <code>{}</code>, <code>'false'</code>, <code>'0'</code>, <code>new Boolean(false)</code>.",
  ["L0_primitives"])

c("CoreJS", "Why is <code>NaN !== NaN</code>?",
  "IEEE 754 standard: NaN is not equal to itself by definition. <code>NaN === NaN</code> is false, <code>Object.is(NaN, NaN)</code> is true. <code>Number.isNaN(x)</code> checks only for NaN (no coercion). <code>isNaN(x)</code> coerces first — <code>isNaN('hello')</code> is true.",
  ["L1_mechanics"])

c("CoreJS", "What is the difference between <code>-0</code> and <code>+0</code>?",
  "<code>-0 === +0</code> is true. <code>Object.is(-0, +0)</code> is false. <code>1 / -0</code> → <code>-Infinity</code>. <code>1 / +0</code> → <code>Infinity</code>. <code>Math.sign(-0)</code> → -0. Division is the most reliable way to detect sign. <code>(-0).toString()</code> → '0'.",
  ["L1_mechanics"])

c("CoreJS", "What are the 4 <code>this</code> binding rules in order of precedence?",
  "1) <code>new</code> binding: <code>new Foo()</code> → <code>this</code> = new empty object. 2) Explicit: <code>.call()</code>, <code>.apply()</code>, <code>.bind()</code> → <code>this</code> = first argument. Hard binding (<code>.bind()</code>) is permanent. 3) Implicit: <code>obj.fn()</code> → <code>this</code> = <code>obj</code>. 4) Default: <code>fn()</code> → global/undefined.",
  ["L1_mechanics"])

c("CoreJS", "How do arrow functions handle <code>this</code> differently?",
  "Arrow functions have NO own <code>this</code>. <code>this</code> is lexically resolved from the enclosing non-arrow function. Binding rules (<code>call</code>, <code>apply</code>, <code>bind</code>) have NO effect on arrow functions. Also: no <code>.prototype</code>, no <code>[[Construct]]</code>, no <code>arguments</code> object.",
  ["L1_mechanics"])

c("CoreJS", "What is hoisting?",
  "<code>var</code> declarations are hoisted to top of function scope (initialized as <code>undefined</code>). <code>let</code>/<code>const</code> are hoisted to top of block scope but UNINITIALIZED (Temporal Dead Zone — accessing pre-declaration throws <code>ReferenceError</code>). <code>function</code> declarations: entire definition hoisted.",
  ["L1_mechanics"])

c("CoreJS", "What is closure?",
  "A function that retains access to its lexical scope even when executed outside that scope. Inner function captures variables from outer function's scope. Stored in heap (<code>Context</code> objects). Powers module pattern, partial application, data privacy before <code>#private</code> fields.",
  ["L1_mechanics"])

c("CoreJS", "What is the Temporal Dead Zone (TDZ)?",
  "The period between entering a scope and the actual declaration of a <code>let</code>/<code>const</code>/<code>class</code>. Accessing the variable during TDZ throws <code>ReferenceError</code>. <code>typeof x</code> in TDZ also throws (unlike <code>typeof</code> on undeclared variable which returns <code>'undefined'</code>). Also applies to <code>class</code> declarations.",
  ["L1_mechanics"])

c("CoreJS", "What is the difference between <code>var</code>, <code>let</code>, and <code>const</code>?",
  "<code>var</code>: function-scoped, hoisted (initialized undefined), reassignable, redeclarable. <code>let</code>: block-scoped, TDZ, reassignable, NOT redeclarable in same scope. <code>const</code>: block-scoped, TDZ, NOT reassignable, must be initialized. <code>const</code> reference is immutable but object contents are still mutable.",
  ["L0_primitives"])

c("CoreJS", "What does <code>Object.is()</code> do vs <code>===</code>?",
  "<code>Object.is(a, b)</code>: SameValue comparison. Differs from <code>===</code> in two cases: <code>Object.is(NaN, NaN)</code> → true (<code>===</code> → false), <code>Object.is(-0, +0)</code> → false (<code>===</code> → true). Otherwise identical. Used internally by <code>Map</code>/<code>Set</code> key equality.",
  ["L1_mechanics"])

# ===== 02-PROTOTYPES-OBJECTS =====
c("Prototypes", "What is the difference between <code>[[Prototype]]</code> and <code>.prototype</code>?",
  "<code>[[Prototype]]</code>: internal slot on EVERY object, accessed via <code>Object.getPrototypeOf(obj)</code>. <code>.prototype</code>: property ONLY on constructor functions. <code>new Foo()</code> sets the new object's <code>[[Prototype]]</code> to <code>Foo.prototype</code>. <code>instance.__proto__ === Constructor.prototype</code>.",
  ["L0_primitives"])

c("Prototypes", "How does prototypal inheritance work?",
  "When you access <code>obj.prop</code>, JS first looks on <code>obj</code> itself. If not found, it follows <code>[[Prototype]]</code> chain up to <code>Object.prototype</code> → <code>null</code>. Method lookups traverse the chain. Property ASSIGNMENT always happens on the object itself (never walks [[Prototype]] for sets).",
  ["L1_mechanics"])

c("Prototypes", "What is <code>Object.create(null)</code> used for?",
  "Creates an object with NO <code>[[Prototype]]</code> — pure dictionary. No inherited methods (<code>toString</code>, <code>hasOwnProperty</code>). Safe for storing user-provided keys that might collide with <code>Object.prototype</code> names (<code>'toString'</code>, <code>'__proto__'</code>). <code>Map</code> is the modern alternative.",
  ["L1_mechanics"])

c("Prototypes", "What are property descriptors?",
  "Each property has a descriptor:<br><code>Data</code>: <code>{ value, writable, enumerable, configurable }</code>. <code>Accessor</code>: <code>{ get, set, enumerable, configurable }</code>.<br><code>writable: false</code> → assignment fails silently (non-strict) or throws (strict).<br><code>configurable: false</code> → cannot delete, cannot change to accessor, cannot change flags (except writable true→false).",
  ["L1_mechanics"])

c("Prototypes", "What does <code>Object.defineProperty</code> do?",
  "<code>Object.defineProperty(obj, key, descriptor)</code> — defines a property with precise control over its behavior. Used to create non-enumerable, non-writable, non-configurable properties. Also creates getters/setters. Returns the object. <code>Object.defineProperties(obj, { key: descriptor })</code> for batch.",
  ["L1_mechanics"])

c("Prototypes", "How do private fields (<code>#field</code>) work internally?",
  "Uses a <code>WeakMap</code>-like mechanism. Each class has a hidden WeakMap per private field; instance is key, value is value. Truly private — no reflection, no <code>Proxy</code> trap override. <code>Object.keys</code>/<code>getOwnPropertyNames</code> don't see them. <code>#field in obj</code> checks existence (only within the defining class).",
  ["L2_composition"])

c("Prototypes", "What is the difference between <code>for...in</code>, <code>Object.keys</code>, and <code>Reflect.ownKeys</code>?",
  "<code>for...in</code>: own + inherited, enumerable only, string keys only. <code>Object.keys</code>: own only, enumerable only, string keys only. <code>Object.getOwnPropertyNames</code>: own only, ALL string keys. <code>Reflect.ownKeys</code>: own only, ALL keys (strings + symbols), enumerable + non-enumerable. The most complete enumeration.",
  ["L1_mechanics"])

c("Prototypes", "What is the difference between <code>Object.seal</code>, <code>Object.freeze</code>, and <code>Object.preventExtensions</code>?",
  "<code>preventExtensions</code>: no new properties. Can delete/modify existing.<br><code>seal</code>: preventExtensions + sets all existing props to <code>configurable: false</code>. Can modify values.<br><code>freeze</code>: seal + sets all data props to <code>writable: false</code>. NOTHING can change (shallow only). All irreversible.",
  ["L1_mechanics"])

# ===== 03-ASYNC-EXECUTION =====
c("Async", "Describe the exact order: macrotasks vs microtasks vs rendering.",
  "Each event loop tick: 1) Take ONE macrotask (setTimeout, I/O, event, MessageChannel), execute fully. 2) Drain ALL microtasks (Promise.then, queueMicrotask, MutationObserver) — run until queue empty, including microtasks added during drain. 3) Render if needed (rAF, style, layout, paint). 4) requestIdleCallback if time remains.",
  ["L2_composition"])

c("Async", "How does <code>async/await</code> desugar to promises and microtasks?",
  "<code>async function f() { const x = await g(); return x + 1; }</code> desugars to: <code>function f() { return Promise.resolve(g()).then(x =&gt; x + 1); }</code>. Each <code>await</code> splits the function; code after <code>await</code> runs as a microtask. Even <code>await 5</code> yields to microtask queue (via <code>Promise.resolve(5)</code>).",
  ["L1_mechanics"])

c("Async", "What is the difference between microtasks and macrotasks?",
  "Microtasks (Promise.then, queueMicrotask, MutationObserver): execute at the END of the current macrotask, before rendering. Macrotasks (setTimeout, setInterval, I/O, MessageChannel): execute one per event loop iteration. Microtasks can starve rendering if they keep spawning more microtasks.",
  ["L1_mechanics"])

c("Async", "What does <code>queueMicrotask(fn)</code> do?",
  "Schedules <code>fn</code> to the microtask queue (same queue as <code>Promise.then</code>). Executes after current synchronous code completes but BEFORE next macrotask. FIFO order within the microtask queue. The standard API — preferred over <code>Promise.resolve().then(fn)</code>.",
  ["L1_mechanics"])

c("Async", "How does <code>Promise.allSettled</code> differ from <code>Promise.all</code>?",
  "<code>all</code>: rejects on FIRST rejection (short-circuits). <code>allSettled</code>: waits for ALL to settle, returns <code>[{status:'fulfilled', value}, {status:'rejected', reason}]</code>. Never short-circuits. Use <code>allSettled</code> when you need results from all promises regardless of failures.",
  ["L1_mechanics"])

c("Async", "How does <code>Promise.any</code> differ from <code>Promise.race</code>?",
  "<code>any</code>: fulfills with FIRST fulfilled promise, rejects ONLY IF ALL reject (throws <code>AggregateError</code>). <code>race</code>: settles with FIRST to settle — whether fulfilled OR rejected. Use <code>any</code> for 'first success' pattern; <code>race</code> for timeout patterns.",
  ["L1_mechanics"])

c("Async", "What is the <code>AbortController</code> pattern?",
  "<code>const ac = new AbortController(); fetch(url, { signal: ac.signal })</code>. <code>ac.abort(reason)</code> cancels the fetch (throws <code>AbortError</code>). <code>signal.aborted</code> (boolean), <code>signal.reason</code> (abort reason). <code>AbortSignal.timeout(5000)</code> auto-aborts after 5s. <code>AbortSignal.any([signal1, signal2])</code> composes.",
  ["L2_composition"])

c("Async", 'What is a "floating promise" and why is it dangerous?',
  "Calling an async function without <code>await</code> or <code>.catch()</code>. <code>fetchData()</code> — the promise is created but errors are silently swallowed (unhandled rejection). In Node.js, unhandled rejections crash the process (since Node 15). Always <code>await</code> or chain <code>.catch()</code>.",
  ["L4_diagnosis"])

# ===== 04-ENGINE-INTERNALS =====
c("Engine", "What are hidden classes (Maps) in V8?",
  "V8 assigns each object a hidden class (Map) describing its shape: property names, types, and memory offsets. Adding properties in different orders creates DIFFERENT Maps. Objects with the same property-addition sequence share the same Map — enabling fast property access via known offsets.",
  ["L2_composition"])

c("Engine", "What is inline caching (IC) in V8?",
  "At property access sites (<code>obj.prop</code>), V8 stores a feedback vector recording the last Map seen and the property offset. Next access with the same Map: load directly from offset (fast path — monomorphic). Different Map: transitions to polymorphic (up to ~4 Maps). Too many Maps: megamorphic, falls back to slow hash-table lookup.",
  ["L2_composition"])

c("Engine", "Describe V8's compilation pipeline tiers.",
  "1) Ignition (interpreter): AST → bytecode, collects type feedback. 2) Sparkplug (baseline JIT): bytecode → machine code, no optimization, fast compile. 3) Maglev (mid-tier JIT): uses IC feedback for better code. 4) TurboFan (optimizing JIT): Sea-of-Nodes IR, speculative optimizations, deopt guards. Progression: Ignition → Sparkplug → Maglev → TurboFan.",
  ["L3_design"])

c("Engine", "What causes a V8 deoptimization?",
  "TurboFan makes speculative assumptions based on IC feedback. A deopt occurs when: type mismatch where IC said monomorphic; <code>arguments</code> object leaked into optimized function; <code>eval()</code>/<code>with</code> encountered; hidden class changed; out-of-bounds array on SMI-specialized code. Deopt means throw away optimized code, restart in interpreter.",
  ["L4_diagnosis"])

c("Engine", "What is a deopt loop?",
  "Code optimizes speculatively → deopts → warms up again → re-optimizes → deopts again. V8 gives up after a few rounds (disables optimization). Common cause: one function called with two very different object shapes, IC sees them alternating between calls. Never stabilizes.",
  ["L4_diagnosis"])

c("Engine", "What are V8's element kinds and why does ordering matter?",
  "Array storage types in a lattice: <code>PACKED_SMI</code> (fastest) → <code>PACKED_DOUBLE</code> → <code>PACKED</code> → <code>HOLEY_SMI</code> → <code>HOLEY_DOUBLE</code> → <code>HOLEY</code> → <code>DICTIONARY</code> (slowest). Transitions are one-way DOWN the lattice. <code>new Array(1000)</code> creates holey array — use <code>[]</code> + <code>.push()</code> or <code>.fill(0)</code> instead.",
  ["L4_diagnosis"])

c("Engine", "What is the holey array pitfall?",
  "Accessing <code>arr[outOfBounds]</code> returns <code>undefined</code> but doesn't store it — the index becomes a 'hole'. The array permanently transitions to HOLEY elements kind, which is slower: no vectorized ops, extra check per access. <code>new Array(N)</code>, <code>delete arr[i]</code>, and some <code>splice</code> operations create holes.",
  ["L4_diagnosis"])

c("Engine", "How does V8 garbage collection work?",
  "New space (young gen): scavenge (Cheney semi-space), pointer bump allocation, ~1MB. Old space: concurrent mark-sweep + mark-compact. Large object space: objects >128KB in their own pages. Incremental marking to reduce pause times. Orinoco GC since 2016: parallel scavenge, concurrent marking.",
  ["L3_design"])

c("Engine", "How do <code>WeakMap</code>, <code>WeakRef</code>, and <code>FinalizationRegistry</code> work internally?",
  "<code>WeakMap</code>: keys held weakly — ephemoron table, entries cleared during GC marking if key not marked. <code>WeakRef.deref()</code>: may return object or <code>undefined</code> non-deterministically. <code>FinalizationRegistry</code> callback runs AFTER object collected, on microtask checkpoint — NOT for critical cleanup. Use explicit lifecycle management.",
  ["L2_composition"])

# ===== 05-MODULES =====
c("Modules", "What are the key differences between ESM and CJS?",
  "ESM: static structure (parse-time), <code>import</code>/<code>export</code> declarative, live bindings, always strict mode, async loading, extension required. CJS: dynamic, <code>require()</code> function call, value copies at require time, non-strict default, synchronous loading. <code>this</code> at top level: ESM = <code>undefined</code>, CJS = <code>exports</code>.",
  ["L1_mechanics"])

c("Modules", "What are live bindings in ESM?",
  "Imported bindings are READ-ONLY LIVE REFERENCES to the exporting module's current value. If exporter does <code>export let x = 1</code> then <code>x = 2</code>, the importer sees <code>2</code>. CJS copies: <code>const { x } = require('./m')</code> captures the value at require time; later changes not reflected.",
  ["L2_composition"])

c("Modules", 'What is the <code>"exports"</code> field in <code>package.json</code>?',
  "Conditional exports control what files are exposed: <code>{ 'exports': { '.': { 'import': './esm/index.js', 'require': './cjs/index.cjs' } } }</code>. Also acts as ENCAPSULATION — files not listed are inaccessible from outside. <code>'imports'</code> field for private internal aliases (<code>#utils</code>).",
  ["L1_mechanics"])

c("Modules", "How does tree shaking work?",
  "Bundler analyzes ESM import graph at build time. Exports never imported are eliminated. Relies on ESM static structure. <code>/*#__PURE__*/</code> annotation tells bundler a call has no side effects. <code>package.json</code> <code>'sideEffects': false</code> declares the package free of side-effecting imports. Barrel files defeat tree shaking.",
  ["L2_composition"])

c("Modules", "How does dynamic <code>import()</code> work?",
  "<code>const module = await import('./mod.js')</code> returns <code>Promise&lt;ModuleNamespaceObject&gt;</code>. The namespace object is sealed with live bindings (getters). Works in both ESM and CJS. Bundlers use it as SPLIT POINTS for code splitting. Non-constant arguments create separate chunks.",
  ["L1_mechanics"])

# ===== 06-ITERABLES-GENERATORS =====
c("Iterables", "What is the iterator protocol?",
  "An object is <code>iterable</code> if it has <code>[Symbol.iterator]</code> method returning an <code>iterator</code>. An iterator has a <code>next()</code> method returning <code>{ value, done: boolean }</code>. <code>for...of</code>, spread <code>[...x]</code>, <code>Array.from()</code>, destructuring all use this protocol.",
  ["L1_mechanics"])

c("Iterables", "How do generator functions work internally?",
  "<code>function* g() { yield 1; yield 2; }</code> returns a generator object. Calling it does NOT execute the body — creates a suspended execution context. Each <code>.next(arg)</code> resumes until next <code>yield</code>; <code>arg</code> becomes the yield expression's value. The entire local state is heap-allocated between resumes (heavier than regular functions).",
  ["L2_composition"])

c("Iterables", "What does <code>yield*</code> do?",
  "Delegates iteration to another iterable. The delegating generator suspends; values from inner iterable are yielded through. The value of the <code>yield*</code> expression is the <code>return</code> value of the delegated iterator. <code>throw</code> and <code>return</code> propagate both ways.",
  ["L1_mechanics"])

c("Iterables", "What is an async generator and how does <code>for-await-of</code> work?",
  "<code>async function* gen() { yield await fetch(); }</code>. <code>for await (const x of gen())</code>: awaits each <code>next().value</code> promise. Each <code>.next()</code> returns <code>Promise&lt;{value, done}&gt;</code>. Supports <code>yield*</code> on async iterables. For streaming: <code>for await (const chunk of readableStream)</code>.",
  ["L1_mechanics"])

c("Iterables", "What are well-known Symbols and their purposes?",
  "<code>Symbol.iterator</code>: <code>for...of</code> protocol. <code>Symbol.toPrimitive</code>: custom coercion (<code>hint: 'string'|'number'|'default'</code>). <code>Symbol.toStringTag</code>: <code>[object Tag]</code>. <code>Symbol.hasInstance</code>: custom <code>instanceof</code>. <code>Symbol.isConcatSpreadable</code>: controls <code>.concat()</code> flattening. <code>Symbol.match/replace/search/split</code>: string method customization.",
  ["L1_mechanics"])

# ===== 07-PROXIES-REFLECT =====
c("Proxies", "What are ALL 13 Proxy traps?",
  "Fundamental: <code>get</code>, <code>set</code>, <code>has</code> (<code>in</code>), <code>deleteProperty</code>, <code>ownKeys</code>, <code>getOwnPropertyDescriptor</code>, <code>defineProperty</code>, <code>preventExtensions</code>, <code>getPrototypeOf</code>, <code>setPrototypeOf</code>, <code>isExtensible</code>.<br>Derived: <code>apply</code> (function call), <code>construct</code> (<code>new</code>).<br>All mirrored by <code>Reflect.*</code> methods.",
  ["L1_mechanics"])

c("Proxies", "What is the <code>receiver</code> parameter in <code>get</code>/<code>set</code> traps?",
  "The proxy (or inheriting proxy) that received the operation. Essential for correct <code>this</code> in getters and for prototype chain interception. Always pass <code>receiver</code> to <code>Reflect.get/set</code> inside traps: <code>Reflect.get(target, prop, receiver)</code>. Without it, inherited accessors get wrong <code>this</code>.",
  ["L2_composition"])

c("Proxies", "How does Vue 3 reactivity use Proxies?",
  "<code>reactive(obj)</code> wraps in a Proxy. <code>get</code> trap tracks dependencies (which effects read which properties). <code>set</code> trap triggers re-runs of subscribed effects. Lazy deep reactivity: nested objects are proxied only when accessed. Handles array mutations, Map/Set, dynamic property addition — things <code>Object.defineProperty</code> (Vue 2) couldn't.",
  ["L6_innovation"])

c("Proxies", "How does Immer use Proxies?",
  "<code>produce(baseState, recipe)</code> wraps <code>baseState</code> in a Proxy. Writes are recorded copy-on-write — only modified parts are cloned. Unchanged parts are structurally shared. The proxy tracks which objects were 'drafted'. At the end: produces a new immutable state tree with maximal structural sharing.",
  ["L6_innovation"])

c("Proxies", "What are the Proxy invariants that can throw?",
  "Violations: <code>getOwnPropertyDescriptor</code> must report non-configurable, non-writable properties consistently. <code>defineProperty</code> cannot add properties to non-extensible target. <code>ownKeys</code> must include all non-configurable own properties. <code>getPrototypeOf</code> must match for non-extensible targets. All throw <code>TypeError</code>.",
  ["L2_composition"])

c("Proxies", "What does <code>Proxy.revocable</code> do?",
  "<code>const { proxy, revoke } = Proxy.revocable(target, handler); revoke()</code>. After revocation, ANY operation on the proxy throws <code>TypeError</code>. Irreversible. Internal <code>[[ProxyTarget]]</code> and <code>[[ProxyHandler]]</code> set to null. Use case: temporary capabilities that expire.",
  ["L1_mechanics"])

# ===== 08-TYPESCRIPT-CORE =====
c("TSCore", "What is the difference between a <code>type</code> alias and an <code>interface</code>?",
  "Interface: declaration merging (same-name interfaces merge), extends. Type: no merging, union/intersection, mapped types, conditional types, primitives, tuples. Use <code>interface</code> for object shapes (extensible); <code>type</code> for unions, intersections, and computed types. Neither has runtime effect.",
  ["L0_primitives"])

c("TSCore", "What are generic constraints with <code>extends</code>?",
  "<code>&lt;T extends HasLength&gt;</code> restricts <code>T</code> to types assignable to <code>HasLength</code>. <code>&lt;T extends keyof SomeType&gt;</code> restricts to keys. <code>&lt;T extends abstract new (...args) =&gt; infer I&gt;</code> for constructor patterns. Structural — not nominal.",
  ["L1_mechanics"])

c("TSCore", "How do conditional types work?",
  "<code>T extends U ? X : Y</code>. Evaluates to <code>X</code> if <code>T</code> assignable to <code>U</code>, else <code>Y</code>. When <code>T</code> is a NAKED generic over a union, it DISTRIBUTES: <code>ToArray&lt;string | number&gt;</code> → <code>string[] | number[]</code>. Suppress distribution by wrapping: <code>[T] extends [U]</code>.",
  ["L2_composition"])

c("TSCore", "What does the <code>infer</code> keyword do?",
  "Captures a type within a conditional type: <code>ReturnType&lt;T&gt; = T extends (...args: any[]) =&gt; infer R ? R : never</code>. <code>ArrayElement&lt;T&gt; = T extends (infer U)[] ? U : never</code>. Multiple infers: <code>FirstArg&lt;T&gt; = T extends (first: infer F, ...rest: any[]) =&gt; any ? F : never</code>.",
  ["L2_composition"])

c("TSCore", "What are mapped types?",
  "<code>{ [K in keyof T]: NewType }</code> — iterates over keys of <code>T</code>. Modifier operators: <code>readonly</code>/<code>?</code> added/removed with <code>+</code>/<code>-</code>: <code>{ -readonly [K in keyof T]: T[K] }</code>. Key remapping (TS 4.1+): <code>[K in keyof T as `get${Capitalize&lt;string &amp; K&gt;}`]</code>.",
  ["L2_composition"])

c("TSCore", "How do template literal types work?",
  "`` type Route = `/api/${string}` `` — matches any string starting with '/api/'. With unions: `` type Evt = `on${Capitalize&lt;'click'|'focus'&gt;}` `` = <code>'onClick' | 'onFocus'</code>. Inference: `` Parse&lt;T&gt; = T extends `${infer Method} /${infer Path}` ? { method: Method, path: Path } : never ``.",
  ["L2_composition"])

c("TSCore", "What are discriminated unions?",
  "A union of types sharing a common literal property (the discriminant). <code>type Shape = { kind: 'circle', radius: number } | { kind: 'rect', w: number, h: number }</code>. <code>switch (s.kind) { case 'circle': s.radius ... }</code> — TypeScript narrows the type in each branch. Exhaustiveness check: assign <code>never</code> to the default case.",
  ["L1_mechanics"])

# ===== 09-TYPESCRIPT-ADVANCED =====
c("TSAdvanced", "What are branded types and how do they simulate nominal typing?",
  "<code>type UserId = string &amp; { __brand: 'UserId' }</code>. TypeScript is structural — branded intersection adds a phantom type tag. <code>getUser(id: UserId)</code> rejects plain string. <code>const uid = 'abc' as UserId</code> explicitly brands. Use <code>unique symbol</code> for truly unique brands.",
  ["L2_composition"])

c("TSAdvanced", "What is declaration merging?",
  "Multiple same-name declarations combine. Interface + Interface: members merge (conflicting types error). Namespace + Class/Function/Enum: members merge. Module augmentation: <code>declare module 'express' { interface Request { user?: User } }</code>. Global augmentation: <code>declare global { interface Window { myApp } }</code>.",
  ["L2_composition"])

c("TSAdvanced", "What does <code>as const</code> do?",
  "Const assertion: <code>const x = { a: 1 } as const</code> makes <code>x</code>'s type <code>{ readonly a: 1 }</code> — deeply readonly, literal types, no widening. Array becomes <code>readonly</code> tuple: <code>[1, 2] as const</code> → <code>readonly [1, 2]</code>. Enum replacement without runtime cost.",
  ["L1_mechanics"])

c("TSAdvanced", "What does the <code>satisfies</code> operator do? (TS 4.9+)",
  "<code>const x = { a: 1 } satisfies Record&lt;string, number&gt;</code>. Validates the expression matches a type WITHOUT changing its inferred type. Unlike <code>: Type</code>, <code>satisfies</code> preserves the narrowest type: <code>x.a</code> is <code>number</code>, not <code>number</code> (it's exactly <code>1</code>).",
  ["L1_mechanics"])

c("TSAdvanced", "What is the <code>unique symbol</code> type?",
  "Each <code>const sym: unique symbol = Symbol()</code> or <code>declare const sym: unique symbol</code> creates a unique type. Used as property keys discriminated unions, nominal brand tokens, and type-level identity. Two different <code>unique symbol</code>s are never assignable to each other.",
  ["L2_composition"])

c("TSAdvanced", "What is the contravariance trick with <code>infer</code>?",
  "Union to Intersection: <code>type UnionToIntersection&lt;U&gt; = (U extends any ? (k: U) =&gt; void : never) extends (k: infer I) =&gt; void ? I : never</code>. Because function parameter types are CONTRAVARIANT, <code>infer</code> there produces an intersection instead of a union. Interview classic.",
  ["L6_innovation"])

c("TSAdvanced", "How does the TypeScript compiler work at a high level?",
  "1) Scanner → tokens. 2) Parser → AST (with binder for symbol resolution). 3) Binder → Symbol table (scope analysis). 4) Type Checker → resolves types, checks assignability. 5) Emitter → transpiles to JS (strips types). Declaration files (<code>.d.ts</code>) emitted from the same AST. Strict mode flags each enable different checker passes.",
  ["L3_design"])

# ===== 10-DOM-WEB-APIS =====
c("DOM", "What is <code>MutationObserver</code> and how does it batch?",
  "<code>const obs = new MutationObserver(callback); obs.observe(node, { childList: true, attributes: true, subtree: true })</code>. <code>callback</code> receives <code>MutationRecord[]</code> — an array of batched mutations since last microtask drain. Use <code>obs.takeRecords()</code> to flush pending records synchronously.",
  ["L1_mechanics"])

c("DOM", "What is <code>IntersectionObserver</code>?",
  "<code>new IntersectionObserver(callback, { root, rootMargin, threshold })</code>. Fires <code>callback(entries)</code> when target's visibility crosses a threshold. Used for: lazy loading (<code>entry.isIntersecting</code>), infinite scroll, analytics (did user see this ad?). More performant than scroll event listeners.",
  ["L1_mechanics"])

c("DOM", "How does <code>structuredClone</code> differ from <code>JSON.parse(JSON.stringify(obj))</code>?",
  "<code>structuredClone(obj)</code>: deep clones including Dates, Maps, Sets, RegExp, ArrayBuffer, Blob, ImageData. Handles circular references. Preserves <code>undefined</code>. Works in transfer mode (<code>structuredClone(buf, { transfer: [buf] })</code>). JSON round-trip: loses all the above, can't handle cycles, drops <code>undefined</code> values.",
  ["L1_mechanics"])

c("DOM", "What are Web Workers and their types?",
  "Dedicated Worker: one-to-one with creator. Shared Worker: accessible by multiple scripts in same origin. Service Worker: intercepts network requests, enables offline, push notifications.<br>Workers run in separate thread — no DOM access. Communicate via <code>postMessage</code>/<code>onmessage</code>. Transferable objects move ownership with zero copy.",
  ["L1_mechanics"])

c("DOM", "What is <code>FormData</code> and when to use it?",
  "<code>new FormData(formElement)</code> — collects all form fields as key-value pairs. Supports file uploads (<code>formData.append('file', fileInput.files[0])</code>). Pass directly to <code>fetch()</code> body for <code>multipart/form-data</code>. <code>.get(key)</code>, <code>.getAll(key)</code>, <code>.set(key, value)</code>, <code>.delete(key)</code>.",
  ["L1_mechanics"])

# ===== 11-PATTERNS-META =====
c("Patterns", "What is the Module Pattern (classic JS encapsulation)?",
  "IIFE returning an object with closures: <code>const counter = (() =&gt; { let count = 0; return { inc: () =&gt; ++count, get: () =&gt; count } })()</code>. Encapsulates private state via closures. Pre-ES6 modules, pre-<code>#private</code> fields. Still used for simple singleton modules.",
  ["L2_composition"])

c("Patterns", "What is the Observer (Pub/Sub) pattern in JS?",
  "Subject maintains list of observers; notifies all on state change. Manual: <code>class Subject { observers = []; subscribe(fn) { this.observers.push(fn); } notify(data) { this.observers.forEach(fn =&gt; fn(data)); } }</code>. Built-in: <code>EventTarget</code> (<code>addEventListener</code>, <code>dispatchEvent</code>), <code>EventEmitter</code> (Node.js).",
  ["L2_composition"])

c("Patterns", "How is the Chain of Responsibility pattern used in middleware?",
  "Each handler decides to handle or pass to next. Express middleware: <code>app.use((req, res, next) =&gt; { ...; next() })</code>. Redux middleware: <code>store =&gt; next =&gt; action =&gt; { ...; return next(action) }</code>. Enables composable request processing pipelines. <code>compose</code> utility chains functions right-to-left.",
  ["L2_composition"])

c("Patterns", "What is the Fluent API (Method Chaining) pattern?",
  "Methods return <code>this</code> for chaining: <code>query.where('a').orderBy('b').limit(10)</code>. Used by jQuery, Lodash, Builder pattern, Query builders. Each method returns the same instance (mutating) or a new instance (immutable). Clean API, but harder to debug — chain breaks silently on <code>undefined</code> return.",
  ["L2_composition"])

c("Patterns", "How does the Revealing Module Pattern extend the basic module pattern?",
  "Define all functions in private scope, return only public API: <code>const module = (() =&gt; { function privateFn() {}; function publicFn() { privateFn(); }; return { publicFn } })()</code>. Clearer separation between public and private. All bindings are closures on the same private scope.",
  ["L2_composition"])

# ===== 12-EXPERT =====
c("Expert", "How does the event loop detect microtask starvation?",
  "It doesn't. Microtasks run to exhaustion before any macrotask. If a microtask handler spawns another microtask endlessly, the queue never empties — the browser freezes. This is a deliberate design: microtasks are for 'ASAP after current task'. Use <code>setTimeout</code> if you need to yield.",
  ["L6_innovation"])

c("Expert", "How do you create a custom thenable (fake promise)?",
  "<code>const thenable = { then(resolve) { resolve(42); } }</code>. Any object with a <code>then</code> method is a thenable. <code>await thenable</code> works. <code>Promise.resolve(thenable)</code> unwraps it. Used for interop between different promise implementations. Danger: accidental thenable — <code>await { then: () =&gt; {} }</code> never resolves.",
  ["L6_innovation"])

c("Expert", "What is the <code>structuredClone</code> transfer mechanism?",
  "<code>structuredClone(buffer, { transfer: [buffer] })</code> MOVES ownership — the original buffer becomes detached (zero bytes). Zero-copy. Works with ArrayBuffer, MessagePort, ImageBitmap, OffscreenCanvas. The transferred objects become unusable in the sender. Great for large binary data between Worker and main thread.",
  ["L6_innovation"])

c("Expert", "How does V8 handle <code>arguments</code> object optimization?",
  "In non-strict mode, <code>arguments</code> is MAGICALLY linked to named parameters — changing <code>arguments[0]</code> changes the parameter. This linkage is expensive and disables many optimizations. Strict mode: <code>arguments</code> is a snapshot copy, no linkage, optimizable. Avoid <code>arguments</code> — use rest params <code>...args</code>.",
  ["L6_innovation"])

c("Expert", "How do you write a recursive conditional type to parse a path string?",
  "<code>type PathValue&lt;T, P extends string&gt; = P extends `${infer Head}.${infer Tail}` ? PathValue&lt;T[Head &amp; keyof T], Tail&gt; : T[P &amp; keyof T];</code>. Recursively splits on <code>.</code>. TypeScript 4.1+ supports recursive conditional types with ~50 depth limit. Exceeding: <code>'Type instantiation is excessively deep'</code>.",
  ["L6_innovation"])

c("Expert", "What is <code>Symbol.species</code> and why is it controversial?",
  "Controls which constructor to use for derived results: <code>class MyArr extends Array { static get [Symbol.species]() { return Array } }</code>. Then <code>new MyArr(1,2).map(x =&gt; x)</code> returns a plain <code>Array</code>. Many consider it an anti-pattern — violates Liskov substitution. Being removed from future specs. Avoid.",
  ["L6_innovation"])

# ===== BUILD =====
for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

fn = "JS_TS_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(fn)
print(f"Built {len(decks)} decks with {len(C)} cards -> {fn}")
