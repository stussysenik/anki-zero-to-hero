import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Protobuf"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "Syntax":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Syntax-Types"),
    "Advanced":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Advanced-Features"),
    "Tooling":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Tooling-Workflow"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ======================================================================
# L0 — FUNDAMENTALS
# ======================================================================

c("Fundamentals",
  "What are Protocol Buffers (protobuf)?",
  "A language-neutral, platform-neutral extensible mechanism for serializing structured data, developed by Google. You define schema in <code>.proto</code> files, then use <code>protoc</code> to generate data access classes in your language.",
  ["fundamentals", "serialization"])

c("Fundamentals",
  "How does binary serialization differ from text formats like JSON/XML?",
  "Binary serialization encodes data as compact bytes (varints, length-delimited chunks) instead of human-readable text. This gives ~3-10× smaller payloads, faster parsing (no string scanning), but loses human readability without tooling.",
  ["fundamentals", "binary", "json"])

c("Fundamentals",
  "What is forward/backward compatibility in protobuf?",
  "<b>Forward compatibility</b>: old binaries can read new messages (unknown fields are preserved but ignored). <b>Backward compatibility</b>: new binaries can read old messages (missing fields get default values). This is the key design goal — services can evolve schemas without coordinated deploys.",
  ["fundamentals", "compatibility"])

c("Fundamentals",
  "What is the protobuf wire format?",
  "Each message is a sequence of key-value pairs. A <b>wire key</b> is a varint encoding <code>(field_number &lt;&lt; 3) | wire_type</code>. The wire type determines how the value bytes are interpreted: varint (0), 64-bit (1), length-delimited (2), 32-bit (5).",
  ["fundamentals", "wire-format"])

c("Fundamentals",
  "Protobuf vs JSON: compare size, speed, and schema enforcement.",
  "<b>Size</b>: protobuf ~3-10× smaller (no field names, binary encoding). <b>Speed</b>: protobuf faster to serialize/deserialize (no string parsing). <b>Schema</b>: protobuf has strict schema enforcement at compile time; JSON is schemaless (unless you add JSON Schema separately). JSON is human-readable; protobuf requires <code>protoc --decode_raw</code>.",
  ["fundamentals", "json", "comparison"])

c("Fundamentals",
  "Protobuf vs MessagePack vs Avro vs FlatBuffers vs Cap'n Proto — summarize the tradeoffs.",
  "<b>Protobuf</b>: schema-first, best ecosystem/tooling, moderate speed. <b>MessagePack</b>: schemaless, JSON-like, good for drop-in JSON replacement. <b>Avro</b>: row-oriented, schema in header, great for Hadoop/big data. <b>FlatBuffers</b>: zero-copy deserialization, no parsing step, ideal for games/embedded. <b>Cap'n Proto</b>: zero-copy, fastest, but larger wire size, smaller ecosystem.",
  ["fundamentals", "comparison"])

c("Fundamentals",
  "What are the key differences between proto2 and proto3?",
  "<b>proto2</b>: fields can be <code>required</code>, <code>optional</code>, or <code>repeated</code>; has extensions, groups, default values you can set; <code>has_</code> methods for all fields. <b>proto3</b>: no <code>required</code>, no <code>optional</code> natively (added later with <code>optional</code> keyword in 3.15); no default value customization; no extensions/groups; enums must start at 0; JSON mapping built-in.",
  ["fundamentals", "proto2", "proto3"])

c("Fundamentals",
  "Walk through the protobuf workflow from schema to code.",
  "<pre>1. Write a <code>.proto</code> file defining messages, enums, services.\n2. Run <code>protoc --proto_path=. --cpp_out=. my.proto</code>\n3. <code>protoc</code> generates classes in your target language.\n4. Import/use the generated code to build, serialize (<code>SerializeToArray</code>), and parse (<code>ParseFromArray</code>) messages.</pre>",
  ["fundamentals", "workflow"])

c("Fundamentals",
  "What syntax declares a proto3 file and sets its package?",
  "<pre>syntax = \"proto3\";\n\npackage mycompany.myservice.v1;\n\nmessage MyMessage {\n  int32 id = 1;\n}</pre>The first non-comment line must be <code>syntax = \"proto3\";</code> (or <code>\"proto2\"</code> or <code>\"editions\"</code>).",
  ["fundamentals", "syntax"])

c("Fundamentals",
  "What happens to unknown fields during deserialization?",
  "In proto3, unknown fields are preserved during parsing and included in re-serialization (since 3.5). In proto2 they were always preserved. This is critical for forward compatibility: a proxy can forward a message with fields it doesn't understand without data loss.",
  ["fundamentals", "unknown-fields"])

c("Fundamentals",
  "What is a <code>.proto</code> file?",
  "A schema definition file written in the Protocol Buffers IDL (Interface Definition Language). It defines messages (data structures), enums, services (RPC methods), and options. It is the single source of truth for your data model.",
  ["fundamentals", "proto-file"])

c("Fundamentals",
  "Why does protobuf use field numbers instead of field names on the wire?",
  "Field names are never transmitted. Each field is identified by its integer <b>field number</b> (1-536,870,911) encoded as a varint in the wire key. This is what makes protobuf compact and enables field renaming without breaking compatibility.",
  ["fundamentals", "field-numbers"])

# ======================================================================
# L1 — SYNTAX & TYPES
# ======================================================================

c("Syntax",
  "List the protobuf scalar types and their corresponding wire types.",
  "<pre>Varint (wire type 0):  int32, int64, uint32, uint64,\n                         sint32, sint64, bool, enum\n64-bit (wire type 1):   fixed64, sfixed64, double\nLength-delimited (2):   string, bytes, embedded messages,\n                         packed repeated fields\n32-bit (wire type 5):   fixed32, sfixed32, float</pre>",
  ["syntax", "scalars", "wire-types"])

c("Syntax",
  "How does varint encoding work in protobuf?",
  "A variable-length integer encoding where each byte uses 7 bits for data and 1 bit (MSB) as a continuation flag. If MSB=1, more bytes follow. Smaller numbers use fewer bytes: values 0-127 take 1 byte, 128-16383 take 2 bytes, etc. Negative numbers in <code>int32</code>/<code>int64</code> always take 10 bytes (sign extension).",
  ["syntax", "varint"])

c("Syntax",
  "What is zigzag encoding and when should you use it?",
  "Zigzag encoding maps signed integers to unsigned integers by interleaving positive and negative values: <code>0→0, -1→1, 1→2, -2→3, 2→4</code>. Used by <code>sint32</code> and <code>sint64</code> so that small negative numbers (like -1) encode compactly as varints instead of always taking 10 bytes. Always use <code>sint*</code> for fields that are frequently negative.",
  ["syntax", "zigzag"])

c("Syntax",
  "What is the valid range for field numbers and which ones are reserved?",
  "<b>Valid range</b>: 1 to 2<sup>29</sup>-1 (536,870,911). <b>Reserved</b>: 19000 through 19999 are reserved for the protobuf implementation (FieldDescriptor::kFirstReservedNumber through kLastReservedNumber). Field numbers 1-15 take 1 byte for the tag; 16-2047 take 2 bytes. Use 1-15 for frequently-occurring fields.",
  ["syntax", "field-numbers"])

