import genanki, random
R = lambda: random.randrange(1 << 30, 1 << 31)
model = genanki.Model(R(), "Swift/Apple Q&A",
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
    "SwiftCore": genanki.Deck(R(), "Swift_Apple::Zero2Hero::01-Swift-Core"),
    "Protocols": genanki.Deck(R(), "Swift_Apple::Zero2Hero::02-Protocols-Generics"),
    "Concurrency": genanki.Deck(R(), "Swift_Apple::Zero2Hero::03-Concurrency"),
    "SwiftUIID": genanki.Deck(R(), "Swift_Apple::Zero2Hero::04-SwiftUI-Identity"),
    "Layout": genanki.Deck(R(), "Swift_Apple::Zero2Hero::05-SwiftUI-Layout"),
    "Animation": genanki.Deck(R(), "Swift_Apple::Zero2Hero::06-SwiftUI-Animation"),
    "Combine": genanki.Deck(R(), "Swift_Apple::Zero2Hero::07-Combine"),
    "SwiftData": genanki.Deck(R(), "Swift_Apple::Zero2Hero::08-SwiftData-Persistence"),
    "Architecture": genanki.Deck(R(), "Swift_Apple::Zero2Hero::09-App-Architecture"),
    "Networking": genanki.Deck(R(), "Swift_Apple::Zero2Hero::10-Networking"),
    "Performance": genanki.Deck(R(), "Swift_Apple::Zero2Hero::11-Performance-Diagnostics"),
    "UIKitObjC": genanki.Deck(R(), "Swift_Apple::Zero2Hero::12-UIKit-ObjC-Runtime"),
    "CoreML": genanki.Deck(R(), "Swift_Apple::Zero2Hero::13-CoreML-Vision-ML"),
    "Xcode": genanki.Deck(R(), "Swift_Apple::Zero2Hero::14-Xcode-Toolchain"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ===== 01-SWIFT-CORE =====
c("SwiftCore", "What is the difference between a struct and a class in Swift?",
  "Struct: value type (stack allocation, copied on assignment), no inheritance, no deinit (unless fields are reference types), implicit memberwise init. Class: reference type (heap allocation), reference semantics, inheritance, deinit. Structs are thread-safe by default; classes require synchronization.",
  ["L0_primitives"])

c("SwiftCore", "How does Copy-on-Write (COW) work in Swift?",
  "Not automatic for custom types. stdlib collections (Array, Dictionary, Set, String) use a heap-allocated internal buffer with a reference count. On mutation, <code>isKnownUniquelyReferenced</code> checks if refcount is 1; if not, the buffer is COPIED before mutation. Custom COW requires manual implementation with class-backed storage.",
  ["L2_composition"])

c("SwiftCore", "How does ARC work internally?",
  "Compiler inserts <code>swift_retain</code>/<code>swift_release</code> at every strong reference operation. Refcount stored in object header. Two paths: inline refcount (small objects, fast) and side table (when weak references exist, larger objects). <code>swift_release</code> → RC hits 0 → <code>swift_deallocObject</code> → call <code>deinit</code> → free memory. Weak refs zeroed when strong RC hits 0.",
  ["L2_composition"])

c("SwiftCore", "When should you use <code>weak</code> vs <code>unowned</code>?",
  "<code>weak</code>: optional, nil after deallocation. Runtime overhead (side table, <code>swift_weakLoadStrongRetained</code>). Use for parent→child OK, child→parent use weak. <code>unowned</code>: non-optional, CRASHES if accessed after deallocation (<code>_swift_abortRetainUnowned</code>). Use when lifetime of referenced object is provably ≥ self. Slightly faster than weak.",
  ["L1_mechanics"])

c("SwiftCore", "How do closures capture variables?",
  "By REFERENCE by default — captures the variable itself, not its value. Capture list <code>[weak self, x = value]</code> executes at closure CREATION time. Escaping closures (<code>@escaping</code>) allocated on heap, retain captures. Non-escaping (default): stack-allocated, no retain cycles possible, compiler can optimize heavily.",
  ["L1_mechanics"])

c("SwiftCore", "What is <code>MemoryLayout</code> and what do <code>.size</code>, <code>.stride</code>, and <code>.alignment</code> mean?",
  "<code>.size</code>: bytes for one instance (padding between consecutive array elements). <code>.stride</code>: bytes between consecutive elements in contiguous storage (size + tail padding). <code>.alignment</code>: byte boundary the type must start on. <code>.size(ofValue:)</code> for runtime values.",
  ["L1_mechanics"])

c("SwiftCore", "How does <code>inout</code> work under the hood?",
  "Semantic model: copy-in copy-out. Value copied IN at call site, modified, copied OUT on return. Optimization: if the argument is a stored property with no observers, compiler elides the copy and passes a direct pointer (<code>&amp;variable</code>). Computed properties / observers always use copy-in copy-out.",
  ["L2_composition"])

c("SwiftCore", "What is the Exclusive Access to Memory law?",
  "A variable cannot be accessed for mutation AND reading (or another mutation) simultaneously. Enforced statically by compiler and dynamically via <code>beginAccess</code>/<code>endAccess</code>. <code>x.append(x.last!)</code> — x mutated + read simultaneously → runtime trap in debug builds. Non-overlapping stored properties of same struct are fine.",
  ["L3_design"])

c("SwiftCore", "What does <code>mutating</code> do on a struct method?",
  "<code>mutating func</code> gets implicit <code>inout self</code>. Semantically: assign modified value back to self. Can reassign <code>self = NewValue</code> (memberwise assignment). Classes do NOT use <code>mutating</code> — reference semantics allow direct mutation. In protocols: if defined without <code>mutating</code>, structs can't reassign self.",
  ["L1_mechanics"])

c("SwiftCore", "What is a <code>defer</code> block and when is it executed?",
  "<code>defer { cleanup() }</code> — block runs when the current scope exits (by return, throw, or falling off the end). Multiple defers execute in REVERSE order (LIFO). Executes even if an error is thrown. Does NOT execute if the process crashes or is force-killed.",
  ["L1_mechanics"])

c("SwiftCore", "What is property wrapper and how is it lowered by the compiler?",
  "<code>@Published var name = ''</code> compiles to: <code>private var _name = Published(wrappedValue: '')</code>, <code>var name: String { get { _name.wrappedValue } set { _name.wrappedValue = newValue } }</code>, <code>var $name: Publisher { _name.projectedValue }</code>. Wrapper struct/class needs <code>wrappedValue</code> and optional <code>projectedValue</code>.",
  ["L2_composition"])

# ===== 02-PROTOCOLS-GENERICS =====
c("Protocols", "What is a Protocol Witness Table (PWT)?",
  "A static table mapping each protocol requirement to a concrete implementation. One PWT per concrete type per protocol conformance. Contains function pointers. At runtime, protocol method dispatch goes through PWT → indirect call. <code>sil_witness_table</code> entries map requirements to implementations in SIL.",
  ["L2_composition"])

c("Protocols", "What is an existential container and how does <code>any P</code> work?",
  "<code>any P</code> is 5 words: 3-word value buffer (if value fits inline, stored directly; if not, heap-allocated with retain/release), metadata pointer, PWT pointer. <code>some P</code> is opaque — NOT existential, fixed concrete type known at compile time, generic specialization, zero boxing overhead.",
  ["L2_composition"])

c("Protocols", "What is the difference between <code>some P</code> and <code>any P</code>?",
  "<code>some P</code>: opaque type. Concrete type fixed at compile time, known to caller. Zero allocation, fully specialized. Function MUST return same concrete type each time. <code>any P</code>: existential. Type erased, boxing overhead. Can hold different types. <code>some View</code> is how SwiftUI avoids existential overhead on every body call.",
  ["L1_mechanics"])

c("Protocols", "What are associated types and the <code>Self</code> requirement?",
  "<code>associatedtype Element</code>: makes a protocol generic. Each conformance provides a concrete <code>typealias</code>. <code>Self</code>: refers to the conforming type itself. Both prevent using the protocol as a concrete type (existential) before Swift 5.7. Primary associated types (<code>Collection&lt;String&gt;</code>) enable existentials with associated types.",
  ["L1_mechanics"])

c("Protocols", "How does generic specialization affect performance?",
  "Compiler monomorphizes: generates a separate copy of the generic function for each unique concrete type used. For <code>Int</code> and <code>String</code> calls, TWO copies in the binary. Zero boxing, static dispatch, fully inlinable. Tradeoff: larger binary size. Can be forced with <code>@_specialize</code> (internal).",
  ["L3_design"])

c("Protocols", "What is a conditional conformance?",
  "<code>extension Array: Equatable where Element: Equatable {}</code>. Array is Equatable ONLY when its elements are. Implemented as additional PWT entries with a runtime predicate check. Transitive: <code>[[Int]]</code> is Equatable because <code>[Int]</code> is.",
  ["L1_mechanics"])

c("Protocols", "What is the difference between static and dynamic dispatch for protocol methods?",
  "Existential (dynamic): <code>let p: any P = Concrete()</code>; <code>p.method()</code> → lookup PWT → function pointer → indirect call. Generic (static): <code>func f&lt;T: P&gt;(_ x: T)</code> → compiler knows <code>T == Concrete</code> → direct call, inlinable, ~0ns after inlining. Protocol extension methods NOT in requirement use STATIC dispatch based on the STATIC type — dangerous footgun.",
  ["L3_design"])

c("Protocols", "Why do protocol extension methods use static dispatch?",
  "Methods defined ONLY in a protocol extension (not declared in the protocol) dispatch based on the STATIC type, not the dynamic type. <code>let x: P = MyType(); x.method()</code> calls P's extension method, not MyType's override. To get dynamic dispatch: the method MUST be a protocol requirement declared in the protocol body.",
  ["L4_diagnosis"])

# ===== 03-CONCURRENCY =====
c("Concurrency", "How does Swift's <code>async/await</code> work under the hood?",
  "<code>await</code> divides the function into partial continuations. The function's frame (locals, program counter) is heap-allocated as an async frame. On suspension, one heap allocation for the entire continuation (not per-suspension). Frame freed on completion. <code>withUnsafeContinuation</code> for manual continuation (must resume exactly once).",
  ["L2_composition"])

c("Concurrency", "What is structured concurrency and Task hierarchy?",
  "Parent task waits for ALL child tasks. Children inherit: priority, task-local values, cancellation, actor context. <code>async let</code> creates child task, implicitly <code>try await</code> at end of scope. Unstructured <code>Task {}</code> — not a child, must manage manually. <code>Task.detached {}</code> — inherits NOTHING.",
  ["L1_mechanics"])

c("Concurrency", "How does Task cancellation work?",
  "COOPERATIVE. <code>Task.checkCancellation()</code> throws <code>CancellationError</code>. <code>Task.isCancelled</code> for non-throwing branches. <code>withTaskCancellationHandler(operation:onCancel:)</code> — handler runs CONCURRENTLY with operation, at most once. Cancellation propagates parent → children. <code>group.cancelAll()</code> cancels all child tasks.",
  ["L1_mechanics"])

c("Concurrency", "What is an actor and how does actor isolation work?",
  "Actor: reference type protecting its state with a serial executor. All non-async methods are ISOLATED — access from outside requires <code>await</code>. Access from inside the actor is synchronous (you're already on the executor). Only ONE task runs at a time. Re-entrancy: after <code>await</code>, the actor can run OTHER tasks — state may change, re-validate after every await.",
  ["L1_mechanics"])

c("Concurrency", "What is <code>Sendable</code> and what types conform automatically?",
  "Marker protocol for types safe to share across concurrency domains. Auto-conforming: value types (structs/enums with all Sendable members), actors, <code>@MainActor</code> classes (properly synchronized). <code>@Sendable</code> closures: cannot capture non-Sendable mutable state, cannot capture actor-isolated state. <code>@unchecked Sendable</code>: programmer guarantees safety.",
  ["L1_mechanics"])

c("Concurrency", "What is <code>@MainActor</code> and how does it work?",
  "Global actor using the main dispatch queue. <code>@MainActor class ViewModel { var data = [] }</code> — all access serialized on main thread. <code>await MainActor.run { }</code> to dispatch. SwiftUI's <code>@StateObject</code>/<code>@ObservedObject</code> are main-actor-isolated by default in Swift 5.7+.",
  ["L1_mechanics"])

c("Concurrency", "What is <code>AsyncStream</code> and how is it used?",
  "<code>AsyncStream(Element.self) { continuation in continuation.yield(value); continuation.finish() }</code>. Bridges callback-based APIs to async sequences. <code>continuation.onTermination</code> called on cancel/finish/deinit — clean up resources there. <code>AsyncThrowingStream</code> for error-yielding variants.",
  ["L1_mechanics"])

# ===== 04-SWIFTUI-IDENTITY =====
c("SwiftUIID", "What is structural identity vs explicit identity in SwiftUI?",
  "Structural: identity determined by POSITION in the view tree. Same view type at same position = same identity. Explicit: <code>ForEach(data, id: \.key)</code> — identity defined by <code>id</code>. <code>.id()</code> modifier resets identity — all previous state destroyed. Mixing them wrong = bugs.",
  ["L2_composition"])

c("SwiftUIID", "How does <code>@State</code> work internally?",
  "Heap-allocated <code>StateStorage&lt;T&gt;</code> managed by SwiftUI. Initial value used ONLY on first render; subsequent renders preserve the stored value. Changing <code>@State</code> marks owning view for update. <code>$</code> prefix projects <code>Binding</code>. When view is recreated, <code>@State</code> is moved (not copied) to the new view instance.",
  ["L2_composition"])

c("SwiftUIID", "What is the difference between <code>@StateObject</code> and <code>@ObservedObject</code>?",
  "<code>@StateObject</code>: view OWNS the object — created once, preserved across updates, lifecycle tied to view's structural identity. MUST use where object is first created. <code>@ObservedObject</code>: view REFERENCES object owned elsewhere — subscribes to <code>objectWillChange</code>, but object's lifecycle is NOT managed. Golden rule: <code>@StateObject</code> where created; <code>@ObservedObject</code> in subviews.",
  ["L1_mechanics"])

c("SwiftUIID", "How does the <code>@Observable</code> macro (iOS 17+) differ from <code>ObservableObject</code>?",
  "<code>@Observable</code>: tracks at PROPERTY level. Only views reading the changed property re-render. <code>ObservableObject</code>: re-renders ALL observing views when ANY <code>@Published</code> property changes. <code>@Observable</code> eliminates manual <code>@Published</code>, all stored properties auto-tracked. <code>@Bindable</code> creates bindings from <code>@Observable</code> properties.",
  ["L1_mechanics"])

c("SwiftUIID", "What is <code>AnyView</code> and why should you avoid it?",
  "Type erasure: <code>AnyView(content)</code> wraps any view, erasing its concrete type. Destroys static type info — SwiftUI cannot optimize, must do existential dispatch on every update. Avoid in hot paths. Use <code>some View</code> or <code>Group</code> instead. Legitimate: heterogeneous view arrays, returning different types from non-ViewBuilder functions.",
  ["L5_opinion"])

c("SwiftUIID", "What is the View tree vs the Render tree?",
  "View tree: ephemeral value types (your <code>body</code> closures), recreated every update. A 'blueprint'. Render tree: persistent graph of <code>UIView</code>/<code>CALayer</code> nodes — what Core Animation and Metal render. SwiftUI's internal <code>_ViewNode</code> tree maps View tree updates to minimal Render tree changes.",
  ["L2_composition"])

# ===== 05-SWIFTUI-LAYOUT =====
c("Layout", "How does the Layout protocol (iOS 16+) work?",
  "<code>protocol Layout { func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout Cache) -&gt; CGSize; func placeSubviews(in:proposal:subviews:cache:) }</code>. <code>ProposedViewSize</code>: <code>.zero</code>, <code>.infinity</code>, <code>.unspecified</code>, or specific size. Gives full control over subview positioning — supercharged stacks.",
  ["L1_mechanics"])

c("Layout", "How does SwiftUI's layout negotiation work?",
  "Parent proposes size to child, child returns its actual size, parent positions child. Root view receives size from the device screen. Three-step: 1) Parent proposes, 2) Child responds, 3) Parent places. <code>.frame(minWidth:maxWidth:)</code>, <code>.fixedSize()</code>, <code>.layoutPriority()</code> affect negotiation.",
  ["L2_composition"])

c("Layout", "What is <code>GeometryReader</code> and when is it dangerous?",
  "Provides <code>GeometryProxy</code>: <code>.size</code>, <code>.safeAreaInsets</code>, <code>.frame(in:)</code>. Fills ALL available space — causes parent to expand. Expensive. Avoid nested GeometryReaders. Coordinate spaces: <code>.global</code>, <code>.local</code>, <code>.named('id')</code> with <code>.coordinateSpace(name:)</code>.",
  ["L1_mechanics"])

c("Layout", "What is the PreferenceKey system?",
  "Bottom-up propagation: children publish preferences, ancestors read them. <code>protocol PreferenceKey { static var defaultValue: Value; static func reduce(value: inout Value, nextValue: () -&gt; Value) }</code>. <code>.preference(key:value:)</code> publishes. <code>.onPreferenceChange(_:perform:)</code> reads. Used to: read child sizes, pass toolbar items, tab bar data.",
  ["L2_composition"])

c("Layout", "What are anchor preferences and why use them over raw GeometryReader?",
  "<code>Anchor&lt;Value&gt;</code>: opaque reference to a child's geometry. Resolves lazily in parent's coordinate space. <code>.anchorPreference(key:value:transform:)</code> publishes. Unlike raw frames, anchors update automatically when view moves — no stale frame bug. The 'correct' way to read child geometry in complex layouts.",
  ["L3_design"])

# ===== 06-SWIFTUI-ANIMATION =====
c("Animation", "What are the three types of animation in SwiftUI?",
  "Implicit: <code>.animation(.easeInOut, value: flag)</code> — animates all changes to <code>flag</code>. Explicit: <code>withAnimation(.spring()) { flag.toggle() }</code> — wraps state mutation. Transaction: <code>withTransaction(Transaction(animation:.default)) {}</code> — underlying mechanism carrying animation, disablesAnimations, user info.",
  ["L1_mechanics"])

c("Animation", "How does <code>matchedGeometryEffect</code> work?",
  "<code>@Namespace var ns</code>; <code>.matchedGeometryEffect(id: 'x', in: ns)</code>. SwiftUI interpolates position (center) + size between source and destination views. NOT a real shared view — two different views animated to look like one. Properties: <code>.isSource</code> affects opacity fade. Must be in same <code>Namespace.ID</code>.",
  ["L2_composition"])

c("Animation", "What is the <code>Animatable</code> protocol?",
  "<code>protocol Animatable { associatedtype AnimatableData: VectorArithmetic; var animatableData: AnimatableData { get set } }</code>. For each animation frame, SwiftUI interpolates <code>animatableData</code> from start to end. Each interpolated value triggers a body re-evaluation. <code>AnimatablePair</code> for multiple animated properties. Shapes use this for smooth stroke animation.",
  ["L2_composition"])

c("Animation", "What is the transition system and how do asymmetric transitions work?",
  "<code>.transition(.asymmetric(insertion: .scale, removal: .opacity))</code> — different effects for appear/disappear. <code>AnyTransition</code> type erases. Combined: <code>.opacity.combined(with: .scale)</code> both simultaneously. Custom: <code>.modifier(active:identity:)</code>. Transitions = insertion/removal effects; animations = value-change effects.",
  ["L1_mechanics"])

# ===== 07-COMBINE =====
c("Combine", "What is the Publisher-Subscriber-Subscription triad?",
  "Publisher → <code>receive(subscriber:)</code> → calls subscriber's <code>receive(subscription:)</code> → subscriber calls <code>subscription.request(.unlimited)</code> → publisher sends values via <code>subscriber.receive(_:)</code> → ends with <code>subscriber.receive(completion:)</code>. <code>Subscribers.Demand</code> controls backpressure: <code>.none</code>, <code>.unlimited</code>, <code>.max(N)</code>.",
  ["L2_composition"])

c("Combine", "What is the difference between <code>combineLatest</code> and <code>zip</code>?",
  "<code>combineLatest</code>: emits tuple when EITHER emits, using latest from each. All must have emitted at least once. <code>zip</code>: pairs Nth value from each — strict pairing, waits for both. Use <code>combineLatest</code> for form validation (any field change); <code>zip</code> for sequential operations.",
  ["L1_mechanics"])

c("Combine", "What do <code>debounce</code> and <code>throttle</code> do?",
  "<code>.debounce(for: .seconds(0.3), scheduler:)</code>: only emits if no new value for 0.3s. Search field pattern. <code>.throttle(for: .seconds(1), scheduler:, latest: true)</code>: emits at most every 1s. <code>latest: true</code> emits most recent; <code>false</code> emits first. <code>debounce</code> resets the timer on each value; <code>throttle</code> guarantees max frequency.",
  ["L1_mechanics"])

c("Combine", "What is the difference between <code>PassthroughSubject</code> and <code>CurrentValueSubject</code>?",
  "<code>PassthroughSubject</code>: no stored value, new subscribers only get values emitted AFTER subscription. <code>CurrentValueSubject</code>: stores latest value, new subscribers immediately receive it. Must initialize with a value. Use CurrentValueSubject for state (always has value); PassthroughSubject for events (button taps).",
  ["L1_mechanics"])

c("Combine", "What is <code>@Published</code> internally?",
  "Property wrapper on <code>ObservableObject</code> classes. Generates <code>$name</code> (projected value = Publisher, type <code>Published&lt;String&gt;.Publisher</code>). The publisher emits BEFORE the value changes (<code>willSet</code> semantics). <code>ObservableObject</code>'s default <code>objectWillChange</code> emits on any <code>@Published</code> change. In <code>sink</code>, property still has old value.",
  ["L2_composition"])

# ===== 08-SWIFTDATA-PERSISTENCE =====
c("SwiftData", "What does the <code>@Model</code> macro do?",
  "Converts a class into a SwiftData persistent model. Expands to: <code>@PersistedProperty</code> for each stored property, conformance to <code>PersistentModel</code>, schema metadata. <code>@Attribute(.unique, .externalStorage)</code> configures properties. <code>@Relationship(deleteRule: .cascade, inverse:)</code> for relationships.",
  ["L1_mechanics"])

c("SwiftData", "What is <code>ModelContainer</code> and <code>ModelContext</code>?",
  "<code>ModelContainer</code>: wraps <code>NSPersistentContainer</code>, manages the persistent store. <code>try ModelContainer(for: Schema.self)</code>. <code>ModelContext</code>: scoped to a view/operation. <code>@Environment(\\.modelContext) var context</code>. Auto-saves. NOT Sendable — use <code>@MainActor</code> for main thread, <code>container.newBackgroundContext()</code> for background.",
  ["L1_mechanics"])

c("SwiftData", "How does <code>#Predicate</code> work?",
  "<code>#Predicate&lt;Task&gt; { $0.isComplete == false }</code>. Macro builds typed predicate supported by the predicate system. Compiler-checked. Supports: comparison, AND/OR/NOT, collection operators. Limited to predicates expressible in SwiftData's SQL backing. Used with <code>FetchDescriptor(predicate:sortBy:)</code>.",
  ["L1_mechanics"])

c("SwiftData", "What is Core Data faulting?",
  "A fault is a placeholder managed object — properties NOT fetched until accessed. <code>object.isFault</code> → true. Firing a fault: accessing a property triggers SQLite fetch (transparent but potentially expensive). <code>context.refresh(object, mergeChanges: false)</code> turns object back into a fault, freeing memory. <code>returnsObjectsAsFaults = false</code> pre-faults.",
  ["L2_composition"])

c("SwiftData", "What is the relationship between SwiftData and Core Data?",
  "SwiftData is built ON TOP of Core Data. Uses Core Data's SQLite store by default. Added: Swift native API, <code>@Model</code> macro, <code>#Predicate</code>, modern concurrency. NOT all Core Data features exposed yet. Can still access Core Data APIs: <code>modelContext.managedObjectContext</code>. No direct <code>NSFetchedResultsController</code> — <code>@Query</code> replaces it.",
  ["L2_composition"])

# ===== 09-APP-ARCHITECTURE =====
c("Architecture", "What is the <code>App</code> protocol?",
  "<code>@main struct MyApp: App { var body: some Scene { WindowGroup { ContentView() } } }</code>. Replaces <code>UIApplicationDelegate</code>. <code>@SceneBuilder</code> body. <code>@UIApplicationDelegateAdaptor</code> to add AppDelegate. <code>@Environment(\\.scenePhase)</code>: <code>.active</code>, <code>.inactive</code>, <code>.background</code>.",
  ["L1_mechanics"])

c("Architecture", "How does SwiftUI scene lifecycle work?",
  "<code>@Environment(\\.scenePhase) var phase</code>: <code>.active</code> (foreground, receiving events) → <code>.inactive</code> (incoming call, system alert) → <code>.background</code> (backgrounded). <code>.onChange(of: phase)</code> to react. <code>UIApplication.didEnterBackgroundNotification</code> for non-SwiftUI code. Multi-window: each <code>Scene</code> is independent.",
  ["L1_mechanics"])

c("Architecture", "How does WidgetKit work?",
  "<code>struct Provider: TimelineProvider { func getTimeline(in:completion:) -&gt; Timeline }</code>. Returns <code>Timeline(entries:policy:)</code>. Policies: <code>.atEnd</code>, <code>.after(Date)</code>, <code>.never</code>. <code>WidgetCenter.shared.reloadAllTimelines()</code> for refresh. Families: <code>.systemSmall</code>, <code>.systemMedium</code>, <code>.systemLarge</code>, <code>.accessory*</code>. Deep link: <code>.widgetURL(url)</code> → <code>.onOpenURL</code>.",
  ["L1_mechanics"])

c("Architecture", "How do App Extensions work archecturally?",
  "Each extension runs in a SEPARATE process with its own sandbox. Different memory space from main app. IPC via XPC. Share extension: <code>SLComposeServiceViewController</code> + <code>NSExtensionContext</code>. <code>NSItemProvider</code> for data transfer. App Groups: <code>UserDefaults(suiteName:)</code> and shared container for data sharing between app and extensions.",
  ["L2_composition"])

# ===== 10-NETWORKING =====
c("Networking", "What are the three <code>URLSessionConfiguration</code> types?",
  "<code>.default</code>: persistent disk cache, keychain credentials, shared cookie storage. <code>.ephemeral</code>: all in-memory only — no persistent storage (private browsing). <code>.background(withIdentifier:)</code>: upload/download via system daemon even when app suspended. Uses <code>nsurlsessiond</code>. Delivers via delegate when app relaunches.",
  ["L1_mechanics"])

c("Networking", "How does <code>Codable</code> work?",
  "<code>protocol Encodable { func encode(to encoder: Encoder) throws }</code>. <code>protocol Decodable { init(from decoder: Decoder) throws }</code>. Compiler synthesizes when all stored properties are Codable. <code>CodingKeys</code>: nested enum mapping property names to JSON keys. Customization: <code>encodeIfPresent</code>, nested containers, <code>superEncoder/superDecoder</code>.",
  ["L1_mechanics"])

c("Networking", "What are <code>JSONEncoder</code>/<code>JSONDecoder</code> strategies?",
  "<code>keyEncodingStrategy</code>: <code>.convertToSnakeCase</code>, <code>.useDefaultKeys</code>. <code>dateEncodingStrategy</code>: <code>.iso8601</code>, <code>.secondsSince1970</code>, <code>.formatted(DateFormatter)</code>. <code>dataEncodingStrategy</code>: <code>.base64</code>. <code>nonConformingFloatEncodingStrategy</code>: <code>.throw</code> or <code>.convertToString</code>. <code>PropertyListEncoder</code> for <code>.binary</code>/<code>.xml</code>.",
  ["L1_mechanics"])

c("Networking", "What is ATS (App Transport Security)?",
  "Enforced by default: HTTPS required, HTTP connections fail. Exceptions: <code>NSAppTransportSecurity</code> → <code>NSExceptionDomains</code>. <code>NSAllowsArbitraryLoads</code> opts out entirely (Apple rejects without justification). WKWebView has separate ATS settings. TLS version requirements can be reduced via exceptions.",
  ["L1_mechanics"])

# ===== 11-PERFORMANCE =====
c("Performance", "What Instruments should you use for different performance issues?",
  "CPU: Time Profiler (sampling, call tree). Memory: Allocations (heap, generations, backtraces), Leaks (reference counting analysis). GPU: Core Animation (FPS, offscreen rendering, blended layers). Battery: Energy Log (per-component energy cost). System-wide: System Trace (thread scheduling, context switches, syscalls).",
  ["L1_mechanics"])

c("Performance", "How does <code>os_signpost</code> work with Instruments?",
  "<code>os_signpost(.begin, log: log, name: 'fetch', 'URL: %{public}@', url)</code>. <code>.end</code> marks completion. <code>.event</code> for single points. Visible in Instruments <code>os_signpost</code> instrument — correlates with other instruments. <code>%{public}@</code> for public data, <code>%@</code> for private (redacted outside development).",
  ["L1_mechanics"])

c("Performance", "What triggers offscreen rendering in iOS?",
  "<code>cornerRadius</code> + <code>masksToBounds</code>, <code>shadow</code> without <code>shadowPath</code>, <code>mask</code>, <code>groupOpacity</code>. GPU creates offscreen buffer, renders into it, composites back. Expensive — measure with Core Animation instrument. Fix: set <code>layer.shadowPath</code>, use pre-rendered images, avoid complex corners on frequently changing views.",
  ["L4_diagnosis"])

c("Performance", "How do you optimize iOS launch time?",
  "Pre-main: load dylibs, rebase/bind, ObjC init, static initializers. Measure with <code>DYLD_PRINT_STATISTICS</code>. Post-main: lazy initialization, defer non-critical work, use <code>Task { @MainActor in }</code> for async setup. <code>MXMetricManager</code> for production metrics: <code>MXAppLaunchMetric</code> has <code>histogrammedTimeToFirstDraw</code>.",
  ["L2_composition"])

# ===== 12-UIKIT-OBJC =====
c("UIKitObjC", "How does <code>UIViewRepresentable</code> bridge UIKit to SwiftUI?",
  "<code>func makeUIView(context:) -&gt; UIView</code> (create). <code>func updateUIView(_:context:)</code> (update). <code>context.coordinator</code> for delegate/callback handling. <code>func makeCoordinator() -&gt; Coordinator</code>. <code>UIViewControllerRepresentable</code> for view controllers. <code>HostingController</code>: embed SwiftUI in UIKit (<code>UIHostingController(rootView:)</code>).",
  ["L1_mechanics"])

c("UIKitObjC", "What is the UIKit responder chain?",
  "Events traverse from first responder up the view hierarchy: view → superview → view controller → parent view controller → window → application → app delegate. <code>next</code> property defines the chain. <code>UITextView</code>, <code>UITextField</code> become first responder. <code>resignFirstResponder()</code> to dismiss keyboard.",
  ["L1_mechanics"])

c("UIKitObjC", "How does <code>objc_msgSend</code> work?",
  "Objective-C's dynamic dispatch. <code>[obj method:arg]</code> compiles to <code>objc_msgSend(obj, @selector(method:), arg)</code>. Looks up method in obj's <code>isa</code> pointer → class method table → superclass chain. Method cache for fast path. This is why ObjC is 'dynamic' — method resolution at runtime, unlike Swift's vtable/dispatch.",
  ["L3_design"])

c("UIKitObjC", "What is method swizzling?",
  "Swapping method implementations at runtime: <code>method_exchangeImplementations(class_getInstanceMethod(cls, @selector(original)), class_getInstanceMethod(cls, @selector(swizzled)))</code>. Used for: analytics injection, UI customization, bug fixes in closed-source frameworks. Dangerous — affects ALL instances globally, order-dependent, conflicts between frameworks. Prefer subclassing.",
  ["L6_innovation"])

c("UIKitObjC", "What are Toll-Free Bridged types?",
  "Core Foundation C types that are interchangeable with their Foundation ObjC counterparts: <code>CFString</code> ↔ <code>NSString</code>, <code>CFArray</code> ↔ <code>NSArray</code>, <code>CFDictionary</code> ↔ <code>NSDictionary</code>, <code>CFData</code> ↔ <code>NSData</code>. <code>as</code> casting bridges automatically. <code>__bridge</code> (no ownership change), <code>__bridge_retained</code> (retain), <code>__bridge_transfer</code> (release).",
  ["L1_mechanics"])

c("UIKitObjC", "How do blocks work in Objective-C?",
  "Stack-allocated by default — must <code>Block_copy</code> to heap for use after scope exits. Capture variables by value unless <code>__block</code> modifier (creates mutable storage). Blocks are ObjC objects — can be <code>retain</code>/<code>release</code>'d. Swift closures are fully interoperable with ObjC blocks (<code>@convention(block)</code>).",
  ["L1_mechanics"])

c("UIKitObjC", "How does <code>@objc</code> attribute work in Swift?",
  "Exposes Swift declarations to the ObjC runtime. Required for: ObjC targets calling Swift code, <code>#selector</code>, <code>KVO</code>, dynamic dispatch. Inferred automatically for <code>NSObject</code> subclasses overriding ObjC methods. Enables <code>dynamic</code> dispatch (vs static/vtable). <code>@objcMembers</code> exposes all members of a class.",
  ["L1_mechanics"])

# ===== 13-COREML-VISION =====
c("CoreML", "What is Core ML's model pipeline?",
  "1) Train model (Python — TensorFlow, PyTorch, scikit-learn). 2) Convert to <code>.mlmodel</code> (coremltools). 3) Add to Xcode → auto-generates Swift class. 4) <code>let model = try MyModel(configuration:)</code>. 5) <code>let prediction = try model.prediction(input:)</code>. Supports on-device inference, CPU/GPU/Neural Engine.",
  ["L1_mechanics"])

c("CoreML", "What are the three compute units in Core ML?",
  "<code>.all</code> (default: Neural Engine → GPU → CPU). <code>.cpuOnly</code> (debugging, testing). <code>.cpuAndGPU</code> (excludes Neural Engine). <code>.cpuAndNeuralEngine</code> (excludes GPU). Neural Engine (ANE) is the fastest for supported ops — up to 11 TOPS on A17 Pro. Not all model ops support all compute units.",
  ["L1_mechanics"])

c("CoreML", "What is <code>MLModel</code> configuration?",
  "<code>MLModelConfiguration()</code> controls: <code>computeUnits</code>, <code>allowLowPrecisionAccumulationOnGPU</code> (faster, less accurate), <code>preferredMetalDevice</code> (specific GPU). For updating: <code>MLUpdateTask</code> for on-device training. <code>MLModel.compileModel(at:)</code> pre-compiles for faster first load.",
  ["L1_mechanics"])

c("CoreML", "How does the Vision framework integrate with Core ML?",
  "<code>VNCoreMLModel(for:).</code> wraps <code>.mlmodel</code> for Vision pipeline. <code>VNImageRequestHandler</code> processes images: <code>VNClassifyImageRequest</code>, <code>VNRecognizeTextRequest</code>, <code>VNDetectFaceRectanglesRequest</code>, <code>VNDetectHumanBodyPoseRequest</code>. VN + CoreML: pre-processing (resize, normalize, crop) handled automatically.",
  ["L2_composition"])

c("CoreML", "What is Create ML?",
  "Apple's no-code/low-code ML training tool. Templates: Image Classification, Object Detection, Sound Classification, Text Classification, Tabular Classification, Recommendation. Trains on-device using Transfer Learning. Exports <code>.mlmodel</code>. Built on top of Core ML. Limited compared to full Python frameworks but sufficient for many app-level ML features.",
  ["L1_mechanics"])

c("CoreML", "What is <code>MLTensor</code> and the MLX framework?",
  "<code>MLTensor</code> (iOS 18+/macOS 15+): lazy tensor computation API. <code>let x = MLTensor(shape: [3, 3], scalars: [1,2,3,4,5,6,7,8,9])</code>. Operations: <code>x.transposed()</code>, <code>x.matmul(y)</code>, <code>x + y</code>. Lazy: computation deferred, optimized graph-level. MLX: Apple's open-source ML framework (Python, Swift) for research — <code>mlx-swift</code> for on-device inference.",
  ["L1_mechanics"])

c("CoreML", "How do you optimize a Core ML model for on-device performance?",
  "1) Quantization: <code>coremltools.models.MLModel.quantize_weights</code> — FP32 → FP16/INT8, ~2-4x smaller, faster on Neural Engine. 2) Palettization: reduces weights to a palette of values. 3) Compile ahead of time: <code>MLModel.compileModel(at:)</code>. 4) Batch prediction: <code>MLArrayBatchProvider</code> for multiple inputs. 5) Profile with Core ML Performance Report in Xcode.",
  ["L2_composition"])

# ===== 14-XCODE-TOOLCHAIN =====
c("Xcode", "What are the key LLDB commands for debugging?",
  "<code>expression</code> (<code>e</code>): evaluate in current frame. <code>po</code> (expression -O): print object description. <code>frame variable</code> (<code>v</code>): show locals (no code execution, faster than e/po). <code>breakpoint set -n funcName</code>. <code>watchpoint set variable</code> (break on value change). <code>thread backtrace</code> (<code>bt</code>). <code>image lookup -a addr</code> (symbolicate).",
  ["L1_mechanics"])

c("Xcode", "What is code signing and provisioning?",
  "Code signing: cryptographic signature proving app comes from you. Provisioning profile: ties your developer account + app ID + device UDIDs + entitlements. Development: debug builds (specific devices). Distribution: App Store or ad-hoc. Managed automatically with Xcode's 'Automatically manage signing' or manually via Apple Developer portal.",
  ["L1_mechanics"])

c("Xcode", "What are module stability and library evolution?",
  "Module stability: compiled <code>.swiftmodule</code> works across compiler versions. Enabled with <code>Build Libraries for Distribution</code>. Library evolution: <code>@frozen</code> (struct/enum layout fixed), <code>@inlinable</code> (function body available for inlining across modules). Enables ABI-stable frameworks. Required for Swift binary frameworks distributed via Swift Package Manager.",
  ["L3_design"])

c("Xcode", "What are the Swift compiler optimization flags?",
  "<code>-Onone</code>: no optimization, fastest compilation (debug). <code>-O</code>: optimize for speed (release). <code>-Osize</code>: optimize for size (smaller binary). <code>-wmo</code> (Whole Module Optimization): optimizes across files (slower compile, better runtime). <code>-enforce-exclusivity=unchecked</code>: disables runtime exclusive access checks (faster, dangerous).",
  ["L1_mechanics"])

c("Xcode", "What are access control levels in Swift?",
  "<code>open</code>: accessible outside module, subclassable, overridable. <code>public</code>: accessible outside module, NOT subclassable/overridable outside. <code>internal</code>: accessible within module (default). <code>fileprivate</code>: accessible within same file. <code>private</code>: accessible within same declaration (class, extension).",
  ["L0_primitives"])

c("Xcode", "What is the Swift Package Manager (SPM) manifest?",
  "<code>Package.swift</code>: <code>let package = Package(name:, products:, dependencies:, targets:)</code>. Targets: <code>.target(name:, dependencies:[])</code>, <code>.testTarget(name:, dependencies:[])</code>. Products: <code>.library(name:, targets:[])</code>, <code>.executable</code>. Dependencies: <code>.package(url:, from:)</code>. Platforms: <code>platforms: [.iOS(.v15)]</code>.",
  ["L1_mechanics"])

# ===== BUILD =====
for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

fn = "Swift_Apple_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(fn)
print(f"Built {len(decks)} decks with {len(C)} cards -> {fn}")
