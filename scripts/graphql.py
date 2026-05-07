import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "GraphQL"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "Queries":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Queries"),
    "Mutations":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Mutations"),
    "Schema":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Schema-Design"),
    "Subscriptions":genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Subscriptions-RealTime"),
    "Performance":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Performance"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ─────────────────────────────────────────────────────────
# 01 – Fundamentals  (~18 cards)
# ─────────────────────────────────────────────────────────

c("Fundamentals",
  "What is GraphQL?",
  "A <b>query language</b> for APIs and a <b>runtime</b> for fulfilling those queries with your existing data. It provides a complete description of the data in your API, gives clients the power to ask for exactly what they need, and nothing more.",
  ["graphql", "L0"])

c("Fundamentals",
  "How does GraphQL differ from REST? (3 key points)",
  "<b>1. Single endpoint</b> – all queries go to <code>POST /graphql</code> (or GET).<br><b>2. Client-specified fields</b> – the client requests exactly which fields to return, avoiding over-fetching and under-fetching.<br><b>3. Strongly-typed schema</b> – the schema serves as a contract between client and server.",
  ["graphql", "L0"])

c("Fundamentals",
  "What is over-fetching and under-fetching in REST?",
  "<b>Over-fetching:</b> The endpoint returns more data than the client needs (e.g., <code>GET /users</code> returning email, address when you only need name).<br><b>Under-fetching:</b> The client must make multiple round-trips to get all needed data (e.g., fetch user, then fetch user's posts, then fetch each post's comments). GraphQL solves both.",
  ["graphql", "L0"])

c("Fundamentals",
  "What are the three operation types in GraphQL?",
  "<pre>\n1. query    – read data (like GET)\n2. mutation – write/change data (like POST/PUT/DELETE)\n3. subscription – real-time push-based updates\n</pre>",
  ["graphql", "L0"])

c("Fundamentals",
  "Is GraphQL a database?",
  "No. GraphQL is a <b>specification</b> for a query language and execution engine. It sits <b>between</b> the client and your data sources (databases, REST APIs, microservices). It does not dictate or care how you store your data.",
  ["graphql", "L0"])

c("Fundamentals",
  "What does the GraphQL type system serve as?",
  "A <b>contract</b> between client and server. The schema defines what data is available, what types exist, and the relationships between them. Clients can introspect the schema at runtime.",
  ["graphql", "L0"])

c("Fundamentals",
  "How does the GraphQL request flow work?",
  "<pre>\nClient sends: POST /graphql with JSON body\n  { \"query\": \"{ user(id: 1) { name } }\" }\n\nServer:\n  1. Parse the query string into an AST\n  2. Validate against schema\n  3. Execute: call resolvers for each field\n  4. Return JSON matching the query shape\n</pre>",
  ["graphql", "L0"])

c("Fundamentals",
  "Compare GraphQL vs REST vs gRPC.",
  "<table>\n<tr><th></th><th>GraphQL</th><th>REST</th><th>gRPC</th></tr>\n<tr><td>Endpoints</td><td>Single</td><td>Multiple</td><td>RPC methods</td></tr>\n<tr><td>Data shape</td><td>Client-driven</td><td>Server-defined</td><td>Protobuf-defined</td></tr>\n<tr><td>Transport</td><td>HTTP (mostly)</td><td>HTTP</td><td>HTTP/2</td></tr>\n<tr><td>Caching</td><td>Complex (POST)</td><td>Easy (URL-based)</td><td>Not built-in</td></tr>\n<tr><td>Versioning</td><td>None (deprecate fields)</td><td>URL versioning</td><td>Protobuf field numbers</td></tr>\n</table>",
  ["graphql", "L0"])

c("Fundamentals",
  "What does GraphQL NOT solve well?",
  "<b>1. Caching</b> – mostly POST, complex to cache at HTTP level.<br><b>2. File uploads</b> – not natively supported (need graphql-upload spec or separate endpoint).<br><b>3. Complex aggregation</b> – no built-in aggregation framework; must build custom resolvers.<br><b>4. Simple CRUD</b> – overkill if REST does the job fine.",
  ["graphql", "L0"])

c("Fundamentals",
  "Write the minimal valid GraphQL query.",
  "<pre>\nquery {\n  __typename\n}\n\n# Or just:\n{ __typename }\n</pre>\nThe query operation type and name are optional; <code>{ }</code> alone is a valid shorthand query.",
  ["graphql", "L0"])

c("Fundamentals",
  "What is the query shorthand syntax?",
  "Omitting the <code>query</code> keyword and operation name:<pre>\n# Full form:\nquery GetUsers { users { name } }\n\n# Shorthand (operation type defaults to \"query\"):\n{ users { name } }\n</pre>Only works for queries; mutations and subscriptions MUST include the keyword.",
  ["graphql", "L0"])

c("Fundamentals",
  "What transport layer does GraphQL use?",
  "Primarily <b>HTTP</b> (POST to <code>/graphql</code>, or GET for short queries). Subscriptions use <b>WebSocket</b> (graphql-ws protocol). Some implementations support HTTP/2, SSE (Server-Sent Events), or multipart for incremental delivery (<code>@defer</code>/<code>@stream</code>).",
  ["graphql", "L0"])

c("Fundamentals",
  "How does the GraphQL response shape relate to the request shape?",
  "The response JSON <b>mirrors</b> the request structure:<pre>\n# Query:\n{ hero { name friends { name } } }\n\n# Response:\n{ \"data\": { \"hero\": { \"name\": \"Luke\",\n  \"friends\": [{\"name\": \"Han\"}, {\"name\": \"Leia\"}] } } }\n</pre>",
  ["graphql", "L0"])

c("Fundamentals",
  "What goes in the top-level <code>\"errors\"</code> key of a GraphQL response?",
  "Operational errors (schema validation, query parse errors, resolver exceptions). They are separate from the <code>\"data\"</code> key — a response can contain <b>both</b> <code>\"data\"</code> and <code>\"errors\"</code>, meaning partial data was returned alongside errors for some fields.",
  ["graphql", "L0"])

c("Fundamentals",
  "What is resolver-based execution?",
  "Each <b>field</b> in a GraphQL schema has an associated <b>resolver function</b>. The engine calls resolvers in a depth-first, parallel fashion for independent branches, collecting results into the final JSON response.",
  ["graphql", "L0"])

c("Fundamentals",
  "What are the four arguments passed to every resolver?",
  "<pre>\nresolve(parent, args, context, info)\n\nparent   – resolved value of the parent field\nargs     – arguments passed in the query (e.g., id: 1)\ncontext  – shared mutable context (auth, DB, etc.)\ninfo     – the full field AST and schema info\n</pre>",
  ["graphql", "L0"])

c("Fundamentals",
  "What is the `graphql` npm package vs `apollo-server` vs `express-graphql`?",
  "<b>graphql</b> – reference JS implementation of the GraphQL spec (parse, validate, execute).<br><b>graphql-http</b> (née express-graphql) – HTTP middleware for GraphQL.<br><b>apollo-server</b> – production-ready GraphQL server by Apollo with batteries included.<br>You always need <code>graphql</code>; the rest are server frameworks built on top.",
  ["graphql", "L0"])

c("Fundamentals",
  "What is a `selection set` in GraphQL?",
  "The set of fields requested within curly braces <code>{ ... }</code>. The selection set of every field is resolved in parallel (except mutations, which are top-level sequential).<pre>\n{ hero {           # selection set of query\n  name             # scalar — no sub-selection\n  friends {        # object — has sub-selection set\n    name\n  }\n} }\n</pre>",
  ["graphql", "L0"])

# ─────────────────────────────────────────────────────────
# 02 – Queries  (~22 cards)
# ─────────────────────────────────────────────────────────

c("Queries",
  "What are GraphQL fields and nested fields? Write an example.",
  "Fields are the units of data you request. Nested fields traverse relationships.<pre>\nquery {\n  hero {\n    name\n    homeworld {       # nested field\n      name\n      population\n    }\n  }\n}\n</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What is a field alias in GraphQL? Write an example.",
  "Aliases let you request the same field with different arguments in one query:<pre>\nquery {\n  empireHero: hero(episode: EMPIRE) {\n    name\n  }\n  jediHero: hero(episode: JEDI) {\n    name\n  }\n}\n</pre>Response keys become <code>\"empireHero\"</code> and <code>\"jediHero\"</code>.",
  ["graphql", "L1", "queries"])

c("Queries",
  "What are field arguments in GraphQL?",
  "Arguments are key-value pairs passed to fields to filter, paginate, or transform data. Every field can accept zero or more arguments defined in the schema.<pre>\nquery {\n  human(id: \"1000\") {   # \"id\" is an argument\n    name\n    height(unit: FOOT) # \"unit\" is an argument\n  }\n}\n</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What are fragments and why use them?",
  "Fragments are <b>reusable units</b> of a GraphQL query. They prevent duplicating field sets across multiple queries or parts of a query.<pre>\nfragment NameParts on Person {\n  firstName\n  lastName\n  title\n}\n\n# Usage with spread:\nquery {\n  leftPerson: person(id: 1) { ...NameParts }\n  rightPerson: person(id: 2) { ...NameParts }\n}\n</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What is the difference between named and inline fragments?",
  "<b>Named fragment:</b> defined with <code>fragment Name on Type { fields }</code>, reusable, must specify type condition.<br><b>Inline fragment:</b> defined inline with <code>... on Type { fields }</code>, used for union/interface type resolution or conditional fields.<pre>\nquery {\n  search(text: \"an\") {\n    __typename\n    ... on Human { height }\n    ... on Droid { primaryFunction }\n  }\n}\n</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What are variables and how do you use them?",
  "Variables make queries reusable and prevent string interpolation. Declare with <code>$varName: Type!</code> and pass in a separate JSON dictionary.<pre>\nquery HeroName($episode: Episode!, $withFriends: Boolean!) {\n  hero(episode: $episode) {\n    name\n    friends @include(if: $withFriends) { name }\n  }\n}\n\n# Variables (JSON):\n{ \"episode\": \"JEDI\", \"withFriends\": true }\n</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What are variable type modifiers (<code>!</code> and <code>[...]</code>)?",
  "<code>$name: String!</code> – non-null variable (required).<br><code>$ids: [Int!]!</code> – non-null list of non-null Ints.<br><code>$tags: [String]</code> – nullable list of nullable Strings.<br><code>$input: [Int]!</code> – required list of nullable Ints.<br>The <code>!</code> means the value cannot be null; <code>[]</code> means a list.",
  ["graphql", "L1", "queries"])

c("Queries",
  "What is an operation name? When is it required?",
  "An operation name is an identifier after the operation type keyword. It is <b>required</b> when sending <b>multiple operations</b> in one document (and you must specify which to execute via <code>operationName</code>).<pre>\nquery GetHero { hero { name } }\nmutation CreateUser { ... }\n\n# Single operation: name is optional\n# Multiple operations: name is required, plus 'operationName' param\n</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What do the built-in directives @include and @skip do?",
  "<code>@include(if: Boolean!)</code> – include the field/fragment only if condition is true.<br><code>@skip(if: Boolean!)</code> – skip the field/fragment if condition is true.<pre>\nquery($showDetails: Boolean!) {\n  hero {\n    name\n    birthYear @include(if: $showDetails)\n    height @skip(if: true)   # never shown\n  }\n}\n</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What is introspection and why is it useful?",
  "Introspection lets you query the schema itself at runtime. Tools like <b>GraphiQL</b>, <b>GraphQL Playground</b>, and code generators use it to provide autocompletion, documentation, and type-safe code.<pre>\nquery {\n  __schema {\n    types { name kind }\n  }\n  __type(name: \"Character\") {\n    fields { name type { name kind } }\n  }\n}\n</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What meta-fields are available on every type?",
  "<code>__typename</code> – returns the type name of an object (indispensable for union/interface resolution in the client).<br>Also: <code>__schema</code>, <code>__type</code>, <code>__Field</code>, <code>__EnumValue</code>, <code>__Directive</code> for introspection.",
  ["graphql", "L1", "queries"])

