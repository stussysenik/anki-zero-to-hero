import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "ReScript"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Types":        genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Types"),
    "React":        genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-React-Bindings"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === RESCRIPT FUNDAMENTALS ===

c("Fundamentals", "What is ReScript?",
  "A robustly typed language that compiles to efficient, readable JavaScript. OCaml heritage with JS-first design. Fast compiler, no runtime library needed — zero-cost interop with JS.",
  ["L0_primitives"])

c("Fundamentals", "How is ReScript different from TypeScript?",
  "ReScript has sound type system (no <code>any</code>), nominal types, pattern matching, variants, and OCaml heritage. TypeScript adds types to JS's dynamic nature. ReScript is a different language; TypeScript is a superset of JS.",
  ["L0_primitives"])

c("Fundamentals", "What is a ReScript module?",
  "Each <code>.res</code> file is a module. The filename becomes the module name (capitalized). Functions/types are accessed via <code>ModuleName.functionName</code>. No export keyword needed — everything is public by default. Use <code>@genType</code> for TS exports.",
  ["L0_primitives"])

c("Fundamentals", "What is a variant in ReScript?",
  "A discriminated union / tagged union. <code>type color = Red | Green | Blue | RGB(int, int, int)</code>. Pattern-matched with <code>switch</code>. The compiler enforces exhaustive matching of all cases.",
  ["L0_primitives"])

c("Fundamentals", "What is an option type in ReScript?",
  "<code>option&lt;'a&gt;</code> = <code>Some(value)</code> or <code>None</code>. ReScript has no <code>null</code> or <code>undefined</code>. Every potentially-missing value must be an <code>option</code>, and the compiler forces you to handle both cases.",
  ["L0_primitives"])

c("Fundamentals", "What is a record in ReScript?",
  "A named, typed collection of fields: <code>type person = {name: string, age: int}</code>. Immutable. Update with spread: <code>{...person, age: person.age + 1}</code>. Fast compilation to plain JS objects.",
  ["L0_primitives"])

c("Fundamentals", "What is pattern matching in ReScript?",
  "The <code>switch</code> expression: <code>switch value { | Some(x) =&gt; x | None =&gt; 0 }</code>. Works on variants, options, lists, arrays, numbers (with guards), strings. Compiler ensures exhaustiveness.",
  ["L0_primitives"])

c("Fundamentals", "What is the pipe operator in ReScript?",
  "<code>-&gt;</code> — passes the left value as the first argument: <code>data-&gt;Array.map(x =&gt; x * 2)-&gt;Array.keep(x =&gt; x &gt; 5)-&gt;Js.log</code>. Creates readable data pipelines.",
  ["L0_primitives"])

c("Fundamentals", "What makes ReScript's compiler fast?",
  "Written in OCaml, uses incremental compilation. Type checking is near-instant. No <code>node_modules</code> type resolution overhead like TypeScript. Build for production in milliseconds.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>@react.component</code> decorator?",
  "JSX-like syntax for React components. ReScript's compiler transforms <code>@react.component</code> functions into efficient React JSX calls. No runtime library needed for JSX transformation.",
  ["L0_primitives"])

# === RESCRIPT CORE OPERATIONS ===

c("CoreOps", "How do you define a let binding?",
  "<code>let x = 42</code> — immutable by default. <code>let name = \"Alice\"</code>. Blocks return the last expression: <code>let result = { let a = 1; let b = 2; a + b }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a function?",
  "<code>let add = (x, y) =&gt; x + y</code>. Type-annotated: <code>let add = (x: int, y: int): int =&gt; x + y</code>. Single-argument shorthand: <code>let square = x =&gt; x * x</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a variant type?",
  "<code>type result&lt;'a&gt; = Ok('a) | Error(string)</code>. Use: <code>let r = Ok(42)</code>. Pattern match: <code>switch r { | Ok(v) =&gt; v | Error(_) =&gt; 0 }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a record type?",
  "<code>type user = { name: string, age: int, email: option&lt;string&gt; }</code>. Create: <code>let u = {name: \"Alice\", age: 30, email: Some(\"a@b.com\")}</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you pattern match on an option?",
  "<code>switch maybeValue { | Some(v) =&gt; Js.log(v) | None =&gt; Js.log(\"nothing\") }</code>. Or use <code>Belt.Option.getWithDefault(maybeValue, defaultValue)</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you work with arrays?",
  "<code>let arr = [1, 2, 3]</code>. Methods via <code>Array</code> or <code>Belt.Array</code>: <code>arr-&gt;Array.map(x =&gt; x * 2)-&gt;Array.toReversed</code>. Arrays are mutable in the JS sense but used immutably in ReScript.",
  ["L1_mechanics"])

