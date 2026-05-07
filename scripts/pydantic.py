import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Pydantic"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "Models":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Models-Fields"),
    "Validators":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Validators"),
    "Serialization":genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Serialization"),
    "Types":        genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Advanced-Types"),
    "Config":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Model-Config"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ═══════════════════════════════════════════
# 01 — FUNDAMENTALS
# ═══════════════════════════════════════════

c("Fundamentals",
  "What is Pydantic?",
  "Pydantic is a <b>data validation library</b> for Python that uses <b>type annotations</b> to define schemas.<br><br>Core capabilities:<br>• <b>Validation</b> — ensures data matches the schema<br>• <b>Coercion</b> — converts compatible types (e.g. <code>\"123\"</code> → <code>123</code>)<br>• <b>Serialization</b> — exports models to <code>dict</code> / JSON<br>• <b>JSON Schema</b> — generates JSON Schema from models<br><br>Powered by <code>pydantic-core</code> (Rust) in V2.",
  ["L0-primitives"])

c("Fundamentals",
  "What is the core class in Pydantic that models inherit from?",
  "<code>BaseModel</code><br><br><code>from pydantic import BaseModel<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int</code><br><br>Inheriting from <code>BaseModel</code> gives you validation, serialization, and JSON schema generation for free.",
  ["L0-primitives"])

c("Fundamentals",
  "How do type annotations act as a schema in Pydantic?",
  "Field types define the <b>schema</b> — Pydantic reads the type hints at runtime and uses them to:<br><br>• <b>Validate</b> incoming data against the declared type<br>• <b>Coerce</b> compatible values (e.g. <code>\"42\"</code> → <code>42</code> for an <code>int</code> field)<br>• <b>Generate JSON Schema</b> automatically<br>• <b>Provide editor autocompletion</b> via static analysis<br><br>No separate schema definition needed — the Python types <i>are</i> the schema.",
  ["L0-primitives"])

c("Fundamentals",
  "What is the validation flow in Pydantic V2?",
  "<b>1. Parse</b> — Raw input (dict, JSON string, ORM object) is read<br><b>2. Validate</b> — Each field is checked against its type and constraints<br><b>3. Coerce</b> — Compatible types are converted (e.g. <code>str</code> → <code>int</code>) if not in strict mode<br><b>4. Python object</b> — A validated model instance is returned<br><br>The parse+validate+coerce steps happen in <code>pydantic-core</code> (Rust), making V2 significantly faster than V1.",
  ["L0-primitives"])

c("Fundamentals",
  "Why use Pydantic over dataclasses?",
  "<b>Pydantic advantages over <code>@dataclass</code>:</b><br><br>• <b>Automatic validation</b> — dataclasses don't validate types at runtime<br>• <b>Coercion</b> — <code>\"123\"</code> automatically becomes <code>123</code> for <code>int</code> fields<br>• <b>Nested validation</b> — nested dicts automatically become nested models<br>• <b>JSON Schema</b> — built-in <code>.model_json_schema()</code><br>• <b>Serialization</b> — <code>.model_dump()</code> / <code>.model_dump_json()</code><br>• <b>Aliases, defaults, constraints</b> — declarative via <code>Field()</code><br><br>Dataclasses are lighter-weight but lack built-in data validation.",
  ["L0-primitives"])

c("Fundamentals",
  "Why use Pydantic over namedtuples?",
  "<b>Pydantic vs <code>NamedTuple</code>:</b><br><br>• NamedTuples are immutable by default (Pydantic can be too via <code>frozen=True</code>)<br>• NamedTuples are lightweight but have <b>no validation</b> — you can put wrong types in fields<br>• NamedTuples don't support nested model validation<br>• NamedTuples have no JSON Schema generation<br>• NamedTuples have no alias system, custom validators, or serialization hooks<br><br>Use NamedTuple for simple, performance-critical data carriers. Use Pydantic when you need guarantees about data shape.",
  ["L0-primitives"])

c("Fundamentals",
  "What changed in Pydantic V2 vs V1?",
  "<b>V1 → V2 key changes:</b><br><br>• Core rewritten in <b>Rust</b> (<code>pydantic-core</code>) — 5-50x faster validation<br>• <code>.dict()</code> replaced by <code>.model_dump()</code><br>• <code>.json()</code> replaced by <code>.model_dump_json()</code><br>• <code>.schema()</code> replaced by <code>.model_json_schema()</code><br>• <code>.parse_obj()</code> replaced by <code>.model_validate()</code><br>• <code>.parse_raw()</code> replaced by <code>.model_validate_json()</code><br>• <code>@validator</code> split into <code>@field_validator</code> and <code>@model_validator</code><br>• <code>__fields__</code> replaced by <code>model_fields</code><br>• <code>Config</code> inner class replaced by <code>model_config = ConfigDict(...)</code><br>• <code>Annotated</code>-style validators as first-class pattern",
  ["L0-primitives"])

c("Fundamentals",
  "What is pydantic-core?",
  "<b><code>pydantic-core</code></b> is the Rust-based validation engine that powers Pydantic V2.<br><br>It provides:<br>• ~5-50x faster validation than V1<br>• Core schema validation logic written in Rust<br>• Python bindings via PyO3<br>• Separate package (<code>pydantic-core</code>) installed as a dependency<br><br>Most users never interact with it directly, but it handles all the heavy lifting behind <code>BaseModel</code>.",
  ["L0-primitives"])

c("Fundamentals",
  "What happens when you call <code>User(name='Alice', age=30)</code>?",
  "Pydantic V2 executes this flow:<br><br>1. The <code>__init__</code> (auto-generated by the metaclass) receives kwargs<br>2. Kwargs are passed to <code>pydantic-core</code>'s validator<br>3. Core parser validates <code>name</code> is <code>str</code> and <code>age</code> is <code>int</code><br>4. If valid, a Python <code>User</code> instance is returned<br>5. If invalid, a <code>ValidationError</code> is raised<br><br>All model creation goes through validation — there is no way to bypass it (by design).",
  ["L0-primitives"])

c("Fundamentals",
  "What is coercion in Pydantic and when does it happen?",
  "<b>Coercion</b> (a.k.a. casting/parsing) is automatic type conversion during validation.<br><br>Examples of coercion (default mode):<br>• <code>\"123\"</code> → <code>123</code> for <code>int</code> fields<br>• <code>\"true\"</code> → <code>True</code> for <code>bool</code> fields<br>• <code>1</code> → <code>1.0</code> for <code>float</code> fields<br>• <code>\"2024-01-01T00:00:00\"</code> → <code>datetime</code> object<br><br>Coercion is <b>enabled by default</b>. Use <b>strict mode</b> (<code>model_validate(..., strict=True)</code>) to disable it.",
  ["L0-primitives"])

c("Fundamentals",
  "What is the difference between strict and lax (default) validation?",
  "<b>Lax (default):</b> Pydantic will <b>coerce</b> compatible types<br>• <code>int</code> field accepts <code>\"42\"</code> (string → int)<br>• <code>bool</code> field accepts <code>\"yes\"</code><br><br><b>Strict:</b> No coercion — types must match exactly<br>• <code>int</code> field rejects <code>\"42\"</code><br>• Use <code>model_validate(data, strict=True)</code> or <code>model_validate_json(json_str, strict=True)</code><br><br>Strict mode is useful for API boundaries where you want to reject ambiguous input.",
  ["L0-primitives"])

c("Fundamentals",
  "What is the difference between <code>model_validate()</code> and <code>model_validate_json()</code>?",
  "<code>model_validate(obj)</code> — validates a <b>Python dict/object</b> (already deserialized)<br><br><code>model_validate_json(json_str)</code> — parses a <b>JSON string</b> first, then validates<br><br>Both return a validated model instance. Both accept <code>strict=True</code> to disable coercion.<br><br><code>model_validate_json()</code> is equivalent to:<br><code>model.model_validate(json.loads(json_str))</code><br>but more efficient (the JSON parsing is integrated into the Rust validator).",
  ["L0-primitives"])

c("Fundamentals",
  "What is the Pydantic ecosystem? (Packages beyond core)",
  "<b>Core ecosystem packages:</b><br><br>• <code>pydantic</code> — core library (BaseModel, validators, types)<br>• <code>pydantic-settings</code> — <code>BaseSettings</code> for env vars / .env files<br>• <code>pydantic-extra-types</code> — additional field types (Color, PaymentCardNumber, etc.)<br>• <code>pydantic-core</code> — Rust validation engine (installed automatically)<br>• <code>pydantic[email]</code> — email validation extras<br>• <code>pydantic[timezone]</code> — timezone-aware datetime extras<br><br>Install: <code>pip install pydantic[email,timezone]</code>",
  ["L0-primitives"])

c("Fundamentals",
  "How does Pydantic compare to marshmallow and cattrs?",
  "<b>Pydantic vs marshmallow:</b><br>• Pydantic uses type annotations; marshmallow uses explicit Schema classes<br>• Pydantic is faster (Rust core in V2)<br>• Pydantic has better IDE support (type hints)<br>• Marshmallow has more serialization formats (e.g., BSON)<br><br><b>Pydantic vs cattrs:</b><br>• Both use type annotations for schema definition<br>• Pydantic is more feature-rich (JSON Schema, aliases, strict mode)<br>• cattrs is lighter-weight and more customizable<br>• cattrs is better for structuring/unstructuring arbitrary classes<br><br>Pydantic is the standard choice for FastAPI and modern Python APIs.",
  ["L0-primitives"])

c("Fundamentals",
  "What is the difference between validation, parsing, and serialization in Pydantic?",
  "<b>Validation:</b> Checking that data conforms to the expected types and constraints. Raises <code>ValidationError</code> on failure.<br><br><b>Parsing (Coercion):</b> Converting input data to the target Python type (e.g., <code>\"123\"</code> → <code>123</code>). Happens during validation in lax mode.<br><br><b>Serialization:</b> Converting a model instance back to a portable format (<code>dict</code>, JSON). Handled by <code>model_dump()</code> / <code>model_dump_json()</code>.<br><br>In Pydantic V2, parsing + validation are integrated in the Rust core. Serialization is a separate pass.",
  ["L0-primitives"])

c("Fundamentals",
  "How does Pydantic handle data coming from CLI arguments or environment variables?",
  "For CLI args (argparse/click) and env vars, Pydantic is ideal for validation after parsing raw strings:<br><br><code>import os<br>from pydantic import BaseModel<br><br>class Config(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;host: str<br>&nbsp;&nbsp;&nbsp;&nbsp;port: int<br><br>raw = {'host': os.getenv('HOST', 'localhost'), 'port': os.getenv('PORT', '8000')}<br>config = Config.model_validate(raw)  # '8000' coerced to 8000</code><br><br>For structured settings, use <code>pydantic-settings</code> (<code>BaseSettings</code>) which reads env vars, <code>.env</code> files, secret dirs, and CLI args natively. Pydantic core handles the coercion of string env vars to typed fields automatically.",
  ["L0-primitives"])

# ═══════════════════════════════════════════
# 02 — MODELS & FIELDS
# ═══════════════════════════════════════════

c("Models",
  "How do you define a basic Pydantic model?",
  "<code>from pydantic import BaseModel<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br>&nbsp;&nbsp;&nbsp;&nbsp;email: str<br><br>user = User(name='Alice', age=30, email='a@b.com')</code><br><br>Each type-annotated class attribute becomes a validated field. Missing required fields raise <code>ValidationError</code>.",
  ["L1-mechanics"])

c("Models",
  "What built-in field types does Pydantic support?",
  "Common built-in types:<br><br>• <code>str</code>, <code>int</code>, <code>float</code>, <code>bool</code>, <code>bytes</code><br>• <code>datetime</code>, <code>date</code>, <code>time</code>, <code>timedelta</code><br>• <code>UUID</code> — validates UUID strings<br>• <code>Decimal</code> — precise decimal numbers<br>• <code>Path</code> / <code>FilePath</code> / <code>DirectoryPath</code> — filesystem paths<br>• <code>AnyUrl</code>, <code>HttpUrl</code>, <code>FileUrl</code> — URL validation<br>• <code>EmailStr</code> — requires <code>pip install pydantic[email]</code><br>• <code>IPvAnyAddress</code>, <code>IPvAnyInterface</code>, <code>IPvAnyNetwork</code><br>• <code>Enum</code>, <code>IntEnum</code>, <code>StrEnum</code><br>• <code>SecretStr</code>, <code>SecretBytes</code> — sensitive data (masked in repr)",
  ["L1-mechanics"])

c("Models",
  "What is <code>Field()</code> and what can it configure?",
  "<code>from pydantic import BaseModel, Field<br><br>class Product(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str = Field(min_length=1, max_length=100)<br>&nbsp;&nbsp;&nbsp;&nbsp;price: float = Field(gt=0, le=9999.99)<br>&nbsp;&nbsp;&nbsp;&nbsp;tags: list[str] = Field(default_factory=list)</code><br><br><b>Common Field() arguments:</b><br>• <code>default</code> — static default value<br>• <code>default_factory</code> — callable producing default (for mutable types!)<br>• <code>alias</code> — alternative field name in input data<br>• <code>title</code>, <code>description</code> — metadata for JSON Schema<br>• <code>gt</code>, <code>ge</code>, <code>lt</code>, <code>le</code> — numeric constraints<br>• <code>min_length</code>, <code>max_length</code> — string/list length<br>• <code>pattern</code> — regex for strings<br>• <code>examples</code> — example values for JSON Schema<br>• <code>frozen</code> — prevent mutation after creation",
  ["L1-mechanics"])

c("Models",
  "Why should you use <code>default_factory</code> instead of a mutable default?",
  "<code>class Bad(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;items: list[str] = []  # BUG: shared across all instances!<br><br>class Good(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;items: list[str] = Field(default_factory=list)  # Correct</code><br><br>Mutable defaults (<code>[]</code>, <code>{}</code>, <code>set()</code>) are evaluated once at class definition time and <b>shared across all instances</b>. <code>default_factory</code> calls a function for each new instance, giving each its own copy.",
  ["L1-mechanics"])

c("Models",
  "How do field aliases work in Pydantic?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;first_name: str = Field(alias='firstName')<br><br>user = User(firstName='Alice')  # Use alias on input<br>print(user.first_name)          # Access by field name<br>print(user.model_dump(by_alias=True))  # {'firstName': 'Alice'}</code><br><br>Aliases map external names to internal Python field names. Use <code>by_alias=True</code> when serializing to output the alias name instead.",
  ["L1-mechanics"])

c("Models",
  "How do you create nested models in Pydantic?",
  "<code>class Address(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;street: str<br>&nbsp;&nbsp;&nbsp;&nbsp;city: str<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;address: Address  # Nested model<br><br>user = User(name='Alice', address={'street': '123 Main', 'city': 'NYC'})<br># address is automatically converted to Address instance</code><br><br>Dicts are automatically validated and converted to nested model instances. Validation recurses into nested models.",
  ["L1-mechanics"])

