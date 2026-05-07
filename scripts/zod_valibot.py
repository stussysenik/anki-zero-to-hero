import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Zod_Valibot"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "ZodCore":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Zod-Core-API"),
    "ValibotCore":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Valibot-Core-API"),
    "Advanced":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Advanced-Patterns"),
    "Comparison":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Comparison"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Expert-Opinions"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ================================================================
# 01 - Fundamentals
# ================================================================

c("Fundamentals",
    "What is schema validation?",
    "Schema validation is the process of verifying that an unknown input (API body, form data, localStorage) conforms to an expected shape at <b>runtime</b>. It bridges the gap between TypeScript's compile-time types and real-world data entering your program.",
    "fundamentals")

c("Fundamentals",
    "Why can't you rely on TypeScript types alone?",
    "TypeScript types are <b>compile-time only</b> — they are erased at runtime. Any data crossing a network boundary, parsed from JSON, or read from localStorage has no type guarantees until validated at runtime.",
    "fundamentals")

c("Fundamentals",
    "Where should you place schema validation in your app?",
    "At every <b>trust boundary</b>: API request handlers, form submissions, <code>localStorage</code> reads, WebSocket message handlers, and environment variable parsing. Validate at the edge, trust internally.",
    "fundamentals")

c("Fundamentals",
    "What is Zod?",
    "Zod is a <b>TypeScript-first</b> schema declaration and validation library with <b>static type inference</b>. It uses an object-oriented, method-chaining API to define schemas and produces rich, human-readable errors.",
    "fundamentals")

c("Fundamentals",
    "What is Valibot?",
    "Valibot is a <b>modular, tree-shakable</b> schema library for TypeScript. It uses a <b>functional API</b> — schemas are built by composing standalone functions rather than method chaining. Core <b>~1 KB</b> when tree-shaken.",
    "fundamentals")

c("Fundamentals",
    "What is Zod's core design philosophy?",
    "Zod is <b>developer-experience first</b>: method chaining for readability, automatic type inference with <code>z.infer</code>, descriptive error messages out of the box, and a large ecosystem of plugins and integrations.",
    "fundamentals")

c("Fundamentals",
    "What is Valibot's core design philosophy?",
    "Valibot is <b>bundle-size first</b>: every feature is a standalone function that tree-shakers can eliminate if unused. It favours composition over chaining, matching the functional style popular in modern TypeScript.",
    "fundamentals")

c("Fundamentals",
    "How does the API style differ between Zod and Valibot?",
    "Zod uses <b>method chaining</b>: <code>z.string().min(3).max(100)</code><br>Valibot uses <b>function composition</b>: <code>pipe(string(), minLength(3), maxLength(100))</code>",
    "fundamentals")

c("Fundamentals",
    "What happens to unused validators in each library at build time?",
    "Zod bundles <b>all of its code</b> regardless of what you use (~12 KB min+gzip). Valibot's tree-shakable design means <b>unused validators are removed</b>, resulting in as little as ~1 KB for simple schemas.",
    "fundamentals")

c("Fundamentals",
    "What is the mental model for schema libraries?",
    "<b>Parse, don't validate</b> — coined by Alexis King. A schema library should not just return <code>true / false</code>; it should <b>transform</b> unknown data into a known, typed shape, or fail with descriptive errors.",
    "fundamentals")

c("Fundamentals",
    "How do both libraries handle the 'parse, don't validate' principle?",
    "Both return <b>strongly typed output</b> on success:<br>Zod: <code>schema.parse(input)</code> returns <code>T</code><br>Valibot: <code>parse(schema, input)</code> returns <code>Output&lt;S&gt;</code><br>Both throw on failure (or use safe variants).",
    "fundamentals")

# ================================================================
# 02 - Zod Core API
# ================================================================

c("ZodCore",
    "How do you define a string schema in Zod?",
    "<code>import { z } from 'zod'</code><br><code>const s = z.string()</code><br>Chain methods: <code>.min(1)</code>, <code>.max(255)</code>, <code>.email()</code>, <code>.url()</code>, <code>.uuid()</code>, <code>.regex(/.../)</code>, <code>.trim()</code>.",
    "zod-core")

c("ZodCore",
    "How do you define a number schema in Zod?",
    "<code>const n = z.number()</code><br>Chain: <code>.int()</code>, <code>.positive()</code>, <code>.nonnegative()</code>, <code>.min(0)</code>, <code>.max(100)</code>, <code>.multipleOf(5)</code>, <code>.finite()</code>, <code>.safe()</code>.",
    "zod-core")

c("ZodCore",
    "How do you define literal and enum schemas in Zod?",
    "<code>z.literal('hello')</code> — matches exactly one value.<br><code>z.enum(['red', 'green', 'blue'])</code> — union of string literals.<br><code>z.nativeEnum(MyEnum)</code> — for TypeScript enums.",
    "zod-core")

c("ZodCore",
    "How do you define an object schema in Zod?",
    "<code>const User = z.object({ name: z.string(), age: z.number() })</code><br>By default, <b>unknown keys are stripped</b>. Use <code>.strict()</code> to reject them or <code>.passthrough()</code> to keep them. Use <code>.keyof()</code> to get a key enum.",
    "zod-core")

c("ZodCore",
    "How do you define array and tuple schemas in Zod?",
    "<code>z.array(z.string())</code> — variable-length array.<br><code>z.tuple([z.string(), z.number()])</code> — fixed-length.<br>Chain on arrays: <code>.min(1)</code>, <code>.max(10)</code>, <code>.nonempty()</code>.",
    "zod-core")

c("ZodCore",
    "How do you define record, union, and discriminatedUnion in Zod?",
    "<code>z.record(z.string(), z.number())</code> — <code>{ [k: string]: number }</code><br><code>z.union([z.string(), z.number()])</code> — A | B<br><code>z.discriminatedUnion('type', [...])</code> — tagged union on the <code>'type'</code> key.",
    "zod-core")