c("Queries",
  "Describe offset-based pagination in GraphQL.",
  "Pass <code>limit</code> and <code>offset</code> arguments:<pre>\nquery {\n  posts(limit: 10, offset: 20) {\n    id\n    title\n  }\n}\n</pre>\n<b>Simple</b> but <b>inconsistent</b> when data mutates between requests (row shifting). Generally discouraged for large/real-time datasets.",
  ["graphql", "L1", "queries"])

c("Queries",
  "Describe cursor-based (Relay-style) pagination.",
  "Uses opaque <b>cursors</b> to navigate forward/backward through a stable sorted list:<pre>\nquery {\n  users(first: 10, after: \"cursor123\") {\n    edges {\n      node { id name }\n      cursor\n    }\n    pageInfo {\n      hasNextPage\n      endCursor\n    }\n  }\n}\n</pre>Stable cursors prevent offset-shifting problems. The Relay Connections spec formalizes this pattern.",
  ["graphql", "L1", "queries"])

c("Queries",
  "What is the Relay Connection spec?",
  "A standard pagination model: <b>Connection</b> (wrapper), <b>Edge</b> (node + cursor), <b>PageInfo</b> (hasNextPage, hasPreviousPage, startCursor, endCursor). Uses <code>first</code>/<code>last</code> + <code>after</code>/<code>before</code> arguments.<pre>\ntype Query {\n  users(first: Int, after: String, last: Int, before: String): UserConnection!\n}\ntype UserConnection { edges: [UserEdge!]! pageInfo: PageInfo! totalCount: Int! }\ntype UserEdge { node: User! cursor: String! }\ntype PageInfo { hasNextPage: Boolean! hasPreviousPage: Boolean! startCursor: String endCursor: String }\n</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What are unions and interfaces in GraphQL queries?",
  "Both represent polymorphic types. Use <b>inline fragments</b> (<code>... on Type</code>) to request fields specific to each type:<pre>\nquery Search {\n  search(text: \"luke\") {\n    __typename\n    ... on Human   { name height }\n    ... on Starship { name length }\n    ... on Droid   { name primaryFunction }\n  }\n}\n</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What is the difference between unions and interfaces in queries?",
  "<b>Interface</b> – types share common fields; you can query shared fields outside the inline fragment:<pre>\nhero { name  # shared field\n  ... on Droid { primaryFunction }\n}</pre>\n<b>Union</b> – types share NO guaranteed common fields; everything must be inside <code>... on Type { }</code>:<pre>\nsearch(text: \"an\") {\n  ... on Human { name }\n  ... on Droid { name }\n}</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What is the <code>@deprecated</code> directive used for in queries?",
  "It marks a schema field or enum value as deprecated. Clients see it in introspection and tooling shows warnings.<pre>\n# In the schema:\ntype User {\n  name: String\n  oldName: String @deprecated(reason: \"Use 'name' instead\")\n}\n\n# Querying the field still works but with warnings.\n</pre>",
  ["graphql", "L1", "queries"])

c("Queries",
  "What tools are used for interactive GraphQL querying?",
  "<b>GraphiQL</b> – the original in-browser GraphQL IDE (by Facebook).<br><b>GraphQL Playground</b> – enhanced IDE with tabs, history, schema polling.<br><b>Apollo Studio Explorer</b> – Apollo's managed explorer.<br><b>Postman / Insomnia</b> – general API clients with GraphQL support.",
  ["graphql", "L1", "queries"])

c("Queries",
  "How do you request related data in a single query (avoiding the 'multiple round-trips' problem)?",
  "Nest the related fields:<pre>\nquery {\n  user(id: 1) {\n    name\n    posts {          # one query, not N+1!\n      title\n      comments {\n        body\n        author { name }\n      }\n    }\n  }\n}\n</pre>This is the <b>graph</b> in GraphQL — traverse relationships in one request.",
  ["graphql", "L1", "queries"])

c("Queries",
  "What does the <code>@defer</code> directive do?",
  "<code>@defer</code> signals the server to send the rest of the response (fields marked with it) <b>incrementally</b> in a later payload. Useful for slow fields.<pre>\nquery {\n  user(id: 1) {\n    name  # delivered immediately\n    slowComputation @defer  # delivered in a later chunk\n  }\n}\n</pre>Part of the incremental delivery spec (experimental).",
  ["graphql", "L1", "queries"])

c("Queries",
  "What does the <code>@stream</code> directive do?",
  "<code>@stream</code> delivers items of a <b>list field</b> incrementally, one item per subsequent payload chunk.<pre>\nquery {\n  feed {\n    posts @stream(initialCount: 5) {\n      title\n    }\n  }\n}\n</pre>Part of the incremental delivery spec (experimental, requires multipart/mixed or SSE transport).",
  ["graphql", "L1", "queries"])

# ─────────────────────────────────────────────────────────
# 03 – Mutations  (~15 cards)
# ─────────────────────────────────────────────────────────

c("Mutations",
  "What is a GraphQL mutation? Write a basic example.",
  "A <b>mutation</b> modifies server-side data (create, update, delete). It must be prefixed with the <code>mutation</code> keyword.<pre>\nmutation CreateUser($name: String!, $email: String!) {\n  createUser(name: $name, email: $email) {\n    id\n    name\n    email\n  }\n}\n\n# Variables: { \"name\": \"Luke\", \"email\": \"luke@rebellion.org\" }\n</pre>",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "How are multiple fields in a mutation executed?",
  "Top-level mutation fields execute <b>sequentially</b> in order (unlike query fields which execute in parallel). This guarantees ordering when one mutation depends on the previous.<pre>\nmutation {\n  first: createPost(title: \"A\") { id }\n  second: createPost(title: \"B\") { id }  # runs after first completes\n}\n</pre>",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "What are GraphQL input types and why use them instead of many arguments?",
  "Input types bundle arguments into a single object. They are <b>required</b> for complex arguments and make the schema evolve gracefully.<pre>\ninput CreateUserInput {\n  name: String!\n  email: String!\n  age: Int\n  role: UserRole = VIEWER\n}\n\nmutation($input: CreateUserInput!) {\n  createUser(input: $input) { id name }\n}\n</pre>",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "What is the mutation payload design pattern?",
  "Every mutation returns a <b>dedicated payload type</b> (not just the mutated object). This allows returning the mutated object, clientMutationId, errors, and any side-effect data.<pre>\ntype CreateUserPayload {\n  user: User\n  clientMutationId: String\n  errors: [UserError!]\n}\n\ntype Mutation {\n  createUser(input: CreateUserInput!): CreateUserPayload!\n}\n</pre>",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "What is <code>clientMutationId</code>?",
  "An opaque string sent by the client with a mutation and returned in the response. It enables the client to <b>correlate</b> an optimistic UI update with the server response, especially when multiple mutations are in-flight. Part of the Relay mutation conventions.",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "How should errors be handled in mutations (top-level vs user errors)?",
  "<b>Top-level errors</b> (<code>\"errors\"</code> key) – for system failures (DB down, auth failure).<br><b>User errors</b> (in the payload) – for validation failures (duplicate email, bad input). This allows partial success and user-friendly error messages.<pre>\ntype UserError {\n  field: [String!]!   # path to the offending field(s)\n  message: String!\n}\n\nmutation {\n  createUser(input: $input) {\n    user { id }\n    errors { field message }   # user-visible errors\n  }\n}\n</pre>",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "What is the optimistic UI pattern with GraphQL mutations?",
  "The client <b>immediately updates</b> the UI assuming success (optimistic), then <b>reconciles</b> when the server response arrives. GraphQL clients like Apollo Client and Relay support this natively via <code>optimisticResponse</code>.<pre>\nconst [addTodo] = useMutation(ADD_TODO, {\n  optimisticResponse: {\n    addTodo: { id: -1, text: newText, __typename: \"Todo\" }\n  },\n  update(cache, { data: { addTodo } }) {\n    cache.modify({ ... });\n  }\n});\n</pre>",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "How do input types differ from arguments?",
  "Arguments are scalar-level (String!, Int!, etc.) whereas <b>input types</b> bundle many arguments into one object. Only input types can contain nested complex structures. The schema evolves more cleanly with input types — adding a field to an input type is backward-compatible.<pre>\n# Arguments (flat):\nmutation createUser(name: String!, email: String!, role: UserRole!): User\n\n# Input type (better):\ninput CreateUserInput { name: String! email: String! role: UserRole! }\nmutation createUser(input: CreateUserInput!): User\n</pre>",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "What is the difference between Object types and Input types?",
  "Object types can contain cyclic references, interfaces, and unions. Input types cannot. Input types have value semantics (no identity, no resolvers).<pre>\n# Valid object type:\ntype User { id: ID! posts: [Post!]! }   # posts references Post\n\n# Input type restrictions:\ninput UserInput { name: String! }        # no cycles, no interfaces\n# input UserInput { posts: [PostInput] } # ERROR if PostInput references UserInput\n</pre>",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "Write a complete mutation with input type, variables, and response selection.",
  "<pre>\n# Schema:\ninput CreateProductInput {\n  name: String!\n  price: Float!\n  category: ProductCategory!\n  tags: [String!]\n}\ntype CreateProductPayload {\n  product: Product\n  errors: [UserError!]!\n}\n\n# Operation:\nmutation CreateNewProduct($input: CreateProductInput!) {\n  createProduct(input: $input) {\n    product { id name price category }\n    errors { field message }\n  }\n}\n\n# Variables:\n{ \"input\": { \"name\": \"Widget\", \"price\": 9.99, \"category\": \"GADGETS\" } }\n</pre>",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "What are the rules for mutation field execution order?",
  "Top-level mutation fields execute <b>serially</b> (one after the other) in the order they appear in the query. Nested sub-fields of a mutation execute in parallel (same as queries). This ensures data-consistency when mutations are interdependent.",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "What is a mutation `field` vs a mutation `operation`?",
  "A <b>mutation operation</b> begins with the <code>mutation</code> keyword. Within it, <b>mutation fields</b> (e.g., <code>createUser</code>, <code>deletePost</code>) are the root mutation fields defined on the <code>type Mutation { ... }</code> type.<pre>\nmutation CreateAndPublish {   # operation\n  c: createPost(title: \"Hi\") { id }  # mutation field\n  p: publishPost(id: 42) { id }      # mutation field\n}\n</pre>",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "How should you design the response of a delete mutation?",
  "Return the <b>ID of the deleted object</b> (so the client can remove it from cache) and optionally a <b>clientMutationId</b>.<pre>\ntype DeleteUserPayload {\n  deletedUserId: ID!\n  clientMutationId: String\n}\n\nmutation {\n  deleteUser(id: \"1\") {\n    deletedUserId\n  }\n}\n</pre>The client can then evict the normalized cache entry for that ID.",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "Can you nest sub-fields inside a mutation selection set?",
  "Yes. Mutations can return rich objects and you can nest selections just like queries:<pre>\nmutation {\n  createUser(input: $input) {\n    user {\n      id\n      posts(first: 5) {     # nested query after creation!\n        edges { node { title } }\n      }\n    }\n  }\n}\n</pre>This is powerful: create and query related data in one round-trip.",
  ["graphql", "L1", "mutations"])

