import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "gRPC"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "Protobuf":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Protobuf-Basics"),
    "ServiceDef":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Service-Definitions"),
    "Streaming":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Streaming"),
    "Ecosystem":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Ecosystem-Tooling"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Advanced-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ── 01 FUNDAMENTALS ──────────────────────────────────────────────

c("Fundamentals",
    "What is gRPC?",
    "<b>gRPC</b> (gRPC Remote Procedure Call) is an open-source, high-performance RPC framework by Google. It uses <b>HTTP/2</b> for transport, <b>Protocol Buffers</b> as the IDL and wire format, and supports unary, server-streaming, client-streaming, and bidirectional-streaming RPCs across many languages.",
    ["fundamentals", "definition"])

c("Fundamentals",
    "What are Protocol Buffers (protobuf)?",
    "<b>Protocol Buffers</b> (protobuf) is a language-neutral, platform-neutral, extensible mechanism for serializing structured data. You define the schema in <code>.proto</code> files, then generate data access classes for your language. It is smaller, faster, and stricter than JSON/XML.",
    ["fundamentals", "protobuf"])

c("Fundamentals",
    "Why does gRPC use HTTP/2 instead of HTTP/1.1?",
    "HTTP/2 provides:<br>• <b>Multiplexing</b> — many requests/streams over one TCP connection<br>• <b>Header compression</b> (HPACK) reduces overhead<br>• <b>Bidirectional streaming</b> (server-push, full-duplex)<br>• <b>Binary framing</b> — smaller and faster to parse<br>HTTP/1.1 is text-based, half-duplex, and requires connections per request.",
    ["fundamentals", "http2"])

c("Fundamentals",
    "What is a <code>.proto</code> file?",
    "A <code>.proto</code> file is a schema definition written in the protobuf IDL. It declares messages (data structures), enums, and services (RPC methods). Example:<br><pre>syntax = \"proto3\";<br>package example;<br><br>message HelloRequest {<br>  string name = 1;<br>}<br>message HelloReply {<br>  string message = 2;<br>}<br>service Greeter {<br>  rpc SayHello (HelloRequest) returns (HelloReply);<br>}</pre>",
    ["fundamentals", "proto-file"])

c("Fundamentals",
    "What is the difference between a <b>service definition</b> and a <b>message definition</b>?",
    "<b>Service definition</b> declares the RPC methods (the API contract):<br><pre>service UserService {<br>  rpc GetUser(GetUserReq) returns (GetUserResp);<br>}</pre><b>Message definition</b> declares the data structures:<br><pre>message GetUserReq {<br>  string user_id = 1;<br>}<br>message GetUserResp {<br>  string name = 1;<br>  int32 age = 2;<br>}</pre>Services describe behavior; messages describe data.",
    ["fundamentals", "service-vs-message"])

c("Fundamentals",
    "What is a <b>client stub</b> and a <b>server stub</b> in gRPC?",
    "A <b>client stub</b> (generated from <code>.proto</code>) provides methods that look like local calls but transparently serialize, send over the network, and deserialize the response.<br><br>A <b>server stub</b> (also generated) receives network requests, deserializes them, calls your service implementation, serializes the reply, and sends it back.<br><br>Together they abstract all networking/serialization.",
    ["fundamentals", "stubs"])

c("Fundamentals",
    "What is a <b>unary RPC</b>?",
    "The simplest gRPC pattern: client sends a <b>single request</b> and gets a <b>single response</b> — just like a normal function call.<br><pre>rpc GetUser (GetUserRequest) returns (GetUserResponse);</pre>No <code>stream</code> keyword on either side.",
    ["fundamentals", "unary"])

c("Fundamentals",
    "What is an <b>IDL (Interface Definition Language)</b> and why does gRPC use one?",
    "An IDL is a language-agnostic way to describe API contracts. gRPC uses <b>protobuf</b> as its IDL so you write the contract once (<code>.proto</code>) and generate type-safe client/server code for any supported language. This enforces the contract at compile time rather than runtime.",
    ["fundamentals", "idl"])

c("Fundamentals",
    "gRPC vs REST: key differences?",
    "<b>gRPC</b>:<br>• Binary (protobuf) — smaller, faster<br>• HTTP/2 — multiplexing, streaming<br>• Strongly typed contracts (<code>.proto</code>)<br>• Auto-generated client/server stubs<br>• Supports all streaming patterns<br><br><b>REST</b>:<br>• JSON (human-readable, larger)<br>• HTTP/1.1 (one request per connection typically)<br>• Loose contracts (OpenAPI optional)<br>• Manual HTTP client code<br>• Unary only (chunked transfer is hacky)",
    ["fundamentals", "vs-rest"])

c("Fundamentals",
    "gRPC vs GraphQL: key trade-offs?",
    "<b>gRPC</b>: Precise, high-performance, strongly-typed contracts. Best for <b>service-to-service</b> communication in microservices.<br><br><b>GraphQL</b>: Flexible queries where clients pick exactly what data they need. Best for <b>client-to-server</b> (web/mobile apps) where bandwidth matters and data shapes vary often.<br><br>gRPC is faster and stricter; GraphQL is more flexible but heavier.",
    ["fundamentals", "vs-graphql"])

c("Fundamentals",
    "gRPC vs tRPC (TypeScript): when choose which?",
    "<b>tRPC</b>: End-to-end type-safe without code generation. Share TypeScript types between client and server. <b>Monorepo-only, TypeScript-only</b>.<br><br><b>gRPC</b>: Language-agnostic via <code>.proto</code>. Code generation for every language. Works in <b>polyglot systems</b> (Go, Java, Python, C++, Rust...).<br><br>Choose tRPC for TS-only monorepos; gRPC for polyglot or cross-org boundaries.",
    ["fundamentals", "vs-trpc"])

c("Fundamentals",
    "Where does gRPC shine? (list 5 scenarios)",
    "1. <b>Microservices-to-microservices</b> — low-latency, binary, typed<br>2. <b>Mobile clients</b> — smaller payloads save battery/bandwidth<br>3. <b>Polyglot systems</b> — one <code>.proto</code> generates code for all languages<br>4. <b>Real-time streaming</b> — native bidirectional streams<br>5. <b>Low-latency trading/telecom</b> — protobuf + HTTP/2 optimized for speed<br>6. <b>Internal APIs</b> where strict contracts and codegen are valuable",
    ["fundamentals", "use-cases"])

c("Fundamentals",
    "How does gRPC's binary framing work at a high level?",
    "gRPC messages are serialized as protobuf bytes, prefixed with a 5-byte header:<br>• <b>1 byte</b>: compression flag (0 = none, 1 = compressed)<br>• <b>4 bytes</b>: big-endian uint32 message length<br><br>This length-prefixed framing sits inside HTTP/2 DATA frames. Each gRPC stream is multiplexed over HTTP/2 streams on a single TCP connection.",
    ["fundamentals", "framing"])

c("Fundamentals",
    "What are the four RPC patterns in gRPC?",
    "1. <b>Unary</b> — 1 request, 1 response<br>2. <b>Server streaming</b> — 1 request, many responses<br>3. <b>Client streaming</b> — many requests, 1 response<br>4. <b>Bidirectional streaming</b> — many requests, many responses (order independent)<br><br>The <code>stream</code> keyword on request and/or response determines the pattern.",
    ["fundamentals", "rpc-patterns"])

c("Fundamentals",
    "How does gRPC handle <b>serialization and deserialization</b>?",
    "gRPC uses <b>Protocol Buffers</b> as the default serialization format. When a client makes an RPC:<br>1. Client stub <b>marshals</b> the request message to protobuf bytes<br>2. Bytes are sent over HTTP/2 DATA frames<br>3. Server stub <b>unmarshals</b> bytes back into the typed request object<br>4. Handler processes request<br>5. Response follows the reverse path<br><br>All of this is <b>transparent to application code</b> — you just call methods on typed stubs. Custom serialization (FlatBuffers, MessagePack) is possible via <code>grpc.Codec</code> interface but rarely needed.",
    ["fundamentals", "serialization"])

# ── 02 PROTOBUF BASICS ───────────────────────────────────────────

c("Protobuf",
    "What is the <code>syntax = \"proto3\";</code> declaration?",
    "It declares the protobuf version for the file. <code>proto3</code> is the current standard (simpler, <code>optional</code> is opt-in). <code>proto2</code> had explicit <code>required</code>/<code>optional</code> keywords. Always put this as the first non-comment line in a <code>.proto</code> file.",
    ["protobuf", "syntax"])

c("Protobuf",
    "Define a basic protobuf message with <code>int32</code>, <code>string</code>, and <code>bool</code> fields.",
    "<pre>message UserProfile {<br>  int32  user_id   = 1;<br>  string full_name = 2;<br>  bool   is_active = 3;<br>}</pre>Each field has a <b>type</b>, a <b>name</b>, and a <b>field number</b> (here 1, 2, 3). Field numbers are critical — they identify fields in the binary wire format, never the name.",
    ["protobuf", "message"])

c("Protobuf",
    "List the scalar integer types available in protobuf and their differences.",
    "<b>Signed:</b> <code>int32</code> (varint, negative=10 bytes), <code>int64</code> (varint, negative=10 bytes)<br><b>Optimized-negative:</b> <code>sint32</code>, <code>sint64</code> (ZigZag encoding, efficient for negatives)<br><b>Unsigned:</b> <code>uint32</code>, <code>uint64</code> (varint, unsigned only)<br><b>Fixed:</b> <code>fixed32</code>/<code>fixed64</code> (always 4/8 bytes, good for large numbers)<br><b>Signed-fixed:</b> <code>sfixed32</code>/<code>sfixed64</code> (always 4/8 bytes, signed)<br><br><b>Rule of thumb:</b> Use <code>sint32</code>/<code>sint64</code> when values are often negative; use <code>fixed</code> types when values are consistently large.",
    ["protobuf", "scalar-types"])

c("Protobuf",
    "List the non-integer scalar types in protobuf.",
    "<code>float</code> — 4-byte IEEE 754<br><code>double</code> — 8-byte IEEE 754<br><code>bool</code> — true or false<br><code>string</code> — UTF-8 encoded text (length-prefixed)<br><code>bytes</code> — arbitrary binary data (length-prefixed)",
    ["protobuf", "scalar-types"])

c("Protobuf",
    "Why are <b>field numbers</b> so important in protobuf?",
    "Field numbers <b>identify fields in the wire format</b>, not field names. The field name can be renamed freely; the number must stay the same.<br><br>• Numbers 1-15 use <b>1 byte</b> overhead → use for frequently-set fields<br>• Numbers 16-2047 use <b>2 bytes</b><br>• Numbers 19000-19999 are <b>reserved</b> for protobuf internals<br>• <b>Never reuse</b> a field number, even after deleting a field",
    ["protobuf", "field-numbers"])

c("Protobuf",
    "How do you make a field <code>optional</code> in proto3?",
    "In proto3, all fields are implicitly optional (they have a default zero value). To explicitly track presence (\"was this field set?\"), use the <code>optional</code> keyword:<br><pre>message Example {<br>  optional string nickname = 1; // has has_nickname()<br>  string       name     = 2; // just returns \"\" if unset<br>}</pre>With <code>optional</code>, generated code gets a <code>has_x()</code> method to distinguish \"unset\" from \"set to zero/empty\".",
    ["protobuf", "optional"])

c("Protobuf",
    "How do you define a <code>repeated</code> field?",
    "<pre>message ItemList {<br>  repeated string tags = 1; // zero or more values<br>}</pre>A <code>repeated</code> field can contain <b>0 or more</b> values. In the wire format, it encodes as the same field number repeated per element. The order is preserved during serialization. In Go/Java it generates slice/list accessors.",
    ["protobuf", "repeated"])

c("Protobuf",
    "How do you define a <code>map</code> field in protobuf?",
    "<pre>message ConfigMap {<br>  map&lt;string, int32&gt; settings = 1;<br>}</pre><b>Key constraints:</b> can be any integral or string type.<br><b>Value constraints:</b> can be any type except another map.<br><b>Order is NOT guaranteed</b> — maps are unordered in the wire format.<br>Behind the scenes, a map is syntactic sugar for:<br><pre>message ConfigMapEntry {<br>  string key = 1;<br>  int32 value = 2;<br>}<br>repeated ConfigMapEntry settings = 1;</pre>",
    ["protobuf", "map"])

