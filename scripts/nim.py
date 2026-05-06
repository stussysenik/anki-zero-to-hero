import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Nim"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Types":        genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Type-System"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === NIM FUNDAMENTALS ===

c("Fundamentals", "What is Nim?",
  "A statically typed, compiled systems programming language with Python-like syntax. Compiles to C, C++, or JavaScript. Features: metaprogramming, compile-time function evaluation, GC (optional), and deterministic memory management.",
  ["L0_primitives"])

c("Fundamentals", "What makes Nim's syntax distinctive?",
  "Python-inspired (indentation-sensitive), with strong static typing. <code>var x = 42</code> — type is inferred. Case-insensitive and underscore-insensitive identifiers. First character case determines scope: lowercase = public, uppercase + first non-uppercase = private in modules.",
  ["L0_primitives"])

c("Fundamentals", "How does Nim compile?",
  "Nim source → Nim VM (compile-time execution) → C/C++/JS code → native binary. The C code is optimized by the backend compiler (GCC/Clang). This gives portability to any platform with a C compiler.",
  ["L0_primitives"])

c("Fundamentals", "What are Nim's memory management options?",
  "Default: optional GC (deferred reference counting + mark-and-sweep). Opt-out: <code>--mm:orc</code> for ORC (cycle collector + destructor-based). <code>--mm:arc</code> for deterministic ARC. Manual: <code>--mm:none</code> with manual <code>alloc</code>/<code>dealloc</code>. ORC/ARC enable move semantics and destructors.",
  ["L0_primitives"])

c("Fundamentals", "What is a template in Nim?",
  "Inline code substitution at compile time. <code>template twice(x: untyped): untyped = (x; x)</code>. Unlike procedures, templates don't introduce new scopes or evaluate arguments. Used for DSL-like syntax and avoiding function call overhead.",
  ["L0_primitives"])

c("Fundamentals", "What is a macro in Nim?",
  "A compile-time function that takes an AST (NimNode) and returns a new AST. <code>macro myAssert(cond: bool) = ...</code>. Full metaprogramming — you manipulate the syntax tree. Macros execute at compile time in the Nim VM.",
  ["L0_primitives"])

c("Fundamentals", "What is <code>distinct</code> type in Nim?",
  "A type-safe alias that shares the same runtime representation but is NOT implicitly convertible. <code>type Dollars = distinct float</code>. Compiler prevents mixing Dollars and float. Zero overhead — erased at runtime.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>var</code>, <code>let</code>, <code>const</code> difference?",
  "<code>var</code>: mutable variable. <code>let</code>: immutable runtime value (computed once). <code>const</code>: compile-time constant (evaluated during compilation). Use <code>let</code> by default, <code>var</code> when mutation needed, <code>const</code> for compile-time values.",
  ["L0_primitives"])

c("Fundamentals", "What is an <code>enum</code> in Nim?",
  "<code>type Color = enum Red, Green, Blue</code> — generates ordered integer values starting at 0. With values: <code>type HttpCode = enum ok = 200, notFound = 404</code>. Can iterate: <code>for c in Color:</code>. Supports <code>ord</code> and <code>succ</code>/<code>pred</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is the Nim standard library called?",
  "The stdlib, imported as <code>import std/[strutils, os, json]</code>. Comprehensive: strings, OS, JSON, HTTP, async, cryptography, databases, regular expressions. Nimble is the package manager; <code>nimble install pkg</code>.",
  ["L0_primitives"])

# === NIM CORE OPERATIONS ===

c("CoreOps", "How do you declare a variable?",
  "<code>var x = 42</code> — mutable, type inferred. <code>var x: int = 42</code> — explicit type. <code>let y = \"hello\"</code> — immutable. <code>const pi = 3.14</code> — compile-time constant.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a procedure (function)?",
  "<code>proc add(a, b: int): int = return a + b</code>. Shorthand with <code>=</code>: <code>proc add(a, b: int): int = a + b</code> (implicit return). <code>proc greet(name: string) = echo \"Hello, \", name</code> (no return).",
  ["L1_mechanics"])

c("CoreOps", "How do you write a for loop?",
  "<code>for i in 0..&lt;10: echo i</code> — 0 to 9. <code>for item in mySeq: echo item</code> — iterate over collection. <code>for key, val in pairs(myTable): echo key, val</code>. <code>..</code> is inclusive, <code>..&lt;</code> exclusive.",
  ["L1_mechanics"])