c("Syntax",
  "How do you define a message with nested types?",
  "<pre>message Outer {\n  message Inner {\n    string value = 1;\n  }\n  Inner inner = 1;\n  enum Status {\n    UNKNOWN = 0;\n    ACTIVE = 1;\n  }\n  Status status = 2;\n}</pre>Nested messages and enums are scoped to the parent. Reference as <code>Outer.Inner</code> outside the parent.",
  ["syntax", "messages", "nested"])

c("Syntax",
  "How do you define an enum in proto3? What rule must the first value follow?",
  "<pre>enum PhoneType {\n  PHONE_TYPE_UNSPECIFIED = 0;\n  PHONE_TYPE_MOBILE = 1;\n  PHONE_TYPE_HOME = 2;\n  PHONE_TYPE_WORK = 3;\n}</pre>The first enum value <b>must be 0</b> (zero-value default). In proto3, enums are <b>open</b> — they can receive unknown values at runtime. Names are <code>SCREAMING_SNAKE_CASE</code> prefixed with the enum type name.",
  ["syntax", "enums"])

c("Syntax",
  "What is the difference between packed and unpacked repeated fields?",
  "<pre>repeated int32 ids = 1;           // unpacked (proto2 default)\nrepeated int32 ids = 1 [packed=true]; // packed (proto3 default)</pre><b>Packed</b>: all values stored in a single length-delimited record — more compact. <b>Unpacked</b>: each value gets its own key-value pair. In proto3, scalar repeated fields are packed by default; you can disable with <code>[packed=false]</code>.",
  ["syntax", "repeated", "packed"])

c("Syntax",
  "How do you define a map field? What are the key restrictions?",
  "<pre>map&lt;string, Project&gt; projects = 3;\nmap&lt;int32, string&gt; id_to_name = 4;</pre><b>Key type</b>: any scalar except float/double, bytes, enums, or messages. <b>Value</b>: any type except another map. Maps are <b>not ordered</b> (iteration order is not guaranteed). They CANNOT be <code>repeated</code>. On the wire, a map is a repeated message with <code>key</code> (field 1) and <code>value</code> (field 2).",
  ["syntax", "maps"])

c("Syntax",
  "What is a <code>oneof</code> and when would you use it?",
  "<pre>message SampleMessage {\n  oneof test_oneof {\n    string name = 4;\n    SubMessage sub_message = 9;\n  }\n}</pre>A <code>oneof</code> enforces that at most one field in the group is set at a time. Setting one field automatically clears all others. In C++, use <code>which_oneof_case()</code> / <code>oneof_name_case()</code>. In proto3, you can't use <code>repeated</code> or <code>map</code> inside a oneof.",
  ["syntax", "oneof"])

c("Syntax",
  "What does the <code>optional</code> keyword do in proto3?",
  "Added in proto3.15 (2021): <code>optional string name = 1;</code> makes the field explicitly optional — it generates <code>has_name()</code> / <code>clear_name()</code> methods, allowing you to distinguish between \"not set\" and \"set to the zero value\". Without <code>optional</code>, proto3 can't tell the difference between <code>0</code> and unset.",
  ["syntax", "optional"])

c("Syntax",
  "How do you reserve field numbers and names?",
  "<pre>message Foo {\n  reserved 2, 15, 9 to 11;\n  reserved \"foo\", \"bar\";\n}</pre>Prevents new fields from reusing old numbers/names that would break deserialization of legacy data. <code>reserved</code> statements can be at message level. You cannot mix field declarations with reserved numbers in the same statement, but you can have separate reserved statements.",
  ["syntax", "reserved"])

c("Syntax",
  "What are the default values in proto3?",
  "<pre>int32/int64/uint32/uint64/fixed*/sfixed* → 0\nbool → false\nstring → \"\" (empty)\nbytes → empty\nenum → first defined value (must be 0)\nmessage → not set (language-specific: null/None/nil)\nrepeated → empty list\noneof → none set</pre>",
  ["syntax", "defaults"])

c("Syntax",
  "What is <code>google.protobuf.Any</code> and how do you use it?",
  "<pre>import \"google/protobuf/any.proto\";\n\nmessage ErrorStatus {\n  repeated google.protobuf.Any details = 2;\n}</pre><code>Any</code> can hold any serialized protobuf message. Fields: <code>type_url</code> (string like <code>\"type.googleapis.com/my.package.MyMessage\"</code>) and <code>value</code> (bytes of serialized message). Use <code>Pack()</code> and <code>UnpackTo()</code> in C++, <code>pack()</code>/<code>unpack()</code> in Python. Enables polymorphic message containers.",
  ["syntax", "well-known", "any"])

c("Syntax",
  "What is <code>google.protobuf.Timestamp</code>? What precision and epoch does it use?",
  "<pre>import \"google/protobuf/timestamp.proto\";\n\ngoogle.protobuf.Timestamp created_at = 1;\n// Fields: int64 seconds, int32 nanos</pre>Represents a point in time with <b>nanosecond precision</b>. Epoch is Unix epoch (1970-01-01T00:00:00Z). <code>seconds</code> can be negative for dates before 1970. <code>nanos</code> must be 0-999,999,999. Always stored in UTC.",
  ["syntax", "well-known", "timestamp"])

c("Syntax",
  "What is <code>google.protobuf.Duration</code>?",
  "<pre>import \"google/protobuf/duration.proto\";\n\ngoogle.protobuf.Duration timeout = 1;\n// Fields: int64 seconds, int32 nanos</pre>Represents a time span with nanosecond precision. <code>seconds</code> can be negative. <code>nanos</code> must be -999,999,999 to +999,999,999 with the same sign as <code>seconds</code> (or zero).",
  ["syntax", "well-known", "duration"])

c("Syntax",
  "What is <code>google.protobuf.Struct</code> and its companion types?",
  "<pre>import \"google/protobuf/struct.proto\";\n\n// Struct: map&lt;string, Value&gt; — dynamic JSON object\n// Value: oneof { null_value, number_value, string_value, bool_value, struct_value, list_value }\n// ListValue: repeated Value — dynamic JSON array\n// NullValue: enum { NULL_VALUE = 0; }</pre>Used for representing arbitrary JSON data without a predefined schema. Maps 1:1 to JSON types.",
  ["syntax", "well-known", "struct"])

c("Syntax",
  "What is <code>google.protobuf.FieldMask</code>?",
  "<pre>import \"google/protobuf/field_mask.proto\";\n\nmessage UpdateRequest {\n  MyMessage data = 1;\n  google.protobuf.FieldMask update_mask = 2;\n}</pre>A set of field paths (strings like <code>\"foo.bar\"</code>) indicating which fields should be updated in a partial update operation. Commonly used in gRPC <code>Update</code> RPCs to implement <b>field masks</b> for PATCH semantics.",
  ["syntax", "well-known", "fieldmask"])

c("Syntax",
  "What are Wrapper types and what is their status?",
  "<pre>import \"google/protobuf/wrappers.proto\";\n\ngoogle.protobuf.Int32Value age = 1;\ngoogle.protobuf.StringValue name = 2;</pre>Wrappers (<code>Int32Value</code>, <code>StringValue</code>, <code>BoolValue</code>, <code>DoubleValue</code>, <code>FloatValue</code>, <code>Int64Value</code>, <code>UInt32Value</code>, <code>UInt64Value</code>, <code>BytesValue</code>) wrap scalars in a message so you can distinguish unset from zero. <b>Deprecated</b> in favor of proto3 <code>optional</code> keyword (proto3.15+).",
  ["syntax", "well-known", "wrappers"])