c("Models",
  "How do you define optional fields in Pydantic?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;bio: str | None = None   # Optional with default<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int | None = None     # Optional with default<br><br>class User2(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;bio: str | None  # Optional BUT required in input!</code><br><br><b>Important:</b> <code>str | None</code> without a default means the field <b>must be provided</b> (but can be <code>None</code>). To make it truly optional, provide a default: <code>= None</code>.<br><br>In V2, <code>Optional[str]</code> and <code>str | None</code> are equivalent.",
  ["L1-mechanics"])

c("Models",
  "How do you create recursive (self-referencing) models?",
  "<code>from __future__ import annotations<br><br>class Category(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;subcategories: list[Category] = []<br><br>Category.model_rebuild()  # Required for recursive types</code><br><br>Use <code>from __future__ import annotations</code> to enable forward references. Call <code>.model_rebuild()</code> after class definition to resolve the recursive type. Without it, Pydantic can't resolve the forward reference.",
  ["L1-mechanics"])

c("Models",
  "What are computed fields?",
  "<code>from pydantic import BaseModel, computed_field<br><br>class Rectangle(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;width: float<br>&nbsp;&nbsp;&nbsp;&nbsp;height: float<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@computed_field<br>&nbsp;&nbsp;&nbsp;&nbsp;@property<br>&nbsp;&nbsp;&nbsp;&nbsp;def area(self) -&gt; float:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return self.width * self.height</code><br><br>Computed fields:<br>• Marked with <code>@computed_field</code><br>• Must also be decorated with <code>@property</code><br>• Included in <code>model_dump()</code> and JSON Schema<br>• Their values are calculated, not stored<br>• Can have <code>alias</code>, <code>title</code>, <code>description</code>, <code>return_type</code>",
  ["L1-mechanics"])

c("Models",
  "What are private fields vs <code>ClassVar</code> in Pydantic?",
  "<code>from typing import ClassVar<br>from pydantic import BaseModel<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;_cache: dict = {}  # Private (underscore) — not a field<br>&nbsp;&nbsp;&nbsp;&nbsp;TABLE_NAME: ClassVar[str] = 'users'  # ClassVar — not a field</code><br><br>• <b>Private fields</b> (<code>_prefix</code>): Names starting with underscore are ignored by the model — no validation, not in <code>model_dump()</code><br>• <b><code>ClassVar</code></b>: Typed as a class variable (not instance field). Pydantic ignores it. Useful for constants shared across all instances.",
  ["L1-mechanics"])

c("Models",
  "What is <code>model_copy()</code> and when is it useful?",
  "<code>user = User(name='Alice', age=30)<br>updated = user.model_copy(update={'age': 31})<br># updated is a new User(name='Alice', age=31)<br># original user is unchanged (age still 30)<br><br>shallow = user.model_copy(deep=False)  # Shallow copy<br>deep = user.model_copy(deep=True)       # Deep copy</code><br><br><code>model_copy()</code> creates a new instance with optional field updates. It goes through validation again (unlike using <code>copy.copy()</code>). <code>deep=True</code> recursively copies nested models.",
  ["L1-mechanics"])

c("Models",
  "What is <code>model_fields</code> and <code>model_computed_fields</code>?",
  "<code>print(User.model_fields)<br># {'name': FieldInfo(...), 'age': FieldInfo(...)}<br><br>print(User.model_computed_fields)<br># {'area': ComputedFieldInfo(...)}</code><br><br><code>model_fields</code> — dict of all regular fields with their <code>FieldInfo</code> metadata<br><code>model_computed_fields</code> — dict of all <code>@computed_field</code> properties<br><br>These replace V1's <code>__fields__</code> attribute. Useful for introspection, dynamic model building, and field metadata access.",
  ["L1-mechanics"])

c("Models",
  "How do you make a field immutable (frozen at field level)?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;id: int = Field(frozen=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str  # Mutable<br><br>user = User(id=1, name='Alice')<br>user.name = 'Bob'  # OK<br>user.id = 2        # Raises ValidationError</code><br><br><code>Field(frozen=True)</code> prevents mutation of a specific field after model creation, even if the model itself is not frozen. This is per-field immutability, distinct from <code>model_config = ConfigDict(frozen=True)</code> which freezes the entire model.",
  ["L1-mechanics"])

c("Models",
  "What is <code>model_dump()</code> and what are its key parameters?",
  "<code>user.model_dump()</code> — returns a <code>dict</code><br><br>Key parameters:<br>• <code>include</code> — set of field names to include<br>• <code>exclude</code> — set of field names to exclude<br>• <code>by_alias</code> — use field aliases as keys (default <code>False</code>)<br>• <code>exclude_unset</code> — omit fields that weren't explicitly set<br>• <code>exclude_defaults</code> — omit fields equal to their default<br>• <code>exclude_none</code> — omit <code>None</code> values<br>• <code>round_trip</code> — ensure output can be passed back to <code>model_validate()</code><br>• <code>mode</code> — <code>'python'</code> or <code>'json'</code> (converts to JSON-compatible types)",
  ["L1-mechanics"])

c("Models",
  "How does <code>round_trip=True</code> affect <code>model_dump()</code>?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;created: datetime<br><br>data = user.model_dump()           # {'created': datetime(2024,1,1)}<br>data = user.model_dump(round_trip=True)  # {'created': '2024-01-01T00:00:00'}<br><br># With round_trip=True, output can be passed directly to model_validate()<br>User.model_validate(user.model_dump(round_trip=True))  # Works!</code><br><br><code>round_trip=True</code> serializes values in a way that <code>model_validate()</code> can parse them back. It's equivalent to <code>mode='json'</code> plus flags to include all needed data.",
  ["L1-mechanics"])

c("Models",
  "What is the <code>model_dump()</code> <code>mode</code> parameter?",
  "<code>model_dump(mode='python')  # Default: Python-native types<br># {'id': UUID('...'), 'created': datetime(2024,1,1)}<br><br>model_dump(mode='json')    # JSON-compatible types<br># {'id': '550e8400-...', 'created': '2024-01-01T00:00:00'}</code><br><br><code>mode='json'</code> converts non-JSON-serializable types (datetime, UUID, Decimal, etc.) to JSON-compatible representations. It's equivalent to what <code>model_dump_json()</code> does internally before JSON encoding.",
  ["L1-mechanics"])

c("Models",
  "How do <code>include</code> and <code>exclude</code> work in <code>model_dump()</code>?",
  "<code>user = User(name='Alice', age=30, email='a@b.com')<br><br>user.model_dump(include={'name', 'email'})<br># {'name': 'Alice', 'email': 'a@b.com'}<br><br>user.model_dump(exclude={'email'})<br># {'name': 'Alice', 'age': 30}<br><br># Can use nested dicts for nested models:<br>user.model_dump(include={'name', 'address': {'city'}})</code><br><br>Use sets for top-level fields and dicts for nested model fields. Cannot use <code>include</code> and <code>exclude</code> together.",
  ["L1-mechanics"])

c("Models",
  "What is <code>model_post_init()</code> and when do you use it?",
  "<code>from pydantic import BaseModel, model_post_init<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;first_name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;last_name: str<br><br>&nbsp;&nbsp;&nbsp;&nbsp;def model_post_init(self, __context):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.full_name = f\"{self.first_name} {self.last_name}\"<br><br>user = User(first_name='Alice', last_name='Smith')<br>print(user.full_name)  # 'Alice Smith'</code><br><br><code>model_post_init()</code> is called after the model is fully validated and initialized. Perfect for derived attributes, caching, or logging. Replaces V1's <code>__init__</code> override pattern. Note: this attribute is NOT a Pydantic field (not validated, not serialized by default).",
  ["L1-mechanics"])

c("Models",
  "How do you exclude a field from JSON Schema but keep it validated?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;password: str = Field(exclude=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;internal_id: str = Field(json_schema_extra={'exclude': True})<br><br># password is excluded from model_dump() by default<br># internal_id schema exclusion requires json_schema_extra<br><br># To exclude from dump AND schema:<br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;secret: str = Field(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exclude=True,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;json_schema_extra={'writeOnly': True}<br>&nbsp;&nbsp;&nbsp;&nbsp;)</code><br><br><code>Field(exclude=True)</code> omits the field from <code>model_dump()</code> by default. Use <code>json_schema_extra</code> to annotate the JSON Schema without fully removing the field from it.",
  ["L1-mechanics"])

c("Models",
  "What is <code>model_rebuild()</code> and when is it required?",
  "<code>from __future__ import annotations<br>from pydantic import BaseModel<br><br>class A(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;b: B | None = None<br><br>class B(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;a: A | None = None<br><br>A.model_rebuild()  # Resolve forward reference to B<br>B.model_rebuild()  # Resolve forward reference to A</code><br><br><code>model_rebuild()</code> resolves forward references, self-references, and <code>Annotated</code> metadata. Required after:<br>• Circular/recursive model definitions<br>• Models that reference types defined later in the module<br>• Dynamically modifying <code>model_fields</code> at runtime<br><br>Without it, you'll get <code>PydanticUndefinedAnnotation</code> or silent <code>Any</code> fallback.",
  ["L1-mechanics"])

c("Models",
  "What does the <code>model_json_schema()</code> parameters control?",
  "<code>from pydantic import BaseModel<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;role: str = 'user'<br><br>schema = User.model_json_schema()  # Full draft-2020-12 schema<br><br># Customize output:<br>User.model_json_schema(by_alias=True)  # Use alias names<br>User.model_json_schema(ref_template='#/components/schemas/{model}')  # Custom $ref<br>User.model_json_schema(schema_generator=MyGenerator)  # Custom generator<br>User.model_json_schema(mode='validation')  # vs 'serialization'</code><br><br>Key parameters:<br>• <code>by_alias</code> — use field aliases as property names<br>• <code>ref_template</code> — format for <code>$ref</code> strings<br>• <code>schema_generator</code> — custom <code>GenerateJsonSchema</code> subclass<br>• <code>mode</code> — <code>'validation'</code> (input schema) or <code>'serialization'</code> (output schema)",
  ["L1-mechanics"])

# ═══════════════════════════════════════════
# 03 — VALIDATORS
# ═══════════════════════════════════════════

c("Validators",
  "What is <code>@field_validator</code> and what modes does it support?",
  "<code>from pydantic import BaseModel, field_validator<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@field_validator('name')<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def name_must_not_be_empty(cls, v: str) -&gt; str:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if not v.strip():<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('Name must not be empty')<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return v</code><br><br><b>Modes (via <code>mode=</code> parameter):</b><br>• <code>'after'</code> (default) — runs after coercion, receives coerced value<br>• <code>'before'</code> — runs before coercion, receives raw input<br>• <code>'wrap'</code> — wraps the validator, receives handler + value<br>• <code>'plain'</code> — similar to 'after' but doesn't receive ValidationInfo",
  ["L1-mechanics"])

c("Validators",
  "What is the difference between <code>mode='before'</code> and <code>mode='after'</code> in field validators?",
  "<code>@field_validator('age', mode='before')<br>@classmethod<br>def parse_age(cls, v):  # v is raw input (could be str, int, etc.)<br>&nbsp;&nbsp;&nbsp;&nbsp;if isinstance(v, str):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return int(v.strip())<br>&nbsp;&nbsp;&nbsp;&nbsp;return v  # Still goes through standard int validation after<br><br>@field_validator('age', mode='after')<br>@classmethod<br>def check_age(cls, v: int):  # v is already coerced to int<br>&nbsp;&nbsp;&nbsp;&nbsp;if v &lt; 0:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('Age must be non-negative')<br>&nbsp;&nbsp;&nbsp;&nbsp;return v</code><br><br><code>'before'</code> gives you the raw value (pre-coercion). <code>'after'</code> gives you the already-coerced/validated value. Use <code>'before'</code> for custom parsing; use <code>'after'</code> for additional constraints.",
  ["L1-mechanics"])

c("Validators",
  "What is <code>@model_validator</code> and its modes?",
  "<code>from pydantic import BaseModel, model_validator<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;password: str<br>&nbsp;&nbsp;&nbsp;&nbsp;password_confirm: str<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@model_validator(mode='after')<br>&nbsp;&nbsp;&nbsp;&nbsp;def passwords_match(self):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if self.password != self.password_confirm:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('Passwords do not match')<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return self</code><br><br><b>Modes:</b><br>• <code>'before'</code> — receives raw input dict, must return dict<br>• <code>'after'</code> — receives model instance, must return instance<br>• <code>'wrap'</code> — wraps, receives handler + raw input<br><br>Perfect for cross-field validation (e.g., passwords match, date ranges).",
  ["L1-mechanics"])

c("Validators",
  "How do you do cross-field validation with <code>@model_validator(mode='after')</code>?",
  "<code>class Booking(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;start_date: date<br>&nbsp;&nbsp;&nbsp;&nbsp;end_date: date<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@model_validator(mode='after')<br>&nbsp;&nbsp;&nbsp;&nbsp;def check_dates(self):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if self.start_date &gt;= self.end_date:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('start_date must be before end_date')<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return self</code><br><br><code>mode='after'</code> provides the fully validated model instance, so you can access all fields with <code>self.field_name</code> and compare them. Return <code>self</code> at the end.",
  ["L1-mechanics"])

c("Validators",
  "How does <code>@model_validator(mode='before')</code> work?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@model_validator(mode='before')<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def normalize(cls, data: Any) -&gt; Any:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if isinstance(data, dict):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if 'full_name' in data:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data['name'] = data.pop('full_name')<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return data</code><br><br>Runs before any field validation. Receives the raw input (usually a dict). Must return the (possibly modified) input dict. Useful for renaming fields, setting defaults dynamically, or normalizing data shape.",
  ["L1-mechanics"])

c("Validators",
  "What are functional validators (<code>AfterValidator</code>, <code>BeforeValidator</code>, <code>WrapValidator</code>)?",
  "<code>from pydantic import BaseModel<br>from pydantic.functional_validators import AfterValidator<br>from typing_extensions import Annotated<br><br>def check_positive(v: int) -&gt; int:<br>&nbsp;&nbsp;&nbsp;&nbsp;if v &lt;= 0:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('Must be positive')<br>&nbsp;&nbsp;&nbsp;&nbsp;return v<br><br>PositiveInt = Annotated[int, AfterValidator(check_positive)]<br><br>class Product(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;price: PositiveInt</code><br><br>Functional validators are <b>reusable, composable validator functions</b> attached via <code>Annotated</code>. They're anonymous (no decorator needed) and work outside of model classes — e.g., with <code>TypeAdapter</code>.",
  ["L1-mechanics"])

c("Validators",
  "Compare decorator validators vs <code>Annotated</code> functional validators.",
  "<b>Decorator (<code>@field_validator</code>):</b><br>• Attached to a specific model class<br>• Named, reference specific field(s) by string<br>• Can access <code>ValidationInfo</code> (other fields, context)<br>• Not reusable across models without mixins<br><br><b>Functional (<code>Annotated</code> + <code>AfterValidator</code>):</b><br>• Reusable — define once, use anywhere<br>• Anonymous — just a function<br>• Composable — chain multiple validators<br>• Works with <code>TypeAdapter</code> and outside <code>BaseModel</code><br>• Cannot access other fields (no <code>ValidationInfo</code>)<br><br>Use functional validators for reusable type-level constraints. Use decorator validators for model-specific logic and cross-field checks.",
  ["L1-mechanics"])

