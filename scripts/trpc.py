import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "tRPC"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Procedures":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Procedures"),
    "Middleware":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Middleware-Context"),
    "NextJS":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-NextJS-Integration"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Advanced-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ==================== 01-Fundamentals ====================

c("Fundamentals",
  "What is tRPC?",
  "tRPC (TypeScript Remote Procedure Call) is a framework for building <b>end-to-end typesafe APIs</b>. It lets you call server functions from the client with full TypeScript type safety — no code generation, no schema stitching. You define a router on the server, infer its type, and use that type on the client.<br><br>Key idea: <b>share types between server and client</b> without REST/GraphQL boilerplate.",
  ["fundamentals", "definition"])

c("Fundamentals",
  "What does 'end-to-end typesafety' mean in tRPC?",
  "The server defines procedures with input/output Zod schemas. The <b>AppRouter type</b> is inferred from the server code. The client imports that type and gets full autocomplete, type-checking, and error detection for every procedure call — from UI all the way to the database query, all in TypeScript.<br><br><code>type AppRouter = typeof appRouter</code> — this single line bridges server and client types.",
  ["fundamentals", "typesafety"])

c("Fundamentals",
  "How does tRPC differ from REST?",
  "<b>tRPC:</b> No URL design, no HTTP method selection, no OpenAPI spec. You define procedures as functions. Types flow automatically. Input validation is built-in via Zod.<br><b>REST:</b> Stateless resources over HTTP verbs. Requires manual type definitions, separate API docs, and client SDK generation. Better for public APIs consumed by diverse clients.",
  ["fundamentals", "rest-comparison"])

c("Fundamentals",
  "How does tRPC differ from GraphQL?",
  "<b>tRPC:</b> Functions, not queries. No query language to learn. No schema-first design. No N+1 problem baked in. Simpler mental model — just call a TS function.<br><b>GraphQL:</b> Declarative query language. Client specifies exact fields. Better for aggregating data from multiple sources. Has a steeper learning curve and more infrastructure (resolvers, schema, Apollo/Relay).",
  ["fundamentals", "graphql-comparison"])

c("Fundamentals",
  "How does tRPC differ from gRPC?",
  "<b>tRPC:</b> TypeScript only. Uses HTTP/JSON (or WebSocket). No .proto files. Types inferred from TS code.<br><b>gRPC:</b> Language-agnostic via Protocol Buffers. Requires .proto files and code generation. Uses HTTP/2. Better for polyglot microservice architectures and high-throughput streaming.",
  ["fundamentals", "grpc-comparison"])

c("Fundamentals",
  "What is the Router/Procedure model in tRPC?",
  "A <b>Router</b> is a collection of <b>Procedures</b>. Each procedure is a query, mutation, or subscription. Routers can be nested and merged. The mental model: your API is a tree of typed function calls.<br><br><pre><code>const appRouter = router({\n  user: router({\n    list: publicProcedure.query(() => db.user.findMany()),\n    byId: publicProcedure.input(z.string()).query(({ input }) => db.user.findById(input)),\n  }),\n});</code></pre>",
  ["fundamentals", "router-procedure"])

c("Fundamentals",
  "What does tRPC <b>NOT</b> do?",
  "tRPC does <b>NOT</b> do:<br>• Code generation (types are inferred)<br>• Schema-first design (no .proto / .graphql files)<br>• HTTP routing (it hooks into an existing server like Express, Fastify, or Next.js)<br>• Transport layer abstraction (it's JSON/HTTP by default, you add WS if needed)<br>• Multi-language support (TypeScript only)",
  ["fundamentals", "what-trpc-isnt"])

c("Fundamentals",
  "What changed in tRPC v11 (the 'new' API)?",
  "tRPC v11 brought:<br>• <b>Clerk-style init</b>: <code>const t = initTRPC.create()</code> pattern stabilized<br>• <b>createCallerFactory</b> for server-side tRPC calls<br>• <b>Better React Query v5 integration</b><br>• <b>Suspense-ready</b> hooks: <code>trpc.hello.useSuspenseQuery()</code><br>• <b>Standalone</b> adapter improvements for Express/Fastify<br>• Removed <code>@trpc/next</code> in favor of <code>@trpc/react-query</code><br>• <code>headers()</code> / <code>cookies()</code> async from next/headers",
  ["fundamentals", "v11"])

c("Fundamentals",
  "What is the central tRPC instance — the entry point for everything?",
  "<pre><code>import { initTRPC } from '@trpc/server';\nimport superjson from 'superjson';\n\nconst t = initTRPC.create({\n  transformer: superjson,\n  errorFormatter({ shape, error }) {\n    return { ...shape, data: { ...shape.data, zodError: error.cause } };\n  },\n});\n\nexport const router = t.router;\nexport const publicProcedure = t.procedure;</code></pre><br>The <code>t</code> object is the factory for routers, procedures, and middleware.",
  ["fundamentals", "initTRPC"])

c("Fundamentals",
  "What are the three procedure types?",
  "<b>Query</b> — read data (GET, idempotent, cached)<br><b>Mutation</b> — write/update data (POST, side effects)<br><b>Subscription</b> — push data from server to client (WebSocket, SSE)<br><br><pre><code>t.procedure.query(() => ...);\nt.procedure.mutation(() => ...);\nt.procedure.subscription(() => ...);</code></pre>",
  ["fundamentals", "procedure-types"])

c("Fundamentals",
  "What is the 'magic import' that bridges server types to the client?",
  "<pre><code>// server/trpc.ts\nexport const appRouter = router({ ... });\nexport type AppRouter = typeof appRouter;\n\n// client/trpc.ts — imports ONLY the type\nimport type { AppRouter } from '@/server/trpc';\nimport { createTRPCReact } from '@trpc/react-query';\nexport const trpc = createTRPCReact&lt;AppRouter&gt;();</code></pre><br><code>import type</code> is erased at runtime — zero bytes on the client.",
  ["fundamentals", "type-bridge"])

c("Fundamentals",
  "What server adapters does tRPC support?",
  "tRPC ships with adapters for:<br>• <b>Fetch API</b> (<code>@trpc/server/adapters/fetch</code>) — Next.js App Router, Cloudflare Workers, Deno<br>• <b>Express</b> (<code>@trpc/server/adapters/express</code>)<br>• <b>Fastify</b> (<code>@trpc/server/adapters/fastify</code>)<br>• <b>Standalone</b> (<code>@trpc/server/adapters/standalone</code>) — built-in Node.js HTTP server<br>• <b>Next.js Pages Router</b> (<code>@trpc/server/adapters/next</code> — legacy in v11, use fetch adapter)<br><br>The fetch adapter is universal: any runtime with the Fetch API (Next.js, Cloudflare, Deno, Bun, Hono).",
  ["fundamentals", "adapters"])

c("Fundamentals",
  "How does tRPC relate to HTTP?",
  "tRPC uses HTTP as a <b>transport layer</b>, not as an API design paradigm. All requests go to a single endpoint (<code>/api/trpc</code>). The procedure path is sent in the request body or as a query parameter.<br><br><b>Queries</b> can use GET with <code>?input=...</code> query params (via <code>httpBatchLink</code>) or POST with JSON body.<br><b>Mutations</b> always use POST with JSON body.<br><b>Subscriptions</b> use WebSocket or SSE (HTTP streaming).<br><br>You don't design URL paths — you design TypeScript functions.",
  ["fundamentals", "http-relationship"])

c("Fundamentals",
  "What is the tRPC client bundle size impact?",
  "The tRPC client (<code>@trpc/client</code> + <code>@trpc/react-query</code>) adds ~5-8 KB gzipped. The <code>import type { AppRouter }</code> is fully erased at runtime — zero bytes. React Query (<code>@tanstack/react-query</code>) is the largest dependency at ~12 KB gzipped.<br><br>Total tRPC stack (client): ~20 KB gzipped. Comparable to a typed fetch wrapper. Much smaller than Apollo Client (~35 KB) or Relay (~40 KB).<br><br>The <b>server</b> (<code>@trpc/server</code>) is ~10 KB gzipped — lightweight enough for serverless.",
  ["fundamentals", "bundle-size"])

# ==================== 02-Core-Operations ====================

c("CoreOps",
  "How do you create the central tRPC instance?",
  "<pre><code>import { initTRPC } from '@trpc/server';\n\nconst t = initTRPC.create();\n\n// Destructure what you need:\nexport const router = t.router;\nexport const publicProcedure = t.procedure;\nexport const middleware = t.middleware;\nexport const mergeRouters = t.mergeRouters;</code></pre><br>You can pass <code>transformer</code>, <code>errorFormatter</code>, etc. to <code>initTRPC.create({})</code>.",
  ["core-ops", "initTRPC"])

c("CoreOps",
  "How do you define a basic router?",
  "<pre><code>import { router, publicProcedure } from './trpc';\nimport { z } from 'zod';\n\nconst userRouter = router({\n  list: publicProcedure.query(() => {\n    return db.user.findMany();\n  }),\n  byId: publicProcedure\n    .input(z.object({ id: z.string().uuid() }))\n    .query(({ input }) => db.user.findById(input.id)),\n  create: publicProcedure\n    .input(z.object({ name: z.string(), email: z.string().email() }))\n    .mutation(({ input }) => db.user.create({ data: input })),\n});</code></pre>",
  ["core-ops", "router-definition"])

c("CoreOps",
  "How do you merge multiple sub-routers into one appRouter?",
  "<pre><code>const appRouter = router({\n  user: userRouter,\n  post: postRouter,\n  health: router({\n    ping: publicProcedure.query(() => 'pong'),\n  }),\n});\n\nexport type AppRouter = typeof appRouter;</code></pre><br>Routers compose naturally — just nest them. No special merge function needed for nesting; <code>mergeRouters</code> is for merging two flat routers horizontally.",
  ["core-ops", "merge-routers"])

c("CoreOps",
  "What is the tRPC context and how do you create it?",
  "Context is per-request state (request headers, user session, database). Created via a factory function:<br><pre><code>const createContext = async ({ req }: CreateNextContextOptions) => {\n  const session = await getServerSession(req);\n  return { session, db: prisma };\n};\n\nexport type Context = Awaited&lt;ReturnType&lt;typeof createContext&gt;&gt;;</code></pre><br>Every procedure receives this context as its first argument.",
  ["core-ops", "context"])

c("CoreOps",
  "What is <code>createCallerFactory</code> used for?",
  "It creates a <b>server-side tRPC caller</b> — you can call your tRPC procedures from another server context (e.g., server actions, testing, background jobs) without HTTP.<br><pre><code>const createCaller = createCallerFactory(appRouter);\nconst caller = createCaller(ctx);\nconst users = await caller.user.list();</code></pre><br>Same types, same context, no HTTP overhead.",
  ["core-ops", "createCallerFactory"])

