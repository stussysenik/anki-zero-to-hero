import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Next.js"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Routing":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Routing"),
    "Rendering":    genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Rendering"),
    "Patterns":     genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-Patterns"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# === NEXT.JS FUNDAMENTALS ===

c("Fundamentals", "What is Next.js?",
  "A React framework for building full-stack web applications. Provides file-system routing, server-side rendering, static generation, API routes, and image optimization out of the box. Built and maintained by Vercel.",
  ["L0_primitives"])

c("Fundamentals", "What is the App Router vs Pages Router?",
  "App Router (Next.js 13+): file-system routing with <code>page.tsx</code>, <code>layout.tsx</code>, <code>loading.tsx</code>, <code>error.tsx</code> special files. Uses React Server Components by default. Pages Router: legacy <code>pages/</code> directory with <code>getServerSideProps</code>. Use App Router for new projects.",
  ["L0_primitives"])

c("Fundamentals", "What is a React Server Component (RSC)?",
  "A React component that runs ONLY on the server. Cannot use hooks, state, event handlers, or browser APIs. In Next.js App Router, all components are Server Components by default unless marked <code>'use client'</code>.",
  ["L0_primitives"])

c("Fundamentals", "What does <code>'use client'</code> do?",
  "Marks a component (and all its children) as a Client Component — runs on server for initial HTML AND in the browser for interactivity. Use when you need <code>useState</code>, <code>useEffect</code>, event handlers, or browser APIs.",
  ["L0_primitives"])

c("Fundamentals", "What is SSR (Server-Side Rendering)?",
  "The server generates full HTML for each request. Good for dynamic, personalized content. In App Router, use <code>dynamic</code> rendering (use cookies/headers/searchParams in the page, or <code>noStore()</code> / <code>force-dynamic</code>).",
  ["L0_primitives"])

c("Fundamentals", "What is SSG (Static Site Generation)?",
  "Pages are rendered at build time to static HTML. No server needed at request time. In App Router, all routes are static by default (when possible). Use <code>generateStaticParams</code> for dynamic routes.",
  ["L0_primitives"])

c("Fundamentals", "What is ISR (Incremental Static Regeneration)?",
  "Statically generated pages are revalidated at a set interval. Combines static speed with fresh data. Set <code>next: { revalidate: 60 }</code> in <code>fetch</code> or <code>export const revalidate = 60</code> in the page.",
  ["L0_primitives"])

c("Fundamentals", "What is a Layout in the App Router?",
  "A <code>layout.tsx</code> wraps child pages and persists across navigations (no re-render). Defines shared UI (nav, footer). Must accept <code>children</code> prop. Can be nested: each folder can have its own layout.",
  ["L0_primitives"])

c("Fundamentals", "What is a middleware in Next.js?",
  "A <code>middleware.ts</code> file at the project root (or <code>src/</code>). Runs before every request. Used for authentication redirects, A/B testing, geo-blocking, bot detection. Returns <code>NextResponse.next()</code>, <code>.redirect()</code>, or <code>.rewrite()</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is the Next.js Image component?",
  "<code>next/image</code> — auto-optimizes images: lazy loading, responsive sizes, WebP/AVIF conversion, blur placeholders, prevents CLS. Requires <code>width</code> and <code>height</code>, or <code>fill</code> property.",
  ["L0_primitives"])

c("Fundamentals", "What is the Next.js Link component?",
  "<code>next/link</code> — client-side navigation with automatic prefetching of linked pages (when visible in viewport). Faster than raw <code>&lt;a&gt;</code> tags. <code>&lt;Link href=\"/about\"&gt;About&lt;/Link&gt;</code>.",
  ["L0_primitives"])

c("Fundamentals", "What is Next.js streaming?",
  "Server sends HTML in chunks as it's ready, not all at once. Use <code>React.Suspense</code> boundaries: <code>&lt;Suspense fallback={&lt;Loading /&gt;}&gt;&lt;SlowComponent /&gt;&lt;/Suspense&gt;</code>. Reduces TTFB and improves perceived performance.",
  ["L0_primitives"])