c("CoreOps", "How do you do string interpolation?",
  "<code>let greet = `Hello, ${name}!`</code> — uses backtick strings with <code>${}</code> syntax. For multi-line: backtick strings support newlines.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a React component?",
  "<code>@react.component<br>let make = (~name: string) =&gt; &lt;div&gt; {React.string(`Hello ${name}`)} &lt;/div&gt;</code>. Props are labeled arguments (<code>~name</code>). <code>React.string</code> converts ReScript strings to React elements.",
  ["L1_mechanics"])

c("CoreOps", "How do you use React hooks?",
  "<code>let (count, setCount) = React.useState(() =&gt; 0)</code>. <code>React.useEffect(() =&gt; { ... None })</code>. Return <code>None</code> for no cleanup, <code>Some(() =&gt; cleanup())</code> for cleanup.",
  ["L1_mechanics"])

c("CoreOps", "How do you bind to a JavaScript module?",
  "<code>@module(\"lodash\") external debounce: (('a =&gt; 'b), int) =&gt; ('a =&gt; 'b) = \"debounce\"</code>. For default imports: <code>@module(\"react\")</code>. For relative: <code>@module(\"./utils\")</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a new ReScript project?",
  "<code>npx create-rescript-app my-app</code> or manually: <code>npm init &amp;&amp; npm install rescript @rescript/react</code>. Config in <code>rescript.json</code>. Compile: <code>npx rescript build -w</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you run tests in ReScript?",
  "Use <code>@rescript/core</code>'s <code>Assert</code> module or Vitest/Jest bindings. <code>Assert.equal(actual, expected)</code>. Or use <code>Belt.Test</code> / <code>rescript-ava</code>.",
  ["L1_mechanics"])

# === TYPES ===

c("Types", "What are labeled arguments?",
  "Named, unordered function arguments: <code>let greet = (~name, ~age) =&gt; { ... }</code>. Call: <code>greet(~age=30, ~name=\"Alice\")</code>. Optional: <code>~name=?</code> — becomes <code>option</code>.",
  ["L1_mechanics"])

c("Types", "What is <code>unboxed</code> in ReScript?",
  "<code>@unboxed type meters = Meters(int)</code> — the wrapper is zero-cost at runtime (no object allocation). Used for newtypes that compile to the underlying JS value directly.",
  ["L3_design"])

c("Types", "What is a polymorphic variant?",
  "<code>type color = [#red | #green | #blue | #hex(string)]</code>. Unlike regular variants, polymorphic variants don't need pre-declaration and can be shared across modules without importing the type.",
  ["L1_mechanics"])

c("Types", "What is a module type / interface?",
  "<code>module type Counter = { let get: unit =&gt; int; let increment: unit =&gt; unit }</code>. Defines a contract that modules must satisfy. Used for dependency injection and abstraction.",
  ["L2_composition"])

# === PATTERNS ===

c("Patterns", "What is the result type pattern?",
  "<code>type result&lt;'a, 'e&gt; = Ok('a) | Error('e)</code>. Replace exceptions with explicit error handling. Chain with switch or helper functions. Similar to Rust's Result.",
  ["L2_composition"])