c("CoreOps",
  "How to use <code>createTRPCContext</code> for Next.js app router?",
  "<pre><code>import { fetchRequestHandler } from '@trpc/server/adapters/fetch';\n\nconst handler = (req: Request) =>\n  fetchRequestHandler({\n    endpoint: '/api/trpc',\n    req,\n    router: appRouter,\n    createContext: () => ({ db: prisma }),\n  });\n\nexport { handler as GET, handler as POST };</code></pre><br>The handler is a standard Request/Response fetch handler — works with any framework using the Fetch API.",
  ["core-ops", "createTRPCContext"])

c("CoreOps",
  "How does <code>t.procedure.input()</code> work?",
  "<code>.input(validator)</code> attaches a validation schema to a procedure. The schema is typically a <b>Zod object</b>. The validated data is available as <code>input</code> in the procedure resolver.<br><br>Validation happens <b>before</b> the resolver runs. Invalid input returns a 400 error automatically — your resolver never sees bad data.<br><br><pre><code>.input(z.object({ page: z.number().min(1).default(1), limit: z.number().min(1).max(100).default(10) }))</code></pre>",
  ["core-ops", "input-validation"])

c("CoreOps",
  "How do you define a query?",
  "<pre><code>export const postRouter = router({\n  latest: publicProcedure.query(async ({ ctx }) => {\n    const posts = await ctx.db.post.findMany({\n      take: 10,\n      orderBy: { createdAt: 'desc' },\n    });\n    return posts;\n  }),\n});</code></pre><br>Queries are for <b>reading</b> data. React Query caches them automatically on the client.",
  ["core-ops", "query-definition"])

c("CoreOps",
  "How do you define a mutation?",
  "<pre><code>export const postRouter = router({\n  create: publicProcedure\n    .input(z.object({ title: z.string(), content: z.string() }))\n    .mutation(async ({ ctx, input }) => {\n      const post = await ctx.db.post.create({ data: input });\n      return post;\n    }),\n});</code></pre><br>Mutations are for <b>writing/updating</b> data. Not cached; they invalidate queries on success.",
  ["core-ops", "mutation-definition"])

c("CoreOps",
  "How is TypeScript inference set up to share types between server and client?",
  "<pre><code>// server/root.ts\nexport const appRouter = router({\n  user: userRouter,\n  post: postRouter,\n});\nexport type AppRouter = typeof appRouter;\n\n// client/trpc.ts\nimport type { AppRouter } from '@/server/root';\nimport { createTRPCReact } from '@trpc/react-query';\nexport const trpc = createTRPCReact&lt;AppRouter&gt;();</code></pre><br>Now the client has full autocomplete: <code>trpc.user.list.useQuery()</code> knows the return type.",
  ["core-ops", "type-inference"])

c("CoreOps",
  "How do you configure tRPC with a data transformer like superjson?",
  "<pre><code>import superjson from 'superjson';\n\nconst t = initTRPC.create({\n  transformer: superjson, // serialize/deserialize Dates, Maps, Sets, BigInt\n});</code></pre><br>Both server and client must use the same transformer. The transformer is applied to <b>inputs</b> (client→server) and <b>outputs</b> (server→client). Without superjson, <code>Date</code> objects become strings.",
  ["core-ops", "transformer"])

c("CoreOps",
  "How does <code>t.mergeRouters</code> differ from nested routers?",
  "<b>Nested routers</b> create namespaces: <code>router({ user: userRouter })</code> → procedures are at <code>user.list</code>.<br><b>mergeRouters</b> flattens two routers into one level: <code>mergeRouters(userRouter, postRouter)</code> → <code>list</code> from both routers conflict directly.<br><br><pre><code>// ✅ Nesting (recommended for domain separation)\nconst appRouter = router({ user: userRouter, post: postRouter });\n\n// ⚠️ Merging (used for composing base routers)\nconst appRouter = mergeRouters(baseRouter, featureRouter);</code></pre><br>Use nesting for namespacing. Use <code>mergeRouters</code> to compose multiple root routers when you need a flat structure.",
  ["core-ops", "mergeRouters"])

c("CoreOps",
  "What is the full tRPC request lifecycle (from client call to server response)?",
  "1. Client calls <code>trpc.user.list.useQuery()</code><br>2. React Query triggers a fetch via tRPC link chain<br>3. <b>Links</b> transform/modify the operation (logger, batching, etc.)<br>4. HTTP link serializes the operation path + input to JSON/query params<br>5. Server receives HTTP request at <code>/api/trpc</code><br>6. Fetch adapter parses the request, extracts path and input<br>7. <b>Context</b> is created (<code>createContext</code>)<br>8. <b>Middlewares</b> execute in order (logger → rate-limit → auth → ...)<br>9. <b>Input validation</b> runs (Zod schema)<br>10. <b>Resolver</b> executes with <code>{ ctx, input }</code><br>11. <b>Output validation</b> runs (if <code>.output()</code> is set)<br>12. Response is serialized (transformer) and sent back<br>13. Link chain unwraps the response (deserialize)<br>14. React Query stores the result in cache<br>15. Component re-renders with data",
  ["core-ops", "lifecycle"])

c("CoreOps",
  "How to use <code>.meta()</code> on a procedure?",
  "<pre><code>const openApiProcedure = publicProcedure\n  .meta({ openapi: { method: 'GET', path: '/users', summary: 'List all users' } })\n  .input(z.object({ limit: z.number().optional() }))\n  .query(({ input }) => db.user.findMany({ take: input.limit }));</code></pre><br><code>.meta()</code> attaches arbitrary metadata to a procedure — used by plugins (trpc-openapi, logging, rate-limiting rules). Accessible in middleware via <code>op.meta</code>. The metadata is <b>type-safe</b> if you configure <code>initTRPC</code> with a meta type.",
  ["core-ops", "meta"])

# ==================== 03-Procedures ====================

c("Procedures",
  "Query vs Mutation vs Subscription — what's the distinction?",
  "<b>Query:</b> Read. Idempotent, cacheable, re-fetched on window focus. Uses HTTP GET.<br><b>Mutation:</b> Write/update. Side effects. Invalidates cache on success. Uses HTTP POST.<br><b>Subscription:</b> Push from server. Long-lived connection (WebSocket/SSE). For real-time data. Use sparingly — polling often suffices.",
  ["procedures", "query-vs-mutation"])

c("Procedures",
  "How to validate input with Zod in a procedure?",
  "<pre><code>publicProcedure\n  .input(z.object({\n    email: z.string().email('Invalid email'),\n    age: z.number().min(0).max(150),\n  }))\n  .query(({ input }) => {\n    // input.email is string, input.age is number — fully typed\n    return findUser(input.email);\n  })</code></pre><br>The Zod schema provides both <b>runtime validation</b> and <b>TypeScript type inference</b>.",
  ["procedures", "zod-validation"])

c("Procedures",
  "How do you handle errors in tRPC?",
  "<pre><code>import { TRPCError } from '@trpc/server';\n\npublicProcedure.query(async ({ ctx }) => {\n  if (!ctx.user) {\n    throw new TRPCError({\n      code: 'UNAUTHORIZED',\n      message: 'You must be logged in',\n    });\n  }\n  return ctx.user;\n});</code></pre><br>Always throw <code>TRPCError</code> — it serializes properly over HTTP and the client gets a typed error.",
  ["procedures", "error-handling"])

c("Procedures",
  "List all tRPC error codes.",
  "<code>BAD_REQUEST</code> (400) — Invalid input<br><code>UNAUTHORIZED</code> (401) — Not logged in<br><code>FORBIDDEN</code> (403) — Logged in but no permission<br><code>NOT_FOUND</code> (404) — Resource missing<br><code>TIMEOUT</code> (408) — Operation timed out<br><code>CONFLICT</code> (409) — Duplicate/version conflict<br><code>PRECONDITION_FAILED</code> (412)<br><code>PAYLOAD_TOO_LARGE</code> (413)<br><code>METHOD_NOT_SUPPORTED</code> (405)<br><code>UNPROCESSABLE_CONTENT</code> (422)<br><code>TOO_MANY_REQUESTS</code> (429) — Rate limit<br><code>CLIENT_CLOSED_REQUEST</code> (499)<br><code>INTERNAL_SERVER_ERROR</code> (500) — Catch-all",
  ["procedures", "error-codes"])

c("Procedures",
  "How to use <code>output()</code> validation?",
  "<pre><code>publicProcedure\n  .input(z.object({ id: z.string() }))\n  .output(z.object({ id: z.string(), name: z.string(), email: z.string() }))\n  .query(async ({ input }) => {\n    return db.user.findById(input.id); // tRPC validates this matches the output schema\n  });</code></pre><br><code>.output()</code> is optional but acts as a <b>safety net</b> — ensures the resolver never leaks unexpected fields to the client. Uses Zod at runtime in dev.",
  ["procedures", "output-validation"])

c("Procedures",
  "How does tRPC batching work?",
  "Multiple tRPC calls made within a short window are <b>batched into a single HTTP request</b>. The server processes them and returns a single response array.<br><br>This is the default behavior with <code>httpBatchLink</code>. It reduces network requests dramatically for pages that call multiple queries on mount.<br><br>Use <code>httpLink</code> (no batching) if you need per-request isolation or streaming responses.",
  ["procedures", "batching"])

c("Procedures",
  "What happens when input validation fails?",
  "tRPC automatically returns a <code>BAD_REQUEST</code> error with Zod's error details in <code>error.cause</code>. The client receives a typed error that you can handle in your error formatter or UI.<br><br>Your resolver code is <b>never executed</b> — tRPC stops at validation. This is a strong security boundary: only validated data reaches your business logic.",
  ["procedures", "validation-failure"])

c("Procedures",
  "How to define a subscription?",
  "<pre><code>const onPost = publicProcedure\n  .input(z.object({ roomId: z.string() }))\n  .subscription(({ input }) => {\n    // return an observable\n    return observable&lt;Post&gt;((emit) => {\n      const handler = (post: Post) => emit.next(post);\n      ee.on(`post:${input.roomId}`, handler);\n      return () => ee.off(`post:${input.roomId}`, handler);\n    });\n  });</code></pre><br>Subscriptions return an Observable. The return value is a cleanup function called when the client unsubscribes.",
  ["procedures", "subscription"])

c("Procedures",
  "Where is input validation executed — client or server?",
  "<b>Server only.</b> Zod schemas are not bundled to the client (unless you explicitly share them). tRPC sends raw input over HTTP; the server validates, then calls the resolver. This means:<br>• Schemas never leak to the client<br>• Validation is a server-side guarantee<br>• You can use server-only Zod refinements (e.g., DB uniqueness checks)",
  ["procedures", "validation-location"])