c("Protobuf",
    "How do you define an <code>enum</code> in protobuf?",
    "<pre>enum Status {<br>  STATUS_UNSPECIFIED = 0; // MUST be 0 (default)<br>  STATUS_ACTIVE      = 1;<br>  STATUS_SUSPENDED   = 2;<br>  STATUS_DELETED     = 3;<br>}</pre><b>Critical rule:</b> the first enum value <b>must be 0</b> (zero-value default). Use a <code>_UNSPECIFIED</code> or <code>_UNKNOWN</code> sentinel. Always prefix enum values to avoid namespace collisions. Use <code>allow_alias = true;</code> in proto2-style enums if needed.",
    ["protobuf", "enum"])

c("Protobuf",
    "How do you define a <code>oneof</code> field?",
    "<pre>message ContactMethod {<br>  oneof method {<br>    string email   = 1;<br>    string phone   = 2;<br>    string address = 3;<br>  }<br>}</pre>A <code>oneof</code> ensures that <b>at most one</b> of the contained fields is set at a time. Setting one auto-clears the others. Backed by a discriminated union on the wire. Use <code>oneof</code> for mutually exclusive fields (e.g., payment methods, contact channels).",
    ["protobuf", "oneof"])

c("Protobuf",
    "How do you define nested messages in protobuf?",
    "<pre>message Outer {<br>  message Inner {<br>    string key   = 1;<br>    int64  value = 2;<br>  }<br>  repeated Inner items = 1;<br>}</pre>Nested messages are scoped inside their parent. Referenced as <code>Outer.Inner</code>. Use for logical grouping when a message is only meaningful in context of its parent.",
    ["protobuf", "nested"])

c("Protobuf",
    "How do you use <code>reserved</code> to prevent field number reuse?",
    "<pre>message LegacyUser {<br>  reserved 2, 15, 9 to 11;      // reserved field numbers<br>  reserved \"old_field\", \"deprecated\"; // reserved field names<br>  string name = 1;<br>  int32  id   = 3;<br>}</pre>Use <code>reserved</code> to <b>permanently prevent</b> reuse of deleted field numbers/names. The compiler will <b>error</b> if anyone tries to use them. This is critical for backward compatibility when removing fields.",
    ["protobuf", "reserved"])

c("Protobuf",
    "What is the role of <code>package</code> in a <code>.proto</code> file?",
    "<pre>package mycompany.services.v1;</pre>The <code>package</code> declaration prevents <b>name collisions</b> across projects/files. It also influences generated code namespaces (e.g., Go package path, Java package, C++ namespace). Different languages map <code>package</code> to their native namespace concepts differently — use <code>option go_package</code> etc. to override.",
    ["protobuf", "package"])

c("Protobuf",
    "How do you import protobuf types from another <code>.proto</code> file?",
    "<pre>import \"google/protobuf/timestamp.proto\";<br>import \"shared/common.proto\";<br><br>message Event {<br>  google.protobuf.Timestamp created_at = 1;<br>  shared.Status status = 2;<br>}</pre><code>import</code> makes types from other <code>.proto</code> files available. The import path is relative to one of the <code>-I</code>/<code>--proto_path</code> directories passed to <code>protoc</code>.",
    ["protobuf", "import"])

c("Protobuf",
    "What is <code>google.protobuf.Timestamp</code> and how is it used?",
    "<pre>import \"google/protobuf/timestamp.proto\";<br>message LogEntry {<br>  google.protobuf.Timestamp created_at = 1;<br>}</pre>Represents a point in time with <b>nanosecond precision</b>. Contains:<br><pre>int64 seconds = 1;<br>int32 nanos   = 2;</pre>Serialized as a varint + int, compact and portable across languages.",
    ["protobuf", "well-known", "timestamp"])

c("Protobuf",
    "What is <code>google.protobuf.Duration</code>?",
    "<pre>import \"google/protobuf/duration.proto\";<br>message Timeout {<br>  google.protobuf.Duration max_wait = 1;<br>}</pre>Represents a time span (e.g., timeout, interval). Contains:<br><pre>int64 seconds = 1;<br>int32 nanos   = 2;</pre>Output format: <code>\"10.500s\"</code> = 10 seconds 500 milliseconds.",
    ["protobuf", "well-known", "duration"])

c("Protobuf",
    "What is <code>google.protobuf.Empty</code> and when to use it?",
    "<pre>import \"google/protobuf/empty.proto\";<br>rpc Ping (google.protobuf.Empty) returns (google.protobuf.Empty);</pre><code>Empty</code> is a message with <b>zero fields</b>. Use it when an RPC has no meaningful input or output (e.g., health checks, ping, shutdown). Serializes to <b>0 bytes</b> on the wire. Prefer this over defining your own empty message for consistency.",
    ["protobuf", "well-known", "empty"])

c("Protobuf",
    "What are <b>Wrapper types</b> (<code>Int32Value</code>, <code>StringValue</code>, etc.)?",
    "<pre>import \"google/protobuf/wrappers.proto\";<br>message User {<br>  google.protobuf.Int32Value  age      = 1; // nullable<br>  google.protobuf.StringValue nickname = 2; // nullable<br>  google.protobuf.BoolValue   active   = 3; // nullable<br>}</pre>Wrapper types wrap scalars in a message to support <b>nullability</b> (distinguish \"unset\" from \"zero\"). Available: <code>DoubleValue</code>, <code>FloatValue</code>, <code>Int64Value</code>, <code>UInt64Value</code>, <code>Int32Value</code>, <code>UInt32Value</code>, <code>BoolValue</code>, <code>StringValue</code>, <code>BytesValue</code>.",
    ["protobuf", "well-known", "wrappers"])

c("Protobuf",
    "What is <code>google.protobuf.Any</code>?",
    "<pre>import \"google/protobuf/any.proto\";<br>message Envelope {<br>  google.protobuf.Any payload = 1;<br>}</pre><code>Any</code> can hold <b>any protobuf message type</b>. It stores the serialized bytes + a type URL (<code>type.googleapis.com/package.MessageName</code>). The receiver must know which type to unpack. Use sparingly — akin to <code>interface{}</code> in Go or <code>Object</code> in Java.",
    ["protobuf", "well-known", "any"])

c("Protobuf",
    "What is <code>google.protobuf.Struct</code> and <code>Value</code>?",
    "<pre>import \"google/protobuf/struct.proto\";<br>message Metadata {<br>  google.protobuf.Struct attrs = 1; // dynamic JSON-like<br>}</pre><code>Struct</code> represents a JSON object with arbitrary keys/values. <code>Value</code> is a <code>oneof</code> of null, number, string, bool, struct, list. They map 1:1 to JSON. Use when you need <b>dynamic/schemaless</b> data in an otherwise strongly-typed protobuf message.",
    ["protobuf", "well-known", "struct"])

c("Protobuf",
    "What is <code>google.protobuf.FieldMask</code>?",
    "<pre>import \"google/protobuf/field_mask.proto\";<br>message UpdateRequest {<br>  User user = 1;<br>  google.protobuf.FieldMask update_mask = 2;<br>}</pre><code>FieldMask</code> lists the fields to include in a partial update. It contains a <code>repeated string paths</code> using field-path notation (<code>\"address.street\"</code>). The canonical way to do <b>field-level updates</b> in gRPC (like GraphQL partial mutations).",
    ["protobuf", "well-known", "fieldmask"])

c("Protobuf",
    "What are <code>option go_package</code> and <code>option java_package</code>?",
    "<pre>option go_package = \"github.com/me/proto/user/v1;userv1\";<br>option java_package = \"com.mycompany.proto.user.v1\";<br>option java_multiple_files = true;</pre>File-level options control <b>code generation</b> for specific languages. <code>go_package</code> sets the Go import path (and optional package alias after <code>;</code>). <code>java_package</code> sets the Java package. These coexist with <code>package</code> which provides the protobuf-level namespace.",
    ["protobuf", "options"])

c("Protobuf",
    "How does protobuf <b>varint encoding</b> work?",
    "Varint encoding uses a variable number of bytes (1-10) for integers. Each byte uses 7 bits for data, 1 bit as a continuation flag (MSB). Smaller numbers use fewer bytes: 0-127 → 1 byte, 128-16383 → 2 bytes.<br><br>Numbers 1-15 in field tags use 1 byte (compact). Negative int32 values encoded as varint use <b>10 bytes</b> (sign-extended to 64 bits) — that's why <code>sint32</code> with ZigZag encoding exists.",
    ["protobuf", "encoding", "varint"])

c("Protobuf",
    "What is the <b>ZigZag encoding</b> used by <code>sint32</code>/<code>sint64</code>?",
    "ZigZag maps signed integers to unsigned integers so that small negative numbers also use few bytes:<br>• 0 → 0, -1 → 1, 1 → 2, -2 → 3, 2 → 4, ...<br><br><pre>// protobuf wire encoding for sint32:<br>// uint32 = (int32 &lt;&lt; 1) ^ (int32 &gt;&gt; 31)<br>// uint64 = (int64 &lt;&lt; 1) ^ (int64 &gt;&gt; 63)</pre>Use <code>sint32</code>/<code>sint64</code> when values can be negative; avoids the 10-byte penalty of <code>int32</code>/<code>int64</code>.",
    ["protobuf", "encoding", "zigzag"])

c("Protobuf",
    "Why does <code>optional</code> matter for backward compatibility?",
    "In proto3 without <code>optional</code>, the zero value is indistinguishable from \"not set\" — you can't tell if <code>0</code> was intentionally set or defaulted. With <code>optional</code>, you get <b>field presence</b> tracking and can distinguish:<br>• <b>unset</b> — not included in wire format at all<br>• <b>set to zero</b> — included in wire format<br><br>This is critical when adding a new optional field — old clients that don't know the field won't accidentally override it with zero.",
    ["protobuf", "optional", "compatibility"])

# ── 03 SERVICE DEFINITIONS ────────────────────────────────────────

c("ServiceDef",
    "How do you declare a <code>service</code> in protobuf?",
    "<pre>service UserService {<br>  rpc GetUser    (GetUserRequest)    returns (GetUserResponse);<br>  rpc ListUsers  (ListUsersRequest)  returns (ListUsersResponse);<br>  rpc CreateUser (CreateUserRequest) returns (CreateUserResponse);<br>  rpc DeleteUser (DeleteUserRequest) returns (google.protobuf.Empty);<br>}</pre>A <code>service</code> is a collection of <b>RPC methods</b>. Each <code>rpc</code> declares one method with a request and response message type. The <code>service</code> block is the API contract that client and server both implement against.",
    ["service-def", "service"])

c("ServiceDef",
    "How do you define a <b>unary RPC</b>? Write the full <code>.proto</code>.",
    "<pre>service Calculator {<br>  rpc Add (AddRequest) returns (AddResponse);<br>}<br><br>message AddRequest {<br>  int32 a = 1;<br>  int32 b = 2;<br>}<br><br>message AddResponse {<br>  int32 result = 1;<br>}</pre>No <code>stream</code> keyword. One request in, one response out. Like a regular function call over the network.",
    ["service-def", "unary"])

c("ServiceDef",
    "How do you define a <b>server-streaming RPC</b>? Write the <code>.proto</code>.",
    "<pre>service LogWatcher {<br>  rpc TailLogs (TailRequest) returns (stream LogEntry);<br>}<br><br>message TailRequest {<br>  string log_file = 1;<br>}<br><br>message LogEntry {<br>  string line      = 1;<br>  int64  timestamp = 2;<br>}</pre>The <code>stream</code> keyword is on the <b>return type</b> only. Client sends one request, server sends many responses.",
    ["service-def", "server-streaming"])

c("ServiceDef",
    "How do you define a <b>client-streaming RPC</b>? Write the <code>.proto</code>.",
    "<pre>service FileUpload {<br>  rpc Upload (stream Chunk) returns (UploadResult);<br>}<br><br>message Chunk {<br>  bytes data     = 1;<br>  int64 offset   = 2;<br>}<br><br>message UploadResult {<br>  string file_id = 1;<br>  int64  size    = 2;<br>}</pre>The <code>stream</code> keyword is on the <b>request type</b> only. Client sends many messages, server sends one response.",
    ["service-def", "client-streaming"])