c("ZodCore",
    "What is <code>z.discriminatedUnion()</code> and why use it?",
    "A <b>performance optimisation</b> over <code>z.union()</code>. It inspects the <b>discriminator key</b> (e.g. <code>'type'</code>) first and only validates against the matching variant — O(1) instead of trying every option.",
    "zod-core")

c("ZodCore",
    "What is the difference between <code>.optional()</code>, <code>.nullable()</code>, and <code>.default()</code>?",
    "<code>.optional()</code> → <code>T | undefined</code> (key may be absent)<br><code>.nullable()</code> → <code>T | null</code> (key present, value may be null)<br><code>.default(v)</code> → fills in <code>v</code> if input is <code>undefined</code>, output is always <code>T</code>",
    "zod-core")

c("ZodCore",
    "What is the difference between <code>.parse()</code> and <code>.safeParse()</code>?",
    "<code>.parse(data)</code> — <b>throws</b> <code>ZodError</code> on failure.<br><code>.safeParse(data)</code> — returns a <b>discriminated result</b>:<br><code>{ success: true, data: T } | { success: false, error: ZodError }</code><br>Use <code>.safeParse</code> to avoid try/catch.",
    "zod-core")

c("ZodCore",
    "What does <code>.refine()</code> do in Zod?",
    "<code>z.string().refine(v =&gt; v.length &gt; 5, 'Too short')</code><br>Adds a <b>custom validation</b> on the parsed value. The function receives the already-parsed (typed) value and returns <code>boolean | void</code>. Can be <b>async</b>.",
    "zod-core")

c("ZodCore",
    "What does <code>.superRefine()</code> do and when do you need it?",
    "<code>.superRefine((val, ctx) =&gt; { ... })</code><br>Like <code>.refine()</code> but gives access to <code>ctx.addIssue({ code, message, path, ... })</code> for <b>multiple errors</b> or errors at <b>nested paths</b>. Use when one field's validity depends on another.",
    "zod-core")

c("ZodCore",
    "What does <code>.transform()</code> do in Zod?",
    "<code>z.string().transform(s =&gt; s.trim())</code><br>Maps the <b>parsed input to a new output type</b>. The output of a transform is what <code>z.infer</code> sees. Can chain after validation for sanitisation.",
    "zod-core")

c("ZodCore",
    "How do you extend, merge, pick, omit, partial, and required in Zod?",
    "<code>.extend({ extra: z.string() })</code> — add fields<br><code>.merge(OtherSchema)</code> — combine two objects<br><code>.pick({ a: true })</code> — keep only listed keys<br><code>.omit({ a: true })</code> — remove listed keys<br><code>.partial()</code> — all fields optional<br><code>.required()</code> — all fields required (opposite of <code>.partial()</code>)",
    "zod-core")

c("ZodCore",
    "How do you extract a TypeScript type from a Zod schema?",
    "<code>type User = z.infer&lt;typeof UserSchema&gt;</code><br>Also: <code>z.input&lt;S&gt;</code> (pre-transform input type) and <code>z.output&lt;S&gt;</code> (post-transform output type).",
    "zod-core")

c("ZodCore",
    "How do you handle and format Zod errors?",
    "<code>error.format()</code> — nested object mirroring schema shape with error messages.<br><code>error.flatten()</code> — flat <code>{ formErrors, fieldErrors }</code> object.<br><code>error.issues</code> — raw array of <code>{ code, message, path, ... }</code>.",
    "zod-core")

c("ZodCore",
    "How do you provide custom error messages in Zod?",
    "Pass a second argument or an options object:<br><code>z.string().min(5, 'Must be at least 5')</code><br><code>z.string().min(5, { message: 'Must be at least 5' })</code><br>Use <code>.refine(fn, { message: '...' })</code> for custom checks.",
    "zod-core")

c("ZodCore",
    "What is <code>z.coerce</code> and when to use it?",
    "<code>z.coerce.number()</code> — calls <code>Number(input)</code> before validating. <br>Use for form inputs (which always arrive as strings). Be careful: <code>Number('')</code> → <code>0</code>, which may be surprising. Prefer <code>z.preprocess()</code> for explicit control.",
    "zod-core")

c("ZodCore",
    "What does <code>z.preprocess()</code> do?",
    "<code>z.preprocess((val) =&gt; ..., z.string())</code><br>Transforms the <b>raw input</b> before any validation. Unlike <code>.transform()</code>, it runs before the schema's parsing (so val is <code>unknown</code>). Use for trimming, defaulting, or normalising inputs.",
    "zod-core")

c("ZodCore",
    "What is <code>z.custom()</code> in Zod?",
    "<code>z.custom&lt;BigInt&gt;((v) =&gt; typeof v === 'bigint')</code><br>Creates a schema for <b>any type</b> not natively supported. The <code>check</code> function receives <code>unknown</code> and returns <code>boolean</code>. Use sparingly — prefer <code>.refine()</code> on existing schemas.",
    "zod-core")

c("ZodCore",
    "What does <code>z.lazy()</code> do in Zod?",
    "Enables <b>recursive schemas</b>:<br><code>const Category = z.lazy(() =&gt; z.object({ name: z.string(), subcategories: z.array(Category) }))</code><br>The thunk <code>() =&gt; ...</code> defers evaluation until the schema is first used.",
    "zod-core")

c("ZodCore",
    "How do you make a field optional with a default value in Zod?",
    "<code>z.string().optional().default('guest')</code><br>The output type will be <code>string</code> (not <code>string | undefined</code>), because <code>.default()</code> eliminates <code>undefined</code>.",
    "zod-core")

c("ZodCore",
    "What is a Zod effect and how does <code>.refine()</code> differ from <code>.transform()</code>?",
    "<b>Effect</b> = any operation after the base parse. <code>.refine()</code> adds a <b>predicate</b> (fails if false); <code>.transform()</code> maps the value to a new type. Both can be chained, and you can have multiple transforms. <code>.pipe()</code> is also available in Zod for chaining schemas.",
    "zod-core")