# === NEXT.JS CORE OPERATIONS ===

c("CoreOps", "How do you create a new Next.js project?",
  "<code>npx create-next-app@latest my-app</code> — interactive setup: TypeScript, ESLint, Tailwind, src/ directory, App Router, import alias. Or <code>pnpm create next-app</code> / <code>bunx create-next-app</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a page in App Router?",
  "Create <code>app/about/page.tsx</code> with a default export React component. Accessible at <code>/about</code>. File-system based: the folder path IS the URL path.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a dynamic route?",
  "Use <code>[slug]</code> folder: <code>app/posts/[slug]/page.tsx</code>. Access params with <code>{ params }: { params: { slug: string } }</code>. The name in brackets matches the param key.",
  ["L1_mechanics"])

c("CoreOps", "How do you create a layout?",
  "<code>app/layout.tsx</code> (root layout, required). Nest: <code>app/dashboard/layout.tsx</code> wraps <code>app/dashboard/*</code> pages. Must accept <code>children: React.ReactNode</code> and return JSX including <code>&lt;html&gt;</code> and <code>&lt;body&gt;</code> (root only).",
  ["L1_mechanics"])

c("CoreOps", "How do you fetch data in a Server Component?",
  "Just <code>const data = await fetch(url)</code> — no <code>useEffect</code>, no <code>useState</code>. async component: <code>export default async function Page() { const data = await fetch(...); return ... }</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you handle loading states?",
  "Create <code>loading.tsx</code> next to <code>page.tsx</code>. Next.js automatically shows it while the page and its children are loading (wrapping in Suspense internally). Or manual <code>&lt;Suspense&gt;</code> for granular boundaries.",
  ["L1_mechanics"])

c("CoreOps", "How do you handle errors?",
  "Create <code>error.tsx</code> (Client Component with <code>'use client'</code>) that receives <code>error</code> and <code>reset</code> props. Catches errors in child components. Use <code>&lt;button onClick={reset}&gt;Retry&lt;/button&gt;</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you create an API route?",
  "In App Router: <code>app/api/hello/route.ts</code>. Export async functions: <code>export async function GET() { return Response.json({ hello: 'world' }) }</code>. Same for POST, PUT, DELETE, PATCH, HEAD, OPTIONS.",
  ["L1_mechanics"])

c("CoreOps", "How do you redirect in Next.js?",
  "<code>import { redirect } from 'next/navigation'</code> — call <code>redirect('/login')</code> in Server Components/Actions. For client: <code>import { useRouter } from 'next/navigation'</code> then <code>router.push('/login')</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you revalidate cached data?",
  "Option 1: <code>fetch(url, { next: { revalidate: 60 } })</code> — background revalidate every 60s. Option 2: <code>revalidatePath('/posts')</code> or <code>revalidateTag('posts')</code> in Server Actions/Route Handlers. Option 3: make route dynamic with <code>noStore()</code>.",
  ["L1_mechanics"])

c("CoreOps", "How do you use environment variables?",
  "Server-side: <code>process.env.MY_VAR</code> in Server Components/API routes. Client-side: prefix with <code>NEXT_PUBLIC_</code>: <code>process.env.NEXT_PUBLIC_API_URL</code>. Client vars are inlined at build time — never expose secrets.",
  ["L1_mechanics"])

c("CoreOps", "How do you run the dev server?",
  "<code>next dev</code> — starts development server on port 3000. Hot Module Replacement. <code>next dev -p 4000</code> for custom port. <code>next dev --turbo</code> for Turbopack (faster, experimental).",
  ["L1_mechanics"])

# === NEXT.JS ROUTING ===

c("Routing", "What are route groups?",
  "Folders wrapped in parentheses: <code>(marketing)/</code> and <code>(shop)/</code>. They organize routes without affecting the URL. Each can have its own layout. <code>(marketing)/about/page.tsx</code> → <code>/about</code>.",
  ["L1_mechanics"])

