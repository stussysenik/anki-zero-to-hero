import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Clojure"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "DataStructs":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Data-Structures"),
    "Concurrency":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Concurrency"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === CLOJURE FUNDAMENTALS ===

c("Fundamentals", "What is Clojure?",
  "A dynamic, functional Lisp dialect that runs on the JVM (and CLR, JavaScript via ClojureScript). Designed for concurrency with immutable data structures and Software Transactional Memory (STM). Hosted language — seamless Java interop.",
  ["L0_primitives"])

c("Fundamentals", "What is a Lisp?",
  "A family of languages using fully parenthesized prefix notation (s-expressions). Code is data (homoiconicity). Clojure is a modern Lisp with immutability, concurrency primitives, and pragmatic pragmatism.",
  ["L0_primitives"])

c("Fundamentals", "What is an s-expression in Clojure?",
  "A parenthesized list where the first element is the operator/function: <code>(+ 1 2 3)</code>. This is both the syntax for code AND the representation of data (list, vector, map all follow this form). Code is data.",
  ["L0_primitives"])

c("Fundamentals", "What does 'homoiconicity' mean in Clojure/Lisp?",
  "Code and data share the same structure. Programs are written as data structures (lists, vectors, maps) that can be manipulated by other programs. This enables macros — code that writes code at compile time.",
  ["L0_primitives"])

c("Fundamentals", "What are Clojure's immutable data structures?",
  "Lists: <code>'(1 2 3)</code>. Vectors: <code>[1 2 3]</code>. Maps: <code>{:a 1 :b 2}</code>. Sets: <code>#{1 2 3}</code>. All persistent — 'updates' return new versions while sharing structure. Built on trees and tries for efficiency.",
  ["L0_primitives"])

c("Fundamentals", "What is a keyword in Clojure?",
  "An identifier prefixed with <code>:</code>: <code>:name</code>, <code>:age</code>. Self-evaluating (evaluates to itself). Commonly used as map keys and enum-like values. Can be namespaced: <code>:user/name</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is a symbol in Clojure?",
  "An identifier that refers to a value or function: <code>x</code>, <code>+</code>, <code>my-function</code>. Symbols are resolved in the current namespace. Don't confuse with keywords — symbols refer, keywords index.",
  ["L0_primitives"])

c("Fundamentals", "What is a macro in Clojure?",
  "A function that transforms code at compile time. Receives unevaluated forms (the AST as data) and returns new code. <code>(defmacro unless [test &amp; body] `(if (not ~test) (do ~@body)))</code>. Enables DSL creation.",
  ["L0_primitives"])

c("Fundamentals", "What is the REPL in Clojure?",
  "Read-Eval-Print-Loop — the interactive development environment. The heart of Clojure development: connect your editor to a running REPL process, evaluate forms inline, inspect results, redefine functions without restarting.",
  ["L0_primitives"])

c("Fundamentals", "What is Leiningen / deps.edn?",
  "Leiningen: traditional Clojure project tool (<code>project.clj</code>). Deps.edn: newer Clojure CLI tools. Both manage dependencies, build, and REPL. Prefer <code>deps.edn</code> for new projects (official tools).",
  ["L0_primitives"])

c("Fundamentals", "What is an atom in Clojure?",
  "A mutable reference to an immutable value. <code>(def counter (atom 0))</code>. Update: <code>(swap! counter inc)</code>, read: <code>@counter</code>. Provides atomic, synchronous, independent state. One of Clojure's reference types.",
  ["L0_primitives"])

c("Fundamentals", "What are Clojure's four reference types?",
  "<code>var</code>: thread-local, mutable root binding (defs). <code>atom</code>: atomic, synchronous, uncoordinated. <code>ref</code>: coordinated, synchronous (STM). <code>agent</code>: asynchronous, uncoordinated. Each for different concurrency needs.",
  ["L0_primitives"])

# === CLOJURE CORE OPERATIONS ===

