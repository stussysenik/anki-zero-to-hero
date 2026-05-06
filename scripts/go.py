import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Go"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Concurrency":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Concurrency"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === GO FUNDAMENTALS ===

c("Fundamentals", "What is Go?",
  "An open-source, statically typed, compiled language designed by Google. Emphasizes simplicity, fast compilation, built-in concurrency (goroutines/channels), garbage collection, and structural typing (interfaces). Often called 'the language of the cloud'.",
  ["L0_primitives"])

c("Fundamentals", "What is a goroutine?",
  "A lightweight thread managed by the Go runtime. <code>go func() { ... }()</code> launches a goroutine. Multiplexed onto OS threads — you can have millions of goroutines. Communicated via channels. Much cheaper than OS threads.",
  ["L0_primitives"])

c("Fundamentals", "What is a channel in Go?",
  "A typed conduit for communication between goroutines. <code>ch := make(chan int)</code>. Send: <code>ch &lt;- 42</code>. Receive: <code>v := &lt;-ch</code>. Buffered: <code>make(chan int, 10)</code>. 'Don't communicate by sharing memory; share memory by communicating.'",
  ["L0_primitives"])

c("Fundamentals", "What is an interface in Go?",
  "A set of method signatures. Any type that implements all methods implicitly satisfies the interface (structural typing — no <code>implements</code> keyword). <code>type Reader interface { Read(p []byte) (n int, err error) }</code>. Core to Go's abstraction model.",
  ["L0_primitives"])

c("Fundamentals", "What is a struct in Go?",
  "A typed collection of fields. <code>type User struct { Name string; Age int }</code>. Methods are defined outside the struct: <code>func (u User) Greet() string { ... }</code>. No inheritance — composition via embedding. Value types by default.",
  ["L0_primitives"])

c("Fundamentals", "What is a pointer in Go?",
  "<code>*T</code> — a reference to a value of type T. <code>&amp;x</code> gets a pointer. <code>*p</code> dereferences. Used for: mutating function arguments, sharing large structs, nil semantics. No pointer arithmetic. Go has garbage collection — pointers don't need manual freeing.",
  ["L0_primitives"])

c("Fundamentals", "What is <code>defer</code> in Go?",
  "Schedules a function call to run when the surrounding function returns. <code>defer file.Close()</code>. Multiple defers execute in LIFO order. Arguments are evaluated immediately, but the call is deferred. Used for cleanup, unlocking mutexes, closing resources.",
  ["L0_primitives"])

c("Fundamentals", "What is a <code>slice</code> in Go?",
  "A dynamic, flexible view into an array. <code>[]int{1, 2, 3}</code>. Actually a struct: pointer to array + length + capacity. <code>make([]int, length, capacity)</code>. <code>append(slice, element)</code> adds elements (may reallocate). Slices share underlying arrays — mutations through one affect others.",
  ["L0_primitives"])

c("Fundamentals", "What is a <code>map</code> in Go?",
  "An unordered key-value store: <code>map[string]int</code>. <code>m := make(map[string]int)</code>. <code>m[\"a\"] = 1</code>. <code>v, ok := m[\"a\"]</code> — <code>ok</code> is false if key not present. Maps are reference types (nil map reads return zero value, but writes to nil map panic).",
  ["L0_primitives"])

c("Fundamentals", "What is Go modules?",
  "Dependency management: <code>go mod init module-name</code>. <code>go.mod</code> tracks dependencies and versions. <code>go.sum</code> contains checksums. <code>go get pkg@version</code> adds a dependency. <code>go mod tidy</code> removes unused deps. Replaces GOPATH-based workflows.",
  ["L0_primitives"])

c("Fundamentals", "What does <code>_</code> (blank identifier) do in Go?",
  "Discards a value: <code>v, _ := someFunc()</code>. Used when a function returns a value but you only need some of them. Also used for import side effects: <code>import _ \"net/http/pprof\"</code>. Prevents 'declared but not used' errors.",
  ["L0_primitives"])