c("Validators",
  "How do you chain multiple validators with <code>Annotated</code>?",
  "<code>from pydantic.functional_validators import AfterValidator<br>from typing_extensions import Annotated<br><br>def strip(v: str) -&gt; str:<br>&nbsp;&nbsp;&nbsp;&nbsp;return v.strip()<br><br>def not_empty(v: str) -&gt; str:<br>&nbsp;&nbsp;&nbsp;&nbsp;if not v:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('Must not be empty')<br>&nbsp;&nbsp;&nbsp;&nbsp;return v<br><br>TrimmedNonEmptyStr = Annotated[str, AfterValidator(strip), AfterValidator(not_empty)]</code><br><br>Multiple <code>AfterValidator</code> (or mix of <code>BeforeValidator</code> / <code>AfterValidator</code> / <code>WrapValidator</code>) annotations chain in order. Each receives the output of the previous validator.",
  ["L1-mechanics"])

c("Validators",
  "What is <code>ValidationInfo</code> and what does it provide?",
  "<code>from pydantic import BaseModel, field_validator, ValidationInfo<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;is_admin: bool<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@field_validator('name')<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def check_name(cls, v: str, info: ValidationInfo) -&gt; str:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if info.data.get('is_admin') and not v:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('Admin must have a name')<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return v</code><br><br><code>ValidationInfo</code> provides:<br>• <code>.data</code> — dict of fields validated so far<br>• <code>.field_name</code> — name of the field being validated<br>• <code>.context</code> — optional context dict passed via <code>model_validate(data, context={...})</code><br><br>Available in <code>mode='after'</code> and <code>mode='wrap'</code> (not in <code>'before'</code>).",
  ["L1-mechanics"])

c("Validators",
  "How do you raise custom validation errors?",
  "<code>from pydantic import BaseModel, field_validator<br>from pydantic_core import PydanticCustomError<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@field_validator('age')<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def check_age(cls, v: int):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if v &lt; 0:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise PydanticCustomError(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'negative_age',<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'Age must be non-negative, got {age}',<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{'age': v}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return v</code><br><br><code>PydanticCustomError</code> produces structured errors with error codes. <code>ValueError</code> also works but gives less structured output. The error message template uses <code>{field_name}</code> placeholders with context dict values.",
  ["L1-mechanics"])

c("Validators",
  "How do you pass context to validators?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@field_validator('age')<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def check_age(cls, v: int, info: ValidationInfo):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_age = info.context.get('max_age', 150)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if v &gt; max_age:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('Too old')<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return v<br><br>User.model_validate({'name': 'Alice', 'age': 200}, context={'max_age': 120})<br># Raises ValidationError</code><br><br>Pass a <code>context</code> dict to <code>model_validate()</code> (or <code>model_validate_json()</code>). Access it via <code>info.context</code> inside any <code>@field_validator</code> or <code>@model_validator</code>.",
  ["L1-mechanics"])

c("Validators",
  "What is <code>WrapValidator</code> and when should you use it?",
  "<code>from pydantic.functional_validators import WrapValidator<br>from typing_extensions import Annotated<br><br>def log_and_validate(v, handler):<br>&nbsp;&nbsp;&nbsp;&nbsp;print(f'Validating: {v}')<br>&nbsp;&nbsp;&nbsp;&nbsp;result = handler(v)  # Run the standard Pydantic validation<br>&nbsp;&nbsp;&nbsp;&nbsp;print(f'Result: {result}')<br>&nbsp;&nbsp;&nbsp;&nbsp;return result<br><br>LoggedInt = Annotated[int, WrapValidator(log_and_validate)]</code><br><br><code>WrapValidator</code> gives you full control: you receive both the raw value and a <code>handler</code> callable that runs the standard validation. You can modify the value before passing it to <code>handler()</code>, then modify the result. Useful for logging, metrics, or custom coercion logic.",
  ["L1-mechanics"])

c("Validators",
  "In what order do validators run?",
  "Validation order for a single field:<br><br>1. <code>@model_validator(mode='before')</code> — whole input<br>2. <code>BeforeValidator</code> (functional) — per field<br>3. Standard Pydantic type coercion<br>4. <code>@field_validator(mode='after')</code> — per field, decorator style<br>5. <code>AfterValidator</code> (functional) — per field, annotated style<br>6. <code>@model_validator(mode='after')</code> — whole model<br><br>Multiple validators of the same type run in definition order. Field validators run before model validators of the same mode.",
  ["L1-mechanics"])

c("Validators",
  "How do you validate each item in a list field?",
  "<code>from pydantic import BaseModel, field_validator<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;tags: list[str]<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@field_validator('tags')<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def tags_not_empty(cls, v: list[str]):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for tag in v:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if not tag.strip():<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('Tags must not be empty')<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return v</code><br><br>Pydantic validates the list as a whole (checks it IS a list of strings), but per-item constraints require custom validators. Use <code>@field_validator</code> on the list field to iterate items. Alternatively, create a reusable <code>Annotated</code> type for list elements.",
  ["L1-mechanics"])

c("Validators",
  "What is <code>field_validator</code> inside a <code>@model_validator(mode='before')</code> for pre-processing?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@model_validator(mode='before')<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def coerce_age(cls, data: Any):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if isinstance(data, dict) and 'age' in data:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if isinstance(data['age'], str):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data['age'] = int(data['age'])<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return data</code><br><br><code>mode='before'</code> lets you transform raw input before any field validation runs. Useful for:<br>• Renaming/mapping fields before validation<br>• Coercing types that Pydantic doesn't auto-coerce<br>• Injecting computed defaults based on other raw values<br><br>Contrast with <code>mode='after'</code> which gets the validated instance.",
  ["L1-mechanics"])

c("Validators",
  "How do you skip a field validator on certain conditions?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;is_admin: bool<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@field_validator('name')<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def admin_name_check(cls, v: str, info: ValidationInfo):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if not info.data.get('is_admin'):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return v  # Skip validation for non-admins<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if len(v) &lt; 5:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('Admin name too short')<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return v</code><br><br>There's no built-in 'skip' mechanism. Simply <b>return early</b> when conditions aren't met. Check <code>info.data</code> for other fields already validated, or use <code>info.context</code> for external flags. For more complex skip logic, split into separate validators.",
  ["L1-mechanics"])

c("Validators",
  "How do you apply one field_validator to multiple fields?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;first_name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;last_name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;middle_name: str<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@field_validator('first_name', 'last_name', 'middle_name')<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def strip_whitespace(cls, v: str) -&gt; str:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return v.strip()<br><br># All three fields get the same validation<br>user = User(first_name=' Alice ', last_name=' Smith ', middle_name='')</code><br><br>Pass multiple field names as positional arguments to <code>@field_validator</code>. The validator runs on each field independently. Combine with <code>mode='before'</code> for pre-processing or <code>mode='after'</code> for post-coercion checks.",
  ["L1-mechanics"])

# ═══════════════════════════════════════════
# 04 — SERIALIZATION
# ═══════════════════════════════════════════

c("Serialization",
  "What is <code>@field_serializer</code>?",
  "<code>from pydantic import BaseModel, field_serializer<br>from datetime import datetime<br><br>class Event(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;timestamp: datetime<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@field_serializer('timestamp')<br>&nbsp;&nbsp;&nbsp;&nbsp;def serialize_ts(self, value: datetime) -&gt; str:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return value.strftime('%Y-%m-%d %H:%M:%S')<br><br>e = Event(name='Launch', timestamp=datetime(2024,1,1,12,0))<br>print(e.model_dump())  # {'name': 'Launch', 'timestamp': '2024-01-01 12:00:00'}</code><br><br><code>@field_serializer</code> customizes how a specific field is serialized in <code>model_dump()</code> / <code>model_dump_json()</code>. The serializer receives <code>self</code> and the field value, and returns the serialized form.",
  ["L1-mechanics"])

c("Serialization",
  "What is <code>@model_serializer</code> and its modes?",
  "<code>from pydantic import BaseModel, model_serializer<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;first_name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;last_name: str<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@model_serializer(mode='wrap')<br>&nbsp;&nbsp;&nbsp;&nbsp;def serialize(self, handler):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result = handler(self)  # Get default serialization<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result['full_name'] = f\"{self.first_name} {self.last_name}\"<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return result</code><br><br><b>Modes:</b><br>• <code>'plain'</code> — replaces default serialization entirely<br>• <code>'wrap'</code> — wraps default serialization, receives <code>handler</code> callable<br><br>With <code>mode='wrap'</code>, call <code>handler(self)</code> to get the default serialized dict, then modify it. With <code>mode='plain'</code>, you produce the entire output from scratch.",
  ["L1-mechanics"])

c("Serialization",
  "What is <code>SerializeAsAny</code>?",
  "<code>from pydantic import BaseModel, SerializeAsAny<br><br>class Dog(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;breed: str<br>class Cat(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;color: str<br><br>class Owner(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;pet: Dog | Cat = Field(discriminator='pet_type')<br>&nbsp;&nbsp;&nbsp;&nbsp;pet_type: Literal['dog', 'cat']<br><br>class Shelter(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;pets: list[SerializeAsAny[Dog | Cat]]</code><br><br>Without <code>SerializeAsAny</code>, a <code>Dog | Cat</code> union serializes only the fields common to both. <code>SerializeAsAny</code> serializes <b>all fields</b> of the actual subtype — it respects the concrete type, not the union.",
  ["L1-mechanics"])

c("Serialization",
  "What is <code>serialization_alias</code> vs <code>validation_alias</code>?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str = Field(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;validation_alias='userName',  # Input name<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serialization_alias='fullName'  # Output name<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br><br>user = User(userName='Alice')  # Input uses validation_alias<br>print(user.model_dump(by_alias=True))  # {'fullName': 'Alice'}</code><br><br><code>validation_alias</code> — name used when <b>parsing/validating</b> input<br><code>serialization_alias</code> — name used when <b>serializing</b> output<br><br>Setting just <code>alias</code> sets both. Use separate aliases when input and output field names differ (e.g., camelCase input, snake_case storage, PascalCase output).",
  ["L1-mechanics"])

c("Serialization",
  "How do you generate JSON Schema from a Pydantic model?",
  "<code>from pydantic import BaseModel<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str = Field(description='Full name')<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int = Field(ge=0, le=150)<br><br>schema = User.model_json_schema()<br>print(schema)<br># {<br>#   'type': 'object',<br>#   'properties': {<br>#     'name': {'type': 'string', 'description': 'Full name'},<br>#     'age': {'type': 'integer', 'minimum': 0, 'maximum': 150}<br>#   },<br>#   'required': ['name', 'age']<br># }</code><br><br>This replaces V1's <code>.schema()</code>. Output is a JSON Schema Draft 2020-12 compliant dict. Often used with FastAPI to auto-generate OpenAPI specs.",
  ["L1-mechanics"])

c("Serialization",
  "How do you use custom JSON encoders in Pydantic?",
  "<code>import json<br>from datetime import datetime<br><br>def custom_encoder(obj):<br>&nbsp;&nbsp;&nbsp;&nbsp;if isinstance(obj, datetime):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return obj.isoformat()<br>&nbsp;&nbsp;&nbsp;&nbsp;raise TypeError<br><br>class Event(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;at: datetime<br><br>e = Event(name='Launch', at=datetime.now())<br>json_str = e.model_dump_json()  # Uses Pydantic's default encoder<br><br># Custom:<br>json_str = json.dumps(e.model_dump(), default=custom_encoder)</code><br><br>Pydantic's <code>model_dump_json()</code> uses its own encoder. For custom encoding, use <code>model_dump()</code> first, then <code>json.dumps()</code> with a custom <code>default</code> function. Or use <code>@field_serializer</code> for model-level control.",
  ["L1-mechanics"])

c("Serialization",
  "What does <code>exclude_unset</code> do in <code>model_dump()</code>?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int = 0<br>&nbsp;&nbsp;&nbsp;&nbsp;email: str = 'default@test.com'<br><br>user = User(name='Alice')<br>print(user.model_dump())<br># {'name': 'Alice', 'age': 0, 'email': 'default@test.com'}<br><br>print(user.model_dump(exclude_unset=True))<br># {'name': 'Alice'}  — Only explicitly provided fields</code><br><br><code>exclude_unset=True</code> omits fields that were not explicitly provided during model creation, even if they have defaults. Very useful for partial updates (PATCH) in APIs — only send back what was set.",
  ["L1-mechanics"])

c("Serialization",
  "What's the difference between <code>exclude_unset</code>, <code>exclude_defaults</code>, and <code>exclude_none</code>?",
  "<b><code>exclude_unset=True</code></b> — omit fields not explicitly provided<br><b><code>exclude_defaults=True</code></b> — omit fields where value equals the default<br><b><code>exclude_none=True</code></b> — omit fields with <code>None</code> value<br><br><code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int = 0<br>&nbsp;&nbsp;&nbsp;&nbsp;bio: str | None = None<br><br>user = User(name='Alice', age=0, bio=None)<br>user.model_dump(exclude_unset=True)    # {'name': 'Alice', 'age': 0, 'bio': None}<br>user.model_dump(exclude_defaults=True) # {'name': 'Alice'}<br>user.model_dump(exclude_none=True)     # {'name': 'Alice', 'age': 0}</code>",
  ["L1-mechanics"])

c("Serialization",
  "How do you pretty-print JSON with <code>model_dump_json()</code>?",
  "<code>user = User(name='Alice', age=30)<br><br># Compact (default)<br>user.model_dump_json()  # '{\"name\":\"Alice\",\"age\":30}'<br><br># Pretty-printed<br>user.model_dump_json(indent=2)<br># {<br>#   \"name\": \"Alice\",<br>#   \"age\": 30<br># }</code><br><br><code>model_dump_json(indent=2)</code> pretty-prints the JSON output. Other <code>json.dumps()</code> parameters are supported: <code>indent</code>, <code>ensure_ascii</code>, <code>separators</code>, etc. Use <code>by_alias=True</code> to use field aliases as JSON keys.",
  ["L1-mechanics"])

c("Serialization",
  "What is the <code>warnings</code> parameter in <code>model_dump()</code>?",
  "<code>from pydantic import BaseModel<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;password: SecretStr<br><br>user = User(name='Alice', password='secret')<br><br># Default: warns about serializing SecretStr<br>user.model_dump()  # Warning: SecretStr being serialized<br><br># Suppress warnings<br>user.model_dump(warnings=False)<br><br># Or always show<br>user.model_dump(warnings=True)</code><br><br>Controls whether Pydantic emits warnings during serialization (e.g., when serializing <code>SecretStr</code>, unserializable types, or deprecated patterns). Set to <code>False</code> to suppress, <code>True</code> to always show (default depends on the specific warning).",
  ["L1-mechanics"])

