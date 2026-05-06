import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "OCaml"

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

# === OCAML FUNDAMENTALS ===

c("Fundamentals", "What is OCaml?",
  "A pragmatic, multi-paradigm programming language extending the Caml dialect of ML. Features strong static typing, type inference, algebraic data types, pattern matching, and a powerful module system. Compiles to native code and bytecode.",
  ["L0_primitives"])

c("Fundamentals", "What is the Hindley-Milner type system?",
  "The type inference algorithm used by OCaml (and ML family). Deduces types automatically without annotations. If it compiles, there are no type errors. Sound and complete within its domain.",
  ["L0_primitives"])

c("Fundamentals", "What is a sum type / variant in OCaml?",
  "A tagged union: <code>type shape = Circle of float | Rectangle of float * float | Point</code>. Each variant can carry data. Pattern matching forces handling all cases — no null pointer exceptions.",
  ["L0_primitives"])

c("Fundamentals", "What is a product type in OCaml?",
  "Tuples: <code>(3, \"hello\", true)</code> = <code>int * string * bool</code>. Records: named product types: <code>type point = { x: float; y: float }</code>. Both are checked at compile time.",
  ["L0_primitives"])

c("Fundamentals", "What is pattern matching in OCaml?",
  "<code>match value with | Pattern1 -&gt; expr1 | Pattern2 -&gt; expr2</code>. Destructures tuples, variants, records, lists, and literals. Compiler warns on non-exhaustive matches — prevents runtime errors.",
  ["L0_primitives"])

c("Fundamentals", "What is a functor in OCaml?",
  "A module parameterized by another module — 'functions from modules to modules.' <code>module Make (M: S) = struct ... end</code>. Enables parametric polymorphism at the module level, like generics for modules.",
  ["L0_primitives"])

c("Fundamentals", "What is the OCaml module system?",
  "Two levels: structures (implementations) and signatures (interfaces). <code>module M = struct ... end</code> defines a structure. <code>module type S = sig ... end</code> defines a signature. <code>module M: S</code> constrains a module by its signature.",
  ["L0_primitives"])

c("Fundamentals", "What is a GADT in OCaml?",
  "Generalized Algebraic Data Type — allows type parameters to vary per constructor. <code>type _ expr = Int: int -&gt; int expr | Bool: bool -&gt; bool expr | Eq: 'a expr * 'a expr -&gt; bool expr</code>. Enables typed ASTs where pattern matching refines types.",
  ["L3_design"])

c("Fundamentals", "What is the difference between <code>'a list</code> and <code>'a array</code>?",
  "List: immutable, singly-linked, <code>O(1)</code> prepend, <code>O(n)</code> random access. Syntax: <code>[1; 2; 3]</code> or <code>1 :: 2 :: 3 :: []</code>. Array: mutable, fixed-size, <code>O(1)</code> random access. Syntax: <code>[|1; 2; 3|]</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>option</code> type?",
  "<code>type 'a option = None | Some of 'a</code>. Replaces null. The compiler forces handling both cases via pattern matching. No <code>NullPointerException</code> equivalent.",
  ["L0_primitives"])

c("Fundamentals", "What is the <code>unit</code> type?",
  "The type with exactly one value: <code>()</code>. Used for functions that return nothing useful (side-effects). Similar to <code>void</code> in C but is an actual value.",
  ["L0_primitives"])

c("Fundamentals", "What is a phantom type?",
  "A type parameter that appears in the type definition but not in the data constructors. <code>type 'a dollars = float</code>. Used to add compile-time units of measure without runtime overhead (e.g., distinguish USD from EUR).",
  ["L3_design"])

# === OCAML CORE OPERATIONS ===

c("CoreOps", "How do you define a let binding?",
  "<code>let x = 42</code> — immutable. <code>let x = 42 in expr</code> — local binding. <code>let f x = x + 1</code> — function definition. In top-level (.ml file): <code>let x = 42</code>. In expressions: <code>let x = 42 in x + 1</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a recursive function?",
  "<code>let rec factorial n = if n = 0 then 1 else n * factorial (n - 1)</code>. <code>let rec</code> is required for recursion. For mutually recursive: <code>let rec f x = ... and g x = ...</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you write an anonymous function (lambda)?",
  "<code>fun x -&gt; x * 2</code> — single argument. <code>fun x y -&gt; x + y</code> — multiple arguments (curried). Shorthand with <code>function</code>: <code>function | 0 -&gt; 0 | n -&gt; n</code> (direct pattern matching).",
  ["L1_mechanics"])