c("CoreOps", "How do you write an if/elif/else?",
  "<code>if x &gt; 0: echo \"positive\"<br>elif x &lt; 0: echo \"negative\"<br>else: echo \"zero\"</code>. <code>if</code> is an expression: <code>let s = if x &gt; 0: \"pos\" else: \"neg\"</code>. <code>case</code> for pattern matching: <code>case x of 0: echo 0; of 1..9: echo \"digit\"</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a sequence (dynamic array)?",
  "<code>var s: seq[int] = @[1, 2, 3]</code>. <code>var s = newSeq[int](10)</code> — uninitialized of length 10. <code>s.add(4)</code>, <code>s.del(0)</code>, <code>s.insert(5, 2)</code>, <code>s[0] = 99</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a table (dictionary)?",
  "<code>import tables</code>. <code>var t = {\"a\": 1, \"b\": 2}.toTable</code> or <code>initTable[string, int]()</code>. <code>t[\"c\"] = 3</code>, <code>t.hasKey(\"a\")</code>, <code>t.getOrDefault(\"z\", 0)</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you import modules?",
  "<code>import std/strutils</code> — full module. <code>from std/strutils import join</code> — specific symbol. <code>import std/[os, strutils, json]</code> — multiple. <code>import mymodule</code> — local module (<code>mymodule.nim</code>).",
  ["L1_mechanics"])

c("CoreOps", "How do you export symbols from a module?",
  "Use <code>*</code> suffix: <code>proc publicProc*() = ...</code> — exported. <code>proc privateProc() = ...</code> — not exported. <code>type MyType* = object</code> — exported type. No explicit <code>export</code> keyword; the <code>*</code> marks public.",
  ["L1_mechanics"])

c("CoreOps", "How do you handle optional values?",
  "Use <code>Option[T]</code>: <code>var x: Option[int] = some(42)</code> or <code>none(int)</code>. Unwrap: <code>if x.isSome: echo x.get</code> or <code>let y = x.get(0)</code> (with default). No implicit null — <code>Option</code> is explicit.",
  ["L1_mechanics"])

c("CoreOps", "How do you create and compile a Nim project?",
  "<code>nimble init myproject</code> — creates project skeleton. Compile: <code>nim c myfile.nim</code>. Run: <code>nim r myfile.nim</code>. Release: <code>nim c -d:release myfile.nim</code>. JS target: <code>nim js myfile.nim</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you do string operations?",
  "<code>\"Hello\" &amp; \" World\"</code> — concatenation. <code>\"$1, $2!\" % [\"Hello\", \"World\"]</code> — format. <code>strutils.join([\"a\", \"b\"], \",\")</code>. <code>strutils.split(\"a,b,c\", \",\")</code>. <code>strutils.parseInt(\"42\")</code>.",
  ["L1_mechanics"])

# === TYPE SYSTEM ===

c("Types", "What is a <code>tuple</code> in Nim?",
  "<code>var t = (name: \"Alice\", age: 30)</code>. Access: <code>t.name</code>, <code>t[0]</code>. Unnamed: <code>(1, \"hello\")</code>. Fields can be mutable: <code>t.age = 31</code>. Type: <code>tuple[name: string, age: int]</code>.",
  ["L1_mechanics"])

c("Types", "What is an <code>object</code> type in Nim?",
  "<code>type Person = object name: string; age: int</code>. Reference object: <code>type Person = ref object</code> — heap-allocated, managed by GC/ARC. Value object (default) — stack-allocated. Use <code>ref</code> for complex graphs, value for small POD.",
  ["L1_mechanics"])

c("Types", "What are generic procedures/types?",
  "<code>proc first[T](s: seq[T]): T = s[0]</code> — works with any type. <code>type Stack[T] = object items: seq[T]</code>. Generic constraints: <code>proc sort[T: SomeNumber](s: var seq[T])</code>. Compile-time specialization; zero runtime overhead.",
  ["L3_design"])

c("Types", "What is type inference in Nim?",
  "The compiler deduces types from context: <code>let x = 42</code> → int. <code>let y = \"hello\"</code> → string. <code>for item in myList</code> → element type. Parameters usually need annotations, return types often inferred. <code>auto</code> can defer type resolution.",
  ["L1_mechanics"])

# === PATTERNS ===

c("Patterns", "What is the UFCS (Uniform Function Call Syntax) pattern?",
  "<code>x.foo(y)</code> is equivalent to <code>foo(x, y)</code>. Enables method-chaining syntax without methods belonging to types. <code>seq.map(f).filter(g)</code> — chains operations as if they were methods.",
  ["L2_composition"])

c("Patterns", "What is the result type pattern for error handling?",
  "Nim's <code>Result[T, E]</code> from <code>std/options</code> or custom: <code>type Result[T] = object case ok: bool of true: value: T of false: error: string</code>. Returns success/failure without exceptions. Chain with if/elif on the discriminator.",
  ["L2_composition"])