c("Procedures",
  "How do async queries work in tRPC?",
  "All procedure resolvers can be async. tRPC awaits the result:<br><pre><code>publicProcedure.query(async ({ ctx, input }) => {\n  const [posts, total] = await Promise.all([\n    ctx.db.post.findMany({ take: input.limit }),\n    ctx.db.post.count(),\n  ]);\n  return { posts, total };\n});</code></pre><br>Errors thrown inside async resolvers are caught and returned as <code>INTERNAL_SERVER_ERROR</code> unless wrapped in <code>TRPCError</code>. Always use <code>TRPCError</code> for expected error cases.",
  ["procedures", "async"])

c("Procedures",
  "How to handle optional/nested properties in Zod input?",
  "<pre><code>publicProcedure\n  .input(z.object({\n    search: z.string().optional(),\n    filters: z.object({\n      tags: z.array(z.string()).optional(),\n    }).optional().default({}),\n    pagination: z.object({\n      page: z.number().default(1),\n      perPage: z.number().default(20),\n    }).optional().default({ page: 1, perPage: 20 }),\n  }))\n  .query(async ({ input }) => {\n    return db.post.findMany({\n      where: {\n        ...(input.search && { title: { contains: input.search } }),\n        ...(input.filters.tags && { tags: { hasSome: input.filters.tags } }),\n      },\n      skip: (input.pagination.page - 1) * input.pagination.perPage,\n      take: input.pagination.perPage,\n    });\n  });</code></pre><br>Use <code>.optional()</code> for optional fields. Use <code>.default()</code> to fill in missing values — input always arrives fully populated.",
  ["procedures", "optional-input"])

c("Procedures",
  "How does <code>TRPCError.cause</code> work?",
  "<code>TRPCError</code> accepts an optional <code>cause</code> property that preserves the original error chain:<br><pre><code>try {\n  const user = await db.user.findUnique({ where: { id: input.id } });\n  if (!user) throw new TRPCError({ code: 'NOT_FOUND' });\n  return user;\n} catch (e) {\n  if (e instanceof TRPCError) throw e;\n  throw new TRPCError({\n    code: 'INTERNAL_SERVER_ERROR',\n    message: 'Database query failed',\n    cause: e, // preserve original error for logging\n  });\n}</code></pre><br>The <code>cause</code> is serialized in the error response if you extend the <code>errorFormatter</code> to include it. Useful for server-side logging while sending a clean message to the client.",
  ["procedures", "trpc-error-cause"])

c("Procedures",
  "How to return nil/empty data from a tRPC procedure?",
  "Return <code>null</code>, <code>undefined</code>, or empty arrays — tRPC handles them all. The return type propagates correctly:<br><pre><code>publicProcedure\n  .input(z.object({ id: z.string() }))\n  .query(async ({ input }) => {\n    const user = await db.user.findUnique({ where: { id: input.id } });\n    return user; // User | null — TypeScript infers this, client sees it\n  });</code></pre><br>On the client, handle <code>null</code> in your component — not in the procedure. tRPC doesn't throw on <code>null</code> returns; <code>NOT_FOUND</code> requires explicitly throwing.",
  ["procedures", "null-return"])

# ==================== 04-Middleware-Context ====================

c("Middleware",
  "How do you create and use tRPC middleware?",
  "<pre><code>const t = initTRPC.create();\n\nconst loggerMiddleware = t.middleware(async ({ ctx, path, type, next }) => {\n  const start = Date.now();\n  const result = await next();\n  const duration = Date.now() - start;\n  console.log(`${type} ${path} took ${duration}ms`);\n  return result;\n});</code></pre><br><code>next()</code> calls the next middleware or the resolver. You can modify context and/or the return value.",
  ["middleware", "middleware-basics"])

c("Middleware",
  "How to extend context with auth middleware (adding <code>user</code> to ctx)?",
  "<pre><code>const authMiddleware = t.middleware(async ({ ctx, next }) => {\n  // ctx.raw is the IncomingMessage, containing headers\n  if (!ctx.user) {\n    throw new TRPCError({ code: 'UNAUTHORIZED' });\n  }\n  return next({\n    ctx: {\n      user: ctx.user, // narrows from User | null to User\n    },\n  });\n});</code></pre><br>The returned <code>ctx</code> is <b>merged</b> with the existing context for all downstream procedures.",
  ["middleware", "auth-middleware"])

c("Middleware",
  "How do you create a reusable auth middleware function?",
  "<pre><code>const isAuthed = t.middleware(({ ctx, next }) => {\n  if (!ctx.session?.user) {\n    throw new TRPCError({ code: 'UNAUTHORIZED' });\n  }\n  return next({\n    ctx: { session: ctx.session, user: ctx.session.user },\n  });\n});\n\nconst protectedProcedure = t.procedure.use(isAuthed);\n\n// Usage:\nconst secretRouter = router({\n  dashboard: protectedProcedure.query(({ ctx }) => {\n    // ctx.user is guaranteed non-null here\n    return getDashboard(ctx.user.id);\n  }),\n});</code></pre>",
  ["middleware", "auth-middleware-pattern"])

c("Middleware",
  "What is the 'protected procedure' pattern?",
  "A pre-built procedure that includes auth middleware, so you don't repeat <code>.use(authMiddleware)</code> everywhere:<br><pre><code>const protectedProcedure = t.procedure.use(isAuthed);\nconst adminProcedure = t.procedure.use(isAdmin);</code></pre><br>Common tiers:<br>• <code>publicProcedure</code> — no auth<br>• <code>protectedProcedure</code> — requires login<br>• <code>adminProcedure</code> — requires admin role",
  ["middleware", "protected-procedure"])

c("Middleware",
  "How to chain multiple middlewares?",
  "<pre><code>const enhancedProcedure = t.procedure\n  .use(loggerMiddleware)\n  .use(rateLimitMiddleware)\n  .use(authMiddleware);\n\n// All three middlewares run in order for every call:\nconst router = router({\n  sensitive: enhancedProcedure.query(({ ctx }) => ...),\n});</code></pre><br>Middlewares execute in the order they're <code>.use()</code>d. Each middleware wraps the next — the first middleware runs first, then the second, then the resolver, then unwinds back.",
  ["middleware", "chaining"])

c("Middleware",
  "How to create a rate-limiting middleware?",
  "<pre><code>import { Ratelimit } from '@upstash/ratelimit';\nimport { TRPCError } from '@trpc/server';\n\nconst ratelimit = new Ratelimit({\n  redis: Redis.fromEnv(),\n  limiter: Ratelimit.slidingWindow(10, '60 s'),\n});\n\nconst rateLimitMiddleware = t.middleware(async ({ ctx, next }) => {\n  const ip = ctx.ip ?? '127.0.0.1';\n  const { success } = await ratelimit.limit(ip);\n  if (!success) {\n    throw new TRPCError({ code: 'TOO_MANY_REQUESTS' });\n  }\n  return next();\n});</code></pre>",
  ["middleware", "rate-limit"])

c("Middleware",
  "How to create a logging middleware?",
  "<pre><code>const loggingMiddleware = t.middleware(async ({ ctx, path, type, rawInput, next }) => {\n  const result = await next();\n  if (result.ok) {\n    console.log(`OK ${type} ${path}`, { rawInput });\n  } else {\n    console.error(`ERR ${type} ${path}`, result.error.message);\n  }\n  return result;\n});</code></pre><br>The middleware result is <code>{ ok: boolean, data?: T, error?: TRPCError }</code> — check <code>result.ok</code> to differentiate success from failure.",
  ["middleware", "logging"])

c("Middleware",
  "What is the context building pattern?",
  "Build context lazily per-request in the <code>createContext</code> function. Fetch sessions, DB connections, headers — everything a procedure might need.<br><pre><code>const createContext = async (opts: CreateNextContextOptions) => {\n  const { req, res } = opts;\n  const session = await getServerAuthSession({ req, res });\n  return { session, db: prisma, headers: req.headers };\n};</code></pre><br>Keep context lean — it's created for every request.",
  ["middleware", "context-pattern"])

c("Middleware",
  "What is <code>.unstable_concat()</code> for middleware?",
  "It merges two middlewares into one, running both and combining their context extensions.<br><pre><code>const combined = middlewareA.unstable_concat(middlewareB);\nconst procedure = t.procedure.use(combined);</code></pre><br>Useful for composing middleware packages. The result is a single middleware with the merged context from both.<br><br>⚠️ API is 'unstable' — may change in future tRPC versions.",
  ["middleware", "concat"])

c("Middleware",
  "How does tRPC middleware interact with the response (return value)?",
  "Middleware can transform the result before it reaches the client:<br><pre><code>const responseMiddleware = t.middleware(async ({ next }) => {\n  const result = await next();\n  if (result.ok) {\n    return { ...result, data: { wrapper: result.data, meta: { version: 1 } } };\n  }\n  return result;\n});</code></pre><br>This wraps every successful response in an envelope. The return type propagates through the type system.",
  ["middleware", "response-transform"])

c("Middleware",
  "How to use middleware to set up per-request database transaction context?",
  "<pre><code>const transactionMiddleware = t.middleware(async ({ ctx, node }) => {\n  return ctx.db.$transaction(async (tx) => {\n    return next({ ctx: { ...ctx, tx } });\n  });\n});\n\n// The entire procedure runs in a single database transaction\nconst transactionalProcedure = t.procedure.use(transactionMiddleware);</code></pre><br>This pattern wraps the entire procedure (including all nested DB calls) in a database transaction. If the procedure throws, the transaction rolls back. Use sparingly — transactions hold DB locks.",
  ["middleware", "transaction"])

c("Middleware",
  "How to create a timing/performance middleware.",
  "<pre><code>const timingMiddleware = t.middleware(async ({ path, type, next }) => {\n  const start = performance.now();\n  const result = await next();\n  const ms = performance.now() - start;\n  result.ok\n    ? console.log(`[${ms.toFixed(2)}ms] ${type} ${path}`)\n    : console.error(`[${ms.toFixed(2)}ms] ${type} ${path} FAILED`);\n  return result;\n});</code></pre><br>Use <code>performance.now()</code> for high-precision timing. Attach via <code>t.procedure.use(timingMiddleware)</code>. Useful for finding slow queries during development.",
  ["middleware", "timing"])

# ==================== 05-NextJS-Integration ====================

c("NextJS",
  "How to set up tRPC with the Next.js app router (v11+)?",
  "<pre><code>// app/api/trpc/[trpc]/route.ts\nimport { fetchRequestHandler } from '@trpc/server/adapters/fetch';\nimport { appRouter } from '@/server/api/root';\n\nconst handler = (req: Request) =>\n  fetchRequestHandler({\n    endpoint: '/api/trpc',\n    req,\n    router: appRouter,\n    createContext: () => ({ db: prisma }),\n  });\n\nexport { handler as GET, handler as POST };</code></pre><br>Uses the standard Fetch API — no Next.js-specific handler needed.",
  ["nextjs", "app-router-setup"])