c("ZodCore",
    "What is <code>.catch()</code> in Zod?",
    "<code>z.string().catch('default')</code><br>If parsing <b>fails</b>, returns the catch value instead of throwing. The output type becomes <code>string</code> (the error path is swallowed). Use for defensive parsing of external data.",
    "zod-core")

c("ZodCore",
    "How do you validate dates in Zod?",
    "<code>z.date()</code> — rejects invalid <code>new Date('bad')</code>.<br><code>z.coerce.date()</code> — parses strings/numbers to Date.<br>Chain: <code>.min(new Date('2020')), .max(new Date())</code>.",
    "zod-core")

# ================================================================
# 03 - Valibot Core API
# ================================================================

c("ValibotCore",
    "What is the import pattern for Valibot?",
    "Valibot uses <b>named imports</b> for every function:<br><code>import { string, number, object, parse, pipe, minLength } from 'valibot'</code><br>Each function is independently tree-shakable — import only what you need.",
    "valibot-core")

c("ValibotCore",
    "How do you define a string schema in Valibot?",
    "<code>import { string, pipe, minLength, maxLength, email } from 'valibot'</code><br><code>const s = pipe(string(), minLength(1), maxLength(255), email())</code><br>Validators are composed via <code>pipe()</code>, not method chaining.",
    "valibot-core")

c("ValibotCore",
    "How do you define a number schema in Valibot?",
    "<code>import { number, pipe, minValue, maxValue, integer } from 'valibot'</code><br><code>const n = pipe(number(), integer(), minValue(0), maxValue(100))</code><br>Functions: <code>minValue</code>, <code>maxValue</code>, <code>integer</code>, <code>multipleOf</code>, <code>finite</code>, <code>safeInteger</code>.",
    "valibot-core")

c("ValibotCore",
    "How do you define literal and enum schemas in Valibot?",
    "<code>literal('hello')</code> — matches exactly one value.<br><code>picklist(['red', 'green', 'blue'])</code> — union of literals.<br><code>enum_(MyEnum)</code> — for TypeScript enums (note the underscore to avoid keyword conflict).",
    "valibot-core")

c("ValibotCore",
    "How do you define an object schema in Valibot?",
    "<code>import { object, string, number } from 'valibot'</code><br><code>const User = object({ name: string(), age: number() })</code><br>By default, <b>unknown keys are stripped</b>. Use <code>strictObject()</code> to reject extra keys or <code>looseObject()</code> to pass them through.",
    "valibot-core")

c("ValibotCore",
    "How do you define array and tuple schemas in Valibot?",
    "<code>array(string())</code> — variable-length array.<br><code>tuple([string(), number()])</code> — fixed-length.<br>Pipe array validators: <code>pipe(array(string()), minLength(1), maxLength(10))</code>.",
    "valibot-core")

c("ValibotCore",
    "How do you define record, union, and variant in Valibot?",
    "<code>record(string(), number())</code> — <code>{ [k: string]: number }</code><br><code>union([string(), number()])</code> — A | B<br><code>variant('type', [...])</code> — discriminated union on the <code>'type'</code> key (Valibot's name for discriminatedUnion).",
    "valibot-core")

c("ValibotCore",
    "What is <code>variant()</code> in Valibot and how is it different from <code>union()</code>?",
    "<code>variant('type', [A, B])</code> is a <b>discriminated union</b>. It reads the <code>'type'</code> property first and validates only against the matching variant — faster and produces clearer errors than <code>union()</code>.",
    "valibot-core")

c("ValibotCore",
    "How do you make a field optional or nullable in Valibot?",
    "<code>optional(string())</code> — <code>T | undefined</code> (key may be absent)<br><code>nullable(string())</code> — <code>T | null</code><br><code>nullish(string())</code> — <code>T | null | undefined</code><br>Note: <code>optional()</code> wraps the schema, unlike Zod's chained <code>.optional()</code>.",
    "valibot-core")

c("ValibotCore",
    "What is <code>pipe()</code> in Valibot?",
    "<code>pipe()</code> is the <b>composition mechanism</b>. It takes a base schema and one or more validation/transformation actions:<br><code>pipe(string(), minLength(3), maxLength(100), toTrimmed())</code><br>Runs actions left-to-right. <b>Order matters!</b>",
    "valibot-core")

c("ValibotCore",
    "How do you parse data with Valibot?",
    "<code>parse(schema, input)</code> — returns typed output, <b>throws</b> <code>ValiError</code> on failure.<br><code>safeParse(schema, input)</code> — returns <b>discriminated result</b>:<br><code>{ success: true, output: T } | { success: false, issues: [...] }</code>",
    "valibot-core")

c("ValibotCore",
    "How do you add custom validation in Valibot?",
    "<code>check</code> function: <code>pipe(string(), check(v =&gt; v !== 'admin', 'Reserved name'))</code><br>Or <code>custom()</code> for more control:<br><code>custom&lt;string&gt;(v =&gt; typeof v === 'string' &amp;&amp; v.length &gt; 0, 'Not a non-empty string')</code>",
    "valibot-core")

c("ValibotCore",
    "How do you transform data in Valibot?",
    "<code>import { transform, toTrimmed, toLowerCase } from 'valibot'</code><br><code>pipe(string(), toTrimmed(), transform(s =&gt; s.toUpperCase()))</code><br>Built-in transforms: <code>toTrimmed</code>, <code>toLowerCase</code>, <code>toUpperCase</code>, <code>toMinValue</code>, <code>toMaxValue</code>.",
    "valibot-core")

c("ValibotCore",
    "How do you extract TypeScript types from a Valibot schema?",
    "<code>type UserInput = Input&lt;typeof UserSchema&gt;</code> — input type (what the schema accepts)<br><code>type UserOutput = Output&lt;typeof UserSchema&gt;</code> — output type (after transforms)<br>Use <code>GenericSchema</code> and <code>GenericSchemaAsync</code> for generic constraints.",
    "valibot-core")