c("ServiceDef",
    "How do you define a <b>bidirectional-streaming RPC</b>? Write the <code>.proto</code>.",
    "<pre>service Chat {<br>  rpc ChatRoom (stream ChatMessage) returns (stream ChatMessage);<br>}<br><br>message ChatMessage {<br>  string user    = 1;<br>  string text    = 2;<br>  int64  sent_at = 3;<br>}</pre>The <code>stream</code> keyword is on <b>both</b> request and response. Both sides can send messages independently. Order is preserved per-direction but not across directions.",
    ["service-def", "bidi-streaming"])

c("ServiceDef",
    "What does the <code>stream</code> keyword placement determine?",
    "<b>No <code>stream</code>:</b> unary — single request, single response<br><b><code>stream</code> on return only:</b> server-streaming — one request, many responses<br><b><code>stream</code> on request only:</b> client-streaming — many requests, one response<br><b><code>stream</code> on both:</b> bidirectional — many requests, many responses<br><br>The keyword is placed before the message type in the RPC definition.",
    ["service-def", "stream-keyword"])

c("ServiceDef",
    "How does a <b>server implementation</b> work? Show a Go example.",
    "<pre>type UserServer struct {<br>  userpb.UnimplementedUserServiceServer<br>}<br><br>func (s *UserServer) GetUser(ctx context.Context, req *userpb.GetUserRequest) (*userpb.GetUserResponse, error) {<br>  // Fetch user from DB using req.UserId<br>  user, err := db.Find(req.UserId)<br>  if err != nil {<br>    return nil, status.Error(codes.NotFound, \"user not found\")<br>  }<br>  return &userpb.GetUserResponse{Name: user.Name, Age: user.Age}, nil<br>}<br><br>func main() {<br>  lis, _ := net.Listen(\"tcp\", \":50051\")<br>  s := grpc.NewServer()<br>  userpb.RegisterUserServiceServer(s, &UserServer{})<br>  s.Serve(lis)<br>}</pre>Implement the generated server interface, register with a <code>grpc.Server</code>, and <code>Serve</code> on a port.",
    ["service-def", "server-impl"])

c("ServiceDef",
    "How do you create a <b>gRPC client</b>? Show a Go example.",
    "<pre>conn, err := grpc.Dial(\"localhost:50051\",<br>  grpc.WithTransportCredentials(insecure.NewCredentials()),<br>)<br>if err != nil {<br>  log.Fatalf(\"did not connect: %v\", err)<br>}<br>defer conn.Close()<br><br>client := userpb.NewUserServiceClient(conn)<br><br>resp, err := client.GetUser(ctx, &userpb.GetUserRequest{UserId: \"123\"})<br>if err != nil {<br>  log.Fatalf(\"could not get user: %v\", err)<br>}<br>log.Printf(\"User: %s, Age: %d\", resp.Name, resp.Age)</pre>Dial the server, create a client stub from the generated code, call RPC methods like local functions.",
    ["service-def", "client-impl"])

c("ServiceDef",
    "List all 17 gRPC status codes with their numeric values and meanings.",
    "<table><tr><td><b>Code</b></td><td><b>#</b></td><td><b>Meaning</b></td></tr><tr><td><code>OK</code></td><td>0</td><td>Success</td></tr><tr><td><code>CANCELLED</code></td><td>1</td><td>Caller cancelled the operation</td></tr><tr><td><code>UNKNOWN</code></td><td>2</td><td>Unknown/catch-all error</td></tr><tr><td><code>INVALID_ARGUMENT</code></td><td>3</td><td>Bad request input</td></tr><tr><td><code>DEADLINE_EXCEEDED</code></td><td>4</td><td>Timeout</td></tr><tr><td><code>NOT_FOUND</code></td><td>5</td><td>Resource not found</td></tr><tr><td><code>ALREADY_EXISTS</code></td><td>6</td><td>Resource already exists</td></tr><tr><td><code>PERMISSION_DENIED</code></td><td>7</td><td>No permission</td></tr><tr><td><code>RESOURCE_EXHAUSTED</code></td><td>8</td><td>Quota depleted / rate limit</td></tr><tr><td><code>FAILED_PRECONDITION</code></td><td>9</td><td>System not in right state</td></tr><tr><td><code>ABORTED</code></td><td>10</td><td>Concurrency conflict (retryable)</td></tr><tr><td><code>OUT_OF_RANGE</code></td><td>11</td><td>Value out of valid range</td></tr><tr><td><code>UNIMPLEMENTED</code></td><td>12</td><td>Method not implemented</td></tr><tr><td><code>INTERNAL</code></td><td>13</td><td>Internal server error</td></tr><tr><td><code>UNAVAILABLE</code></td><td>14</td><td>Service unavailable (retryable)</td></tr><tr><td><code>DATA_LOSS</code></td><td>15</td><td>Unrecoverable data loss</td></tr><tr><td><code>UNAUTHENTICATED</code></td><td>16</td><td>Missing/expired credentials</td></tr></table>",
    ["service-def", "status-codes"])

c("ServiceDef",
    "Which gRPC status codes are safe to <b>retry</b>?",
    "<b>Retryable:</b><br>• <code>CANCELLED</code> (1) — if not the client's own cancellation<br>• <code>ABORTED</code> (10) — optimistic lock failure<br>• <code>UNAVAILABLE</code> (14) — transient server outage<br>• <code>DEADLINE_EXCEEDED</code> (4) — if idempotent<br><br><b>NOT retryable:</b><br>• <code>INVALID_ARGUMENT</code> (3), <code>NOT_FOUND</code> (5), <code>ALREADY_EXISTS</code> (6), <code>PERMISSION_DENIED</code> (7), <code>UNIMPLEMENTED</code> (12), <code>UNAUTHENTICATED</code> (16) — retrying won't help; same input = same error.",
    ["service-def", "status-codes", "retry"])

c("ServiceDef",
    "How do you return a gRPC error with details from a server? (Go example)",
    "<pre>import \"google.golang.org/genproto/googleapis/rpc/errdetails\"<br>import \"google.golang.org/grpc/status\"<br>import \"google.golang.org/grpc/codes\"<br><br>st := status.New(codes.InvalidArgument, \"invalid email format\")<br>detail := &errdetails.BadRequest_FieldViolation{<br>  Field:       \"email\",<br>  Description: \"must contain '@'\",<br>}<br>st, _ = st.WithDetails(&errdetails.BadRequest{<br>  FieldViolations: []*errdetails.BadRequest_FieldViolation{detail},<br>})<br>return st.Err()</pre>Use <code>status.New()</code> + <code>.WithDetails()</code> to attach structured error information. Clients decode with <code>status.FromError(err)</code>.",
    ["service-def", "error-details"])

c("ServiceDef",
    "How do you use <b>metadata</b> (headers/trailers) in gRPC?",
    "Metadata is key-value pairs sent in HTTP/2 headers (initial) and trailers (final).<br><br><b>Client sending metadata:</b><br><pre>md := metadata.Pairs(\"auth-token\", \"xyz\", \"request-id\", \"42\")<br>ctx := metadata.NewOutgoingContext(ctx, md)<br>resp, err := client.GetUser(ctx, req)</pre><b>Server reading metadata:</b><br><pre>md, ok := metadata.FromIncomingContext(ctx)<br>token := md.Get(\"auth-token\")</pre><b>Server sending trailers:</b><br><pre>header := metadata.Pairs(\"x-custom\", \"value\")<br>grpc.SetHeader(ctx, header) // headers (before response)<br>grpc.SetTrailer(ctx, md)    // trailers (after response)</pre>Keys are <b>lowercase</b> by convention; gRPC normalizes them.",
    ["service-def", "metadata"])

c("ServiceDef",
    "How do <b>deadlines/timeouts</b> work in gRPC?",
    "Set a deadline on the client context:<br><pre>ctx, cancel := context.WithTimeout(ctx, 5*time.Second)<br>defer cancel()<br>resp, err := client.GetUser(ctx, &pb.GetUserRequest{Id: \"42\"})</pre>If the deadline expires, gRPC returns <code>DEADLINE_EXCEEDED</code>. Deadlines <b>propagate</b> — the server sees the remaining deadline in <code>ctx</code> and can stop work early.<br><br><b>Best practice:</b> Always set deadlines! Without one, a hanging server can block a client indefinitely.",
    ["service-def", "deadlines"])

c("ServiceDef",
    "What is <b>cancellation</b> in gRPC?",
    "When a client cancels a context:<br><pre>ctx, cancel := context.WithCancel(ctx)<br>go func() { cancel() }() // some goroutine cancels<br>resp, err := client.StreamCall(ctx)</pre>The RPC receives <code>CANCELLED</code>. The server's <code>ctx.Done()</code> channel closes. Both sides stop processing. Cancellation is propagated over HTTP/2 RST_STREAM frames. Different from deadline — cancellation is <b>explicit</b> rather than time-based.",
    ["service-def", "cancellation"])

c("ServiceDef",
    "How does gRPC <b>connection</b> vs <b>channel</b> differ?",
    "In gRPC:<br>• A <b>connection</b> is a single TCP connection (with HTTP/2 multiplexing).<br>• A <b>channel</b> is a virtual abstraction over 0+ connections, with load balancing and name resolution.<br><br><pre>conn, _ := grpc.Dial(\"svc:50051\", ...) // returns a *ClientConn<br>// Channel = ClientConn. It manages sub-connections.<br>client := pb.NewUserClient(conn)</pre>The channel may open multiple TCP connections for load balancing. Connections are transparently reconnected on failure.",
    ["service-def", "connection-vs-channel"])

# ── 04 STREAMING ─────────────────────────────────────────────────

c("Streaming",
    "How do you implement a <b>server-streaming</b> RPC handler? (Go example)",
    "<pre>func (s *LogServer) TailLogs(req *pb.TailRequest, stream pb.LogService_TailLogsServer) error {<br>  file, _ := os.Open(req.LogFile)<br>  scanner := bufio.NewScanner(file)<br>  for scanner.Scan() {<br>    entry := &pb.LogEntry{Line: scanner.Text()}<br>    if err := stream.Send(entry); err != nil {<br>      return err<br>    }<br>  }<br>  return nil<br>}</pre>Call <code>stream.Send()</code> repeatedly. The server writes to the stream until done (<code>return nil</code>). The client reads with <code>stream.Recv()</code> until <code>io.EOF</code>.",
    ["streaming", "server-side"])

c("Streaming",
    "How do you implement a <b>client-streaming</b> RPC handler? (Go example)",
    "<pre>func (s *UploadServer) Upload(stream pb.UploadService_UploadServer) error {<br>  var total int64<br>  for {<br>    chunk, err := stream.Recv()<br>    if err == io.EOF {<br>      // All chunks received, send response<br>      return stream.SendAndClose(&pb.UploadResult{<br>        Size: total,<br>      })<br>    }<br>    if err != nil { return err }<br>    total += int64(len(chunk.Data))<br>  }<br>}</pre>Call <code>stream.Recv()</code> in a loop. When <code>io.EOF</code> arrives, all client messages are done. <code>SendAndClose()</code> sends the single response and closes the server side.",
    ["streaming", "client-side"])

c("Streaming",
    "How do you implement a <b>bidirectional streaming</b> RPC handler? (Go example)",
    "<pre>func (s *ChatServer) ChatRoom(stream pb.ChatService_ChatRoomServer) error {<br>  for {<br>    msg, err := stream.Recv()<br>    if err == io.EOF { return nil }<br>    if err != nil { return err }<br>    log.Printf(\"%s: %s\", msg.User, msg.Text)<br>    // Echo back to everyone (simplified)<br>    if err := stream.Send(msg); err != nil { return err }<br>  }<br>}</pre>Both <code>Send()</code> and <code>Recv()</code> are available. They can be used in any order, even concurrently from separate goroutines. Each direction is independent. The server <code>return nil</code> when done.",
    ["streaming", "bidi"])

c("Streaming",
    "How does a <b>client</b> call a bidirectional streaming RPC? (Go example)",
    "<pre>stream, err := client.ChatRoom(ctx)<br><br>// Send goroutine<br>go func() {<br>  for _, msg := range messages {<br>    stream.Send(msg)<br>  }<br>  stream.CloseSend() // signal no more sends<br>}()<br><br>// Receive loop<br>for {<br>  msg, err := stream.Recv()<br>  if err == io.EOF { break }<br>  if err != nil { log.Fatal(err) }<br>  fmt.Println(msg)<br>}</pre>The client calls <code>CloseSend()</code> to signal it's done sending (half-close). It can still receive until <code>io.EOF</code>. Separating send/recv into goroutines is the common pattern.",
    ["streaming", "bidi-client"])