c("NextJS",
  "How to set up the tRPC <b>React client</b> for the app router?",
  "<pre><code>// trpc/react.tsx\nimport { createTRPCReact } from '@trpc/react-query';\nimport type { AppRouter } from '@/server/api/root';\n\nexport const trpc = createTRPCReact&lt;AppRouter&gt;();</code></pre><br>Then create a <b>TRPCReactProvider</b> wrapping <code>trpc</code> and <code>QueryClient</code>.",
  ["nextjs", "react-client"])

c("NextJS",
  "How to create a <code>TRPCReactProvider</code>?",
  "<pre><code>'use client';\nimport { QueryClient, QueryClientProvider } from '@tanstack/react-query';\nimport { httpBatchLink } from '@trpc/client';\nimport { trpc } from './client';\nimport { useState } from 'react';\n\nexport function TRPCReactProvider({ children }: { children: React.ReactNode }) {\n  const [queryClient] = useState(() => new QueryClient());\n  const [trpcClient] = useState(() =>\n    trpc.createClient({\n      links: [httpBatchLink({ url: '/api/trpc' })],\n    })\n  );\n  return (\n    &lt;trpc.Provider client={trpcClient} queryClient={queryClient}&gt;\n      &lt;QueryClientProvider client={queryClient}&gt;{children}&lt;/QueryClientProvider&gt;\n    &lt;/trpc.Provider&gt;\n  );\n}</code></pre>",
  ["nextjs", "provider"])

c("NextJS",
  "What is <code>httpBatchLink</code>?",
  "<code>httpBatchLink</code> batches multiple tRPC calls into a single HTTP request. All queries fired within the same microtask are combined.<br><br><pre><code>links: [httpBatchLink({ url: '/api/trpc' })]</code></pre><br>Pros: fewer network requests, faster page loads.<br>Cons: one slow query in a batch delays all responses. Use <code>httpLink</code> if you need per-request streaming or isolation.",
  ["nextjs", "httpBatchLink"])

c("NextJS",
  "What is <code>httpLink</code> vs <code>httpBatchLink</code>?",
  "<b>httpLink</b>: Each tRPC call is a separate HTTP request. Good for streaming, SSR, and when you need per-request headers.<br><br><b>httpBatchLink</b>: Multiple calls are combined into one request. Good for client-side, reduces network overhead.<br><br>In practice, <code>httpBatchLink</code> is the default recommendation for client-side. Use <code>httpLink</code> for SSR / server components.",
  ["nextjs", "httpLink"])

c("NextJS",
  "What is <code>wsLink</code> for?",
  "<code>wsLink</code> enables WebSocket-based subscriptions:<br><pre><code>links: [\n  splitLink({\n    condition: (op) => op.type === 'subscription',\n    true: wsLink({ url: 'ws://localhost:3001' }),\n    false: httpBatchLink({ url: '/api/trpc' }),\n  }),\n]</code></pre><br>Subscriptions require a long-lived connection — HTTP can't push data; WebSocket can.",
  ["nextjs", "wsLink"])

c("NextJS",
  "How does <code>splitLink</code> work?",
  "<b>splitLink</b> routes tRPC operations to different links based on a condition function:<br><pre><code>import { splitLink, httpBatchLink, wsLink } from '@trpc/client';\n\nsplitLink({\n  condition: (op) => op.type === 'subscription',\n  true: wsLink(...),\n  false: httpBatchLink(...),\n})</code></pre><br>Common uses: subscriptions→WS, everything else→HTTP; or mutations→httpLink, queries→httpBatchLink.",
  ["nextjs", "splitLink"])

c("NextJS",
  "What is <code>loggerLink</code>?",
  "<code>loggerLink</code> logs tRPC operations to the console, useful for debugging:<br><pre><code>links: [\n  loggerLink({\n    enabled: (opts) => process.env.NODE_ENV === 'development',\n  }),\n  httpBatchLink({ url: '/api/trpc' }),\n]</code></pre><br>Place it <b>first</b> in the links array to log outgoing requests, or <b>last</b> to log responses too.",
  ["nextjs", "loggerLink"])

c("NextJS",
  "How to call a tRPC query on the client with Suspense?",
  "<pre><code>'use client';\nimport { trpc } from '@/trpc/client';\n\nexport function UserList() {\n  const [users] = trpc.user.list.useSuspenseQuery();\n  return users.map(u => &lt;div key={u.id}&gt;{u.name}&lt;/div&gt;);\n}</code></pre><br><code>useSuspenseQuery</code> throws a promise if data isn't ready — wrap in a <code>&lt;Suspense&gt;</code> boundary. No loading states to manage.",
  ["nextjs", "useSuspenseQuery"])

c("NextJS",
  "How to use a tRPC mutation on the client?",
  "<pre><code>const createPost = trpc.post.create.useMutation({\n  onSuccess: () => {\n    utils.post.list.invalidate(); // refetch the list\n  },\n});\n\nconst handleSubmit = (data: CreatePostInput) => {\n  createPost.mutate(data);\n};</code></pre><br>Mutations return <code>{ mutate, mutateAsync, isLoading, isError, error, data }</code>.",
  ["nextjs", "useMutation"])

c("NextJS",
  "How to use <code>useUtils</code> for cache invalidation?",
  "<pre><code>const utils = trpc.useUtils();\n\nconst deleteUser = trpc.user.delete.useMutation({\n  onSuccess: () => {\n    utils.user.list.invalidate(); // refetch user list\n    utils.user.byId.invalidate({ id: deletedId }); // refetch specific user\n  },\n});</code></pre><br><code>useUtils()</code> gives you access to the tRPC cache utilities from React Query. Use <code>.invalidate()</code> to mark queries as stale; <code>.refetch()</code> to force immediate refetch.",
  ["nextjs", "useUtils"])

c("NextJS",
  "How to server-side prefetch a tRPC query?",
  "<pre><code>// app/users/page.tsx (Server Component)\nimport { api } from '@/trpc/server'; // server-side caller\n\nexport default async function UsersPage() {\n  const users = await api.user.list();\n  return &lt;UserList initialData={users} /&gt;;\n}</code></pre><br>The <code>trpc/server</code> import provides a <b>server-side caller</b> that directly invokes procedures without HTTP.",
  ["nextjs", "ssr-prefetch"])

c("NextJS",
  "What is <code>createHydrateClient</code>?",
  "<pre><code>// app/layout.tsx\nimport { HydrateClient, api } from '@/trpc/server';\n\nexport default async function Layout({ children }) {\n  return &lt;HydrateClient&gt;{children}&lt;/HydrateClient&gt;;\n}</code></pre><br><b>HydrateClient</b> wraps children in a React Query <code>HydrationBoundary</code>. Server-fetched data (via <code>api.*</code>) is dehydrated into the client cache, so <code>useSuspenseQuery()</code> on the client reads from cache instantly — no flash of loading.",
  ["nextjs", "createHydrateClient"])

c("NextJS",
  "How to call a tRPC procedure from a server component?",
  "<pre><code>// trpc/server.ts\nimport { headers } from 'next/headers';\nimport { cache } from 'react';\nimport { createTRPCContext } from '@/server/api/trpc';\nimport { appRouter } from '@/server/api/root';\nimport { createCallerFactory } from '@trpc/server';\n\nconst createContext = cache(async () => {\n  const heads = new Headers(await headers());\n  heads.set('x-trpc-source', 'rsc');\n  return createTRPCContext({ headers: heads });\n});\n\nconst createCaller = createCallerFactory(appRouter);\nexport const api = createCaller(createContext);</code></pre><br>Use <code>api.user.list()</code> directly in server components. React's <code>cache()</code> ensures one context per request.",
  ["nextjs", "server-component-call"])

c("NextJS",
  "How to set up tRPC for the Next.js <b>Pages Router</b> (using <code>createTRPCNext</code>)?",
  "<pre><code>// utils/trpc.ts\nimport { createTRPCNext } from '@trpc/next';\nimport { httpBatchLink } from '@trpc/client';\nimport type { AppRouter } from '@/server/routers/_app';\n\nexport const trpc = createTRPCNext&lt;AppRouter&gt;({\n  config() {\n    return {\n      links: [httpBatchLink({ url: '/api/trpc' })],\n    };\n  },\n  ssr: true,\n});\n\n// Wrap _app.tsx with trpc.withTRPC(MyApp);</code></pre><br>For Pages Router, <code>createTRPCNext</code> is the official pattern (though <code>@trpc/next</code> is being replaced by <code>@trpc/react-query</code>).",
  ["nextjs", "pages-router"])

c("NextJS",
  "What is <code>createTRPCNext</code> (Pages Router vs App Router)?",
  "<code>createTRPCNext</code> is for the <b>Pages Router</b>. It creates an HOC (<code>withTRPC</code>) that wraps <code>_app.tsx</code>.<br><br>For the <b>App Router</b>, use <code>createTRPCReact</code> + <code>TRPCReactProvider</code> instead — no HOC needed.<br><br>tRPC v11 encourages moving to <code>@trpc/react-query</code> for both routers, phasing out <code>createTRPCNext</code> long-term.",
  ["nextjs", "createTRPCNext"])

c("NextJS",
  "How to access request headers in a tRPC procedure (Next.js app router)?",
  "<pre><code>import { headers } from 'next/headers';\n\nconst createContext = async () => {\n  const heads = await headers();\n  return { ip: heads.get('x-forwarded-for'), userAgent: heads.get('user-agent') };\n};</code></pre><br>Since <code>headers()</code> is async in Next.js 14+, your <code>createContext</code> must be async.",
  ["nextjs", "headers"])

c("NextJS",
  "How to use tRPC with React Query's <code>useQuery</code> (non-suspense)?",
  "<pre><code>const { data, isLoading, error } = trpc.user.list.useQuery();\n\nif (isLoading) return &lt;Skeleton /&gt;;\nif (error) return &lt;Error message={error.message} /&gt;;\nreturn data.map(u => &lt;UserCard key={u.id} user={u} /&gt;);</code></pre><br><code>useQuery</code> returns loading/error states that you handle manually — good for custom loading UIs. <code>useSuspenseQuery</code> throws to a Suspense boundary instead.",
  ["nextjs", "useQuery"])

c("NextJS",
  "How to handle tRPC errors in the UI?",
  "<pre><code>const createPost = trpc.post.create.useMutation({\n  onError: (err) => {\n    if (err.data?.code === 'CONFLICT') {\n      toast.error('A post with this title already exists');\n    } else if (err.data?.code === 'UNAUTHORIZED') {\n      signIn();\n    } else {\n      toast.error('Something went wrong');\n    }\n  },\n});</code></pre><br>Check <code>err.data.code</code> (the TRPCError code) to handle specific error types. <code>err.message</code> is the human-readable message. Use <code>err.shape</code> for the full error shape from the error formatter.",
  ["nextjs", "error-handling-ui"])