c("CoreOps", "How do you define a variant type?",
  "<code>type color = Red | Green | Blue | RGB of int * int * int</code>. Construct: <code>RGB (255, 0, 0)</code>. Pattern match: <code>match c with Red -&gt; ... | RGB (r, g, b) -&gt; ...</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a record type?",
  "<code>type person = { name: string; mutable age: int }</code>. Create: <code>let p = { name = \"Alice\"; age = 30 }</code>. Update: <code>{ p with age = p.age + 1 }</code>. Mutable fields: <code>p.age &lt;- 31</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you work with lists?",
  "Construct: <code>[1; 2; 3]</code> or <code>1 :: [2; 3]</code>. Pattern: <code>match list with [] -&gt; 0 | hd :: tl -&gt; hd + sum tl</code>. Functions: <code>List.map</code>, <code>List.filter</code>, <code>List.fold_left</code>, <code>List.length</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you use the pipe operator?",
  "<code>|&gt;</code> — reversed application: <code>data |&gt; List.map f |&gt; List.filter pred</code>. Equivalent to <code>List.filter pred (List.map f data)</code>. Read left-to-right data flow.",
  ["L1_mechanics"])

c("CoreOps", "How do you handle options?",
  "<code>match opt with Some v -&gt; v | None -&gt; default</code>. Or: <code>Option.value opt ~default</code>, <code>Option.map</code>, <code>Option.bind</code>, <code>Option.get</code> (partial function, can raise).",
  ["L1_mechanics"])

c("CoreOps", "How do you raise and catch exceptions?",
  "<code>raise (Failure \"message\")</code>. Catch: <code>try expr with Failure msg -&gt; ... | Not_found -&gt; ... | exn -&gt; ...</code>. For functional error handling, prefer <code>result</code> type over exceptions.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a module?",
  "File-based: <code>my_module.ml</code> becomes <code>My_module</code> module automatically. Or inline: <code>module M = struct let x = 1 end</code>. Access: <code>M.x</code>. Module signature: <code>module type S = sig val x: int end</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you compile and run an OCaml program?",
  "<code>ocamlc file.ml -o program</code> (bytecode) or <code>ocamlopt file.ml -o program</code> (native). REPL: <code>ocaml</code> or <code>utop</code>. Build tool: <code>dune build</code>, <code>dune exec ./main.exe</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you use Dune (the build system)?",
  "Create <code>dune-project</code> and <code>dune</code> file: <code>(executable (name main))</code>. Build: <code>dune build</code>. Run: <code>dune exec ./main.exe</code>. Test: <code>dune runtest</code>. Install: <code>opam install dune</code>.",
  ["L1_mechanics"])

# === TYPE SYSTEM ===

c("Types", "What is parametric polymorphism in OCaml?",
  "Functions work for any type: <code>let id x = x</code> inferred as <code>'a -&gt; 'a</code>. <code>'a</code> is a type variable (read as 'alpha'). Similar to generics in other languages but inferred automatically.",
  ["L1_mechanics"])

c("Types", "What is type inference in OCaml?",
  "The compiler deduces types without annotations. <code>let add x y = x + y</code> infers <code>int -&gt; int -&gt; int</code> (because <code>+</code> works on <code>int</code>). For floats: <code>let add x y = x +. y</code> = <code>float -&gt; float -&gt; float</code>.",
  ["L1_mechanics"])

c("Types", "What is the difference between <code>val</code> and <code>let</code>?",
  "<code>val</code>: declaration in a signature (<code>.mli</code> file). <code>let</code>: definition in an implementation (<code>.ml</code> file). <code>val square: int -&gt; int</code> in .mli declares what exists; <code>let square x = x * x</code> in .ml defines it.",
  ["L1_mechanics"])

c("Types", "What is row polymorphism?",
  "The type of objects and polymorphic variants. <code>&lt; x: int; .. &gt;</code> means 'an object with at least <code>x: int</code>'. The <code>..</code> indicates the row can have additional fields. Enables structural subtyping.",
  ["L3_design"])

# === PATTERNS ===

c("Patterns", "What is the Map-Reduce pattern in OCaml?",
  "<code>list |&gt; List.map transform |&gt; List.filter pred |&gt; List.fold_left combine init</code>. The standard data pipeline: transform each element, keep some, combine into a result. Pure and composable.",
  ["L2_composition"])

c("Patterns", "What is the 'Parse, Don't Validate' pattern?",
  "Convert raw data to typed representations at the boundary: <code>type email = Email of string</code>. Parse <code>string -&gt; email option</code> once, then pass the typed <code>Email</code> throughout. No repeated validation in business logic.",
  ["L3_design"])

c("Patterns", "What is the Result-based error handling pattern?",
  "Define <code>type ('a, 'e) result = Ok of 'a | Error of 'e</code>. Chain with <code>Result.bind</code>: <code>fetch_user id |&gt; Result.bind validate |&gt; Result.bind save</code>. Short-circuits on first error. More explicit than exceptions.",
  ["L2_composition"])