c("CoreOps", "How do you call a function in Clojure?",
  "Prefix notation: <code>(function arg1 arg2)</code>. <code>(+ 1 2 3)</code> → 6. <code>(str \"Hello, \" name)</code>. <code>(println \"Hi\")</code>. No commas, just spaces. Nest for composition: <code>(* (+ 1 2) 3)</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a variable?",
  "<code>(def x 42)</code> — binds the symbol <code>x</code> to 42 in the current namespace. Uses <code>var</code> internally. Prefer <code>let</code> for local bindings.",
  ["L1_mechanics"])

c("CoreOps", "How do you create local bindings?",
  "<code>(let [x 1 y 2] (+ x y))</code> — binds <code>x</code> and <code>y</code> within the <code>let</code> body. Vectors of pairs: [symbol value symbol value]. Returns the last expression.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a function?",
  "<code>(defn greet [name] (str \"Hello, \" name))</code>. Multi-arity: <code>(defn greet ([] \"Hello\") ([name] (str \"Hello, \" name)))</code>. Anonymous: <code>(fn [x] (* x 2))</code> or shorthand <code>#(* % 2)</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you access vector elements?",
  "Vectors are functions of their indices: <code>([1 2 3] 1)</code> → 2. Or <code>(get [1 2 3] 1)</code> → 2. <code>(get [1 2 3] 99 :default)</code> returns <code>:default</code> if out of bounds.",
  ["L1_mechanics"])

c("CoreOps", "How do you access map values?",
  "Maps are functions of their keys: <code>({:a 1 :b 2} :a)</code> → 1. Keywords are functions of maps: <code>(:a {:a 1 :b 2})</code> → 1. <code>(get my-map :key default)</code> with fallback.",
  ["L1_mechanics"])

c("CoreOps", "How do you update a map?",
  "<code>(assoc {:a 1} :b 2)</code> → <code>{:a 1 :b 2}</code>. <code>(dissoc {:a 1 :b 2} :b)</code> → <code>{:a 1}</code>. <code>(update {:a 1} :a inc)</code> → <code>{:a 2}</code>. All return new maps.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a conditional?",
  "<code>(if condition then-expr else-expr)</code>. <code>(when condition expr)</code> (no else). <code>(cond test1 expr1 test2 expr2 :else default)</code>. <code>(case value :key1 expr1 :key2 expr2 default)</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you do threading (data transformation)?",
  "<code>(-&gt; data (fn1) (fn2 arg))</code> — thread-first, result goes as first arg. <code>(-&gt;&gt; data (map inc) (filter even?))</code> — thread-last, result goes as last arg. <code>(as-&gt; data $ (fn1 $) (fn2 $ arg))</code> for explicit positioning.",
  ["L1_mechanics"])

c("CoreOps", "How do you work with sequences?",
  "<code>(map inc [1 2 3])</code> → <code>(2 3 4)</code>. <code>(filter even? [1 2 3 4])</code> → <code>(2 4)</code>. <code>(reduce + [1 2 3])</code> → 6. <code>(take 2 [1 2 3 4])</code> → <code>(1 2)</code>. <code>(drop 2 [1 2 3 4])</code> → <code>(3 4)</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a namespace?",
  "<code>(ns my-app.core (:require [clojure.string :as str]))</code>. The <code>ns</code> form goes at the top of the file. <code>:require</code> for dependencies, <code>:use</code> (deprecated), <code>:import</code> for Java classes.",
  ["L1_mechanics"])

c("CoreOps", "How do you use the REPL effectively?",
  "Connect your editor (VS Code Calva, Emacs CIDER, IntelliJ Cursive) to a running REPL. Type <code>, e f</code> (send form), <code>, e b</code> (send buffer). Redefine functions live. Inspect with <code>, e i</code>. Use <code>tap&gt;</code> and portal for rich inspection.",
  ["L1_mechanics"])

# === DATA STRUCTURES ===

c("DataStructs", "What is a lazy sequence in Clojure?",
  "A sequence whose elements are computed on demand. <code>(take 5 (iterate inc 0))</code> — infinite sequence, only first 5 are realized. Powers <code>map</code>, <code>filter</code>, <code>range</code> — all return lazy seqs. <code>doall</code> or <code>dorun</code> to force evaluation.",
  ["L1_mechanics"])