c("ValibotCore",
    "How do you handle and format Valibot errors?",
    "<code>import { flatten, ValiError } from 'valibot'</code><br><code>flatten(error)</code> — returns <code>{ nested, root?: string }</code> with nested field errors.<br><code>error.issues</code> — raw array of <code>{ reason, validation, input, path, ... }</code>.<br><code>error.message</code> — human-readable summary.",
    "valibot-core")

c("ValibotCore",
    "How do you provide custom error messages in Valibot?",
    "Pass a <b>string message</b> as the last argument to validation functions:<br><code>pipe(string(), minLength(3, 'Must be at least 3 characters'))</code><br>This is <b>required</b> for user-facing errors — Valibot's default messages are technical.",
    "valibot-core")

c("ValibotCore",
    "How do you pick, omit, partial, and required in Valibot?",
    "<code>pick(UserSchema, ['name'])</code> — keep only listed keys<br><code>omit(UserSchema, ['password'])</code> — remove listed keys<br><code>partial(UserSchema)</code> — all fields optional<br><code>required(UserSchema)</code> — all fields required<br>These are standalone functions, not methods.",
    "valibot-core")

c("ValibotCore",
    "What is <code>coerce()</code> in Valibot?",
    "<code>import { coerce, number } from 'valibot'</code><br><code>const n = coerce(number(), input =&gt; Number(input))</code><br>Transforms input <b>before</b> validation. Unlike Zod's <code>z.coerce</code>, you provide the coercion function explicitly, giving more control.",
    "valibot-core")

c("ValibotCore",
    "What does <code>brand()</code> do in Valibot?",
    "<code>pipe(string(), brand('UserId'))</code><br>Creates a <b>branded/nominal type</b>: <code>string &amp; { __brand: 'UserId' }</code>. Enables distinguishing <code>UserId</code> from a plain <code>string</code> at the type level, preventing accidental mixing.",
    "valibot-core")

c("ValibotCore",
    "How do you define a schema with a default value in Valibot?",
    "<code>optional(string(), 'guest')</code><br>The second argument to <code>optional()</code> is the <b>default value</b>. If input is <code>undefined</code>, the default replaces it. The output type is <code>string</code> (not <code>string | undefined</code>).",
    "valibot-core")

c("ValibotCore",
    "How do you create recursive schemas in Valibot?",
    "Use <code>lazy()</code>:<br><code>const Category = lazy(() =&gt; object({ name: string(), children: array(Category) }))</code><br><code>lazy()</code> takes a thunk that returns the schema, deferring evaluation to avoid circular reference errors.",
    "valibot-core")

c("ValibotCore",
    "What is <code>forward()</code> used for in Valibot?",
    "<code>pipe(object({ a: string(), b: string() }), forward(check(..., ...), ['b']))</code><br>Forwards a validation <b>to a specific path</b> so the error points to the right field. Use when a validation on the whole object should be attributed to a specific nested key.",
    "valibot-core")

c("ValibotCore",
    "What is <code>partialCheck()</code> in Valibot?",
    "Like <code>check</code> but only runs if the input passes <b>a subset of validations first</b>. Useful when a cross-field check should only execute if individual fields are already valid, avoiding cascading errors.",
    "valibot-core")

c("ValibotCore",
    "How do you validate dates in Valibot?",
    "<code>import { date, pipe, minValue, maxValue } from 'valibot'</code><br><code>pipe(date(), minValue(new Date('2020-01-01')), maxValue(new Date()))</code><br>Valibot's <code>date()</code> schema validates <code>Date</code> objects.",
    "valibot-core")

c("ValibotCore",
    "What is the difference between <code>nullable_()</code> and <code>nullable()</code> in Valibot?",
    "<code>nullable(string())</code> — wraps a schema to accept <code>null</code>.<br><code>nullable_(string())</code> — outputs <b>non-nullable</b> type after parsing (the underscore variant). This is a v0.x artifact; in v1+ the API was simplified. Check current docs.",
    "valibot-core")

# ================================================================
# 04 - Advanced Patterns
# ================================================================

c("Advanced",
    "How do you create recursive schemas in Zod?",
    "<code>const Category = z.lazy(() =&gt; z.object({ name: z.string(), children: z.array(Category) }))</code><br>The thunk defers evaluation, breaking the circular reference. TypeScript infers the recursive type correctly.",
    "advanced")

c("Advanced",
    "How do you create recursive schemas in Valibot?",
    "<code>import { lazy, object, string, array } from 'valibot'</code><br><code>const Category = lazy(() =&gt; object({ name: string(), children: array(Category) }))</code><br>Same pattern as Zod's <code>z.lazy()</code> — thunk-based deferred evaluation.",
    "advanced")

c("Advanced",
    "How do you perform async validation in Zod?",
    "<code>z.string().refine(async (v) =&gt; { const exists = await db.check(v); return exists; }, 'Already taken')</code><br>Use <code>.safeParseAsync()</code> or <code>.parseAsync()</code> — they return <code>Promise</code>. Async <code>.refine</code> and <code>.transform</code> are fully supported.",
    "advanced")

c("Advanced",
    "How do you perform async validation in Valibot?",
    "<code>import { pipeAsync, checkAsync } from 'valibot'</code><br><code>pipeAsync(string(), checkAsync(async (v) =&gt; { ... }, 'Error'))</code><br>Use <code>safeParseAsync()</code> or <code>parseAsync()</code>. Async validations use <code>pipeAsync()</code> instead of <code>pipe()</code>.",
    "advanced")

c("Advanced",
    "How do you compose and reuse schema fragments in Zod?",
    "Extract common fields into a <b>base schema</b>:<br><code>const WithTimestamps = z.object({ createdAt: z.date(), updatedAt: z.date() })</code><br><code>const User = WithTimestamps.extend({ name: z.string() })</code><br>Or use <code>.merge()</code> to combine two independent schemas.",
    "advanced")