c("Fundamentals", "What is the empty interface <code>interface{}</code>?",
  "Satisfied by any type — the Go equivalent of <code>any</code>. <code>var x interface{} = 42</code>. Use type assertion: <code>x.(int)</code> or type switch: <code>switch v := x.(type) { case int: ... }</code>. Since Go 1.18, <code>any</code> is an alias for <code>interface{}</code>.",
  ["L0_primitives"])

# === GO CORE OPERATIONS ===

c("CoreOps", "How do you declare a variable?",
  "<code>var x int = 42</code> — explicit type. <code>var x = 42</code> — type inferred. <code>x := 42</code> — short declaration (inside functions only). <code>var x int</code> — zero value (0 for int, \"\" for string, nil for pointers/slices/maps).",
  ["L1_mechanics"])

c("CoreOps", "How do you define a function?",
  "<code>func add(a, b int) int { return a + b }</code>. Multiple returns: <code>func div(a, b int) (int, error) { ... }</code>. Named returns: <code>func split(sum int) (x, y int) { x = sum * 4/9; y = sum - x; return }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you define a method?",
  "<code>func (u User) Greet() string { return \"Hello, \" + u.Name }</code>. Value receiver (<code>u User</code>): operates on a copy. Pointer receiver (<code>u *User</code>): can modify the original. Use pointer receiver for mutation or to avoid copying large structs.",
  ["L1_mechanics"])

c("CoreOps", "How do you handle errors in Go?",
  "Return <code>error</code> as the last return value: <code>f, err := os.Open(\"file\"); if err != nil { return err }</code>. No exceptions — explicit error checking. <code>errors.New(\"message\")</code> creates errors. <code>fmt.Errorf(\"context: %w\", err)</code> wraps with <code>%w</code> for <code>errors.Is</code> and <code>errors.As</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you write a for loop?",
  "Go has only <code>for</code> (no while). <code>for i := 0; i &lt; 10; i++ { ... }</code>. <code>for condition { ... }</code> (while-style). <code>for { ... }</code> (infinite). <code>for index, value := range slice { ... }</code>. <code>for key, value := range map { ... }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you write if/else?",
  "<code>if x &gt; 0 { ... } else if x &lt; 0 { ... } else { ... }</code>. <code>if v, err := someFunc(); err != nil { return err } else { use(v) }</code> — short statement before condition.",
  ["L1_mechanics"])

c("CoreOps", "How do you use switch?",
  "<code>switch x { case 1: ... case 2, 3: ... default: ... }</code>. No fallthrough by default (C gotcha avoided). Switch without expression: <code>switch { case x &gt; 0: ..., case x &lt; 0: ... }</code> — replaces if-else chains. Type switch: <code>switch v := x.(type) { case int: ... }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you create slices and maps?",
  "Slice: <code>s := make([]int, 5, 10)</code> (len 5, cap 10). <code>s := []int{1, 2, 3}</code> (literal). Map: <code>m := make(map[string]int)</code>. <code>m := map[string]int{\"a\": 1}</code>. Always initialize maps before use — a nil map panics on write.",
  ["L1_mechanics"])

c("CoreOps", "How do you use <code>append</code> and <code>copy</code>?",
  "<code>s = append(s, 4, 5)</code> — appends elements. <code>s = append(s, otherSlice...)</code> — appends a slice (ellipsis). <code>copy(dst, src)</code> — copies elements, returns count. <code>len(s)</code> for length, <code>cap(s)</code> for capacity.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a struct and access fields?",
  "<code>u := User{Name: \"Alice\", Age: 30}</code>. <code>u := User{\"Alice\", 30}</code> (positional, fragile). <code>u.Age = 31</code>. <code>uPtr := &amp;User{...}</code> — pointer to struct (fields accessed with <code>uPtr.Name</code>, auto-dereferenced).",
  ["L1_mechanics"])

