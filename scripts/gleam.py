import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Gleam"

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
    "Workflows":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Workflows"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Expert"),
    "Internals":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Internals"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === GLEAM FUNDAMENTALS ===

c("Fundamentals", "What is Gleam?",
  "A statically typed, functional programming language that compiles to Erlang (BEAM) and JavaScript. Combines ML-style types with Erlang's fault-tolerant runtime.",
  ["L0_primitives"])

c("Fundamentals", "What makes Gleam different from Elixir?",
  "Gleam is statically typed (ML/Hindley-Milner) while Elixir is dynamically typed. Gleam compiles to both Erlang and JS. Gleam has no macros — it's simpler and more explicit.",
  ["L0_primitives"])

c("Fundamentals", "What is the type system in Gleam?",
  "Static, strong, inferred (Hindley-Milner). The compiler catches type errors before runtime. You can annotate types explicitly or let the compiler infer them.",
  ["L0_primitives"])

c("Fundamentals", "What are Gleam's two compilation targets?",
  "Erlang (BEAM VM) and JavaScript (Node.js/Deno/browser). The same Gleam code can run on both targets, using target-specific externals for platform APIs.",
  ["L0_primitives"])

c("Fundamentals", "What is a Gleam module?",
  "A file containing functions and types. Defined implicitly by the file name. Functions are public (<code>pub fn</code>) or private (<code>fn</code>). Imported with <code>import module_name</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is the unit type in Gleam?",
  "<code>Nil</code> — represents no meaningful value. Similar to <code>()</code> in Rust, <code>nil</code> in Elixir. Used for side-effecting functions that don't return data.",
  ["L0_primitives"])

c("Fundamentals", "What is a Result type in Gleam?",
  "<code>Result(value, error)</code> — an enum with variants <code>Ok(value)</code> and <code>Error(error)</code>. Used for error handling instead of exceptions. Enforced by the type system.",
  ["L0_primitives"])

c("Fundamentals", "What is an Option type in Gleam?",
  "<code>Option(value)</code> — an enum with variants <code>Some(value)</code> and <code>None</code>. Replaces nullable values. The compiler forces you to handle both cases.",
  ["L0_primitives"])

c("Fundamentals", "What is pattern matching in Gleam?",
  "The <code>case</code> expression destructures values and matches on constructors: <code>case result { Ok(v) -> v; Error(e) -> panic }</code>. The compiler checks exhaustiveness.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>use</code> expression in Gleam?",
  "Syntactic sugar for callbacks/call-with-current-continuation. Aims to replace monadic <code>flat_map</code> chains with imperative-looking code. Compiles to regular function calls — zero runtime overhead.",
  ["L0_primitives"])

c("Fundamentals", "What is a custom type in Gleam?",
  "Algebraic Data Types: <code>type Animal { Cat(name: String); Dog(age: Int) }</code>. Each variant can hold data. Pattern-matched with <code>case</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is the Gleam build tool?",
  "Gleam's CLI (<code>gleam</code>) handles project creation, building, testing, formatting, and dependency management. No separate Mix/Gradle-like tool needed.",
  ["L0_primitives"])

c("Fundamentals", "What is a tuple in Gleam?",
  "A fixed-size, heterogeneous collection: <code>#(1, \"hello\", True)</code>. Access elements by position with pattern matching: <code>let #(a, b, c) = my_tuple</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is a List in Gleam?",
  "An immutable singly-linked list. Type: <code>List(Int)</code>. Built with <code>[1, 2, 3]</code>. Prepending is <code>O(1)</code>. Module <code>gleam/list</code> provides <code>map</code>, <code>filter</code>, <code>fold</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is a BitArray in Gleam?",
  "A sequence of bits/bytes. Type: <code>BitArray</code>. Used for binary data, network protocols, file I/O. Syntax: <code>&lt;&lt;1, 2, 3&gt;&gt;</code>. Pattern match: <code>&lt;&lt;header:4, body:binary&gt;&gt;</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is an external function in Gleam?",
  "An FFI bridge to the target platform: <code>@external(erlang, \"module\", \"function\")</code> for BEAM, <code>@external(javascript, \"../path.mjs\", \"fnName\")</code> for JS. Allows platform-specific escape hatches.",
  ["L0_primitives"])