c("Advanced",
    "How do you compose and reuse schema fragments in Valibot?",
    "Use <b>object merging</b>:<br><code>const WithTimestamps = object({ createdAt: date(), updatedAt: date() })</code><br><code>const User = merge([WithTimestamps, object({ name: string() })])</code><br>Valibot's <code>merge()</code> function combines multiple object schemas.",
    "advanced")

c("Advanced",
    "What are branded/nominal types and how do they work in Zod?",
    "Zod has <code>.brand&lt;'Name'&gt;()</code>:<br><code>const UserId = z.string().brand('UserId')</code><br>Creates <code>string &amp; z.BRAND&lt;'UserId'&gt;</code> — structurally still a string but TypeScript treats it as a distinct type, preventing accidental mixing with plain strings.",
    "advanced")

c("Advanced",
    "What are branded/nominal types and how do they work in Valibot?",
    "Valibot uses the <code>brand()</code> action:<br><code>pipe(string(), brand('UserId'))</code><br>Creates a branded string type. Both Zod and Valibot support the same pattern — useful for <code>UserId</code>, <code>Email</code>, <code>OrderId</code> etc.",
    "advanced")

c("Advanced",
    "How do you convert Zod schemas to JSON Schema?",
    "Use <code>z.toJSONSchema()</code> (available via <code>zod-to-json-schema</code> package):<br><code>import { zodToJsonSchema } from 'zod-to-json-schema'</code><br><code>const jsonSchema = zodToJsonSchema(MySchema)</code><br>Or use the built-in (v3.22+) utility via community packages.",
    "advanced")

c("Advanced",
    "How do you convert Valibot schemas to JSON Schema?",
    "Use <code>toJsonSchema()</code>:<br><code>import { toJsonSchema } from '@valibot/to-json-schema'</code><br><code>const jsonSchema = toJsonSchema(MySchema)</code><br>Valibot provides this as a separate, tree-shakable package.",
    "advanced")

c("Advanced",
    "How do you integrate Zod with React Hook Form?",
    "Use <code>@hookform/resolvers/zod</code>:<br><code>import { zodResolver } from '@hookform/resolvers/zod'</code><br><code>const form = useForm({ resolver: zodResolver(MySchema) })</code><br>Errors are automatically mapped from <code>ZodError</code> to field-level form errors.",
    "advanced")

c("Advanced",
    "How do you integrate Valibot with React Hook Form?",
    "Use <code>@hookform/resolvers/valibot</code>:<br><code>import { valibotResolver } from '@hookform/resolvers/valibot'</code><br><code>const form = useForm({ resolver: valibotResolver(MySchema) })</code><br>Same pattern as Zod — the resolver adapter handles error mapping.",
    "advanced")

c("Advanced",
    "How do you use schemas for tRPC input validation?",
    "tRPC supports Zod natively:<br><code>t.procedure.input(UserSchema).query(...)</code><br>Valibot works via adapter or by manually calling <code>parse()</code>:<br><code>input: UserSchema</code> if using a valibot-tRPC adapter, or:<br><code>const validated = parse(UserSchema, ctx.input)</code> in a middleware.",
    "advanced")

c("Advanced",
    "How do schemas enable 'schema-first API design'?",
    "Define your <b>API contracts as schemas</b> first, then:<br>1. Extract types with <code>z.infer</code> / <code>Output</code><br>2. Validate at runtime in handlers<br>3. Generate OpenAPI/Swagger docs<br>4. Share schemas between client &amp; server (monorepo or published package)",
    "advanced")

c("Advanced",
    "How do you generate OpenAPI / Swagger documentation from schemas?",
    "<b>Zod</b>: <code>@asteasolutions/zod-to-openapi</code> or <code>zod-openapi</code> — creates OpenAPI 3.x specs directly from Zod schemas with annotations.<br><b>Valibot</b>: Convert to JSON Schema first via <code>toJsonSchema()</code>, then use tools like <code>openapi-json-schema</code>.",
    "advanced")

c("Advanced",
    "How do you use schemas for runtime contract testing?",
    "Write <b>integration tests</b> that validate real API responses against your schemas:<br><code>const res = await fetch('/api/users/1')</code><br><code>const data = UserSchema.parse(await res.json())</code><br>If the API changes shape, tests fail immediately — catching contract breaks before users do.",
    "advanced")

c("Advanced",
    "What is zod-to-ts and what problem does it solve?",
    "<code>zod-to-ts</code> generates TypeScript <b>type definitions</b> from Zod schemas as strings, useful for library authors who want to ship types without shipping Zod. Valibot can achieve similar results with <code>Output</code> type extraction at build time.",
    "advanced")

c("Advanced",
    "How do you handle nullable vs optional in API design with schemas?",
    "<b>Optional</b> (<code>undefined</code>) = field may be <b>absent</b> from the payload.<br><b>Nullable</b> (<code>null</code>) = field is present but has no value.<br>In PATCH endpoints, optional means 'don't change', while nullable means 'clear this field'. Both libraries support this distinction.",
    "advanced")

c("Advanced",
    "What is the 'strip vs strict vs passthrough' distinction for object schemas?",
    "<b>Strip</b> (default in both): unknown keys are silently removed.<br><b>Strict</b>: unknown keys cause a validation error.<br><b>Passthrough</b> (Zod) / Loose (Valibot): unknown keys pass through unchanged.<br>Zod: <code>.strict()</code>, <code>.passthrough()</code>. Valibot: <code>strictObject()</code>, <code>looseObject()</code>.",
    "advanced")

# ================================================================
# 05 - Comparison
# ================================================================

c("Comparison",
    "What is the bundle size comparison: Zod vs Valibot?",
    "<b>Valibot</b>: ~1 KB for a minimal schema (tree-shaken). Core ~7 KB with common validators.<br><b>Zod</b>: ~12 KB min+gzip (v3.x), ~15 KB (v4 alpha). Zod includes everything — tree-shaking is ineffective because the <code>z</code> object is a single namespace import.",
    "comparison")