c("Syntax",
  "What is <code>google.protobuf.Empty</code>?",
  "An empty message with no fields. Used for RPC methods that take no input or return no output (e.g., <code>rpc DeleteThing(DeleteRequest) returns (google.protobuf.Empty);</code>). Avoids having to define one-off empty messages.",
  ["syntax", "well-known", "empty"])

c("Syntax",
  "How is a <code>bytes</code> field different from <code>string</code>?",
  "<code>string</code> must be valid UTF-8 (protobuf runtime enforces this). <code>bytes</code> can contain arbitrary binary data (no encoding constraints). Both use <b>length-delimited</b> wire type. Use <code>bytes</code> for binary blobs, images, hashes, encrypted data. Use <code>string</code> for text.",
  ["syntax", "scalars"])

c("Syntax",
  "What are the <code>fixed32</code>/<code>fixed64</code> types and when to use them?",
  "<code>fixed32</code> always takes 4 bytes; <code>fixed64</code> always takes 8 bytes. <code>sfixed32</code>/<code>sfixed64</code> are the signed variants. Use them for values that are usually large (e.g., hashes, timestamps in seconds) where varint's variable-length encoding is wasteful. They use wire types 5 (32-bit) and 1 (64-bit).",
  ["syntax", "scalars", "fixed"])

c("Syntax",
  "Can you use <code>repeated</code> inside a <code>oneof</code>? What about <code>map</code>?",
  "No and no. <code>oneof</code> fields cannot be <code>repeated</code> or <code>map</code> fields. Only singular message, scalar, or enum fields are allowed inside a <code>oneof</code>. If you need multiple values, wrap them in a containing message: <code>oneof foo { RepeatedWrapper wrapper = 1; }</code>.",
  ["syntax", "oneof", "restrictions"])

c("Syntax",
  "How do you set custom options on a field?",
  "<pre>import \"google/protobuf/descriptor.proto\";\n\nextend google.protobuf.FieldOptions {\n  bool my_field_flag = 50000;\n}\n\nmessage Foo {\n  int32 id = 1 [(my_field_flag) = true];\n}</pre>Options are set using square bracket syntax. Built-in field options include <code>[packed=true]</code>, <code>[deprecated=true]</code>, <code>[json_name=\"...\"]</code>. Custom options require extending <code>google.protobuf.FieldOptions</code>.",
  ["syntax", "options"])

# ======================================================================
# L2 — ADVANCED FEATURES
# ======================================================================

c("Advanced",
  "How do import statements work in protobuf?",
  "<pre>import \"google/protobuf/timestamp.proto\";\nimport \"mycompany/common/types.proto\";</pre>Makes types from other <code>.proto</code> files available. The path is relative to one of the <code>--proto_path</code> (or <code>-I</code>) directories specified in <code>protoc</code>. Does <b>not</b> transitively expose imported types — use <code>import public</code> for that.",
  ["advanced", "imports"])

c("Advanced",
  "What is <code>import public</code> (transitive import)?",
  "<pre>// a.proto\nimport public \"b.proto\";  // anyone importing a.proto also gets b.proto\nimport \"c.proto\";          // c.proto is private to a.proto</pre><code>import public</code> makes the imported file's types available to anyone who imports the current file. This lets you create \"facade\" proto files that re-export types. Used heavily in <code>google/protobuf/</code> well-known types.",
  ["advanced", "imports", "public"])

c("Advanced",
  "What are weak imports and what is their status in proto3?",
  "<pre>import weak \"other.proto\";  // proto2 only</pre>Weak imports allow referencing types from another file without forcing a build dependency. If the imported file is not available, references fall back to <code>google.protobuf.Any</code>. <b>Deprecated</b> and removed from proto3; not supported in most language runtimes (Java, C++ dropped support). Use <code>import public</code> instead.",
  ["advanced", "imports", "weak"])

c("Advanced",
  "What are extensions (proto2)? How do you define and use them?",
  "<pre>// base.proto\nmessage Foo {\n  extensions 100 to 200;  // reserve extension range\n}\n\n// ext.proto\nimport \"base.proto\";\nextend Foo {\n  optional int32 bar = 100;\n}\n\n// usage (C++)\nfoo.SetExtension(bar, 42);</pre>Extensions allow third-party <code>.proto</code> files to add fields to existing messages using field numbers in a reserved <code>extensions</code> range. <b>Removed from proto3</b> — use <code>Any</code> or composition instead.",
  ["advanced", "extensions", "proto2"])

c("Advanced",
  "What is <code>extend google.protobuf.FieldOptions</code> used for?",
  "It is the mechanism for defining <b>custom options</b>. You extend a descriptor options message (like <code>FieldOptions</code>, <code>MessageOptions</code>, <code>FileOptions</code>) to define new annotations that can be placed on proto elements. Example: <code>extend google.protobuf.FieldOptions { bool sensitive = 50001; }</code> then use <code>string password = 1 [(sensitive) = true];</code>.",
  ["advanced", "extensions", "options"])

c("Advanced",
  "What are protobuf options and where can they be applied?",
  "Options are annotations that control code generation and runtime behavior. They can be applied at: <b>file level</b> (<code>option go_package = \"...\";</code>), <b>message level</b> (<code>option message_set_wire_format = true;</code>), <b>field level</b> (<code>[packed=true]</code>), <b>enum level</b> (<code>option allow_alias = true;</code>), <b>service/method level</b>. Accessed via descriptors at runtime.",
  ["advanced", "options"])

c("Advanced",
  "What are descriptors in protobuf?",
  "Descriptors are runtime metadata objects that describe the structure of proto files, messages, enums, fields, etc. <code>google.protobuf.FileDescriptor</code> represents a whole .proto file. <code>google.protobuf.Descriptor</code> represents a message. <code>google.protobuf.FieldDescriptor</code> represents a field. They enable <b>reflection</b> — inspecting and manipulating messages without generated code.",
  ["advanced", "descriptors", "reflection"])

c("Advanced",
  "What is protobuf reflection used for?",
  "Reflection allows you to dynamically inspect message structure at runtime: iterate fields, get/set values by name, traverse nested messages, check types, access options. Used for: debugging tools, generic serialization code, config-driven data pipelines, protobuf-to-JSON conversion, and building libraries that work with any message type.",
  ["advanced", "reflection"])

c("Advanced",
  "What are dynamic messages?",
  "Messages constructed at runtime using <code>google.protobuf.DynamicMessage</code> (C++/Java/Python). You create a <code>DynamicMessageFactory</code> from a <code>Descriptor</code> and build messages without compile-time generated classes. Essential for tools that process proto files at runtime (e.g., <code>protoc</code> plugins, debugging proxies, schema registries).",
  ["advanced", "dynamic-messages", "reflection"])