c("Streaming",
    "What is <b>flow control</b> in gRPC streaming?",
    "HTTP/2 provides <b>per-stream flow control</b>. A sender can buffer up to the receiver's advertised window size. If the receiver is slow, the sender blocks on <code>Send()</code> until the window opens.<br><br>• Protects against buffer bloat<br>• Automatic — no application-level config required<br>• Can cause head-of-line blocking if not careful<br>• Use <code>grpc.MaxConcurrentStreams</code> to limit concurrent streams<br><br>If you need to drop messages under backpressure, implement your own buffer with <code>select</code> + <code>ctx.Done()</code>.",
    ["streaming", "flow-control"])

c("Streaming",
    "How do you handle <b>errors in a stream</b>?",
    "<pre>// Server: return an error to terminate the stream<br>if strings.TrimSpace(msg.Text) == \"\" {<br>  return status.Errorf(codes.InvalidArgument, \"text cannot be empty\")<br>}<br><br>// Client: errors from Recv() or Send() terminate the stream<br>msg, err := stream.Recv()<br>if err != nil {<br>  st := status.Convert(err)<br>  log.Printf(\"code=%v msg=%s\", st.Code(), st.Message())<br>  return<br>}</pre>Errors on either side terminate the stream. The peer gets a status error on their next <code>Recv()</code>/<code>Send()</code>. <code>io.EOF</code> from <code>Recv()</code> is not an error — it indicates normal stream completion.",
    ["streaming", "errors"])

c("Streaming",
    "What are the <b>gRPC rich error details</b> types? (from <code>google.rpc</code>)",
    "<b><code>google.rpc.ErrorInfo</code></b> — machine-readable reason + domain + metadata<br><b><code>google.rpc.BadRequest</code></b> — per-field validation violations<br><b><code>google.rpc.PreconditionFailure</code></b> — list of failed preconditions<br><b><code>google.rpc.ResourceInfo</code></b> — which resource caused the error<br><b><code>google.rpc.QuotaFailure</code></b> — which quota was exceeded<br><b><code>google.rpc.RetryInfo</code></b> — suggested retry delay<br><b><code>google.rpc.DebugInfo</code></b> — stack traces (strip in production!)<br><b><code>google.rpc.Help</code></b> — link to documentation<br><b><code>google.rpc.LocalizedMessage</code></b> — human-readable with locale<br><b><code>google.rpc.RequestInfo</code></b> — request ID for support<br><br>Use these inside <code>Status.WithDetails()</code> to give clients structured error data.",
    ["streaming", "rich-errors"])

c("Streaming",
    "What is the <b>gRPC Reflection API</b>?",
    "Reflection allows clients to <b>discover the service definition at runtime</b> without a pre-compiled <code>.proto</code>.<br><br><b>Enable on server (Go):</b><br><pre>import \"google.golang.org/grpc/reflection\"<br>reflection.Register(s) // s is *grpc.Server</pre><b>Client side:</b> tools like <code>grpcurl</code> and <code>grpcui</code> use reflection to list services/methods and construct requests dynamically. Great for debugging. <b>Disable in production</b> — it exposes your API surface to anyone who can reach the server.",
    ["streaming", "reflection"])

c("Streaming",
    "How does <b>deadline propagation</b> work across gRPC services?",
    "When service A calls service B, it passes the same context:<br><pre>// Service A handler<br>func (s *SvcA) Handle(ctx context.Context, req *pb.Req) (*pb.Resp, error) {<br>  // ctx contains the deadline from the original client<br>  return clientB.Call(ctx, &pb.InnerReq{})<br>}</pre>If the original deadline was 5s and service A took 2s, service B has 3s remaining. The deadline is encoded in <code>grpc-timeout</code> header and decremented at each hop. This prevents cascading timeouts — one deep service timing out won't leave upstream services hanging.",
    ["streaming", "deadline-propagation"])

c("Streaming",
    "How do you extract <b>rich error details</b> on the gRPC client side? (Go example)",
    "<pre>resp, err := client.Call(ctx, req)<br>if err != nil {<br>  st := status.Convert(err) // get code + message<br>  for _, detail := range st.Details() {<br>    switch t := detail.(type) {<br>    case *errdetails.BadRequest:<br>      for _, v := range t.FieldViolations {<br>        log.Printf(\"field=%s: %s\", v.Field, v.Description)<br>      }<br>    case *errdetails.ErrorInfo:<br>      log.Printf(\"error domain=%s reason=%s\", t.Domain, t.Reason)<br>    case *errdetails.RetryInfo:<br>      delay := t.RetryDelay.AsDuration()<br>      log.Printf(\"retry after %v\", delay)<br>    }<br>  }<br>}</pre><code>status.Convert(err)</code> + <code>.Details()</code> returns <code>[]interface{}</code>. Type-switch to access specific detail types. Rich errors let clients handle failures programmatically.",
    ["streaming", "client-error-details"])

c("Streaming",
    "What is the difference between <b>per-RPC call options</b> and <b>dial options</b> in gRPC?",
    "<b>Dial options</b> (set at <code>grpc.Dial()</code>):<br>• Apply to <b>all RPCs</b> on that connection/channel<br>• Examples: TLS credentials, interceptors, keepalive, resolver, default service config<br>• Set once, reused for lifetime of the <code>*grpc.ClientConn</code><br><br><b>Call options</b> (passed per RPC call):<br>• Apply to a <b>single RPC</b><br>• Override dial options for that call<br>• Examples: call timeout, compressor, max message sizes, custom metadata<br><br><pre>// Dial-level<br>conn, _ := grpc.Dial(\"svc:50051\", grpc.WithInsecure())<br><br>// Per-call override<br>ctx, cancel := context.WithTimeout(ctx, 100*time.Millisecond)<br>resp, _ := client.Call(ctx, req,<br>  grpc.UseCompressor(gzip.Name),<br>  grpc.MaxCallRecvMsgSize(50*1024*1024),<br>)</pre>Dial options set infrastructure; call options set per-request behavior.",
    ["streaming", "dial-vs-call-options"])

# ── 05 ECOSYSTEM & TOOLING ───────────────────────────────────────

c("Ecosystem",
    "What is <code>protoc</code> and what does it do?",
    "<code>protoc</code> is the <b>official Protobuf compiler</b>. It reads <code>.proto</code> files and outputs code in your target language via <b>plugins</b>.<br><br><pre>protoc --go_out=. --go_opt=paths=source_relative \\<br>       --go-grpc_out=. --go-grpc_opt=paths=source_relative \\<br>       -I. proto/**.proto</pre><code>protoc</code> itself handles parsing and validation. Language-specific plugins (<code>--go_out</code>, <code>--python_out</code>, etc.) generate the actual code. <code>-I</code> flags set the import search paths.",
    ["ecosystem", "protoc"])

c("Ecosystem",
    "What is <b>Buf</b> and why should you use it instead of raw <code>protoc</code>?",
    "<b>Buf</b> is a modern replacement for <code>protoc</code>-based workflows:<br>• <b>buf lint</b> — enforce API design rules (no raw protoc equivalent)<br>• <b>buf format</b> — auto-format <code>.proto</code> files<br>• <b>buf breaking</b> — detect backward-incompatible changes<br>• <b>buf generate</b> — run code generation (faster, file-watching)<br>• <b>buf build</b> — compile to a <code>FileDescriptorSet</code> image<br>• <b>buf push</b> — push to BSR (Buf Schema Registry)<br><br>Single <code>buf.yaml</code> config replaces complex <code>protoc</code> shell scripts. <code>buf.gen.yaml</code> declares plugins and options declaratively.",
    ["ecosystem", "buf"])

c("Ecosystem",
    "What does <code>buf lint</code> do? Show example output.",
    "<pre>$ buf lint<br>proto/api/v1/user.proto:10:1:RPC \"GetUser\" has no comment<br>proto/api/v1/user.proto:15:3:Field name \"user_id\" should be lower_snake_case<br>proto/api/v1/user.proto:1:1:Files with package \"api.v1\" must have version suffix</pre>Buf lint enforces rules from categories: <code>STANDARD</code>, <code>MINIMAL</code>, <code>COMMENTS</code>, <code>UNARY_RPC</code>, or custom. Configure in <code>buf.yaml</code>:<br><pre>lint:<br>  use:<br>    - STANDARD<br>  except:<br>    - FIELD_LOWER_SNAKE_CASE</pre>",
    ["ecosystem", "buf-lint"])

c("Ecosystem",
    "What does <code>buf breaking</code> detect?",
    "<pre>$ buf breaking --against 'https://github.com/foo/api.git'</pre>Detects backward-incompatible changes between revisions:<br>• Removing or renaming a field/method<br>• Changing a field number or type<br>• Changing a method signature<br>• Removing a service or enum value<br>• Changing streaming/non-streaming RPC type<br><br>Runs in CI to prevent breaking API changes. Can compare against git history, BSR, or local file descriptor sets.",
    ["ecosystem", "buf-breaking"])

c("Ecosystem",
    "What is the <b>Buf Schema Registry (BSR)</b>?",
    "BSR is a <b>hosted registry for <code>.proto</code> files</b>, like npm for JavaScript or Maven for Java. Features:<br>• <b>Store</b> protobuf schema versions<br>• <b>Generate</b> code (managed mode — BSR runs <code>buf generate</code> in the cloud)<br>• <b>Documentation</b> — auto-generated docs with method cards<br>• <b>Dependency management</b> — <code>buf mod update</code><br>• <b>Remote plugins</b> — use community plugins without local install<br><pre>buf push                # push schema<br>buf generate buf.build/MyOrg/MyProto # remote gen</pre>",
    ["ecosystem", "bsr"])

c("Ecosystem",
    "List the major <code>protoc</code> plugin ecosystems by language.",
    "<b>Go:</b> <code>protoc-gen-go</code> (messages), <code>protoc-gen-go-grpc</code> (services)<br><b>Java:</b> <code>protoc-gen-java</code>, <code>protoc-gen-grpc-java</code><br><b>Python:</b> <code>protoc-gen-python</code> (built-in), <code>grpcio-tools</code><br><b>JavaScript/TypeScript:</b> <code>protoc-gen-js</code>, <code>protoc-gen-grpc-web</code>, <code>protoc-gen-ts</code> (via <code>ts-proto</code> or <code>@bufbuild/protobuf</code>)<br><b>C++:</b> <code>protoc-gen-cpp</code>, <code>protoc-gen-grpc-cpp</code><br><b>C#:</b> <code>protoc-gen-csharp</code>, <code>Grpc.Tools</code><br><b>Rust:</b> <code>prost</code> / <code>tonic</code><br><b>Dart:</b> <code>protoc-gen-dart</code><br><b>Kotlin:</b> <code>protoc-gen-grpc-kotlin</code>",
    ["ecosystem", "plugins"])

c("Ecosystem",
    "What is <code>grpcurl</code> and how do you use it?",
    "<code>grpcurl</code> is a CLI tool like <code>curl</code> but for gRPC. It can list services/methods and send requests.<br><br><pre># List services (requires reflection)<br>grpcurl -plaintext localhost:50051 list<br><br># List methods<br>grpcurl -plaintext localhost:50051 list myapp.UserService<br><br># Call a method<br>grpcurl -plaintext -d '{\"user_id\": \"123\"}' \\<br>  localhost:50051 myapp.UserService/GetUser<br><br># With protoset (no reflection)<br>grpcurl -protoset myapp.protoset \\<br>  -plaintext localhost:50051 myapp.UserService/GetUser</pre>Essential for debugging. No pre-compiled client needed — just the server address.",
    ["ecosystem", "grpcurl"])

c("Ecosystem",
    "What is <code>grpcui</code>?",
    "<code>grpcui</code> generates a <b>web UI</b> for interacting with gRPC servers — like Postman for gRPC.<br><br><pre>grpcui -plaintext localhost:50051</pre>Opens a browser with:<br>• Method list with request/response explorers<br>• Form-based input fields (auto-generated from proto)<br>• Streaming support<br>• Request history<br><br>Uses the reflection API or a protoset file. Great for manual testing and demos.",
    ["ecosystem", "grpcui"])