c("Comparison",
    "Why is Valibot tree-shakable while Zod is not?",
    "Valibot exports <b>individual functions</b> (<code>string</code>, <code>number</code>, <code>minLength</code>, etc.). Each is a standalone module — bundlers can eliminate unused ones. Zod exports a <b>single namespace object</b> <code>z</code> with all methods, which bundlers cannot tree-shake.",
    "comparison")

c("Comparison",
    "How does the API style differ: Zod method chaining vs Valibot functional composition?",
    "Zod: <code>z.string().min(3).max(100).email()</code><br>Valibot: <code>pipe(string(), minLength(3), maxLength(100), email())</code><br>Zod feels more <b>declarative</b>; Valibot is more <b>explicit</b> about ordering and dependencies.",
    "comparison")

c("Comparison",
    "Which library has better TypeScript inference?",
    "Both are <b>excellent</b>. Zod uses <code>z.infer</code>; Valibot uses <code>Input</code> and <code>Output</code>. Minor differences:<br>- Valibot separates input/output types (useful for transforms)<br>- Zod's <code>z.infer</code> gives the output type; use <code>z.input</code> for pre-transform<br>- Both handle recursive types correctly",
    "comparison")

c("Comparison",
    "How do error messages compare between Zod and Valibot?",
    "<b>Zod</b> generates <b>user-friendly messages by default</b>:<br><code>'Expected string, received number'</code><br><b>Valibot</b> messages are more <b>technical by default</b>:<br><code>'Invalid type: Expected string but received 123'</code><br>Valibot <b>requires</b> explicit messages for user-facing errors; Zod gives decent defaults.",
    "comparison")

c("Comparison",
    "How do the ecosystems compare?",
    "<b>Zod</b>: Very mature — React Hook Form, tRPC, Next.js, TanStack, Conform, dnd-kit, Prisma (zod-prisma), OpenAPI/Swagger generators, and tens of thousands of tutorials.<br><b>Valibot</b>: Growing fast — RHF, Conform, Modular Forms, tRPC (adapters), JSON Schema conversion. Smaller but expanding ecosystem.",
    "comparison")

c("Comparison",
    "Which library is faster for validation?",
    "<b>Valibot</b> is generally <b>faster</b>, especially for large/complex schemas. Its functional, modular design avoids the overhead of Zod's method chaining and object creation. For most apps the difference is negligible; for high-throughput APIs, Valibot may matter.",
    "comparison")

c("Comparison",
    "What are the performance characteristics of discriminated unions in each library?",
    "<b>Zod</b>: <code>z.discriminatedUnion()</code> is an explicit opt-in; <code>z.union()</code> tries every variant until one passes.<br><b>Valibot</b>: <code>variant()</code> is also optimised — reads the discriminator first and validates only one branch.<br>Both skip unnecessary validation when the discriminator matches.",
    "comparison")

c("Comparison",
    "When should you choose Zod over Valibot?",
    "Choose <b>Zod</b> when:<br>- Team is already familiar with it<br>- You need the mature ecosystem (tRPC, tutorials, Stack Overflow)<br>- You prefer method chaining<br>- Bundle size is not a primary concern (server-side Node.js)<br>- You need complex transforms with minimal boilerplate",
    "comparison")

c("Comparison",
    "When should you choose Valibot over Zod?",
    "Choose <b>Valibot</b> when:<br>- Bundle size matters (edge functions, browsers, Cloudflare Workers)<br>- You prefer functional/modular style<br>- You want explicit control over what's imported<br>- You're starting a new project and want the smallest footprint<br>- You need maximum tree-shaking for a library/SDK",
    "comparison")

c("Comparison",
    "How hard is it to migrate from Zod to Valibot?",
    "Moderate effort. The concepts are similar but the API is inverted:<br>- <code>z.string().min(3)</code> → <code>pipe(string(), minLength(3))</code><br>- <code>.optional()</code> is a method in Zod, a wrapper in Valibot<br>- <code>.refine()</code> → <code>check()</code> or <code>custom()</code><br>- <code>z.infer</code> → <code>Output</code><br>Use <code>valibot-compat</code> or <code>valibot/toZod</code> helpers for gradual migration.",
    "comparison")

c("Comparison",
    "Can you use Zod and Valibot together in the same project?",
    "Yes. They are independent libraries. You might use Valibot for client-side form validation (smaller bundle) and Zod for server-side API validation (mature ecosystem). Be aware of duplicated bundle size if both end up in the same chunk.",
    "comparison")

c("Comparison",
    "How do the two libraries handle <code>undefined</code> and <code>null</code>?",
    "Both treat <code>undefined</code> and <code>null</code> as distinct from each other and from the base type. Neither coerces <code>null</code> to <code>undefined</code> unless explicitly configured. Zod: <code>.optional()</code> / <code>.nullable()</code>. Valibot: <code>optional()</code> / <code>nullable()</code> wrappers.",
    "comparison")

c("Comparison",
    "What is the default behaviour for unknown object keys in each library?",
    "Both <b>strip unknown keys by default</b> (they're silently removed).<br>Zod: <code>.strict()</code> to reject, <code>.passthrough()</code> to keep.<br>Valibot: <code>strictObject()</code> to reject, <code>looseObject()</code> to keep.<br>This is a deliberate choice for defensive parsing of external API responses.",
    "comparison")

c("Comparison",
    "How do Zod and Valibot handle coercion differently?",
    "<b>Zod</b>: <code>z.coerce.number()</code> — built-in coercions for primitives, but limited to predefined rules.<br><b>Valibot</b>: <code>coerce(number(), fn)</code> — you provide the coercion function, giving full control over how the input is transformed before validation.",
    "comparison")

# ================================================================
# 06 - Gotchas
# ================================================================