c("Advanced",
  "How do you pack and unpack <code>google.protobuf.Any</code>?",
  "<pre>// Pack\nAny any;\nmy_message.PackTo(&any);  // C++\nany = Any.pack(my_message)  # Python\n\n// Unpack\nmy_message.ParseFromString(any.value());  // manual\nany.UnpackTo(&my_message);  // C++ with type check\nmy_message = Any.unpack(any)  # Python</pre><code>type_url</code> is set to <code>\"type.googleapis.com/package.Message\"</code>. Unpacking validates the type URL.",
  ["advanced", "any", "pack-unpack"])

c("Advanced",
  "How does <code>google.protobuf.FieldMask</code> implement partial updates?",
  "Specify paths like <code>\"user.name\"</code>, <code>\"user.email\"</code> in the FieldMask. The server applies only those fields from the request message. Sub-fields use dot-notation: <code>\"address.city\"</code>. For repeated fields, use <code>\"repeated_field\"</code> (entire list) — individual repeated elements cannot be masked. Use <code>FieldMaskUtil::Merge()</code> / <code>Intersect()</code> / <code>Subtract()</code>.",
  ["advanced", "fieldmask", "partial-update"])

c("Advanced",
  "What are proto2 groups and why were they deprecated?",
  "<pre>message Foo {\n  optional group Bar = 1 {  // proto2 only\n    optional int32 baz = 2;\n  }\n}</pre>Groups were an alternative syntax for nested messages that used a different wire format (start-group/end-group wire types 3 and 4). Deprecated because: confusing syntax, slower parsing, harder to evolve, and the wire types 3/4 were removed from proto3. Use nested messages instead.",
  ["advanced", "groups", "proto2"])

c("Advanced",
  "What were the proto2 label specifiers: <code>required</code>, <code>optional</code>, <code>repeated</code>?",
  "<b>required</b>: must be set, otherwise parsing fails. <b>optional</b>: may be unset (has <code>has_</code> methods). <b>repeated</b>: zero or more values. <code>required</code> is <b>forever</b> — you can never remove a required field or change it to optional without breaking compatibility. This is the main reason it was removed from proto3.",
  ["advanced", "proto2", "labels"])

c("Advanced",
  "How do you migrate from proto2 to proto3?",
  "<b>Step 1</b>: change all <code>required</code> fields to <code>optional</code> (or validate at application level). <b>Step 2</b>: remove field-level default values (proto3 uses type defaults). <b>Step 3</b>: remove extensions and groups. <b>Step 4</b>: ensure all enums start at 0. <b>Step 5</b>: change <code>syntax</code> declaration. Proto2 and proto3 messages can coexist in the same binary — migration can be incremental per message.",
  ["advanced", "proto2", "proto3", "migration"])

c("Advanced",
  "What are proto editions?",
  "Introduced in 2023, editions replace the <code>syntax = \"proto2\"</code> / <code>\"proto3\"</code> dichotomy with fine-grained feature flags: <code>edition = \"2023\"</code>. Features like <code>field_presence</code>, <code>enum_type</code>, <code>repeated_field_encoding</code>, <code>message_encoding</code> can be set per file or per field. Goal: evolve the language without breaking changes to syntax declarations.",
  ["advanced", "editions"])

c("Advanced",
  "How does protobuf handle JSON mapping in proto3?",
  "proto3 defines a canonical JSON mapping: field names become camelCase, enums become strings, <code>bytes</code> become base64, <code>Timestamp</code> becomes RFC 3339, <code>Duration</code> becomes <code>\"1.5s\"</code>, <code>Any</code> uses <code>@type</code> property, null is omitted, default values are omitted. Use <code>json_name</code> option to override field names. Protobuf libraries include <code>JsonFormat</code> / <code>util::JsonStringToMessage</code>.",
  ["advanced", "json", "mapping"])

# ======================================================================
# L3 — TOOLING & WORKFLOW
# ======================================================================

c("Tooling",
  "How do you use <code>protoc</code> to compile a .proto file?",
  "<pre>protoc --proto_path=src \\\n       --cpp_out=gen/cpp \\\n       --python_out=gen/python \\\n       src/my.proto</pre><code>--proto_path</code> (or <code>-I</code>) specifies import directories. <code>--X_out</code> specifies output directory for language X. Multiple <code>--proto_path</code> and <code>--X_out</code> flags can be used. Run <code>protoc --help</code> to see all supported languages.",
  ["tooling", "protoc"])

c("Tooling",
  "List common <code>protoc</code> plugin flags for different languages.",
  "<pre>--cpp_out         C++\n--csharp_out      C#\n--java_out        Java\n--kotlin_out      Kotlin\n--objc_out        Objective-C\n--php_out         PHP\n--python_out      Python\n--ruby_out        Ruby\n--go_out          Go (requires protoc-gen-go plugin)\n--js_out          JavaScript\n--ts_out          TypeScript (via protoc-gen-ts)\n--dart_out        Dart\n--rust_out        Rust (via protoc-gen-rust)\n--swift_out       Swift</pre>",
  ["tooling", "protoc", "plugins"])

c("Tooling",
  "What is the <code>buf</code> tool and why use it over <code>protoc</code>?",
  "<code>buf</code> is a modern protobuf toolchain: <b>buf lint</b> enforces style/compatibility rules, <b>buf format</b> formats .proto files, <b>buf breaking</b> detects breaking changes, <b>buf generate</b> replaces protoc with a YAML-driven pipeline, <b>buf build</b> compiles to a FileDescriptorSet, <b>BSR</b> is a hosted schema registry. Config is in <code>buf.yaml</code> and <code>buf.gen.yaml</code>.",
  ["tooling", "buf"])

c("Tooling",
  "What does <code>buf.yaml</code> configure?",
  "<pre>version: v2\nmodules:\n  - path: proto\nlint:\n  use:\n    - DEFAULT\nbreaking:\n  use:\n    - FILE\ndeps:\n  - buf.build/googleapis/googleapis</pre>Defines the workspace modules, lint rules, breaking change detection rules, and external dependencies (pulled from BSR). The root config file for <code>buf lint</code> and <code>buf breaking</code>.",
  ["tooling", "buf", "buf.yaml"])

c("Tooling",
  "What does <code>buf.gen.yaml</code> configure?",
  "<pre>version: v2\nplugins:\n  - plugin: buf.build/protocolbuffers/go\n    out: gen/go\n    opt: paths=source_relative\n  - plugin: buf.build/grpc/go\n    out: gen/go\n    opt: paths=source_relative</pre>Defines the code generation pipeline: which plugins to run, output directories, and plugin options. Replaces long <code>protoc</code> command lines with a declarative config that can be version-controlled.",
  ["tooling", "buf", "buf.gen.yaml"])

c("Tooling",
  "What does <code>buf lint</code> check?",
  "Enforces protobuf style and best practices: file layout, package naming, consistent syntax declarations, no <code>reserved</code> collisions, field naming conventions (lower_snake_case), enum value naming (UPPER_SNAKE_CASE), rpc naming, proper import paths (<code>DIRECTORY_SAME_PACKAGE</code>), and many more rules from the <code>DEFAULT</code> and <code>COMMENTS</code> categories.",
  ["tooling", "buf", "lint"])

c("Tooling",
  "What does <code>buf breaking</code> do?",
  "Detects breaking changes between two versions of your protobuf schema. Categories: <code>FILE</code> (file-level changes like moving/renaming), <code>PACKAGE</code> (package-level), <code>WIRE</code> (wire-format breaking — field number changes, type changes), <code>WIRE_JSON</code> (JSON breaking). Run in CI to prevent accidental breaking changes to APIs.",
  ["tooling", "buf", "breaking"])