c("Mutations",
  "What is the difference between `null` input fields and omitted input fields?",
  "If a field is omitted from the input object, it's treated as <b>not provided</b>. If set to <code>null</code>, it's explicitly <b>null</b>. This matters for partial updates:<pre>\ninput UpdateUserInput {\n  name: String    # nullable\n  email: String   # nullable\n}\n\n# Patch: { name: \"Luke\" }        – only update name; email unchanged\n# Patch: { name: null }           – explicitly set name to null\n# Patch: { name: \"Luke\", email: null }  – update name, nullify email\n</pre>",
  ["graphql", "L1", "mutations"])

# ─────────────────────────────────────────────────────────
# 04 – Schema Design  (~25 cards)
# ─────────────────────────────────────────────────────────

c("Schema",
  "What is SDL (Schema Definition Language)?",
  "A language-agnostic syntax for describing a GraphQL schema. It uses the same tokens as the query language but for defining types instead of querying them:<pre>\ntype User {\n  id: ID!\n  name: String!\n  posts: [Post!]!\n}\n\ntype Query {\n  user(id: ID!): User\n}\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What are the five main kinds of type definitions in GraphQL?",
  "<pre>\n1. Object types   – type User { id: ID! name: String! }\n2. Scalar types   – scalar DateTime  (custom) or built-in (Int, Float)\n3. Enum types     – enum Role { ADMIN USER VIEWER }\n4. Input types    – input CreateUserInput { name: String! }\n5. Interface types – interface Node { id: ID! }\n6. Union types    – union SearchResult = User | Post | Page\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What are the five built-in scalar types?",
  "<pre>\nInt     – signed 32-bit integer\nFloat   – signed double-precision floating-point\nString  – UTF-8 character sequence\nBoolean – true or false\nID      – unique identifier (serialized as String, not intended to be human-readable)\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What is a custom scalar and how do you define one?",
  "A custom scalar represents a value not covered by the five built-in scalars. You define it in SDL and provide serialization/parsing logic in your resolver map.<pre>\nscalar DateTime\nscalar JSON\nscalar EmailAddress\nscalar URL\n\ntype Event {\n  id: ID!\n  startsAt: DateTime!   # custom scalar\n}\n\n# In resolvers you must provide:\n# serialize(value) – for output\n# parseValue(value) – for input (variables)\n# parseLiteral(ast) – for inline literal values\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What are the three root operation types?",
  "<pre>\nschema {\n  query: Query          # required — all read operations\n  mutation: Mutation    # optional — all write operations\n  subscription: Subscription  # optional — real-time push events\n}\n\n# If omitted, defaults to:\n# schema { query: Query mutation: Mutation subscription: Subscription }\n</pre>Every GraphQL service has at least a <code>Query</code> type.",
  ["graphql", "L2", "schema"])

c("Schema",
  "How does the <code>schema { ... }</code> block work and when is it needed?",
  "It explicitly names the root types. Required when root types are not named <code>Query</code>, <code>Mutation</code>, <code>Subscription</code>, or when you have multiple schema definitions.<pre>\nschema {\n  query: MyCustomQueryType\n  mutation: MyCustomMutationType\n}\n\ntype MyCustomQueryType {\n  version: String!\n  users: [User!]!\n}\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What is the Non-Null modifier (<code>!</code>)?",
  "Appended to a type, it guarantees the resolved value is never <code>null</code>. If a resolver returns <code>null</code>, the <b>null propagates</b> up to the nearest nullable parent.<pre>\ntype User {\n  id: ID!        # always non-null\n  name: String!  # always non-null\n  bio: String    # can be null\n}\n\n# Null propagation:\nuser(id: 1) { posts { title } }   # if posts is [Post!]! and is null\n  → user field becomes null, even if other fields had data\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What is the List modifier (<code>[Type]</code>)?",
  "Wraps a type, indicating it returns a list. Combine with <code>!</code> for precise nullability:<pre>\n[User]     – list can be null; items can be null\n[User!]    – list can be null; items CANNOT be null\n[User]!    – list CANNOT be null; items can be null\n[User!]!   – list CANNOT be null; items CANNOT be null\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What are GraphQL enum types? Define one.",
  "Enums restrict a field to a fixed set of values:<pre>\nenum Episode {\n  NEWHOPE\n  EMPIRE\n  JEDI\n}\n\ntype Query {\n  hero(episode: Episode!): Character\n}\n\n# Query:\n{ hero(episode: EMPIRE) { name } }\n</pre>Enum values are NOT quoted in queries.",
  ["graphql", "L2", "schema"])

c("Schema",
  "What are interface types? Write an example.",
  "An interface defines a set of fields that multiple types must implement. Useful for polymorphic queries.<pre>\ninterface Character {\n  id: ID!\n  name: String!\n  friends: [Character!]\n  appearsIn: [Episode!]!\n}\n\ntype Human implements Character {\n  id: ID!\n  name: String!\n  friends: [Character!]\n  appearsIn: [Episode!]!\n  homePlanet: String    # Human-specific field\n}\n\ntype Droid implements Character {\n  id: ID!\n  name: String!\n  friends: [Character!]\n  appearsIn: [Episode!]!\n  primaryFunction: String  # Droid-specific field\n}\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What are union types? Write an example.",
  "A union declares that a field can return one of several object types, with <b>no guaranteed common fields</b>.<pre>\nunion SearchResult = Human | Droid | Starship\n\ntype Query {\n  search(text: String!): [SearchResult!]!\n}\n\n# Query:\nquery {\n  search(text: \"an\") {\n    __typename\n    ... on Human { name height }\n    ... on Droid { name primaryFunction }\n    ... on Starship { name length }\n  }\n}\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "How do interfaces differ from unions in the schema?",
  "<b>Interfaces:</b> Types <code>implement</code> them, share common fields, can be queried for shared fields without inline fragment.<br><b>Unions:</b> Types are just listed, no shared fields guaranteed, <i>must</i> use inline fragments for every field. Also, interfaces can implement other interfaces; unions cannot.<pre>\ninterface Node { id: ID! }\ninterface Timestamped { createdAt: DateTime! updatedAt: DateTime! }\ntype User implements Node & Timestamped { ... }\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What is the <code>@deprecated</code> directive syntax in SDL?",
  "<pre>\ntype User {\n  oldField: String @deprecated(reason: \"Use 'newField' instead\")\n  newField: String\n}\n\nenum Role {\n  OLD_ROLE @deprecated\n  NEW_ROLE\n}\n</pre>The <code>reason</code> argument is optional. Deprecated fields still resolve normally but show warnings in tooling.",
  ["graphql", "L2", "schema"])

c("Schema",
  "How do you add documentation/descriptions to GraphQL types and fields?",
  "Use triple-quoted strings before the type or field definition:<pre>\n\"\"\"\nA character in the Star Wars universe.\nCan be either a Human or a Droid.\n\"\"\"\ninterface Character {\n  \"The unique identifier of the character\"\n  id: ID!\n\n  \"The name of the character\"\n  name: String!\n}\n</pre>These descriptions are available via introspection (<code>__schema</code>, <code>__type</code>).",
  ["graphql", "L2", "schema"])

c("Schema",
  "What is the <code>extend</code> keyword used for?",
  "To add fields to an existing type from another location/module. Useful for modular schemas and Federation subgraphs.<pre>\n# base.graphql\ntype User { id: ID! name: String! }\n\n# extended.graphql\nextend type User {\n  posts: [Post!]!\n  followers: [User!]!\n}\n\n# Also works for:\nextend type Query { ... }\nextend type Mutation { ... }\nextend enum Role { ... }\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What is a field argument vs an input type? When use which?",
  "<b>Field argument:</b> simple scalar values passed directly to a field (<code>user(id: \"1\")</code>). Good for scalars only.<br><b>Input type:</b> complex structured data passed to a mutation or deeply nested field. Mandatory when you need nested arguments.<pre>\n# Field arguments (scalars only):\nquery { user(id: \"1\", source: WEB) { name } }\n\n# Input type (complex data):\nmutation { createUser(input: { name: \"A\", profile: { bio: \"...\" } }) { id } }\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What happens during schema validation?",
  "The server checks the query against the schema:<br>— Every field name exists on its parent type<br>— Every argument name and type is valid<br>— Every fragment spread resolves to a known fragment<br>— Every type condition on <code>... on Type</code> is a valid subtype<br>— No invalid inline fragments (e.g., <code>... on String</code>)<br>If any check fails, the query is rejected with a validation error before execution.",
  ["graphql", "L2", "schema"])

c("Schema",
  "What are the limitations of input types?",
  "<b>Cannot:</b><br>— Use interfaces inside input types<br>— Use unions inside input types<br>— Have cyclic references between input types<br>— Have resolvers (they are plain data)<br><b>Can:</b><br>— Have default values (<code>input { limit: Int = 10 }</code>)<br>— Reference other input types<br>— Use all scalars, enums, and list/non-null modifiers",
  ["graphql", "L2", "schema"])

c("Schema",
  "How would you design a GraphQL schema for a blog?",
  "<pre>\n# Core types\ntype Post {\n  id: ID!\n  title: String!\n  content: String!\n  author: User!\n  comments: [Comment!]!\n}\n\ntype User {\n  id: ID!\n  name: String!\n  posts: [Post!]!\n}\n\ntype Comment {\n  id: ID!\n  body: String!\n  author: User!\n  post: Post!\n}\n\n# Inputs\ninput CreatePostInput { title: String! content: String! }\n\n# Root types\ntype Query {\n  posts: [Post!]!\n  post(id: ID!): Post\n}\n\ntype Mutation {\n  createPost(input: CreatePostInput!): CreatePostPayload\n}\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What is the difference between <code>[User!]</code> and <code>[User]!</code>?",
  "<code>[User!]</code> – the list itself can be null, but any item cannot be null. If non-null, you get <code>[{...}, {...}]</code> or <code>null</code>.<br><code>[User]!</code> – the list is never null (always an array), but individual items can be null: <code>[{...}, null, {...}]</code>.<br><code>[User!]!</code> – list never null, items never null: <code>[{...}, {...}]</code> always.<br>This is known as <b>list nullability</b>.",
  ["graphql", "L2", "schema"])

c("Schema",
  "Write a complete schema with an interface and a union used in Query.",
  "<pre>\ninterface Animal {\n  id: ID!\n  species: String!\n}\n\ntype Dog implements Animal {\n  id: ID!\n  species: String!\n  breed: String!\n}\n\ntype Cat implements Animal {\n  id: ID!\n  species: String!\n  livesLeft: Int!\n}\n\nunion SearchResult = Dog | Cat | User\n\ntype Query {\n  allAnimals: [Animal!]!\n  search(term: String!): [SearchResult!]!\n}\n\nschema { query: Query }\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "How does default value assignment work for input fields?",
  "If a field in an input type has a default value and the client omits it, the default is used. If the client passes <code>null</code> (and the field is nullable), the default is <b>ignored</b> and the field becomes null.<pre>\ninput PaginationInput {\n  first: Int = 10\n  after: String\n}\n\n# Omitting 'first' → first = 10\n# Passing first: null → first = null (explicit null overrides default)\n</pre>",
  ["graphql", "L2", "schema"])

c("Schema",
  "What is a schema directive and how do you define a custom one?",
  "Directives are annotations that modify schema or execution behavior. Define them with <code>directive @name on LOCATION</code>:<pre>\ndirective @auth(requires: Role = ADMIN) on OBJECT | FIELD_DEFINITION\ndirective @uppercase on FIELD_DEFINITION\ndirective @cacheControl(maxAge: Int!) on FIELD_DEFINITION\n\ntype Query {\n  secretData: String @auth(requires: ADMIN)\n  name: String @uppercase\n  posts: [Post!]! @cacheControl(maxAge: 60)\n}\n</pre>You implement the directive logic in your server code (transforms, middleware, etc.).",
  ["graphql", "L2", "schema"])