c("Fundamentals", "What is the Gleam standard library structure?",
  "Organized by module: <code>gleam/list</code>, <code>gleam/result</code>, <code>gleam/option</code>, <code>gleam/string</code>, <code>gleam/int</code>, <code>gleam/bool</code>, <code>gleam/dict</code>, <code>gleam/set</code>, <code>gleam/io</code>. Minimal but complete.",
  ["L0_primitives"])

c("Fundamentals", "What is a Dict in Gleam?",
  "An immutable key-value map. Type: <code>Dict(key, value)</code>. From <code>gleam/dict</code>. <code>dict.from_list</code>, <code>dict.get</code>, <code>dict.insert</code>, <code>dict.delete</code> — all return new Dicts.",
  ["L0_primitives"])

c("Fundamentals", "What is Gleam's approach to side effects?",
  "Functions are pure by default. Side effects (IO, HTTP, DB) are explicit in the type: functions return <code>Result</code> or use <code>use &lt;-</code> chaining via the <code>gleam/otp/actor</code> module.",
  ["L0_primitives"])

# === GLEAM MECHANICS ===

c("CoreOps", "How do you define a function in Gleam?",
  "<code>pub fn add(x: Int, y: Int) -&gt; Int { x + y }</code> — public. <code>fn helper(x: Int) -&gt; Int { x * 2 }</code> — private (no <code>pub</code>).",
  ["L1_mechanics"])

c("CoreOps", "How do you do a let binding in Gleam?",
  "<code>let x = 42</code> — immutable binding. <code>let assert Ok(val) = result</code> — assertion pattern match (panics on mismatch). <code>let #(a, b) = tuple</code> — destructuring.",
  ["L1_mechanics"])

c("CoreOps", "How do you write a type annotation?",
  "<code>let x: Int = 42</code> or <code>fn name(arg: String) -&gt; Bool { ... }</code>. Most types are inferred; annotate when ambiguous or at public API boundaries.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a custom type (ADT)?",
  "<code>type Color { Red; Green; Blue; Custom(Int, Int, Int) }</code>. Variants can be empty or hold data.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a new project?",
  "<code>gleam new my_project</code> — creates <code>src/</code>, <code>test/</code>, <code>gleam.toml</code>. <code>gleam new --name gleam_project</code> to specify a different package name.",
  ["L1_mechanics"])

c("CoreOps", "How do you run a Gleam project?",
  "<code>gleam run</code> — builds and executes <code>src/PROJECT_NAME.gleam</code>'s <code>main</code> function. <code>gleam run -m my_module</code> to run a different module.",
  ["L1_mechanics"])

c("CoreOps", "How do you run tests?",
  "<code>gleam test</code> — runs all tests. <code>gleam test -- --target=javascript</code> to test the JS target. Tests are in <code>test/</code> with <code>pub fn my_test() { ... }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you add a dependency?",
  "<code>gleam add package_name</code> — adds to <code>gleam.toml</code> and downloads. <code>gleam add --dev gleeunit</code> for dev/test-only dependencies.",
  ["L1_mechanics"])

c("CoreOps", "How do you import a module?",
  "<code>import gleam/list</code> — unqualified access: <code>list.map(...)</code>. <code>import gleam/list.{map}</code> — imports specific function unqualified. <code>import gleam/string as str</code> — aliased import.",
  ["L1_mechanics"])

c("CoreOps", "How do you pattern match with case?",
  "<code>case value { True -&gt; \"yes\"<br> False -&gt; \"no\"<br> }</code> — compiler enforces exhaustive handling of all variants.",
  ["L1_mechanics"])

c("CoreOps", "How do you use the pipe operator?",
  "<code>list |&gt; list.map(fn(x) { x * 2 }) |&gt; list.filter(fn(x) { x &gt; 5 })</code> — passes the result as the FIRST argument to the next function call.",
  ["L1_mechanics"])

c("CoreOps", "How do you write a list literal and prepend?",
  "<code>[1, 2, 3]</code> or <code>[1, ..rest]</code> for destructuring. Prepending: <code>[0, ..list]</code> is <code>O(1)</code>. <code>list.concat</code> for joining, <code>list.append</code> for single element at end (<code>O(n)</code>).",
  ["L1_mechanics"])

c("CoreOps", "How do you define a tuple literal?",
  "<code>#(1, \"hello\", True)</code> — comma-separated values prefixed with <code>#</code>. Type is inferred from elements.",
  ["L1_mechanics"])

