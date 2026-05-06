import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Unreal_Engine"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Blueprint":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Blueprints"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === UNREAL FUNDAMENTALS ===

c("Fundamentals", "What is Unreal Engine?",
  "A real-time 3D engine by Epic Games for games, film, architecture, and simulation. Uses C++ with Blueprint visual scripting. Known for high-fidelity graphics, Nanite geometry, Lumen GI.",
  ["L0_primitives"])

c("Fundamentals", "What is an Actor in Unreal?",
  "The base class for any object that can be placed in a level. Actors have a transform (position, rotation, scale) and can contain Components. <code>AActor</code> in C++, every object in the world is an Actor.",
  ["L0_primitives"])

c("Fundamentals", "What is a Component in Unreal?",
  "A reusable piece of functionality that can be added to an Actor. Examples: <code>UStaticMeshComponent</code>, <code>USkeletalMeshComponent</code>, <code>UCameraComponent</code>. Actors are containers; Components do the work.",
  ["L0_primitives"])

c("Fundamentals", "What is a Pawn?",
  "A subclass of Actor that can be possessed by a Controller. Represents the player or AI's physical presence in the world. Can receive input. <code>APawn</code> is the base for <code>ACharacter</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is a Character?",
  "A Pawn subclass with built-in movement: <code>ACharacter</code> comes with a <code>CapsuleComponent</code> for collision, <code>CharacterMovementComponent</code> for walking/flying/swimming, and a SkeletalMesh for the visual.",
  ["L0_primitives"])

c("Fundamentals", "What is a Controller?",
  "The brain of a Pawn. <code>APlayerController</code> processes human input. <code>AAIController</code> runs behavior trees for AI. A Controller can possess/unpossess Pawns at runtime (e.g., switching characters).",
  ["L0_primitives"])

c("Fundamentals", "What is Blueprint Visual Scripting?",
  "A node-based scripting system. Dragging wires between nodes to define gameplay logic, no C++ required. Blueprints are compiled into bytecode. Great for iteration; C++ for performance-critical code.",
  ["L0_primitives"])

c("Fundamentals", "What is a GameMode?",
  "Defines the rules of the game. Only exists on the server. Sets default Pawn class, PlayerController class, and handles spawning, scoring, win conditions. <code>AGameModeBase</code> for basic, <code>AGameMode</code> for full match states.",
  ["L0_primitives"])

c("Fundamentals", "What is the GameInstance?",
  "A persistent object that exists for the lifetime of the game process. Survives level transitions. Stores global data (settings, save data, multiplayer sessions). <code>UGameInstance</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is a Level in Unreal?",
  "A <code>.umap</code> file containing Actors, geometry, lights. Think of it as a scene/map. Levels can be streamed in/out at runtime (Level Streaming) for open-world games.",
  ["L0_primitives"])

c("Fundamentals", "What is the Unreal reflection system?",
  "A system that inspects classes, properties, and functions at runtime. Enabled by macros: <code>UCLASS()</code>, <code>UPROPERTY()</code>, <code>UFUNCTION()</code>. Powers Blueprint exposure, garbage collection, serialization, network replication.",
  ["L0_primitives"])

c("Fundamentals", "What is Nanite?",
  "Unreal Engine 5's virtualized geometry system. Imports film-quality meshes (millions of polygons) and automatically creates multi-resolution data. Only processes visible detail. No manual LOD creation needed.",
  ["L0_primitives"])

c("Fundamentals", "What is Lumen?",
  "Unreal Engine 5's dynamic global illumination and reflections system. Computes lighting in real-time as lights/geometry change. No lightmap baking needed. Works with emissive surfaces, skylight, and bounced light.",
  ["L0_primitives"])

c("Fundamentals", "What is the Gameplay Ability System (GAS)?",
  "A framework for building attribute-driven, ability-based gameplay (RPGs, MOBAs). Uses <code>GameplayAbilities</code>, <code>GameplayEffects</code>, <code>AttributeSet</code>, and <code>GameplayTags</code>. Built-in prediction and replication.",
  ["L0_primitives"])

# === UNREAL CORE OPS ===

c("CoreOps", "What does <code>UPROPERTY()</code> do?",
  "Exposes a C++ member variable to the Unreal reflection system. Enables Blueprint access, serialization, replication, editor visibility, and garbage collection. Example: <code>UPROPERTY(EditAnywhere) int32 Health;</code>",
  ["L1_mechanics"])

c("CoreOps", "What does <code>UFUNCTION()</code> do?",
  "Exposes a C++ function to the reflection system. Specifiers: <code>BlueprintCallable</code> (call from BP), <code>Server/Client/NetMulticast</code> (RPC), <code>BlueprintImplementableEvent</code> (implement in BP), <code>BlueprintNativeEvent</code> (default in C++, override in BP).",
  ["L1_mechanics"])

c("CoreOps", "What is the <code>BeginPlay</code> event?",
  "Called when the Actor enters the world and gameplay begins. Equivalent to <code>Start</code> in Unity. Use for initialization that requires the world state. Called after all components are initialized.",
  ["L1_mechanics"])