# ─────────────────────────────────────────────────────────
# 05 – Resolvers  (~18 cards)
# ─────────────────────────────────────────────────────────

c("Schema",
  "What is the resolver function signature?",
  "<pre>\nfieldName(parent, args, context, info) => value\n\nparent   – previous resolver's return value\nargs     – arguments passed in the query (object)\ncontext  – shared object across all resolvers (auth, loaders, DB)\ninfo     – execution details (AST, schema, field name, path)\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "What is a root resolver vs a field-level resolver?",
  "<b>Root resolver:</b> resolves a top-level field on <code>Query</code>, <code>Mutation</code>, or <code>Subscription</code>. Often fetches the 'entry point' data.<br><b>Field-level resolver:</b> resolves a field on a non-root type. May be omitted if the parent object already has the field by that name (default resolver).<pre>\nconst resolvers = {\n  Query: {           # root resolvers\n    user: (_, { id }, ctx) => ctx.db.findUser(id),\n  },\n  User: {            # field-level resolvers\n    fullName: (user) => `${user.firstName} ${user.lastName}`,\n    posts: (user, args, ctx) => ctx.loaders.posts.load(user.id),\n  }\n};\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "What is a resolver chain?",
  "When a field's resolver returns an object, the engine calls the <b>next level</b> of resolvers with that object as <code>parent</code>. This forms a chain from root to leaf.<pre>\nQuery.user → returns { id: 1, name: \"Luke\" }\n  User.posts({ id: 1 }, args, ctx) → returns [Post1, Post2]\n    Post.title(Post1, args, ctx) → returns \"Hello World\"\n    Post.comments(Post1, args, ctx) → returns [Comment1]\n      Comment.body(Comment1, args, ctx) → returns \"Nice!\"\n</pre>Each step can fetch data independently (but watch out for N+1!).",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "What is the DataLoader pattern and what problem does it solve?",
  "DataLoader <b>batching and caching</b> coalesces individual DB calls into a single batch call, eliminating the N+1 query problem.<pre>\nconst userLoader = new DataLoader(async (ids) => {\n  const users = await db.users.findByIds(ids);\n  return ids.map(id => users.find(u => u.id === id));\n});\n\n// Resolver:\nUser.posts = (user, args, ctx) => ctx.postLoader.load(user.id);\n\n// Instead of N SQL queries, DataLoader collects all user.id\n// values from the query execution tick and sends ONE query:\n// SELECT * FROM posts WHERE author_id IN (1, 2, 3, ...)\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "What is the <code>context</code> argument typically used for?",
  "It carries <b>per-request shared state</b>: authenticated user, database connection, DataLoader instances, dataloader cache, API clients. Created per-request in the server setup:<pre>\nconst server = new ApolloServer({\n  typeDefs, resolvers,\n  context: ({ req }) => ({\n    currentUser: getUserFromToken(req.headers.authorization),\n    loaders: createLoaders(),\n    db: connectToDb(),\n  }),\n});\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "How does field-level authorization work in resolvers?",
  "Check the authenticated user in the resolver before returning data:<pre>\nconst resolvers = {\n  Query: {\n    secretDocuments: (parent, args, ctx) => {\n      if (!ctx.currentUser) throw new AuthenticationError('Login required');\n      if (!ctx.currentUser.roles.includes('ADMIN')) {\n        throw new ForbiddenError('Admins only');\n      }\n      return ctx.db.secretDocuments.findAll();\n    },\n  },\n  User: {\n    email: (user, args, ctx) => {\n      if (ctx.currentUser?.id !== user.id) return null;  // hide email\n      return user.email;\n    },\n  },\n};\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "How do you resolve interface and union types?",
  "Provide a <code>__resolveType</code> function that determines the concrete type from the returned object:<pre>\nconst resolvers = {\n  Character: {\n    __resolveType(obj) {\n      if (obj.primaryFunction) return 'Droid';\n      if (obj.homePlanet) return 'Human';\n      return null;  // should never happen\n    },\n  },\n  SearchResult: {\n    __resolveType(obj) {\n      if (obj.breed) return 'Dog';\n      if (obj.livesLeft) return 'Cat';\n      if (obj.email) return 'User';\n      return null;\n    },\n  },\n};\n</pre>Without this, GraphQL cannot know which type of object it received.",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "What is the default resolver and when is it used?",
  "If you don't provide a resolver for a field, GraphQL uses a <b>default resolver</b> that looks for a property of the same name on the parent object.<pre>\n# Schema:\ntype User { id: ID! name: String! }\n\n# Parent object from DB:\n# { id: 1, name: \"Luke\", email: \"luke@reb.org\" }\n\n# No resolver needed for 'id' or 'name' — default resolver reads\n# parent[\"id\"] and parent[\"name\"] automatically.\n# 'email' is not in the schema, so it's never exposed.\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "How do you implement a custom scalar (e.g., DateTime)?",
  "Provide <code>serialize</code>, <code>parseValue</code>, and <code>parseLiteral</code> methods:<pre>\nimport { GraphQLScalarType, Kind } from 'graphql';\n\nconst DateTime = new GraphQLScalarType({\n  name: 'DateTime',\n  description: 'ISO-8601 date string',\n  serialize(value) {\n    return value instanceof Date ? value.toISOString() : null;\n  },\n  parseValue(value) {\n    return new Date(value);  // from JSON variables\n  },\n  parseLiteral(ast) {\n    if (ast.kind === Kind.STRING) return new Date(ast.value);\n    return null;  // invalid literal\n  },\n});\n\nconst resolvers = { DateTime };\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "What is the N+1 problem in GraphQL?",
  "When each item in a list triggers an additional database query inside a field resolver. For a list of N items with a resolved sub-field, you get 1 + N queries.<pre>\n# Query: { users { name posts { title } } }\n# 1 query to get all users\n# + N queries for each user's posts (one per user)\n# Total: 1 + N queries — inefficient!\n\n# Fix: DataLoader batches the N post queries into 1:\n# 1 query for users + 1 query for posts WHERE author_id IN (...)\n# Total: 2 queries — optimal!\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "What is the <code>info</code> argument used for in resolvers?",
  "<code>info</code> contains the full GraphQLResolveInfo: AST of the current field, sub-fields requested, schema, return type, path, variable values. Useful for advanced patterns:<pre>\nconst resolvers = {\n  user: (parent, args, ctx, info) => {\n    const requestedFields = info.fieldNodes[0].selectionSet\n      .selections.map(s => s.name.value);\n    console.log('Client asked for:', requestedFields);\n    // Optimize DB query based on which fields were requested\n  },\n};\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "How do error handling patterns work in resolvers?",
  "Throw (or return) errors. Use standard GraphQL error classes or custom errors:<pre>\nimport { GraphQLError } from 'graphql';\n\nconst resolvers = {\n  Query: {\n    user: async (_, { id }, ctx) => {\n      const user = await ctx.db.user.findById(id);\n      if (!user) {\n        throw new GraphQLError('User not found', {\n          extensions: { code: 'NOT_FOUND', userId: id },\n        });\n      }\n      return user;\n    },\n  },\n};\n\n// Response: { \"errors\": [{ \"message\": \"User not found\",\n//   \"extensions\": { \"code\": \"NOT_FOUND\", \"userId\": \"1\" } }] }\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "What is the <code>GraphQLError</code> extensions field used for?",
  "The <code>extensions</code> map carries structured machine-readable error metadata. Useful for: error codes, validation details, stack traces (dev only), retry hints, field paths.<pre>\nthrow new GraphQLError('Validation failed', {\n  extensions: {\n    code: 'VALIDATION_ERROR',\n    fields: { email: 'Invalid format', age: 'Must be positive' },\n    retryable: false,\n  },\n});\n\n// Apollo errors are subclasses with built-in extensions:\nnew AuthenticationError('...')  // code: 'UNAUTHENTICATED'\nnew ForbiddenError('...')       // code: 'FORBIDDEN'\nnew UserInputError('...', { fields: {...} })  // code: 'BAD_USER_INPUT'\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "What are Apollo Server error codes?",
  "<pre>\nBAD_USER_INPUT    – invalid user input (UserInputError)\nUNAUTHENTICATED   – not logged in (AuthenticationError)\nFORBIDDEN         – logged in but no permission (ForbiddenError)\nNOT_FOUND         – resource doesn't exist (custom)\nINTERNAL_SERVER_ERROR – unhandled exception\nGRAPHQL_PARSE_FAILED  – invalid query syntax\nGRAPHQL_VALIDATION_FAILED – query doesn't match schema\n</pre>Use <code>ApolloServerErrorCode</code> enum for standard codes.",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "What does the DataLoader constructor look like and what are its options?",
  "<pre>\nnew DataLoader(batchLoadFn, options?)\n\nbatchLoadFn: async (keys: K[]) => Promise<(V | Error)[]>\n  - Receives an array of keys, must return array of same length\n\nOptions:\n  maxBatchSize – max keys in one batch (default: Infinity)\n  batchScheduleFn – custom scheduling (default: process.nextTick)\n  cache – whether to cache results (default: true)\n  cacheKeyFn – how to generate cache keys (default: identity)\n  cacheMap – custom cache implementation\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "How do you prime a DataLoader cache manually?",
  "Use <code>.prime(key, value)</code> to pre-populate the cache. Useful when you already fetched data elsewhere:<pre>\n// In a mutation, after creating a user:\nconst newUser = await db.user.create(input);\nctx.loaders.user.prime(newUser.id, newUser);\n// Now any subsequent user.load(newUser.id) returns cached value without DB call\n</pre>",
  ["graphql", "L3", "resolvers"])

c("Schema",
  "How does the DataLoader batch scheduler work?",
  "DataLoader collects all <code>.load()</code> calls within a single <b>tick</b> of the event loop (by default <code>process.nextTick</code>). It then batches them into one <code>batchLoadFn</code> call. This means all resolvers that run synchronously (or within the same promise microtask) get batched:<pre>\n// These 3 calls happen in the same tick, so DataLoader calls\n// batchLoadFn([1, 2, 3]) once.\nuserLoader.load(1);\nuserLoader.load(2);\nuserLoader.load(3);\n\n// After next tick batch runs, the cache is populated.\nuserLoader.load(1); // returns from cache (no additional call)\n</pre>",
  ["graphql", "L3", "resolvers"])

# ─────────────────────────────────────────────────────────
# 06 – Subscriptions  (~14 cards)
# ─────────────────────────────────────────────────────────