c("CoreOps", "How do you embed (composition)?",
  "<code>type Admin struct { User; Permissions []string }</code>. <code>admin.Name</code> — promoted field, no <code>admin.User.Name</code> needed. Methods are also promoted. This is Go's answer to inheritance (it's composition, not inheritance).",
  ["L1_mechanics"])

# === CONCURRENCY ===

c("Concurrency", "How do you launch a goroutine?",
  "<code>go func() { process(data) }()</code> or <code>go process(data)</code>. The goroutine runs concurrently with the caller. Use <code>sync.WaitGroup</code> or channels to wait for completion.",
  ["L1_mechanics"])

c("Concurrency", "What is <code>sync.WaitGroup</code>?",
  "<code>var wg sync.WaitGroup; wg.Add(3); go func() { defer wg.Done(); work() }(); wg.Wait()</code>. Waits for a collection of goroutines to finish. <code>Add</code> before launch, <code>Done</code> on completion, <code>Wait</code> blocks until counter is zero.",
  ["L1_mechanics"])

c("Concurrency", "What is a buffered vs unbuffered channel?",
  "Unbuffered (<code>make(chan int)</code>): send blocks until receive, receive blocks until send — synchronous. Buffered (<code>make(chan int, 10)</code>): send blocks only when buffer is full. Use unbuffered for synchronization, buffered for decoupling.",
  ["L1_mechanics"])

c("Concurrency", "What is <code>select</code> in Go?",
  "Wait on multiple channel operations: <code>select { case msg := &lt;-ch1: ...; case ch2 &lt;- val: ...; case &lt;-time.After(1*time.Second): ...; default: ... }</code>. Blocks until one case is ready. If multiple ready, picks randomly. <code>default</code> makes it non-blocking.",
  ["L1_mechanics"])

c("Concurrency", "What is a <code>sync.Mutex</code>?",
  "<code>var mu sync.Mutex; mu.Lock(); ... shared access ...; mu.Unlock()</code>. <code>defer mu.Unlock()</code> right after <code>Lock()</code>. <code>sync.RWMutex</code>: <code>RLock()/RUnlock()</code> for multiple readers, <code>Lock()/Unlock()</code> for exclusive write.",
  ["L1_mechanics"])

# === PATTERNS ===

c("Patterns", "What is the context propagation pattern?",
  "<code>func(ctx context.Context) error</code>. Pass <code>context.Context</code> as the first parameter. Carries deadlines, cancellation signals, and request-scoped values. <code>ctx, cancel := context.WithTimeout(parent, 5*time.Second); defer cancel()</code>.",
  ["L2_composition"])

c("Patterns", "What is the functional options pattern?",
  "<code>type Option func(*Server); func WithTimeout(d time.Duration) Option { ... }; func NewServer(opts ...Option) *Server { ... }</code>. Replaces constructors with many parameters. Caller: <code>s := NewServer(WithTimeout(5s), WithPort(8080))</code>. Extensible, readable.",
  ["L2_composition"])

c("Patterns", "What is the interface segregation pattern?",
  "Define small, focused interfaces (1-3 methods) where they are USED, not where they're implemented. <code>io.Reader</code>, <code>io.Writer</code>, <code>io.Closer</code>. Accept interfaces, return structs. Enables easy testing with mocks/stubs.",
  ["L2_composition"])

c("Patterns", "What is the worker pool pattern?",
  "Create N goroutines that read from a shared channel, process, and send results: <code>for i := 0; i &lt; numWorkers; i++ { go worker(jobs, results) }</code>. Limits concurrency, balances load. Use <code>errgroup</code> for automatic error propagation and cancellation.",
  ["L2_composition"])

c("Patterns", "What is the pipeline pattern?",
  "Chain goroutines connected by channels: <code>gen → square → print</code>. Each stage reads from input channel, processes, writes to output channel. Data flows through stages concurrently. Close output channel when done to signal downstream stages.",
  ["L2_composition"])

# === GOTCHAS ===