c("NextJS",
  "How to conditionally enable/disable a tRPC query?",
  "<pre><code>const [userId, setUserId] = useState&lt;string | null&gt;(null);\n\nconst { data: user } = trpc.user.byId.useQuery(\n  { id: userId! },\n  { enabled: !!userId } // only fetch when userId is truthy\n);</code></pre><br>Pass <code>{ enabled: boolean }</code> as the second argument. The query doesn't fire until <code>enabled</code> is true. Useful for queries that depend on user input or another query's result.",
  ["nextjs", "enabled-query"])

# ==================== 06-Advanced-Patterns ====================

c("Patterns",
  "How to structure a monorepo with tRPC (shared types package)?",
  "Typical structure:<br><pre><code>packages/\n  api/              # tRPC routers, context, server logic\n    src/routers/\n  shared/           # Zod schemas, shared types\n    src/schemas/\n  web/              # Next.js app, imports type from api\n    trpc/client.ts</code></pre><br>The <b>shared package</b> contains Zod schemas re-used by both server and client. The <b>web</b> package imports only the <code>AppRouter</code> type from <b>api</b> — not the runtime code.",
  ["patterns", "monorepo"])

c("Patterns",
  "How to split routers by domain?",
  "<pre><code>// routers/admin/user.ts — admin user management\nexport const adminUserRouter = router({\n  ban: adminProcedure.input(z.object({ userId: z.string() })).mutation(...),\n});\n\n// routers/public/post.ts — public post routes\nexport const postRouter = router({\n  list: publicProcedure.query(...),\n  bySlug: publicProcedure.input(...).query(...),\n});\n\n// routers/_app.ts — root\nconst appRouter = router({\n  admin: router({ user: adminUserRouter }),\n  post: postRouter,\n});</code></pre><br>One file per domain. Nest related routers under a namespace (e.g., <code>admin.user</code>).",
  ["patterns", "split-routers"])

c("Patterns",
  "What is <code>createCaller()</code> and when do you use it?",
  "It creates a <b>server-side tRPC caller</b> — bypasses HTTP to call tRPC procedures directly with the same context and types:<br><pre><code>const createCaller = createCallerFactory(appRouter);\nconst caller = createCaller(ctx);\nawait caller.user.byId({ id: '123' });\nawait caller.post.create({ title: 'Hello', content: 'World' });</code></pre><br>Use cases: server actions, background jobs, webhook handlers, testing, calling one router from another.",
  ["patterns", "createCaller"])

c("Patterns",
  "How to do optimistic updates with tRPC?",
  "<pre><code>const utils = trpc.useUtils();\n\nconst updatePost = trpc.post.update.useMutation({\n  onMutate: async (newPost) => {\n    await utils.post.byId.cancel();\n    const previous = utils.post.byId.getData({ id: newPost.id });\n    utils.post.byId.setData({ id: newPost.id }, (old) => ({ ...old, ...newPost }));\n    return { previous };\n  },\n  onError: (err, newPost, context) => {\n    utils.post.byId.setData({ id: newPost.id }, context!.previous);\n  },\n  onSettled: () => {\n    utils.post.byId.invalidate({ id: newPost.id });\n  },\n});</code></pre><br>Update the cache immediately, then reconcile with the server. Rollback on error.",
  ["patterns", "optimistic-updates"])

c("Patterns",
  "How to implement cursor-based pagination with tRPC?",
  "<pre><code>const postRouter = router({\n  feed: publicProcedure\n    .input(z.object({ cursor: z.string().optional(), limit: z.number().min(1).max(50).default(10) }))\n    .query(async ({ input, ctx }) => {\n      const posts = await ctx.db.post.findMany({\n        take: input.limit + 1,\n        cursor: input.cursor ? { id: input.cursor } : undefined,\n        orderBy: { createdAt: 'desc' },\n      });\n      let nextCursor: string | undefined;\n      if (posts.length > input.limit) {\n        const next = posts.pop()!;\n        nextCursor = next.id;\n      }\n      return { posts, nextCursor };\n    }),\n});</code></pre><br>Use <code>useInfiniteQuery</code> on the client to fetch more pages.",
  ["patterns", "cursor-pagination"])

c("Patterns",
  "How to use infinite queries with tRPC on the client?",
  "<pre><code>const [allPosts, { fetchNextPage, hasNextPage }] =\n  trpc.post.feed.useSuspenseInfiniteQuery(\n    { limit: 10 },\n    { getNextPageParam: (lastPage) => lastPage.nextCursor }\n  );\n\n// allPosts.pages is an array of { posts: Post[], nextCursor: string | undefined }\nconst posts = allPosts.pages.flatMap(p => p.posts);</code></pre><br><code>useSuspenseInfiniteQuery</code> handles the cursor automatically. Call <code>fetchNextPage()</code> in a click handler or intersection observer.",
  ["patterns", "infinite-query"])

c("Patterns",
  "How to implement WebSocket subscriptions in tRPC?",
  "<pre><code>// server\nimport { observable } from '@trpc/server/observable';\nimport { EventEmitter } from 'events';\nconst ee = new EventEmitter();\n\nconst subRouter = router({\n  onMessage: publicProcedure.subscription(() =>\n    observable&lt;Message&gt;((emit) => {\n      const handler = (msg: Message) => emit.next(msg);\n      ee.on('message', handler);\n      return () => ee.off('message', handler);\n    })\n  ),\n});\n\n// client — wsLink sends subscriptions over WebSocket\nconst subscription = trpc.sub.onMessage.useSubscription(undefined, {\n  onData: (msg) => console.log('New message:', msg),\n});</code></pre>",
  ["patterns", "websocket-subscription"])

c("Patterns",
  "How to implement SSE (Server-Sent Events) subscriptions in tRPC?",
  "<pre><code>// Use httpSubscriptionLink for SSE (tRPC v11+)\nimport { httpSubscriptionLink } from '@trpc/client';\n\nlinks: [\n  splitLink({\n    condition: (op) => op.type === 'subscription',\n    true: httpSubscriptionLink({ url: '/api/trpc' }),\n    false: httpBatchLink({ url: '/api/trpc' }),\n  }),\n]</code></pre><br><b>httpSubscriptionLink</b> uses Server-Sent Events (SSE) over HTTP instead of WebSocket. Works with serverless platforms (Vercel, Cloudflare Workers) that don't support persistent WebSocket connections.",
  ["patterns", "sse-subscription"])

c("Patterns",
  "How to handle file uploads in tRPC?",
  "tRPC uses JSON — files can't be sent natively. Options:<br><pre><code>// Option 1: Pre-signed URL pattern\nconst avatarRouter = router({\n  getUploadUrl: protectedProcedure.mutation(async ({ ctx }) => {\n    const url = await s3.getSignedUrl('putObject', { Key: `avatars/${ctx.user.id}` });\n    return { url, key: `avatars/${ctx.user.id}` };\n  }),\n});\n\n// Option 2: Use Next.js Route Handler for the upload, tRPC for metadata\n// Option 3: Base64 encode (small files only)</code></pre><br>The pre-signed URL pattern is the most common and scalable approach.",
  ["patterns", "file-upload"])

c("Patterns",
  "How to create a custom tRPC link?",
  "<pre><code>import { TRPCLink } from '@trpc/client';\nimport { observable } from '@trpc/server/observable';\n\nconst retryLink: TRPCLink&lt;AppRouter&gt; = () => {\n  return ({ next, op }) => {\n    return observable((observer) => {\n      const attempt = (retriesLeft: number) => {\n        next(op).subscribe({\n          next: observer.next,\n          error: (err) => {\n            if (retriesLeft > 0) return attempt(retriesLeft - 1);\n            observer.error(err);\n          },\n          complete: observer.complete,\n        });\n      };\n      attempt(3);\n    });\n  };\n};</code></pre><br>Links form a chain — each link can transform, retry, or short-circuit operations.",
  ["patterns", "custom-link"])

c("Patterns",
  "How to create a custom error formatter?",
  "<pre><code>import { initTRPC } from '@trpc/server';\nimport { ZodError } from 'zod';\n\nconst t = initTRPC.create({\n  errorFormatter({ shape, error }) {\n    return {\n      ...shape,\n      data: {\n        ...shape.data,\n        zodError: error.cause instanceof ZodError ? error.cause.flatten() : null,\n        timestamp: new Date().toISOString(),\n      },\n    };\n  },\n});</code></pre><br>The error formatter runs on every error before it's sent to the client. Use it to add metadata, sanitize sensitive info, or transform Zod errors.",
  ["patterns", "error-formatter"])

c("Patterns",
  "How to configure a custom data transformer (superjson for Dates/Maps/Sets)?",
  "<pre><code>import superjson from 'superjson';\n\n// Server:\nconst t = initTRPC.create({ transformer: superjson });\n\n// Client:\nconst client = trpc.createClient({\n  links: [httpBatchLink({ url: '/api/trpc', transformer: superjson })],\n});</code></pre><br>Both ends must use the same transformer. <b>superjson</b> handles: Date, Map, Set, BigInt, RegExp, undefined, Infinity, NaN — all the types JSON.stringify loses.",
  ["patterns", "superjson"])

c("Patterns",
  "How to use tRPC with React Native?",
  "<pre><code>// trpc.ts (React Native)\nimport { createTRPCReact } from '@trpc/react-query';\nimport { httpBatchLink } from '@trpc/client';\nimport type { AppRouter } from '@/server/api/root';\n\nexport const trpc = createTRPCReact&lt;AppRouter&gt;();\n\nexport const trpcClient = trpc.createClient({\n  links: [httpBatchLink({ url: 'https://api.example.com/api/trpc' })],\n});\n\n// Wrap app with:\n// &lt;trpc.Provider client={trpcClient} queryClient={queryClient}&gt;...&lt;/trpc.Provider&gt;</code></pre><br>Works identically to web — same hooks, same types. Just point <code>url</code> to your deployed API.",
  ["patterns", "react-native"])

c("Patterns",
  "How to use tRPC with Express/Fastify standalone (without Next.js)?",
  "<pre><code>// server.ts (Express)\nimport { createExpressMiddleware } from '@trpc/server/adapters/express';\nimport express from 'express';\n\nconst app = express();\napp.use(\n  '/trpc',\n  createExpressMiddleware({\n    router: appRouter,\n    createContext: ({ req }) => ({ db: prisma, user: req.user }),\n  })\n);\napp.listen(3001);\n\n// Or Fastify:\nimport { fastifyTRPCPlugin } from '@trpc/server/adapters/fastify';\nfastify.register(fastifyTRPCPlugin, { prefix: '/trpc', trpcOptions: { router: appRouter } });</code></pre><br>tRPC is server-agnostic. The <code>adapters/*</code> packages provide bindings for each server.",
  ["patterns", "standalone"])

c("Patterns",
  "How to integrate tRPC with Prisma?",
  "<pre><code>// context.ts\nimport { PrismaClient } from '@prisma/client';\n\nexport const db = new PrismaClient();\n\nconst createContext = () => ({ db });\n\nexport type Context = Awaited&lt;ReturnType&lt;typeof createContext&gt;&gt;;\n\n// In procedures:\npublicProcedure.query(async ({ ctx }) => {\n  return ctx.db.user.findMany({ include: { posts: true } });\n});</code></pre><br>Put Prisma in context. Singleton instance. All procedures access it via <code>ctx.db</code>. Types flow from Prisma through tRPC to the client automatically.",
  ["patterns", "prisma"])