c("CoreOps", "What is the event graph in Blueprints?",
  "A graph where you wire event nodes (BeginPlay, Tick, input events, custom events) to function nodes. Event nodes are red, function nodes are blue. Execution flows left-to-right along white wires.",
  ["L1_mechanics"])

c("CoreOps", "How do you trace a line in Unreal?",
  "<code>UKismetSystemLibrary::LineTraceSingle</code> in C++, or <code>LineTraceByChannel</code> node in Blueprints. Returns a hit result with the Actor, location, normal. Used for shooting, interaction, vision.",
  ["L1_mechanics"])

c("CoreOps", "How do you spawn an Actor?",
  "In C++: <code>GetWorld()-&gt;SpawnActor&lt;AMyActor&gt;(Class, &amp;Transform, SpawnParams)</code>. In BP: <code>Spawn Actor from Class</code> node. Always pass a valid World context.",
  ["L1_mechanics"])

c("CoreOps", "How do you destroy an Actor?",
  "Call <code>Actor-&gt;Destroy()</code> in C++, or <code>Destroy Actor</code> node in BP. The Actor is removed from the world during garbage collection. Use <code>IsValid()</code> to check if still alive.",
  ["L1_mechanics"])

c("CoreOps", "How do you play a sound?",
  "<code>UGameplayStatics::PlaySound2D</code> or <code>PlaySoundAtLocation</code>. In BP: <code>Play Sound 2D</code> or <code>Play Sound at Location</code> node. <code>UAudioComponent</code> for looping/3D spatialized audio.",
  ["L1_mechanics"])

c("CoreOps", "What is a Timer in Unreal?",
  "<code>GetWorldTimerManager().SetTimer(Handle, this, &amp;AMyActor::TimerFunc, 1.0f, bLoop)</code>. In BP: <code>Set Timer by Event</code> or <code>Set Timer by Function Name</code>. <code>ClearTimer</code> to cancel.",
  ["L1_mechanics"])

c("CoreOps", "How do you bind input in C++?",
  "In <code>SetupPlayerInputComponent</code>: <code>InputComponent-&gt;BindAction(\"Jump\", IE_Pressed, this, &amp;ACharacter::Jump)</code> or <code>BindAxis(\"MoveForward\", this, &amp;AMyPawn::MoveForward)</code>. Requires <code>EnhancedInputComponent</code> for UE5 Input System.",
  ["L1_mechanics"])

c("CoreOps", "What is <code>Cast</code> in Blueprints?",
  "Type conversion: safely converts a generic reference to a specific class. <code>Cast To MyClass</code> node. If the object is of that type, execution continues from <code>then</code> pin. If not, from <code>cast failed</code>. Use <code>CastChecked</code> when you know the type.",
  ["L1_mechanics"])

# === BLUEPRINT MECHANICS ===

c("Blueprint", "What is the <code>Event Tick</code> node?",
  "Fires every frame. Provides <code>Delta Seconds</code> — time since last frame. Use for continuous updates (movement, rotation). Multiply all changes by Delta Seconds for frame-rate independence.",
  ["L1_mechanics"])

c("Blueprint", "What is a Macro in Blueprints?",
  "A reusable node graph with input/output pins, like a function but expanded inline. No execution overhead. Used for utility operations: <code>ForEach Loop with Break</code> is a built-in macro.",
  ["L2_composition"])

c("Blueprint", "What is a Blueprint Interface?",
  "A contract defining function signatures without implementation. Any Blueprint/Actor implementing the interface MUST provide the function body. Enables polymorphic communication between unrelated Actors.",
  ["L0_primitives"])

c("Blueprint", "What's the difference between <code>Pure</code> and <code>Impure</code> functions in BP?",
  "Pure: no execution pins (green node), no side effects, called on-demand when output is needed. Impure: has execution pins (white wire), called when execution reaches it. Use pure for getters/calculations.",
  ["L4_diagnosis"])

c("Blueprint", "What is an Event Dispatcher?",
  "A multicast delegate in Blueprints. One Actor binds to it (<code>Bind Event to ...</code>), another calls it. Decouples sender and receiver. Use for loose coupling between Blueprints.",
  ["L0_primitives"])

c("Blueprint", "What is the <code>Delay</code> node?",
  "Pauses execution for a specified number of seconds. Uses a latent action — execution continues from the <code>Completed</code> pin after the delay. Cannot be used in functions (only event graphs/macros).",
  ["L1_mechanics"])

c("Blueprint", "What is a Blueprint Native Event?",
  "A C++ function with <code>UFUNCTION(BlueprintNativeEvent)</code>. C++ provides the default implementation (<code>_Implementation</code> suffix). Blueprints can override it. Used when you need a C++ base with BP customization.",
  ["L2_composition"])

# === UNREAL PATTERNS ===