c("Ecosystem",
    "What is <b>gRPC-gateway</b> (grpc-gateway)?",
    "<b>gRPC-gateway</b> generates a <b>reverse proxy</b> that translates REST/JSON HTTP calls to gRPC. Write one <code>.proto</code> with <code>google.api.http</code> annotations, and it generates both a gRPC server stub and a REST gateway.<br><br><pre>rpc GetUser (GetUserRequest) returns (GetUserResponse) {<br>  option (google.api.http) = {<br>    get: \"/v1/users/{user_id}\"<br>  };<br>}</pre>Single source of truth — gRPC for internal services, REST for external consumers. The gateway just proxies JSON ↔ Protobuf.",
    ["ecosystem", "grpc-gateway"])

c("Ecosystem",
    "What is <b>gRPC-Web</b> and what are its limitations?",
    "gRPC-Web enables <b>browser clients</b> to call gRPC services via HTTP/1.1 or HTTP/2 (with a proxy).<br><br><b>Supported in browsers:</b><br>• Unary RPCs ✓<br>• Server-streaming RPCs ✓<br><br><b>NOT supported in browsers:</b><br>• Client-streaming RPCs ✗<br>• Bidirectional-streaming RPCs ✗<br><br>Works by wrapping the gRPC wire format in a body that browsers can send (<code>application/grpc-web</code> content type). Requires a proxy (Envoy, gRPC-gateway, or custom) between browser and gRPC server. For full-duplex in browsers, use WebSockets or the Connect protocol.",
    ["ecosystem", "grpc-web"])

c("Ecosystem",
    "How does <b>Envoy proxy</b> integrate with gRPC?",
    "Envoy has native gRPC support:<br>• <b>gRPC bridge</b> — translates gRPC-Web to gRPC<br>• <b>gRPC-JSON transcoding</b> — REST/JSON ↔ gRPC<br>• <b>gRPC health checks</b> — discovers healthy/terminating backends<br>• <b>xDS integration</b> — dynamic configuration for routing/load balancing<br>• <b>gRPC access logging</b> — log every RPC with metadata<br><br>Envoy is the default sidecar in Istio/Consul service meshes and is often deployed between gRPC clients and servers for observability and traffic management.",
    ["ecosystem", "envoy"])

c("Ecosystem",
    "What is the <b>gRPC health checking protocol</b>?",
    "A standard health service defined by gRPC:<br><pre>service Health {<br>  rpc Check (HealthCheckRequest) returns (HealthCheckResponse);<br>  rpc Watch (HealthCheckRequest) returns (stream HealthCheckResponse);<br>}<br>message HealthCheckRequest { string service = 1; }<br>message HealthCheckResponse {<br>  enum ServingStatus {<br>    UNKNOWN = 0; SERVING = 1; NOT_SERVING = 2;<br>    SERVICE_UNKNOWN = 3; // per-service unknown<br>  }<br>  ServingStatus status = 1;<br>}</pre>Implement this on your server. <code>Check</code> is unary (one-shot), <code>Watch</code> is server-streaming (status changes). Load balancers (Envoy, gRPC-LB) use this to route traffic.",
    ["ecosystem", "health-check"])

c("Ecosystem",
    "How do you configure <b>buf generate</b> with plugins? Show <code>buf.gen.yaml</code>.",
    "<pre>version: v2<br>managed:<br>  enabled: true<br>  override:<br>    - file_option: go_package_prefix<br>      value: github.com/me/myproject/gen<br>plugins:<br>  - remote: buf.build/protocolbuffers/go<br>    out: gen/go<br>    opt: paths=source_relative<br>  - remote: buf.build/grpc/go<br>    out: gen/go<br>    opt: paths=source_relative<br>  - local: protoc-gen-es<br>    out: gen/es</pre><code>managed</code> mode auto-sets <code>go_package</code>/<code>java_package</code> etc. <code>plugins</code> lists code generators (remote BSR plugins or local). <code>out</code> is the output directory.",
    ["ecosystem", "buf-generate"])

c("Ecosystem",
    "What is a <b>buf.yaml</b> workspace and module?",
    "<pre># buf.yaml<br>version: v2<br>modules:<br>  - path: proto/user<br>    name: buf.build/myorg/user<br>  - path: proto/common<br>    name: buf.build/myorg/common<br><br>lint:<br>  use:<br>    - STANDARD<br><br>breaking:<br>  use:<br>    - FILE</pre>A <b>module</b> is a directory with <code>.proto</code> files (optionally named/pushed to BSR). A <b>workspace</b> allows multiple modules within a single repo to <b>reference each other locally</b> while being pushed independently. This replaces complex <code>--proto_path</code> setups with declarative config.",
    ["ecosystem", "buf-workspace"])

# ── 06 ADVANCED PATTERNS ─────────────────────────────────────────

c("Patterns",
    "What are <b>interceptors</b> in gRPC?",
    "Interceptors are <b>middleware</b> for gRPC. They intercept RPCs on client or server side, before/after the actual handler.<br><br><b>Types:</b><br>• <b>Unary server interceptor</b> — wraps handler execution<br>• <b>Stream server interceptor</b> — wraps stream handler<br>• <b>Unary client interceptor</b> — wraps client call<br>• <b>Stream client interceptor</b> — wraps client stream<br><br>Common uses: logging, auth, metrics, tracing, rate limiting, panic recovery, request validation.",
    ["patterns", "interceptors"])

c("Patterns",
    "Write a simple unary server interceptor in Go that logs request duration.",
    "<pre>func loggingInterceptor(ctx context.Context, req interface{},<br>  info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {<br>  start := time.Now()<br>  resp, err := handler(ctx, req)<br>  log.Printf(\"method=%s duration=%v err=%v\", info.FullMethod, time.Since(start), err)<br>  return resp, err<br>}<br><br>s := grpc.NewServer(<br>  grpc.UnaryInterceptor(loggingInterceptor),<br>)</pre>The <code>handler(ctx, req)</code> call forwards to the next interceptor or the actual implementation. Chain multiple interceptors with <code>grpc_middleware</code>.",
    ["patterns", "interceptor-logging"])

c("Patterns",
    "How do you implement <b>authentication</b> in gRPC?",
    "Use a unary server interceptor:<br><pre>func authInterceptor(ctx context.Context, req interface{},<br>  info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {<br>  md, ok := metadata.FromIncomingContext(ctx)<br>  if !ok { return nil, status.Error(codes.Unauthenticated, \"missing metadata\") }<br>  tokens := md.Get(\"authorization\")<br>  if len(tokens) == 0 {<br>    return nil, status.Error(codes.Unauthenticated, \"missing token\")<br>  }<br>  claims, err := validateJWT(tokens[0])<br>  if err != nil { return nil, status.Error(codes.Unauthenticated, err.Error()) }<br>  newCtx := context.WithValue(ctx, \"user\", claims)<br>  return handler(newCtx, req)<br>}</pre>Extract token from metadata → validate → inject claims into context → call handler. Works with JWT, OAuth2, mTLS, or API keys.",
    ["patterns", "interceptor-auth"])

c("Patterns",
    "How do you implement <b>rate limiting</b> as a gRPC interceptor?",
    "<pre>func rateLimitInterceptor(limiter *rate.Limiter) grpc.UnaryServerInterceptor {<br>  return func(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo,<br>    handler grpc.UnaryHandler) (interface{}, error) {<br>    if !limiter.Allow() {<br>      return nil, status.Error(codes.ResourceExhausted, \"rate limit exceeded\")<br>    }<br>    return handler(ctx, req)<br>  }<br>}<br><br>s := grpc.NewServer(<br>  grpc.UnaryInterceptor(rateLimitInterceptor(rate.NewLimiter(100, 10))),<br>)</pre>Return <code>RESOURCE_EXHAUSTED</code> when the limit is hit. For distributed rate limiting, use Redis or a token bucket service. For per-user limits, extract user identity from metadata first.",
    ["patterns", "rate-limiting"])

c("Patterns",
    "How do you configure <b>retry logic</b> in gRPC clients?",
    "Use <b>service config</b> (JSON sent by client at connection time or by the resolver):<br><pre>{<br>  \"methodConfig\": [{<br>    \"name\": [{\"service\": \"myapp.UserService\"}],<br>    \"retryPolicy\": {<br>      \"maxAttempts\": 5,<br>      \"initialBackoff\": \"0.1s\",<br>      \"maxBackoff\": \"10s\",<br>      \"backoffMultiplier\": 2,<br>      \"retryableStatusCodes\": [\"UNAVAILABLE\"]<br>    }<br>  }]<br>}</pre>Built into gRPC core. The client transparently retries on specified status codes. For server-streaming, only retry if the server hasn't sent any messages yet.",
    ["patterns", "retry"])

c("Patterns",
    "What is <b>hedging</b> in gRPC?",
    "Hedging sends the same request to <b>multiple backends simultaneously</b> and uses whichever responds first (cancelling the rest).<br><br><pre>{<br>  \"methodConfig\": [{<br>    \"name\": [{\"service\": \"myapp.SearchService\"}],<br>    \"hedgingPolicy\": {<br>      \"maxAttempts\": 5,<br>      \"hedgingDelay\": \"0.5s\",<br>      \"nonFatalStatusCodes\": [\"UNAVAILABLE\", \"INTERNAL\"]<br>    }<br>  }]<br>}</pre>Send first request → wait 500ms → if no response, send second → repeat. Different from retry — hedging is <b>speculative parallelism</b> for latency reduction, not error recovery.",
    ["patterns", "hedging"])

c("Patterns",
    "List the gRPC <b>client-side load balancing</b> policies.",
    "<b><code>pick_first</code></b> — connect to the first address that works. Simple, no balancing.<br><b><code>round_robin</code></b> — distribute RPCs across all available backends in rotation.<br><b><code>ring_hash</code></b> — consistently hash a request attribute (header) to a backend. Good for sticky sessions or cache affinity.<br><b><code>outlier_detection</code></b> — eject unhealthy backends based on error rate/latency. Wraps another policy (commonly <code>round_robin</code>).<br><b><code>grpclb</code></b> — legacy, uses external load balancer.<br><b><code>xds</code></b> — Envoy's discovery service for dynamic config.<br><br>Configured via service config JSON, DNS SRV records, or xDS.",
    ["patterns", "load-balancing"])

c("Patterns",
    "How does gRPC <b>connection backoff</b> work?",
    "When a gRPC client can't connect, it retries with exponential backoff:<br><br>1. Initial reconnect after ~1 second<br>2. Each subsequent attempt doubles the backoff (up to ~120s max)<br>3. Jitter is added to avoid thundering herd<br>4. On disconnect, a channel enters <code>TRANSIENT_FAILURE</code> state<br>5. RPCs fail-fast with <code>UNAVAILABLE</code> during this state<br><br>Customizable via <code>grpc.WithConnectParams()</code>:<br><pre>grpc.WithConnectParams(grpc.ConnectParams{<br>  Backoff:           backoff.Config{BaseDelay: 1*time.Second, MaxDelay: 30*time.Second, Multiplier: 1.6},<br>  MinConnectTimeout: 5*time.Second,<br>})</pre>",
    ["patterns", "backoff"])

c("Patterns",
    "What are <b>keepalive</b> settings in gRPC?",
    "<b>Client-side keepalive:</b> sends pings when idle to detect dead connections.<br><pre>grpc.WithKeepaliveParams(keepalive.ClientParameters{<br>  Time:                10 * time.Second, // send ping every 10s if idle<br>  Timeout:             3 * time.Second,  // wait 3s for ping ack<br>  PermitWithoutStream: true,             // ping even without active RPCs<br>})</pre><b>Server-side enforcement:</b><br><pre>grpc.KeepaliveEnforcementPolicy(<br>  keepalive.EnforcementPolicy{<br>    MinTime:             5 * time.Second, // min interval client can ping<br>    PermitWithoutStream: true,<br>  },<br>)<br>grpc.KeepaliveParams(keepalive.ServerParameters{<br>  MaxConnectionIdle:     15 * time.Minute, // close if idle<br>  MaxConnectionAge:      30 * time.Minute, // close after age<br>  MaxConnectionAgeGrace: 5 * time.Second,  // grace period before force close<br>  Time:                  2 * time.Minute,  // server ping interval<br>  Timeout:               20 * time.Second, // wait for ping ack<br>})</pre>Keepalives help detect dead connections that TCP won't notice (e.g., firewall drops). But too-aggressive pings waste resources.",
    ["patterns", "keepalive"])