c("Patterns",
  "How to integrate tRPC with Drizzle ORM?",
  "<pre><code>// db.ts\nimport { drizzle } from 'drizzle-orm/node-postgres';\nimport { Pool } from 'pg';\n\nconst pool = new Pool({ connectionString: process.env.DATABASE_URL });\nexport const db = drizzle(pool, { schema });\n\n// context.ts\nconst createContext = () => ({ db });\n\n// In procedures:\npublicProcedure.query(async ({ ctx }) => {\n  return ctx.db.select().from(users).where(eq(users.id, input.id));\n});</code></pre><br>Drizzle's inferred types propagate through tRPC. Drizzle is lighter-weight than Prisma with better SQL control.",
  ["patterns", "drizzle"])

c("Patterns",
  "How to do dependent queries (one query depends on another's result)?",
  "<pre><code>// Query 1: Get current user\nconst { data: user } = trpc.user.me.useQuery();\n\n// Query 2: Get user's posts (only after userId is known)\nconst { data: posts } = trpc.post.byUser.useQuery(\n  { userId: user?.id ?? '' },\n  { enabled: !!user?.id } // waits for user query to resolve\n);</code></pre><br>Use the <code>enabled</code> option to chain queries. React Query won't fire the second query until the first resolves. This is the standard pattern for data dependencies.",
  ["patterns", "dependent-queries"])

c("Patterns",
  "How to implement selective cache invalidation with <code>useUtils</code>?",
  "<pre><code>const utils = trpc.useUtils();\n\nconst updatePost = trpc.post.update.useMutation({\n  onSuccess: (updatedPost) => {\n    // Invalidate the list — causes refetch\n    utils.post.list.invalidate();\n\n    // Update specific cache entry without refetch (optimistic-ish)\n    utils.post.byId.setData({ id: updatedPost.id }, updatedPost);\n  },\n});\n\n// Also: cancel outgoing queries before mutation\nconst deletePost = trpc.post.delete.useMutation({\n  onMutate: async ({ id }) => {\n    await utils.post.list.cancel(); // cancel in-flight list queries\n  },\n});</code></pre><br>Use <code>.cancel()</code> before mutation, <code>.invalidate()</code> after success, <code>.setData()</code> for zero-refetch updates.",
  ["patterns", "cache-invalidation"])

c("Patterns",
  "How to use tRPC with tRPC's <code>inferRouterInputs</code>/<code>inferRouterOutputs</code> helper types?",
  "<pre><code>import type { inferRouterInputs, inferRouterOutputs } from '@trpc/server';\nimport type { AppRouter } from '@/server/api/root';\n\ntype RouterInput = inferRouterInputs&lt;AppRouter&gt;;\ntype RouterOutput = inferRouterOutputs&lt;AppRouter&gt;;\n\n// Use in typed server actions:\nexport async function createPost(input: RouterInput['post']['create']) {\n  return api.post.create(input);\n}</code></pre><br>These utility types extract the exact input/output shape of any procedure in the router. Ship them to client components for type-safe form props without importing the full router.",
  ["patterns", "infer-types"])

# ==================== 07-Gotchas ====================

c("Gotchas",
  "What happens when server and client use different Zod versions?",
  "If server and client have different <b>Zod major versions</b>, TypeScript types may resolve differently — you get <code>never</code> or <code>any</code> in place of expected types. This breaks end-to-end typesafety silently.<br><br><b>Fix:</b> Hoist Zod to the workspace root in a monorepo, or use <code>pnpm.overrides</code> / <code>resolutions</code> to enforce a single version.",
  ["gotchas", "zod-version-mismatch"])

c("Gotchas",
  "Input validation strips extra properties by default — what does this mean?",
  "Zod's <code>.object()</code> strips unknown keys by default (<code>.strip()</code> mode):<br><pre><code>const schema = z.object({ name: z.string() });\nschema.parse({ name: 'Alice', role: 'admin' }); // { name: 'Alice' } — 'role' is stripped</code></pre><br>If you expect extra fields to be passed through, use <code>.passthrough()</code>:<br><pre><code>z.object({ name: z.string() }).passthrough();</code></pre>",
  ["gotchas", "input-stripping"])

c("Gotchas",
  "Context not properly typed — how to ensure correct context inference?",
  "Always export the <b>context type</b> from the inferred type:<br><pre><code>const createContext = async () => ({ db: prisma, user: null as User | null });\n\nexport type Context = Awaited&lt;ReturnType&lt;typeof createContext&gt;&gt;;</code></pre><br>Pass <code>Context</code> as a generic to <code>initTRPC</code>:<br><pre><code>const t = initTRPC.context&lt;Context&gt;().create();</code></pre><br>Without the generic, tRPC infers <code>ctx</code> as <code>any</code> in procedures and middleware.",
  ["gotchas", "context-typing"])

c("Gotchas",
  "Circular references between routers — what's the problem and fix?",
  "Router A imports Router B, Router B imports Router A → circular dependency → <code>undefined</code> at runtime or build errors.<br><br><b>Fix:</b> Use <b>lazy loading</b> or extract shared logic into a separate file. Avoid importing routers into each other. Use <code>createCaller()</code> for cross-router communication instead of direct import:<br><pre><code>// Instead of importing postRouter, use the caller\nconst caller = createCaller(ctx);\nawait caller.post.unpublishByUser({ userId });</code></pre>",
  ["gotchas", "circular-routers"])

c("Gotchas",
  "Batching causing unintended request coupling — what's the issue?",
  "With <code>httpBatchLink</code>, all queries in the same microtask share one HTTP request. If one query takes 5 seconds (slow DB), all other queries in the batch wait for it — <b>head-of-line blocking</b>.<br><br><b>Fix:</b> Use <code>httpLink</code> for expensive queries; <code>httpBatchLink</code> only for fast ones. Or use <code>splitLink</code> to route by procedure name.<br><br>tRPC v11+ sends <b>streamed responses</b> for batches — each query in the batch is streamed independently.",
  ["gotchas", "batching-coupling"])

c("Gotchas",
  "Subscription memory leaks — what causes them and how to prevent?",
  "Every subscriber callback added to an EventEmitter must be removed on unsubscribe. If the cleanup function (return value of <code>observable</code>) doesn't remove the listener, memory leaks accumulate.<br><br><pre><code>// ❌ Leaky — never removed\nobservable((emit) => {\n  ee.on('event', handler);\n  return () => {}; // empty cleanup\n});\n\n// ✅ Correct — removes listener on unsubscribe\nobservable((emit) => {\n  ee.on('event', handler);\n  return () => ee.off('event', handler);\n});</code></pre>",
  ["gotchas", "subscription-leaks"])

c("Gotchas",
  "superjson not configured causing Date serialization issues — what happens?",
  "Without superjson, <code>Date</code> objects serialize as ISO strings (<code>'2024-01-01T00:00:00.000Z'</code>) over JSON. On the client, they're strings, not <code>Date</code> objects.<br><br>This means:<br>• <code>post.createdAt.getFullYear()</code> crashes (not a Date)<br>• TypeScript still thinks it's a Date (type mismatch)<br>• You must manually convert <code>new Date(post.createdAt)</code> everywhere<br><br><b>Fix:</b> Configure superjson on both server and client. Then <code>Date</code> objects stay as <code>Date</code> across the wire.",
  ["gotchas", "superjson-gotcha"])

c("Gotchas",
  "TRPCError codes not matching HTTP semantics — what's the mismatch?",
  "tRPC overrides HTTP status codes with 200 for everything (by default with <code>httpBatchLink</code>). Errors are communicated in the <b>response body</b>, not via HTTP status.<br><br>This means:<br>• HTTP proxies/caches can't differentiate errors<br>• Monitoring tools looking at status codes miss errors<br>• <code>httpLink</code> sends proper HTTP status codes per error<br><br>Use the <code>errorFormatter</code> to add status codes if you need them, or use <code>httpLink</code> for per-request HTTP semantics.",
  ["gotchas", "error-http-semantics"])

c("Gotchas",
  "Middleware ordering effects — why does order matter?",
  "Middlewares execute in the order they're added. If auth middleware comes after rate-limiting, an attacker can hammer the endpoint even if unauthenticated — the rate limit check happens after the auth check.<br><br><pre><code>// ❌ Wrong order — auth throws first, rate limit never reaches unauthenticated users\n.procedure.use(auth).use(rateLimit)\n\n// ✅ Correct — rate limit first, then auth\n.procedure.use(rateLimit).use(auth)</code></pre><br>Put <b>non-discriminating middleware</b> (logging, rate-limiting) first. Put <b>discriminating middleware</b> (auth, role checks) after.",
  ["gotchas", "middleware-order"])

c("Gotchas",
  "React Query cache stale data — how does it affect tRPC?",
  "React Query's <code>staleTime</code> defaults to 0, meaning data is considered stale immediately. When you navigate away and back, queries refetch. If a mutation and refetch race, you may briefly see stale data.<br><br><b>Fix:</b> Set appropriate <code>staleTime</code>:<br><pre><code>new QueryClient({\n  defaultOptions: { queries: { staleTime: 30 * 1000 } }, // 30 seconds\n})</code></pre><br>Or use <code>useUtils().invalidate()</code> + <code>refetch()</code> explicitly after mutations.",
  ["gotchas", "stale-data"])

c("Gotchas",
  "Vercel serverless cold starts with tRPC — what's the problem?",
  "Vercel serverless functions (and similar platforms) have <b>cold starts</b>: first request after idle spins up a new container. tRPC context creation (DB connections, auth) adds latency to that first request.<br><br><b>Mitigations:</b><br>• Use edge functions where possible (faster cold starts)<br>• Keep context creation fast — don't do heavy work<br>• Use connection pooling (PgBouncer, PlanetScale) instead of per-request connections<br>• Prefer <code>@upstash/redis</code> over self-hosted Redis for serverless",
  ["gotchas", "cold-starts"])

c("Gotchas",
  "Why do my tRPC procedures show <code>any</code> types in the client?",
  "Common causes:<br>1. <b>Missing context generic</b> — use <code>initTRPC.context&lt;Context&gt;().create()</code><br>2. <b>Circular imports</b> — AppRouter type resolves to <code>any</code><br>3. <b>Zod version mismatch</b> — server and client resolve different types<br>4. <b>Not exporting AppRouter type</b> — <code>export type AppRouter = typeof appRouter</code><br>5. <b>Client importing value, not type</b> — use <code>import type { AppRouter }</code>",
  ["gotchas", "any-types"])