c("Routing", "What is a catch-all segment?",
  "<code>[...slug]</code> — matches <code>/docs/a</code>, <code>/docs/a/b</code>, <code>/docs/a/b/c</code>. Params: <code>slug = ['a', 'b', 'c']</code>. Optional catch-all: <code>[[...slug]]</code> — also matches the parent route with empty array.",
  ["L1_mechanics"])

c("Routing", "What are parallel routes?",
  "Slots: <code>@analytics</code>, <code>@team</code> folders in a layout. Rendered simultaneously in the layout as props: <code>{analytics, team, children}</code>. Each has independent loading/error states. Used for dashboards.",
  ["L3_design"])

c("Routing", "What are intercepting routes?",
  "<code>(.)folder</code> = same level, <code>(..)parent</code> = one level up, <code>(...)root</code> = from root, <code>(..)(..)two-levels</code>. Intercept navigation to show content in a modal/overlay instead of full page navigation. Used with parallel routes for modals.",
  ["L3_design"])

# === NEXT.JS RENDERING ===

c("Rendering", "What are the three rendering strategies in Next.js App Router?",
  "Static (default): rendered at build time. Dynamic: rendered at request time (uses cookies, headers, <code>noStore()</code>, <code>searchParams</code>, or <code>force-dynamic</code>). Streaming: rendered progressively with Suspense.",
  ["L1_mechanics"])

c("Rendering", "What does <code>unstable_noStore</code> / <code>noStore</code> do?",
  "Opts out of caching for the current component/data fetch. Each request gets fresh data. From <code>next/cache</code>. Use <code>import { unstable_noStore as noStore } from 'next/cache'</code>.",
  ["L1_mechanics"])

c("Rendering", "What is the difference between <code>useSearchParams</code> and <code>searchParams</code> prop?",
  "<code>searchParams</code>: Server Component prop, available in <code>page.tsx</code>. <code>useSearchParams()</code>: Client Component hook from <code>next/navigation</code>. Page receiving <code>searchParams</code> opts into dynamic rendering.",
  ["L1_mechanics"])

c("Rendering", "What is Partial Prerendering (PPR)?",
  "A hybrid: static shell with dynamic holes (streamed). Configure <code>next.config.js: { experimental: { ppr: true } }</code>. Use <code>&lt;Suspense&gt;</code> boundaries: static content is prerendered, dynamic content streams.",
  ["L3_design"])

# === NEXT.JS PATTERNS ===

c("Patterns", "What is a Server Action?",
  "An async function marked <code>'use server'</code> that runs on the server. Can be called from Client Components. Replaces API routes for mutations. <code>async function create(formData: FormData) { 'use server'; await db.insert(...) }</code>.",
  ["L2_composition"])

c("Patterns", "What is the data-fetching-in-parent, render-in-child pattern?",
  "Fetch data in the Server Component parent (layout/page). Pass data as props to Client Component children. This keeps data fetching on the server and interactivity in the browser. Clean separation of concerns.",
  ["L2_composition"])

c("Patterns", "What is the Optimistic Updates pattern with Server Actions?",
  "Use <code>useOptimistic</code> hook to show the expected result immediately, then the server confirms/rejects. <code>useOptimistic(currentState, (state, newData) =&gt; [...state, newData])</code>. Roll back on error.",
  ["L2_composition"])

c("Patterns", "What is the form + Server Action pattern?",
  "<code>&lt;form action={myServerAction}&gt;</code> — works without JS (progressive enhancement). Use <code>useFormStatus</code> for pending state, <code>useFormState</code> for server-returned state (validation errors).",
  ["L2_composition"])

c("Patterns", "What is the parallel data fetching pattern?",
  "In Server Components, multiple <code>await fetch()</code> calls run sequentially. Use <code>Promise.all([fetch1(), fetch2()])</code> to fetch in parallel. Or use <code>&lt;Suspense&gt;</code> boundaries for streaming each data source independently.",
  ["L2_composition"])

# === NEXT.JS GOTCHAS ===