c("Serialization",
  "What is the <code>fallback</code> parameter in <code>model_dump()</code>?",
  "<code>from pydantic import BaseModel<br>from datetime import datetime<br><br>def custom_fallback(value):<br>&nbsp;&nbsp;&nbsp;&nbsp;if isinstance(value, datetime):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return str(value)  # Fallback to string<br>&nbsp;&nbsp;&nbsp;&nbsp;raise PydanticSerializationError<br><br>class Event(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;at: datetime<br><br>e = Event(name='Launch', at=datetime.now())<br>print(e.model_dump(mode='json', fallback=custom_fallback))</code><br><br><code>fallback</code> provides a callable that handles types Pydantic can't serialize. Receives the value and must return a serializable result or raise. Useful for custom types that don't implement <code>__get_pydantic_core_schema__</code>. Only called when standard serialization fails.",
  ["L1-mechanics"])

c("Serialization",
  "What is <code>serialization_alias</code> and when do you use it separately from <code>alias</code>?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;created_at: datetime = Field(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;validation_alias='created',  # Input: created<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serialization_alias='createdAt'  # Output: createdAt<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br><br>user = User(created='2024-01-01T00:00:00')<br>print(user.model_dump(by_alias=True))  # {'createdAt': '...'}</code><br><br>Separate aliases when <b>input and output field names differ</b>. Common in APIs that consume snake_case but produce camelCase. If you only set <code>alias</code>, it's used for both. In V2, <code>alias</code> primarily affects validation; use <code>serialization_alias</code> for output control.",
  ["L1-mechanics"])

c("Serialization",
  "What is <code>model_validate_json()</code> and when does it parse dates?",
  "<code>from pydantic import BaseModel<br>from datetime import datetime<br><br>class Event(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;at: datetime<br><br>json_str = '{\"name\": \"Launch\", \"at\": \"2024-01-01T12:00:00Z\"}'<br>event = Event.model_validate_json(json_str)<br>print(event.at)  # datetime(2024, 1, 1, 12, 0, tzinfo=UTC)<br><br># Strict mode: rejects non-JSON types<br>Event.model_validate_json(json_str, strict=True)</code><br><br><code>model_validate_json()</code> parses JSON string AND validates in one pass. Date/time strings in ISO 8601 format are automatically parsed to <code>datetime</code> objects. Unlike <code>model_validate()</code> which takes a Python dict, this takes a raw JSON string. More efficient than <code>json.loads()</code> + <code>model_validate()</code>.",
  ["L1-mechanics"])

c("Serialization",
  "How do you serialize a model to a JSON string that can be re-validated?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;created: datetime<br><br>user = User(name='Alice', created=datetime.now())<br><br># Using round_trip=True<br>json_str = user.model_dump_json(round_trip=True)<br># '{\"name\":\"Alice\",\"created\":\"2024-01-01T00:00:00Z\"}'<br><br># Can re-validate from this JSON:<br>user2 = User.model_validate_json(json_str)<br>assert user == user2<br><br># Without round_trip, datetime might serialize differently<br># and re-validation could fail or produce different results</code><br><br><code>round_trip=True</code> ensures the serialized JSON can be parsed back into an identical model. It adds necessary type information (e.g., timezone qualifiers on datetimes) and serializes in a lossless format.",
  ["L1-mechanics"])

c("Serialization",
  "How do you serialize a Pydantic model to formats other than JSON?",
  "<code>import yaml<br>from pydantic import BaseModel<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br><br>user = User(name='Alice', age=30)<br><br># To YAML: dump dict first, then serialize<br>yaml_str = yaml.dump(user.model_dump())<br># name: Alice<br># age: 30<br><br># To MessagePack<br>import msgpack<br>packed = msgpack.dumps(user.model_dump())<br>restored = User.model_validate(msgpack.loads(packed))<br><br># To XML (third-party)<br>from dicttoxml import dicttoxml<br>xml_bytes = dicttoxml(user.model_dump())<br><br># Key pattern: model_dump() → external serializer<br># To deserialize: external parser → model_validate()</code><br><br>Pydantic only outputs <code>dict</code> (Python) and JSON natively. For other formats, use <code>model_dump()</code> as an intermediate dict and pass to a format-specific serializer. Deserialize by parsing to dict first, then <code>model_validate()</code>.",
  ["L1-mechanics"])

# ═══════════════════════════════════════════
# 05 — ADVANCED TYPES
# ═══════════════════════════════════════════

c("Types",
  "How do you use <code>Annotated</code> with validators for reusable types?",
  "<code>from typing_extensions import Annotated<br>from pydantic import BaseModel, AfterValidator<br><br>def must_be_positive(v: int) -&gt; int:<br>&nbsp;&nbsp;&nbsp;&nbsp;if v &lt;= 0:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('Must be positive')<br>&nbsp;&nbsp;&nbsp;&nbsp;return v<br><br>PositiveInt = Annotated[int, AfterValidator(must_be_positive)]<br><br>class Product(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;price: PositiveInt<br>&nbsp;&nbsp;&nbsp;&nbsp;quantity: PositiveInt  # Reuse!</code><br><br><code>Annotated[BaseType, Validator1, Validator2, ...]</code> creates a reusable type alias with built-in validation. Define once, use across many models. This is the <b>functional validator pattern</b> recommended in V2.",
  ["L2-composition"])

c("Types",
  "How do discriminated unions work in Pydantic V2?",
  "<code>from pydantic import BaseModel, Field<br>from typing import Literal, Annotated, Union<br>from pydantic import Discriminator<br><br>class Cat(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;pet_type: Literal['cat']<br>&nbsp;&nbsp;&nbsp;&nbsp;meows: bool<br><br>class Dog(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;pet_type: Literal['dog']<br>&nbsp;&nbsp;&nbsp;&nbsp;barks: bool<br><br>class Owner(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;pet: Cat | Dog = Field(discriminator='pet_type')<br><br>owner = Owner(pet={'pet_type': 'cat', 'meows': True})<br># pet is correctly resolved to Cat instance</code><br><br>The <code>discriminator</code> field tells Pydantic which field to inspect to determine the concrete type. Error messages are much clearer with discriminators.",
  ["L2-composition"])

c("Types",
  "How do you use <code>Literal</code> types in Pydantic?",
  "<code>from typing import Literal<br>from pydantic import BaseModel<br><br>class TrafficLight(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;color: Literal['red', 'yellow', 'green']<br><br>light = TrafficLight(color='red')   # OK<br>light = TrafficLight(color='blue')  # ValidationError</code><br><br><code>Literal</code> restricts a field to a specific set of values. Pydantic validates that the input is exactly one of the literal values. Excellent for enums, states, and discriminated unions. Can also use with numeric literals: <code>Literal[1, 2, 3]</code>.",
  ["L2-composition"])

c("Types",
  "How do you use Python <code>Enum</code> with Pydantic?",
  "<code>from enum import Enum, IntEnum<br>from pydantic import BaseModel<br><br>class Color(str, Enum):<br>&nbsp;&nbsp;&nbsp;&nbsp;RED = 'red'<br>&nbsp;&nbsp;&nbsp;&nbsp;GREEN = 'green'<br>&nbsp;&nbsp;&nbsp;&nbsp;BLUE = 'blue'<br><br>class Shirt(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;color: Color<br>&nbsp;&nbsp;&nbsp;&nbsp;size: Literal['S', 'M', 'L', 'XL']  # Or IntEnum<br><br>shirt = Shirt(color='red')   # Coerced to Color.RED<br>shirt = Shirt(color=Color.RED)  # Works too</code><br><br>Pydantic validates and coerces string/int values to Enum members. Use <code>StrEnum</code> (Python 3.11+) or <code>(str, Enum)</code> for automatic string serialization. Use <code>use_enum_values=True</code> in <code>model_config</code> to serialize the enum value instead of the member.",
  ["L2-composition"])

c("Types",
  "How do you create generic Pydantic models?",
  "<code>from typing import TypeVar, Generic<br>from pydantic import BaseModel<br><br>T = TypeVar('T')<br><br>class PaginatedResponse(BaseModel, Generic[T]):<br>&nbsp;&nbsp;&nbsp;&nbsp;items: list[T]<br>&nbsp;&nbsp;&nbsp;&nbsp;total: int<br>&nbsp;&nbsp;&nbsp;&nbsp;page: int<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br><br>response = PaginatedResponse[User](items=[{'name': 'A'}], total=1, page=1)<br># items become list[User]</code><br><br>Use <code>TypeVar</code> + <code>Generic[BaseModel]</code> to create reusable generic models. Parameterize with a concrete type when creating instances. The type parameter propagates validation to nested items.",
  ["L2-composition"])

c("Types",
  "What is <code>RootModel</code> and when do you use it?",
  "<code>from pydantic import RootModel<br><br># For list root types<br>Users = RootModel[list[str]]<br>users = Users(['alice', 'bob'])<br>print(users.root)  # ['alice', 'bob']<br><br># For dict root types<br>Config = RootModel[dict[str, int]]<br>c = Config({'a': 1, 'b': 2})<br>print(c.root)  # {'a': 1, 'b': 2}</code><br><br><code>RootModel</code> is for validating/serializing types that aren't objects (like a plain <code>list</code> or <code>dict</code>). Access the root value via <code>.root</code>. If you need to validate a plain list of ints, <code>RootModel[list[int]]</code> is the tool.",
  ["L2-composition"])

c("Types",
  "What is <code>TypeAdapter</code> and how does it differ from <code>BaseModel</code>?",
  "<code>from pydantic import TypeAdapter<br><br># Validate a simple list without defining a model<br>IntList = TypeAdapter(list[int])<br>result = IntList.validate_python([1, 2, '3'])  # [1, 2, 3]<br>json_result = IntList.validate_json('[1, 2, 3]')<br><br># Serialize<br>dump = IntList.dump_python([1, 2, 3])  # [1, 2, 3]<br>json_dump = IntList.dump_json([1, 2, 3])  # b'[1,2,3]'</code><br><br><code>TypeAdapter</code> validates and serializes <b>any Pydantic-compatible type</b> without defining a model class. Use it for list/dict validation, function parameters, or any context where a full <code>BaseModel</code> would be overkill.",
  ["L2-composition"])

c("Types",
  "What are <code>SecretStr</code> and <code>SecretBytes</code>?",
  "<code>from pydantic import BaseModel, SecretStr, SecretBytes<br><br>class Config(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;api_key: SecretStr<br>&nbsp;&nbsp;&nbsp;&nbsp;cert: SecretBytes<br><br>c = Config(api_key='sk-abc123', cert=b'my-cert-data')<br>print(c)  # api_key=SecretStr('**********') — masked!<br>print(c.api_key.get_secret_value())  # 'sk-abc123'</code><br><br><code>SecretStr</code> / <code>SecretBytes</code> mask sensitive values in <code>repr()</code>, <code>str()</code>, and <code>model_dump()</code> (by default, unless <code>model_dump(mode='json')</code>). Access the raw value with <code>.get_secret_value()</code>. Use for API keys, passwords, tokens.",
  ["L2-composition"])

c("Types",
  "What constrained types does Pydantic provide?",
  "<code>from pydantic import BaseModel<br>from pydantic.types import (<br>&nbsp;&nbsp;&nbsp;&nbsp;constr, conint, confloat, condecimal,<br>&nbsp;&nbsp;&nbsp;&nbsp;conlist, conset, confrozenset<br>)<br><br>class Product(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: constr(min_length=1, max_length=100)<br>&nbsp;&nbsp;&nbsp;&nbsp;price: confloat(gt=0, le=9999.99)<br>&nbsp;&nbsp;&nbsp;&nbsp;tags: conlist(str, min_length=1, max_length=10)</code><br><br>Constrained types embed validation rules directly in the type annotation. They're an alternative to using <code>Field()</code> constraints. <code>constr</code>, <code>conint</code>, <code>confloat</code>, <code>condecimal</code>, <code>conlist</code>, <code>conset</code>, etc. Note: <code>Annotated</code> + functional validators is the modern V2 pattern.",
  ["L2-composition"])

c("Types",
  "What URL types does Pydantic provide?",
  "<code>from pydantic import BaseModel, HttpUrl, FileUrl, AnyUrl<br>from pydantic import PostgresDsn, RedisDsn, MySQLDsn<br><br>class Service(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;website: HttpUrl  # Must be http/https<br>&nbsp;&nbsp;&nbsp;&nbsp;docs: FileUrl    # Must be file://<br>&nbsp;&nbsp;&nbsp;&nbsp;any_url: AnyUrl  # Any valid URL scheme<br>&nbsp;&nbsp;&nbsp;&nbsp;db: PostgresDsn  # postgres://user:pass@host/db</code><br><br>Pydantic provides validated URL types that check URL format, scheme, and structure. DSN types (<code>PostgresDsn</code>, <code>RedisDsn</code>, <code>MySQLDsn</code>, etc.) validate specific connection string formats. All URL types strip trailing whitespace.",
  ["L2-composition"])

c("Types",
  "What IP address types does Pydantic provide?",
  "<code>from pydantic import BaseModel<br>from pydantic.networks import IPvAnyAddress, IPvAnyInterface, IPvAnyNetwork<br><br>class Server(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;ip: IPvAnyAddress       # e.g., 192.168.1.1 or ::1<br>&nbsp;&nbsp;&nbsp;&nbsp;iface: IPvAnyInterface  # e.g., 192.168.1.1/24<br>&nbsp;&nbsp;&nbsp;&nbsp;net: IPvAnyNetwork      # e.g., 192.168.0.0/16</code><br><br>Validates IPv4 and IPv6 addresses using Python's <code>ipaddress</code> module. <code>IPvAnyAddress</code> accepts individual IPs. <code>IPvAnyInterface</code> accepts IP with subnet mask. <code>IPvAnyNetwork</code> accepts network addresses. All accept both IPv4 and IPv6.",
  ["L2-composition"])

c("Types",
  "What datetime-related types does Pydantic provide?",
  "<code>from pydantic import BaseModel<br>from pydantic.types import (<br>&nbsp;&nbsp;&nbsp;&nbsp;PastDate, FutureDate,<br>&nbsp;&nbsp;&nbsp;&nbsp;AwareDatetime, NaiveDatetime<br>)<br><br>class Event(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;birthday: PastDate  # Must be in the past<br>&nbsp;&nbsp;&nbsp;&nbsp;deadline: FutureDate  # Must be in the future<br>&nbsp;&nbsp;&nbsp;&nbsp;created_at: AwareDatetime  # Must have timezone info<br>&nbsp;&nbsp;&nbsp;&nbsp;local_time: NaiveDatetime  # Must NOT have timezone info</code><br><br>Specialized datetime types enforce temporal and timezone constraints at the type level. <code>PastDate</code> / <code>FutureDate</code> compare against <code>datetime.now()</code>. <code>AwareDatetime</code> requires tzinfo; <code>NaiveDatetime</code> forbids it.",
  ["L2-composition"])

c("Types",
  "What is the <code>Json</code> type and how does it work?",
  "<code>from pydantic import BaseModel, Json<br>from typing import Any<br><br>class Config(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;settings: Json[dict[str, Any]]  # Validates JSON structure<br><br># From Python dict — stores as dict<br>c = Config(settings={'theme': 'dark', 'version': 2})<br>print(c.settings)  # {'theme': 'dark', 'version': 2}<br>print(type(c.settings))  # &lt;class 'dict'&gt;<br><br># From JSON string — parses it first<br>c = Config(settings='{\"theme\": \"dark\"}')<br>print(c.settings)  # {'theme': 'dark'} (parsed!)</code><br><br><code>Json[T]</code> stores arbitrary JSON-valid data but validates it against the type <code>T</code>. It can accept either a Python object or a JSON string. When serializing, <code>model_dump(mode='json')</code> keeps the <code>settings</code> field as a nested JSON object (not a double-encoded string).",
  ["L2-composition"])