c("Tooling",
  "What is the Buf Schema Registry (BSR)?",
  "A hosted registry (like npm/Docker Hub) for protobuf schemas at <code>buf.build</code>. You can publish modules with <code>buf push</code>, depend on others' modules with <code>deps</code> in <code>buf.yaml</code>, and discover community schemas. Supports generated SDKs (Go, TypeScript, etc.) served directly from the registry. Enables a proto monorepo or federated model.",
  ["tooling", "buf", "bsr"])

c("Tooling",
  "What are best practices for organizing proto files in a repository?",
  "<pre>proto/\n  mycompany/\n    myservice/\n      v1/\n        myservice.proto\n        types.proto\n      v2/\n        myservice.proto\n  google/\n    api/\n      annotations.proto</pre><b>1.</b> Mirror the package path in the file path. <b>2.</b> Version APIs in the package name (<code>mycompany.myservice.v1</code>). <b>3.</b> Keep shared types in separate files. <b>4.</b> Never mix API versions in the same directory. <b>5.</b> Vendor or depend on external protos via BSR or git submodules.",
  ["tooling", "best-practices", "organization"])

c("Tooling",
  "What are protobuf package naming conventions?",
  "<pre>package mycompany.myservice.v1;  // lowercase, dots as separators</pre>All lowercase, use reverse domain name (<code>com.mycompany...</code>) or your org prefix. Include API version. Avoid: Java package names with <code>_</code>, generic names like <code>types</code> or <code>common</code> at top level (they conflict across projects). Package name affects generated code namespace.",
  ["tooling", "packages", "naming"])

c("Tooling",
  "What is <code>protoc-gen-go</code> and what options does it support?",
  "The Go protoc plugin that generates <code>.pb.go</code> files. Key options: <code>paths=source_relative</code> (output follows proto file layout), <code>paths=import</code> (output follows Go import paths), <code>module=...</code> (prefix for import paths). Separate from <code>protoc-gen-go-grpc</code> which generates gRPC stubs. In proto file: <code>option go_package = \"github.com/myorg/mypkg/v1\";</code>.",
  ["tooling", "go", "protoc-gen-go"])

c("Tooling",
  "What is the <code>proto-validate</code> library?",
  "A protobuf validation library that lets you define validation rules as field options: <pre>message Person {\n  string email = 1 [(validate.rules).string.email = true];\n  int32 age = 2 [(validate.rules).int32 = {gte: 0, lte: 150}];\n}</pre>Generates validation code in Go, Java, C++, Python. Rules cover strings (len, pattern, email), numbers (gt, lt, in), repeated (min_items), maps, messages, and cross-field validation via CEL expressions.",
  ["tooling", "validate"])

c("Tooling",
  "What is <code>protodep</code>?",
  "A dependency management tool for proto files. Uses <code>protodep.toml</code> to declare dependencies on external proto repositories. Resolves, downloads, and copies dependent proto files into your project tree. Similar to npm/gem but for <code>.proto</code> files. Consider <code>buf</code>'s BSR dependency management as the modern alternative.",
  ["tooling", "protodep"])

c("Tooling",
  "How do you build protobuf libraries as reusable packages?",
  "<b>1.</b> Publish <code>.proto</code> files to BSR with <code>buf push</code>. <b>2.</b> Publish generated code to language package registries (npm, PyPI, Maven, Go modules). <b>3.</b> Use git submodules for mono-repo setups. <b>4.</b> Ship both the raw proto (for other compiled languages) and generated code (for convenience). Example: <code>googleapis/googleapis</code> publishes proto definitions only — consumers generate their own code.",
  ["tooling", "packages", "libraries"])

# ======================================================================
# L4 — GOTCHAS
# ======================================================================

c("Gotchas",
  "What happens if you reuse an old field number for a new field?",
  "Old serialized data with that field number will deserialize into the new field type, potentially causing data corruption or crashes. The binary data doesn't carry type information — only field number and wire type. If the wire types happen to match, you get garbage data; if they don't, the field is silently skipped (unknown field behavior). <b>Never reuse field numbers.</b>",
  ["gotchas", "field-numbers"])

c("Gotchas",
  "What is the proto3 zero-value problem (the \"has\" problem)?",
  "In proto3 without <code>optional</code>, you cannot distinguish between \"field not set\" and \"field set to its zero value\" (<code>0</code>, <code>\"\"</code>, <code>false</code>, empty enum). This makes it impossible to implement partial updates correctly. Solutions: <b>1.</b> Use <code>optional</code> keyword (proto3.15+). <b>2.</b> Use Wrapper types (deprecated). <b>3.</b> Use <code>oneof</code> wrappers.",
  ["gotchas", "zero-value", "has"])

c("Gotchas",
  "What is the proto3 enum behavior when receiving unknown values?",
  "proto3 enums are <b>open</b> — they can hold integer values not defined in the enum. The enum field retains the unknown numeric value (not the default 0). This enables forward compatibility: an old client receiving a new enum value won't crash. In C++, use <code>Enum_Name()</code> which returns <code>\"UNKNOWN_ENUM_VALUE_<number>\"</code> for unknown values.",
  ["gotchas", "enums", "unknown-values"])

c("Gotchas",
  "Are map fields ordered?",
  "No. <code>map&lt;K, V&gt;</code> iteration order is not guaranteed and should not be relied upon. Different language runtimes may iterate in different orders. The wire format itself has no ordering guarantees for map entries. If you need ordering, use <code>repeated</code> with an explicit key-value message or sort after deserialization.",
  ["gotchas", "maps", "ordering"])

c("Gotchas",
  "Why does int64 lose precision when serialized as JSON?",
  "JavaScript uses IEEE 754 doubles for all numbers, which can only represent integers up to 2<sup>53</sup> exactly. int64 values can go up to 2<sup>63</sup>-1. When proto3 JSON mapping converts int64 to a JSON number, values outside the safe integer range lose precision. <b>Solution</b>: use <code>string</code> representation for int64 in JSON APIs, or use <code>(jstype) = JS_STRING</code> option on the field.",
  ["gotchas", "json", "int64"])

c("Gotchas",
  "What are the backward compatibility rules for evolving protobuf schemas?",
  "<b>Safe</b>: add new fields, add new enum values, rename fields, add new messages/enums, make a singular field <code>repeated</code> (wire-compatible). <b>Unsafe</b>: change field numbers, change field types (unless wire-compatible), remove <code>reserved</code> fields still in use, change <code>optional</code> to <code>required</code> (proto2), rename packages (breaks code). <b>Wire-compatible type changes</b>: <code>int32↔uint32↔bool</code>, <code>sint32↔sint64</code>, <code>fixed32↔sfixed32</code>, <code>string↔bytes</code> (if UTF-8).",
  ["gotchas", "compatibility", "rules"])

c("Gotchas",
  "What is the difference between a nil message and a default instance?",
  "In proto3, accessing an unset message field returns a <b>default instance</b> (all fields at zero values) — not nil/null. This is a frequent source of bugs: you can call getters on it without null checks, but <code>has_field()</code> returns false. In proto2, unset optional message fields return null. Use <code>optional</code> keyword for explicit nil/null semantics.",
  ["gotchas", "nil", "default-instance"])