c("Gotchas", "Why does my page not update after deploying?",
  "Statically generated pages show stale data. Use <code>revalidate</code> in fetch or <code>export const revalidate = 60</code> in the page for ISR. Or use <code>revalidatePath()</code> in a Server Action to on-demand revalidate.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>use client</code> not make a component client-only?",
  "<code>'use client'</code> marks the boundary where client code starts. The component still renders on the server for initial HTML (SSR). Use dynamic import with <code>ssr: false</code> or <code>typeof window !== 'undefined'</code> checks for client-only code.",
  ["L4_diagnosis"])

c("Gotchas", "Why can't I use server-only code in a Client Component?",
  "Client Components cannot import <code>fs</code>, <code>path</code>, or use <code>process.env</code> secrets directly. Mark server-only modules with <code>import 'server-only'</code> (npm package) to get build-time errors if imported in client.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>useRouter</code> return null?",
  "You imported <code>useRouter</code> from <code>next/router</code> (Pages Router API). In App Router, import from <code>next/navigation</code>: <code>import { useRouter } from 'next/navigation'</code>.",
  ["L4_diagnosis"])

c("Gotchas", "What causes hydration errors with Next.js?",
  "Server HTML and client-rendered HTML differ. Common causes: <code>Date.now()</code>, <code>Math.random()</code>, browser-specific globals, or rendering based on <code>navigator</code> without suppression. Use <code>suppressHydrationWarning</code> or move logic to <code>useEffect</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why is my layout not re-rendering on navigation?",
  "Layouts persist across navigations by design. They do NOT re-render when child pages change. If you need per-page logic in a layout, use <code>usePathname()</code> in a Client Component wrapper or pass data from pages.",
  ["L4_diagnosis"])

# === NEXT.JS EXPERT ===

c("Expert", "What is Turbopack?",
  "Next.js's Rust-based bundler (replaces Webpack). Opt in with <code>next dev --turbo</code>. Significantly faster HMR and build times. Under active development; not yet stable for production builds.",
  ["L6_innovation"])

c("Expert", "What is the Edge Runtime?",
  "A lightweight runtime based on Web APIs (not Node.js). Use for middleware and API routes. Opt in: <code>export const runtime = 'edge'</code>. Runs on Vercel's Edge Network at CDN edge locations. Limited Node.js API access — uses <code>fetch</code>, <code>Response</code>, etc.",
  ["L3_design"])

c("Expert", "How do you set up caching with <code>next/cache</code>?",
  "<code>import { cache } from 'react'</code> — memoizes function results per request (deduplication). <code>import { unstable_cache } from 'next/cache'</code> — persists across requests with revalidation and tags. Layer: cache → unstable_cache → CDN.",
  ["L3_design"])

c("Expert", "What is the Metadata API?",
  "Export a <code>metadata</code> object or <code>generateMetadata</code> function from layouts/pages. Sets <code>&lt;title&gt;</code>, <code>&lt;meta&gt;</code>, OG images, etc. Server-side, can fetch data. Merges from layout to page. <code>generateMetadata({ params, searchParams })</code>.",
  ["L3_design"])

c("Expert", "How do you structure a large Next.js application?",
  "Feature-based colocation: <code>app/(auth)/login/</code>, <code>app/(dashboard)/analytics/</code>. Shared layouts with route groups. Domain logic in <code>lib/</code>. Server Actions close to their consuming forms. Keep data access layer separate (<code>lib/db.ts</code>).",
  ["L5_opinion"])

c("Expert", "What are Draft Mode and Preview Mode?",
  "Draft Mode enables viewing unpublished content (headless CMS). Enable via API route: <code>draftMode().enable()</code>. During rendering, check <code>draftMode().isEnabled</code> to bypass cache. Disable: <code>draftMode().disable()</code>. Uses a secure cookie.",
  ["L6_innovation"])

c("Expert", "How does Next.js decide between static and dynamic rendering?",
  "Static if: no <code>cookies()</code>, <code>headers()</code>, <code>searchParams</code>, <code>noStore()</code>, or <code>force-dynamic</code>. Dynamic otherwise. Output in terminal during build: <code>○ Static</code>, <code>λ Dynamic</code>, <code>ƒ Dynamic (streaming)</code>.",
  ["L3_design"])

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