c("CoreOps", "How do you write a string and interpolate?",
  "<code>\"Hello, \" &lt;&gt; name</code> — concatenation. <code>\"Hello, \" &lt;&gt; string.inspect(42)</code> — for interpolation. No built-in interpolation syntax; use <code>&lt;&gt;</code> with <code>string.inspect</code> or <code>int.to_string</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you write an anonymous function?",
  "<code>fn(x) { x * 2 }</code> — single arg. <code>fn(x, y) { x + y }</code> — multiple args. Type is inferred: <code>fn(Int) -&gt; Int</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you handle Result values?",
  "<code>case result { Ok(v) -&gt; v; Error(_) -&gt; default }</code> or <code>result.unwrap(result, default)</code> or <code>result.map</code> + <code>result.try</code> for chaining.",
  ["L1_mechanics"])

c("CoreOps", "How do you unwrap an Option?",
  "<code>option.unwrap(opt, default)</code> — provides fallback. <code>case opt { Some(v) -&gt; v; None -&gt; default }</code> for explicit handling.",
  ["L1_mechanics"])

c("CoreOps", "How do you write an if expression?",
  "<code>case condition { True -&gt; \"yes\"; False -&gt; \"no\" }</code> — Gleam has no <code>if/else</code> keyword; use <code>case</code> on booleans instead.",
  ["L1_mechanics"])

c("CoreOps", "How do you convert between types?",
  "<code>int.to_string(42)</code>, <code>string.to_int(\"42\")</code> — explicit functions in type modules. No implicit coercion.",
  ["L1_mechanics"])

c("CoreOps", "How do you format Gleam code?",
  "<code>gleam format</code> — formats all <code>.gleam</code> files in the project. No configuration — Gleam enforces a single canonical style. Use in CI with <code>gleam format --check</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you write a record constructor?",
  "For <code>type Person { Person(name: String, age: Int) }</code>, construct with <code>Person(name: \"Alice\", age: 30)</code>. Pattern match: <code>let Person(name: n, age: a) = person</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you use the <code>use</code> expression?",
  "<code>use &lt;- result</code> — unwraps <code>Ok</code> or early-returns <code>Error</code> from the enclosing function. <code>use profile &lt;- fetch_user(id)</code>. Must be the last expression in a block.",
  ["L1_mechanics"])

c("CoreOps", "How do you write an assertion?",
  "<code>let assert Ok(val) = some_result</code> — panics if pattern doesn't match. Use for invariants you're certain of. <code>let assert [first, ..] = list</code> — assertion destructuring.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a constant?",
  "<code>pub const port_number = 8080</code> — constant values available at compile time. Types must be <code>Int</code>, <code>Float</code>, <code>String</code>, or <code>Bool</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you work with BitArrays?",
  "<code>let raw = &lt;&lt;1, 2, 3&gt;&gt;</code> — byte array. <code>let &lt;&lt;first, rest:binary&gt;&gt; = raw</code> — pattern match header byte. <code>bit_array.byte_size(raw)</code> — get length.",
  ["L1_mechanics"])

# === GLEAM PATTERNS ===

c("Patterns", "What is the Result chaining pattern?",
  "<code>result.try(fn() { step1() }, fn(v) { step2(v) })</code> or with <code>use</code>: <code>use a &lt;- step1(); use b &lt;- step2(a); Ok(b)</code>. Short-circuits on first Error.",
  ["L2_composition"])

c("Patterns", "How do you use the <code>use</code> pattern for error handling?",
  "Each <code>use &lt;-</code> unwraps a Result: if Ok, continues; if Error, returns early. The enclosing function must return <code>Result(a, e)</code>. Replaces nested case chains.",
  ["L2_composition"])

c("Patterns", "What is the state monad pattern in Gleam?",
  "Passing state explicitly through functions: <code>fn step(state) -&gt; Result(#(new_state, output), error)</code>. Gleam's purity makes state threading explicit. Use <code>use</code> to flatten.",
  ["L2_composition"])

c("Patterns", "What is the validation pattern using Result?",
  "Accumulate errors across multiple validations with <code>result.all([validate_name(n), validate_email(e)])</code>. Returns Ok(list) or Error(first_failure). For all errors, use a custom accumulate function.",
  ["L2_composition"])

c("Patterns", "What is the opaque type pattern?",
  "<code>pub opaque type UserId { UserId(Int) }</code> with a private constructor and public constructor function. Prevents creating invalid UserIds from raw ints. Use <code>pub fn new(id: Int) -&gt; Result(UserId, String)</code>.",
  ["L3_design"])