c("DataStructs", "What is destructuring in Clojure?",
  "Extracting values from data in <code>let</code>/<code>fn</code> parameters: <code>(let [{:keys [name age]} person] ...)</code>. Vector: <code>(let [[a b &amp; rest] [1 2 3 4]] ...)</code>. Nested: <code>(let [{[x y] :coords} location] ...)</code>.",
  ["L1_mechanics"])

c("DataStructs", "What is a record in Clojure?",
  "A typed map with named fields: <code>(defrecord Person [name age])</code>. Create: <code>(-&gt;Person \"Alice\" 30)</code> or <code>(map-&gt;Person {:name \"Alice\" :age 30})</code>. Supports protocols and is faster than plain maps for field access.",
  ["L2_composition"])

c("DataStructs", "What is a protocol in Clojure?",
  "A type-based polymorphism mechanism similar to interfaces: <code>(defprotocol Speak (say [this]))</code>. Implement: <code>(extend-type Person Speak (say [p] (str \"I'm \" (:name p))))</code>. Open — can extend existing types with new protocols.",
  ["L2_composition"])

# === CONCURRENCY ===

c("Concurrency", "How do atoms work for mutable state?",
  "<code>(def state (atom {:count 0}))</code>. Read: <code>@state</code> or <code>(deref state)</code>. Update: <code>(swap! state update :count inc)</code> — applies function atomically. <code>(reset! state new-val)</code> — unconditional set.",
  ["L1_mechanics"])

c("Concurrency", "What is a <code>ref</code> and STM in Clojure?",
  "Software Transactional Memory: <code>(def balance (ref 100))</code>. Updates must be in a transaction: <code>(dosync (alter balance + 50))</code>. If two transactions conflict, one retries. Ensures consistency across multiple refs.",
  ["L1_mechanics"])

c("Concurrency", "What is a <code>future</code> in Clojure?",
  "<code>(future (expensive-computation))</code> — runs on a thread pool, returns immediately. Dereference to get result: <code>@f</code> (blocks until done). For unblocking: <code>(realized? f)</code> checks if done.",
  ["L1_mechanics"])

c("Concurrency", "What is a <code>promise</code> in Clojure?",
  "A one-time write, many-reader container: <code>(def p (promise))</code>. Deliver: <code>(deliver p \"result\")</code>. Read: <code>@p</code> — blocks until delivered. Used for coordinating threads, like a single-value channel.",
  ["L1_mechanics"])

c("Concurrency", "What is <code>core.async</code>?",
  "A library for CSP-style (Communicating Sequential Processes) concurrency with channels and go blocks. <code>(go (&gt;! ch val))</code> puts, <code>(go (let [v (&lt;! ch)] ...))</code> takes. Channels are queues; go blocks are lightweight 'processes' that park instead of blocking.",
  ["L3_design"])

# === PATTERNS ===

c("Patterns", "What is the ring middleware pattern?",
  "Ring is Clojure's HTTP abstraction. Handler: <code>(fn [request] response)</code>. Middleware: <code>(fn [handler] (fn [request] (handler enriched-request)))</code>. Compose: <code>(-&gt; handler (wrap-json-body) (wrap-session))</code>.",
  ["L2_composition"])

c("Patterns", "What is the component/Integrant system pattern?",
  "Lifecycle management for stateful components (DB connections, HTTP servers). Defines start/stop hooks. Component library: <code>(defrecord Database [url] component/Lifecycle ...)</code>. Integrant: data-driven configuration map with suspend/resume.",
  ["L3_design"])

c("Patterns", "What is the Spec validation pattern?",
  "<code>clojure.spec.alpha</code> — describe data shapes: <code>(s/def ::email (s/and string? #(re-find #\"@\" %)))</code>. Validate: <code>(s/valid? ::email \"a@b\")</code>. Generate test data: <code>(s/exercise ::email)</code>. Conform for parsing.",
  ["L2_composition"])

c("Patterns", "What is the multimethod pattern?",
  "Runtime dispatch based on a function of arguments: <code>(defmulti area :shape)</code>. <code>(defmethod area :circle [{:keys [r]}] (* Math/PI r r))</code>. <code>(defmethod area :rectangle [{:keys [w h]}] (* w h))</code>. More flexible than protocols.",
  ["L2_composition"])