c("Subscriptions",
  "What is a GraphQL subscription?",
  "A subscription is a <b>long-lived connection</b> that pushes data from the server to the client when specific events occur. It maintains a stateful stream, typically over WebSocket.<pre>\nsubscription {\n  messageAdded(channelId: \"general\") {\n    id\n    text\n    author { name }\n  }\n}\n\n# Server pushes whenever a new message is added to that channel.\n</pre>",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "What is the pub/sub model in GraphQL subscriptions?",
  "The server uses a <b>Publish-Subscribe</b> pattern: resolvers <b>subscribe</b> to events via an event emitter, and mutations <b>publish</b> events.<pre>\n// Using graphql-subscriptions PubSub:\nconst pubsub = new PubSub();\n\n// Subscription resolver:\nsubscribe: () => pubsub.asyncIterator(['MESSAGE_ADDED'])\n\n// Inside a mutation resolver:\npubsub.publish('MESSAGE_ADDED', { messageAdded: newMessage });\n</pre>",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "What transport does GraphQL use for subscriptions?",
  "Primarily <b>WebSocket</b>. The modern protocol is <b>graphql-ws</b> (new, maintained by the-guild-org). The legacy protocol is <b>subscriptions-transport-ws</b> (deprecated, by Apollo). Both start with WebSocket but use different message formats.",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "What is the difference between <code>graphql-ws</code> and <code>subscriptions-transport-ws</code>?",
  "<table>\n<tr><th></th><th>graphql-ws</th><th>subscriptions-transport-ws</th></tr>\n<tr><td>Status</td><td>Active, maintained</td><td>Deprecated</td></tr>\n<tr><td>Init msg</td><td><code>ConnectionInit</code></td><td><code>GQL_CONNECTION_INIT</code></td></tr>\n<tr><td>Auth</td><td>ConnectionInit payload</td><td>connectionParams</td></tr>\n<tr><td>Ping/Pong</td><td>Ping/Pong</td><td>GQL_CONNECTION_KEEP_ALIVE</td></tr>\n<tr><td>Complete</td><td>Complete</td><td>GQL_STOP</td></tr>\n</table><br>New projects should use <code>graphql-ws</code>.",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "How does authentication work with GraphQL subscriptions?",
  "Auth token is sent in the <b>connection_init</b> payload (WebSocket has no headers after the initial upgrade). The server validates it and sets up context:<pre>\n// Client (graphql-ws):\nconst client = createClient({\n  url: 'ws://localhost:4000/graphql',\n  connectionParams: { authToken: 'Bearer xxx' },\n});\n\n// Server (graphql-ws):\nuseServer({ schema, context: (ctx) => {\n  const token = ctx.connectionParams?.authToken;\n  return { currentUser: getUserFromToken(token) };\n}}, wsServer);\n</pre>",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "How do subscription filters work?",
  "Use arguments in the subscription and filter inside <code>withFilter</code>:<pre>\nconst resolvers = {\n  Subscription: {\n    messageAdded: {\n      subscribe: withFilter(\n        () => pubsub.asyncIterator(['MESSAGE_ADDED']),\n        (payload, variables) => {\n          return payload.messageAdded.channelId === variables.channelId;\n        },\n      ),\n    },\n  },\n};\n</pre>Only clients whose filter matches the published event receive the payload.",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "What is a `live query` and how does it differ from subscriptions?",
  "A <b>live query</b> is like a regular query that the server keeps alive and pushes <b>the full updated result</b> whenever underlying data changes. Subscriptions push <b>individual events</b>. Live queries are not yet part of the spec (experimental/proposals exist).<br>Some implementations: GraphQL Live Query (n1ru4l), Apollo's proposed <code>@live</code> directive.",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "How do you scale subscriptions across multiple server instances?",
  "Use an <b>external PubSub</b> backed by <b>Redis</b> (or Kafka, RabbitMQ, PostgreSQL NOTIFY). The built-in <code>PubSub</code> only works in-process (single server).<pre>\nimport { RedisPubSub } from 'graphql-redis-subscriptions';\n\nconst pubsub = new RedisPubSub({\n  connection: { host: 'localhost', port: 6379 },\n});\n\n// Now any server in the cluster can publish, and all servers\n// receive the event and forward to their connected WebSocket clients.\n</pre>",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "What is the subscription initialization lifecycle?",
  "<pre>\n1. Client ↔ Server: WebSocket handshake (HTTP Upgrade)\n2. Client → Server: GQL_CONNECTION_INIT (or ConnectionInit) with auth\n3. Server → Client: GQL_CONNECTION_ACK (or ConnectionAck)\n4. Client → Server: GQL_START (or Subscribe) with subscription query\n5. Server → Client: GQL_DATA (or Next) — event payloads\n   ... (multiple data events over time) ...\n6. Client → Server: GQL_STOP (or Complete)\n7. Server → Client: GQL_COMPLETE (or Complete acknowledgment)\n</pre>",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "How do you handle client disconnections in subscriptions?",
  "On unsubscribe, clean up any resources in the resolver's <code>subscribe</code> return value:<pre>\nconst resolvers = {\n  Subscription: {\n    messages: {\n      subscribe: (parent, args, ctx) => {\n        const iterator = pubsub.asyncIterator('MESSAGE');\n        return {\n          [Symbol.asyncIterator]() { return iterator; },\n          async return() {\n            // Called when client disconnects or unsubscribes\n            await iterator.return();\n            console.log('Client unsubscribed, cleaned up');\n          },\n        };\n      },\n    },\n  },\n};\n</pre>",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "How are subscription errors communicated to the client?",
  "Via <code>GQL_ERROR</code> (or <code>Error</code>) message type. Unlike queries/mutations, subscription errors are sent over the WebSocket stream, not in the HTTP response body.<pre>\n// Server sends when resolver throws:\n{ \"id\": \"1\", \"type\": \"error\", \"payload\": [{ \"message\": \"...\" }] }\n\n// Client handles:\nclient.subscribe({ query }, {\n  next: (data) => { ... },\n  error: (errors) => { console.error(errors); },\n  complete: () => { ... },\n});\n</pre>",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "Write a complete subscription schema with a pre-aggregated counter example.",
  "<pre>\ntype Subscription {\n  voteCount(pollId: ID!): Int!\n}\n\n# In mutation:\ntype Mutation {\n  vote(pollId: ID!, optionId: ID!): VotePayload\n}\n\n# Resolver:\nconst resolvers = {\n  Subscription: {\n    voteCount: {\n      subscribe: (_, { pollId }) => {\n        return pubsub.asyncIterator(`POLL_${pollId}`);\n      },\n      resolve: (payload) => payload.voteCount,\n    },\n  },\n  Mutation: {\n    vote: async (_, { pollId, optionId }, ctx) => {\n      const count = await ctx.db.votes.count({ where: { pollId } });\n      pubsub.publish(`POLL_${pollId}`, { voteCount: count });\n      return { success: true };\n    },\n  },\n};\n</pre>",
  ["graphql", "L2", "subscriptions"])

c("Subscriptions",
  "What is <code>withFilter</code> and when should you use it?",
  "A higher-order function from <code>graphql-subscriptions</code> that wraps a subscription resolver. It filters events based on the subscription's arguments, ensuring only matching clients receive the payload.<pre>\nimport { withFilter } from 'graphql-subscriptions';\n\nsubscribe: withFilter(\n  () => pubsub.asyncIterator('EVENT'),\n  (payload, variables, context) => {\n    return payload.event.groupId === variables.groupId;\n  }\n)\n</pre>Without <code>withFilter</code>, all subscribers to the same event channel receive the event regardless of arguments.",
  ["graphql", "L2", "subscriptions"])

# ─────────────────────────────────────────────────────────
# 07 – Performance  (~16 cards)
# ─────────────────────────────────────────────────────────

c("Performance",
  "What is the N+1 problem and how does it manifest in GraphQL?",
  "When resolving a list of N items, each item triggers a separate query for a sub-field. E.g., 10 users × 1 query each for their posts = 11 queries total. Solved by <b>DataLoader</b>, which coalesces individual lookups into a single batched query.",
  ["graphql", "L3", "performance"])

c("Performance",
  "How do you set up DataLoader for a one-to-many relationship (e.g., users → posts)?",
  "<pre>\nconst postsByUserLoader = new DataLoader(async (userIds) => {\n  const posts = await db.posts.find({ authorId: { $in: userIds } });\n  return userIds.map(id => posts.filter(p => p.authorId === id));\n});\n\n// Resolver:\nconst resolvers = {\n  User: {\n    posts: (user, args, ctx) => ctx.loaders.posts.load(user.id),\n  },\n};\n\n// Result: For N users, ONE DB query instead of N\n</pre>",
  ["graphql", "L3", "performance"])

c("Performance",
  "What is query complexity analysis?",
  "A technique to <b>limit expensive queries</b>. Each field is assigned a complexity cost, and the total query complexity is computed pre-execution. Queries exceeding a threshold are rejected.<pre>\n// With graphql-query-complexity:\nconst rule = createComplexityRule({\n  maximumComplexity: 1000,\n  defaultComplexity: 1,\n  variables: {},\n  onComplete: (complexity) => console.log('Complexity:', complexity),\n});\n\nconst server = new ApolloServer({\n  validationRules: [rule],\n});\n</pre>",
  ["graphql", "L3", "performance"])

c("Performance",
  "What is query depth limiting and why use it?",
  "Prevents deeply nested queries (e.g., recursive <code>friend { friend { friend { ... } } }</code>) that could cause performance issues or DoS. Typically set to 5-7 levels.<pre>\nimport depthLimit from 'graphql-depth-limit';\n\nconst server = new ApolloServer({\n  validationRules: [depthLimit(5)],  // Max 5 levels deep\n});\n</pre>",
  ["graphql", "L3", "performance"])

c("Performance",
  "What are Automatic Persisted Queries (APQ)?",
  "The client sends a <b>hash (SHA-256)</b> of the query instead of the full query string. The server stores executed queries by hash, reducing bandwidth and enabling server-side caching. If the hash is unknown, the client resends the full query.<pre>\n// Client sends:\n{ \"extensions\": { \"persistedQuery\": { \"version\": 1,\n    \"sha256Hash\": \"abc123...\" } } }\n\n// Server either executes from cache or responds with\n// \"PersistedQueryNotFound\", client then sends full query.\n\n// Apollo Server: install apollo-server-plugin-response-cache\n</pre>",
  ["graphql", "L3", "performance"])

c("Performance",
  "What is query batching and how does it help?",
  "Multiple queries are sent in a single HTTP request as a JSON array. The server executes them independently and returns an array of responses. Reduces network round-trips.<pre>\n// Request:\n[\n  { \"query\": \"{ user(id: 1) { name } }\" },\n  { \"query\": \"{ user(id: 2) { name } }\" },\n]\n\n// Response:\n[\n  { \"data\": { \"user\": { \"name\": \"Luke\" } } },\n  { \"data\": { \"user\": { \"name\": \"Leia\" } } },\n]\n</pre>Supported by Apollo Link, urql, and most servers out of the box.",
  ["graphql", "L3", "performance"])

c("Performance",
  "What caching strategies exist for GraphQL?",
  "<b>1. Client-side cache</b> (Apollo InMemoryCache, Relay Store, urql) – normalized entity caching, automatic cache updates after mutations.<br><b>2. Field-level caching</b> – <code>@cacheControl</code> directive on fields with maxAge.<br><b>3. Query-level response caching</b> – cache the entire JSON response for a query (works with APQ).<br><b>4. CDN/Edge caching</b> – use GET requests for cacheable queries, cache at the edge.<br><b>5. Redis-backed server cache</b> – cache resolver return values in Redis.",
  ["graphql", "L3", "performance"])

c("Performance",
  "How does Apollo Client's InMemoryCache work?",
  "It normalizes query results into a flat entity store (like a database), keyed by <code>__typename:id</code>. Queries are read from the cache when possible, avoiding network requests. After mutations, the cache is updated (manually or automatically).<pre>\n// Normalized cache:\n{ \"User:1\": { id: \"1\", name: \"Luke\", __typename: \"User\" },\n  \"User:2\": { id: \"2\", name: \"Leia\", __typename: \"User\" } }\n\n// cache.identify({ id: \"1\", __typename: \"User\" }) → \"User:1\"\n</pre>",
  ["graphql", "L3", "performance"])