c("Gotchas",
  "tRPC input properties silently dropped — what's happening?",
  "Zod strips unknown properties by default. If client sends <code>{ name: 'Alice', extra: true }</code> and schema only has <code>z.object({ name: z.string() })</code>, <code>extra</code> is silently removed.<br><br>This can hide bugs where the client sends fields the server ignores.<br><br><b>Fix:</b> Use <code>.strict()</code> to reject unknown keys with an error instead of stripping them:<br><pre><code>z.object({ name: z.string() }).strict();</code></pre>",
  ["gotchas", "silent-strip"])

c("Gotchas",
  "Windows vs Linux line endings in tRPC client code import — issue?",
  "Not a tRPC-specific issue, but <code>import type</code> on Windows with CRLF can cause TypeScript to resolve the value module instead of the type — resulting in server code leaking to the client bundle.<br><br><b>Fix:</b> Use <code>.gitattributes</code> with <code>* text=auto</code>. Set editor to LF. Use <code>typescript.preferences.importModuleSpecifier</code> to <code>'non-relative'</code> or <code>'relative'</code> consistently.",
  ["gotchas", "line-endings"])

c("Gotchas",
  "tRPC procedure returning <code>never</code> type — what's wrong?",
  "When a procedure's return type resolves to <code>never</code>, it usually means:<br>1. <b>Context is <code>any</code></b> — forgot <code>initTRPC.context&lt;Context&gt;().create()</code><br>2. <b>Zod version mismatch</b> — server and client have different Zod versions<br>3. <b>Circular import</b> — AppRouter imports itself<br>4. <b>Middleware breaks inference</b> — incorrectly typed middleware<br><br>The fix is usually adding the Context generic to <code>initTRPC</code>.",
  ["gotchas", "never-type"])

c("Gotchas",
  "Mutation not invalidating queries — why doesn't my UI update?",
  "Mutations don't auto-invalidate. You must call <code>utils.*.invalidate()</code> in <code>onSuccess</code>:<br><pre><code>const createPost = trpc.post.create.useMutation({\n  onSuccess: () => {\n    utils.post.list.invalidate(); // mandatory!\n  },\n});</code></pre><br>Alternatively, return the new data from the mutation and use <code>utils.*.setData()</code> to update the cache directly (no refetch).<br><br>⚠️ React Query's <code>refetchOnMount</code> is <code>true</code> by default — but that won't refetch an already-mounted list after a mutation.",
  ["gotchas", "mutation-no-refresh"])

c("Gotchas",
  "Hard-to-debug <code>TRPCClientError</code> with no useful message — what to check?",
  "1. Server threw a <b>non-TRPCError</b> — it becomes <code>INTERNAL_SERVER_ERROR</code> with a generic message<br>2. <b>Network error</b> — server is down, CORS, or wrong URL<br>3. <b>Transformer mismatch</b> — server uses superjson but client doesn't (or vice versa)<br>4. <b>Input serialization fails</b> — sending undefined/Functions/BigInt without custom transformer<br>5. <b>Response parsing errors</b> — server returns non-JSON (e.g., HTML error page from reverse proxy)<br><br>Check DevTools Network tab for the raw HTTP response.",
  ["gotchas", "opaque-errors"])

c("Gotchas",
  "<code>useSuspenseQuery</code> hangs forever — what's wrong?",
  "<code>useSuspenseQuery</code> never resolves if the query never finishes. Common causes:<br>1. <b>Server endpoint missing</b> — 404 returns HTML, tRPC can't parse it<br>2. <b>Missing Suspense boundary</b> — the promise is thrown but nothing catches it<br>3. <b>Infinite retry loop</b> — query fails, retries, fails…<br>4. <b>Context deadlock</b> — <code>createContext</code> has an infinite await<br>5. <b>SSR misconfiguration</b> — hydration expects data that doesn't exist<br><br><b>Fix:</b> Always wrap in <code>&lt;Suspense&gt;</code> with a <b>fallback</b>. Use <code>useQuery</code> (non-suspense) during development to see errors.",
  ["gotchas", "suspense-hang"])

# ==================== 08-Expert ====================

c("Expert",
  "tRPC vs GraphQL vs REST — what's the decision framework?",
  "<b>Use tRPC when:</b> Full-stack TypeScript, tight client-server coupling, internal tools, admin panels, single consumer (your own app).<br><b>Use GraphQL when:</b> Multiple clients need different data shapes, you need a query language, aggregating many data sources, public API with field-level access control.<br><b>Use REST when:</b> Public API consumed by non-TS clients, caching matters (CDNs), simple CRUD, you need tooling like Postman and OpenAPI.",
  ["expert", "decision-framework"])

c("Expert",
  "When does tRPC shine?",
  "tRPC shines when:<br>• <b>Full-stack TypeScript</b> — same language everywhere<br>• <b>Tight client-server coupling</b> — your web app is the only consumer<br>• <b>Internal tools and admin panels</b> — speed > API design<br>• <b>Rapid prototyping</b> — no schema stitching, no code generation<br>• <b>Type-driven development</b> — change a procedure return type, client gets red squiggles instantly<br>• <b>Solo developer or small team</b> — less ceremony than GraphQL",
  ["expert", "when-trpc-shines"])

c("Expert",
  "When should you NOT use tRPC?",
  "Avoid tRPC when:<br>• <b>Public APIs</b> consumed by non-TypeScript clients (mobile apps in Swift/Kotlin, third-party integrations)<br>• <b>Microservices in different languages</b> — tRPC is TypeScript-only<br>• <b>Mobile-first with offline support</b> — REST/GraphQL with Apollo has better caching/offline primitives<br>• <b>You need OpenAPI/Swagger docs</b> — tRPC has no built-in spec generation (plugins exist but are unofficial)<br>• <b>Streaming large binary data</b> — use gRPC or direct S3 pre-signed URLs",
  ["expert", "when-not-trpc"])

c("Expert",
  "tRPC + Prisma vs tRPC + Drizzle — how to choose?",
  "<b>Prisma:</b> Great DX, auto-generated migrations, Prisma Studio. Heavier runtime, own query engine. Better for teams that want a managed ORM experience.<br><br><b>Drizzle:</b> Lighter, SQL-like syntax, no code generation. Better for SQL experts who want full control. Smaller bundle, faster cold starts.<br><br>Both work seamlessly with tRPC. Prisma types are slightly richer (include relations), Drizzle types are closer to raw SQL. Choose Prisma for speed of development, Drizzle for performance and control.",
  ["expert", "prisma-vs-drizzle"])

c("Expert",
  "How to use tRPC without Next.js (standalone Node.js server)?",
  "<pre><code>// server.ts\nimport { createHTTPServer } from '@trpc/server/adapters/standalone';\nimport { appRouter } from './router';\n\nconst server = createHTTPServer({\n  router: appRouter,\n  createContext: () => ({ db: prisma }),\n});\nserver.listen(3001);</code></pre><br>tRPC includes a standalone HTTP server adapter. Or use Express/Fastify adapters. Works with any Node.js deployment — Railway, Fly.io, bare VPS, Docker.",
  ["expert", "standalone-node"])

c("Expert",
  "How does tRPC work with React Server Components?",
  "In Server Components, you don't use hooks. Instead, use the <b>server-side caller</b>:<br><pre><code>// app/page.tsx (Server Component)\nimport { api } from '@/trpc/server';\n\nexport default async function Page() {\n  const posts = await api.post.latest();\n  return &lt;PostList posts={posts} /&gt;;\n}</code></pre><br>Client Components (with <code>'use client'</code>) use hooks as normal. RSCs get data at render time, not at request time — zero client-side JavaScript for data fetching.",
  ["expert", "server-components"])

c("Expert",
  "Zod vs Valibot for tRPC input validation — how to choose?",
  "<b>Zod:</b> Mature, huge ecosystem, works everywhere. Static methods (<code>z.string()</code>). Can be tree-shaken.<br><br><b>Valibot:</b> Modular design — <code>import { string, object } from 'valibot'</code>. Better tree-shaking. Smaller bundle (1.5KB vs 12KB). Pipe-based transformations.<br><br>For tRPC: both work. Zod has better tRPC integration historically. Valibot is gaining support. Choose Zod for stability and documentation; Valibot for bundle size in edge/RN environments.",
  ["expert", "zod-vs-valibot"])

c("Expert",
  "How to build a custom retry link?",
  "<pre><code>import { TRPCLink } from '@trpc/client';\nimport { observable } from '@trpc/server/observable';\n\nconst retryLink = (opts: { maxRetries: number }): TRPCLink&lt;AppRouter&gt; => () => {\n  return ({ next, op }) =>\n    observable((observer) => {\n      let retriesLeft = opts.maxRetries;\n      const attempt = () => {\n        next(op).subscribe({\n          next: observer.next,\n          error: (err) => {\n            if (retriesLeft > 0 && isRetryable(err)) {\n              retriesLeft--;\n              setTimeout(attempt, 1000 * (opts.maxRetries - retriesLeft));\n              return;\n            }\n            observer.error(err);\n          },\n          complete: observer.complete,\n        });\n      };\n      attempt();\n    });\n};</code></pre><br>Wrap network-sensitive operations. Only retry transient errors (network failures, 408, 429, 5xx), not validation errors.",
  ["expert", "custom-retry-link"])

c("Expert",
  "How to build an auth-refresh link?",
  "<pre><code>const authRefreshLink: TRPCLink&lt;AppRouter&gt; = () => {\n  return ({ next, op }) =>\n    observable((observer) => {\n      next(op).subscribe({\n        next: observer.next,\n        error: async (err) => {\n          if (err.data?.code === 'UNAUTHORIZED') {\n            try {\n              await refreshToken(); // get new access token\n              next(op).subscribe(observer); // retry with new token\n            } catch {\n              observer.error(err); // refresh failed, propagate error\n            }\n          } else {\n            observer.error(err);\n          }\n        },\n        complete: observer.complete,\n      });\n    });\n};</code></pre><br>Intercepts UNAUTHORIZED errors, refreshes the token, and retries the original request transparently.",
  ["expert", "auth-refresh-link"])

c("Expert",
  "How to build an offline queue link?",
  "<pre><code>// High-level approach — offline queue as a link\nconst offlineLink: TRPCLink&lt;AppRouter&gt; = () => {\n  const queue: Operation[] = [];\n  return ({ next, op }) =>\n    observable((observer) => {\n      if (!navigator.onLine) {\n        queue.push(op); // store for later\n        observer.complete(); // don't error — the app thinks it succeeded\n        return;\n      }\n      next(op).subscribe(observer);\n    });\n};\n\n// On reconnect, replay queue:\nwindow.addEventListener('online', () => {\n  queue.forEach(op => trpcClient.request(op));\n  queue.length = 0;\n});</code></pre><br>For mutations only — queries should NOT be queued. Combine with IndexedDB for persistence across page reloads.",
  ["expert", "offline-queue"])