c("Gotchas",
  "What can go wrong with <code>google.protobuf.Any</code> serialization?",
  "1. The <code>type_url</code> must exactly match the receiving end's expectation — including the package prefix (<code>type.googleapis.com/</code> vs <code>type.example.com/</code>). 2. The embedded message might reference a schema version the receiver doesn't have. 3. Unpacking without type checking can crash. 4. The <code>@type</code> field in JSON mapping must be a fully qualified URL. 5. If the sender and receiver compile with different proto definitions, unpacking may silently produce garbage.",
  ["gotchas", "any", "serialization"])

c("Gotchas",
  "Does <code>google.protobuf.Timestamp</code> normalize timezones?",
  "No. Timestamp stores UTC epoch seconds+nano. The proto library normalizes to UTC on construction but doesn't retain the original timezone. This is usually fine — but if you need wall-clock time (e.g., \"9 AM local time regardless of DST\"), store timezone separately or use <code>google.type.TimeOfDay</code> / <code>google.type.DateTime</code> with <code>google.type.TimeZone</code>.",
  ["gotchas", "timestamp", "timezone"])

c("Gotchas",
  "What are the string encoding requirements?",
  "proto3 <code>string</code> fields must contain valid UTF-8 data. The protobuf runtime will enforce this (C++ debug builds assert, Java throws <code>Utf8</code>, Python 3 enforces by string type). If you need arbitrary bytes, use <code>bytes</code> type. <b>Note</b>: proto2 C++ had lax UTF-8 checking — migration to proto3 can surface encoding bugs.",
  ["gotchas", "string", "utf8"])

c("Gotchas",
  "Can protobuf handle binary data with null bytes?",
  "Yes, safely — protobuf uses length-delimited encoding for <code>string</code> and <code>bytes</code>. The length is stored before the data, so null bytes (<code>\\0</code>) don't terminate the field. However, if you pass a proto byte string to a C function that expects null-terminated strings, truncation may occur. Always use size-aware APIs.",
  ["gotchas", "binary", "null-bytes"])

c("Gotchas",
  "What is the 2GB message size limit?",
  "Before protobuf v26 (2024), protobuf had a hard 2GB (2<sup>31</sup>-1 bytes) limit on message size because sizes were tracked with 32-bit signed integers internally. Protobuf v26+ supports 64-bit sizes and can handle much larger messages (configured via <code>ParseContext</code> / C++ <code>io::CodedInputStream::SetTotalBytesLimit()</code>). Still, protobuf is designed for small-to-medium messages; for huge data, use streaming or chunking.",
  ["gotchas", "size-limit"])

c("Gotchas",
  "Can proto3 enums have negative values?",
  "Historically no — proto3 enums must be non-negative with the first value being 0. But with <b>proto editions 2023+</b>, enums can have negative values (using <code>features.enum_type = OPEN</code>). This allows representing error codes and status values more naturally. Proto3 editions with <code>OPEN</code> enum type remove the non-negative restriction.",
  ["gotchas", "enums", "negative"])

c("Gotchas",
  "What happens if you change a field's type from <code>int32</code> to <code>string</code>?",
  "This is a <b>wire-type incompatible</b> change. <code>int32</code> uses varint (wire type 0); <code>string</code> uses length-delimited (wire type 2). Old data written as int32 will be parsed with the wrong wire type, likely resulting in <b>parse errors</b> or silently skipped as unknown fields, causing data loss on re-serialization. Never change field types — create a new field number instead.",
  ["gotchas", "compatibility", "type-change"])

c("Gotchas",
  "What goes wrong when you remove a <code>reserved</code> field that's still in use?",
  "If you remove a <code>reserved</code> declaration and reuse the field number, old clients sending data with that number will have it misinterpreted as the new field type. This silently corrupts data. The purpose of <code>reserved</code> is to <b>permanently block</b> field number/name reuse — removing it defeats the entire point.",
  ["gotchas", "reserved"])

# ======================================================================
# L5 — EXPERT
# ======================================================================

c("Expert",
  "Proto2 vs Proto3 vs Editions — which should you choose for a new project in 2025?",
  "<b>Use editions</b> (e.g., <code>edition = \"2023\"</code>) for new projects. Editions offer: fine-grained feature control (field presence, enum behavior, encoding choices), no more forced proto2/proto3 dichotomy, and a path for future evolution. If editions tooling support is insufficient in your language (check <code>buf</code> support), use proto3 with explicit <code>optional</code> for nullable fields.",
  ["expert", "editions", "choice"])

c("Expert",
  "When is protobuf overkill?",
  "For small internal services with simple data, JSON or even query params can be simpler. If you don't need schema evolution (data is short-lived, services deploy together), the overhead of <code>.proto</code> files, code generation, and library dependencies isn't justified. If you need human readability more than performance. If your data is document-like (arbitrary nested JSON) — <code>google.protobuf.Struct</code> defeats the purpose.",
  ["expert", "overkill"])

c("Expert",
  "Why would you use FlatBuffers over protobuf for game development?",
  "FlatBuffers provides <b>zero-copy deserialization</b>: you access fields directly from the wire bytes without parsing. This eliminates deserialization latency and memory allocations — critical for game frames where every millisecond counts. FlatBuffers also supports storing serialized data in GPU buffers. Protobuf requires allocating and populating objects, which creates GC pressure and latency spikes.",
  ["expert", "games", "flatbuffers"])

c("Expert",
  "Why would you use Cap'n Proto over protobuf for performance?",
  "Cap'n Proto is <b>infinitely faster</b> for reads because it encodes data in a format that matches in-memory layout — you literally <code>mmap</code> the bytes and use pointers. No deserialization step at all. Zero-allocation reads. Encoding is also cheaper (just memory layout). Trade-off: larger wire size (no varints, 8-byte alignment), smaller ecosystem, no official Google support.",
  ["expert", "performance", "capnp"])

c("Expert",
  "How does protobuf work with Kafka and event sourcing?",
  "Kafka messages are byte arrays — protobuf serializes to bytes efficiently. Patterns: <b>1.</b> Use protobuf as the envelope + payload format for events. <b>2.</b> Store the schema version (or fingerprint) in the message header for schema registry lookup. <b>3.</b> Use <code>google.protobuf.Any</code> for polymorphic event types. <b>4.</b> Evolve event schemas using only backward-compatible changes. <b>5.</b> Use Confluent Schema Registry or BSR for schema governance.",
  ["expert", "kafka", "event-sourcing"])

c("Expert",
  "What are schema design best practices for evolvable protobuf schemas?",
  "<b>1.</b> Reserve field numbers for deleted fields — never reuse. <b>2.</b> Use <code>optional</code> for all fields that might be added later (or removed). <b>3.</b> Prefer <code>string</code> IDs over enums for extensibility. <b>4.</b> Wrap scalars in separate messages for future expansion. <b>5.</b> Use <code>oneof</code> for mutually exclusive states. <b>6.</b> Version packages: <code>my.service.v1</code>, <code>my.service.v2</code>. <b>7.</b> Write a compatibility test (serialize v1, deserialize v2, reserialize, compare).",
  ["expert", "schema-design", "compatibility"])