c("Performance",
  "What is the <code>@cacheControl</code> directive and how do you use it?",
  "Sets cache expiration for fields, inherited by parent types:<pre>\nimport { ApolloServerPluginCacheControl } from '@apollo/server/plugin/cacheControl';\n\ntype User @cacheControl(maxAge: 60) {\n  id: ID!\n  name: String!\n  posts: [Post!]! @cacheControl(maxAge: 10)  # shorter TTL\n}\n\n# 'id' and 'name' inherit maxAge: 60 from User\n# 'posts' overrides to maxAge: 10\n\n# Server setup:\nnew ApolloServer({\n  plugins: [ApolloServerPluginCacheControl({ defaultMaxAge: 5 })],\n});\n</pre>",
  ["graphql", "L3", "performance"])

c("Performance",
  "How can you use GET requests for GraphQL queries to enable CDN caching?",
  "Send the query, variables, and operationName as URL query parameters. The server must support GET. The CDN caches the response by URL.<pre>\nGET /graphql?query={user(id:\"1\"){name}}&variables={}\n\n# Or with persisted queries (APQ) — even more cache-friendly:\nGET /graphql?extensions={\"persistedQuery\":{\"sha256Hash\":\"abc...\"}}\n\n# Apollo Client: use HttpLink with useGETForQueries: true\n</pre>",
  ["graphql", "L3", "performance"])

c("Performance",
  "What is the <code>@defer</code> directive's role in performance?",
  "It improves <b>perceived performance</b> by splitting the response: fast fields return immediately, slow fields are delivered later in incremental payloads. The client can render partial UI while waiting for the rest. Requires multipart/mixed or SSE transport.",
  ["graphql", "L3", "performance"])

c("Performance",
  "How do you use DataLoader for mutations too?",
  "DataLoader's batching is useful for <b>bulk operations</b> inside mutations. Instead of inserting N items one-by-one, batch them:<pre>\nconst userCreator = new DataLoader(async (inputs) => {\n  // batch insert:\n  const users = await db.users.insertMany(inputs);\n  return inputs.map((_, i) => users[i]);\n});\n\n// In a mutation that creates users in a loop:\nfor (const input of userInputs) {\n  userCreator.load(input);  // collected and batched\n}\n</pre>Note: DataLoader is primarily designed for reads; mutation batching requires careful handling of ordering and side effects.",
  ["graphql", "L3", "performance"])

c("Performance",
  "Why are APQs a security improvement as well as a performance one?",
  "With APQ, the server can maintain an <b>allow-list</b> (whitelist) of known query hashes. Unknown queries (adversarial attempts at complex/prohibited operations) can be rejected outright. This eliminates the need for complexity analysis on unknown queries — only known queries execute.",
  ["graphql", "L3", "performance"])

c("Performance",
  "What is a DataLoader batch function's return requirement?",
  "The batch function <b>must return an array of the same length</b> as the keys array, in the same order. If a key has no result, return <code>null</code> in that position (not skip it).<pre>\nconst loader = new DataLoader(async (ids) => {\n  const users = await db.users.findByIds(ids);\n  // MUST return same length and order:\n  return ids.map(id => users.find(u => u.id === id) ?? null);\n});\n\n// ids = [1, 2, 3] → must return [User1, User2, null]\n// NOT [User1, User2] (length mismatch → error)\n</pre>",
  ["graphql", "L3", "performance"])

c("Performance",
  "How do field-level cost analysis and complexity analysis differ?",
  "<b>Query depth:</b> counts nesting levels (simple, coarse).<br><b>Query complexity:</b> assigns each field a weight/cost, sums all field costs (finer-grained).<br><b>Field-level cost analysis:</b> worst-case estimated cost based on list cardinalities, accounts for pagination arguments (most accurate).<pre>\n# Complexity = 1 for 'user' + 1 per 'posts' + 10*1 for 'comments'\n# (assuming first: 10 on posts)\n{ user { posts(first: 10) { comments { body } } } }\n# Complexity: 1 + 10 + 100 = 111 (if each post has ~10 comments)\n</pre>",
  ["graphql", "L3", "performance"])

# ─────────────────────────────────────────────────────────
# 08 – Gotchas  (~18 cards)
# ─────────────────────────────────────────────────────────

c("Gotchas",
  "What is null propagation in GraphQL?",
  "If any field in a non-null chain resolves to <code>null</code>, the null <b>propagates up</b> to the nearest nullable parent field. This means a single null can wipe out the entire parent result.<pre>\n# Schema: posts: [Post!]! (non-null list of non-null posts)\n# If the 'posts' field returns null (due to DB error):\n# → user field becomes null, even though 'name' succeeded!\n\n# Response: { \"data\": { \"user\": null } }  # name is lost!\n\n# Mitigation: use nullable types for lists that might fail:\n# posts: [Post!]  (nullable list) — error stays scoped\n</pre>",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "How should you design nullability to prevent catastrophic null propagation?",
  "Be <b>conservative with non-null (!) on lists and top-level object fields</b>. Prefer:<pre>\n# Risky: null anywhere in the chain blanks the whole user\ntype User {\n  posts: [Post!]!   # if posts fails, user becomes null\n}\n\n# Safer: partial results survive\ntype User {\n  posts: [Post!]    # nullable list → user still returns with posts: null\n}\n\n# Or return an empty list instead of null:\nUser.posts = (user) => user.posts ?? [];\n</pre>",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "What are circular fragment references and why are they forbidden?",
  "Fragments cannot recursively reference themselves. This is caught at validation time.<pre>\n# INVALID — circular:\nfragment UserFields on User {\n  friends {\n    ...UserFields\n  }\n}\n\n# Workaround: use field nesting (no fragment):\nquery {\n  user {\n    friends {\n      friends { name }\n    }\n  }\n}\n</pre>",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "What is over-fetching from deeply nested queries?",
  "Even in GraphQL, clients can accidentally request huge nested trees (e.g., <code>user → posts → comments → author → posts → ...</code>). This is a <b>client-side</b> over-fetching problem — the schema author can't prevent it. Mitigation: <b>depth limiting, complexity analysis, pagination</b> on nested fields.",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "Compare authorization at schema level, field level, and resolver level.",
  "<b>Schema-level:</b> custom directives like <code>@auth(requires: ADMIN)</code> applied to types/fields. Clean but requires directive implementation.<br><b>Field-level:</b> check <code>ctx.currentUser</code> in each resolver. Flexible but verbose.<br><b>Resolver-level:</b> check in the root resolver only — simplest but can't restrict sub-fields differently per caller.<br>Best practice: field-level for granular control, with schema directives as sugar.",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "How do you handle file uploads in GraphQL?",
  "GraphQL doesn't natively support binary uploads. The <b>graphql-upload</b> spec adds the <code>Upload</code> scalar and multipart request format.<pre>\n# Schema:\nscalar Upload\n\ntype Mutation {\n  uploadAvatar(file: Upload!): User!\n}\n\n# Client sends multipart/form-data with:\n# - operations: { \"query\": \"mutation($file: Upload!) { uploadAvatar(file: $file) { id } }\", \"variables\": { \"file\": null } }\n# - map: { \"0\": [\"variables.file\"] }\n# - 0: [binary file data]\n</pre>Alternative: use a separate REST endpoint for uploads and return the URL to GraphQL.",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "What is schema stitching and what are common stitching conflicts?",
  "Schema stitching combines multiple GraphQL schemas into one. Conflicts arise when:<br>— Two schemas define the same type differently<br>— Field name collisions<br>— Conflicting directives or descriptions<br>— Duplicate root fields<br>Resolved via <b>merge configuration</b> in tools like <code>@graphql-tools/stitch</code>. <b>Apollo Federation</b> is the modern alternative.",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "How should you handle subscription reconnection?",
  "WebSocket connections drop. Clients must <b>reconnect and re-subscribe</b> automatically. The <code>graphql-ws</code> client has built-in retry with exponential backoff:<pre>\nimport { createClient } from 'graphql-ws';\n\nconst client = createClient({\n  url: 'ws://localhost:4000/graphql',\n  retryAttempts: Infinity,\n  shouldRetry: () => true,\n  retryWait: (retries) => new Promise(resolve =>\n    setTimeout(resolve, Math.min(2 ** retries * 100, 30000))\n  ),\n  on: {\n    closed: () => console.log('Disconnected'),\n    connected: () => console.log('Reconnected'),\n  },\n});\n</pre>Also consider <b>replay</b> of missed events on reconnect (complex, often app-specific).",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "What is cursor stability in pagination and why does it matter?",
  "A <b>cursor</b> must be <b>stable</b> — it must always point to the same item in the list. If cursors are based on mutable values (e.g., <code>lastUpdated</code>), the cursor becomes invalid when the item changes. Use <b>immutable fields</b> (e.g., <code>id</code>, <code>createdAt</code>) or a combination that guarantees uniqueness and ordering stability.",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "Can you deprecate an enum value? What happens if you remove it?",
  "You <b>can</b> deprecate enum values with <code>@deprecated</code>. <b>Never remove</b> an enum value — existing clients might send it, and older API versions reference it. Removing it is a <b>breaking change</b>. Instead, mark it deprecated and handle it gracefully (or alias to the new value in the resolver).",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "What happens when a non-null field inside a non-null list returns null?",
  "If any element of a <code>[Type!]!</code> resolves to null, the <b>entire list</b> nulls out, and that null propagates further up if the list field is non-null.<pre>\n# Schema: friends: [Character!]!\n# If the 3rd friend resolver returns null:\n# → friends becomes null (not [Character1, Character2, null])\n# → If friends is non-null, the parent becomes null too\n\n# Mitigation: use [Character]! (nullable items) or handle null items in resolver\n</pre>",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "What is the risk of allowing introspection in production?",
  "Introspection exposes the <b>entire schema</b> — types, fields, arguments, descriptions, deprecation reasons. Attackers can discover hidden/admin-only operations, understand your data model, and craft complex attacks. <b>Disable introspection in production</b> or restrict it with authentication:<pre>\n// Apollo Server 4:\nnew ApolloServer({\n  introspection: process.env.NODE_ENV !== 'production',\n});\n\n// Or use a validation rule to block __schema/__type queries\n</pre>",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "What is a 'REST endpoint fallback pattern' in GraphQL?",
  "For operations GraphQL doesn't handle well (file uploads, streaming, webhooks), create a REST endpoint alongside your GraphQL endpoint. The GraphQL schema can reference REST resources by URL/ID:<pre>\n# GraphQL schema returns a URL, client fetches it separately:\ntype File {\n  id: ID!\n  url: String!   # REST endpoint to download the file\n}\n\n# GET /files/:id → binary response\n\n# Avoids forcing everything through GraphQL.\n</pre>",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "Why might a resolver be called more times than expected?",
  "Because of the N+1 problem — a field-level resolver is called <b>once per parent object</b>. If the parent is a list of 100 items, the resolver runs 100 times. This is expected behavior. The fix is DataLoader, which defers the actual DB calls and batches them.<pre>\n# Without DataLoader:\nUser.posts called 100 times → 101 DB queries (1 for users + 100 for posts)\n\n# With DataLoader:\nUser.posts called 100 times → 2 DB queries (1 for users + 1 batched)\n# The magic: DataLoader deduplicates the 100 .load(user.id) calls\n</pre>",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "How does field argument order affect caching?",
  "Most GraphQL caches treat arguments as <b>key-value pairs</b>, so order doesn't matter. However, if you're using string-based memoization or manual cache keys, argument order may produce different keys. The GraphQL spec treats argument order as semantically insignificant — <code>(id: 1, name: \"X\")</code> and <code>(name: \"X\", id: 1)</code> are equivalent.",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "What is the danger of exposing database IDs in GraphQL?",
  "If you expose auto-incrementing integer IDs, attackers can guess/fuzz them. Use the <code>ID</code> scalar with opaque strings (UUIDs, hashed IDs, relay global IDs).<pre>\n# Bad: id: ID! → returns \"42\" (guessable)\n# Good: id: ID! → returns \"VXNlcjo0Mg==\" (base64 global ID)\n\n# Relay global ID encoding:\nfunction toGlobalId(type, id) {\n  return Buffer.from(`${type}:${id}`).toString('base64');\n}\n</pre>",
  ["graphql", "L4", "gotchas"])