c("Patterns", "What is the actor-component-composition pattern?",
  "Prefer adding Components to Actors over deep inheritance. Instead of <code>ADamageableDestroyableMovingActor</code>, compose: <code>UHealthComponent</code> + <code>UDestructionComponent</code> + <code>UMovementComponent</code>.",
  ["L3_design"])

c("Patterns", "What is the Gameplay Tag pattern?",
  "Hierarchical tags (<code>Ability.Magic.Fire</code>) used for categorization and queries. Replace boolean flags and enums. Used in GAS for ability blocking, damage types, buff categories. <code>HasTag()</code> checks.",
  ["L3_design"])

c("Patterns", "What is the interface communication pattern?",
  "Instead of hard-referencing specific classes, use Blueprint Interfaces. Actor A calls <code>Interact</code> on whatever it's looking at. Actor B, C, D can each implement <code>Interact</code> differently.",
  ["L2_composition"])

c("Patterns", "What is the Data Asset pattern?",
  "Use <code>UDataAsset</code> or <code>UPrimaryDataAsset</code> for configuration data. Instead of hardcoding item stats, create a <code>UItemData</code> asset. Designers can tweak values without touching code.",
  ["L3_design"])

c("Patterns", "What is the Subsystem pattern?",
  "<code>UGameInstanceSubsystem</code>, <code>UWorldSubsystem</code>, <code>ULocalPlayerSubsystem</code>. Singletons scoped to GameInstance, World, or LocalPlayer. Auto-instantiated. Use for manager classes (AchievementSystem, UIManager).",
  ["L3_design"])

# === UNREAL GOTCHAS ===

c("Gotchas", "Why is my <code>BeginPlay</code> not called?",
  "Actor might not be spawned yet, or <code>Super::BeginPlay()</code> is missing in C++ override. Also check that the Actor is actually placed in a loaded level or spawned via <code>SpawnActor</code>.",
  ["L4_diagnosis"])

c("Gotchas", "What causes 'Accessed None' errors?",
  "Trying to access a variable that is null. Common in Blueprints when a reference isn't set in the details panel. Always use <code>IsValid</code> node before accessing references.",
  ["L4_diagnosis"])

c("Gotchas", "Why does my C++ class not appear in Blueprints?",
  "Missing <code>UCLASS(Blueprintable)</code> or <code>UCLASS(BlueprintType)</code> on the struct/class. Also check the module's <code>Build.cs</code> includes the necessary dependency modules.",
  ["L4_diagnosis"])

c("Gotchas", "What is the client-server replication mismatch?",
  "In multiplayer, code runs on server AND clients. <code>GameMode</code> only exists on server. Use <code>HasAuthority()</code> to check. RPCs must be marked <code>Server</code>, <code>Client</code>, or <code>NetMulticast</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why did my Blueprint compile but logic is wrong?",
  "Execution order on the same node depends on pin connection order. Blueprints evaluate <code>then 0, then 1, ...</code> in order. For deterministic order, use a <code>Sequence</code> node. For parallel, wire separately.",
  ["L4_diagnosis"])

c("Gotchas", "What are 'Hot Reload' dangers in C++?",
  "Live coding / hot reload can corrupt Blueprint references or cause crashes. After structural C++ changes (new UPROPERTY, UFUNCTION), close the editor and rebuild. Use Live Coding only for function implementation changes.",
  ["L4_diagnosis"])

# === UNREAL EXPERT ===

c("Expert", "What is Enhanced Input System vs Legacy Input?",
  "Enhanced Input (UE5): Input Actions + Input Mapping Contexts, more flexible (chords, hold/tap, priority). Legacy: Action/Axis mappings in Project Settings. Use Enhanced Input for new projects.",
  ["L3_design"])

c("Expert", "What are Quixel Megascans?",
  "A library of photorealistic 3D assets (scanned surfaces, plants, rocks) free for Unreal Engine users. Integrated via Bridge plugin. Use for environment art and prototyping.",
  ["L5_opinion"])

c("Expert", "When should you use C++ vs Blueprints?",
  "C++: performance-critical code, complex algorithms, engine extensions, threading. Blueprints: gameplay scripting, UI logic, rapid prototyping, designer-facing logic. Best practice: C++ base classes with Blueprint children for tweaks.",
  ["L5_opinion"])

c("Expert", "What is World Partition?",
  "UE5's replacement for World Composition/Level Streaming. Divides the world into a grid of cells. Only cells within the streaming distance are loaded. Automatically managed — no manual level streaming setup.",
  ["L6_innovation"])

c("Expert", "What is the MetaHuman framework?",
  "Cloud-based tool for creating photorealistic human characters. Provides a fully rigged, animation-ready skeletal mesh with facial rig. Exports to Unreal. Use for realistic NPCs and player characters.",
  ["L6_innovation"])

c("Expert", "What is Niagara VFX?",
  "UE5's advanced particle and visual effects system. Replaces Cascade. Uses a modular, GPU-simulation-friendly approach. Supports Houdini-like data flow, custom modules, and complex GPU particle interactions.",
  ["L6_innovation"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