c("Patterns", "What is the reducer/useReducer pattern in ReScript React?",
  "<code>type action = Increment | Decrement | Set(int)</code>. <code>let (state, dispatch) = React.useReducer((state, action) =&gt; switch action { | Increment =&gt; state + 1 ... }, 0)</code>.",
  ["L2_composition"])

c("Patterns", "What is the variant-as-state-machine pattern?",
  "<code>type remoteData&lt;'a&gt; = NotAsked | Loading | Done('a) | Error(string)</code>. Render different UI for each state. Forces handling all states — no more <code>isLoading &amp;&amp; data &amp;&amp; error</code> confusion.",
  ["L2_composition"])

c("Patterns", "What is the functor pattern (parameterized modules)?",
  "<code>module Make = (Config: ConfigType) =&gt; { ... }</code>. Parameterize a module by another module. Similar to dependency injection at the module level. Used in ReScript's Map/Set implementations.",
  ["L3_design"])

# === GOTCHAS ===

c("Gotchas", "Why does my ReScript component not re-render?",
  "ReScript's records are compared by reference. If you 'update' by mutating, React won't see the change. Always use spread: <code>{...old, field: newValue}</code>. For lists, always create a new list reference.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>Js.log</code> print <code>[object Object]</code> for records?",
  "ReScript records compile to JS objects without <code>toString</code>. Use <code>Js.log(value-&gt;Js.Json.stringifyAny)</code> or the <code>debug</code> function from <code>@rescript/core</code> for structured logging.",
  ["L4_diagnosis"])

c("Gotchas", "What is the uncurried vs curried function gotcha?",
  "By default, ReScript functions are curried. <code>let add = (a, b) =&gt; a + b</code> compiles to <code>function add(a) { return function(b) { return a + b } }</code>. This can cause issues with JS interop expecting uncurried functions. Use <code>@uncurried</code> for JS-friendly output.",
  ["L4_diagnosis"])

c("Gotchas", "Why do I get 'The type of this module is not allowed'?",
  "Some ReScript module types can't be used because of OCaml type system restrictions. Use an interface file (<code>.resi</code>) to define the public API instead, or restructure your types.",
  ["L4_diagnosis"])

c("Gotchas", "How do you handle nullable React refs?",
  "Use <code>React.useRef(Js.Nullable.null)</code>. Check: <code>switch ref.current-&gt;Js.Nullable.toOption { | Some(el) =&gt; ... | None =&gt; ... }</code>. ReScript's option wrapping of JS nulls.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "What is <code>@genType</code> and why use it?",
  "Generates TypeScript/Flow type declarations from ReScript source. Enables seamless ReScript ←→ TypeScript interop in mixed codebases. Auto-generates <code>.ts</code> files from ReScript exports.",
  ["L6_innovation"])

c("Expert", "What is the difference between <code>Array</code> and <code>Belt.Array</code>?",
  "Belt is ReScript's standard library (faster, more functional APIs, immutable-style operations). <code>Array</code> is a thin wrapper over JS array methods. Belt is the preferred choice for ReScript development.",
  ["L5_opinion"])

c("Expert", "How do you write a custom ReScript PPX (preprocessor)?",
  "PPXes transform the AST at compile time. Written in OCaml. Example: <code>@graphql</code> PPX that generates typed functions from GraphQL queries. ReScript's <code>@react.component</code> is itself a PPX.",
  ["L6_innovation"])

c("Expert", "What is the module system's open/include/extension story?",
  "<code>open Module</code>: bring all names into scope. <code>include Module</code>: copy all definitions into current module (mixin-like). <code>module X = Module</code>: alias. Extension: <code>module type TypeName = ...</code> for module interfaces.",
  ["L3_design"])

c("Expert", "How do you structure a production ReScript + React codebase?",
  "Separate: <code>Core</code> (pure logic, types, business rules), <code>UI</code> (React components), <code>Bindings</code> (JS interop). Core should be testable without React. Keep components thin — delegate logic to Core modules. Use variants for state management over ad-hoc booleans.",
  ["L5_opinion"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
