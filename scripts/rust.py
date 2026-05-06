import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Rust"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "Ownership":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Ownership"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Core-Operations"),
    "Types":        genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Type-System"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === RUST FUNDAMENTALS ===

c("Fundamentals", "What is Rust?",
  "A systems programming language focused on safety, speed, and concurrency. Guarantees memory safety without a garbage collector via ownership, borrowing, and lifetimes. Empowers fearless concurrency.",
  ["L0_primitives"])

c("Fundamentals", "What is ownership in Rust?",
  "Every value has exactly one owner at a time. When the owner goes out of scope, the value is dropped (freed). Ownership can be moved (transferred) or borrowed (temporarily accessed via references). No double-free, no use-after-free.",
  ["L0_primitives"])

c("Fundamentals", "What is borrowing in Rust?",
  "Accessing a value without taking ownership. <code>&amp;T</code> — immutable reference (shared, <code>n</code> allowed). <code>&amp;mut T</code> — mutable reference (exclusive, only one at a time). The borrow checker enforces these rules at compile time.",
  ["L0_primitives"])

c("Fundamentals", "What are lifetimes in Rust?",
  "Annotations <code>'a</code> that tell the compiler how long references are valid. <code>fn longest&lt;'a&gt;(x: &amp;'a str, y: &amp;'a str) -&gt; &amp;'a str</code>. Most lifetimes are elided (inferred). Only annotate when the compiler can't figure it out.",
  ["L0_primitives"])

c("Fundamentals", "What is a <code>String</code> vs <code>&amp;str</code>?",
  "<code>String</code>: owned, heap-allocated, growable UTF-8 string. <code>&amp;str</code>: borrowed string slice, reference to UTF-8 data (stack string literal or slice of String). <code>\"hello\"</code> is <code>&amp;str</code>. <code>String::from(\"hello\")</code> is <code>String</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is a <code>Vec&lt;T&gt;</code> in Rust?",
  "A growable array (heap-allocated). <code>let mut v = vec![1, 2, 3];</code>. <code>v.push(4)</code>, <code>v.pop()</code>, <code>v.len()</code>. Indexing: <code>&amp;v[0]</code> (panics if OOB) or <code>v.get(0)</code> (returns <code>Option</code>). Owned — freed when it goes out of scope.",
  ["L0_primitives"])

c("Fundamentals", "What is an <code>Option&lt;T&gt;</code> in Rust?",
  "<code>enum Option&lt;T&gt; { Some(T), None }</code>. Replaces null. The compiler forces handling both cases. <code>match opt { Some(v) =&gt; ..., None =&gt; ... }</code>. <code>opt.unwrap()</code> (panics on None), <code>opt.unwrap_or(default)</code> (safe).",
  ["L0_primitives"])

c("Fundamentals", "What is a <code>Result&lt;T, E&gt;</code> in Rust?",
  "<code>enum Result&lt;T, E&gt; { Ok(T), Err(E) }</code>. The standard error handling type. <code>match result { Ok(v) =&gt; ..., Err(e) =&gt; ... }</code>. <code>?</code> operator propagates errors: <code>let x = fallible()?;</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is a trait in Rust?",
  "A collection of methods that types can implement. Like interfaces in other languages. <code>trait Display { fn fmt(&amp;self, f: &amp;mut Formatter) -&gt; fmt::Result; }</code>. Implement: <code>impl Display for MyType { ... }</code>. Use generics: <code>fn show&lt;T: Display&gt;(x: T)</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is <code>cargo</code>?",
  "Rust's build system and package manager. <code>cargo new project</code>, <code>cargo build</code>, <code>cargo run</code>, <code>cargo test</code>, <code>cargo clippy</code>, <code>cargo fmt</code>. Manages dependencies in <code>Cargo.toml</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is <code>unsafe</code> in Rust?",
  "A block/function that allows raw pointer dereferencing, calling unsafe functions, accessing mutable statics, implementing unsafe traits, and accessing union fields. 'I promise to uphold the safety invariants manually.' Used for FFI and performance.",
  ["L0_primitives"])