c("Patterns", "What is the dependency injection pattern in Gleam?",
  "Pass dependencies as function arguments (no DI frameworks): <code>fn handle(db: Database, email: EmailSender, req: Request) { ... }</code>. Pure functions make this explicit and testable.",
  ["L3_design"])

c("Patterns", "How do you handle mutable state in Gleam?",
  "Use OTP actors (processes): <code>gleam/otp/actor</code>. Actors hold state and respond to messages. Gleam wraps Erlang's GenServer. No global mutable variables.",
  ["L2_composition"])

c("Patterns", "What is the gleam/otp supervisor pattern?",
  "<code>pub fn main() { otp.supervisor.start(fn() { ... }) }</code> — starts a supervisor tree. Children are actors. If a child crashes, the supervisor restarts it according to strategy.",
  ["L2_composition"])

c("Patterns", "How do you handle JSON in Gleam?",
  "Use <code>gleam/json</code>: <code>json.decode(input, my_decoder)</code>. Decoders are composable functions: <code>fn decoder() { dynamic.decode2(T, dynamic.field(\"name\", dynamic.string), dynamic.field(\"age\", dynamic.int)) }</code>.",
  ["L2_composition"])

c("Patterns", "What is the Gleam dynamic decoder pattern?",
  "Decoders describe how to parse untyped <code>Dynamic</code> data into typed Gleam values. Compose with <code>dynamic.decode1</code>, <code>dynamic.decode2</code>, etc. Also <code>dynamic.list</code>, <code>dynamic.optional</code>.",
  ["L2_composition"])

# === GLEAM DIAGNOSIS ===

c("Gotchas", "What is the 'Infinite type' compiler error in Gleam?",
  "Occurs when a recursive type definition has no variant without self-reference. Fix by adding a non-recursive variant or using the <code>@target(erlang)</code>/<code>@target(javascript)</code> pattern.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>use</code> not work in all positions?",
  "<code>use</code> must be the last statement in a block (before the closing <code>}</code>). It captures all following code as a callback. Place it just before the final expression in a function body.",
  ["L4_diagnosis"])

c("Gotchas", "Why is my list append slow?",
  "<code>list.append(list, item)</code> is <code>O(n)</code> because lists are singly-linked. For repeated appends, build the list in reverse with prepend (<code>O(1)</code>) then <code>list.reverse</code> at the end.",
  ["L4_diagnosis"])

c("Gotchas", "How does Gleam handle nil/null?",
  "Gleam has NO null. Use <code>Option(a)</code> for optional values. <code>Nil</code> is the unit type (like void), not null. Compiler guarantees no null-pointer exceptions.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my external function fail on JavaScript target?",
  "Externals must be defined per-target: <code>@external(erlang, ...)</code> AND a separate <code>@external(javascript, ...)</code> for JS. Missing one causes a compile error only for that target.",
  ["L4_diagnosis"])

c("Gotchas", "What happens if I shadow a variable?",
  "Gleam allows shadowing: <code>let x = 1; let x = 2</code> — the second <code>x</code> shadows the first. This can cause confusing bugs. The compiler warns about unused variables to help catch mistakes.",
  ["L4_diagnosis"])

c("Gotchas", "Why is my <code>case</code> expression not exhaustive?",
  "The compiler checks that all variants are covered. For custom types, you must handle every variant or use a catch-all <code>_ -&gt;</code>. Missing variants cause a compile error.",
  ["L4_diagnosis"])

c("Gotchas", "How does Gleam format work? Is it configurable?",
  "No. Gleam enforces exactly one formatting style. <code>gleam format</code> has zero configuration options. This is intentional to end style debates and make all Gleam code look the same.",
  ["L5_opinion"])

c("Gotchas", "Why can't I compare different types?",
  "Gleam does not have operator overloading or implicit comparison. <code>1 == \"hello\"</code> is a type error. Use explicit conversion: <code>int.to_string(x) == str</code>.",
  ["L4_diagnosis"])

c("Gotchas", "What causes the 'Variable already used' error in case?",
  "You cannot reuse a variable binding across multiple case branches: <code>case x { a -&gt; a; a -&gt; a }</code> — the second <code>a</code> conflicts. Each branch must use distinct variable names for their bindings.",
  ["L4_diagnosis"])

# === GLEAM EXPERT ===