c("Patterns",
    "What is <b>name resolution</b> in gRPC?",
    "Name resolution translates a target string (<code>\"dns:///myservice:50051\"</code>) into a list of backend addresses.<br><br><b>Built-in resolvers:</b><br>• <code>dns</code> — resolves DNS A/AAAA and SRV records<br>• <code>passthrough</code> — uses the address as-is (default)<br>• <code>unix</code> — Unix domain sockets<br><br><b>Custom resolvers:</b><br><pre>resolver.Register(&myResolverBuilder{})<br>conn, _ := grpc.Dial(\"myresolver:///service-name\")</pre>The resolved address list is continuously watched — if DNS or a service registry (Consul, ZooKeeper, etc.) changes, gRPC updates its sub-connections transparently.",
    ["patterns", "name-resolution"])

c("Patterns",
    "What is <b>xDS</b> in gRPC?",
    "<b>xDS</b> (x Discovery Service) is Envoy's control-plane protocol. gRPC can act as an xDS client to get dynamic configuration from a control plane (Istio, Consul Connect, custom).<br><br>Configures dynamically:<br>• <b>LDS</b> (Listener Discovery) — what ports to listen on<br>• <b>RDS</b> (Route Discovery) — routing rules<br>• <b>CDS</b> (Cluster Discovery) — backend clusters<br>• <b>EDS</b> (Endpoint Discovery) — backend IPs<br><br>Enables zero-downtime config changes, canary deploys, traffic splitting, circuit breaking — all without restarting the gRPC server.",
    ["patterns", "xds"])

c("Patterns",
    "How does <b>OpenTelemetry</b> integrate with gRPC?",
    "OpenTelemetry provides automatic instrumentation for gRPC:<br><br><b>Client:</b><br><pre>import \"go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc\"<br>conn, _ := grpc.Dial(\"svc:50051\",<br>  grpc.WithUnaryInterceptor(otelgrpc.UnaryClientInterceptor()),<br>)</pre><b>Server:</b><br><pre>s := grpc.NewServer(<br>  grpc.UnaryInterceptor(otelgrpc.UnaryServerInterceptor()),<br>)</pre>This creates spans for each RPC with attributes: <code>rpc.service</code>, <code>rpc.method</code>, <code>rpc.grpc.status_code</code>, <code>net.peer.name</code>. Traces propagate via <code>traceparent</code> metadata header. Works with any OTel-compatible backend (Jaeger, Zipkin, Datadog, Grafana).",
    ["patterns", "opentelemetry"])

c("Patterns",
    "What is <b>TLS/mTLS</b> in gRPC and how to set it up?",
    "<b>Server TLS:</b><br><pre>creds, _ := credentials.NewServerTLSFromFile(\"cert.pem\", \"key.pem\")<br>s := grpc.NewServer(grpc.Creds(creds))</pre><b>Client TLS:</b><br><pre>creds, _ := credentials.NewClientTLSFromFile(\"ca.pem\", \"server.example.com\")<br>conn, _ := grpc.Dial(\"svc:50051\", grpc.WithTransportCredentials(creds))</pre><b>mTLS (both sides):</b> Server also passes <code>tls.Config{ClientAuth: tls.RequireAndVerifyClientCert}</code>. Client provides its own cert/key.<br><br>In production, use <code>grpc.WithTransportCredentials()</code> (not <code>insecure</code>). gRPC supports TLS 1.2+.",
    ["patterns", "tls"])

c("Patterns",
    "How do you <b>chain interceptors</b> in gRPC? (Go example)",
    "gRPC core supports only one interceptor per type by default. Use <code>grpc-middleware</code> to chain:<br><pre>import \"github.com/grpc-ecosystem/go-grpc-middleware/v2\"<br><br>s := grpc.NewServer(<br>  grpc.ChainUnaryInterceptor(<br>    otelgrpc.UnaryServerInterceptor(),   // 1: tracing<br>    loggingInterceptor,                    // 2: logging<br>    authInterceptor,                       // 3: auth<br>    recoveryInterceptor,                   // 4: panic recovery<br>  ),<br>  grpc.ChainStreamInterceptor(<br>    otelgrpc.StreamServerInterceptor(),<br>    loggingStreamInterceptor,<br>    authStreamInterceptor,<br>  ),<br>)</pre>Interceptors execute in <b>top-to-bottom order</b>. The first interceptor wraps the second, which wraps the third, which wraps the handler. For clients, use <code>ChainUnaryClient</code> / <code>ChainStreamClient</code>.",
    ["patterns", "interceptor-chaining"])

c("Patterns",
    "How does <b>compression</b> work in gRPC?",
    "gRPC supports per-message compression transparently:<br><pre>// Client: enable compression<br>conn, _ := grpc.Dial(\"svc:50051\",<br>  grpc.WithDefaultCallOptions(grpc.UseCompressor(gzip.Name)),<br>)<br><br>// Or per-call:<br>opts := []grpc.CallOption{grpc.UseCompressor(gzip.Name)}<br>resp, _ := client.Call(ctx, req, opts...)</pre>Supported codecs: <code>gzip</code> (default), <code>deflate</code>, <code>snappy</code>. Compression is negotiated per-message — client proposes, server accepts/rejects. The <b>compression flag</b> in the 5-byte gRPC header indicates whether the message body is compressed.<br><br><b>Guidance:</b> Compress payloads > 1KB. Don't compress small messages (overhead > savings). Protobuf is already compact — compression helps mostly for <code>string</code> and <code>bytes</code> fields.",
    ["patterns", "compression"])

c("Patterns",
    "What is <b>outlier detection</b> in gRPC load balancing?",
    "Outlier detection monitors backend health and ejects unhealthy backends from the load balancing pool:<br><pre>{<br>  \"loadBalancingConfig\": [{<br>    \"outlier_detection_experimental\": {<br>      \"interval\": \"10s\",<br>      \"baseEjectionTime\": \"30s\",<br>      \"maxEjectionTime\": \"300s\",<br>      \"maxEjectionPercent\": 10,<br>      \"successRateEjection\": {<br>        \"requestVolume\": 100,<br>        \"minimumHosts\": 3,<br>        \"enforcementPercentage\": 100<br>      },<br>      \"failurePercentageEjection\": {<br>        \"threshold\": 50,<br>        \"enforcementPercentage\": 100<br>      },<br>      \"childPolicy\": [{ \"round_robin\": {} }]<br>    }<br>  }]<br>}</pre>Ejects backends based on:<br>• <b>Success rate</b> — too many failed RPCs<br>• <b>Failure percentage</b> — ratio of failures > threshold<br>Reintegrates backends after ejection time expires. Essential for high-availability deployments.",
    ["patterns", "outlier-detection"])

c("Patterns",
    "What is the <b>gRPC service config</b> and how is it delivered?",
    "Service config is a JSON document that controls client behavior. It can be delivered via:<br><br>1. <b>Dial option:</b><br><pre>conn, _ := grpc.Dial(\"svc:50051\", grpc.WithDefaultServiceConfig(`{...}`))</pre>2. <b>DNS resolver:</b> return config via DNS TXT record at <code>_grpc_config.svc.example.com</code><br>3. <b>Custom resolver:</b> return config from your service discovery<br>4. <b>xDS:</b> config from control plane<br><br>Config controls: load balancing, retry, hedging, health checking, timeouts, method-level overrides. Changes are applied dynamically — no reconnect needed if the resolver pushes an update.",
    ["patterns", "service-config"])

# ── 07 GOTCHAS ───────────────────────────────────────────────────

c("Gotchas",
    "How does <b>protobuf JSON mapping</b> (proto3 JSON) work?",
    "Protobuf has a canonical JSON mapping for proto3 messages. Used by gRPC-gateway, <code>google.protobuf.util.JsonFormat</code>, and <code>grpcurl</code>:<br><br>• <b>Field names:</b> camelCase in JSON (not snake_case)<br>• <b>Enums:</b> string names, not integers<br>• <b>int64/uint64:</b> encoded as JSON strings (JS can't handle 64-bit ints)<br>• <b>bytes:</b> base64-encoded string<br>• <b>Timestamp:</b> RFC 3339 string <code>\"1972-01-01T10:00:20.021Z\"</code><br>• <b>Duration:</b> string <code>\"1.000340012s\"</code><br>• <b>FieldMask:</b> string <code>\"fName,fAge\"</code><br>• <b>Null:</b> <code>null</code> for wrapper types, omitted for normal fields<br>• <b>oneof:</b> only the set field appears (no discriminator)<br><br>Zero-value fields are <b>omitted</b> from JSON output (matching wire behavior).",
    ["gotchas", "json-mapping"])

c("Gotchas",
    "What is <b>protoc-gen-validate (pgv)</b> and how does it work?",
    "<b>protoc-gen-validate</b> is a protoc plugin that generates validation logic from annotations in the <code>.proto</code> file:<br><pre>import \"validate/validate.proto\";<br><br>message CreateUserRequest {<br>  string email = 1 [(validate.rules).string.email = true];<br>  string name  = 2 [(validate.rules).string = {<br>    min_len: 1, max_len: 100<br>  }];<br>  int32  age   = 3 [(validate.rules).int32 = {gte: 0, lte: 150}];<br>  repeated string roles = 4 [(validate.rules).repeated = {<br>    min_items: 1, unique: true<br>  }];<br>}</pre>Call <code>req.Validate()</code> in your handler to check all constraints before processing. Returns structured errors. Supports <b>cross-field validation</b>. Integrates with gRPC interceptors for automatic validation.",
    ["gotchas", "protoc-gen-validate"])

c("Gotchas",
    "What are the pitfalls of <b>large protobuf messages</b>?",
    "Beyond the 4MB default limit:<br>• <b>Memory:</b> Entire message is deserialized into RAM. A 100MB message uses 100MB+ per request.<br>• <b>Latency:</b> gRPC is synchronous per-message — client waits for full serialization before sending, server waits for full receive before handler.<br>• <b>Head-of-line blocking:</b> A large message on one stream can block others on the same HTTP/2 connection.<br>• <b>Partial failure:</b> If the connection drops mid-transfer, the entire message is lost (no partial recovery).<br><br><b>Solutions:</b><br>• Use <b>streaming</b> — chunk large data into multiple small messages<br>• Return a <b>URL/presigned URL</b> for large blobs (direct HTTP/object storage)<br>• Use <code>google.api.HttpBody</code> for custom media types<br>• Increase the limit only when truly necessary, and pair with request timeouts",
    ["gotchas", "large-messages"])

# ── 08 EXPERT ─────────────────────────────────────────────────────

c("Gotchas",
    "What happens if you <b>change a field number</b> in protobuf?",
    "<b>Breakage!</b> The wire format uses field numbers, not names. Changing field number 1 to 2 means:<br>• Old clients still send data at number 1 — server reads as field 2 (or junk)<br>• New clients send at number 2 — old server can't read it<br>• Data gets silently corrupted or ignored<br><br><b>Rule:</b> Field numbers are <b>permanent</b>. Once assigned, never change. Remove a field by marking it <code>reserved N;</code> instead.",
    ["gotchas", "field-number-change"])

c("Gotchas",
    "Why are <b>zero values</b> tricky in proto3?",
    "In proto3, zero values (<code>0</code>, <code>\"\"</code>, <code>false</code>, <code>0.0</code>) are <b>omitted from the wire format</b>. This means:<br><br>• <code>int32 count = 1;</code> — if count=0, it's not sent at all<br>• Receiver sees 0 as the default — but can't tell if it was explicitly set to 0 or never sent<br>• Problematic for booleans (<code>false</code> disappears)<br>• Problematic for enums (the first enum value MUST be 0, making it indistinguishable from \"unset\")<br><br><b>Fix:</b> Use <code>optional</code> keyword or <code>google.protobuf.Int32Value</code> wrapper for nullable semantics.",
    ["gotchas", "zero-value"])