c("Fundamentals", "What is pattern matching in Rust?",
  "<code>match</code> is exhaustive: <code>match value { Pattern =&gt; expr, ... }</code>. Destructure enums, tuples, structs, ranges, and literals. <code>if let</code> for single case: <code>if let Some(v) = opt { ... }</code>. <code>while let</code> for looping matches.",
  ["L0_primitives"])

# === OWNERSHIP DEEP DIVE ===

c("Ownership", "What is a move in Rust?",
  "When ownership transfers: <code>let s2 = s1;</code> — <code>s1</code> is no longer valid (can't use it). For <code>Copy</code> types (<code>i32</code>, <code>bool</code>, <code>&amp;T</code>), assignment copies instead of moves. For non-Copy types (<code>String</code>, <code>Vec</code>), assignment is a move.",
  ["L1_mechanics"])

c("Ownership", "What is a clone?",
  "Explicit deep copy: <code>let s2 = s1.clone();</code>. <code>Clone</code> trait. Both <code>s1</code> and <code>s2</code> are valid, independent. More expensive than move (heap allocation). Use when you need two independent copies.",
  ["L1_mechanics"])

c("Ownership", "What is the borrow checker rule: 'shared XOR mutable'?",
  "At any given time, you can have either ONE mutable reference OR any number of immutable references. Cannot have both simultaneously. This prevents data races at compile time. References must always be valid (lifetime enforcement).",
  ["L1_mechanics"])

c("Ownership", "What is <code>Rc&lt;T&gt;</code> and when to use it?",
  "Reference-counted shared ownership for single-threaded scenarios. <code>Rc::new(val)</code>. Clone creates new pointer, increments count. <code>Rc::clone(&amp;rc)</code>. Use when multiple parts of code need to share ownership (tree structures, graphs). <code>Weak</code> for non-owning cycles.",
  ["L3_design"])

c("Ownership", "What is <code>Arc&lt;T&gt;</code> and how is it different from <code>Rc&lt;T&gt;</code>?",
  "<code>Arc</code> = Atomic Reference Counted. Thread-safe version of <code>Rc</code> (atomic operations instead of non-atomic). Use <code>Arc</code> for multi-threaded shared ownership. More overhead than <code>Rc</code>. <code>Mutex&lt;T&gt;</code> or <code>RwLock&lt;T&gt;</code> wrap <code>Arc</code> for mutable access.",
  ["L3_design"])

c("Ownership", "What do <code>Cell&lt;T&gt;</code> and <code>RefCell&lt;T&gt;</code> do?",
  "Interior mutability: mutate data through a shared (<code>&amp;T</code>) reference. <code>Cell</code>: <code>Copy</code> types only, <code>.set()</code>/<code>.get()</code>. <code>RefCell</code>: any type, runtime borrow checking (<code>.borrow()</code>/<code>.borrow_mut()</code>). <code>RefCell</code> panics if borrow rules violated at runtime instead of compile time.",
  ["L3_design"])

# === RUST CORE OPERATIONS ===

c("CoreOps", "How do you declare a variable?",
  "<code>let x = 42;</code> — immutable. <code>let mut x = 42;</code> — mutable. <code>let x: i32 = 42;</code> — with type annotation. <code>const MAX: u32 = 100_000;</code> — compile-time constant (always immutable, must have type).",
  ["L1_mechanics"])

c("CoreOps", "How do you define a function?",
  "<code>fn add(x: i32, y: i32) -&gt; i32 { x + y }</code> — last expression is return value (no semicolon). <code>return x + y;</code> for early returns. <code>fn main() { ... }</code> is the entry point.",
  ["L1_mechanics"])