c("Expert",
  "Monorepo vs distributed proto repositories — what are the tradeoffs?",
  "<b>Monorepo</b>: all protos in one repo — easy to make coordinated changes, simple import paths, atomic commits. But: harder to version independently, CI gets slower at scale, tight coupling. <b>Distributed</b>: each service owns its protos — independent versioning (semver), decoupled release cycles, but: harder to make cross-service changes, dependency hell if not managed carefully. Use BSR or similar registry in distributed model.",
  ["expert", "monorepo", "repository"])

c("Expert",
  "Code generation vs runtime reflection — when to use which?",
  "<b>Code generation</b>: type-safe, fast, compile-time checks, IDE support, smaller binary. Best for production RPC services. <b>Runtime reflection</b>: flexible, no code gen step, can process messages defined at runtime. Best for tools (debuggers, proxies, generic serializers), config-driven pipelines, and platforms that process user-defined schemas. Can be 10-100× slower than generated code.",
  ["expert", "codegen", "reflection"])

c("Expert",
  "Buf vs protoc ecosystem — what are the key differences?",
  "<b>protoc</b>: the canonical compiler, very stable, ships with <code>google/protobuf/</code> includes, plugins via PATH convention. Minimal — just compiles. <b>Buf</b>: wraps protoc but adds: linting, formatting, breaking change detection (critical for CI), BSR schema registry, simpler config (<code>buf.yaml</code> vs long CLI), remote plugins (no local protoc install needed), and a plugin ecosystem. Buf is the modern standard for new projects.",
  ["expert", "buf", "protoc"])

c("Expert",
  "How do <code>google.api.http</code> annotations compare to OpenAPI?",
  "<code>google.api.http</code> annotations let you define REST/JSON transcoding directly on gRPC service methods: <pre>rpc GetBook(GetBookRequest) returns (Book) {\n  option (google.api.http) = {\n    get: \"/v1/{name=books/*}\"\n  };\n}</pre>OpenAPI is a separate spec for REST APIs. The Google approach: define in protobuf, generate both gRPC and REST (via gRPC-Gateway / <code>google.api.HttpRule</code>). OpenAPI is broader (authentication, servers) but decoupled from implementation.",
  ["expert", "google.api.http", "openapi"])

c("Expert",
  "What is protobuf edition 2023 — key features?",
  "Replaces <code>syntax = \"proto3\"</code> with <code>edition = \"2023\"</code>. Introduces <b>features</b>: <code>field_presence</code> (EXPLICIT/IMPLICIT/LEGACY_REQUIRED), <code>enum_type</code> (OPEN/CLOSED), <code>repeated_field_encoding</code> (PACKED/EXPANDED), <code>message_encoding</code>, <code>json_format</code>. Features can be set file-wide or per-field. Editions enable evolving the language without new <code>syntax</code> declarations.",
  ["expert", "editions", "2023"])

c("Expert",
  "How do you handle schema versioning for long-lived data (years)?",
  "<b>1.</b> Never delete fields — only mark as <code>reserved</code>. <b>2.</b> Avoid enums for taxonomies that change (use <code>string</code>). <b>3.</b> Wrap any field that might need sub-fields in a message (message wrapping enables <code>optional</code>). <b>4.</b> Use <code>int64</code> for sizes/counts even if <code>int32</code> seems sufficient today. <b>5.</b> Test round-trip compatibility in CI with golden serialized data from production.",
  ["expert", "versioning", "compatibility"])

# ======================================================================
# L6 — INNOVATION / CUSTOM PLUGINS & ADVANCED USE CASES
# ======================================================================

c("Expert",
  "How do you build a custom protoc plugin?",
  "A protoc plugin reads a <code>CodeGeneratorRequest</code> (serialized proto) from stdin and writes a <code>CodeGeneratorResponse</code> to stdout. The plugin is invoked via <code>--custom_out=...</code> on the protoc command line. Key types: <code>google.protobuf.compiler.CodeGeneratorRequest</code> with <code>FileDescriptorProto</code> for each file, <code>CodeGeneratorResponse</code> with <code>File</code> entries for generated output files.",
  ["expert", "protoc", "plugins", "custom"])

c("Expert",
  "Write a minimal custom protoc plugin pseudocode.",
  "<pre># Read CodeGeneratorRequest from stdin\nrequest = CodeGeneratorRequest.FromString(sys.stdin.buffer.read())\n\nfor proto_file in request.proto_file:\n    for message in proto_file.message_type:\n        content = generate_code(proto_file, message)\n        response.file.add(\n            name=output_filename,\n            content=content\n        )\n\n# Write CodeGeneratorResponse to stdout\nsys.stdout.buffer.write(response.SerializeToString())</pre>",
  ["expert", "protoc", "plugins", "code"])

c("Expert",
  "How do you use protobuf without code generation (dynamic messages)?",
  "<pre>import google.protobuf.descriptor_pb2 as desc\nimport google.protobuf.message_factory\n\n# Build descriptor dynamically\nfile_desc = desc.FileDescriptorProto()\nfile_desc.name = \"dynamic.proto\"\nfile_desc.package = \"dynamic\"\nmsg_desc = file_desc.message_type.add()\nmsg_desc.name = \"DynamicMessage\"\nfield = msg_desc.field.add()\nfield.name = \"id\"\nfield.number = 1\nfield.type = desc.FieldDescriptorProto.TYPE_INT32\n\n# Build FileDescriptor from proto\npool = descriptor_pool.Default()\npool.Add(file_desc)\n\n# Create message factory\nfactory = message_factory.MessageFactory(pool=pool)\nmsg_class = factory.GetPrototype(pool.FindMessageTypeByName(\"dynamic.DynamicMessage\"))\n\n# Use like normal\nmsg = msg_class()\nmsg.id = 42\ndata = msg.SerializeToString()</pre>",
  ["expert", "dynamic", "no-codegen"])

c("Expert",
  "What is nanopb and when would you use it?",
  "nanopb is a lightweight protobuf implementation for embedded systems. It uses a C code generator that produces small, static-memory code with no dynamic allocation. Configuration is via <code>.options</code> files: max sizes, fixed array limits, callback-based encoding/decoding for large fields. Ideal for microcontrollers (Arduino, STM32, ESP32) where standard protobuf C++ is too heavy. Protocol: <code>https://github.com/nanopb/nanopb</code>.",
  ["expert", "embedded", "nanopb"])

c("Expert",
  "Can protobuf be used as a config file format? Why or why not?",
  "<b>Yes</b>, but with caveats. Pros: type-safe, schema-validated, cross-language, easier to generate programmatically. Cons: binary format not human-editable (use text format <code>TextFormat::Print</code> for debugging), no comments in binary, schema must be compiled before use. Use protobuf text format (<code>.textproto</code>) as a human-readable alternative: it supports comments and looks like JSON with field names.",
  ["expert", "config", "textproto"])

c("Expert",
  "How is protobuf used in game networking?",
  "<b>1.</b> Define game messages (player state, actions, events) in <code>.proto</code> files. <b>2.</b> Compile to C++/C# for engine integration. <b>3.</b> Serialize game state deltas as binary protobuf over UDP/TCP. <b>4.</b> Use <code>repeated</code> fields for entity arrays with packed encoding. <b>5.</b> Use <code>oneof</code> for action/event type dispatching. <b>6.</b> Consider FlatBuffers for latency-critical paths (frame data), protobuf for slower RPC-style communication (matchmaking, chat).",
  ["expert", "gamedev", "networking"])