c("Gotchas",
  "What happens if you query a field that no longer exists in the schema?",
  "The query <b>fails validation</b> and doesn't execute. Unlike REST where extra fields are silently ignored, GraphQL rejects unknown fields. This is a strength — it catches client bugs early — but it makes schema evolution harder because removing fields is always a breaking change. <b>Deprecate</b> instead of removing.",
  ["graphql", "L4", "gotchas"])

# ─────────────────────────────────────────────────────────
# 09 – Expert  (~20 cards)
# ─────────────────────────────────────────────────────────

c("Expert",
  "What is schema-first vs code-first development in GraphQL?",
  "<b>Schema-first:</b> Write SDL manually, then implement resolvers. Clear contract, language-agnostic.<br><b>Code-first:</b> Use language-native constructs (classes, decorators, types) that generate the SDL. Better DX with type-safe resolvers.<pre>\n# Schema-first (SDL file):\ntype User { id: ID! name: String! }\n\n# Code-first (TypeGraphQL, NestJS, gqlgen, Strawberry):\n@ObjectType()\nclass User {\n  @Field(type => ID) id: string;\n  @Field() name: string;\n}\n</pre>",
  ["graphql", "L5", "expert"])

c("Expert",
  "Compare Apollo Client vs Relay vs urql.",
  "<table>\n<tr><th></th><th>Apollo Client</th><th>Relay</th><th>urql</th></tr>\n<tr><td>Reqs</td><td>Any GraphQL API</td><td>Relay-compliant schema</td><td>Any GraphQL API</td></tr>\n<tr><td>Cache</td><td>Normalized (InMemoryCache)</td><td>Relay Store (normalized)</td><td>Normalized or document cache</td></tr>\n<tr><td>Bundle size</td><td>~34 kB</td><td>~28 kB + compiler</td><td>~7 kB</td></tr>\n<tr><td>Fragments</td><td>Optional</td><td>Required (colocated)</td><td>Optional</td></tr>\n<tr><td>Learning curve</td><td>Medium</td><td>High</td><td>Low</td></tr>\n<tr><td>Ecosystem</td><td>Largest</td><td>Meta + Community</td><td>Growing</td></tr>\n</table>Choose Apollo for broad adoption, Relay for huge apps (Meta-scale), urql for simplicity and bundle size.",
  ["graphql", "L5", "expert"])

c("Expert",
  "What is Apollo Federation and how does it work?",
  "Federation splits a single GraphQL schema across <b>multiple services</b> (subgraphs), unified by a <b>gateway</b>. Each subgraph contributes its own types and resolvers. The gateway composes them into one supergraph and routes queries.<pre>\n# User service (subgraph):\nextend type Query { user(id: ID!): User }\ntype User @key(fields: \"id\") { id: ID! name: String! }\n\n# Post service (subgraph):\ntype Post @key(fields: \"id\") { id: ID! title: String! }\nextend type User @key(fields: \"id\") { id: ID! posts: [Post!]! }  # extends User\n\n# Gateway transparently combines them.\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What are the key Federation directives?",
  "<pre>\n@key(fields: \"id\")         – marks an entity's primary key (required for entities)\n@external                 – field is resolved by another subgraph\n@requires(fields: \"...\")  – needs fields from another subgraph to resolve this one\n@provides(fields: \"...\")  – this subgraph resolves fields that another subgraph could also resolve\n@shareable                – field can be resolved by multiple subgraphs\n@override(from: \"subgraph\") – overrides another subgraph's field\n@tag                      – adds metadata (used in contracts/API variants)\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is the <code>_entities</code> query in Federation?",
  "The gateway uses <code>_entities</code> to <b>resolve entity references</b> across subgraphs. When a query spans subgraphs, the gateway fetches the entity from the owning subgraph via this special query:<pre>\nquery ($representations: [_Any!]!) {\n  _entities(representations: $representations) {\n    ... on User { id name posts { title } }\n  }\n}\n\n# representations: [{ __typename: \"User\", id: \"1\" }]\n</pre>Every subgraph must implement <code>_entities</code> and <code>_service</code> queries.",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is the <code>_service</code> query in Federation?",
  "Returns the <b>subgraph's SDL</b> (sdl field). The gateway uses it to compose the supergraph schema:<pre>\nquery { _service { sdl } }\n\n# Response: the SDL string of the subgraph\n# { \"data\": { \"_service\": { \"sdl\": \"extend type Query ...\" } } }\n</pre>Every subgraph must provide this query. The gateway calls it at startup and on schema updates.",
  ["graphql", "L6", "expert"])

c("Expert",
  "What are the differences between Federation and schema stitching?",
  "<b>Federation (Apollo):</b> declarative, directives on types, gateway auto-composes, <code>@key</code> for entity lookups, managed federation with Apollo Studio. Newer, actively developed.<br><b>Schema Stitching:</b> imperative/configuration-based, more flexible (can transform schemas arbitrarily), manual resolver delegation, can combine non-GraphQL sources, has schema directives but they're optional. Older approach (pre-Federation).<br>Federation is generally preferred for new projects; stitching for complex legacy integrations.",
  ["graphql", "L6", "expert"])

c("Expert",
  "When should you use a monolithic GraphQL schema vs a federated schema?",
  "<b>Monolithic</b>: Single team, small-medium project, simple domain, one codebase, low operational overhead.<br><b>Federated</b>: Multiple teams owning different domains, need independent deployment, large organization, different languages/frameworks per domain. The operational complexity of Federation is significant — don't prematurely federate.",
  ["graphql", "L5", "expert"])

c("Expert",
  "When is GraphQL <b>NOT</b> the right choice?",
  "<b>1. Simple CRUD</b> – REST is simpler and better tooled.<br><b>2. File-heavy APIs</b> – file uploads/downloads are awkward in GraphQL.<br><b>3. Real-time gaming</b> – latency-sensitive, leverages binary protocols; gRPC/WebSocket custom is better.<br><b>4. Internal service-to-service</b> – gRPC (with protobuf) is faster, typed, and has better performance tooling.<br><b>5. Cache-heavy read workloads</b> – REST with HTTP caching is simpler.<br><b>6. Simple microservice architectures</b> – each service having its own GraphQL endpoint is an anti-pattern.",
  ["graphql", "L5", "expert"])

c("Expert",
  "What is the 'BFF' (Backend For Frontend) pattern with GraphQL?",
  "A dedicated GraphQL layer sits between frontend(s) and backend services. Each frontend (mobile, web, TV) gets its own optimized BFF. The BFF aggregates data from multiple services and tailors it to the specific frontend's needs. GraphQL is a natural fit because the client specifies exactly what it needs.<pre>\n[Web App] ──→ [Web BFF (GraphQL)] ──→ [User Service]\n[Mobile]  ──→ [Mobile BFF (GraphQL)] ──→ [Product Service]\n                                        → [Order Service]\n</pre>",
  ["graphql", "L5", "expert"])

c("Expert",
  "What is a REST + GraphQL hybrid approach?",
  "Expose a GraphQL endpoint for read-focused UI needs and REST endpoints for file uploads, webhooks, and third-party integrations. The GraphQL schema can reference REST resources:<pre>\n# GraphQL for complex reads:\nquery { user(id: 1) { name posts { title } } }\n\n# REST for file upload:\nPOST /files (multipart/form-data)\n\n# REST for webhooks:\nPOST /webhooks/stripe (external services call this)\n</pre>The key insight: GraphQL doesn't have to be the <b>only</b> API.",
  ["graphql", "L5", "expert"])

c("Expert",
  "Compare subscriptions vs polling vs live queries for real-time data.",
  "<b>Subscriptions:</b> Push-based, server pushes events. Low latency, high complexity (WebSocket management). Best for event-driven updates.<br><b>Polling:</b> Client sends query periodically. Simple, no persistent connection, works everywhere. High latency and waste (requests when nothing changed). Good for rare changes.<br><b>Live queries:</b> Like a query that stays open and pushes updated results. Simplest client code but high server cost (re-evaluates entire query on any data change). Experimental.",
  ["graphql", "L5", "expert"])

c("Expert",
  "What is the Relay Connections spec in detail?",
  "A standardized pagination model with these types:<pre>\n# Connection type — wraps the paginated results\ntype XxxConnection {\n  edges: [XxxEdge!]!\n  pageInfo: PageInfo!\n  totalCount: Int!\n}\n\n# Edge type — represents one item + its cursor\ntype XxxEdge {\n  node: Xxx!\n  cursor: String!\n}\n\n# PageInfo — navigation metadata\ntype PageInfo {\n  hasNextPage: Boolean!\n  hasPreviousPage: Boolean!\n  startCursor: String\n  endCursor: String\n}\n\n# Arguments: first/last (Int), after/before (String)\n</pre>The cursor is an opaque string (often base64-encoded) that identifies the item's position.",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is GraphQL Code Generator (codegen)?",
  "A tool that generates typed code (TypeScript, Flow, Kotlin, Swift, etc.) from your GraphQL schema and operations. It reads <code>.graphql</code> files and outputs type-safe hooks, components, and SDK functions.<pre>\n# Query:\nquery GetUser($id: ID!) { user(id: $id) { name email } }\n\n# Generated TypeScript:\nconst { data } = useGetUserQuery({ variables: { id: '1' } });\n// data: { user?: { name: string, email: string } | null }\n\n# Config: codegen.ts\n# plugins: typescript, typescript-operations, typescript-react-apollo\n</pre>Essential for large TypeScript GraphQL projects.",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is GraphQL Mesh?",
  "A tool that creates a unified GraphQL API from <b>multiple non-GraphQL sources</b>: REST, gRPC, OpenAPI/Swagger, SQL, SOAP, etc. It generates a GraphQL schema that wraps these sources, letting you query everything with GraphQL.<pre>\n# .meshrc.yml:\nsources:\n  - name: Users\n    handler:\n      openapi:\n        source: ./users-openapi.yml\n  - name: Products\n    handler:\n      grpc:\n        endpoint: localhost:50051\n\n# Query everything via GraphQL!\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is the GraphQL over HTTP spec?",
  "A formal specification (draft, nearing RFC status) that defines <b>exactly</b> how GraphQL should be served over HTTP. Key points: uses POST by default, <code>application/json</code> content type, server SHOULD support GET for queries, <code>application/graphql-response+json</code> media type for the response, defines status codes for success/error/partial responses.<pre>\n# New media type distinguishes GraphQL responses from generic JSON:\nContent-Type: application/graphql-response+json\n\n# Status codes:\n200 – data present (with or without errors)\n400 – validation error (no data)\n...\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What are the GraphQL security best practices?",
  "<pre>\n1. Disable introspection in production\n2. Query depth limiting (max 5-10 levels)\n3. Query complexity analysis (cost-based limits)\n4. Rate limiting (per user/IP, token bucket or sliding window)\n5. Allow-lists (with APQ, only known queries execute)\n6. Timeout (max execution time, cancel long-running queries)\n7. Pagination required (never return unlimited lists)\n8. Field-level authorization (not just resolver-level)\n9. Sanitize error messages (no stack traces in production)\n10. Use graphql-armor or secureGraphQL middleware\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is graphql-armor?",
  "A middleware for GraphQL servers that bundles multiple security protections into one package. Includes: character limit, query depth, aliases limit, cost analysis, block field suggestions. Works with Apollo, Yoga, Envelop, etc.<pre>\nimport { EnvelopArmorPlugin } from '@escape.tech/graphql-armor';\n\nconst server = createYoga({\n  plugins: [\n    EnvelopArmorPlugin({\n      maxDepth: { n: 6 },\n      maxAliases: { n: 15 },\n      costLimit: { maxCost: 5000 },\n    }),\n  ],\n});\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "How do you build a custom GraphQL gateway?",
  "Use <code>@graphql-tools</code> to stitch or delegate schemas. The gateway serves as a <b>single entry point</b> that routes fields to the appropriate upstream service:<pre>\nimport { stitchSchemas } from '@graphql-tools/stitch';\n\nconst gateway = stitchSchemas({\n  subschemas: [\n    { schema: userSchema, executor: makeHTTPExecutor('http://user-svc/graphql') },\n    { schema: postSchema, executor: makeHTTPExecutor('http://post-svc/graphql') },\n  ],\n});\n\n// Or with Apollo Federation:\nimport { ApolloGateway } from '@apollo/gateway';\nconst gateway = new ApolloGateway({\n  supergraphSdl: new IntrospectAndCompose({\n    subgraphs: [{ name: 'users', url: 'http://...' }],\n  }),\n});\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is the supergraph in Apollo Federation?",
  "The <b>composed schema</b> resulting from merging all subgraphs. It includes the combined type definitions, entity keys, and all the routing/query-plan information. It can be pre-composed (static supergraph SDL) or composed at runtime. Apollo Studio provides managed federation with automated composition checks.",
  ["graphql", "L6", "expert"])