c("Patterns", "What is the monadic let-binding pattern?",
  "Use <code>let*</code> <code>let+</code> bindings (since OCaml 4.08+): <code>let* user = fetch id in let* valid = validate user in Ok valid</code>. Desugars to <code>Result.bind</code>. Makes monadic code read like sequential code.",
  ["L2_composition"])

c("Patterns", "What is the interpreter pattern using GADTs?",
  "Define a typed AST: <code>type _ expr = Int: int -&gt; int expr | Add: int expr * int expr -&gt; int expr | Eq: 'a expr * 'a expr -&gt; bool expr</code>. Write an <code>eval: 'a expr -&gt; 'a</code> that's type-safe: <code>eval (Eq (Int 1, Int 2))</code> returns <code>bool</code>.",
  ["L3_design"])

# === GOTCHAS ===

c("Gotchas", "Why does <code>1 + 1.0</code> fail in OCaml?",
  "OCaml does NOT do implicit numeric conversion. <code>+</code> is for ints, <code>+.</code> for floats. Use <code>float_of_int 1 +. 1.0</code> or <code>1 + int_of_float 1.0</code>. This is intentional type safety.",
  ["L4_diagnosis"])

c("Gotchas", "What is the value restriction?",
  "A type system limitation: <code>let id = fun x -&gt; x</code> is polymorphic, but <code>let f = ref []</code> can't be polymorphic. The compiler infers a monomorphic type. Fix: eta-expand <code>let f () = ref []</code> or add type annotation.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my <code>match</code> with <code>Exception</code> get a warning?",
  "OCaml 4.02+ distinguishes exceptions from constructors. You must qualify: <code>match ... with exception Not_found -&gt; ...</code> or use <code>try ... with</code> for exception handling.",
  ["L4_diagnosis"])

c("Gotchas", "What is the semicolon <code>;</code> vs <code>;;</code> difference?",
  "<code>;</code>: expression separator in sequences (<code>expr1; expr2</code>). <code>expr1</code> must return unit (typically). <code>;;</code>: top-level terminator in the REPL (not needed in source files). Source files use <code>;;</code> only to separate top-level items.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>print_string</code> not flush immediately?",
  "OCaml output is buffered. Use <code>print_endline</code> (adds newline + flush) or <code>flush stdout</code> after <code>print_string</code>. In REPL, output may not appear until newline or explicit flush.",
  ["L4_diagnosis"])

c("Gotchas", "What is the difference between <code>==</code> and <code>=</code>?",
  "<code>=</code>: structural equality (compare contents). <code>==</code>: physical equality (same memory address). Use <code>=</code> for values, <code>==</code> rarely (e.g., comparing object references). <code>!=</code> is physical inequality, <code>&lt;&gt;</code> is structural.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "What is OPAM?",
  "OCaml Package Manager — manages OCaml compiler versions and packages. <code>opam switch create 5.1.0</code> creates a compiler environment. <code>opam install dune core utop</code> installs packages. Manages compiler toolchain and libraries.",
  ["L1_mechanics"])

c("Expert", "What is Jane Street's Core / Base library?",
  "An alternative standard library (Core, Core_kernel, Base) replacing OCaml's stdlib. Provides consistent APIs, better data structures, monadic interfaces, and time/date handling. Used in production at Jane Street for financial systems.",
  ["L5_opinion"])

c("Expert", "What is the OCaml Multicore runtime?",
  "OCaml 5.0+ adds native support for shared-memory parallelism via Domains (OS threads with OCaml's memory model) and Algebraic Effects for direct-style concurrency. Domains share memory; effects handle async I/O. Two complementary parallelism models.",
  ["L6_innovation"])

c("Expert", "What are Algebraic Effects in OCaml 5?",
  "A concurrency primitive that generalizes exceptions with resumable continuations. <code>effect Yield: unit</code> — suspend a computation and resume later. Enables direct-style async code (no monads/callbacks). Basis for libraries like Eio and Miou.",
  ["L6_innovation"])

c("Expert", "What is the ppx (preprocessor extension) system?",
  "OCaml's syntax extension mechanism: PPX transforms parse tree at compile time. Written in OCaml. Libraries: <code>ppx_deriving</code> (auto-derive serialization/comparison), <code>ppx_expect</code> (inline tests), <code>ppx_sexp_conv</code> (s-expression conversion).",
  ["L6_innovation"])

c("Expert", "When should you choose OCaml over Rust or Haskell?",
  "OCaml: rapid prototyping with strong types, compilers/analysis tools, financial systems, when you need both performance and fast compilation. Rust: systems programming with memory safety. Haskell: pure functional programming. OCaml strikes a pragmatic balance.",
  ["L5_opinion"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