c("CoreOps", "How do you use <code>if</code> as an expression?",
  "<code>let num = if condition { 5 } else { 6 };</code> — both branches must return the same type. <code>if condition { ... } else if other { ... } else { ... }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you write loops?",
  "<code>loop { ... break; }</code> — infinite, break to exit. <code>while condition { ... }</code>. <code>for item in iterable { ... }</code> — <code>for i in 0..5 { ... }</code>. Loops can return values: <code>let x = loop { break 42; };</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a struct?",
  "<code>struct User { name: String, age: u32, active: bool }</code>. Create: <code>let u = User { name: String::from(\"Alice\"), age: 30, active: true };</code>. Update syntax: <code>User { age: 31, ..user }</code> (moves non-Copy fields).",
  ["L1_mechanics"])

c("CoreOps", "How do you define an enum?",
  "<code>enum Message { Quit, Move { x: i32, y: i32 }, Write(String), ChangeColor(i32, i32, i32) }</code>. Each variant can hold data. <code>match msg { Message::Quit =&gt; ..., Message::Write(s) =&gt; ..., _ =&gt; {} }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you implement methods on a type?",
  "<code>impl User { fn new(name: String) -&gt; Self { User { name, age: 0, active: true } } fn greet(&amp;self) { ... } }</code>. <code>&amp;self</code>: borrow. <code>&amp;mut self</code>: mutable borrow. <code>self</code>: take ownership. Associated functions (no self) are <code>User::new(...)</code>.",
  ["L1_mechanics"])

c("CoreOps", "What is the <code>?</code> operator?",
  "Propagates errors: <code>let x = fallible()?;</code>. If <code>Ok(v)</code>, unwraps to <code>v</code>. If <code>Err(e)</code>, returns <code>Err(e.into())</code> from the enclosing function. Function must return <code>Result</code> or <code>Option</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you use iterators?",
  "<code>vec.iter().map(|x| x * 2).filter(|x| x &gt; 5).collect()</code>. Lazy — no work done until consumed. <code>.iter()</code>: borrows. <code>.into_iter()</code>: consumes, moves ownership. <code>.iter_mut()</code>: mutable borrows. <code>.collect::&lt;Vec&lt;_&gt;&gt;()</code> gathers results.",
  ["L1_mechanics"])

c("CoreOps", "How do closures work in Rust?",
  "<code>|x| x + 1</code> — simple. <code>|x: i32| -&gt; i32 { x + 1 }</code> — annotated. Closures capture variables by reference by default. <code>move || ...</code> forces move capture. Implement <code>Fn</code>, <code>FnMut</code>, or <code>FnOnce</code> traits automatically.",
  ["L1_mechanics"])

c("CoreOps", "How do you use generics?",
  "<code>fn largest&lt;T: PartialOrd&gt;(list: &amp;[T]) -&gt; &amp;T { ... }</code>. <code>struct Point&lt;T&gt; { x: T, y: T }</code>. Monomorphized at compile time — zero runtime overhead. <code>where</code> clause for complex bounds: <code>fn foo&lt;T&gt;(x: T) where T: Display + Clone { ... }</code>.",
  ["L1_mechanics"])

c("CoreOps", "What is <code>derive</code> in Rust?",
  "Auto-implement common traits: <code>#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, PartialOrd, Ord)]</code>. <code>Debug</code>: <code>{:?}</code> printing. <code>Clone/Copy</code>: duplication semantics. <code>PartialEq/Eq</code>: equality. Works on structs and enums with compatible fields.",
  ["L1_mechanics"])

# === TYPE SYSTEM ===

c("Types", "What is a slice in Rust?",
  "<code>&amp;[T]</code> — a reference to a contiguous sequence of elements in memory. <code>&amp;vec[0..2]</code> — borrow a portion of a Vec. <code>&amp;str</code> is a slice of <code>str</code>. Slices are fat pointers (pointer + length).",
  ["L1_mechanics"])

c("Types", "What is a tuple struct?",
  "Named struct without named fields: <code>struct Color(i32, i32, i32);</code>. Create: <code>let black = Color(0, 0, 0);</code>. Access: <code>black.0</code>, <code>black.1</code>. Destructure: <code>let Color(r, g, b) = black;</code>.",
  ["L1_mechanics"])