c("Types",
  "What is <code>model_validate_strings</code> and when do you need it?",
  "<code>from pydantic import BaseModel, ConfigDict<br><br>class Product(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(coerce_numbers_to_str=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;price: str<br>&nbsp;&nbsp;&nbsp;&nbsp;stock: str<br><br>p = Product.model_validate({'price': 99.99, 'stock': 42})<br># price='99.99', stock='42' — numbers coerced to strings<br><br># V2 alternative for ad-hoc validation:<br>from pydantic import TypeAdapter<br>ta = TypeAdapter(list[int])<br>ta.validate_strings('1,2,3')  # [1, 2, 3]</code><br><br><code>coerce_numbers_to_str=True</code> in model config allows automatic conversion of numbers to strings. <code>TypeAdapter.validate_strings()</code> validates a string representation of the type (e.g., a comma-separated list).",
  ["L2-composition"])

c("Types",
  "What are <code>ImportString</code> and <code>PyObject</code> types?",
  "<code>from pydantic import BaseModel<br>from pydantic.types import ImportString, PyObject<br><br>class Plugin(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;path: ImportString  # Dotted path to import<br>&nbsp;&nbsp;&nbsp;&nbsp;obj: PyObject       # Dotted path to a specific Python object<br><br>p = Plugin(path='os.path', obj='json.loads')<br>import os.path<br>print(p.path is os.path)  # True<br>print(p.obj is json.loads)  # True</code><br><br><code>ImportString</code> validates and imports a dotted path to a module. <code>PyObject</code> validates and imports a dotted path to any Python object (module, function, class, etc.). Both resolve via <code>importlib</code>. Use for plugin systems or dynamic class loading.",
  ["L2-composition"])

c("Types",
  "What is <code>EmailStr</code> and how do you install it?",
  "<code># Install: pip install pydantic[email]<br>from pydantic import BaseModel, EmailStr<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;email: EmailStr<br><br>User(email='user@example.com')  # OK<br>User(email='not-an-email')      # ValidationError<br>User(email='test@[192.168.1.1]') # Validates domain format too</code><br><br><code>EmailStr</code> validates email addresses using the <code>email-validator</code> library. Requires <code>pip install pydantic[email]</code>. Validates format, domain structure, and rejects obviously invalid addresses. For V2, import from <code>pydantic</code> directly (not <code>pydantic.types</code>).",
  ["L2-composition"])

c("Types",
  "What is <code>PaymentCardNumber</code>?",
  "<code># Install: pip install pydantic-extra-types<br>from pydantic_extra_types.payment import PaymentCardNumber<br>from pydantic import BaseModel<br><br>class Payment(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;card: PaymentCardNumber<br><br>p = Payment(card='4111111111111111')  # Valid Visa test number<br>print(p.card.brand)   # 'Visa'<br>print(p.card.bin)     # '411111'<br>print(p.card.last4)   # '1111'<br>print(p.card.masked)  # '411111******1111'</code><br><br><code>PaymentCardNumber</code> (from <code>pydantic-extra-types</code>) validates credit card numbers using the Luhn algorithm. Provides <code>.brand</code>, <code>.bin</code>, <code>.last4</code>, and <code>.masked</code> properties. Requires <code>pip install pydantic-extra-types</code>.",
  ["L2-composition"])

c("Types",
  "What is the <code>Color</code> type from pydantic-extra-types?",
  "<code># Install: pip install pydantic-extra-types<br>from pydantic_extra_types.color import Color<br>from pydantic import BaseModel<br><br>class Theme(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;primary: Color<br><br>t = Theme(primary='#ff0000')<br>print(t.primary.as_hex())   # '#ff0000'<br>print(t.primary.as_rgb())   # 'rgb(255, 0, 0)'<br>print(t.primary.as_hsl())   # 'hsl(0, 100%, 50%)'<br><br># Also accepts named colors<br>Theme(primary='red')  # Works!<br>Theme(primary='rebeccapurple')  # Works!</code><br><br><code>Color</code> validates CSS color values: hex (<code>#fff</code>, <code>#ffffff</code>), RGB/RGBA, HSL/HSLA, and named colors. Provides conversion between formats. From <code>pydantic-extra-types</code>.",
  ["L2-composition"])

c("Types",
  "How do you use <code>PastDatetime</code> and <code>FutureDatetime</code>?",
  "<code>from pydantic import BaseModel<br>from pydantic.types import PastDatetime, FutureDatetime<br>from datetime import datetime, timezone<br><br>class Event(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;created: PastDatetime  # Must be in the past<br>&nbsp;&nbsp;&nbsp;&nbsp;expires: FutureDatetime  # Must be in the future<br><br># Both compare against datetime.now()<br>Event(created='2020-01-01T00:00:00Z', expires='2099-01-01T00:00:00Z')  # OK<br>Event(created='2099-01-01T00:00:00Z', expires='2020-01-01T00:00:00Z')  # Error</code><br><br><code>PastDatetime</code> / <code>FutureDatetime</code> are datetime-specific versions of <code>PastDate</code> / <code>FutureDate</code>. They validate against <code>datetime.now(tz=timezone.utc)</code> and require timezone-aware datetimes (use <code>AwareDatetime</code> or attach tzinfo).",
  ["L2-composition"])

c("Types",
  "What is <code>DirectoryPath</code> and how does it differ from <code>FilePath</code>?",
  "<code>from pydantic import BaseModel, DirectoryPath, FilePath<br><br>class Config(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;log_dir: DirectoryPath  # Must be an existing directory<br>&nbsp;&nbsp;&nbsp;&nbsp;config_file: FilePath    # Must be an existing file<br><br># Both validate that the path EXISTS on the filesystem<br>Config(log_dir='/tmp', config_file='/etc/hosts')  # OK if paths exist<br>Config(log_dir='/nonexistent', config_file='/etc/hosts')  # Error</code><br><br><code>FilePath</code> validates that the path points to an <b>existing file</b>. <code>DirectoryPath</code> validates that the path points to an <b>existing directory</b>. Both resolve relative paths (relative to CWD). Use <code>Path</code> if you don't need existence checks.",
  ["L2-composition"])

# ═══════════════════════════════════════════
# 06 — MODEL CONFIG
# ═══════════════════════════════════════════

c("Config",
  "How do you configure a model in Pydantic V2?",
  "<code>from pydantic import BaseModel, ConfigDict<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;frozen=True,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;extra='forbid',<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;str_strip_whitespace=True,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;validate_assignment=True<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int</code><br><br>V2 uses <code>model_config = ConfigDict(...)</code> instead of V1's inner <code>class Config</code>. <code>ConfigDict</code> is a <code>TypedDict</code> with all available settings. Model config applies to all fields in the model.",
  ["L3-design"])

c("Config",
  "What does <code>extra</code> control in model config?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(extra='forbid')<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br><br>User(name='Alice', unknown_field=42)  # ValidationError!<br><br># Options:<br># extra='ignore'  — silently drops unknown fields (default)<br># extra='forbid'  — raises ValidationError on unknown fields<br># extra='allow'   — keeps unknown fields (stored in __pydantic_extra__)</code><br><br><code>extra='forbid'</code> is recommended for strict API contracts. <code>extra='allow'</code> is useful when you need to pass through arbitrary fields. The default (<code>'ignore'</code>) silently drops unknowns, which can hide bugs.",
  ["L3-design"])

c("Config",
  "What does <code>frozen=True</code> do?",
  "<code>class Settings(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(frozen=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;host: str<br>&nbsp;&nbsp;&nbsp;&nbsp;port: int<br><br>s = Settings(host='localhost', port=8000)<br>s.port = 9000  # Raises ValidationError: instance is frozen</code><br><br><code>frozen=True</code> makes the entire model <b>immutable</b> after creation. Any attempt to set an attribute raises a <code>ValidationError</code>. For per-field immutability, use <code>Field(frozen=True)</code> instead. Useful for config objects, DTOs, and value objects where mutation would break invariants.",
  ["L3-design"])

c("Config",
  "What does <code>validate_assignment=True</code> do?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(validate_assignment=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int = Field(ge=0)<br><br>user = User(name='Alice', age=30)<br>user.age = -5  # ValidationError: age must be >= 0</code><br><br>Without <code>validate_assignment=True</code>, setting an attribute after creation bypasses validation. With it enabled, <b>every attribute assignment</b> goes through validation. Essential for mutable models that should maintain data integrity.",
  ["L3-design"])

c("Config",
  "What does <code>validate_default=True</code> do?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(validate_default=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int = Field(default=-1, ge=0)  # Invalid default!<br><br># Without validate_default=True: -1 would be accepted<br># With validate_default=True: Raises ValidationError at class definition</code><br><br>By default, Pydantic doesn't validate default values (assumes you know what you're doing). <code>validate_default=True</code> validates defaults just like user-provided values. Catches bugs where defaults violate field constraints.",
  ["L3-design"])

c("Config",
  "What does <code>from_attributes=True</code> do?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(from_attributes=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;id: int<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br><br># From ORM object (e.g., SQLAlchemy)<br>orm_user = db.query(UserORM).first()<br>pydantic_user = User.model_validate(orm_user)<br><br># From any object with attributes<br>from types import SimpleNamespace<br>obj = SimpleNamespace(id=1, name='Alice')<br>User.model_validate(obj)  # Works!</code><br><br><code>from_attributes=True</code> allows <code>model_validate()</code> to extract data from objects with attributes (not just dicts). Essential for ORM integration (SQLAlchemy, Django ORM, etc.). Replaces V1's <code>orm_mode=True</code>.",
  ["L3-design"])

c("Config",
  "What are <code>str_strip_whitespace</code>, <code>str_to_upper</code>, and <code>str_to_lower</code>?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;str_strip_whitespace=True,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;str_to_lower=True<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br>&nbsp;&nbsp;&nbsp;&nbsp;username: str<br>&nbsp;&nbsp;&nbsp;&nbsp;email: str<br><br>user = User(username='  Alice  ', email='A@B.COM')<br>print(user.username)  # 'alice'<br>print(user.email)     # 'a@b.com'</code><br><br>String transformation configs apply to all <code>str</code> fields in the model:<br>• <code>str_strip_whitespace</code> — strips leading/trailing whitespace<br>• <code>str_to_upper</code> — converts to uppercase<br>• <code>str_to_lower</code> — converts to lowercase<br>• <code>str_min_length</code>, <code>str_max_length</code> — global length constraints",
  ["L3-design"])

c("Config",
  "What does <code>populate_by_name=True</code> do?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(populate_by_name=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;first_name: str = Field(alias='firstName')<br><br># Without populate_by_name: must use alias<br># With populate_by_name: both work<br>User(firstName='Alice')   # using alias — works<br>User(first_name='Alice')  # using field name — also works!</code><br><br><code>populate_by_name=True</code> allows fields to be set using <b>either the alias or the field name</b>. Without it, only the alias is accepted during validation. Useful for migration periods or when you want to accept both API-style and Python-style naming.",
  ["L3-design"])

c("Config",
  "What does <code>use_enum_values</code> do?",
  "<code>from enum import Enum<br>from pydantic import BaseModel, ConfigDict<br><br>class Color(str, Enum):<br>&nbsp;&nbsp;&nbsp;&nbsp;RED = 'red'<br>&nbsp;&nbsp;&nbsp;&nbsp;GREEN = 'green'<br><br>class Shirt(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(use_enum_values=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;color: Color<br><br>s = Shirt(color='red')<br>print(s.model_dump())  # {'color': 'red'} — not Color.RED</code><br><br><code>use_enum_values=True</code> serializes the <b>value</b> of enum members (e.g., <code>'red'</code>) instead of the enum member itself. Without it, the output would still be a <code>Color</code> enum. Also affects validation: accepting raw values becomes more lenient.",
  ["L3-design"])

c("Config",
  "What does <code>arbitrary_types_allowed</code> do?",
  "<code>class CustomType:<br>&nbsp;&nbsp;&nbsp;&nbsp;def __init__(self, x):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.x = x<br><br>class Container(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(arbitrary_types_allowed=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;data: CustomType<br><br>c = Container(data=CustomType(42))<br># Works, but CustomType gets no validation or coercion<br># Pydantic just checks isinstance(data, CustomType)</code><br><br><code>arbitrary_types_allowed=True</code> allows fields typed with non-Pydantic types. Pydantic only does <code>isinstance</code> checks — no validation, no coercion, no JSON Schema for these fields. Use sparingly; prefer wrapping custom types in Pydantic models.",
  ["L3-design"])

c("Config",
  "What is <code>protected_namespaces</code>?",
  "<code>class Model(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(protected_namespaces=())  # Disable protection<br>&nbsp;&nbsp;&nbsp;&nbsp;model_name: str  # 'model_' prefix allowed now<br><br># By default, Pydantic reserves:<br># protected_namespaces = ('model_',)  # Blocks fields starting with 'model_'</code><br><br>Pydantic reserves certain field name prefixes (default: <code>model_</code>) to prevent conflicts with internal methods. <code>protected_namespaces=()</code> disables this protection (but your field names might shadow model methods). You can also add custom prefixes: <code>protected_namespaces=('model_', 'myapp_')</code>.",
  ["L3-design"])

c("Config",
  "What does <code>revalidate_instances</code> do?",
  "<code>from pydantic import BaseModel, ConfigDict<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(revalidate_instances='always')<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br><br>user = User(name='Alice')<br>User.model_validate(user)  # Re-validates even though it's already a User<br><br># Options:<br># 'never' — skip validation for existing model instances (default)<br># 'subclass-instances' — validate only subclass instances<br># 'always' — always re-validate, even if already the right type</code><br><br>Controls whether passing an existing model instance to <code>model_validate()</code> triggers re-validation. <code>'always'</code> is useful in pipelines where you want to ensure data integrity at every step.",
  ["L3-design"])

c("Config",
  "How can you share config across multiple models?",
  "<code>from pydantic import BaseModel, ConfigDict<br><br>base_config = ConfigDict(<br>&nbsp;&nbsp;&nbsp;&nbsp;extra='forbid',<br>&nbsp;&nbsp;&nbsp;&nbsp;str_strip_whitespace=True,<br>&nbsp;&nbsp;&nbsp;&nbsp;validate_assignment=True<br>)<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = base_config<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br><br>class Product(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = base_config<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;price: float</code><br><br>Since <code>ConfigDict</code> is just a <code>TypedDict</code>, you can define a shared config dict and use it across models. For more complex cases, create a base model class with the shared config and inherit from it.",
  ["L3-design"])