c("Expert", "When should you use Gleam vs Elixir?",
  "Gleam: when you want static types, compile-time guarantees, and a simpler language. Elixir: when you need macros, metaprogramming, or the larger ecosystem (Phoenix, Nerves). Both run on BEAM.",
  ["L5_opinion"])

c("Expert", "What is the Gleam Wisp framework?",
  "A web framework for Gleam inspired by Express/Sinatra. Routes: <code>wisp.route(\"/\", fn(_) -&gt; wisp.text_response(\"Hello\") end)</code>. Lighter than Phoenix, compiles to both BEAM and JS.",
  ["L5_opinion"])

c("Expert", "What is the Lustre framework for Gleam?",
  "A frontend framework for Gleam targeting JavaScript. Inspired by Elm's Model-View-Update architecture. Compiles Gleam to JS for browser UIs. Used for SPAs and web components.",
  ["L5_opinion"])

c("Expert", "How does Gleam target both Erlang and JavaScript?",
  "The compiler generates Erlang source or JavaScript from the same AST. Target-specific code is handled via <code>@external</code> annotations. You can write once, run on both platforms.",
  ["L3_design"])

c("Expert", "What are Gleam's interop capabilities with Erlang?",
  "Gleam compiles to Erlang AST, so it can call any Erlang/Elixir library. Use <code>@external(erlang, \"module\", \"function\")</code>. Gleam's types make interop safer by wrapping dynamic Erlang functions.",
  ["L3_design"])

c("Expert", "What is the Gleam actor model implementation?",
  "<code>gleam/otp/actor</code> wraps Erlang's GenServer. <code>actor.start(fn() -&gt; actor.State(state) end)</code>, handle messages with <code>actor.continue</code>, <code>actor.reply</code>. Type-safe actor model.",
  ["L3_design"])

c("Expert", "What is 'gleam compile-package' and why use it?",
  "Precompiles all modules of a package into a single Erlang BEAM file or JS bundle. Faster startup for production deployments. Used in release pipelines.",
  ["L6_innovation"])

c("Expert", "How do you write a custom decoder for complex JSON?",
  "Decoders are functions <code>Dynamic -&gt; Result(a, DecodeError)</code>. Compose with <code>dynamic.decodeN</code> or write manually: <code>fn(dyn) { case dynamic.field(\"type\", dynamic.string)(dyn) { Ok(\"user\") -&gt; decode_user(dyn); _ -&gt; Error(DecodeError(...)) } }</code>.",
  ["L6_innovation"])

c("Expert", "What is Gleam's approach to code generation?",
  "No built-in macros. Rely on external code generators or build tools. Use <code>@external</code> for platform interop. The language is intentionally simple — if you need macros, consider Elixir.",
  ["L5_opinion"])

c("Expert", "How do you benchmark Gleam vs Elixir on the same task?",
  "Gleam compiles to Erlang — performance is nearly identical to hand-written Erlang for pure functions. Static types enable more compiler optimizations. For JS target, Gleam generates efficient, readable JS.",
  ["L5_opinion"])

# === GLEAM INTERNALS ===

c("Internals", "How does the Gleam compiler work?",
  "Compiles <code>.gleam</code> -&gt; AST -&gt; type checking -&gt; Erlang AST or JavaScript AST -&gt; source code. Written in Rust for speed. Produces readable Erlang/JS output.",
  ["L6_innovation"])

c("Internals", "What is the Gleam Language Server (GLS)?",
  "LSP server written in Rust that provides autocomplete, go-to-definition, inline errors, and hover documentation. Integrates with VS Code, Vim, Emacs. Zero configuration needed.",
  ["L6_innovation"])

c("Internals", "How does Gleam's type inference algorithm work?",
  "Hindley-Milner with let-polymorphism. Types are inferred bottom-up through the AST. The compiler tracks type constraints and unifies them. Type errors show the specific constraint that couldn't be satisfied.",
  ["L6_innovation"])

c("Internals", "How does the <code>use</code> expression desugar?",
  "<code>use x &lt;- expr; body</code> desugars to <code>expr(fn(x) { body })</code>. The expression must be a function that takes a callback as its last argument. This is purely syntactic — no runtime overhead.",
  ["L6_innovation"])

c("Internals", "What is the Gleam package ecosystem (Hex)?",
  "Gleam packages are published to Hex.pm with <code>gleam publish</code>. The <code>gleam.toml</code> defines metadata. Compiler targets both Erlang and JS from a single package. <code>gleam docs build</code> generates HexDocs.",
  ["L6_innovation"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