c("Expert",
  "How to create a custom data transformer (beyond superjson)?",
  "<pre><code>import { DataTransformer } from '@trpc/server';\n\nconst decimalTransformer: DataTransformer = {\n  serialize: (obj) => traverseAndTransform(obj, (val) => {\n    if (val instanceof Decimal) return { __type: 'Decimal', value: val.toString() };\n    return val;\n  }),\n  deserialize: (obj) => traverseAndTransform(obj, (val) => {\n    if (val?.__type === 'Decimal') return new Decimal(val.value);\n    return val;\n  }),\n};\n\n// For Decimal.js / Prisma Decimal types:\nconst t = initTRPC.create({ transformer: decimalTransformer });</code></pre><br>Custom transformers let you serialize any type — Decimal, BigInt, custom classes. Combine with superjson for a superset.",
  ["expert", "custom-transformer"])

c("Expert",
  "How to build a tRPC plugin/extension?",
  "tRPC has no official plugin system, but you can build re-usable packages that export middleware, procedures, and routers:<br><pre><code>// trpc-plugin-audit-log/index.ts\nexport const createAuditLogPlugin = (config: { log: (event: AuditEvent) => void }) => {\n  const auditMiddleware = t.middleware(async ({ ctx, path, type, next }) => {\n    const result = await next();\n    config.log({ path, type, ok: result.ok, user: ctx.user?.id });\n    return result;\n  });\n  return { auditMiddleware, withAudit: t.procedure.use(auditMiddleware) };\n};\n\n// Usage:\nconst audit = createAuditLogPlugin({ log: console.log });\nconst auditedProcedure = audit.withAudit;</code></pre><br>Package as npm module. Export middleware, procedures, and context creators.",
  ["expert", "plugin-extension"])

c("Expert",
  "How to use tRPC for internal service-to-service communication?",
  "Services communicate via <b>server-side callers</b>, not HTTP:<br><pre><code>// service-a calls service-b's tRPC procedures\nimport { createCallerFactory } from '@trpc/server';\nimport { serviceBRouter } from '@service-b/api';\n\nconst createCaller = createCallerFactory(serviceBRouter);\nconst caller = createCaller({ db: sharedDb, serviceAuth: true });\n\n// Now call service B's procedures directly\nawait caller.inventory.checkStock({ productId: '123' });</code></pre><br>This gives you <b>type-safe RPC between services</b> without HTTP overhead. Both services must be in the same TypeScript codebase (monorepo) or share types via a package.",
  ["expert", "service-to-service"])

c("Expert",
  "Can you build a tRPC client in another language?",
  "In theory, yes — tRPC uses JSON over HTTP with a predictable protocol. But it's <b>not officially supported</b>. You'd need to:<br>1. Replicate the request format (operation path, input serialization)<br>2. Handle batching<br>3. Implement the same transformer logic<br><br>For non-TS clients, consider <b>generating OpenAPI from tRPC</b> using <code>trpc-openapi</code>, then use standard REST clients.<br><br>Or: wrap tRPC in a REST gateway for non-TS consumers.",
  ["expert", "non-ts-client"])

c("Expert",
  "How to generate OpenAPI spec from tRPC routers?",
  "<pre><code>import { generateOpenApiDocument } from 'trpc-openapi';\nimport { openApiRouter } from './router';\n\nconst openApiDoc = generateOpenApiDocument(openApiRouter, {\n  title: 'My API',\n  version: '1.0.0',\n  baseUrl: 'https://api.example.com',\n});</code></pre><br>Use <b>trpc-openapi</b> (community package). Replaces the standard tRPC HTTP handler with one that also serves OpenAPI. Procedures are annotated with <code>.meta({ openapi: { method: 'GET', path: '/users' } })</code>. Enables Swagger UI and code generation for non-TS clients.",
  ["expert", "openapi"])

c("Expert",
  "How to use tRPC with Electron?",
  "In Electron, the renderer acts as the 'client' and the main process as the 'server'. Use IPC instead of HTTP:<br><pre><code>// main process (server)\nimport { ipcMain } from 'electron';\nipcMain.handle('trpc', (event, payload) => {\n  // Pass to tRPC handler, return result\n});\n\n// renderer (client) — use a custom Electron link\nconst electronLink: TRPCLink&lt;AppRouter&gt; = () => {\n  return ({ next, op }) => observable((observer) => {\n    ipcRenderer.invoke('trpc', op).then(result => {\n      observer.next(result);\n      observer.complete();\n    }).catch(observer.error);\n  });\n};</code></pre><br>No HTTP server needed — tRPC runs over Electron's IPC. All types flow through.",
  ["expert", "electron-trpc"])

c("Expert",
  "How to think about tRPC architecture at scale?",
  "<b>Start:</b> Single appRouter, one file. Simple.<br><b>Growing:</b> Split by domain (user, post, admin). Each in its own file. Merge into root.<br><b>Scaling:</b> Monorepo with shared types package. Multiple tRPC services (user-service, content-service) each with their own AppRouter. Backend-for-frontend (BFF) pattern: a Next.js app that calls multiple tRPC backends via <code>createCaller</code>.<br><br><b>Key principle:</b> tRPC scales vertically (within a TypeScript monorepo), not horizontally (across languages). If you need polyglot services, put a tRPC-to-REST gateway or use gRPC.",
  ["expert", "architecture-at-scale"])

c("Expert",
  "How to test tRPC procedures?",
  "<pre><code>import { createCallerFactory } from '@trpc/server';\nimport { appRouter } from '@/server/api/root';\n\nconst createCaller = createCallerFactory(appRouter);\n\ntest('createUser returns a new user', async () => {\n  const caller = createCaller({ db: testDb, user: null });\n  const result = await caller.user.create({ name: 'Test', email: 'test@test.com' });\n  expect(result.name).toBe('Test');\n});\n\ntest('createUser throws UNAUTHORIZED without session', async () => {\n  const caller = createCaller({ db: testDb, session: null });\n  await expect(caller.user.create({ name: 'X' })).rejects.toThrow('UNAUTHORIZED');\n});</code></pre><br><code>createCaller</code> is the secret to testable tRPC: direct function calls, no HTTP, inject any context. Use Vitest or Jest.",
  ["expert", "testing"])

c("Expert",
  "How to handle tRPC with tRPC's own <code>caller</code> for server actions?",
  "<pre><code>// actions/user.ts (Next.js Server Action)\n'use server';\nimport { caller } from '@/server/api/caller';\n\nexport async function createUser(data: { name: string; email: string }) {\n  'use server';\n  return caller.user.create(data);\n}\n\n// components/UserForm.tsx (Client Component)\nimport { createUser } from '@/actions/user';\n\nfunction handleSubmit(data: { name: string; email: string }) {\n  createUser(data); // calls server action → calls tRPC caller → DB\n}</code></pre><br><b>Server Actions + tRPC caller</b> gives you progressive enhancement: the form works without JS, but becomes instant with JS.",
  ["expert", "server-actions"])

c("Expert",
  "How to think about tRPC in a t3 stack?",
  "The t3 stack (Next.js + tRPC + Prisma/Drizzle + NextAuth + Tailwind) is the canonical tRPC use case. tRPC is the <b>API layer between the frontend and the database</b>. It replaces REST endpoints and GraphQL schemas with plain TypeScript functions.<br><br><pre><code>// Typical t3 procedure:\nprotectedProcedure\n  .input(z.object({ title: z.string().min(1) }))\n  .mutation(({ ctx, input }) =>\n    ctx.db.post.create({\n      data: { title: input.title, authorId: ctx.session.user.id },\n    })\n  );</code></pre><br>Input comes from form → Zod validates → tRPC passes to Prisma/Drizzle → result types flow back to the client. Four layers of type safety in one chain.",
  ["expert", "t3-stack"])

c("Expert",
  "What is the tRPC WebSocket subscription lifecycle?",
  "1. Client connects via <code>wsLink</code><br>2. tRPC establishes WebSocket connection<br>3. Client calls <code>.useSubscription()</code> — sends <code>subscription</code> message<br>4. Server creates an Observable, starts emitting events<br>5. Server sends <code>data</code> frames to client<br>6. Client's <code>onData</code> callback fires with typed data<br>7. On unmount / <code>subscription.unsubscribe()</code>: client sends <code>stop</code> message<br>8. Server calls the Observable's cleanup function<br>9. WebSocket stays open for other subscriptions<br><br>The connection is <b>multiplexed</b> — many subscriptions share one WS connection.",
  ["expert", "subscription-lifecycle"])

c("Expert",
  "How does tRPC handle type inference with conditional types in the router?",
  "tRPC uses <b>deep recursive TypeScript inference</b> to build the AppRouter type from nested routers and procedures. Each procedure's input/output types are inferred from Zod schemas and resolver return types.<br><br><pre><code>type AppRouter = typeof appRouter;\n// Resolves to:\n// { user: { list: BuildProcedure&lt;...&gt;; byId: BuildProcedure&lt;...&gt; } }\n\ntype UserListOutput = inferRouterOutputs&lt;AppRouter&gt;['user']['list'];\n// Inferred from the actual resolver return type</code></pre><br><code>inferRouterInputs</code> and <code>inferRouterOutputs</code> are helper types for extracting input/output types from the router.",
  ["expert", "type-inference-deep"])

c("Expert",
  "How to use <code>inferRouterInputs</code> and <code>inferRouterOutputs</code>?",
  "<pre><code>import type { inferRouterInputs, inferRouterOutputs } from '@trpc/server';\nimport type { AppRouter } from '@/server/api/root';\n\ntype RouterInput = inferRouterInputs&lt;AppRouter&gt;;\ntype RouterOutput = inferRouterOutputs&lt;AppRouter&gt;;\n\n// Extract specific procedure types:\ntype PostCreateInput = RouterInput['post']['create']; // { title: string; content: string }\ntype PostListOutput = RouterOutput['post']['list'];    // Post[]\n\n// Use in components:\nfunction PostForm({ onSubmit }: { onSubmit: (data: PostCreateInput) => void }) { ... }</code></pre><br>These utility types let you extract the exact input/output types of any procedure — useful for component props, server actions, and test fixtures.",
  ["expert", "infer-types"])

c("Expert",
  "What to do when tRPC procedure names collide?",
  "tRPC procedure names are their keys in the router object. Collisions happen if you merge routers with the same key names.<br><br><pre><code>// ❌ Collision — both have 'list'\nconst appRouter = router({\n  user: userRouter,   // has user.list\n  post: postRouter,   // has post.list\n});\n// ✅ No collision — different namespacing\n\n// ❌ Collision — flat merge\nconst appRouter = mergeRouters(userRouter, postRouter); // both have 'list' at root!\n\n// ✅ Prefix explicitly:\nconst prefixedPostRouter = router({\n  post: postRouter, // all post procedures now under 'post.'\n});</code></pre><br>Namespacing via nested routers is the built-in solution. <code>mergeRouters</code> is for horizontal composition — use it carefully.",
  ["expert", "procedure-collisions"])

# ==================== Build ====================

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