c("Expert",
  "How do you build a protobuf schema registry?",
  "A schema registry stores versioned <code>.proto</code> files or <code>FileDescriptorSet</code>s and serves them to producers/consumers. Key capabilities: <b>1.</b> Register new schema version (validate compatibility with previous). <b>2.</b> Lookup schema by subject+version. <b>3.</b> Serve JSON-to-protobuf and protobuf-to-JSON conversion using the schema. <b>4.</b> Integrate with Kafka/event systems (Confluent-style). Build it on BSR, or DIY with a database of <code>FileDescriptorProto</code>s.",
  ["expert", "schema-registry"])

c("Expert",
  "What custom proto lint rules might you write?",
  "Common custom lint rules: <b>1.</b> Enforce field naming conventions (e.g., <code>snake_case</code> with specific prefixes). <b>2.</b> Prevent certain types (e.g., no <code>double</code> for monetary values). <b>3.</b> Enforce <code>reserved</code> declaration for removed fields (Auto-reserve). <b>4.</b> Check that all messages have <code>reserved</code> blocks for historic field numbers. <b>5.</b> Validate <code>go_package</code> / <code>java_package</code> matches directory structure. <b>6.</b> Ban deprecated fields from being used in new messages.",
  ["expert", "lint", "custom"])

c("Expert",
  "Describe building a protobuf-based data pipeline.",
  "<pre>Ingestion → protobuf → Kafka/stream → consumers → storage\n\n1. Define data models as .proto files (source of truth).\n2. Ingest data and serialize as protobuf (compact, fast).\n3. Stream through Kafka (binary bytes).\n4. Consumers deserialize with the SAME schema version.\n5. Transform: deserialize v1 → convert → serialize v2.\n6. Store in columnar format (Parquet) with protobuf schema.\n7. Use schema registry to track compatibility across pipeline stages.</pre>Benefits: type safety end-to-end, no parsing ambiguities, small wire overhead.",
  ["expert", "data-pipeline"])

c("Expert",
  "What is <code>google.protobuf.compiler.CodeGeneratorRequest</code>?",
  "A protobuf message type (defined in <code>plugin.proto</code>) that protoc sends to plugins via stdin. Contains: the parsed <code>FileDescriptorProto</code> for each file to generate, file-to-generate list, compiler version, and any plugin parameters. Plugins read this, generate code, and write <code>CodeGeneratorResponse</code> to stdout with generated file contents.",
  ["expert", "protoc", "plugins", "api"])

c("Expert",
  "What is the protobuf text format (<code>.textproto</code>)?",
  "<pre># example.textproto\nname: \"Alice\"\nage: 30\nemails: \"alice@example.com\"\nemails: \"alice@work.com\"\naddress {\n  street: \"123 Main\"\n  city: \"Springfield\"\n}</pre>A human-readable text representation of protobuf messages. Supports comments, multi-line strings, and the same structure as binary. Use <code>TextFormat::Print()</code> / <code>Parse()</code> in C++, <code>text_format</code> module in Python. Common for config files, test fixtures, and debugging.",
  ["expert", "textproto", "format"])

c("Expert",
  "How does protobuf edition <code>field_presence</code> feature work?",
  "<pre>edition = \"2023\";\n\nmessage Example {\n  int32 implicit_field = 1;  // IMPLICIT (default): no has_ method\n  int32 explicit_field = 2 [features.field_presence = EXPLICIT];  // has_ method\n  int32 required_field = 3 [features.field_presence = LEGACY_REQUIRED];  // must be set\n}</pre><b>IMPLICIT</b>: no tracking of unset vs zero (proto3 default). <b>EXPLICIT</b>: tracks presence (like proto3 <code>optional</code>). <b>LEGACY_REQUIRED</b>: sets the required bit (like proto2 <code>required</code>). This is the editions replacement for proto2/proto3 label semantics.",
  ["expert", "editions", "field-presence"])

c("Expert",
  "How do you implement a cross-platform serialization layer with protobuf?",
  "<b>1.</b> Define canonical <code>.proto</code> files — single source of truth. <b>2.</b> Generate code for each platform (C++ for server, Java for Android, Swift for iOS, JS for web). <b>3.</b> Use protobuf as the wire format between all services. <b>4.</b> Use gRPC or REST+JSON transcoding for APIs. <b>5.</b> For client-side local storage, serialize protobuf to <code>bytes</code> (not JSON) for efficiency. <b>6.</b> Use <code>protoc</code> or <code>buf generate</code> in CI to regenerate code on schema changes.",
  ["expert", "cross-platform"])

c("Expert",
  "What does <code>option allow_alias = true</code> do in enums?",
  "<pre>enum Status {\n  option allow_alias = true;\n  UNKNOWN = 0;\n  STARTED = 1;\n  RUNNING = 1;  // alias for STARTED — valid with allow_alias\n}</pre>Without this option, duplicate enum values cause a compile error. With it, multiple names can share the same numeric value. Useful for maintaining backward compatibility when renaming enum values — keep the old name as an alias. <b>proto2 only</b>; proto3 doesn't support aliases (editions OPEN enums are more flexible).",
  ["expert", "enums", "aliases"])

c("Expert",
  "How does <code>google.protobuf.util.JsonFormat</code> handle default values?",
  "By default, proto3 JSON output <b>omits</b> fields with default values (0, empty string, false) — only non-default fields are printed. You can configure: <code>JsonPrintOptions.always_print_primitive_fields = true</code> to include all fields. For parsing: <code>JsonParseOptions.ignore_unknown_fields = true</code> to tolerate unknown JSON fields. This behavior matches the proto3 JSON spec but differs from proto2.",
  ["expert", "json", "format"])

c("Expert",
  "What is the protobuf <code>--descriptor_set_out</code> flag?",
  "<pre>protoc --descriptor_set_out=foo.pb --include_imports foo.proto</pre>Serializes the parsed <code>FileDescriptorSet</code> (all compiled proto files with their descriptors) to a binary file. This enables <b>self-describing</b>: you can reconstruct the schema from the binary alone. Used by: <code>grpc_cli</code> for reflection, dynamically loading schemas, schema registries, and tools that need to interpret protobuf without access to <code>.proto</code> source files.",
  ["expert", "descriptor-set", "self-describing"])

c("Expert",
  "How do you debug protobuf serialization issues?",
  "<b>1.</b> Dump raw: <code>protoc --decode_raw &lt; message.bin</code> shows field-level breakdown. <b>2.</b> Decode with schema: <code>protoc --decode=pkg.Msg schema.proto &lt; data.bin</code>. <b>3.</b> Compare binary with <code>xxd</code> to inspect wire format. <b>4.</b> Use <code>TextFormat::Print</code> in code for human-readable debug output. <b>5.</b> Check <code>has_field()</code> (explicit optional) vs value == 0 (implicit). <b>6.</b> Verify <code>type.googleapis.com</code> prefix for <code>Any</code> fields. <b>7.</b> Use <code>buf breaking</code> to catch wire-incompatible schema changes.",
  ["expert", "debugging", "troubleshooting"])

# ======================================================================
# BUILD
# ======================================================================

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