c("Types", "What is a unit-like struct?",
  "A struct with no fields: <code>struct AlwaysEqual;</code>. Useful as a marker type or to implement a trait without storing data. Like <code>struct Unit</code> — zero size at runtime.",
  ["L1_mechanics"])

c("Types", "What are <code>dyn Trait</code> (trait objects)?",
  "Dynamic dispatch: <code>let shapes: Vec&lt;Box&lt;dyn Draw&gt;&gt;</code>. Uses a vtable — each method call goes through a pointer lookup. Slightly slower than static dispatch. Use when you need heterogeneous collections of types implementing the same trait.",
  ["L3_design"])

c("Types", "What is <code>impl Trait</code>?",
  "Opaque return type or argument shorthand: <code>fn returns_closure() -&gt; impl Fn(i32) -&gt; i32 { |x| x + 1 }</code>. The caller knows it implements the trait but not the concrete type. Syntactic sugar that uses generics under the hood (static dispatch).",
  ["L3_design"])

# === PATTERNS ===

c("Patterns", "What is the newtype pattern?",
  "<code>struct Meters(f64);</code>. Wraps a primitive in a new type for type safety: can't mix Meters with Kilometers. Zero runtime overhead. Implement traits on the wrapper for domain-specific behavior.",
  ["L2_composition"])

c("Patterns", "What is the builder pattern in Rust?",
  "<code>User::builder().name(\"Alice\").age(30).build()?;</code>. Uses <code>&amp;mut self</code> methods returning <code>Self</code>. <code>build()</code> validates and returns <code>Result&lt;User, Error&gt;</code>. Handles complex construction logic cleanly.",
  ["L2_composition"])

c("Patterns", "What is the <code>From</code>/<code>Into</code> conversion pattern?",
  "<code>impl From&lt;i32&gt; for MyType { ... }</code>. Then <code>MyType::from(42)</code> or <code>let x: MyType = 42.into();</code>. <code>?</code> uses <code>From</code> for error conversion. Makes APIs ergonomic and consistent.",
  ["L2_composition"])

c("Patterns", "What is the RAII guard pattern?",
  "Use <code>Drop</code> to clean up resources: <code>impl Drop for Connection { fn drop(&amp;mut self) { self.close(); } }</code>. Mutex lock: <code>let guard = mutex.lock().unwrap();</code> — auto-unlocked when guard drops. File, socket, DB connection all use this.",
  ["L2_composition"])

c("Patterns", "What is the typestate pattern?",
  "Encode state in the type system: <code>struct Open(Connection); struct Closed(Connection); struct Authenticated(Connection);</code>. Transitions: <code>fn authenticate(conn: Open) -&gt; Authenticated</code>. Compile-time guarantee of correct state transitions.",
  ["L3_design"])

c("Patterns", "What is the extension trait pattern?",
  "<code>trait StrExt { fn is_awesome(&amp;self) -&gt; bool; } impl StrExt for str { ... }</code>. Add methods to types you don't own. Import the trait to get the methods. Used extensively in <code>itertools</code>, <code>rayon</code>, <code>anyhow</code>.",
  ["L2_composition"])

# === GOTCHAS ===

c("Gotchas", "Why do I get 'cannot move out of borrowed content'?",
  "Trying to take ownership through a reference. <code>&amp;v[0]</code> borrows; <code>v[0]</code> tries to move (if non-Copy). Use <code>.clone()</code> or restructure to not need ownership. Or use methods that return references: <code>.get(0)</code>.",
  ["L4_diagnosis"])

c("Gotchas", "What is the 'borrowed value does not live long enough' error?",
  "A reference outlives the data it points to. <code>let r; { let x = 5; r = &amp;x; } println!(\"{}\", r);</code> — <code>x</code> goes out of scope but <code>r</code> still references it. Restructure scope or use owned values.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>println!(\"{}\", vec)</code> not work?",
  "<code>println!</code> needs <code>Display</code> trait, Vec doesn't implement it. Use <code>{:?}</code> for <code>Debug</code>: <code>println!(\"{:?}\", vec)</code>. Derive <code>Debug</code> on custom types. Or implement <code>Display</code> for readable output.",
  ["L4_diagnosis"])