c("Config",
  "What is <code>loc_by_alias</code> in model config?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(loc_by_alias=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;first_name: str = Field(alias='firstName')<br><br>try:<br>&nbsp;&nbsp;&nbsp;&nbsp;User(firstName=123)  # Wrong type<br>except ValidationError as e:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(e.errors())<br>&nbsp;&nbsp;&nbsp;&nbsp;# Without loc_by_alias: loc=('first_name',)<br>&nbsp;&nbsp;&nbsp;&nbsp;# With loc_by_alias:    loc=('firstName',)</code><br><br><code>loc_by_alias=True</code> makes validation errors report the <b>alias</b> instead of the internal field name in the error location (<code>loc</code>). Useful for APIs where clients use the alias names and error messages should match.",
  ["L3-design"])

c("Config",
  "What is <code>hide_input_in_errors</code>?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(hide_input_in_errors=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;password: SecretStr<br><br>try:<br>&nbsp;&nbsp;&nbsp;&nbsp;User(password=123)  # Wrong type<br>except ValidationError as e:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(e.errors())<br>&nbsp;&nbsp;&nbsp;&nbsp;# Input value is HIDDEN in the error message<br>&nbsp;&nbsp;&nbsp;&nbsp;# Without: shows the actual input value<br>&nbsp;&nbsp;&nbsp;&nbsp;# With: shows '**********' or omits it</code><br><br><code>hide_input_in_errors=True</code> prevents sensitive input values from appearing in validation error messages. Useful when errors might be logged or returned to clients, preventing secret leakage.",
  ["L3-design"])

c("Config",
  "What are <code>ser_json_timedelta</code> and <code>ser_json_bytes</code> configs?",
  "<code>class Model(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ser_json_timedelta='float',  # Default: 'iso8601'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ser_json_bytes='base64'       # Default: 'base64'<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br>&nbsp;&nbsp;&nbsp;&nbsp;duration: timedelta<br>&nbsp;&nbsp;&nbsp;&nbsp;data: bytes<br><br>m = Model(duration=timedelta(seconds=5), data=b'hello')<br>print(m.model_dump_json())<br># duration serialized as float seconds (5.0)<br># data serialized as base64</code><br><br>Serialization configs control how specific types are encoded in JSON:<br>• <code>ser_json_timedelta</code>: <code>'iso8601'</code> or <code>'float'</code><br>• <code>ser_json_bytes</code>: <code>'base64'</code> or <code>'hex'</code><br>• <code>ser_json_inf_nan</code>: <code>'null'</code>, <code>'constants'</code>, or <code>'strings'</code><br><br>These apply to <code>model_dump(mode='json')</code> and <code>model_dump_json()</code>.",
  ["L3-design"])

c("Config",
  "How does config inheritance work across Pydantic model hierarchies?",
  "<code>class Base(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(extra='forbid')<br><br>class Child(Base):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(str_strip_whitespace=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br><br># Child's config RESETS — extra is NOT inherited!<br># Child.extra defaults to 'ignore' (the default)</code><br><br><b>Config inheritance is NOT additive.</b> Each <code>model_config</code> completely replaces the parent's config. To inherit config, create a shared <code>ConfigDict</code> variable and merge manually, or use a base class that all models inherit from with the desired config.",
  ["L3-design"])

# ═══════════════════════════════════════════
# 07 — GOTCHAS
# ═══════════════════════════════════════════

c("Gotchas",
  "Why does <code>Optional[str]</code> without a default require the field?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;nickname: str | None  # Optional? No — still REQUIRED<br><br>User(name='Alice')  # ValidationError: nickname is required<br>User(name='Alice', nickname=None)  # OK<br>User(name='Alice', nickname='Al')  # OK<br><br># To make truly optional, provide a default:<br>class User2(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;nickname: str | None = None  # Now optional</code><br><br><code>str | None</code> means the field <b>can be None</b>, but it still must be <b>provided</b> (just like <code>str</code> must be provided). Add <code>= None</code> to make the field itself optional.",
  ["L4-diagnosis"])

c("Gotchas",
  "What's the danger of mutable default values in Pydantic?",
  "<code># WRONG — shared list across all instances!<br>class Bad(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;tags: list[str] = []<br><br>a = Bad()<br>b = Bad()<br>a.tags.append('bug')<br>print(b.tags)  # ['bug'] — leaked from a!<br><br># CORRECT — each instance gets its own list<br>class Good(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;tags: list[str] = Field(default_factory=list)</code><br><br>Pydantic <b>does</b> make a shallow copy of the default, but for nested mutables (list of dicts, etc.), issues can still occur. Always use <code>default_factory</code> for <code>list</code>, <code>dict</code>, <code>set</code>, and nested mutable structures.",
  ["L4-diagnosis"])

c("Gotchas",
  "What is the validation order and why does it matter for cross-field logic?",
  "<b>Field validators run before model validators.</b> If you need to compare two fields, you must use <code>@model_validator(mode='after')</code> — not <code>@field_validator</code>.<br><br><code>@field_validator('end_date')</code> might not have access to validated <code>start_date</code> because validation order is based on field definition order and validators for later fields may not have been executed yet. <code>ValidationInfo.data</code> contains only fields processed so far.<br><br>For cross-field validation, always use <code>@model_validator(mode='after')</code> where all fields are guaranteed to be validated.",
  ["L4-diagnosis"])

c("Gotchas",
  "What's the gotcha with <code>model_dump()</code> and default values?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;role: str = 'user'  # Has a default<br><br>u = User(name='Alice')<br>u.model_dump()             # {'name': 'Alice', 'role': 'user'}<br>u.model_dump(exclude_unset=True)  # {'name': 'Alice'} — role omitted<br>u.model_dump(exclude_defaults=True)  # {'name': 'Alice'} — role omitted<br><br># But if user explicitly sets the default value:<br>u2 = User(name='Bob', role='user')<br>u2.model_dump(exclude_unset=True)  # {'name': 'Bob', 'role': 'user'}</code><br><br><code>exclude_defaults</code> checks if the value <b>equals</b> the default, not if it was explicitly set. <code>exclude_unset</code> checks if the field was provided at creation. They can give different results.",
  ["L4-diagnosis"])

c("Gotchas",
  "Why do discriminated unions without a discriminator field fail confusingly?",
  "<code># Without discriminator — confusing errors<br>class Owner(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;pet: Cat | Dog  # No discriminator<br><br>Owner(pet={'meows': True})<br># Error: tries Cat first, fails on missing fields,<br># then tries Dog, fails on missing fields<br># Error message mentions BOTH failures — confusing!<br><br># With discriminator — clear error<br>class Owner2(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;pet: Cat | Dog = Field(discriminator='pet_type')<br><br>Owner2(pet={'meows': True})<br># Error: Missing discriminator field 'pet_type'<br># MUCH clearer error message</code><br><br>Without <code>discriminator</code>, Pydantic tries each union member in order, giving verbose cumulative errors. Always use <code>Field(discriminator='field_name')</code> with tagged unions for clear error messages.",
  ["L4-diagnosis"])

c("Gotchas",
  "Why do I get errors creating models from ORM objects?",
  "<code># SQLAlchemy model<br>class UserORM(Base):<br>&nbsp;&nbsp;&nbsp;&nbsp;__tablename__ = 'users'<br>&nbsp;&nbsp;&nbsp;&nbsp;id = Column(Integer, primary_key=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;name = Column(String)<br><br># Pydantic model — will fail without from_attributes!<br>class UserSchema(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;id: int<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br><br>orm_user = session.query(UserORM).first()<br># This will fail — Pydantic expects a dict, not an ORM object<br>UserSchema.model_validate(orm_user)  # ValidationError!<br><br># FIX: add from_attributes=True to model_config<br>class UserSchema(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(from_attributes=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;id: int<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str</code><br><br>In V1, this was <code>class Config: orm_mode = True</code>. In V2, it's <code>ConfigDict(from_attributes=True)</code>. Without it, Pydantic can only validate dicts/mappings.",
  ["L4-diagnosis"])

c("Gotchas",
  "How do you handle circular references between models?",
  "<code>from __future__ import annotations<br>from pydantic import BaseModel<br><br>class Author(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;books: list[Book] = []  # Forward reference<br><br>class Book(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;title: str<br>&nbsp;&nbsp;&nbsp;&nbsp;author: Author  # References Author<br><br>Author.model_rebuild()  # Must call after all models defined!</code><br><br><b>Steps:</b><br>1. Add <code>from __future__ import annotations</code> at the top<br>2. Define both models<br>3. Call <code>model_rebuild()</code> on the model with the forward reference<br><br>Or use <code>TYPE_CHECKING</code> import guard and string annotations for non-Pydantic types.",
  ["L4-diagnosis"])

c("Gotchas",
  "What's the gotcha with <code>Json</code> type and model creation from dicts?",
  "<code>class Config(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;settings: Json[dict]<br><br># From Python dict — stores as dict<br>c = Config(settings={'key': 'value'})  # Works<br><br># From JSON string — parses it<br>c = Config(settings='{\"key\": \"value\"}')  # Works<br><br># The gotcha: model_dump() vs model_dump_json() behavior<br>c.model_dump()        # {'settings': {'key': 'value'}}  — dict<br>c.model_dump(mode='json')  # {'settings': {'key': 'value'}}  — embedded JSON<br>c.model_dump_json()   # '{\"settings\": {\"key\": \"value\"}}'  — not double-encoded</code><br><br><code>Json[T]</code> doesn't double-encode during JSON serialization. But if you need the field as a JSON <b>string</b> in the output, you'll need a custom serializer or different approach.",
  ["L4-diagnosis"])

c("Gotchas",
  "Can Pydantic V2 be slow? When?",
  "<b>V2 is significantly faster than V1, but can still be slow when:</b><br><br>• Many custom Python validators (they run in Python, not Rust)<br>• Deeply nested models with many fields<br>• Large lists of complex models (each item validated individually)<br>• Excessive use of <code>@model_validator</code> that runs on the entire model<br>• <code>model_rebuild()</code> called frequently (rebuilds core schema)<br>• <code>arbitrary_types_allowed=True</code> with heavy custom types<br><br><b>Optimization:</b> Use <code>Annotated</code> functional validators (they're optimized), minimize Python-level validators, use <code>model_rebuild(force=True)</code> strategically, and consider <code>TypeAdapter</code> for repeated list validation.",
  ["L4-diagnosis"])

c("Gotchas",
  "When should you use <code>TypeAdapter</code> instead of <code>BaseModel</code>?",
  "<b>Use <code>TypeAdapter</code> when:</b><br>• Validating a single list/dict type (no need for a named model)<br>• Validating function parameters outside a model context<br>• Converting between formats repeatedly (TypeAdapter caches the schema)<br>• You need <code>.validate_python()</code> / <code>.validate_json()</code> / <code>.dump_json()</code> for a bare type<br><br><b>Use <code>BaseModel</code> when:</b><br>• You have multiple named fields with relationships<br>• You need model methods, properties, or validators<br>• You want JSON Schema generation for an object<br>• You need nested model behavior<br><br><code>TypeAdapter</code> example:<br><code>adapter = TypeAdapter(list[int])<br>adapter.validate_json('[1,2,3]')  # [1, 2, 3]</code>",
  ["L4-diagnosis"])

c("Gotchas",
  "Why does <code>model_validate()</code> reject perfectly valid objects sometimes?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br><br>user = User(name='Alice', age=30)<br>data = user.model_dump()  # {'name': 'Alice', 'age': 30}<br>User.model_validate(data)  # Works — validates the dict<br><br># But passing the model instance back may surprise you:<br>User.model_validate(user)  # Works by default (no revalidation)<br># Unless revalidate_instances='always' is set</code><br><br>The gotcha is that <code>model_validate()</code> accepts dicts, not model instances (by design). If you pass a model instance with default <code>revalidate_instances='never'</code>, it's returned as-is. Use <code>model_validate(data, strict=True)</code> to ensure no coercion happens.",
  ["L4-diagnosis"])

c("Gotchas",
  "What happens when you forget <code>model_rebuild()</code> on recursive types?",
  "<code>class Category(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;children: list[Category] = []  # Forward reference to self<br><br># Forgot model_rebuild()?<br>Category.model_rebuild()  # Without this, creating instances may fail or<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# silently wrap nested dicts as plain dicts</code><br><br>Without <code>model_rebuild()</code>, forward references (including self-references) are not resolved. Pydantic may: (1) raise an error about unresolvable types, or (2) silently treat the forward reference as <code>Any</code> and skip validation for that field. Always call <code>model_rebuild()</code> after self-referencing model definitions.",
  ["L4-diagnosis"])

c("Gotchas",
  "Why should you use <code>from __future__ import annotations</code> in Pydantic projects?",
  "<code>from __future__ import annotations  # ALWAYS add this<br><br>from pydantic import BaseModel<br><br>class A(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;b: B | None = None  # Forward reference works without quotes<br><br>class B(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;a: A | None = None<br><br>A.model_rebuild()<br>B.model_rebuild()</code><br><br>Without this import, forward references must be quoted (<code>'B | None'</code>). With it, all annotations are strings at runtime, making forward references work naturally. Pydantic resolves them during <code>model_rebuild()</code>. Essential for circular references and self-referencing models.",
  ["L4-diagnosis"])

c("Gotchas",
  "What happens with <code>alias</code> and <code>populate_by_name</code> interaction?",
  "<code>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;# Without populate_by_name<br>&nbsp;&nbsp;&nbsp;&nbsp;first_name: str = Field(alias='firstName')<br><br>User(first_name='Alice')  # FAILS — must use alias<br>User(firstName='Alice')   # OK<br><br># With populate_by_name=True<br>class User2(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(populate_by_name=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;first_name: str = Field(alias='firstName')<br><br>User2(first_name='Alice')  # OK — accepts field name<br>User2(firstName='Alice')   # OK — accepts alias</code><br><br>Without <code>populate_by_name=True</code>, only the alias is accepted. With it, both alias and field name work. Gotcha: if both are provided, Pydantic uses the <b>alias</b> value (last one wins depending on order).",
  ["L4-diagnosis"])

c("Gotchas",
  "Why might <code>exclude</code> not work as expected with nested models?",
  "<code>class Address(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;street: str<br>&nbsp;&nbsp;&nbsp;&nbsp;city: str<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;address: Address<br><br>user = User(name='A', address={'street': '1', 'city': 'NYC'})<br><br># This excludes the ENTIRE address field:<br>user.model_dump(exclude={'address'})  # {'name': 'A'}<br><br># To exclude a nested field, use a dict:<br>user.model_dump(exclude={'address': {'city'}})<br># {'name': 'A', 'address': {'street': '1'}}<br><br># Complex nested exclusion:<br>user.model_dump(exclude={'address': {'__all__', 'city'}})  # Not supported!<br># Must be explicit about which nested fields to keep/exclude</code><br><br>Gotcha: <code>exclude</code> with nested models requires dict-of-sets syntax. The top-level key determines which nested model, and the set determines which nested fields. Cannot use <code>__all__</code> or wildcards.",
  ["L4-diagnosis"])