c("Gotchas",
    "Why must the first enum value in proto3 be <code>0</code>?",
    "Protobuf enums use the zero value as the <b>default</b> when no value is set. If your first enum is <code>ACTIVE = 1</code>, an unset field defaults to... 0, which is not a valid enum value, causing undefined behavior.<br><br><b>Correct pattern:</b><br><pre>enum Status {<br>  STATUS_UNSPECIFIED = 0; // always start with a sentinel<br>  STATUS_ACTIVE      = 1;<br>  STATUS_INACTIVE    = 2;<br>}</pre>Use <code>_UNSPECIFIED</code> or <code>_UNKNOWN</code> as the 0-value sentinel.",
    ["gotchas", "enum-zero"])

c("Gotchas",
    "Why is <code>map</code> field ordering not guaranteed?",
    "Protobuf maps are stored as repeated key-value message pairs on the wire. The wire format <b>does not guarantee order</b> — entries can arrive in any sequence. If you serialize the same map twice, you may get different byte order.<br><br><b>Implications:</b><br>• Don't rely on map iteration order<br>• Don't use map order for hashing/checksums<br>• If you need ordered entries, use <code>repeated KeyValuePair</code> instead",
    ["gotchas", "map-ordering"])

c("Gotchas",
    "What are the key challenges when <b>upgrading from proto2 to proto3</b>?",
    "1. <b>Required fields are gone</b> — proto3 has no <code>required</code> keyword. Redesign validation.<br>2. <b>Optional tracking</b> — proto2 distinguishes \"unset\" from \"zero\"; proto3 doesn't (unless you use <code>optional</code>).<br>3. <b>Default values</b> — proto2 allows custom defaults; proto3 uses only zero/<code>UNSPECIFIED</code>.<br>4. <b>Groups are removed</b> — proto2 <code>group</code> syntax doesn't exist in proto3; convert to nested messages.<br>5. <b>Extensions removed</b> — use <code>Any</code> or <code>oneof</code> instead.<br>6. <b>Enums</b> — proto2 enums can have a non-zero default; proto3 requires 0.<br><br><b>Strategy:</b> Don't mix proto2 and proto3 in the same package. Upgrade one package at a time with careful deploy sequencing.",
    ["gotchas", "proto2-to-proto3"])

c("Gotchas",
    "What is the default <b>message size limit</b> in gRPC and how to change it?",
    "The default limit is <b>4 MB</b> per message (both send and receive). This prevents memory exhaustion from unexpectedly large payloads.<br><br><b>Change on server:</b><br><pre>s := grpc.NewServer(<br>  grpc.MaxRecvMsgSize(100 * 1024 * 1024), // 100MB receive<br>  grpc.MaxSendMsgSize(100 * 1024 * 1024), // 100MB send<br>)</pre><b>Change on client:</b><br><pre>conn, _ := grpc.Dial(\"svc:50051\",<br>  grpc.WithDefaultCallOptions(<br>    grpc.MaxCallRecvMsgSize(100*1024*1024),<br>    grpc.MaxCallSendMsgSize(100*1024*1024),<br>  ),<br>)</pre>For streaming, use <code>MaxSendMsgSize</code>/<code>MaxRecvMsgSize</code> dial options. For truly large data, consider chunking or using a different transport.",
    ["gotchas", "message-size"])

c("Gotchas",
    "Why does gRPC <b>require HTTP/2</b> and not HTTP/1.1?",
    "gRPC relies on HTTP/2 features that HTTP/1.1 lacks:<br>• <b>Multiplexing</b> — concurrent streams over one connection (essential for streaming RPCs)<br>• <b>Binary framing</b> — gRPC's length-prefixed message format requires it<br>• <b>Header compression</b> — gRPC uses HPACK for metadata<br>• <b>Full-duplex</b> — bidirectional streaming needs both sides to send simultaneously<br>• <b>Trailers</b> — gRPC sends status codes and metadata in HTTP trailers<br><br>If you need HTTP/1.1 compatibility, use gRPC-Web or the Connect protocol instead.",
    ["gotchas", "http2-requirement"])

c("Gotchas",
    "What are the <b>limitations of gRPC-Web</b> in browsers?",
    "gRPC-Web lets browsers call gRPC, but with restrictions:<br>• <b>Client-streaming and bidirectional streaming are NOT supported</b> — browsers lack the HTTP/2 framing APIs needed<br>• Requires a <b>proxy</b> (Envoy, grpcwebproxy, or gRPC-gateway) between browser and gRPC server<br>• <b>No trailers</b> in the browser (browsers don't expose HTTP trailers to JS)<br>• <b>Header/trailer merging</b> — the proxy folds headers+trailers into the response body<br>• Slower than native gRPC due to proxy hop<br><br>For full gRPC streaming in browsers, consider <b>Connect protocol</b> (buf's HTTP-based alternative) which works in browsers with all streaming patterns.",
    ["gotchas", "grpc-web-limits"])

c("Gotchas",
    "How does <b>deadline propagation</b> fail silently?",
    "If service A calls service B with a context, but service B <b>creates a new context</b> (e.g., <code>context.Background()</code>), the deadline is lost:<br><pre>// BAD — deadline lost<br>func (s *SvcA) Handle(ctx context.Context, req *pb.Req) (*pb.Resp, error) {<br>  return clientB.Call(context.Background(), &pb.InnerReq{}) // timeout won't propagate!<br>}<br><br>// GOOD — deadline preserved<br>func (s *SvcA) Handle(ctx context.Context, req *pb.Req) (*pb.Resp, error) {<br>  return clientB.Call(ctx, &pb.InnerReq{})<br>}</pre>Always pass the incoming context through to downstream calls. Background workers should create new contexts but explicitly set deadlines appropriate for the work.",
    ["gotchas", "deadline-propagation"])

c("Gotchas",
    "Why are metadata keys <b>case-insensitive</b> in gRPC?",
    "Metadata is transmitted as HTTP/2 headers, which are <b>case-insensitive</b> per the HTTP spec. gRPC <b>normalizes keys to lowercase</b>:<br><pre>md := metadata.Pairs(\"X-Request-ID\", \"123\")<br>md.Get(\"x-request-id\") // ✓ works<br>md.Get(\"X-Request-ID\") // ✗ returns \"\" — key was lowercased<br><br>// Always use lowercase when reading:<br>md.Get(\"x-request-id\") // correct</pre>Use <code>kebab-case</code> or <code>snake_case</code> for custom metadata keys. Avoid mixed-case or uppercase.",
    ["gotchas", "metadata-case"])

c("Gotchas",
    "What is the difference between a <b>connection</b> and a <b>channel</b> in gRPC? (Go)",
    "<b>Connection (<code>*grpc.ClientConn</code>)</b>: A concrete TCP connection with HTTP/2 setup. Created by <code>grpc.Dial()</code>.<br><br><b>Channel (same <code>*grpc.ClientConn</code> in Go)</b>: An abstraction that may hold <b>multiple sub-connections</b> (for load balancing). The channel manages reconnect, picker, and resolver logic.<br><br><b>Key insight:</b> <code>grpc.Dial()</code> returns a channel, not a single connection. The channel is lightweight — create one per backend and reuse it (thread-safe). Don't call <code>Dial</code> per RPC — that's expensive and leaks resources.",
    ["gotchas", "connection-vs-channel"])

c("Gotchas",
    "Why should you <b>disable server reflection in production</b>?",
    "Server reflection exposes your entire API surface to anyone who can reach the server — all service names, method signatures, and message structures. An attacker can:<br>• <b>Enumerate all services/methods</b> (api discovery)<br>• <b>Fuzz every endpoint</b> with auto-generated payloads<br>• <b>Find hidden/internal endpoints</b><br>• <b>Map your data model</b> from message schemas<br><br><b>Mitigation:</b><br>• Disable reflection in prod (<code>// reflection.Register(s)</code> commented out)<br>• Use <code>protoset</code> files with <code>grpcurl</code> instead<br>• Keep reflection on in staging/dev for debugging only",
    ["gotchas", "reflection-security"])

# ── 08 EXPERT ─────────────────────────────────────────────────────

c("Expert",
    "gRPC vs REST vs GraphQL vs event-driven (Kafka/NATS): decision matrix?",
    "<table><tr><td><b>Pattern</b></td><td><b>Best for</b></td><td><b>Trade-off</b></td></tr><tr><td><b>gRPC</b></td><td>Service-to-service sync RPC, strong contracts</td><td>Hard to consume from browsers; tight coupling</td></tr><tr><td><b>REST+JSON</b></td><td>Public APIs, browser clients, caching</td><td>Larger payloads; no streaming; loose contracts</td></tr><tr><td><b>GraphQL</b></td><td>Client-driven data fetching, mobile/web</td><td>Query complexity; N+1; heavy server-side</td></tr><tr><td><b>Event-driven</b> (Kafka/NATS)</td><td>Async workflows, decoupled services, CQRS</td><td>Eventual consistency; harder to debug/trace</td></tr></table><br><b>Reality:</b> Most systems use a mix. gRPC for internal sync calls, Kafka for events, REST for public APIs.",
    ["expert", "comparison"])

c("Expert",
    "When is gRPC <b>overkill</b>?",
    "gRPC adds complexity. It's overkill when:<br>• Simple CRUD API consumed only by browsers — use REST<br>• Single-team TypeScript monorepo — use tRPC<br>• Fire-and-forget operations — use message queues<br>• Large file transfers (>4MB messages) — use chunked HTTP or object storage URLs<br>• Public APIs with unknown consumers — harder to consume without codegen<br>• Prototyping rapidly — <code>.proto</code> + codegen cycle slows iteration<br>• Team has no protobuf/gRPC experience — steep learning curve<br><br>gRPC shines in <b>high-throughput, polyglot, microservice</b> environments. Outside that, simpler alternatives often suffice.",
    ["expert", "overkill"])

c("Expert",
    "What is the <b>Connect protocol</b> (by Buf)?",
    "Connect is an <b>HTTP/1.1 and HTTP/2 compatible</b> protocol that supports gRPC's streaming patterns without requiring gRPC's full stack:<br><br>• Uses <code>.proto</code> schemas (same as gRPC)<br>• Works in browsers with <b>all streaming patterns</b> (including client/bidi streaming!)<br>• Uses <b>JSON or Protobuf</b> over HTTP<br>• Supports gRPC clients natively (compatible wire format)<br>• No proxy needed for browser access<br><br><pre>$ buf generate buf.build/connectrpc/go<br>$ buf generate buf.build/connectrpc/es</pre>Generated client code works identically in Node and browsers. Connect is gRPC-Web's spiritual successor — all the benefits of gRPC, none of the browser limitations.",
    ["expert", "connect"])

c("Expert",
    "gRPC-Web vs Connect-Web vs gRPC-gateway: which for browser clients?",
    "<b>gRPC-Web:</b> HTTP/1.1 proxy bridge; no client/bidi streaming; legacy option.<br><br><b>Connect-Web:</b> Native HTTP; all streaming patterns; modern. Uses protobuf or JSON. Part of Buf ecosystem. <b>Recommended for new projects.</b><br><br><b>gRPC-gateway:</b> REST/JSON translation layer; adds REST endpoints from <code>.proto</code> annotations. Good when you need both REST and gRPC from one schema, but adds complexity and latency.<br><br><b>Quick guide:</b><br>• Browser-only app + streaming → Connect<br>• Need REST + gRPC from same schema → gRPC-gateway<br>• Legacy browser support (IE11) → gRPC-Web with Envoy",
    ["expert", "browser-options"])

c("Expert",
    "Monorepo vs polyrepo for <code>.proto</code> files: trade-offs?",
    "<b>Monorepo:</b><br>✓ Single source of truth; easy refactoring across services<br>✓ CI validates all proto compatibility at once<br>✓ No versioning headaches<br>✗ Large repos; slow tooling; harder access control<br>✗ Can create unwanted coupling<br><br><b>Polyrepo (BSR):</b><br>✓ Each team owns their APIs; clean boundaries<br>✓ Independent versioning and release cycles<br>✓ BSR manages dependencies (<code>buf mod update</code>)<br>✗ Need strict backward-compatibility discipline<br>✗ Cross-service refactors are harder<br>✗ Dependency graph complexity<br><br><b>Common pattern:</b> Polyrepo per domain, with shared \"common\" proto repo for cross-cutting types.",
    ["expert", "monorepo-vs-polyrepo"])