c("Gotchas", "Why does <code>range</code> capture the same variable address?",
  "<code>for _, val := range items { go func() { use(val) }() }</code> — all goroutines see the last <code>val</code>. Fix: <code>val := val</code> (copy), or pass as argument: <code>go func(v int) { use(v) }(val)</code>. <code>range</code> reuses the loop variable.",
  ["L4_diagnosis"])

c("Gotchas", "What happens when you append to a slice and it reallocates?",
  "If <code>append</code> exceeds capacity, a new backing array is created. Other slices sharing the OLD array are unaffected. This can cause subtle bugs: <code>a := b[0:2]; a = append(a, x)</code> may or may not affect <code>b</code>. Always consider capacity.",
  ["L4_diagnosis"])

c("Gotchas", "Why does nil map cause a panic?",
  "<code>var m map[string]int; m[\"a\"] = 1</code> — PANIC: assignment to entry in nil map. Reads are fine (returns zero value). Always <code>make()</code> maps or use a literal. <code>var m map[string]int</code> is nil.",
  ["L4_diagnosis"])

c("Gotchas", "What is the 'declared and not used' error?",
  "Go refuses to compile if a variable or import is declared but not used. This enforces clean code but can be annoying during debugging. Use <code>_ = unusedVar</code> to suppress temporarily. Or use <code>goimports</code> to auto-manage imports.",
  ["L4_diagnosis"])

c("Gotchas", "Why does nil interface not equal nil?",
  "<code>var p *int = nil; var i interface{} = p; i != nil</code> — the interface has type <code>*int</code> but nil value. The interface itself is not nil. Always compare to nil directly, not through an interface variable containing a typed nil.",
  ["L4_diagnosis"])

c("Gotchas", "What causes goroutine leaks?",
  "Goroutines blocked forever on channel operations (send to unbuffered channel with no receiver, receive from channel nobody sends to). Always ensure goroutines have an exit path. Use <code>context</code> for cancellation. Use <code>goleak</code> in tests.",
  ["L4_diagnosis"])

# === EXPERT ===

c("Expert", "What are generics in Go 1.18+?",
  "<code>func Max[T constraints.Ordered](a, b T) T { if a &gt; b { return a }; return b }</code>. Type parameters in brackets. <code>constraints</code> package for common constraints. <code>any</code> for unconstrained. No performance penalty — monomorphized or uses type dictionary.",
  ["L3_design"])

c("Expert", "What is <code>go:embed</code>?",
  "Embeds files into the binary at compile time: <code>//go:embed templates/*.html<br>var templates embed.FS</code>. Access with <code>templates.ReadFile(\"templates/index.html\")</code>. No external files needed in production. Use for templates, static assets, configs.",
  ["L6_innovation"])

c("Expert", "What is the <code>sync/atomic</code> package?",
  "Low-level atomic operations on integers and pointers: <code>atomic.AddInt64(&amp;counter, 1)</code>, <code>atomic.LoadInt64(&amp;counter)</code>, <code>atomic.CompareAndSwapInt64</code>. Lock-free operations. Use for simple counters and flags; prefer <code>sync.Mutex</code> or channels for complex state.",
  ["L3_design"])

c("Expert", "What is profiling in Go?",
  "<code>import _ \"net/http/pprof\"</code> adds <code>/debug/pprof/</code> endpoints. CPU profile: <code>go tool pprof http://localhost:6060/debug/pprof/profile</code>. Memory: <code>/debug/pprof/heap</code>. Goroutine dump: <code>/debug/pprof/goroutine</code>. Use <code>pprof</code> for flame graphs and optimization.",
  ["L6_innovation"])

c("Expert", "When should you use Go over Rust or Zig?",
  "Go: network services, CLI tools, cloud infrastructure, when development speed and simplicity matter more than raw performance. Rust: when memory safety without GC is critical, or need zero-cost abstractions. Zig: when you need C interop without bindings and explicit control. Go's strength is its simplicity and concurrency model.",
  ["L5_opinion"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