c("Gotchas",
  "Why do <code>Annotated</code> validators and <code>strict=True</code> sometimes conflict?",
  "<code>from typing_extensions import Annotated<br>from pydantic import BaseModel, AfterValidator<br><br>def must_be_even(v: int) -&gt; int:<br>&nbsp;&nbsp;&nbsp;&nbsp;if v % 2 != 0:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise ValueError('Must be even')<br>&nbsp;&nbsp;&nbsp;&nbsp;return v<br><br>EvenInt = Annotated[int, AfterValidator(must_be_even)]<br><br>class Model(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;num: EvenInt<br><br># Lax mode: coercion happens, then validator runs<br>Model(num='4')  # OK — '4' coerced to 4, then checked<br><br># Strict mode: coercion disabled, validator still runs<br>Model.model_validate({'num': '4'}, strict=True)  # Error: '4' is not int</code><br><br>Gotcha: In strict mode, type coercion is disabled but <code>AfterValidator</code> still runs. If your validator assumes the coerced type, strict mode inputs may fail before the validator even runs. Use <code>BeforeValidator</code> to handle both modes.",
  ["L4-diagnosis"])

c("Gotchas",
  "What happens when you have a model with <code>validate_default=True</code> and an invalid default?",
  "<code>class Bad(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(validate_default=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int = Field(default=-1, ge=0)<br><br># This RAISES at class DEFINITION time, not at instance creation!<br># ValidationError: default value -1 violates ge=0 constraint</code><br><br>With <code>validate_default=True</code>, Pydantic validates default values at class definition time. An invalid default will prevent the class from being defined (raises <code>ValidationError</code> during <code>class</code> statement execution). This is a feature — catches invalid defaults early — but can be surprising if you expect lazy validation.",
  ["L4-diagnosis"])

# ═══════════════════════════════════════════
# 08 — EXPERT
# ═══════════════════════════════════════════

c("Expert",
  "What's the recommended migration path from Pydantic V1 to V2?",
  "<b>Step-by-step migration:</b><br><br>1. Install <code>pydantic>=2.0</code> + <code>pydantic-settings</code> + <code>pydantic-extra-types</code><br>2. Run <code>bump-pydantic</code> CLI tool for automatic refactoring<br>3. Replace <code>.dict()</code> → <code>.model_dump()</code><br>4. Replace <code>.json()</code> → <code>.model_dump_json()</code><br>5. Replace <code>.schema()</code> → <code>.model_json_schema()</code><br>6. Replace <code>.parse_obj()</code> → <code>.model_validate()</code><br>7. Replace <code>.parse_raw()</code> → <code>.model_validate_json()</code><br>8. Replace <code>@validator</code> → <code>@field_validator</code><br>9. Replace <code>@root_validator</code> → <code>@model_validator</code><br>10. Replace <code>class Config</code> → <code>model_config = ConfigDict(...)</code><br>11. Replace <code>__fields__</code> → <code>model_fields</code><br>12. Replace <code>orm_mode</code> → <code>from_attributes</code><br><br>Test thoroughly — validation behavior is slightly stricter in V2.",
  ["L5-opinion"])

c("Expert",
  "Pydantic vs dataclasses vs attrs vs msgspec — when to use which?",
  "<b>Pydantic</b> — Best for API validation (especially FastAPI), config management, data pipelines. Rich validation, coercion, JSON Schema.<br><br><b>Dataclasses</b> — Best for simple data containers with no validation needed. Standard library, lightweight, great for internal DTOs.<br><br><b>attrs</b> — Similar to dataclasses but more powerful. Custom validators, converters, slots support. Good middle ground when you need some validation but not the full Pydantic stack.<br><br><b>msgspec</b> — Fastest option. Pure C, no Rust dependency. Schema-less, Protocol Buffers-like. Best for high-performance serialization/deserialization where validation is secondary.<br><br><b>Rule of thumb:</b> API layer → Pydantic. Internal data carriers → dataclasses. Speed-critical hot paths → msgspec.",
  ["L5-opinion"])

c("Expert",
  "How does Pydantic integrate with FastAPI?",
  "<code>from fastapi import FastAPI<br>from pydantic import BaseModel, Field<br><br>app = FastAPI()<br><br>class ItemCreate(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str = Field(min_length=1)<br>&nbsp;&nbsp;&nbsp;&nbsp;price: float = Field(gt=0)<br><br>class ItemResponse(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;id: int<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;price: float<br><br>@app.post('/items/', response_model=ItemResponse)<br>def create_item(item: ItemCreate):<br>&nbsp;&nbsp;&nbsp;&nbsp;# FastAPI auto-validates request body against ItemCreate<br>&nbsp;&nbsp;&nbsp;&nbsp;# FastAPI auto-serializes response to ItemResponse<br>&nbsp;&nbsp;&nbsp;&nbsp;...</code><br><br>FastAPI uses Pydantic natively: request bodies are validated via <code>model_validate()</code>, responses are serialized via <code>model_dump()</code>, and OpenAPI schemas are generated via <code>model_json_schema()</code>. No glue code needed.",
  ["L5-opinion"])

c("Expert",
  "How do you use Pydantic for settings management?",
  "<code>from pydantic_settings import BaseSettings<br>from pydantic import Field<br><br>class Settings(BaseSettings):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(env_file='.env')<br>&nbsp;&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;host: str = 'localhost'<br>&nbsp;&nbsp;&nbsp;&nbsp;port: int = 8000<br>&nbsp;&nbsp;&nbsp;&nbsp;database_url: str = Field(alias='DATABASE_URL')<br><br>settings = Settings()  # Reads from env vars + .env file<br>print(settings.database_url)</code><br><br><code>BaseSettings</code> (from <code>pydantic-settings</code> package, separate in V2) reads from environment variables, <code>.env</code> files, secrets, etc. Field names are automatically mapped to uppercase env vars. Uses Pydantic validation on all settings. Essential for 12-factor apps.",
  ["L5-opinion"])

c("Expert",
  "When should you NOT use Pydantic?",
  "<b>Avoid Pydantic for:</b><br><br>• <b>Simple one-off scripts</b> — overhead not worth it; use dataclasses or plain dicts<br>• <b>Performance-critical hot paths</b> — even V2 Rust core has overhead; use <code>msgspec</code> or manual validation<br>• <b>Data frames / numeric arrays</b> — use <code>pandas</code> / <code>numpy</code><br>• <b>Streaming data</b> — Pydantic validates whole objects; streaming requires different patterns<br>• <b>Protobuf/gRPC-first systems</b> — use protobuf codegen; Pydantic would be redundant<br>• <b>Very large datasets</b> (millions of records) — validation overhead per record adds up<br>• <b>When you don't need validation at all</b> — don't pay for what you don't use<br><br>Pydantic shines at API boundaries, configuration, and data ingestion where data integrity matters.",
  ["L5-opinion"])

c("Expert",
  "What's the difference between V2's <code>model_dump()</code> and V1's <code>dict()</code>?",
  "<b>V1 <code>.dict()</code>:</b><br>• Simple dict conversion<br>• <code>include</code>/<code>exclude</code> based on field names<br>• <code>by_alias</code> parameter<br>• <code>exclude_unset</code>, <code>exclude_defaults</code>, <code>exclude_none</code><br><br><b>V2 <code>.model_dump()</code>:</b><br>• All V1 parameters plus:<br>• <code>mode</code> — <code>'python'</code> or <code>'json'</code> (controls type conversion)<br>• <code>round_trip</code> — ensures output can be re-validated<br>• <code>warnings</code> — control serialization warnings<br>• <code>fallback</code> — callable for handling unserializable types<br>• More performant (Rust-powered)<br><br><code>.dict()</code> still works in V2 but is deprecated. Migrate to <code>.model_dump()</code>.",
  ["L5-opinion"])

c("Expert",
  "Functional validators (<code>Annotated</code>) vs decorator validators — which to use when?",
  "<b>Use <code>Annotated</code> + Functional (<code>AfterValidator</code>, etc.) when:</b><br>• The validation rule is <b>reusable</b> across many models<br>• The rule is purely about the value (no cross-field logic)<br>• You want to compose multiple rules on one type<br>• You're working with <code>TypeAdapter</code> or bare types<br>• You prefer a functional, immutable style<br><br><b>Use Decorator (<code>@field_validator</code>) when:</b><br>• The validation depends on <b>other fields</b> (via <code>ValidationInfo</code>)<br>• You need access to <code>info.context</code><br>• The validation is specific to one model<br>• You prefer OOP style with named validators<br>• You need <code>mode='before'</code> to pre-process raw input<br><br>Many teams use <code>Annotated</code> for type-level constraints and <code>@field_validator</code> for model-specific business logic.",
  ["L5-opinion"])

c("Expert",
  "How do you do schema-first API development with Pydantic + FastAPI?",
  "<b>Schema-first approach:</b><br><br>1. <b>Define models first</b> — create Pydantic models for request/response schemas<br>2. <b>Generate OpenAPI</b> — FastAPI auto-generates OpenAPI from Pydantic models<br>3. <b>Share models</b> — extract Pydantic models to a shared <code>schemas/</code> package<br>4. <b>Generate client SDKs</b> — use OpenAPI Generator from the Pydantic-derived schema<br>5. <b>Contract testing</b> — validate that API responses match the Pydantic schema<br><br><code># schemas/user.py<br>class UserCreate(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str = Field(min_length=1, max_length=100)<br>&nbsp;&nbsp;&nbsp;&nbsp;email: EmailStr<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int = Field(ge=0, le=150)<br><br>class UserResponse(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;id: int<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;email: EmailStr<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br>&nbsp;&nbsp;&nbsp;&nbsp;created_at: datetime</code><br><br>Pydantic models serve as the single source of truth for API contracts.",
  ["L5-opinion"])

c("Expert",
  "How do you create custom Pydantic types with <code>__get_pydantic_core_schema__</code>?",
  "<code>from pydantic_core import core_schema<br>from pydantic import GetCoreSchemaHandler<br><br>class PositiveFloat:<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def __get_pydantic_core_schema__(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cls, source_type, handler: GetCoreSchemaHandler<br>&nbsp;&nbsp;&nbsp;&nbsp;):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return core_schema.no_info_after_validator_function(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lambda v: v if v &gt; 0 else (_ for _ in ()).throw(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ValueError('Must be positive')<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;core_schema.float_schema()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)</code><br><br>By implementing <code>__get_pydantic_core_schema__</code> on a class, you can define custom validation logic at the core schema level. The <code>handler</code> can delegate to standard validation for inner types. This is how Pydantic internally validates all types — you're hooking into the same mechanism.",
  ["L6-innovation"])

c("Expert",
  "How do you build a Pydantic plugin/extension?",
  "<b>Pydantic plugins can hook into the schema generation process:</b><br><br>1. Implement <code>__get_pydantic_core_schema__</code> for custom types<br>2. Use <code>GenerateSchema</code> hooks to modify how schemas are built<br>3. Register your plugin via <code>SchemaSerializer</code> / <code>SchemaValidator</code> customizations<br>4. Override <code>model_rebuild()</code> or metaclass behavior for model-level plugins<br><br><b>Example patterns:</b><br>• Custom types that validate domain concepts (email, phone, ISBN)<br>• Field-level plugins via <code>Field()</code> metadata<br>• ORM plugins that auto-generate Pydantic models from SQLAlchemy tables<br>• Decorator-based plugins that add fields to models<br><br>Check <code>pydantic-extra-types</code> for examples of custom types built as plugins.",
  ["L6-innovation"])

c("Expert",
  "How do you optimize Pydantic model performance with <code>model_rebuild(force=True)</code>?",
  "<code># During development, models are lazily rebuilt<br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br><br># In production, force rebuild to pre-compute core schema<br>User.model_rebuild(force=True)<br><br># Or rebuild entire namespace<br>import myapp.models<br>from pydantic import BaseModel<br>for name, obj in vars(myapp.models).items():<br>&nbsp;&nbsp;&nbsp;&nbsp;if isinstance(obj, type) and issubclass(obj, BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;obj.model_rebuild(force=True)</code><br><br><code>model_rebuild(force=True)</code> pre-computes the core schema and validator, avoiding lazy initialization overhead at first use. Useful for production deployments where startup time is amortizable. Also resolves any lingering forward reference issues.",
  ["L6-innovation"])

c("Expert",
  "How do you integrate Pydantic with SQLAlchemy?",
  "<code>from pydantic import BaseModel, ConfigDict<br>from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column<br><br># SQLAlchemy model<br>class UserORM(DeclarativeBase):<br>&nbsp;&nbsp;&nbsp;&nbsp;id: Mapped[int] = mapped_column(primary_key=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;name: Mapped[str] = mapped_column(String(100))<br><br># Pydantic schema<br>class UserRead(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;model_config = ConfigDict(from_attributes=True)<br>&nbsp;&nbsp;&nbsp;&nbsp;id: int<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br><br># Usage<br>orm_user = session.query(UserORM).first()<br>response = UserRead.model_validate(orm_user)<br><br># For create/update, reverse the flow<br>data_in = UserCreate.model_dump()  # dict from Pydantic model<br>orm_user = UserORM(**data_in)</code><br><br>Key: <code>from_attributes=True</code> for reading ORM → Pydantic. <code>model_dump()</code> for writing Pydantic → ORM. Consider <code>SQLModel</code> (by the same author) for tighter integration with fewer classes.",
  ["L6-innovation"])

c("Expert",
  "How does Pydantic integrate with Strawberry GraphQL?",
  "<code>import strawberry<br>from pydantic import BaseModel<br><br>class UserModel(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br><br>@strawberry.experimental.pydantic.type(UserModel)<br>class User:<br>&nbsp;&nbsp;&nbsp;&nbsp;name: strawberry.auto<br>&nbsp;&nbsp;&nbsp;&nbsp;age: strawberry.auto<br><br>@strawberry.type<br>class Query:<br>&nbsp;&nbsp;&nbsp;&nbsp;@strawberry.field<br>&nbsp;&nbsp;&nbsp;&nbsp;def user(self) -&gt; User:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data = UserModel(name='Alice', age=30)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return User.from_pydantic(data)</code><br><br>Strawberry provides <code>@strawberry.experimental.pydantic.type()</code> to auto-generate GraphQL types from Pydantic models. Field types, default values, and descriptions are mapped automatically. This gives you a single source of truth — Pydantic model → GraphQL schema.",
  ["L6-innovation"])

c("Expert",
  "How do you create dynamic models with <code>create_model()</code>?",
  "<code>from pydantic import BaseModel, Field, create_model<br><br># Dynamic model creation<br>DynamicUser = create_model(<br>&nbsp;&nbsp;&nbsp;&nbsp;'DynamicUser',<br>&nbsp;&nbsp;&nbsp;&nbsp;name=(str, Field(min_length=1)),<br>&nbsp;&nbsp;&nbsp;&nbsp;age=(int, Field(ge=0, default=0)),<br>&nbsp;&nbsp;&nbsp;&nbsp;__base__=BaseModel<br>)<br><br>user = DynamicUser(name='Alice')<br>print(user.model_dump())  # {'name': 'Alice', 'age': 0}<br><br># With config<br>DynamicUser2 = create_model(<br>&nbsp;&nbsp;&nbsp;&nbsp;'DynamicUser2',<br>&nbsp;&nbsp;&nbsp;&nbsp;name=(str, ...),<br>&nbsp;&nbsp;&nbsp;&nbsp;__config__=ConfigDict(extra='forbid')<br>)</code><br><br><code>create_model()</code> creates a <code>BaseModel</code> subclass at runtime. Useful for:<br>• Generating models from database schemas<br>• Dynamic API endpoints that accept varying fields<br>• Plugin systems where models are defined in config files<br>• Generating Pydantic models from JSON Schema at runtime",
  ["L6-innovation"])