c("Patterns", "What is the reduce-kv pattern for maps?",
  "<code>(reduce-kv (fn [acc k v] (assoc acc k (inc v))) {} {:a 1 :b 2})</code> — <code>reduce-kv</code> takes key, value, and accumulator. The efficient way to reduce over maps without intermediate sequences.",
  ["L2_composition"])

# === GOTCHAS ===

c("Gotchas", "Why do I get <code>ArityException Wrong number of args</code>?",
  "A function was called with the wrong number of arguments. Clojure functions can have fixed arities. Check your function definition and the number of args you're passing. Use multi-arity <code>defn</code> if needed.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my lazy sequence not realize before side effects?",
  "Lazy sequences evaluate items on demand. If you have side effects in <code>map</code> or <code>for</code>, they won't execute until the result is consumed. Use <code>doall</code> (keeps head), <code>dorun</code> (discards), or <code>run!</code> (side effects only).",
  ["L4_diagnosis"])

c("Gotchas", "What is the 'holding onto the head' memory leak?",
  "If you <code>def</code> a reference to the head of a large lazy sequence, the entire sequence stays in memory as it's realized. Use <code>doall</code> with careful scope, or process sequences incrementally without holding the head.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>let</code> not support destructuring with <code>=</code>?",
  "<code>(let [{:keys [a]} = my-map])</code> — the <code>=</code> is NOT assignment, it's the equality function. Destructuring uses vector binding: <code>(let [{:keys [a]} my-map] a)</code>. No <code>=</code> in let binding forms.",
  ["L4_diagnosis"])

c("Gotchas", "How do you handle Java interop nulls in Clojure?",
  "Java methods can return <code>null</code>. Use <code>(some? x)</code> or <code>(nil? x)</code> checks. <code>some-&gt;</code> macro for nil-check chaining: <code>(some-&gt; obj .getA .getB .getC)</code>. Returns nil if any step returns nil, without NPE.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>def</code> inside <code>defn</code> create a global var?",
  "<code>def</code> always creates/updates a namespace-level var, even when called inside a function. For local bindings, use <code>let</code>. <code>def</code> inside functions is almost always a bug.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "What is transducers in Clojure?",
  "Composable algorithmic transformations independent of the context (sequence, channel, observable). <code>(into [] (comp (filter even?) (map inc)) [1 2 3 4])</code>. No intermediate sequences created. Used with <code>into</code>, <code>sequence</code>, <code>transduce</code>, <code>eduction</code>.",
  ["L3_design"])

c("Expert", "What is the difference between <code>reduce</code> and <code>transduce</code>?",
  "<code>reduce</code> with a transducer: <code>(transduce xf + [1 2 3])</code> — no intermediate sequences, applies reducing function directly. <code>reduce</code> iterates; <code>transduce</code> applies xf and reduces in one pass. More efficient for large data.",
  ["L3_design"])

c("Expert", "What is 'REPL-driven development'?",
  "A development workflow where you connect your editor to a running REPL, write code in the editor, evaluate inline, inspect results, and build the program interactively. You never restart — you redefine functions and replay data flows. The program grows in the REPL.",
  ["L5_opinion"])

c("Expert", "When should you use a macro vs a function in Clojure?",
  "Macro: when you need to control evaluation (short-circuit, custom control flow, DSL syntax), or transform code at compile time. Function: 99% of the time. Macros are powerful but create opaque behavior. 'Never write a macro when a function will do.'",
  ["L5_opinion"])

c("Expert", "What is ClojureScript?",
  "Clojure compiling to JavaScript. Shares the same reader, syntax, and philosophy. Differences: no JVM interop (uses Google Closure), different concurrency model (no atoms/refs, uses core.async), browser/Node.js targets. <code>cljs</code> / <code>shadow-cljs</code> for builds.",
  ["L3_design"])

c("Expert", "What are Datomic and XTDB?",
  "Datomic: immutable database with Datalog queries, designed for Clojure. Stores facts with time, enabling queries 'as of' any point in time. XTDB: open-source bitemporal database inspired by Datomic. Both treat database as a value.",
  ["L5_opinion"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