c("Patterns", "What is the converter pattern?",
  "<code>converter toInt(s: string): int = parseInt(s)</code> — implicitly called when type mismatch. <code>let x: int = \"42\"</code> automatically invokes converter. Use sparingly — can make code unclear.",
  ["L2_composition"])

c("Patterns", "What is the pragma pattern?",
  "Metadata annotations: <code>{.inline.}</code>, <code>{.exportc.}</code>, <code>{.threadvar.}</code>, <code>{.compileTime.}</code>. Pragmas modify compiler behavior. Custom pragmas: <code>{.myCustom: \"value\".}</code>. Used extensively for FFI and optimization.",
  ["L3_design"])

c("Patterns", "What is the async/await pattern in Nim?",
  "<code>import std/asyncdispatch</code>. <code>proc fetch(): Future[string] {.async.} = ...</code>. <code>let data = await fetch()</code>. Non-blocking I/O with <code>asyncdispatch</code>. <code>waitFor</code> to run sync code calling async procs.",
  ["L2_composition"])

# === GOTCHAS ===

c("Gotchas", "Why does <code>echo</code> behave differently with different types?",
  "<code>echo</code> uses <code>$</code> (stringify) on arguments. Some types have custom <code>$</code> procedures, others use default. For debugging, <code>echo repr(x)</code> for detailed representation. For custom types, implement <code>$</code> proc.",
  ["L4_diagnosis"])

c("Gotchas", "What is the off-by-one gotcha with <code>..</code> vs <code>..&lt;</code>?",
  "<code>0..5</code> includes 5 (6 elements). <code>0..&lt;5</code> excludes 5 (5 elements). <code>a..b</code> is inclusive-inclusive, <code>a..&lt;b</code> is inclusive-exclusive. Python users beware: Nim's <code>..</code> is NOT Python's <code>range()</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>var</code> inside <code>proc</code> become a global?",
  "Top-level <code>var</code> creates a module-level global. Inside procs, <code>var</code> creates a local. But if you're at module scope inside a <code>when</code> block, the scope can be surprising. Be explicit about scope.",
  ["L4_diagnosis"])

c("Gotchas", "What is the case-insensitivity / underscore-insensitivity gotcha?",
  "<code>myVar</code>, <code>myvar</code>, <code>my_var</code> all refer to the SAME identifier. Can cause subtle bugs if you expect them to be distinct. The style is: capitalize the first letter of each word (e.g., <code>myVariable</code>), no underscores.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>return</code> not always return?",
  "<code>return</code> returns from the enclosing procedure. But in nested blocks (try, for, when), <code>return</code> still returns from the proc, not the block. This is correct but can surprise newcomers.",
  ["L4_diagnosis"])

c("Gotchas", "What happens with forward declarations and recursive types?",
  "Nim requires order-independent declarations. <code>type A = ref object; b: B; type B = ref object; a: A</code> — this works because both are forward-declared. But <code>A = object; b: B</code> (without ref) fails because object size can't be determined.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "What is Nim's compile-time function execution (CTFE)?",
  "Any pure proc can be executed at compile time: <code>const result = complexComputation(42)</code>. The Nim VM runs the proc during compilation. Enables computing tables, parsing files, generating code at compile time.",
  ["L6_innovation"])

c("Expert", "What is the <code>sink</code> and <code>lent</code> type system for move semantics?",
  "<code>sink T</code>: the procedure takes ownership (moved into). <code>lent T</code>: borrowed reference, no ownership. Part of Nim's ORC/ARC memory model. Enables zero-copy designs without manual memory management.",
  ["L6_innovation"])

c("Expert", "What is Nim's FFI (Foreign Function Interface)?",
  "Call C/C++/JS directly: <code>{.importc.}</code> for C imports, <code>{.exportc.}</code> to expose Nim to C. Header translation: <code>c2nim</code> tool. <code>{.compile: \"file.c\".}</code> to compile alongside. Use <code>{.header: \"lib.h\".}</code> for header import.",
  ["L3_design"])

c("Expert", "When should you choose Nim over other languages?",
  "Nim: when you want Python-like syntax with C-like performance, rapid prototyping that becomes production code, metaprogramming-heavy domains (DSLs, codegen), and when you dislike Rust's borrow checker but want memory safety.",
  ["L5_opinion"])

c("Expert", "What is metaprogramming in Nim?",
  "Three levels: 1) Templates: inline code substitution. 2) Macros: AST transformation at compile time. 3) Compile-time execution: run any proc at compile time to generate data/code. This continuum enables domain-specific optimizations impossible in most languages.",
  ["L6_innovation"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