c("Expert",
    "Code-first vs proto-first: which approach?",
    "<b>Proto-first (write <code>.proto</code> first):</b><br>✓ Language-agnostic; single source of truth<br>✓ Contract reviewed independently of implementation<br>✓ Enforces API design thinking upfront<br>✗ Write twice — proto + implementation<br>✗ Slower iteration in early prototyping<br><br><b>Code-first (write code, generate proto):</b><br>✓ Faster prototyping; write code naturally<br>✓ Generate <code>.proto</code> from annotations (e.g., <code>protoc-gen-prost</code>, <code>@grpc/proto-loader</code>)<br>✗ Tied to a language; harder to share across teams<br>✗ Generated proto may not follow best practices<br><br><b>Recommendation:</b> Proto-first for multi-team/multi-language. Code-first for single-team internal services. Start proto-first once the API stabilizes.",
    ["expert", "code-first-vs-proto-first"])

c("Expert",
    "Should you use gRPC for <b>public APIs</b> or only internal?",
    "<b>Internal (microservice-to-microservice):</b> Strong fit. Low-latency, binary, streaming. Teams can share <code>.proto</code> easily.<br><br><b>Public APIs:</b> Challenging but possible:<br>✗ External users may not have protobuf tooling<br>✗ gRPC is harder to explore than REST (no browser URL bar)<br>✗ Some networks/firewalls block HTTP/2<br>✗ Versioning is harder (no URL versioning convention)<br>✓ Can pair with gRPC-gateway for REST fallback<br>✓ Works well for SDK-based APIs (mobile, partner integrations)<br>✓ Used by Google, Twitch, Netflix for public streaming APIs<br><br><b>Rule of thumb:</b> for public APIs where your users are developers, offer both gRPC and REST. For purely browser-facing APIs, start with REST/GraphQL.",
    ["expert", "public-vs-internal"])

c("Expert",
    "How does gRPC work with <b>Kubernetes and service meshes</b>?",
    "<b>Service discovery:</b> Use headless services + DNS resolver:<br><pre>service user-service {<br>  clusterIP: None # headless<br>}<br># gRPC dials: dns:///user-service:50051</pre><b>Sidecar proxies (Istio, Linkerd):</b><br>• Envoy sidecar intercepts all gRPC traffic<br>• Automatic mTLS between services<br>• Distributed tracing via propagated headers<br>• Traffic splitting for canary deploys<br>• Circuit breaking and retry at proxy level<br><b>Liveness/Readiness probes:</b> Use gRPC health protocol or <code>grpc_health_probe</code> binary for Kubernetes probes since <code>curl</code> can't call gRPC natively.",
    ["expert", "kubernetes"])

c("Expert",
    "How does gRPC <b>performance</b> compare to JSON REST?",
    "Independent benchmarks consistently show gRPC is:<br>• <b>7-10x faster</b> serialization than JSON (protobuf vs JSON marshal)<br>• <b>3-5x smaller</b> payloads (binary fields vs quoted strings)<br>• <b>2-3x higher throughput</b> in requests/sec<br>• <b>Lower CPU usage</b> — binary parsing is cheaper than JSON parsing<br>• <b>Better connection efficiency</b> — HTTP/2 multiplexing vs HTTP/1.1 connection-per-request<br><br>However, the bottleneck is usually <b>business logic + I/O</b>, not the serialization format. gRPC's real win is the <b>ecosystem</b> (codegen, streaming, deadlines, observability) more than raw bytes-per-second.",
    ["expert", "performance"])

c("Expert",
    "How do you build <b>custom protoc plugins</b>?",
    "Custom plugins read a <code>CodeGeneratorRequest</code> from stdin and write <code>CodeGeneratorResponse</code> to stdout:<br><pre>func main() {<br>  genReq := &pluginpb.CodeGeneratorRequest{}<br>  data, _ := io.ReadAll(os.Stdin)<br>  proto.Unmarshal(data, genReq)<br><br>  var files []*pluginpb.CodeGeneratorResponse_File<br>  descriptor := reg.File(genReq.ProtoFile[0])<br>  for _, svc := range descriptor.Services {<br>    // Generate code for each service<br>    files = append(files, &pluginpb.CodeGeneratorResponse_File{<br>      Name:    proto.String(svc.Name + \"_docs.md\"),<br>      Content: proto.String(generateDocs(svc)),<br>    })<br>  }<br><br>  resp := &pluginpb.CodeGeneratorResponse{File: files}<br>  out, _ := proto.Marshal(resp)<br>  os.Stdout.Write(out)<br>}</pre>Name the binary <code>protoc-gen-&lt;name&gt;</code>, put it on PATH. Then: <code>protoc --&lt;name&gt;_out=.</code>. Common use cases: custom code generators, linting, documentation, authorization policies, mock generation.",
    ["expert", "custom-plugins"])

c("Expert",
    "What are <b>custom codecs</b> in gRPC?",
    "gRPC allows replacing the default protobuf codec with a custom one:<br><pre>conn, _ := grpc.Dial(\"svc:50051\",<br>  grpc.WithDefaultCallOptions(grpc.ForceCodec(&flatbuffers.Codec{})),<br>)</pre>Implement <code>grpc.Codec</code> interface:<br><pre>type Codec interface {<br>  Marshal(v interface{}) ([]byte, error)<br>  Unmarshal(data []byte, v interface{}) error<br>  Name() string<br>}</pre>Use cases:<br>• <b>FlatBuffers</b> — zero-copy deserialization for performance<br>• <b>MessagePack</b> — smaller than JSON, faster than protobuf in some cases<br>• <b>Avro</b> — schema evolution without codegen<br>• <b>Raw bytes</b> — proxy/passthrough services that don't inspect payloads<br>• <b>Encrypted codec</b> — transparent payload encryption<br><br>Rarely needed — protobuf is already excellent.",
    ["expert", "custom-codecs"])

c("Expert",
    "How can you use gRPC for <b>A/B testing</b> at the RPC level?",
    "Use <b>metadata headers</b> to carry experiment flags:<br><pre>// Client<br>md := metadata.Pairs(\"x-experiment\", \"new-algo-v2\", \"x-user-id\", \"42\")<br>ctx := metadata.NewOutgoingContext(ctx, md)<br><br>// Server interceptor<br>func abTestInterceptor(ctx context.Context, req interface{},<br>  info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {<br>  md, _ := metadata.FromIncomingContext(ctx)<br>  exp := md.Get(\"x-experiment\")<br>  ctx = context.WithValue(ctx, \"experiment\", exp)<br>  return handler(ctx, req)<br>}</pre>You can also use <b>xDS route configuration</b> to split traffic by header at the proxy layer (Envoy), routing <code>x-experiment: v2</code> to a different backend deployment. Works with canary and blue-green deployment strategies.",
    ["expert", "ab-testing"])

c("Expert",
    "How do you design an <b>API gateway for gRPC</b>?",
    "An gRPC API gateway sits between clients and backend services:<br><br><b>Responsibilities:</b><br>1. <b>Auth</b> — validate JWT/API key, inject identity into context<br>2. <b>Rate limiting</b> — per-user/per-service quotas<br>3. <b>Request routing</b> — route by method to backends<br>4. <b>Protocol translation</b> — gRPC-Web → gRPC, REST → gRPC (gRPC-gateway)<br>5. <b>Observability</b> — centralized logging, tracing, metrics<br>6. <b>Response caching</b> — cache unary responses (respect deadline)<br>7. <b>Request/response transformation</b> — field masking, enrichment<br><br><b>Implementation options:</b><br>• Envoy with gRPC filter chain<br>• Custom gateway using <code>grpc.Server</code> + forwarding handler<br>• Commercial: Kong, Tyk (with gRPC plugins)<br>• Buf's Connect: edge-to-edge with a Connect gateway",
    ["expert", "api-gateway"])

c("Expert",
    "What are the considerations for gRPC on <b>mobile</b>?",
    "Mobile gRPC needs special care:<br><br>1. <b>Connection management:</b> Phones switch networks (WiFi ↔ cellular). Use <code>grpc.WithDisableRetry()</code> for streaming; detect network changes and reconnect.<br>2. <b>Battery:</b> Keepalives drain battery. Use longer intervals (60-120s) or disable keepalive; rely on OS-level push notifications instead.<br>3. <b>Bandwidth:</b> Protobuf binary is already small, but still compress large payloads with <code>grpc.WithDefaultCallOptions(grpc.UseCompressor(gzip.Name))</code>.<br>4. <b>Background sync:</b> Use WorkManager (Android) / BGTaskScheduler (iOS) to batch RPCs in a background window.<br>5. <b>Streaming:</b> gRPC native streaming works on mobile (Swift, Kotlin) — great for real-time features (chat, live location).<br>6. <b>Security:</b> Always use TLS. Pin certificates to prevent MITM.",
    ["expert", "mobile"])

c("Expert",
    "How to use gRPC streams for <b>real-time collaboration</b>?",
    "Bidirectional streaming is ideal for collaborative editing:<br><pre>service Collab {<br>  rpc Session (stream Operation) returns (stream Operation);<br>}<br>message Operation {<br>  string user_id    = 1;<br>  int32  position   = 2;<br>  string insert     = 3;<br>  int32  delete_len = 4;<br>  int64  timestamp  = 5;<br>}</pre><b>Architecture pattern:</b><br>1. Each client opens a bidi stream to the collaboration server<br>2. Server receives ops, applies OT (Operational Transformation) or CRDT<br>3. Server broadcasts transformed ops to all connected clients<br>4. Deadlines: Use <code>Keepalive</code> to detect disconnected clients<br>5. Scale: Shard by document ID across server instances<br><br>gRPC beats WebSockets here — typed messages, built-in flow control, deadlines, and interceptors for auth/logging.",
    ["expert", "real-time-collab"])

c("Expert",
    "What is <b>nanopb</b> and why use it for IoT/embedded?",
    "nanopb is a tiny protobuf implementation for <b>resource-constrained</b> systems (8/32-bit microcontrollers, RTOS, bare-metal).<br><br><b>Key features:</b><br>• < 10KB code footprint<br>• No dynamic memory allocation (static buffers)<br>• ISO C98 compatible (no libc required beyond basics)<br>• Generates <code>.pb.c</code>/<code>.pb.h</code> from <code>.proto</code> files<br>• Callback-based streaming for low-memory devices<br><br><b>Use case:</b> IoT sensor → gRPC-incompatible MCU → sends nanopb-encoded protobuf over MQTT/CoAP → cloud bridge decodes → sends to gRPC backend. Not full gRPC (no HTTP/2), but interoperable protobuf encoding.",
    ["expert", "nanopb"])

c("Expert",
    "How does the <b>Connect protocol</b> differ from gRPC on the wire?",
    "gRPC uses HTTP/2 with a specific framing protocol (length-prefixed messages, trailers, etc.). Connect supports:<br><br><b>Connect protocol (over HTTP/1.1):</b><br>• POST with <code>Content-Type: application/connect+json</code> or <code>application/connect+proto</code><br>• Unary: request in body → response in body (like REST)<br>• Server-streaming: each message as a JSON stream or protobuf message in the response body<br>• Client/bidi streaming: uses low-latency HTTP if available, falls back to request/response with chunking<br><br><b>gRPC protocol (over HTTP/1.1):</b><br>• Connect supports gRPC wire format too via <code>application/grpc</code> content-type<br>• gRPC servers can serve Connect clients, and Connect servers can serve gRPC clients<br>• This is the key value — <b>one server, both protocols</b>, no translation layer needed<br><br>In short: Connect is gRPC semantics on web-friendly transports.",
    ["expert", "connect-protocol"])

c("Expert",
    "What is <b>gRPC Transcoding</b> and how to set it up?",
    "gRPC Transcoding converts REST/JSON to gRPC using <code>google.api.http</code> annotations in <code>.proto</code>:<br><pre>import \"google/api/annotations.proto\";<br><br>rpc GetBook (GetBookRequest) returns (Book) {<br>  option (google.api.http) = {<br>    get: \"/v1/{name=books/*}\"<br>  };<br>}<br>rpc CreateBook (CreateBookRequest) returns (Book) {<br>  option (google.api.http) = {<br>    post: \"/v1/books\"<br>    body: \"*\"<br>  };<br>}</pre>Routes map HTTP methods + URL patterns to gRPC methods. Path parameters (<code>{name=books/*}</code>) are extracted into request fields. Request body maps to the message field.<br><br>Implemented by <b>Envoy's gRPC-JSON transcoder</b> filter and <b>gRPC-gateway</b>. Both read the annotations and proxy REST → gRPC transparently.",
    ["expert", "transcoding"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