c("Expert",
  "How do you use pydantic-core directly for maximum performance?",
  "<code>from pydantic_core import SchemaValidator, core_schema<br><br># Build a validator directly (bypasses BaseModel overhead)<br>schema = core_schema.dict_schema(<br>&nbsp;&nbsp;&nbsp;&nbsp;core_schema.model_fields_schema(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'name': core_schema.model_field(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;core_schema.str_schema()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'age': core_schema.model_field(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;core_schema.int_schema(ge=0)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br>)<br><br>validator = SchemaValidator(schema)<br>result = validator.validate_python({'name': 'Alice', 'age': 30})<br># {'name': 'Alice', 'age': 30} — as fast as possible</code><br><br>Using <code>pydantic-core</code> directly bypasses Python-level model metaclass overhead. Useful for:<br>• Extreme performance requirements<br>• Embedding validation in C extensions or other languages<br>• Building custom validation pipelines<br><br>Trade-off: lose all <code>BaseModel</code> conveniences (methods, JSON Schema, etc.).",
  ["L6-innovation"])

c("Expert",
  "How does Pydantic V2 handle Protocol Buffers / gRPC integration?",
  "<b>Pydantic is not a protobuf replacement, but can complement gRPC:</b><br><br>1. <b>Validate before serialization</b> — validate incoming data with Pydantic before converting to protobuf<br>2. <b>Validate after deserialization</b> — validate deserialized protobuf objects before business logic<br>3. <b>Schema generation</b> — use <code>model_json_schema()</code> for REST/gRPC-transcoding gateways<br><br><code>from pydantic import BaseModel<br><br># Pydantic model for request validation<br>class CreateUserRequest(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str = Field(min_length=1)<br>&nbsp;&nbsp;&nbsp;&nbsp;email: str<br><br># Convert to gRPC protobuf<br>def create_user(request: CreateUserRequest):<br>&nbsp;&nbsp;&nbsp;&nbsp;pb = user_pb2.CreateUserRequest(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name=request.name,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;email=request.email<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br>&nbsp;&nbsp;&nbsp;&nbsp;stub.CreateUser(pb)</code><br><br>Pydantic handles input validation at the API boundary; protobuf handles wire serialization. Each does what it's best at.",
  ["L6-innovation"])

c("Expert",
  "How do you use <code>@model_validator(mode='wrap')</code>?",
  "<code>from pydantic import BaseModel, model_validator<br>from typing import Any<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@model_validator(mode='wrap')<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def log_validation(cls, data: Any, handler):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(f'Before validation: {data}')<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result = handler(data)  # Run standard validation<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(f'After validation: {result}')<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return result</code><br><br><code>mode='wrap'</code> gives you a <code>handler</code> that runs the default validation. You get both the raw input and the chance to modify the validated result. Useful for logging, metrics, profiling validation time, or modifying output after validation.",
  ["L6-innovation"])

c("Expert",
  "How do you create a custom validation error with structured metadata?",
  "<code>from pydantic_core import PydanticCustomError<br>from pydantic import BaseModel, field_validator<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;email: str<br><br>&nbsp;&nbsp;&nbsp;&nbsp;@field_validator('email')<br>&nbsp;&nbsp;&nbsp;&nbsp;@classmethod<br>&nbsp;&nbsp;&nbsp;&nbsp;def validate_email(cls, v: str):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if '@' not in v:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise PydanticCustomError(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'invalid_email',<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'{value} is not a valid email address',<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{'value': v}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return v<br><br>try:<br>&nbsp;&nbsp;&nbsp;&nbsp;User(email='notanemail')<br>except ValidationError as e:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(e.errors())<br>&nbsp;&nbsp;&nbsp;&nbsp;# [{'type': 'invalid_email', 'msg': 'notanemail is not a valid...', ...}]</code><br><br><code>PydanticCustomError</code> creates a structured error with a <b>custom error code</b> (<code>'invalid_email'</code>), a formatted message template, and a context dict. Error codes are stable identifiers useful for i18n, client-side error handling, and API error responses.",
  ["L6-innovation"])

c("Expert",
  "What is the difference between <code>AnyUrl</code>, <code>HttpUrl</code>, <code>FileUrl</code>, and <code>WebsocketUrl</code>?",
  "<code>from pydantic import BaseModel, AnyUrl, HttpUrl, FileUrl, WebsocketUrl<br><br>class Links(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;a: AnyUrl         # Accepts any valid URL scheme<br>&nbsp;&nbsp;&nbsp;&nbsp;b: HttpUrl        # http:// or https:// ONLY<br>&nbsp;&nbsp;&nbsp;&nbsp;c: FileUrl        # file:// ONLY<br>&nbsp;&nbsp;&nbsp;&nbsp;d: WebsocketUrl   # ws:// or wss:// ONLY<br><br># Valid examples<br>a = AnyUrl('ftp://files.example.com')        # OK<br>b = HttpUrl('https://example.com')            # OK<br>b = HttpUrl('ftp://example.com')              # FAILS<br>c = FileUrl('file:///etc/hosts')             # OK<br>d = WebsocketUrl('wss://chat.example.com')   # OK</code><br><br>Each URL type validates the <b>scheme</b> (protocol) in addition to general URL validity. <code>AnyUrl</code> is the most permissive. <code>HttpUrl</code> also validates <code>host</code> is present.",
  ["L6-innovation"])

c("Expert",
  "How do you handle polymorphic model lists with proper serialization?",
  "<code>from pydantic import BaseModel, Field, SerializeAsAny<br>from typing import Literal<br><br>class Cat(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;type: Literal['cat']<br>&nbsp;&nbsp;&nbsp;&nbsp;breed: str<br><br>class Dog(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;type: Literal['dog']<br>&nbsp;&nbsp;&nbsp;&nbsp;size: str<br><br>Animal = Cat | Dog<br><br>class Zoo(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;animals: list[SerializeAsAny[Animal]] = Field(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;discriminator='type'<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br><br>zoo = Zoo(animals=[<br>&nbsp;&nbsp;&nbsp;&nbsp;{'type': 'cat', 'breed': 'Siamese'},<br>&nbsp;&nbsp;&nbsp;&nbsp;{'type': 'dog', 'size': 'large'}<br>])<br>print(zoo.model_dump())<br># [{'type': 'cat', 'breed': 'Siamese'}, {'type': 'dog', 'size': 'large'}]</code><br><br><code>SerializeAsAny</code> ensures each item serializes with <b>all</b> its fields, not just the union-common fields. Combined with <code>discriminator</code>, you get correct parsing AND correct serialization of heterogeneous lists.",
  ["L6-innovation"])

c("Expert",
  "How do you use Pydantic with Django Ninja?",
  "<code>from ninja import NinjaAPI, Schema<br><br>api = NinjaAPI()<br><br># Django Ninja uses Pydantic under the hood<br>class UserIn(Schema):  # Extends Pydantic BaseModel<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;email: str<br><br>class UserOut(Schema):<br>&nbsp;&nbsp;&nbsp;&nbsp;id: int<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;email: str<br><br>@api.post('/users/', response=UserOut)<br>def create_user(request, payload: UserIn):<br>&nbsp;&nbsp;&nbsp;&nbsp;user = User.objects.create(**payload.dict())<br>&nbsp;&nbsp;&nbsp;&nbsp;return user</code><br><br>Django Ninja's <code>Schema</code> is a Pydantic <code>BaseModel</code> subclass. It provides the same validation, serialization, and JSON Schema generation. The <code>.dict()</code> method (Pydantic V1 API shim) converts to dict for Django ORM. Use <code>.model_dump()</code> for V2 compatibility.",
  ["L6-innovation"])

c("Expert",
  "How do you profile and benchmark Pydantic model performance?",
  "<code>import timeit<br>from pydantic import BaseModel<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br><br># Benchmark validation<br>data = {'name': 'Alice', 'age': 30}<br>t = timeit.timeit(lambda: User.model_validate(data), number=100_000)<br>print(f'100k validations: {t:.3f}s')<br><br># Benchmark with pre-built validator<br>User.model_rebuild(force=True)  # Pre-compute core schema<br>t = timeit.timeit(lambda: User.model_validate(data), number=100_000)<br>print(f'After rebuild: {t:.3f}s')<br><br># Profile individual validators<br>import cProfile<br>cProfile.run('User.model_validate(data)')</code><br><br>Key optimization: call <code>model_rebuild(force=True)</code> to pre-compute the Rust core schema. Profile to identify slow custom validators. Consider <code>TypeAdapter</code> for repeated single-type validation (it caches schemas more aggressively).",
  ["L6-innovation"])

c("Expert",
  "What is the Pydantic V2 plugin system?",
  "<b>Pydantic V2 has a plugin architecture for extending validation:</b><br><br>1. <b>Type-level plugins</b> — Implement <code>__get_pydantic_core_schema__</code> on custom types<br>2. <b>Schema generation hooks</b> — Override how Pydantic generates core schemas<br>3. <b>Metaclass plugins</b> — Hook into <code>ModelMetaclass</code> for model-level extensions<br>4. <b>Field metadata</b> — Use <code>json_schema_extra</code> and custom metadata dicts<br><br><b>Examples of the plugin system in action:</b><br>• <code>pydantic-extra-types</code> — custom types as plugins<br>• <code>SQLModel</code> — ties SQLAlchemy columns to Pydantic fields<br>• <code>strawberry-graphql</code> — generates GraphQL types from Pydantic models<br><br>Plugins are discovered and applied during <code>model_rebuild()</code>. Most users interact with plugins indirectly through libraries.",
  ["L6-innovation"])

c("Expert",
  "How do you integrate Pydantic with Pydantic dataclasses?",
  "<code>from pydantic.dataclasses import dataclass as pydantic_dataclass<br><br>@pydantic_dataclass<br>class Point:<br>&nbsp;&nbsp;&nbsp;&nbsp;x: float<br>&nbsp;&nbsp;&nbsp;&nbsp;y: float<br><br># Behaves like a dataclass but with Pydantic validation<br>p = Point(x=1.5, y='2.5')  # '2.5' coerced to 2.5<br>print(p.x, p.y)  # 1.5 2.5<br><br># Supports all Pydantic features<br>from pydantic import Field<br><br>@pydantic_dataclass<br>class Point2:<br>&nbsp;&nbsp;&nbsp;&nbsp;x: float = Field(gt=0)<br>&nbsp;&nbsp;&nbsp;&nbsp;y: float = Field(gt=0)<br><br># config, validators, serializers all work</code><br><br><code>pydantic.dataclasses.dataclass</code> is a drop-in replacement for <code>@dataclass</code> that adds Pydantic validation. Supports all <code>BaseModel</code> features: <code>Field()</code> constraints, validators, <code>model_dump()</code>, <code>model_json_schema()</code>. Use when you prefer dataclass syntax but need validation.",
  ["L6-innovation"])

c("Expert",
  "How do you handle <code>model_validate()</code> with bytes input?",
  "<code>from pydantic import BaseModel<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int<br><br># model_validate accepts dict or object with attributes<br># For JSON bytes, use model_validate_json instead<br><br>json_bytes = b'{\"name\": \"Alice\", \"age\": 30}'<br>user = User.model_validate_json(json_bytes)  # Accepts bytes too!<br><br># Or manually decode<br>import json<br>user = User.model_validate(json.loads(json_bytes))</code><br><br><code>model_validate_json()</code> accepts both <code>str</code> and <code>bytes</code>. <code>model_validate()</code> accepts dicts and objects with attributes (<code>from_attributes=True</code>). Don't pass raw bytes to <code>model_validate()</code> — it won't parse them as JSON.",
  ["L6-innovation"])

c("Expert",
  "What is the difference between <code>model_dump_json()</code> returning <code>bytes</code> in V1 and <code>str</code> in V2?",
  "<b>V1 <code>.json()</code>:</b> Returns a <code>str</code> (JSON string)<br><br><b>V2 <code>.model_dump_json()</code>:</b> Returns <code>bytes</code> (UTF-8 encoded JSON)<br><br><code># V2<br>user = User(name='Alice', age=30)<br>result = user.model_dump_json()<br>print(type(result))  # &lt;class 'bytes'&gt;<br>print(result)  # b'{\"name\":\"Alice\",\"age\":30}'<br><br># If you need a string:<br>json_str = user.model_dump_json().decode()  # or<br>json_str = user.model_dump_json(by_alias=True).decode()</code><br><br>V2 returns <code>bytes</code> for efficiency (no decode/encode roundtrip when writing to files/sockets). Use <code>.decode()</code> if you need a <code>str</code>. This is a breaking change from V1.",
  ["L6-innovation"])

c("Expert",
  "How do you test Pydantic models with Hypothesis (property-based testing)?",
  "<code>from hypothesis import given, strategies as st<br>from pydantic import BaseModel, Field<br><br>class User(BaseModel):<br>&nbsp;&nbsp;&nbsp;&nbsp;name: str = Field(min_length=1, max_length=100)<br>&nbsp;&nbsp;&nbsp;&nbsp;age: int = Field(ge=0, le=150)<br><br># Strategy: generate valid User inputs<br>user_strategy = st.builds(<br>&nbsp;&nbsp;&nbsp;&nbsp;User,<br>&nbsp;&nbsp;&nbsp;&nbsp;name=st.text(min_size=1, max_size=100),<br>&nbsp;&nbsp;&nbsp;&nbsp;age=st.integers(min_value=0, max_value=150)<br>)<br><br>@given(user_strategy)<br>def test_user_roundtrip(user: User):<br>&nbsp;&nbsp;&nbsp;&nbsp;# model_dump → model_validate should be idempotent<br>&nbsp;&nbsp;&nbsp;&nbsp;data = user.model_dump()<br>&nbsp;&nbsp;&nbsp;&nbsp;user2 = User.model_validate(data)<br>&nbsp;&nbsp;&nbsp;&nbsp;assert user == user2<br><br># Test invalid inputs should fail<br>@given(st.text(min_size=101))<br>def test_name_too_long(name: str):<br>&nbsp;&nbsp;&nbsp;&nbsp;from pydantic import ValidationError<br>&nbsp;&nbsp;&nbsp;&nbsp;try:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;User(name=name, age=30)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assert len(name) &lt;= 100  # Only valid names pass<br>&nbsp;&nbsp;&nbsp;&nbsp;except ValidationError:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;assert len(name) &gt; 100  # Invalid names rejected</code><br><br>Hypothesis + Pydantic is excellent for testing invariants: roundtrip fidelity, validation boundaries, and edge cases. Use <code>st.builds()</code> with field strategies that match <code>Field()</code> constraints. Tests that pass for thousands of generated cases give high confidence in model correctness.",
  ["L6-innovation"])

# ═══════════════════════════════════════════
# BUILD APKG
# ═══════════════════════════════════════════

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