c("Gotchas",
    "What is the <code>.passthrough()</code> vs <code>.strict()</code> gotcha in Zod?",
    "By default, <code>z.object({...})</code> <b>strips unknown keys silently</b>. If your API relies on rejecting extra fields, you <b>must</b> explicitly use <code>.strict()</code>. Forgetting this means unexpected fields are accepted and silently dropped — a common source of bugs when validating API responses.",
    "gotchas")

c("Gotchas",
    "What is the <code>strictObject()</code> vs <code>looseObject()</code> gotcha in Valibot?",
    "By default, <code>object()</code> <b>strips unknown keys</b>, same as Zod. If you want to keep extra fields, use <code>looseObject()</code>. If you want to reject them, use <code>strictObject()</code>. Always be explicit about your intent.",
    "gotchas")

c("Gotchas",
    "Zod: <code>.refine()</code> does NOT run on optional fields when value is <code>undefined</code>. Why?",
    "<code>z.string().optional().refine(...)</code> — if the field is <b>absent</b> (undefined), <code>.refine()</code> is <b>skipped</b>. This is by design: optional means 'may or may not be present'. If you need to validate when present, put <code>.refine()</code> on the inner schema before <code>.optional()</code>:<br><code>z.string().refine(...).optional()</code>",
    "gotchas")

c("Gotchas",
    "Valibot: <code>pipe()</code> order matters. Why and what can go wrong?",
    "Validations in <code>pipe()</code> run <b>left to right</b>. If a transform runs before a validation, the validation receives the transformed value, not the original. Example: <code>pipe(string(), toTrimmed(), minLength(3))</code> checks trimmed length — which may pass even if the original had leading spaces. Usually this is desired, but be aware.",
    "gotchas")

c("Gotchas",
    "Zod: What is the <code>z.coerce</code> empty-string-to-number surprise?",
    "<code>z.coerce.number().parse('')</code> → <code>0</code> (not an error).<br><code>Number('')</code> is <code>0</code> in JavaScript. If you expect empty form fields to be treated as missing, use <code>z.preprocess((v) =&gt; v === '' ? undefined : v, z.number().optional())</code>.",
    "gotchas")

c("Gotchas",
    "Valibot: What is the <code>coerce()</code> empty-string-to-number surprise?",
    "Same as Zod: <code>coerce(number(), (v) =&gt; Number(v))</code> turns <code>''</code> into <code>0</code>. The solution is to handle the empty case in the coercion function:<br><code>coerce(number(), (v) =&gt; v === '' ? NaN : Number(v))</code> — then <code>number()</code> rejects <code>NaN</code>.",
    "gotchas")

c("Gotchas",
    "What is the discriminated union gotcha when the discriminator value is missing?",
    "In both libraries, if the discriminator key (e.g. <code>'type'</code>) is <b>missing</b> from the input, the error message can be confusing — it tries every variant and fails all of them. Solution: validate the discriminator exists first, or use a <b>base schema</b> that includes the discriminator as <code>.literal()</code>.",
    "gotchas")

c("Gotchas",
    "How does TypeScript strict mode interact with Zod and Valibot schemas?",
    "With <code>strictNullChecks</code> on, optional/nulled fields are correctly reflected in inferred types. With it off, <code>null</code> and <code>undefined</code> are assignable to everything — inferred types lose precision. <b>Always enable strictNullChecks</b> when using schema libraries.",
    "gotchas")

c("Gotchas",
    "Zod: What happens when you chain <code>.optional().default(...)</code> vs <code>.default(...).optional()</code>?",
    "<code>.optional().default(v)</code> — input is optional, output is always <code>T</code> (default fills in).<br><code>.default(v).optional()</code> — makes the <b>entire result</b> optional again, output is <code>T | undefined</code>. The order of optional/default in the chain determines the output type.",
    "gotchas")

c("Gotchas",
    "Valibot: What happens with <code>optional()</code> and <code>pipe()</code> ordering?",
    "Wrap the <b>piped schema</b> in <code>optional()</code>:<br><code>optional(pipe(string(), minLength(3)))</code> — validates only if present.<br>Do NOT put <code>optional</code> inside <code>pipe()</code>:<br><code>pipe(optional(string()), minLength(3))</code> — would try to check length on <code>undefined</code>, which makes no sense.",
    "gotchas")

c("Gotchas",
    "Date validation gotcha: <code>new Date('invalid')</code> is NOT a validation error in either library?",
    "Zod's <code>z.date()</code> and Valibot's <code>date()</code> <b>do reject</b> invalid Date objects (<code>NaN</code>). However, both accept <b>any valid Date</b> — including dates like year 10,000. Use <code>.min()</code> and <code>.max()</code> to constrain the range.",
    "gotchas")

c("Gotchas",
    "What is the 'ZodError not thrown' gotcha with <code>.safeParse()</code>?",
    "<code>.safeParse()</code> returns a result object — it <b>never throws</b>. If you forget to check <code>result.success</code> and access <code>result.data</code>, TypeScript will flag it (discriminated union), but at runtime you could get <code>undefined</code> if you bypass type checking.",
    "gotchas")

c("Gotchas",
    "What is the 'Valibot parse vs safeParse' gotcha?",
    "Same as Zod: <code>parse()</code> throws <code>ValiError</code>; <code>safeParse()</code> returns a result object. Always use <code>safeParse()</code> for user input and <code>parse()</code> only when you want the throw-on-failure behaviour (e.g. for configuration that must be correct).",
    "gotchas")

c("Gotchas",
    "Zod: How does <code>.catch()</code> affect the inferred type?",
    "<code>.catch(defaultValue)</code> changes the <b>output type</b> to non-optional. The error is swallowed and replaced with the default. This can hide schema mismatches — use <code>.catch()</code> only for truly optional external data where a fallback is safe.",
    "gotchas")