c("Expert",
  "What does <code>@shareable</code> do in Federation?",
  "Marks a field that can be <b>resolved by multiple subgraphs</b>. Without <code>@shareable</code>, a field can only be defined/owned by one subgraph.<pre>\n# Both subgraphs define 'name' — allowed because @shareable:\n# Subgraph A (users):\ntype User @key(fields: \"id\") {\n  id: ID!\n  name: String! @shareable\n}\n\n# Subgraph B (reviews):\ntype User @key(fields: \"id\") {\n  id: ID!\n  name: String! @shareable\n  reviews: [Review!]!\n}\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What does <code>@override</code> do in Federation?",
  "Tells the gateway to route a field to a <b>different subgraph</b> than the one that owns the type. Useful for migrating fields between services.<pre>\n# Subgraph A (users-v2) — new owner of 'email':\nextend type User @key(fields: \"id\") {\n  id: ID!\n  email: String! @override(from: \"users-v1\")\n}\n\n# Subgraph B (users-v1) — old owner, now overridden:\ntype User @key(fields: \"id\") {\n  id: ID!\n  email: String!  # overridden by users-v2\n}\n\n# Gateway routes email queries to users-v2.\n</pre>",
  ["graphql", "L6", "expert"])

# ─────────────────────────────────────────────────────────
# 10 – Bonus: Advanced/Edge cases  (~14 cards)
# ─────────────────────────────────────────────────────────

c("Expert",
  "What is a `GraphQL Directive` and how do you define a custom one in SDL?",
  "A directive is a schema annotation that modifies behavior. Defined with <code>directive @name on TARGET</code>:<pre>\ndirective @auth(\n  requires: Role = ADMIN,\n) on OBJECT | FIELD_DEFINITION | ARGUMENT_DEFINITION\n\n# Target locations:\n# SCHEMA, SCALAR, OBJECT, FIELD_DEFINITION, ARGUMENT_DEFINITION,\n# INTERFACE, UNION, ENUM, ENUM_VALUE, INPUT_OBJECT, INPUT_FIELD_DEFINITION\n</pre>You must implement the directive's behavior in your server code (schema transform or middleware).",
  ["graphql", "L6", "expert"])

c("Expert",
  "How does the <code>@defer</code> and <code>@stream</code> incremental delivery work technically?",
  "The server uses <b>multipart/mixed</b> or <b>text/event-stream</b> content-type to push multiple payloads over a single HTTP connection. Each chunk is a partial GraphQL response.<pre>\n# HTTP Response (multipart/mixed):\nContent-Type: multipart/mixed; boundary=\"-\"\n\n---\nContent-Type: application/json\n\n{ \"data\": { \"user\": { \"name\": \"Luke\" } }, \"hasNext\": true }\n---\nContent-Type: application/json\n\n{ \"incremental\": [{ \"data\": { \"slowComputation\": 42 }, \"path\": [\"user\"] }], \"hasNext\": false }\n-----\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is the GraphQL multipart request specification (for file uploads)?",
  "Extends the standard GraphQL HTTP request to support binary uploads. Uses <code>multipart/form-data</code> with three parts:<br><b>operations</b>: JSON string of the GraphQL request<br><b>map</b>: JSON mapping file indices to variable paths<br><b>file parts</b>: binary data keyed by index<pre>\nPOST /graphql\nContent-Type: multipart/form-data\n\n--boundary\nContent-Disposition: form-data; name=\"operations\"\n\n{ \"query\": \"mutation($file: Upload!) { upload(file: $file) { id } }\",\n  \"variables\": { \"file\": null } }\n--boundary\nContent-Disposition: form-data; name=\"map\"\n\n{ \"0\": [\"variables.file\"] }\n--boundary\nContent-Disposition: form-data; name=\"0\"; filename=\"photo.jpg\"\n\n[binary data]\n--boundary--\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is GraphQL Yoga?",
  "A <b>fully-featured GraphQL Server</b> built by The Guild on top of <code>graphql-js</code> and the Envelop plugin system. Supports: GraphQL over HTTP spec, subscriptions over SSE, file uploads, persisted queries, response caching, rate limiting, and more — all pluggable. Uses a plugin-based architecture (<b>Envelop</b>).<pre>\nimport { createYoga } from 'graphql-yoga';\n\nconst yoga = createYoga({ schema });\nconst server = createServer(yoga);\nserver.listen(4000);\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is the Envelop plugin system?",
  "A <b>GraphQL plugin system</b> from The Guild. Provides hooks into every phase of GraphQL execution (parse, validate, context building, execute, subscribe). Plugins are composable.<pre>\nimport { envelop, useLogger, useTiming } from '@envelop/core';\n\nconst getEnveloped = envelop({\n  plugins: [\n    useLogger(),\n    useTiming(),\n    // custom plugins, auth, rate limiting, etc.\n  ],\n});\n\n// Yoga uses Envelop internally.\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "How does GraphQL handle circular references in types?",
  "The <b>schema</b> allows circular references (e.g., <code>User → Post → User</code>). The <b>resolver</b> must handle termination. The <b>query</b> can request finite depth only (otherwise it's infinitely deep and rejected by depth limiting).<pre>\ntype User { id: ID! posts: [Post!]! }\ntype Post { id: ID! author: User! comments: [Comment!]! }\ntype Comment { id: ID! post: Post! }\n\n# Danger: user → posts → author → posts → ...\n# Safe: { user { posts { title } } }  # finite depth\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is a `GraphQL execution context`?",
  "The per-request state created by the server before execution begins. It includes the parsed document, schema, variable values, context object, operation to execute, and the root value. The execution engine uses this throughout the request lifecycle.",
  ["graphql", "L6", "expert"])

c("Expert",
  "What are the steps of the GraphQL execution pipeline?",
  "<pre>\n1. Parse       – string → Document AST\n2. Validate    – AST + Schema → errors or ok\n3. CoerceVariableValues – variables against schema types\n4. Execute     – walk the AST, call resolvers\n   a. For each field in the selection set:\n      - Resolve the field (call resolver)\n      - Complete the value (coerce to type)\n      - Recurse into sub-selection\n5. Serialize  – result → JSON response\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What does the <code>@requires</code> directive do in Federation?",
  "Declares that a field depends on <b>fields from another subgraph</b> to compute its value. The gateway fetches those fields first, then passes them to this subgraph.<pre>\n# Reviews subgraph:\ntype Review @key(fields: \"id\") {\n  id: ID!\n  body: String!\n  author: User! @provides(fields: \"username\")\n}\n\ntype User @key(fields: \"id\") {\n  id: ID!\n  username: String! @external\n  reviews: [Review!]! @requires(fields: \"username\")\n  # 'reviews' needs 'username' from Users subgraph to filter properly\n}\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is the difference between <code>@provides</code> and <code>@external</code>?",
  "<code>@external</code> marks a field that is <b>owned by another subgraph</b> but needed locally. It must be resolved by the owning subgraph first, and the value is passed via <code>@requires</code>.<br><code>@provides</code> tells the gateway that a child entity field can be <b>resolved by this subgraph</b> instead of the owning subgraph, saving a cross-service hop.<pre>\n# If User.email is @shareable and this subgraph returns it:\ntype Review {\n  author: User! @provides(fields: \"email\")\n  # Gateway can use review subgraph's User.email, skipping users service\n}\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is the <code>@oneOf</code> input directive?",
  "A proposal/pattern for marking an input type where <b>exactly one field</b> must be provided. Used to model discriminated unions in input data.<pre>\ndirective @oneOf on INPUT_OBJECT\n\ninput PetInput @oneOf {\n  cat: CatInput\n  dog: DogInput\n  fish: FishInput\n}\n\n# Client must provide exactly one:\n# Valid: { cat: { name: \"Whiskers\" } }\n# Invalid: { cat: {...}, dog: {...} }  (more than one)\n# Invalid: {}  (none provided)\n</pre>Adopted by GraphQL Yoga v3+ and some other servers.",
  ["graphql", "L6", "expert"])

c("Expert",
  "How do you handle batching for different field arguments with DataLoader?",
  "Use a composite cache key with <code>cacheKeyFn</code>:<pre>\nconst postsLoader = new DataLoader(async (keys) => {\n  // keys: [{userId: 1, status: 'PUBLISHED'}, {userId: 2, status: 'DRAFT'}]\n  const results = await db.posts.find({\n    $or: keys.map(k => ({ authorId: k.userId, status: k.status })),\n  });\n  return keys.map(k => results.filter(r => r.authorId === k.userId && r.status === k.status));\n}, {\n  cacheKeyFn: (key) => `${key.userId}:${key.status}`,\n});\n\n// Resolver:\nUser.posts = (user, args) => postsLoader.load({ userId: user.id, status: args.status });\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is a good strategy for handling GraphQL errors in the client?",
  "<pre>\n1. Always check response.errors even when response.data is present\n2. Distinguish between graphQLErrors and networkError\n3. Use error extensions.code for programmatic handling\n4. Show user-friendly messages, not raw GraphQL errors\n5. Retry on network errors (exponential backoff)\n6. Use error links/policies in your client library\n\n// Apollo Client error link:\nconst errorLink = onError(({ graphQLErrors, networkError }) => {\n  if (graphQLErrors) {\n    graphQLErrors.forEach(({ message, extensions }) => {\n      if (extensions?.code === 'UNAUTHENTICATED') logout();\n    });\n  }\n  if (networkError) console.log(`Network error: ${networkError}`);\n});\n</pre>",
  ["graphql", "L6", "expert"])

c("Expert",
  "What is GraphQL's approach to versioning?",
  "GraphQL <b>avoids versioning</b>. Instead, you <b>evolve</b> the schema by:<br>1. Add new fields and types (backward compatible)<br>2. Deprecate old fields with <code>@deprecated</code><br>3. Never remove fields or rename types<br>4. Avoid changing field types (except nullability — adding <code>!</code> is breaking)<br>The schema is a <b>living contract</b> that grows but never breaks.<pre>\n@deprecated(reason: \"Use 'displayName' instead\")\nname: String\ndisplayName: String\n</pre>",
  ["graphql", "L6", "expert"])

# ─────────────────────────────────────────────────────────
# Compose & Write
# ─────────────────────────────────────────────────────────

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