c("Gotchas", "Why can't I call a method that takes <code>&amp;mut self</code> when I have <code>&amp;self</code>?",
  "Immutable borrow (<code>&amp;self</code>), mutable borrow (<code>&amp;mut self</code>). You can't call <code>&amp;mut self</code> methods through an immutable reference. Either make the reference mutable, or the method immutable.",
  ["L4_diagnosis"])

c("Gotchas", "What happens with <code>unwrap()</code> on <code>None</code>?",
  "Panics! Thread will unwind. Use <code>unwrap_or(default)</code>, <code>unwrap_or_else(|| compute_default())</code>, or pattern matching. In production, handle errors — <code>unwrap</code> is for prototyping/places where it's logically impossible to fail.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>match</code> need to be exhaustive?",
  "The compiler enforces that every possible enum variant is handled. This prevents bugs from forgetting to handle a state. Use <code>_ =&gt; {}</code> as a catch-all if you genuinely don't care about remaining variants.",
  ["L4_diagnosis"])

c("Gotchas", "What is the 'move occurs because value has type X which does not implement Copy'?",
  "Non-Copy types are moved on assignment/function call. After <code>let y = x;</code>, <code>x</code> is invalid. Clone if you need both copies, or restructure to not need multiple ownership. This is the borrow checker ensuring no double-free.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "What is async/await in Rust?",
  "<code>async fn fetch() -&gt; Result&lt;Data, Error&gt; { ... }</code>. Returns a <code>Future</code>. <code>let data = fetch().await?;</code>. Needs a runtime: <code>tokio</code> (most common), <code>async-std</code>, <code>smol</code>. <code>#[tokio::main]</code> starts the runtime.",
  ["L3_design"])

c("Expert", "What is <code>Send</code> and <code>Sync</code>?",
  "<code>Send</code>: type can be transferred across thread boundaries (ownership). <code>Sync</code>: type can be shared across threads (<code>&amp;T</code> is safe). Most types are <code>Send + Sync</code>. <code>Rc</code> is neither. <code>Arc</code> is <code>Send + Sync</code> if <code>T</code> is.",
  ["L3_design"])

c("Expert", "What is a proc macro?",
  "Code that transforms other code at compile time. Three kinds: derive macros (<code>#[derive(Debug)]</code>), attribute macros (<code>#[tokio::main]</code>), function-like macros (<code>sqlx::query!()</code>). Operates on token streams, outputs new token streams.",
  ["L6_innovation"])

c("Expert", "What is <code>Pin</code> and why does async need it?",
  "Futures are self-referential (the state machine references itself). <code>Pin</code> guarantees the memory won't be moved. Without <code>Pin</code>, moving a future would invalidate its internal pointers. <code>Box::pin(future)</code> or <code>pin!</code> macro.",
  ["L3_design"])

c("Expert", "What is WASM and how does Rust target it?",
  "Compile Rust to WebAssembly: <code>wasm-pack build</code>. Target the browser or WASI (server-side). <code>wasm-bindgen</code> generates JS bindings. Use libraries like <code>yew</code>, <code>leptos</code>, <code>sycamore</code> for Rust frontend frameworks.",
  ["L6_innovation"])

c("Expert", "What is <code>unsafe</code> really needed for?",
  "1. Raw pointer dereferencing. 2. Calling <code>unsafe</code> functions (FFI). 3. Implementing <code>unsafe</code> traits (<code>Send</code>, <code>Sync</code>). 4. Accessing mutable statics. 5. Accessing union fields. Build safe abstractions around unsafe — the caller shouldn't need <code>unsafe</code>.",
  ["L3_design"])

c("Expert", "How does Rust compare to C++ for new projects?",
  "Rust: memory safety guarantees, no header files, cargo instead of CMake, algebraic types, pattern matching, modern tooling. C++: larger ecosystem, more libraries, templates/constexpr, existing codebases. Choose Rust for new systems projects; C++ for legacy/integration.",
  ["L5_opinion"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