c("Gotchas",
    "Valibot: What is the <code>nullable()</code> vs <code>nullish()</code> vs <code>optional()</code> confusion?",
    "<code>nullable()</code> → <code>T | null</code><br><code>optional()</code> → <code>T | undefined</code><br><code>nullish()</code> → <code>T | null | undefined</code><br>Using the wrong one can cause subtle type mismatches, especially when your API uses <code>null</code> for 'no value' but your form library uses <code>undefined</code>.",
    "gotchas")

# ================================================================
# 07 - Expert Opinions
# ================================================================

c("Expert",
    "How do you create a custom schema in Zod?",
    "<code>z.custom&lt;T&gt;(checkFn, params?)</code><br><code>const BigInt = z.custom&lt;bigint&gt;(v =&gt; typeof v === 'bigint', 'Expected bigint')</code><br>For more control, use <code>z.custom()</code> with a <code>ZodType</code> subclass, implementing <code>_parse()</code> for full control over parsing and error generation.",
    "expert")

c("Expert",
    "How do you create a custom schema in Valibot?",
    "<code>import { custom, BaseSchema } from 'valibot'</code><br><code>const BigInt = custom&lt;bigint&gt;(v =&gt; typeof v === 'bigint' ? { output: v } : { issues: [{ reason: 'type', ... }] })</code><br>Return <code>{ output }</code> on success or <code>{ issues }</code> on failure. For advanced use, implement <code>BaseSchema</code> or <code>BaseValidation</code>.",
    "expert")

c("Expert",
    "How do you create reusable validation functions with <code>pipe</code> in Valibot?",
    "Define a validator as a function that returns a <code>BaseValidation</code>:<br><code>const isNotReserved = (name: string) =&gt; check((v: string) =&gt; v !== name, `Cannot use '${name}'`)</code><br>Then compose: <code>pipe(string(), isNotReserved('admin'), isNotReserved('root'))</code><br>This is Valibot's primary composition pattern.",
    "expert")

c("Expert",
    "How do you create reusable validation functions in Zod?",
    "Wrap <code>.refine()</code> or <code>.superRefine()</code> in a helper function:<br><code>const notReserved = (name: string) =&gt; (s: z.ZodString) =&gt; s.refine(v =&gt; v !== name, `Cannot use '${name}'`)</code><br>Use with <code>pipe()</code> or manually chain. Zod 4 introduced <code>.pipe()</code> for composition too.",
    "expert")

c("Expert",
    "What is schema-first API design and why does it matter?",
    "Define your API's data contracts as schemas first, then <b>generate</b> types, validation, and documentation from them — not the other way around. The schema is the single source of truth. Both Zod and Valibot enable this: write the schema, extract types with <code>z.infer</code> / <code>Output</code>.",
    "expert")

c("Expert",
    "How do you share schemas between client and server?",
    "Put schemas in a <b>shared package</b> (monorepo workspace or published npm package):<br><code>@myapp/schemas</code> exports <code>UserSchema</code>, <code>CreateUserSchema</code>, etc.<br>Both client (form validation) and server (API validation) import the same schema — guaranteeing consistency.",
    "expert")

c("Expert",
    "How can you use Zod/Valibot schemas for environment variable validation?",
    "Validate on startup:<br><code>const env = EnvSchema.parse(process.env)</code><br>If the schema fails, the app fails fast with a clear error instead of crashing mysteriously later. Use <code>z.coerce</code> / <code>coerce()</code> because env vars are always strings. Popularised by T3 stack and env-validated patterns.",
    "expert")

c("Expert",
    "How do you generate types from JSON Schema (reverse of schema-to-JSON)?",
    "Both libraries support the forward path (schema → JSON Schema). For the reverse (JSON Schema → Zod/Valibot), use tools like <code>json-schema-to-zod</code> or <code>json-schema-to-valibot</code>. Useful when integrating with external APIs that publish JSON Schema definitions.",
    "expert")

c("Expert",
    "What is the <code>z.promise()</code> schema in Zod?",
    "<code>z.promise(z.string())</code> validates that a value is a <code>Promise&lt;string&gt;</code>. Mostly useful for testing async function return values, not for typical API validation. Valibot does not have a direct equivalent — you'd validate the resolved value instead.",
    "expert")

c("Expert",
    "What is the <code>z.function()</code> schema in Zod?",
    "<code>z.function(z.tuple([z.string()]), z.number())</code><br>Validates a function's <b>arguments and return type</b> at runtime. Niche feature — mainly used for plugin systems or runtime contract enforcement. Valibot does not have an equivalent; validate the call manually.",
    "expert")

c("Expert",
    "How do you approach large schema refactoring safely?",
    "1. Write tests that validate <b>known-good outputs</b> against the schema<br>2. Use <code>.safeParse()</code> in tests to get detailed errors<br>3. Refactor the schema, run tests<br>4. Update inferred types — any breaking type changes will show at compile time<br>Both libraries' <code>safeParse</code> makes this workflow reliable.",
    "expert")

c("Expert",
    "What is the Zod 4 roadmap and how does it affect comparison with Valibot?",
    "Zod 4 (alpha) is a <b>complete rewrite</b> aiming for:<br>- Smaller bundle size<br>- Better tree-shaking<br>- Faster validation<br>- Plugin system<br>This addresses Valibot's key advantages. Until stable, Zod 3 remains the production choice; Valibot's lead on bundle size may shrink.",
    "expert")

c("Expert",
    "How does Valibot's modularity affect library/SDK authors?",
    "If you're a library author, importing Zod adds ~12 KB to every consumer. Valibot's tree-shaking means consumers only pay for the validators they actually use from your library's schema definitions — a significant advantage for SDK development.",
    "expert")

c("Expert",
    "What is the 'parse, don't validate' principle applied to API clients?",
    "When consuming a third-party API, validate the response with a schema even if it's documented. APIs change, docs are wrong, networks corrupt data. A schema parse at the boundary catches these issues immediately with clear errors, rather than propagating <code>undefined</code> bugs throughout your app.",
    "expert")

# ================================================================
# Assemble and write
# ================================================================

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
