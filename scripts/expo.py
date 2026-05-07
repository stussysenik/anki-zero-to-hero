import genanki, random

R = lambda: random.randrange(1 << 30, 1 << 31)
TOPIC = "Expo"

model = genanki.Model(
    R(), f"{TOPIC} Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": "{{Front}}", "afmt": "{{FrontSide}}<hr id=answer>{{Back}}"}],
    css=""" .card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px; text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; } .front { font-weight: bold; margin-top: 60px; } .back { font-size: 20px; text-align: left; padding: 10px 30px; } code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244; padding: 2px 6px; border-radius: 4px; font-size: 18px; } hr { border-color: #45475a; }""",
)

decks = {
    "Fundamentals": genanki.Deck(R(), f"{TOPIC}::Zero2Hero::01-Fundamentals"),
    "CoreOps":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::02-Core-Operations"),
    "Router":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::03-Expo-Router"),
    "Components":   genanki.Deck(R(), f"{TOPIC}::Zero2Hero::04-Components-APIs"),
    "EAS":          genanki.Deck(R(), f"{TOPIC}::Zero2Hero::05-EAS-Build-Submit"),
    "DevWorkflow":  genanki.Deck(R(), f"{TOPIC}::Zero2Hero::06-Development-Workflow"),
    "Gotchas":      genanki.Deck(R(), f"{TOPIC}::Zero2Hero::07-Gotchas"),
    "Expert":       genanki.Deck(R(), f"{TOPIC}::Zero2Hero::08-Expert"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ═══════════════════════════════════════════
# L0: FUNDAMENTALS
# ═══════════════════════════════════════════

c("Fundamentals",
  "What is Expo?",
  "Expo is an open-source framework built on top of React Native that provides a <b>managed runtime</b>, a <b>universal native toolchain</b> (EAS), and a <b>file-based router</b>. It lets you write React code and deploy to iOS, Android, and web from a single codebase without touching Xcode or Android Studio.",
  "expo::fundamentals")

c("Fundamentals",
  "What is the <b>managed workflow</b> in Expo?",
  "The managed workflow means you write <b>only JavaScript/TypeScript</b> and Expo handles all native code. You don't have <code>ios/</code> or <code>android/</code> directories in your project. The Expo team maintains native modules, config plugins, and builds for you via EAS. Use Expo Go or a development build to test.",
  "expo::fundamentals")

c("Fundamentals",
  "What is the <b>bare workflow</b> in Expo?",
  "The bare workflow gives you full control over native <code>ios/</code> and <code>android/</code> directories. You can edit native code directly (Swift, Kotlin, Objective-C, Java) while still using Expo SDK packages. Generated via <code>npx expo prebuild</code> or by ejecting. You lose the ability to use Expo Go but gain unlimited native extensibility.",
  "expo::fundamentals")

c("Fundamentals",
  "What is <b>Expo Go</b>?",
  "Expo Go is a <b>sandboxed mobile app</b> (available on App Store / Google Play) that lets you load and test your Expo project instantly by scanning a QR code. It bundles a fixed set of Expo SDK modules. You cannot use custom native modules, Bluetooth, or background services with it.",
  "expo::fundamentals")

c("Fundamentals",
  "What is a <b>development build</b> in Expo?",
  "A development build is a <b>debug version of your app</b> compiled with <code>expo-dev-client</code>. Unlike Expo Go, it includes <b>all your custom native modules</b> and config plugins. You build it via <code>eas build --profile development</code> or <code>npx expo run:ios</code>. It has an in-app launcher, Dev Menu, and supports Fast Refresh.",
  "expo::fundamentals")

c("Fundamentals",
  "What is the <b>Expo SDK</b>?",
  "The Expo SDK is a <b>versioned set of cross-platform native APIs</b> shipped as npm packages under <code>expo-*</code>. Each SDK version (e.g. SDK 50, 51, 52) is tied to specific React Native and Expo Go versions. It includes modules for camera, location, notifications, file system, sensors, and 50+ more.",
  "expo::fundamentals")

c("Fundamentals",
  "How does Expo relate to React Native?",
  "Expo is a <b>superset / framework layer</b> on top of React Native. React Native provides the core bridge and primitives (View, Text, etc.). Expo adds:<br>• Managed native builds via EAS<br>• The Expo SDK (50+ audited native modules)<br>• Expo Router (file-based routing)<br>• OTA updates via <code>expo-updates</code><br>• Config plugins to modify native projects declaratively",
  "expo::fundamentals")

c("Fundamentals",
  "Why choose Expo over plain React Native?",
  "<b>1.</b> Zero native setup — no Xcode, no Android Studio<br><b>2.</b> OTA updates via <code>expo-updates</code> (bypass app store review)<br><b>3.</b> EAS Build handles cloud CI for both platforms<br><b>4.</b> File-based routing with Expo Router<br><b>5.</b> Audited, version-locked SDK modules that work together<br><b>6.</b> Config plugins let you customize native projects without writing native code",
  "expo::fundamentals")

c("Fundamentals",
  "What is the <b>Expo ecosystem</b>?",
  "Three core pillars:<br><b>1. Expo SDK</b> — versioned native module library (<code>expo-camera</code>, <code>expo-notifications</code>, etc.)<br><b>2. Expo Router</b> — file-based routing for universal apps<br><b>3. EAS (Expo Application Services)</b> — cloud build, submit, update, and secrets infrastructure",
  "expo::fundamentals")

c("Fundamentals",
  "What are <b>Expo Modules</b>?",
  "The <b>Expo Modules API</b> is the new native module system (since SDK 47+) that replaces the old <code>expo-modules-core</code> imperative API. It uses <b>Swift</b> (iOS) and <b>Kotlin</b> (Android) with declarative module definitions, automatic lifecycle management, and first-class TypeScript/JavaScript interop. It's used by all modern <code>expo-*</code> packages.",
  "expo::fundamentals")

c("Fundamentals",
  "What are the <b>limitations</b> of Expo?",
  "<b>1.</b> Expo Go cannot run custom native modules or Bluetooth/background services<br><b>2.</b> Some native APIs (CarPlay, WatchOS, WidgetKit) require bare workflow<br><b>3.</b> Games/3D with heavy OpenGL/Metal are better suited to React Native directly<br><b>4.</b> EAS Build has build concurrency limits on free tier<br><b>5.</b> SDK update cycle can lag behind latest React Native release by a few weeks",
  "expo::fundamentals")

c("Fundamentals",
  "What is <b>expo-dev-client</b>?",
  "<code>expo-dev-client</code> is a package that replaces Expo Go in development builds. It provides:<br>• An in-app <b>launcher UI</b> to switch between dev servers<br>• A <b>Dev Menu</b> (shake gesture or <code>Cmd+D</code>) with reload, debug, and perf options<br>• Support for custom native modules<br>• Extensible via Dev Tools plugins",
  "expo::fundamentals")

c("Fundamentals",
  "What is the difference between <code>expo-cli</code> and <code>npx expo</code>?",
  "The old <code>expo-cli</code> (<code>npm install -g expo-cli</code>) was a global CLI and is <b>deprecated</b>. The new CLI is <b>local</b> — installed per-project as part of <code>expo</code> package and invoked via <code>npx expo</code>. This ensures the CLI version matches the project's SDK version, preventing version mismatch bugs.",
  "expo::fundamentals")

c("Fundamentals",
  "What does the <code>app.json</code> / <code>app.config.js</code> file do in Expo?",
  "It is the <b>central configuration file</b> for an Expo project. It defines:<br>• <code>name</code>, <code>slug</code>, <code>version</code> of the app<br>• <code>scheme</code> for deep linking<br>• <code>plugins</code> array for config plugins<br>• iOS/Android-specific settings (bundle identifier, permissions)<br>• EAS build profiles<br>• <code>extra</code> for runtime config values<br>Use <code>app.config.js</code> or <code>app.config.ts</code> for dynamic config (based on environment, for example).",
  "expo::fundamentals")

c("Fundamentals",
  "What is the <code>expo</code> package in <code>package.json</code>?",
  "The <code>expo</code> npm package is the <b>core runtime</b> for Expo projects. It includes:<br>• The local CLI (<code>npx expo</code>)<br>• Metro bundler configuration<br>• Core native module shims<br>• Environment variable support (<code>EXPO_PUBLIC_</code>)<br>• The <code>expo-modules-core</code> bridge<br>Its version determines your <b>Expo SDK version</b>.",
  "expo::fundamentals")

c("Fundamentals",
  "What is <b>npx expo prebuild</b>?",
  "<code>npx expo prebuild</code> generates the native <code>ios/</code> and <code>android/</code> directories from your <code>app.json</code> and installed plugins. It's the command that bridges managed config to native projects. Run it when:<br>• Adding/removing a config plugin<br>• Changing native settings in app.json<br>• First setting up a bare workflow project<br>• After upgrading the Expo SDK",
  "expo::fundamentals")

# ═══════════════════════════════════════════
# L1: CORE OPERATIONS
# ═══════════════════════════════════════════

c("CoreOps",
  "How do you create a new Expo project?",
  "<code>npx create-expo-app@latest MyApp</code><br><br>This creates a new Expo project with:<br>• The latest Expo SDK<br>• Expo Router v3+ pre-configured<br>• TypeScript support<br>• Example <code>app/</code> directory with <code>_layout.tsx</code><br>• Pre-configured Metro bundler<br>Use <code>--template blank</code> for minimal setup or <code>--template tabs</code> for tab navigation starter.",
  "expo::core-ops")

c("CoreOps",
  "How do you start the Expo dev server?",
  "<code>npx expo start</code><br><br>Launches the Metro bundler with a QR code in the terminal. Flags:<br>• <code>--ios</code> — open iOS Simulator automatically<br>• <code>--android</code> — open Android Emulator automatically<br>• <code>--web</code> — open in web browser<br>• <code>--tunnel</code> — expose via ngrok (for physical devices on different networks)<br>• <code>-c</code> or <code>--clear</code> — clear Metro cache before starting<br>• <code>--go</code> — launch with Expo Go<br>• <code>--dev-client</code> — launch with development build",
  "expo::core-ops")

c("CoreOps",
  "How do you run an Expo app on an iOS simulator?",
  "<code>npx expo run:ios</code><br><br>This command:<br>1. Runs <code>prebuild</code> if no <code>ios/</code> directory exists<br>2. Installs CocoaPods dependencies<br>3. Builds the native Xcode project<br>4. Launches the iOS Simulator<br>Add <code>--device</code> to run on a connected physical iPhone. Add <code>--configuration Release</code> for production builds.",
  "expo::core-ops")

c("CoreOps",
  "How do you run an Expo app on an Android emulator?",
  "<code>npx expo run:android</code><br><br>This command:<br>1. Runs <code>prebuild</code> if no <code>android/</code> directory exists<br>2. Builds the Gradle project<br>3. Installs the APK on the emulator/device<br>4. Launches the app<br>Requirements: Android SDK, a running AVD emulator (or physical device connected via USB with ADB debugging enabled).",
  "expo::core-ops")

c("CoreOps",
  "What is <code>expo install</code> and why use it instead of <code>npm install</code>?",
  "<code>npx expo install &lt;package-name&gt;</code> installs a version of the package that is <b>known to be compatible</b> with your project's Expo SDK version. It queries the Expo registry for the correct version and resolves transitive dependencies. This prevents SDK version mismatch errors. Under the hood it calls your package manager (npm/yarn/pnpm) with the compatible version.",
  "expo::core-ops")

c("CoreOps",
  "How does Expo SDK versioning work?",
  "Each Expo SDK version (SDK 49, 50, 51, 52...) maps to:<br>• A specific <b>React Native version</b><br>• A corresponding <b>Expo Go app version</b><br>• Compatible versions of all <code>expo-*</code> packages<br>New SDK versions are released roughly <b>quarterly</b>, about 2–4 weeks after each new React Native stable release. Upgrade with <code>npx expo install expo@^52.0.0 --fix</code>.",
  "expo::core-ops")

c("CoreOps",
  "What is <code>npx expo-doctor</code> and when should you run it?",
  "<code>npx expo-doctor</code> is a <b>diagnostic tool</b> that checks your project for common issues:<br>• SDK version mismatches between packages<br>• Missing or incompatible native dependencies<br>• <code>app.json</code> validation errors<br>• Metro/Webpack config issues<br>Run it when builds fail, after upgrading the SDK, or when you see cryptic native errors.",
  "expo::core-ops")

c("CoreOps",
  "What is <code>npx expo install --fix</code>?",
  "<code>npx expo install --fix</code> scans your <code>package.json</code> and <code>node_modules</code>, then <b>automatically corrects</b> version mismatches for all <code>expo-*</code> packages to match your SDK version. It's essential after SDK upgrades to align the entire dependency tree. Think of it as <code>expo-doctor</code> + auto-repair.",
  "expo::core-ops")

c("CoreOps",
  "What does <code>app.json</code> <code>expo.scheme</code> do?",
  "The <code>scheme</code> field defines the <b>custom URL scheme</b> for deep linking into your app. Example: <code>\"myapp\"</code> means <code>myapp://</code> URLs will open your app. It's used by:<br>• Expo Router deep linking<br>• OAuth redirect URIs<br>• Universal links (in combination with associated domains)<br>Must be <b>lowercase</b> and <b>URL-safe</b>.",
  "expo::core-ops")

c("CoreOps",
  "What is <code>eas.json</code> and where does it live?",
  "<code>eas.json</code> is the configuration file for <b>EAS Build and EAS Submit</b>, located at your project root. It defines build profiles (development, preview, production) with platform-specific settings, submit profiles for App Store / Google Play submission, and global EAS CLI settings. Each profile can override <code>app.json</code> values.",
  "expo::core-ops")

c("CoreOps",
  "How do you configure environment variables in Expo?",
  "Variables prefixed with <code>EXPO_PUBLIC_</code> in <code>.env</code> or system environment are <b>inlined at build time</b> and accessible via <code>process.env.EXPO_PUBLIC_X</code> in your JS bundle.<br><br>For <b>EAS Build</b> secrets (API keys, tokens), use <code>eas secret:create</code> to store them server-side; they are available during build but not baked into the binary. Use <code>eas secret:list</code> and <code>eas secret:delete</code> to manage them.",
  "expo::core-ops")

c("CoreOps",
  "How do you upgrade an Expo project to a newer SDK?",
  "<code>npx expo install expo@latest</code><br><code>npx expo install --fix</code><br><code>npx expo-doctor</code><br><br>This upgrades the <code>expo</code> package, then <code>--fix</code> aligns all <code>expo-*</code> packages to the new SDK version. Follow up with <code>npx expo prebuild --clean</code> to regenerate native directories. Check the Expo SDK changelog for breaking changes specific to that version.",
  "expo::core-ops")

# ═══════════════════════════════════════════
# L2: EXPO ROUTER
# ═══════════════════════════════════════════

c("Router",
  "What is <b>Expo Router</b>?",
  "Expo Router is a <b>file-based routing framework</b> for Expo apps (web, iOS, Android). It maps the <code>app/</code> directory structure to navigation routes automatically. Key features:<br>• Convention-based (like Next.js App Router)<br>• Typed routes (with <code>expo-router</code> autocomplete)<br>• Deep linking out of the box<br>• iOS/Android native navigation + web URLs<br>• Built on React Navigation<br>• Support for Stack, Tab, Drawer layouts",
  "expo::router")

c("Router",
  "What is the <code>app/</code> directory in Expo Router?",
  "The <code>app/</code> directory is the <b>root of all routes</b>. Every <code>.tsx</code> file inside becomes a screen/route. Conventions:<br>• <code>app/index.tsx</code> → <code>/</code><br>• <code>app/about.tsx</code> → <code>/about</code><br>• <code>app/profile/settings.tsx</code> → <code>/profile/settings</code><br>• <code>app/[id].tsx</code> → <code>/:id</code> (dynamic)<br>• <code>app/_layout.tsx</code> → shared layout wrapper<br>This is the <b>single convention</b> that drives all routing.",
  "expo::router")

c("Router",
  "What is the entry point for Expo Router?",
  "Set <code>\"main\": \"expo-router/entry\"</code> in <code>package.json</code> and the <code>\"scheme\"</code> in <code>app.json</code>. This tells Metro to start from Expo Router's internal entry point, which:<br>1. Loads the <code>app/</code> directory<br>2. Sets up navigation state<br>3. Handles deep links<br>4. Renders the root layout<br>No explicit <code>NavigationContainer</code> needed — Expo Router manages it internally.",
  "expo::router")

c("Router",
  "What is <code>_layout.tsx</code> in Expo Router?",
  "<code>_layout.tsx</code> is a <b>shared layout wrapper</b> for all routes in its directory (and subdirectories). It must render a <code>&lt;Slot /&gt;</code> or a navigator (<code>&lt;Stack&gt;</code>, <code>&lt;Tabs&gt;</code>, <code>&lt;Drawer&gt;</code>). The root <code>app/_layout.tsx</code> wraps all pages. Nested <code>_layout.tsx</code> files create nested navigators — e.g. <code>app/(tabs)/_layout.tsx</code> wraps only the tab group.",
  "expo::router")

c("Router",
  "What is <code>&lt;Slot /&gt;</code> in Expo Router?",
  "<code>&lt;Slot /&gt;</code> is a <b>placeholder</b> that renders the current child route inside a layout. If your <code>_layout.tsx</code> does NOT use a navigator, you must render <code>&lt;Slot /&gt;</code> so the child screen appears. Example:<br><code>export default function Layout() {</code><br><code>  return &lt;Stack&gt;&lt;Stack.Screen name=\"index\" /&gt;&lt;Slot /&gt;&lt;/Stack&gt;</code><br><code>}</code>",
  "expo::router")

c("Router",
  "How do you define a <b>Stack navigator</b> in Expo Router?",
  "Import <code>Stack</code> from <code>expo-router</code> and wrap in <code>_layout.tsx</code>:<br><code>import { Stack } from 'expo-router';</code><br><code>export default function Layout() {</code><br><code>  return &lt;Stack screenOptions={{ headerStyle: { backgroundColor: '#fff' } }} /&gt;;</code><br><code>}</code><br>Each file in that directory automatically becomes a screen on the stack. Use <code>&lt;Stack.Screen name=\"...\" options={{...}} /&gt;</code> for per-screen config.",
  "expo::router")

c("Router",
  "How do you define a <b>Tab navigator</b> in Expo Router?",
  "Use <code>Tabs</code> from <code>expo-router</code> inside a layout:<br><code>import { Tabs } from 'expo-router';</code><br><code>export default function TabLayout() {</code><br><code>  return (</code><br><code>    &lt;Tabs&gt;</code><br><code>      &lt;Tabs.Screen name=\"index\" options={{ title: 'Home', tabBarIcon: ... }} /&gt;</code><br><code>      &lt;Tabs.Screen name=\"settings\" options={{ title: 'Settings' }} /&gt;</code><br><code>    &lt;/Tabs&gt;</code><br><code>  );</code><br><code>}</code><br>Tab screens are defined by <code>app/(tabs)/</code> directory convention (or any nested group).",
  "expo::router")

c("Router",
  "How does <code>&lt;Link&gt;</code> work in Expo Router?",
  "<code>import { Link } from 'expo-router';</code><br><code>&lt;Link href=\"/profile/123\"&gt;Go to Profile&lt;/Link&gt;</code><br><br><code>&lt;Link&gt;</code> renders a <b>touchable element</b> that navigates to a route. Props:<br>• <code>href</code> — target route path<br>• <code>asChild</code> — use with custom button components<br>• <code>push</code> — push onto stack instead of default behavior<br>• <code>replace</code> — replace current screen<br>It's typed — Expo Router provides autocomplete for href values.",
  "expo::router")

c("Router",
  "How do you navigate <b>programmatically</b> with Expo Router?",
  "Import <code>router</code> from <code>expo-router</code>:<br><code>import { router } from 'expo-router';</code><br><br><code>router.push('/profile/123')</code> — push a new screen on the stack<br><code>router.replace('/dashboard')</code> — replace current screen<br><code>router.back()</code> — go back one screen<br><code>router.dismissAll()</code> — go to root<br><code>router.navigate('/login')</code> — navigate (push by default, but can resolve to replace for tabs)<br><code>router.setParams({ id: '456' })</code> — update params on current route",
  "expo::router")

c("Router",
  "What are <b>dynamic routes</b> in Expo Router?",
  "Use bracket syntax in filenames:<br>• <code>app/[id].tsx</code> → matches <code>/123</code>, <code>/about</code><br>• <code>app/user/[userId].tsx</code> → matches <code>/user/42</code><br>• <code>app/[...rest].tsx</code> → catch-all<br>• <code>app/post/[id]/[commentId].tsx</code> → multiple params<br>Access params with <code>useLocalSearchParams()</code> hook.",
  "expo::router")

c("Router",
  "How do you access <b>route parameters</b> in Expo Router?",
  "<code>import { useLocalSearchParams } from 'expo-router';</code><br><code>const { id, userId } = useLocalSearchParams&lt;{ id: string; userId?: string }&gt;();</code><br><br><code>useLocalSearchParams()</code> returns the parsed search/route params for the current screen. Use <b>global search params</b> with <code>useGlobalSearchParams()</code> if you need params from parent/ancestor routes. For regular navigation params use <code>useSearchParams()</code>.",
  "expo::router")

c("Router",
  "What are <b>route groups</b> <code>(group)/</code> in Expo Router?",
  "Parenthesized directory names like <code>app/(auth)/</code> or <code>app/(tabs)/</code> create <b>route groups</b> — they affect layout organization <b>without</b> appearing in the URL. A group's <code>_layout.tsx</code> wraps all children with a shared navigator/layout. This lets you create multiple stacks or tab navigators without polluting the path structure.",
  "expo::router")

c("Router",
  "What is the <code>&lt;Redirect&gt;</code> component?",
  "<code>import { Redirect } from 'expo-router';</code><br><code>&lt;Redirect href=\"/login\" /&gt;</code><br><br>Renders a <b>redirect</b> — as soon as the component mounts, navigation replaces the current route with the target. Commonly used in <code>app/index.tsx</code> to redirect based on auth state to <code>/(tabs)</code> or <code>/login</code>.",
  "expo::router")

c("Router",
  "What is <code>+not-found.tsx</code> in Expo Router?",
  "A special file at <code>app/+not-found.tsx</code> that renders when a route doesn't exist (404). It's automatically shown by Expo Router when navigation can't resolve a path. Customize it with your own UI. You can also create nested not-found files (e.g. <code>app/profile/+not-found.tsx</code>) for section-specific 404s.",
  "expo::router")

c("Router",
  "How do you set <b>custom headers</b> per screen in Expo Router?",
  "Use <code>&lt;Stack.Screen&gt;</code> inside your layout:<br><code>&lt;Stack&gt;</code><br><code>  &lt;Stack.Screen name=\"index\" options={{ headerShown: false }} /&gt;</code><br><code>  &lt;Stack.Screen</code><br><code>    name=\"profile\"</code><br><code>    options={{ headerTitle: 'My Profile', headerRight: () => &lt;SettingsIcon /&gt; }}</code><br><code>  /&gt;</code><br><code>&lt;/Stack&gt;</code><br>Or use the <code>useNavigation()</code> hook with <code>navigation.setOptions({...})</code> inside the screen component.",
  "expo::router")

c("Router",
  "How do <b>deep links</b> work with Expo Router?",
  "Expo Router automatically wires deep links through the URL scheme defined in <code>app.json</code>. With <code>\"scheme\": \"myapp\"</code>, clicking <code>myapp://profile/123</code> opens <code>app/profile/[id].tsx</code> with <code>id=123</code>. For <b>universal links</b> (iOS) / <b>app links</b> (Android), configure <code>associatedDomains</code> in <code>app.json</code> and host an <code>apple-app-site-association</code> / <code>assetlinks.json</code> file on your domain.",
  "expo::router")

c("Router",
  "What hook gives you <b>navigation</b> in Expo Router?",
  "<code>import { useNavigation } from 'expo-router';</code><br><code>const navigation = useNavigation();</code><br><br>Returns the React Navigation navigation object. Use it for:<br>• <code>navigation.setOptions({ headerTitle: 'Custom' })</code><br>• <code>navigation.addListener('focus', callback)</code><br>• <code>navigation.goBack()</code><br>• <code>navigation.getParent()</code> to access parent navigator<br>For basic navigation, prefer <code>router</code> object — <code>useNavigation()</code> is for advanced imperative control.",
  "expo::router")

c("Router",
  "What are <b>typed routes</b> in Expo Router?",
  "Expo Router generates TypeScript types from your <code>app/</code> directory structure. After running <code>npx expo start</code>, it creates type definitions so that:<br>• <code>href</code> in <code>&lt;Link&gt;</code> is autocompleted and type-checked<br>• <code>router.push()</code> only accepts valid routes<br>• <code>useLocalSearchParams</code> infers param names<br>This is enabled by having <code>\"expo-router\"</code> in your <code>tsconfig.json</code> types.",
  "expo::router")

c("Router",
  "What are <b>modal routes</b> in Expo Router?",
  "Any screen file can be presented as a modal by adding <code>presentation: 'modal'</code> in its screen options within the layout:<br><code>&lt;Stack.Screen name=\"compose\" options={{ presentation: 'modal' }} /&gt;</code><br>This slides the screen up from the bottom on iOS (and fades on Android by default). Combine with <code>animation: 'fade'</code> or <code>animation: 'slide_from_bottom'</code> for cross-platform consistency.",
  "expo::router")

c("Router",
  "How does <b>nested navigation</b> work in Expo Router?",
  "Create a subdirectory with its own <code>_layout.tsx</code>:<br><code>app/profile/_layout.tsx</code> → can define its own Stack/Tabs<br><code>app/profile/index.tsx</code> → <code>/profile</code><br><code>app/profile/settings.tsx</code> → <code>/profile/settings</code><br><br>The inner layout wraps only routes within <code>profile/</code>. This creates nested navigators. The outer layout's <code>&lt;Slot /&gt;</code> or navigator renders the inner layout, creating a hierarchy.",
  "expo::router")

# ═══════════════════════════════════════════
# L2: COMPONENTS & APIs
# ═══════════════════════════════════════════

c("Components",
  "What is <code>expo-camera</code> and how do you use it?",
  "<code>expo-camera</code> provides cross-platform camera access. Key usage pattern:<br><code>import { CameraView, useCameraPermissions } from 'expo-camera';</code><br><br>• <code>CameraView</code> — the camera preview component (replaces old <code>Camera</code>)<br>• <code>useCameraPermissions()</code> — request/check camera permission<br>• Supports photo capture (<code>takePictureAsync</code>), video recording, barcode scanning, flash mode, zoom, and face detection<br>• <code>facing</code> prop: <code>'front'</code> or <code>'back'</code><br>• SDK 51+ uses the new <code>CameraView</code> API.",
  "expo::components")

c("Components",
  "What is <code>expo-location</code> and what are its key methods?",
  "<code>expo-location</code> provides geolocation and geofencing APIs. Key methods:<br>• <code>requestForegroundPermissionsAsync()</code> — ask for while-in-use access<br>• <code>getCurrentPositionAsync()</code> — one-time location fix<br>• <code>watchPositionAsync()</code> — continuous location updates<br>• <code>geocodeAsync(address)</code> — address to coordinates<br>• <code>reverseGeocodeAsync({latitude, longitude})</code> — coordinates to address<br>• <code>startGeofencingAsync()</code> — region monitoring (background)<br>Requires <code>expo-location</code> config plugin in <code>app.json</code>.",
  "expo::components")

c("Components",
  "What is <code>expo-notifications</code> and how do you set it up?",
  "<code>expo-notifications</code> handles local and push notifications. Setup steps:<br>1. <code>npx expo install expo-notifications expo-device</code><br>2. Add <code>expo-notifications</code> config plugin to <code>app.json</code><br>3. Request <code>Notifications.getPermissionsAsync()</code> (iOS)<br>4. Get push token with <code>getExpoPushTokenAsync()</code><br>5. Handle incoming via <code>setNotificationHandler()</code><br>6. Schedule local with <code>scheduleNotificationAsync()</code><br>Supports categories, attachments (iOS), and notification channels (Android).",
  "expo::components")

c("Components",
  "What is <code>expo-image-picker</code> and how do you use it?",
  "<code>expo-image-picker</code> allows users to select images/videos from the library or take new photos. Key API:<br>• <code>launchImageLibraryAsync(options)</code> — pick from gallery<br>• <code>launchCameraAsync(options)</code> — take a photo<br>• <code>requestMediaLibraryPermissionsAsync()</code><br>• <code>requestCameraPermissionsAsync()</code><br>Options: <code>mediaTypes</code>, <code>allowsEditing</code>, <code>quality</code>, <code>base64</code><br>Returns: <code>{ cancelled, assets[{uri, width, height}] }</code><br>No config plugin needed — uses built-in native pickers.",
  "expo::components")

c("Components",
  "What is <code>expo-file-system</code> and what can it do?",
  "<code>expo-file-system</code> provides access to the device's file system. Key features:<br>• <code>documentDirectory</code> — persistent app-internal storage<br>• <code>cacheDirectory</code> — cache that may be cleared by OS<br>• <code>readAsStringAsync(uri)</code>, <code>writeAsStringAsync(uri, content)</code><br>• <code>getInfoAsync(uri)</code> — file size, existence, modification time<br>• <code>downloadAsync(uri, fileUri)</code> — download files with progress<br>• <code>uploadAsync(url, fileUri)</code> — upload files with multipart support<br>• <code>deleteAsync(uri)</code>, <code>makeDirectoryAsync(uri)</code>, <code>moveAsync()</code>",
  "expo::components")

c("Components",
  "What is <code>expo-secure-store</code> and when do you use it?",
  "<code>expo-secure-store</code> provides encrypted key-value storage using iOS Keychain and Android EncryptedSharedPreferences. Use it for tokens, passwords, and sensitive data — <b>not</b> <code>AsyncStorage</code>. Key methods:<br>• <code>setItemAsync(key, value)</code><br>• <code>getItemAsync(key)</code><br>• <code>deleteItemAsync(key)</code><br>Options: <code>keychainAccessible</code> (iOS), <code>requireAuthentication</code> (biometric lock).",
  "expo::components")

c("Components",
  "What sensors does <code>expo-sensors</code> provide?",
  "<code>expo-sensors</code> gives access to device motion and environmental sensors:<br>• <b>Accelerometer</b> — device acceleration (including gravity)<br>• <b>Gyroscope</b> — rotation rate<br>• <b>Magnetometer</b> — magnetic field<br>• <b>Pedometer</b> — step counting (iOS &amp; Android)<br>• <b>Barometer</b> — air pressure (iOS only)<br>• <b>DeviceMotion</b> — combined attitude/rotation/acceleration<br>Each sensor has <code>addListener(callback)</code> and <code>setUpdateInterval(ms)</code>.",
  "expo::components")

c("Components",
  "What is <code>expo-haptics</code> and how do you trigger feedback?",
  "<code>expo-haptics</code> provides haptic (vibration) feedback. Methods:<br>• <code>Haptics.impactAsync(style)</code> — light, medium, heavy impact<br>• <code>Haptics.notificationAsync(type)</code> — success, warning, error<br>• <code>Haptics.selectionAsync()</code> — subtle tap for UI selection changes<br>Use for button presses, gesture confirmations, and notifications. Requires no permissions. Falls back to <code>Vibration</code> API on Android.",
  "expo::components")

c("Components",
  "What is <code>expo-av</code> and what does it support?",
  "<code>expo-av</code> (Audio/Video) provides a unified playback API:<br>• <code>Audio.Sound.createAsync(source)</code> — play sound effects<br>• <code>Audio.Recording</code> — record audio to file<br>• <code>Video</code> component — video playback with controls<br>• <code>Audio.setAudioModeAsync()</code> — configure audio session (background, category, etc.)<br>Key features: rate/pitch control, looping, progress, status callbacks, and multiple simultaneous instances.",
  "expo::components")

c("Components",
  "What is <code>expo-barcode-scanner</code>?",
  "<code>expo-barcode-scanner</code> (deprecated in SDK 51, replaced by <code>expo-camera</code> barcode scanning or <code>expo-camera/next</code>) scans barcodes and QR codes using the camera. <code>&lt;BarCodeScanner&gt;</code> component with <code>onBarCodeScanned</code> callback. In modern Expo, use <code>CameraView</code> from <code>expo-camera</code> with the <code>barcodeScannerSettings</code> prop instead.",
  "expo::components")

c("Components",
  "What is <code>expo-device</code> and what info does it provide?",
  "<code>expo-device</code> returns device hardware and OS information. Key properties:<br>• <code>Device.modelName</code> — e.g. \"iPhone 15 Pro\"<br>• <code>Device.osName</code> — \"iOS\" or \"Android\"<br>• <code>Device.osVersion</code> — e.g. \"17.2\"<br>• <code>Device.platformApiLevel</code> (Android)<br>• <code>Device.deviceYearClass</code> — estimated performance tier<br>• <code>Device.isDevice</code> — true on physical device, false on simulator<br>• <code>Device.totalMemory</code>, <code>Device.supportedCpuArchitectures</code><br>Use for analytics, feature gating, and bug reports.",
  "expo::components")

c("Components",
  "What is <code>expo-constants</code> and what data does it expose?",
  "<code>expo-constants</code> provides build-time constants and app metadata:<br>• <code>Constants.expoConfig</code> — parsed <code>app.json</code> at runtime<br>• <code>Constants.appOwnership</code> — 'expo' (Go), 'standalone' (build), 'guest'<br>• <code>Constants.deviceName</code><br>• <code>Constants.nativeAppVersion</code> / <code>nativeBuildVersion</code><br>• <code>Constants.manifest</code> — full manifest<br>• <code>Constants.systemFonts</code><br>• <code>Constants.executionEnvironment</code> — 'storeClient', 'standalone', 'bare'",
  "expo::components")

c("Components",
  "What is <code>expo-linking</code> and how does it work?",
  "<code>expo-linking</code> provides utilities for working with deep links:<br>• <code>Linking.createURL('/profile/123')</code> — build a full deep link URL using your app's scheme<br>• <code>Linking.addEventListener('url', callback)</code> — listen for incoming links<br>• <code>Linking.parse(url)</code> — parse a URL into path and queryParams<br>• <code>Linking.openURL('https://...')</code> — open external URL in browser<br>In Expo Router, deep link handling is mostly automatic — use this for custom link logic.",
  "expo::components")

c("Components",
  "What is <code>expo-web-browser</code> and how does it differ from <code>Linking.openURL</code>?",
  "<code>expo-web-browser</code> opens an <b>in-app browser</b> (SFSafariViewController on iOS, Chrome Custom Tabs on Android) instead of switching apps. Key methods:<br>• <code>openBrowserAsync(url)</code> — opens the browser<br>• <code>dismissBrowser()</code> — close the browser<br>• <code>openAuthSessionAsync(url, redirectUrl)</code> — for OAuth flows (auto-closes on redirect)<br>• <code>maybeCompleteAuthSession()</code> — handle OAuth redirect in web<br>Provides better UX for auth flows and keeps users in your app.",
  "expo::components")

c("Components",
  "What is <code>expo-clipboard</code> and how do you use it?",
  "<code>expo-clipboard</code> provides copy/paste access to the system clipboard:<br>• <code>Clipboard.setStringAsync('text')</code> — copy text<br>• <code>Clipboard.getStringAsync()</code> — paste text<br>• <code>Clipboard.setImageAsync(imageUri)</code> — copy image<br>• <code>Clipboard.getImageAsync()</code> — paste image (returns <code>{data, size}</code>)<br>• <code>Clipboard.hasStringAsync()</code>, <code>Clipboard.hasImageAsync()</code> — check clipboard contents<br>No permissions required on either platform.",
  "expo::components")

c("Components",
  "What is <code>expo-sharing</code> and when do you use it?",
  "<code>expo-sharing</code> opens the native share dialog for files. Key method:<br><code>Sharing.shareAsync(fileUri, { mimeType, UTI, dialogTitle })</code><br><br>Use when you have generated a file (PDF, image, etc.) in <code>expo-file-system</code> and want to let the user share it via Mail, Messages, AirDrop, etc. Under the hood uses <code>UIActivityViewController</code> (iOS) and <code>Intent.ACTION_SEND</code> (Android).",
  "expo::components")

c("Components",
  "What is <code>expo-splash-screen</code> and how do you control it?",
  "<code>expo-splash-screen</code> lets you keep the native splash screen visible while your app loads:<br>• <code>SplashScreen.preventAutoHideAsync()</code> — keep splash visible<br>• <code>SplashScreen.hideAsync()</code> — dismiss splash when app is ready<br>• <code>SplashScreen.setOptions({ duration, fade })</code> — animation settings<br>Configure the splash image/background in <code>app.json</code> under <code>expo.splash</code>.<br>Best practice: keep splash visible until fonts are loaded and initial data is ready.",
  "expo::components")

c("Components",
  "What is <code>expo-screen-orientation</code> and what does it control?",
  "<code>expo-screen-orientation</code> allows locking and reading screen orientation:<br>• <code>lockAsync(ORIENTATION_LOCK)</code> — lock to portrait, landscape, etc.<br>• <code>lockPlatformAsync(options)</code> — platform-specific lock<br>• <code>getOrientationAsync()</code> — current orientation<br>• <code>addOrientationChangeListener(callback)</code><br>Useful for video players (lock to landscape), camera screens, and iPad multi-window support.",
  "expo::components")

c("Components",
  "What is <code>expo-status-bar</code> and how is it used?",
  "<code>expo-status-bar</code> is a React component that controls the status bar appearance:<br><code>import { StatusBar } from 'expo-status-bar';</code><br><code>&lt;StatusBar style=\"light\" /&gt;</code><br><br>Props: <code>style</code> ('light', 'dark', 'auto'), <code>hidden</code>, <code>backgroundColor</code> (Android), <code>translucent</code> (Android), <code>animated</code>. Unlike React Native's <code>StatusBar</code>, it works correctly in Expo Go and handles both platforms uniformly.",
  "expo::components")

c("Components",
  "What is <code>expo-navigation-bar</code> and what does it do?",
  "<code>expo-navigation-bar</code> controls the Android navigation bar (bottom system buttons). Methods:<br>• <code>setBackgroundColorAsync(color)</code><br>• <code>setButtonStyleAsync('light' | 'dark')</code><br>• <code>setVisibilityAsync('visible' | 'hidden')</code><br>• <code>setBehaviorAsync('overlay-swipe' | ...)</code><br>No effect on iOS (no equivalent system UI). Use with <code>expo-status-bar</code> for a cohesive immersive look.",
  "expo::components")

c("Components",
  "What is <code>expo-font</code> and how do you load custom fonts?",
  "<code>import { useFonts } from 'expo-font';</code><br><code>const [loaded] = useFonts({</code><br><code>  'Inter-Bold': require('./assets/fonts/Inter-Bold.ttf'),</code><br><code>  'SpaceMono': require('./assets/fonts/SpaceMono-Regular.ttf'),</code><br><code>});</code><br><br>Returns <code>[loaded, error]</code>. Keep the splash screen visible until <code>loaded</code> is <code>true</code>. Alternatively, use <code>Font.loadAsync()</code> (async/await). Fonts are cached after first load per app session.",
  "expo::components")

c("Components",
  "What is <code>expo-asset</code> and what problem does it solve?",
  "<code>expo-asset</code> provides a unified way to load assets (images, fonts, audio, video) with download progress across all platforms. Key API:<br>• <code>Asset.loadAsync(modules)</code> — preload assets<br>• <code>Asset.fromModule(require('./image.png'))</code> — get asset object<br>• <code>asset.downloadAsync()</code> — download remote asset and cache locally<br>Assets are served from the embedded bundle in production and can be optimized via bundler configuration.",
  "expo::components")

c("Components",
  "What is <code>expo-task-manager</code> and <code>expo-background-fetch</code>?",
  "<code>expo-task-manager</code> lets you define JavaScript tasks that run in the background:<br>• <code>TaskManager.defineTask('NAME', callback)</code> — define a task<br>• <code>TaskManager.isTaskRegisteredAsync('NAME')</code><br><br><code>expo-background-fetch</code> periodically runs these tasks even when the app is closed:<br>• <code>BackgroundFetch.registerTaskAsync('NAME', options)</code><br>• <code>BackgroundFetch.setMinimumIntervalAsync(minutes)</code><br>Note: background execution is platform-restricted and NOT available in Expo Go.",
  "expo::components")

c("Components",
  "What is <code>expo-auth-session</code> and how does it handle OAuth?",
  "<code>expo-auth-session</code> implements PKCE-based OAuth 2.0 flows in a browser:<br>• <code>AuthSession.useAuthRequest(config, discovery)</code> — hook for OAuth<br>• <code>AuthSession.AuthRequest</code> — class-based API<br>• <code>AuthSession.exchangeCodeAsync()</code> — exchange auth code for tokens<br>• <code>AuthSession.makeRedirectUri()</code> — generate redirect URI<br>Uses <code>expo-web-browser</code> internally. Supports Google, Facebook, Spotify, and any OAuth 2.0 provider with PKCE. Proxy option available for providers that don't support PKCE.",
  "expo::components")

c("Components",
  "What is <code>expo-google-sign-in</code>?",
  "<code>expo-google-sign-in</code> provides native Google Sign-In integration using the Google Sign-In SDK (NOT OAuth in browser). Key methods:<br>• <code>GoogleSignIn.initAsync(config)</code><br>• <code>GoogleSignIn.signInAsync()</code><br>• <code>GoogleSignIn.signOutAsync()</code><br><b>Deprecated by Google</b> in favor of Credential Manager (Android) and Sign In With Google (iOS). For new apps, use <code>expo-auth-session</code> with Google's OAuth flow or <code>@react-native-google-signin/google-signin</code> (in a dev build).",
  "expo::components")

c("Components",
  "What is <code>expo-apple-authentication</code> and what does it provide?",
  "<code>expo-apple-authentication</code> provides Sign In with Apple on iOS:<br>• <code>&lt;AppleAuthentication.AppleAuthenticationButton&gt;</code><br>• <code>AppleAuthentication.signInAsync()</code><br>Returns identity token, authorization code, user identifier, email, name. On Android, this module is a no-op (Sign In with Apple is only required by Apple for apps that use third-party social sign-in on iOS).",
  "expo::components")

c("Components",
  "What is <code>expo-updates</code> and how does OTA update work?",
  "<code>expo-updates</code> enables <b>over-the-air (OTA) updates</b> — pushing JavaScript/asset changes without going through app store review. How it works:<br>1. You publish an update via <code>eas update</code><br>2. On next app launch, <code>expo-updates</code> checks for an update<br>3. If found, downloads the new JS bundle/assets in the background<br>4. On next launch, the app loads the new update<br>• <code>Updates.checkForUpdateAsync()</code><br>• <code>Updates.fetchUpdateAsync()</code><br>• <code>Updates.reloadAsync()</code> — apply and reload<br>Native code changes (.apk/.ipa) still require a new build.",
  "expo::components")

c("Components",
  "What is the <b>Expo Modules API</b> and how does it improve over old native modules?",
  "The Expo Modules API (since SDK 47) is a <b>declarative native module system</b> using Swift (iOS) and Kotlin (Android). Advantages over old React Native TurboModules:<br>• Auto-generated JavaScript/TypeScript bindings<br>• Lifecycle-aware modules (onCreate, onDestroy)<br>• First-class coroutine/async support in Kotlin<br>• Event emitter pattern built-in<br>• Easier to write — no manual bridge code<br>• Bi-directional type safety<br>Modules are packaged as npm packages and consumed via <code>expo-module.config.json</code>.<br>Use <code>npx create-expo-module</code> to scaffold a new module.",
  "expo::components")

# ═══════════════════════════════════════════
# L3: EAS (Expo Application Services)
# ═══════════════════════════════════════════

c("EAS",
  "What is <b>EAS Build</b>?",
  "EAS Build is Expo's <b>cloud CI/CD service</b> for compiling native iOS and Android binaries. You don't need a Mac, Xcode, or Android Studio locally. Trigger a build with:<br><code>eas build --platform ios</code><br><code>eas build --platform android</code><br><code>eas build --platform all</code><br>Builds run in Expo's cloud infrastructure. Results are installable via QR code/test flight link (iOS) or direct APK/AAB download (Android). Free tier includes ~20 builds/month.",
  "expo::eas")

c("EAS",
  "What is <code>eas.json</code> and what is its structure?",
  "<code>eas.json</code> is the EAS configuration file at the project root. Structure:<br><code>{</code><br><code>  \"cli\": { \"version\": \">= 5.0.0\" },</code><br><code>  \"build\": {</code><br><code>    \"development\": { \"developmentClient\": true, \"distribution\": \"internal\" },</code><br><code>    \"preview\": { \"distribution\": \"internal\" },</code><br><code>    \"production\": { \"distribution\": \"store\" }</code><br><code>  },</code><br><code>  \"submit\": { \"production\": {} }</code><br><code>}</code><br>Profiles are referenced via <code>--profile</code> flag. Each profile can set <code>ios.image</code>, <code>android.buildType</code>, env vars, caching, and more.",
  "expo::eas")

c("EAS",
  "What are the three common <b>build profiles</b> in EAS?",
  "<b>1. Development</b> — <code>developmentClient: true</code>, <code>distribution: 'internal'</code>. Produces a debug build with <code>expo-dev-client</code> for daily development.<br><b>2. Preview</b> — <code>distribution: 'internal'</code>. Production-like build distributed to testers via EAS internal distribution (no TestFlight needed).<br><b>3. Production</b> — <code>distribution: 'store'</code>. Ready for App Store / Google Play submission. Uses release keystore and production certs.<br>Run with <code>eas build --profile preview</code>.",
  "expo::eas")

c("EAS",
  "What is <b>EAS Submit</b> and how does it work?",
  "EAS Submit uploads your built binary to app stores:<br><code>eas submit --platform ios</code> — upload to App Store Connect<br><code>eas submit --platform android</code> — upload to Google Play Console<br>Requires app store credentials configured via <code>eas credentials</code>. Handles:<br>• App Store Connect API key or Apple ID login<br>• Google Play service account JSON<br>• Automatic version bump handling<br>• Release notes management<br>Can be combined: <code>eas build --auto-submit</code> (build + submit in one command).",
  "expo::eas")

c("EAS",
  "What is <b>EAS Update</b>?",
  "EAS Update is Expo's <b>over-the-air update hosting service</b>. It's the cloud backend for <code>expo-updates</code>. Commands:<br>• <code>eas update --branch production --message \"Fixed crash\"</code><br>• <code>eas update:list</code> — view update history<br>• <code>eas update:rollback</code> — revert to a previous update<br>• <code>eas channel:create staging</code> — create a distribution channel<br><b>Channels</b> are named pointers (like git branches) that point to a specific update. <b>Branches</b> are update groupings. The app binary is linked to a channel at build time.",
  "expo::eas")

c("EAS",
  "What is the difference between <b>EAS Update channels and branches</b>?",
  "<b>Branches</b> are Git-like named sequences of updates. You publish to a branch:<br><code>eas update --branch staging</code><br><br><b>Channels</b> are aliases that point to a branch. Your build is linked to a channel at build time. This decouples build configuration from update routing. Example flow:<br>1. Build links to \"production\" channel<br>2. \"production\" channel points to \"v1\" branch<br>3. Publish updates to \"v1\" branch<br>4. When v2 ships, repoint channel to \"v2\" branch<br>This enables staged rollouts and A/B testing.",
  "expo::eas")

c("EAS",
  "What is <b>EAS Metadata</b> and what does it manage?",
  "EAS Metadata (still evolving, part of EAS ecosystem) manages store listing content in code:<br>• App Store Connect metadata (description, keywords, screenshots)<br>• Google Play Console metadata (title, short description, feature graphic)<br>• Upload screenshots in multiple device sizes<br>• Localized metadata for multiple languages<br>Controlled via <code>eas.json</code> and/or <code>store.config.json</code>. Enables storing app store metadata in version control alongside your code.<br>Use <code>eas metadata:push</code> to upload to stores.",
  "expo::eas")

c("EAS",
  "What are <b>EAS Secrets</b> and how do you manage them?",
  "EAS Secrets are <b>encrypted environment variables</b> stored on Expo's servers and injected only during EAS Build. Commands:<br>• <code>eas secret:create --name API_KEY --value \"sk-abc123\"</code><br>• <code>eas secret:list</code><br>• <code>eas secret:delete API_KEY</code><br><br>Secrets are available as environment variables during build. They are <b>NOT</b> included in the binary. Use <code>EXPO_PUBLIC_</code> prefix for values that should be readable at app runtime (baked into the JS bundle — use only for non-sensitive config).",
  "expo::eas")

c("EAS",
  "How does EAS support <b>monorepos</b>?",
  "EAS Build supports monorepos (Turborepo, Nx, pnpm workspaces) with configuration in <code>eas.json</code>. Key settings:<br>• <code>\"projectRoot\": \"apps/mobile\"</code> — point to the Expo project location<br>• <code>\"NPM_TOKEN\"</code> secret for private packages<br>• Automatic workspace-aware install via <code>npm install</code> or <code>pnpm install</code><br>• Build caching across project boundaries via <code>\"cache\": { \"key\": \"...\" }</code><br>Best practice: define EAS config in the root <code>eas.json</code> with per-app profiles.",
  "expo::eas")

c("EAS",
  "What is <b>build caching</b> in EAS?",
  "EAS Build caches <code>node_modules</code>, CocoaPods, and Gradle dependencies between builds to speed up subsequent builds. Configure in <code>eas.json</code>:<br><code>\"cache\": {</code><br><code>  \"disabled\": false,</code><br><code>  \"key\": \"v1\",</code><br><code>  \"cacheDefaultPaths\": true</code><br><code>}</code><br>Change the <code>key</code> to invalidate the cache. Caching is enabled by default and can dramatically reduce build times from ~15 minutes to ~2-5 minutes for incremental changes.",
  "expo::eas")

c("EAS",
  "What is the difference between <b>local builds</b> and <b>remote builds</b> in EAS?",
  "<b>Remote builds</b> (<code>eas build</code>) run on Expo's cloud servers — no local Xcode/Android Studio needed. Build result is downloadable.<br><b>Local builds</b> (<code>eas build --local</code>) run on your own machine using your local Xcode/Android Studio. Useful for:<br>• Debugging build failures locally<br>• Faster iteration (no upload queue)<br>• Working offline<br>• Using local certificates and provisioning profiles<br>Local builds require the same native toolchain as bare workflow.",
  "expo::eas")

c("EAS",
  "What is <code>eas build --auto-submit</code>?",
  "<code>eas build --auto-submit</code> tells EAS to automatically submit the resulting binary to app stores after a successful build. Combine with a profile:<br><code>eas build --platform all --profile production --auto-submit</code><br>This creates a <b>fully automated CI pipeline</b>: build → upload to TestFlight / Google Play → ready for review. No manual steps between build and submission.",
  "expo::eas")

c("EAS",
  "What are <b>EAS Build hooks</b>?",
  "Build hooks let you inject custom scripts into the EAS Build pipeline. Configured in <code>eas.json</code>:<br><code>\"build\": {</code><br><code>  \"production\": {</code><br><code>    \"hooks\": {</code><br><code>      \"prebuild\": \"echo 'Run before expo prebuild'\",</code><br><code>      \"postinstall\": \"node ./scripts/setup.js\",</code><br><code>      \"postbuild\": \"curl -X POST $SLACK_WEBHOOK\"</code><br><code>    }</code><br><code>  }</code><br><code>}</code><br>Available hooks: <code>preinstall</code>, <code>postinstall</code>, <code>prebuild</code>, <code>postbuild</code>. Use for code generation, notifications, or cleanup steps.",
  "expo::eas")

c("EAS",
  "How do you <b>log in</b> to EAS?",
  "<code>eas login</code><br><br>Authenticates with your Expo account (email/password or GitHub). After login, commands like <code>eas build</code>, <code>eas submit</code>, and <code>eas update</code> are available. Check status with <code>eas whoami</code>. Log out with <code>eas logout</code>. The session token is stored in <code>~/.expo/state.json</code>.",
  "expo::eas")

c("EAS",
  "What is <b>internal distribution</b> in EAS Build?",
  "Internal distribution (<code>\"distribution\": \"internal\"</code> in <code>eas.json</code>) makes your build available via a <b>QR code and download link</b> after the build completes. Testers don't need TestFlight or Play Console access. On iOS, the device UDID must be registered in your Apple Developer account (EAS can handle this: <code>eas device:create</code>). Ideal for preview and development builds shared with your team.",
  "expo::eas")

# ═══════════════════════════════════════════
# L2: DEVELOPMENT WORKFLOW
# ═══════════════════════════════════════════

c("DevWorkflow",
  "When should you use <b>Expo Go</b> vs a <b>development build</b>?",
  "Use <b>Expo Go</b> when:<br>• You're prototyping or learning<br>• You only use built-in Expo SDK modules<br>• You don't need custom native modules, Bluetooth, or background services<br>• You want zero-config instant testing<br><br>Use a <b>development build</b> when:<br>• You have custom native modules or config plugins<br>• You need <code>expo-dev-client</code> launcher<br>• You use Bluetooth (<code>expo-bluetooth</code>) or background services<br>• Your app requires a specific native SDK version<br>• You're preparing for production",
  "expo::dev-workflow")

c("DevWorkflow",
  "What is <code>expo-dev-client</code> and how does it improve the dev experience?",
  "<code>expo-dev-client</code> adds a development UI to your app:<br>• <b>Launcher screen</b>: choose which dev server to connect to (localhost, tunnel, custom URL)<br>• <b>Dev Menu</b>: shake gesture or three-finger long-press to access reload, performance monitor, element inspector<br>• <b>Extensible</b>: third-party dev plugins can add menu items<br>Install: <code>npx expo install expo-dev-client</code><br>Build with: <code>eas build --profile development</code> or <code>npx expo run:ios --configuration Debug</code><br>Now the <b>recommended</b> dev approach for most Expo projects.",
  "expo::dev-workflow")

c("DevWorkflow",
  "How does <b>Fast Refresh</b> work in Expo?",
  "Fast Refresh is a React Native feature enabled by default in Expo. When you save a file:<br>1. Metro detects the change<br>2. The changed module is hot-replaced<br>3. React state is <b>preserved</b> (for function components with hooks)<br>4. UI updates immediately without losing scroll position or form input<br>• Class components lose state and remount<br>• Syntax errors show a full-screen red box until fixed<br>• Controlled by the <b>Dev Menu</b> toggle<br>It's powered by React Refresh, the same mechanism used in React web.",
  "expo::dev-workflow")

c("DevWorkflow",
  "What debugging tools are available for Expo?",
  "<b>React Native DevTools</b> (SDK 51+) — Hermes-compatible debugger (press <code>j</code> in terminal, or Dev Menu → Open DevTools). Replaces Flipper.<br><b>React DevTools</b> — inspect React component tree (via Dev Menu).<br><b>Performance Monitor</b> — toggle FPS/RAM overlay via Dev Menu.<br><b>Element Inspector</b> — inspect component layout/ styles (Dev Menu → Toggle Element Inspector).<br><b>Reactotron</b> — third-party desktop app for logging, state inspection, and benchmarking.<br><b>Flipper is deprecated</b> for React Native 0.73+ and Expo SDK 50+. Use React Native DevTools instead.",
  "expo::dev-workflow")

c("DevWorkflow",
  "What is <b>React Native DevTools</b> and how do you open it in Expo?",
  "React Native DevTools is the <b>new debugging tool</b> (replacing Flipper, Hermes-compatible) integrated into React Native 0.73+ and Expo SDK 50+. Features:<br>• JavaScript debugger (breakpoints, watch, call stack)<br>• Console logging<br>• React component tree inspection<br>• Network request monitoring<br>Open it by:<br>1. Press <code>j</code> in the terminal running <code>npx expo start</code><br>2. OR: Dev Menu → Open DevTools<br>3. Opens in Chrome/Edge browser at <code>localhost:8081</code>",
  "expo::dev-workflow")

c("DevWorkflow",
  "How do you set up <b>testing</b> in an Expo project?",
  "<b>1. Unit tests:</b> Use <code>jest</code> with the <code>jest-expo</code> preset:<br><code>\"preset\": \"jest-expo\"</code> in <code>jest.config.js</code><br>This configures mocks for all Expo modules, makes <code>expo-font</code>, <code>expo-asset</code>, etc. work in Jest.<br><b>2. Component tests:</b> Use <code>@testing-library/react-native</code>:<br><code>import { render, fireEvent } from '@testing-library/react-native';</code><br><b>3. E2E tests:</b> Use <code>detox</code> or <code>maestro</code> with a development build. Run: <code>npx jest</code> or <code>npx expo start --dev-client &amp;&amp; npx detox test</code>.",
  "expo::dev-workflow")

c("DevWorkflow",
  "What is <b>jest-expo</b>?",
  "<code>jest-expo</code> is a <b>Jest preset</b> tailored for Expo projects. It provides:<br>• Automatic mocks for all Expo SDK modules (<code>expo-camera</code>, <code>expo-location</code>, etc.)<br>• Metro-compatible module resolution<br>• Asset file transforms (<code>.png</code>, <code>.jpg</code>, <code>.ttf</code>)<br>• <code>react-native</code> testing environment<br>Add to <code>package.json</code>:<br><code>\"jest\": { \"preset\": \"jest-expo\" }</code><br>Or create <code>jest.config.js</code> with <code>preset: 'jest-expo'</code>.",
  "expo::dev-workflow")

c("DevWorkflow",
  "How do <b>environment variables</b> with <code>EXPO_PUBLIC_</code> prefix work?",
  "Any environment variable starting with <code>EXPO_PUBLIC_</code> is <b>inlined at build time</b> into your JavaScript bundle and accessible at runtime:<br><code>const apiUrl = process.env.EXPO_PUBLIC_API_URL;</code><br><br>Set them:<br>• In <code>.env</code> files (auto-loaded by Metro)<br>• Via command line: <code>EXPO_PUBLIC_API_URL=https://api.dev npx expo start</code><br>• In CI: set as environment variables before build<br>Variables <b>without</b> the prefix are stripped from the bundle and only available during build. This is secure — only explicitly public values reach the client.",
  "expo::dev-workflow")

c("DevWorkflow",
  "What are <b>app variants</b> in Expo?",
  "App variants are different configurations of the same app. Common variants:<br><b>Development</b> — debug build with <code>expo-dev-client</code>, dev API endpoints, verbose logging<br><b>Preview</b> — production-like build with staging API, distributed to internal testers<br><b>Production</b> — final build with production API, crash reporting, distribution via app stores<br>Configure variants via <b>EAS build profiles</b> in <code>eas.json</code> and <b>app.config.ts</b> dynamic configuration that reads the profile name to set API URLs, feature flags, and bundle identifiers.",
  "expo::dev-workflow")

c("DevWorkflow",
  "How do you create a <b>development build for iOS</b>?",
  "<code>eas build --profile development --platform ios</code><br><br>Prerequisites:<br>1. Apple Developer account ($99/year)<br>2. <code>expo-dev-client</code> installed in your project<br>3. <code>\"developmentClient\": true</code> in <code>eas.json</code> development profile<br>4. Register your iOS device UDID: <code>eas device:create</code><br>The build produces an <code>.ipa</code> signed for development. Install via QR code or direct download link. Open the app, enter your Metro server URL, and start developing with Fast Refresh and custom native modules.",
  "expo::dev-workflow")

c("DevWorkflow",
  "What is <b>deep link debugging</b> and how do you test deep links in Expo?",
  "Test deep links in Expo:<br>• <b>iOS Simulator</b>: <code>npx uri-scheme open \"myapp://profile/123\" --ios</code><br>• <b>Android Emulator</b>: <code>npx uri-scheme open \"myapp://profile/123\" --android</code><br>• Or use <code>xcrun simctl openurl booted \"myapp://profile\"</code> (iOS)<br>• Or <code>adb shell am start -W -a android.intent.action.VIEW -d \"myapp://profile\"</code> (Android)<br><br>The <code>uri-scheme</code> package (by Expo) simplifies this. Install: <code>npx expo install uri-scheme</code>. Note: custom URL schemes may not work in Expo Go — test with a development build.",
  "expo::dev-workflow")

c("DevWorkflow",
  "What is <b>config plugin</b> in Expo and how do you create one?",
  "A config plugin is a JavaScript/TypeScript function that modifies the native <code>ios/</code> and <code>android/</code> projects declaratively during <code>prebuild</code>. Create one:<br><br><code>// withPlugins.js</code><br><code>const { withPlugins } = require('@expo/config-plugins');</code><br><code>module.exports = (config) => {</code><br><code>  // Modify config.ios, config.android</code><br><code>  return config;</code><br><code>};</code><br><br>Add to <code>app.json</code> <code>plugins</code> array: <code>[\"./withPlugins\"]</code>. Plugins can add permissions, modify Info.plist, AndroidManifest.xml, Podfile, build.gradle, and more. Many expo-* packages ship their own config plugins.",
  "expo::dev-workflow")

# ═══════════════════════════════════════════
# L4: GOTCHAS
# ═══════════════════════════════════════════

c("Gotchas",
  "What causes <b>SDK version mismatch</b> errors and how do you fix them?",
  "SDK version mismatches happen when some <code>expo-*</code> packages are installed for a different SDK version than your <code>expo</code> core package. Symptom: red screen on launch, native crashes, or Metro errors. Fix:<br><code>npx expo-doctor</code> (diagnose)<br><code>npx expo install --fix</code> (auto-correct)<br>Or manually: ensure all <code>expo-*</code> packages in <code>node_modules</code> match your SDK version.",
  "expo::gotchas")

c("Gotchas",
  "What are the <b>Expo Go limitations</b> you must know?",
  "Expo Go cannot use:<br>• Custom native modules (any npm package with native code not in the Expo SDK)<br>• Bluetooth (<code>expo-bluetooth</code>)<br>• Background services (background fetch, location, audio — limited)<br>• In-app purchases (<code>expo-in-app-purchases</code>)<br>• Custom URL schemes may not work reliably<br>• Some push notification features<br>• AR/VR libraries<br><b>Fix:</b> Use a development build with <code>expo-dev-client</code> instead.",
  "expo::gotchas")

c("Gotchas",
  "Why should you use <code>expo install</code> instead of <code>npm install</code>?",
  "<code>npm install expo-camera</code> may install a version that's <b>incompatible</b> with your SDK version, causing crashes. <code>npx expo install expo-camera</code> queries Expo's registry for the exact compatible version. This is the #1 cause of SDK version mismatch errors. Always use <code>npx expo install</code> for <code>expo-*</code> packages, <code>react-native</code>, <code>react</code>, and <code>@react-navigation/*</code>.",
  "expo::gotchas")

c("Gotchas",
  "What <b>Metro bundler cache issues</b> can occur and how do you fix them?",
  "Stale Metro cache can cause:<br>• Old code running despite changes<br>• \"Unable to resolve module\" for modules that exist<br>• Babel config changes not taking effect<br>• Assets not updating<br>Fix: <code>npx expo start -c</code> (clear cache and restart) or <code>rm -rf node_modules/.cache</code>. If persistent, also clear the Metro cache dir: <code>rm -rf $TMPDIR/metro-*</code> and <code>rm -rf $TMPDIR/haste-*</code>.",
  "expo::gotchas")

c("Gotchas",
  "Why doesn't <b>deep linking</b> work with a custom URL scheme in Expo Go?",
  "Expo Go has its own URL scheme (<code>exp://</code>) and does not support custom schemes from <code>app.json</code>. Deep links with <code>myapp://profile</code> fail in Expo Go. Solutions:<br>1. Use a <b>development build</b> (custom scheme works there)<br>2. Use <code>exp://</code> with the Expo Go URL format during development<br>3. Test universal links on a physical device with a development build<br>For production, deep linking works normally in standalone builds.",
  "expo::gotchas")

c("Gotchas",
  "Why does <b>plugin ordering</b> matter in <code>app.json</code>?",
  "Config plugins in the <code>plugins</code> array are applied <b>sequentially</b> during <code>npx expo prebuild</code>. If plugin A modifies a file that plugin B also modifies, ordering determines the final result. Example: <code>expo-camera</code> must come before <code>expo-barcode-scanner</code> because both modify the same <code>Info.plist</code> key. Always put more foundational plugins first, app-specific plugins last.",
  "expo::gotchas")

c("Gotchas",
  "Why is <code>react-native-safe-area-context</code> required in Expo projects?",
  "Expo apps use <code>react-native-safe-area-context</code> to handle <b>safe area insets</b> (notch, dynamic island, home indicator, status bar). It's included by default in Expo Router templates. If you get layout issues (content hidden behind notch/status bar), ensure:<br>1. It's installed: <code>npx expo install react-native-safe-area-context</code><br>2. <code>SafeAreaProvider</code> wraps your root layout<br>3. Use <code>SafeAreaView</code> from <code>react-native-safe-area-context</code> (not React Native's version)",
  "expo::gotchas")

c("Gotchas",
  "What are common <b>iOS Simulator vs physical device differences</b>?",
  "<b>Simulator</b>:<br>• Based on x86_64/arm64 Mac architecture<br>• Some hardware APIs return mock data (camera, accelerometer)<br>• Push notifications don't work (no APNs)<br>• Keychain access always succeeds<br>• Faster networking (localhost)<br><b>Physical device</b>:<br>• Real ARM64 iOS<br>• Actual camera, sensors, biometric auth<br>• Push notifications work<br>• Keychain requires proper entitlements<br>• Some gesture behaviors differ<br>Always test on a physical device before shipping.",
  "expo::gotchas")

c("Gotchas",
  "What are the <b>Android permissions</b> gotchas with Expo?",
  "Android permissions must be configured in <code>app.json</code> via config plugins, NOT directly in <code>AndroidManifest.xml</code> (managed workflow). Example:<br><code>\"plugins\": [</code><br><code>  [\"expo-camera\", { \"cameraPermission\": \"Allow $(PRODUCT_NAME) to access camera.\" }]</code><br><code>]</code><br>Each <code>expo-*</code> module documents which plugin config it needs. Some permissions also require <b>runtime requests</b> via <code>useCameraPermissions()</code> or <code>PermissionsAndroid</code>. Mismatch between declared and requested permissions causes silent failures.",
  "expo::gotchas")

c("Gotchas",
  "What are <b>Hermes engine</b> gotchas in Expo?",
  "Hermes is the default JS engine in Expo SDK 50+. Gotchas:<br>• <b>No Remote JS Debugging</b> in Chrome (Hermes doesn't support it). Use React Native DevTools instead<br>• <b>Intl API</b> — some locales need polyfill (<code>intl</code> package)<br>• <b>Source maps</b> must be Hermes-compatible for crash reporting<br>• <b>Proxy support</b> is limited compared to JSC<br>• <b>Memory usage</b> is lower but GC behavior differs<br>To disable Hermes, set <code>\"jsEngine\": \"jsc\"</code> in <code>app.json</code> under <code>expo</code>. Hermes is <b>required</b> on iOS for apps > 128 MB (App Store requirement).",
  "expo::gotchas")

c("Gotchas",
  "What is the <b>New Architecture</b> (Fabric / TurboModules) compatibility story with Expo?",
  "Expo SDK 51+ supports the React Native New Architecture (Fabric renderer, TurboModules, JSI). To enable:<br><code>\"plugins\": [[\"expo-build-properties\", { \"newArchEnabled\": true }]]</code><br>Gotchas:<br>• Not all expo-* modules are fully New Architecture compatible yet<br>• Some third-party native modules break<br>• Debugging tooling is different (no bridge-based debugging)<br>• Performance improvements are most noticeable in animation-heavy apps<br>• Expo Go does NOT support New Architecture — use a development build<br>Test thoroughly before enabling in production.",
  "expo::gotchas")

c("Gotchas",
  "What are <b>EAS Update rollback</b> gotchas?",
  "When rolling back an EAS Update:<br>• Rollback doesn't delete the bad update — it points the branch to a previous update<br>• Devices that already downloaded the bad update won't switch until next launch<br>• <code>eas update:rollback</code> requires knowing the update ID<br>• Channel-based rollbacks affect only builds linked to that channel<br>• If you shipped a binary with a crash in native code (not JS), an OTA rollback won't fix it — you need a new build<br>• Test updates on a staging channel before promoting to production",
  "expo::gotchas")

c("Gotchas",
  "What are <b><code>@expo/vector-icons</code></b> font loading gotchas?",
  "<code>@expo/vector-icons</code> is bundled with Expo but may require font loading for custom icon sets. Gotchas:<br>• Icon fonts are loaded lazily — you may see a flash of missing icons<br>• Use <code>useFonts</code> from <code>expo-font</code> to preload icon fonts<br>• Some icon sets (MaterialCommunityIcons) are large and may cause initial load delay<br>• In web, icon fonts may render differently or not load without proper CSS<br>• For custom icons, use <code>expo-symbols</code> (SF Symbols on iOS) or a custom font file with <code>createIconSet</code>",
  "expo::gotchas")

c("Gotchas",
  "Why does <b>bundling/web performance</b> sometimes degrade?",
  "Common causes:<br>• Large <code>node_modules</code> being bundled unnecessarily — use <code>expo/metro-config</code> and configure <code>blockList</code><br>• Too many dynamic <code>require()</code> calls — Metro can't tree-shake them<br>• Uncompressed images/assets — use <code>expo-optimize</code> or manually compress<br>• Not using the Hermes engine's precompilation features<br>• Debug builds are slower than production — test perf on release builds<br>• Large SVG icon sets imported entirely rather than as individual icons<br>Fix: use <code>npx expo start --minify</code> for production-like bundling in dev, and run <code>npx expo-optimize</code> to compress assets.",
  "expo::gotchas")

# ═══════════════════════════════════════════
# L5: EXPERT
# ═══════════════════════════════════════════

c("Expert",
  "When should you <b>eject from managed to bare workflow</b>?",
  "Eject when you need to:<br>• Write custom native UI components (SwiftUI/Compose embedded in RN views)<br>• Integrate third-party native SDKs without Expo config plugin support<br>• Access iOS APIs not covered by Expo (WidgetKit, WatchOS, CarPlay, App Clips)<br>• Fine-tune native build settings beyond what config plugins allow<br>• Custom native threading/performance optimization<br><b>But:</b> many use cases previously requiring eject are now handled by config plugins and the Expo Modules API — evaluate these first.",
  "expo::expert")

c("Expert",
  "Expo Router vs React Navigation standalone — when to use each?",
  "Use <b>Expo Router</b> if:<br>• You're on Expo SDK 49+<br>• You want file-based routing (like Next.js)<br>• You need deep linking without manual config<br>• You're building a universal app (web + native)<br>• You want typed routes out of the box<br><br>Use <b>React Navigation</b> standalone if:<br>• You're on bare workflow without Expo Router<br>• You need very custom navigator layouts not expressible in files<br>• You're on an older codebase migrating incrementally<br>• You need to control the navigation container directly<br>Expo Router is built on React Navigation — it's not a replacement but a higher-level API.",
  "expo::expert")

c("Expert",
  "EAS vs Fastlane for CI/CD — what's the trade-off?",
  "<b>EAS:</b><br>• Zero config cloud builds<br>• Managed signing and provisioning<br>• Built-in OTA update deployment<br>• Tight Expo SDK integration<br>• Less flexible for non-Expo customizations<br>• Costs at scale (paid EAS plans)<br><b>Fastlane:</b><br>• Full control over the build pipeline<br>• Works with any React Native project (Expo or bare)<br>• Huge plugin ecosystem (screenshots, Slack, TestFlight metadata)<br>• Requires self-hosted CI (GitHub Actions, CircleCI, etc.) or a Mac Mini<br>• Steep learning curve for match/cert/sigh<br>Common pattern: use <b>EAS Build for builds, Fastlane for submission automation</b>.",
  "expo::expert")

c("Expert",
  "When should you use <code>expo-updates</code> vs CodePush?",
  "Use <b><code>expo-updates</code></b> (first-party):<br>• You're on Expo SDK 49+<br>• You want deep EAS integration (channels, branches, rollbacks)<br>• You need asset updates (images, fonts) not just JS<br>• You want predictable release management<br>• Zero additional setup in Expo projects<br><br>Use <b>CodePush</b> (third-party, App Center):<br>• You're on bare workflow or older React Native<br>• You need mandatory update enforcement<br>• You want update targeting by app version/staging ring<br>• You're already on App Center ecosystem<br>Note: Microsoft is sunsetting App Center (March 2025) — <code>expo-updates</code> is the future-proof choice.",
  "expo::expert")

c("Expert",
  "What's the best <b>Expo SDK upgrade strategy</b>?",
  "Two approaches:<br><b>1. Always upgrade</b> (recommended for most teams):<br>• Stay on the latest SDK within 2–4 weeks of release<br>• Run <code>npx expo-doctor</code> and <code>npx expo install --fix</code> regularly<br>• Smaller, incremental upgrades are easier than big jumps<br>• Get latest React Native features and performance<br><b>2. LTS-style</b> (teams with long QA cycles):<br>• Stick to a stable SDK for 6–9 months<br>• Upgrade only when you need a new feature or security fix<br>• Risk: batching upgrades across multiple SDK versions is painful<br>Expo doesn't officially offer LTS versions, but the quarterly cycle means you're never more than 3 months behind.",
  "expo::expert")

c("Expert",
  "When is Expo <b>NOT the right choice</b>?",
  "Avoid Expo for:<br>• <b>Games</b> (Unity, Unreal, or raw Metal/Vulkan) — use react-native-game-engine at best, but Expo's hot-reload and managed overhead aren't ideal<br>• <b>AR/VR</b> — ARKit/ARCore are partially accessible but complex setups (ViroReact, expo-three) are fragile on managed workflow<br>• <b>Heavy native integrations</b> — if your app wraps a native C++ library 1:1 with a thin RN layer<br>• <b>WatchOS/iMessage Apps</b> — no Expo support for companion apps<br>• <b>Highly regulated industries</b> with custom cert pinning, offline-first, and audited native code — bare RN gives more transparency<br>• <b>Existing large native apps</b> adding RN incrementally — Brownfield RN is harder with Expo",
  "expo::expert")

c("Expert",
  "How do you set up a <b>monorepo with Expo</b>?",
  "Use <b>Turborepo</b> (recommended) or Nx with pnpm workspaces:<br>1. Root <code>package.json</code> with <code>workspaces</code> config<br>2. <code>apps/mobile/</code> — the Expo project<br>3. <code>packages/shared/</code> — shared types, constants, API client<br>4. <code>packages/ui/</code> — shared components<br>Configure:<br>• Root <code>eas.json</code> with <code>\"projectRoot\": \"apps/mobile\"</code><br>• Metro config in the Expo project must watch workspace packages: add <code>watchFolders</code><br>• Use <code>turbo.json</code> for build pipeline orchestration<br>• <code>pnpm</code> works best for strict dependency resolution",
  "expo::expert")

c("Expert",
  "What are the <b>CSS/styling options</b> in Expo?",
  "<b>1. StyleSheet</b> (built-in, no dependencies):<br>• React Native's default styling API<br>• No build step, works everywhere<br>• Verbose, no theming built-in<br><br><b>2. NativeWind</b> (Tailwind CSS for RN):<br>• <code>className=\"bg-blue-500 p-4\"</code><br>• Works with Expo Router<br>• Requires Babel plugin + <code>tailwind.config.js</code><br>• Great DX if you know Tailwind<br>• Faster to write, but adds build complexity<br><br><b>3. Tamagui</b>:<br>• Styled component + design system<br>• Built-in theming, animations, variants<br>• Optimizing compiler for production<br>• Larger learning curve, full-featured design system<br>• Best for complex design needs<br><b>Recommendation:</b> StyleSheet for simple apps, NativeWind for Tailwind fans, Tamagui for design-system-heavy apps.",
  "expo::expert")

c("Expert",
  "How do <b>config plugins</b> work under the hood?",
  "Config plugins are <b>modifier functions</b> applied as a pipeline during <code>npx expo prebuild</code>. Each plugin receives the Expo config object and returns a modified copy. Under the hood:<br>1. Expo reads <code>app.json</code> / <code>app.config.ts</code> into a config object<br>2. The <b>mod-compiler</b> runs each plugin in the <code>plugins</code> array sequentially<br>3. Plugins use <b>mods</b> (modifier interfaces) to mutate specific native files: <code>withInfoPlist</code>, <code>withAndroidManifest</code>, <code>withGradleProperties</code>, <code>withPodfile</code>, <code>withXcodeProject</code>, <code>withEntitlementsPlist</code><br>4. The final config is written to native files using <code>@expo/config-plugins</code><br>This is how <code>expo-camera</code> adds camera permission to <code>Info.plist</code> without a native project on disk.",
  "expo::expert")

c("Expert",
  "What are the <b>Expo Dev Tools plugins</b>?",
  "Dev Tools plugins extend the <b>in-app Dev Menu</b> in development builds. Create one:<br><code>import { DevToolsPlugin } from 'expo-dev-client';</code><br><code>DevToolsPlugin.register({ name: 'MyPlugin', render: () => &lt;MyPluginUI /&gt; });</code><br><br>Plugins appear as items in the Dev Menu. Popular examples: React Navigation devtools, Redux devtools, Apollo Client inspector. They enable in-app debugging experiences without external desktop tools.",
  "expo::expert")

c("Expert",
  "What is <code>expo-gl</code> / <code>expo-three</code> and when would you use them?",
  "<code>expo-gl</code> provides an OpenGL ES context in Expo. <code>expo-three</code> is a Three.js renderer that uses it. Use cases:<br>• 3D product viewers<br>• Simple 3D scenes and animations<br>• Data visualization in 3D<br>• AR experiences (with <code>expo-camera</code> as camera feed)<br>Limitations:<br>• Not GPU-optimized for complex games<br>• No Metal/Vulkan backend — OpenGL only<br>• Performance is not game-ready<br>• Better suited for lightweight 3D than full game engines<br>For heavy 3D/games, use Unity or a bare RN project with native rendering.",
  "expo::expert")

c("Expert",
  "What's the state of <b>React Server Components (RSC)</b> in Expo?",
  "RSC in Expo is <b>experimental</b> (as of SDK 51/52). Expo Router can render RSC on the server and stream them to the client. This enables:<br>• Server-rendered content in native apps<br>• Data fetching on the server before render<br>• Reduced client-side JavaScript<br>• Hybrid server/client component trees<br>Currently experimental and not recommended for production. Part of the broader Expo + React Server Components exploration. Requires Metro config changes and a server runtime. Track the <code>expo-router</code> and <code>@expo/server</code> packages for updates.",
  "expo::expert")

c("Expert",
  "How do you implement <b>local-first</b> with Expo?",
  "Local-first architecture with Expo uses a local database as the primary data source, syncing to a server. Options:<br>• <code>expo-sqlite</code> (SDK 51+) — synchronous SQLite, great for simple local storage<br>• <code>@nozbe/watermelondb</code> — reactive ORM on top of SQLite, designed for local-first<br>• <code>drizzle-orm</code> + <code>expo-sqlite</code> — type-safe SQL<br>• <code>@op-engineering/op-sqlite</code> — high-performance SQLite with JSI<br>Pattern: write to local DB first, sync to server in background, use CRDTs or sync engines for conflict resolution. Combine with <code>expo-background-fetch</code> for background sync.",
  "expo::expert")

c("Expert",
  "How do you write a <b>custom native module</b> with the Expo Modules API?",
  "1. <code>npx create-expo-module my-module</code> to scaffold<br>2. Write the module in <b>Swift</b> (iOS) and <b>Kotlin</b> (Android) using the declarative API<br>3. Define <code>expo-module.config.json</code> with module metadata<br>4. Import and use in JavaScript: <code>import MyModule from 'my-module'</code><br><br>Example (Swift):<br><code>public class MyModule: Module {</code><br><code>  public func definition() -> ModuleDefinition {</code><br><code>    Name(\"MyModule\")</code><br><code>    Function(\"greet\") { (name: String) in</code><br><code>      return \"Hello, \\(name)!\"</code><br><code>    }</code><br><code>  }</code><br><code>}</code><br>The JS binding is auto-generated via codegen. Module is consumed in a development build or production build, NOT Expo Go.",
  "expo::expert")

c("Expert",
  "What is the <b>Expo release cycle</b> and how should teams plan around it?",
  "New Expo SDK versions ship approximately <b>quarterly</b>, following the React Native release cadence by ~2–4 weeks. The cycle:<br>• React Native releases RC → Expo team tests and adapts<br>• Expo SDK beta available (opt-in via <code>expo@next</code>)<br>• Stable Expo SDK release (typically includes new React Native major/minor)<br>• SDK version is supported with critical fixes for ~1 year<br>Planning tips:<br>• Subscribe to the <b>Expo Changelog</b> (blog.expo.dev)<br>• Test betas when they align with your timeline<br>• Plan upgrades as part of regular sprint maintenance (not one-off fire drills)<br>• Use <code>expo-doctor</code> pre- and post-upgrade",
  "expo::expert")

c("Expert",
  "How does <b>OTA update compatibility</b> work across SDK versions?",
  "OTA updates are <b>JavaScript-bundle-scoped</b> — they cannot change native code. This means:<br>• An update published with SDK 51 can run on an SDK 51 binary<br>• An update CANNOT run on an SDK 50 binary (or vice versa)<br>• The runtime version in app config enforces this: <code>\"runtimeVersion\": \"1.0.0\"</code><br>• Changing the <code>runtimeVersion</code> in <code>app.json</code> forces a new build (protects against incompatible updates)<br>• Set <code>\"runtimeVersion\": { \"policy\": \"appVersion\" }</code> to auto-bind to <code>version</code> in <code>app.json</code><br>Best practice: bump <code>runtimeVersion</code> whenever native code changes.",
  "expo::expert")

c("Expert",
  "What is <code>expo-build-properties</code> plugin and what does it configure?",
  "<code>expo-build-properties</code> is a config plugin for setting <b>native build properties</b> from <code>app.json</code>. Key settings:<br>• <code>\"newArchEnabled\": true</code> — enable Fabric/TurboModules<br>• <code>\"useFrameworks\": \"static\"</code> — iOS static framework linking<br>• <code>\"android.kotlinVersion\"</code> — set Kotlin version<br>• <code>\"android.compileSdkVersion\"</code><br>• <code>\"ios.deploymentTarget\"</code><br>• <code>\"ios.useFrameworks\"</code> — use_frameworks! in Podfile<br>Add it: <code>\"plugins\": [[\"expo-build-properties\", { \"newArchEnabled\": true }]]</code>. These were previously only configurable by ejecting/modifying native files directly.",
  "expo::expert")

c("Expert",
  "What are <b>fingerprints</b> in EAS (runtime version policy)?",
  "Expo <b>fingerprints</b> create a hash of your native project configuration (SDK version, native module versions, config plugin output, etc.). This hash is used as the <code>runtimeVersion</code> to ensure OTA updates are only served to compatible builds. If any native dependency changes, the fingerprint changes, preventing incompatible updates from being delivered. Set in <code>app.json</code>:<br><code>\"runtimeVersion\": { \"policy\": \"fingerprint\" }</code><br>This is the safest policy — fully automatic compatibility enforcement.",
  "expo::expert")

c("Expert",
  "What is <code>@expo/server</code> and when is it used?",
  "<code>@expo/server</code> is a package that enables <b>server-side rendering</b> (SSR) of Expo Router apps. It provides:<br>• A Node.js server runtime for Expo Router<br>• Static site generation (SSG) capabilities<br>• Server-side data fetching patterns<br>• Integration with React Server Components (experimental)<br>Used when you want to render Expo Router pages on a server before sending to the client — improves initial load time and SEO. Part of the universal Expo vision where the same code runs on native, web, and server.",
  "expo::expert")

c("Expert",
  "How do you handle <b>offline mode</b> in Expo?",
  "Offline-first strategy for Expo apps:<br>1. <b>Local storage</b>: <code>expo-sqlite</code> / WatermelonDB for structured data, <code>expo-file-system</code> for files<br>2. <b>Network detection</b>: <code>@react-native-community/netinfo</code> to detect connectivity changes<br>3. <b>Sync queue</b>: Store mutations locally, replay when online<br>4. <b>Conflict resolution</b>: CRDTs (Automerge, Yjs) or simpler last-write-wins with timestamps<br>5. <b>Stale-while-revalidate</b>: Show cached data immediately, refresh in background<br>6. <b>Background sync</b>: <code>expo-background-fetch</code> for periodic sync tasks<br>Expo's OTA update system also works offline — the app runs the last downloaded update without network.",
  "expo::expert")

# ═══════════════════════════════════════════
# ADDITIONAL CARDS (to reach ~160)
# ═══════════════════════════════════════════

c("Fundamentals",
  "What is the difference between <code>npx expo prebuild</code> and <code>expo eject</code>?",
  "<code>npx expo prebuild</code> (modern) generates <code>ios/</code> and <code>android/</code> directories from <code>app.json</code> and config plugins. It's <b>idempotent</b> — you can delete and regenerate freely. <code>expo eject</code> (legacy, deprecated) permanently converted a managed project to bare. <b>Prebuild is the current approach</b> — it treats native directories as generated artifacts, not source code you edit.",
  "expo::fundamentals")

c("CoreOps",
  "How do you add <b>web support</b> to an Expo project?",
  "Web support is included by default in <code>create-expo-app</code> (SDK 50+). For existing projects: <code>npx expo install react-dom react-native-web @expo/metro-runtime</code>. Run with <code>npx expo start --web</code>. Expo Router handles routing for both native and web using the same <code>app/</code> directory. Use <code>Platform.select({ web: ..., default: ... })</code> for web-specific behavior.",
  "expo::core-ops")

c("CoreOps",
  "What does <code>npx expo prebuild --clean</code> do differently?",
  "Adding <code>--clean</code> deletes the existing <code>ios/</code> and <code>android/</code> directories before regenerating them. This ensures a completely fresh native project with no stale artifacts. Use it:<br>• After upgrading the Expo SDK<br>• When build errors persist after plugin changes<br>• When switching between managed and bare workflow patterns<br>Without <code>--clean</code>, prebuild merges changes incrementally, which can leave orphaned files.",
  "expo::core-ops")

c("CoreOps",
  "What is the <code>@expo/metro-config</code> package?",
  "<code>@expo/metro-config</code> provides the default Metro bundler configuration for Expo projects. It extends Metro with:<br>• Proper resolution of <code>expo-*</code> package entry points<br>• Asset import support (<code>.png</code>, <code>.svg</code>, <code>.ttf</code>)<br>• CSS/Sass support via <code>@expo/metro-config/css</code><br>• Environment variable inlining<br>• Monorepo workspace support<br>Customize by creating <code>metro.config.js</code>:<br><code>const { getDefaultConfig } = require('@expo/metro-config');</code><br><code>module.exports = getDefaultConfig(__dirname);</code>",
  "expo::core-ops")

c("Router",
  "What is the <b>catch-all route</b> <code>[...rest].tsx</code> in Expo Router?",
  "<code>app/[...rest].tsx</code> matches any route under its directory level. For example, <code>app/docs/[...rest].tsx</code> matches <code>/docs/a</code>, <code>/docs/a/b</code>, <code>/docs/a/b/c</code>. Access the full path segments via <code>useLocalSearchParams().rest</code> (an array). Useful for:<br>• Documentation sites (catch all nested paths)<br>• Blog with flexible URL structures<br>• Fallback screens for unknown routes<br>Use <code>[...rest]</code> for one-segment-plus, <code>[[...rest]]</code> for zero-or-more (optional catch-all).",
  "expo::router")

c("Router",
  "How do you handle <b>authentication flows</b> with Expo Router?",
  "Pattern: use <b>route groups</b> to separate auth and app screens:<br><code>app/(auth)/_layout.tsx</code> — stack navigator for login/signup/forgot-password<br><code>app/(app)/_layout.tsx</code> — main app with tabs<br><code>app/index.tsx</code> — root that redirects based on auth state:<br><code>const { session } = useAuth();</code><br><code>if (!session) return &lt;Redirect href=\"/(auth)/login\" /&gt;;</code><br><code>return &lt;Redirect href=\"/(app)/home\" /&gt;;</code><br>This keeps auth screens isolated from the main app's navigation hierarchy.",
  "expo::router")

c("Router",
  "What is <code>useSegments()</code> in Expo Router?",
  "<code>import { useSegments } from 'expo-router';</code><br><code>const segments = useSegments();</code><br><br>Returns an array of the current route segments. For <code>/profile/123/settings</code>, it returns <code>['profile', '123', 'settings']</code>. Useful for:<br>• Knowing which tab/group the user is in<br>• Conditional layout rendering based on current section<br>• Analytics and screen tracking<br>• Auth guards: redirect if user is in <code>(app)</code> group without a valid session",
  "expo::router")

c("Router",
  "What are <b>screen options</b> and how do you configure them per-file?",
  "In Expo Router, you configure React Navigation screen options in two ways:<br><b>1. In layout</b> — using <code>&lt;Stack.Screen name=\"...\" options={{...}} /&gt;</code><br><b>2. Per screen file</b> — export an <code>options</code> object or function from the route file itself (similar to React Navigation inline options).<br><br>Example in <code>app/profile.tsx</code>:<br><code>export const options: StackScreenOptions = {</code><br><code>  headerTitle: 'Profile',</code><br><code>  presentation: 'modal',</code><br><code>};</code><br>This keeps screen-specific config co-located with the screen code.",
  "expo::router")

c("Components",
  "What is <code>expo-symbols</code> and when should you use it?",
  "<code>expo-symbols</code> provides access to Apple's <b>SF Symbols</b> icon library (iOS, iPadOS, macOS). It gives you 6000+ system icons with dynamic weight, scale, and rendering mode — without bundling font files. Usage:<br><code>import { SymbolView } from 'expo-symbols';</code><br><code>&lt;SymbolView name=\"heart.fill\" tintColor=\"red\" /&gt;</code><br>On Android and web, it falls back to a default icon or you must provide an alternative. Best for iOS-centric apps that want native-feeling icons.",
  "expo::components")

c("Components",
  "What is <code>expo-linear-gradient</code> and how is it used?",
  "<code>expo-linear-gradient</code> provides a performant gradient component backed by native drawing (CoreAnimation on iOS, native shader on Android). Usage:<br><code>import { LinearGradient } from 'expo-linear-gradient';</code><br><code>&lt;LinearGradient colors={['#ff7e5f', '#feb47b']} start={{ x: 0, y: 0 }} end={{ x: 1, y: 1 }}&gt;</code><br><code>  &lt;Text&gt;Gradient text bg&lt;/Text&gt;</code><br><code>&lt;/LinearGradient&gt;</code><br>Much better performance than JS-based gradient solutions. Supports multiple color stops, angles, and can be used as a background for any component.",
  "expo::components")

c("Components",
  "What is <code>expo-media-library</code> and what does it allow?",
  "<code>expo-media-library</code> provides read/write access to the user's photo library:<br>• <code>getAssetsAsync(options)</code> — query photos/videos with pagination<br>• <code>getAssetInfoAsync(asset, options)</code> — get detailed metadata<br>• <code>createAssetAsync(uri)</code> — save an image/video to the library<br>• <code>createAlbumAsync(name, asset)</code> — create an album<br>• <code>deleteAssetsAsync(assets)</code> — remove from library<br>• <code>getPermissionsAsync()</code> / <code>requestPermissionsAsync()</code><br>Requires <code>NSPhotoLibraryUsageDescription</code> (iOS) and <code>READ/WRITE_EXTERNAL_STORAGE</code> (Android).",
  "expo::components")

c("Components",
  "What is <code>expo-print</code> and <code>expo-print-to-pdf</code>?",
  "<code>expo-print</code> enables printing HTML content and generating PDFs:<br>• <code>Print.printAsync({ html, uri })</code> — open the native print dialog<br>• <code>Print.printToFileAsync({ html, width, height })</code> — generate a PDF file on disk<br>Common use cases: receipts, invoices, reports, ticket PDFs. Output file is written to <code>expo-file-system</code> cache/document directory. Combine with <code>expo-sharing</code> to let users share/email the generated PDF.",
  "expo::components")

c("Components",
  "What is <code>expo-image</code> and how does it improve on React Native's <code>&lt;Image&gt;</code>?",
  "<code>expo-image</code> (from <code>expo-image</code> package) is a <b>high-performance image component</b> built on the native Glide (Android) and SDWebImage (iOS) libraries. Advantages over RN <code>Image</code>:<br>• <b>BlurHash</b> and <b>ThumbHash</b> placeholders<br>• <b>Automatic caching</b> (memory + disk)<br>• <b>Transition animations</b> on load<br>• <b>Priority</b> and <b>recycling</b> for lists<br>• Faster rendering in large FlatLists<br>• <code>contentFit</code> prop for aspect ratio control<br>Usage: <code>&lt;Image source={{ uri: '...' }} placeholder={blurhash} /&gt;</code>",
  "expo::components")

c("EAS",
  "What is <code>eas build:version:set</code> and how do you manage versioning with EAS?",
  "EAS can manage app version numbers automatically:<br>• <code>eas build:version:set</code> — manually set the next version/bundle number<br>• <b>Remote version source</b> — configure <code>eas.json</code> to read version from a remote URL (your own API)<br>• <b>Auto-increment</b> — EAS auto-increments build numbers for each build<br>Configure in <code>eas.json</code>:<br><code>\"build\": { \"production\": {</code><br><code>  \"autoIncrement\": true,</code><br><code>  \"ios\": { \"autoIncrement\": \"buildNumber\" },</code><br><code>  \"android\": { \"autoIncrement\": \"versionCode\" }</code><br><code>}}</code><br>This prevents manual version management errors across CI builds.",
  "expo::eas")

c("EAS",
  "What is <b>EAS Environment</b> and how do you set build-time variables?",
  "EAS allows setting environment variables per build profile in <code>eas.json</code>:<br><code>\"build\": { \"production\": {</code><br><code>  \"env\": {</code><br><code>    \"API_URL\": \"https://api.prod.com\",</code><br><code>    \"SENTRY_DSN\": \"...\"</code><br><code>  }</code><br><code>}}</code><br><br>These are available during <b>build-time only</b> (Gradle, Xcode, prebuild scripts). For runtime access, prefix variables with <code>EXPO_PUBLIC_</code>. For secrets, use <code>eas secret:create</code> instead of hardcoding in <code>eas.json</code>.",
  "expo::eas")

c("DevWorkflow",
  "What is the recommended <b>CI/CD pipeline</b> for Expo with GitHub Actions?",
  "1. <b>PR checks</b>: lint, type-check, unit tests on every PR<br>2. <b>Preview builds</b>: <code>eas build --profile preview --platform all</code> on main branch merge<br>3. <b>OTA updates</b>: <code>eas update --branch staging</code> on main merge (for JS-only changes)<br>4. <b>Production builds</b>: <code>eas build --profile production --auto-submit</code> on git tags<br>Use the <code>expo/expo-github-action</code> to set up the EAS CLI in CI:<br><code>- uses: expo/expo-github-action@v8</code><br><code>  with:</code><br><code>    eas-version: latest</code><br><code>    token: ${{ secrets.EXPO_TOKEN }}</code>",
  "expo::dev-workflow")

c("DevWorkflow",
  "How do you configure <b>Storybook</b> with Expo?",
  "Storybook 7+ supports React Native via <code>@storybook/react-native</code>. Setup for Expo:<br>1. <code>npx expo install @storybook/react-native</code><br>2. Create <code>.storybook/main.ts</code> and <code>preview.tsx</code><br>3. Add Storybook as an Expo Router route: <code>app/_storybook.tsx</code> (or <code>app/(dev)/_storybook.tsx</code> in a dev group)<br>4. Conditionally render Storybook in dev:<br><code>if (process.env.EXPO_PUBLIC_STORYBOOK === 'true') {</code><br><code>  return &lt;StorybookUIRoot /&gt;;</code><br><code>}</code><br>Works with <code>expo-dev-client</code> for component isolation during development.",
  "expo::dev-workflow")

c("DevWorkflow",
  "What is <b>Expo Orbit</b>?",
  "Expo Orbit is a <b>desktop app</b> (macOS, Windows, Linux) for managing development builds and simulators:<br>• Install and launch development builds with one click<br>• Manage iOS simulators and Android emulators<br>• View build logs and device info<br>• Drag-and-drop APK/IPA installation<br>• No CLI needed for device management<br>It's the successor to the old Expo XDE and complements the CLI for visual device management. Download from <code>expo.dev/orbit</code>.",
  "expo::dev-workflow")

c("DevWorkflow",
  "What is the <b>expo-splash-screen config plugin</b> and how do you customize the splash?",
  "Configure the splash screen in <code>app.json</code> under <code>expo.splash</code>:<br><code>\"splash\": {</code><br><code>  \"image\": \"./assets/splash.png\",</code><br><code>  \"resizeMode\": \"contain\",</code><br><code>  \"backgroundColor\": \"#1e1e2e\",</code><br><code>  \"dark\": {</code><br><code>    \"image\": \"./assets/splash-dark.png\",</code><br><code>    \"backgroundColor\": \"#000000\"</code><br><code>  }</code><br><code>}</code><br>For Android 12+ splash customization (branded splash with icon), use the <code>expo-splash-screen</code> config plugin for additional options like <code>android.imageSize</code>. The splash image should be 1284x2778 pixels (for iPhone 13 Pro Max scaling).",
  "expo::dev-workflow")

c("Gotchas",
  "What are <b>source map issues</b> in production Expo builds?",
  "Production builds need source maps uploaded to a crash reporting service (Sentry, Bugsnag) to deobfuscate stack traces. Gotchas:<br>• Hermes generates different source maps than JSC<br>• EAS Build outputs source maps but doesn't auto-upload them<br>• Use <code>eas build</code> with <code>\"env\": { \"SENTRY_AUTH_TOKEN\": \"...\" }</code> and a build hook to upload<br>• Source maps contain file paths — ensure your CI doesn't expose internal paths publicly<br>• If source map upload fails silently, crash reports become unreadable minified stack traces<br>Test your source map pipeline before going to production.",
  "expo::gotchas")

c("Gotchas",
  "Why do <b>native modules</b> sometimes fail silently in development builds?",
  "Common causes:<br>• Missing config plugin — the native code wasn't linked into <code>ios/</code> or <code>android/</code> during <code>prebuild</code><br>• Cocoapods not installed: run <code>npx pod-install</code> in <code>ios/</code> directory<br>• The package wasn't installed with <code>npx expo install</code> (wrong version)<br>• Gradle sync issues (Android): clean build with <code>cd android && ./gradlew clean</code><br>• Simulator/emulator arch mismatch (Apple Silicon running x86 packages)<br>Fix steps: <code>npx expo prebuild --clean && npx expo run:ios</code> to force a full rebuild.",
  "expo::gotchas")

c("Gotchas",
  "What <b>AsyncStorage</b> gotchas exist in Expo?",
  "React Native's <code>@react-native-async-storage/async-storage</code> is the standard key-value store for non-sensitive data. Gotchas:<br>• <b>Not encrypted</b> — don't store tokens or secrets (use <code>expo-secure-store</code>)<br>• <b>Async only</b> — all operations return Promises<br>• <b>Size limits</b>: ~6MB on Android per entry, no hard limit on iOS but can impact performance<br>• <b>Serialization</b>: only strings — JSON.stringify/parse every read/write<br>• <b>Performance</b>: slow for large datasets (1000+ keys). Use <code>expo-sqlite</code> instead<br>• <b>Clearing</b>: storage persists across app reinstalls in some cases (iOS keychain-like behavior)",
  "expo::gotchas")

c("Gotchas",
  "What are <b>EAS Build timeout</b> gotchas?",
  "EAS Build has a <b>timeout limit</b> (typically ~60 minutes on free tier, configurable on paid plans). Gotchas:<br>• Large <code>node_modules</code> can cause timeout during install step<br>• Broken CocoaPods or Gradle downloads hang forever, eating timeout<br>• Network issues during dependency fetching silently fail after timeout<br>• <b>Fix:</b> use build caching to skip redundant steps, avoid unnecessary heavy dependencies, and ensure all URLs in Podfile/gradle are accessible. Monitor build logs for stalled steps.<br>If builds consistently time out, consider <code>eas build --local</code> for debugging.",
  "expo::gotchas")

c("Gotchas",
  "Why do <b>fonts fail to load</b> on first app launch?",
  "If fonts are loaded asynchronously (via <code>Font.loadAsync</code> or <code>useFonts</code>), the first render may show fallback system fonts before the custom font is ready. Fix:<br>1. Keep <code>SplashScreen.preventAutoHideAsync()</code> active<br>2. Load fonts in the root <code>_layout.tsx</code><br>3. Call <code>SplashScreen.hideAsync()</code> only after fonts are loaded<br>4. Hook pattern: <code>const [loaded, error] = useFonts({...});</code><br><code>useEffect(() => { if (loaded || error) SplashScreen.hideAsync(); }, [loaded, error]);</code><br>Never render app UI before fonts are confirmed loaded.",
  "expo::gotchas")

c("Expert",
  "How do you implement <b>A/B testing</b> with EAS Update?",
  "Use EAS Update <b>channels and branches</b> for A/B testing:<br>1. Create experimental branches: <code>eas update --branch experiment-a</code>, <code>--branch experiment-b</code><br>2. Point different channels to different experiment branches<br>3. Build separate binaries linked to each channel (or use a feature flag system to switch channels at runtime)<br>4. Measure metrics per channel<br>5. Promote the winner: repoint the production channel to the winning branch<br>Alternatively, use remote config (<code>Firebase Remote Config</code> or <code>expo-constants</code> with <code>extra</code>) for in-app A/B without separate builds.",
  "expo::expert")

c("Expert",
  "What is <code>expo-router/head</code> and what does it do?",
  "<code>import { Head } from 'expo-router/head';</code><br><code>&lt;Head&gt;&lt;title&gt;My Page&lt;/title&gt;&lt;/Head&gt;</code><br><br>Expo Router's <code>&lt;Head&gt;</code> component (SDK 51+) lets you set the document <code>&lt;head&gt;</code> content for <b>web rendering</b>. It works like Next.js <code>Head</code>: set page title, meta tags, Open Graph tags, favicon, and other <code>&lt;head&gt;</code> elements. On native (iOS/Android), it's a no-op. This is how you get proper SEO and social sharing metadata when your Expo app renders on the web.",
  "expo::expert")

c("Expert",
  "How do you handle <b>Apple App Store review</b> with Expo?",
  "App Store review common Expo issues and solutions:<br>• <b>UIWebView deprecation</b>: ensure all dependencies use WKWebView (Expo does by default since SDK 38)<br>• <b>Privacy manifests</b> (SDK 50+): required privacy info plist for APIs used. Expo includes these but custom native modules need their own<br>• <b>Entitlements</b>: use <code>eas credentials</code> to manage App Store Connect API keys<br>• <b>App tracking transparency</b>: implement <code>expo-tracking-transparency</code> if using IDFA<br>• <b>Minimum iOS version</b>: set in <code>app.json</code> via <code>expo.ios.deploymentTarget</code><br>Use <code>eas submit --platform ios</code> with proper App Store Connect credentials for smooth submission.",
  "expo::expert")

c("Expert",
  "What is the <b>Expo Dashboard</b> and what can you do with it?",
  "The Expo Dashboard (<code>expo.dev</code>) provides a web UI for managing your Expo account and projects:<br>• View all EAS Build history and logs<br>• Manage EAS Update channels and branches<br>• Monitor OTA update deployment status<br>• Manage credentials (push notification keys, app signing)<br>• Invite team members and set permissions<br>• View crash analytics (if using Sentry integration)<br>• Create and manage organizations for team projects<br>It's the central hub for all EAS services — complementary to the CLI for visual management.",
  "expo::expert")

c("Expert",
  "How does <b>tree shaking</b> work with Expo and what can break it?",
  "Metro (Expo's bundler) does NOT tree-shake like Webpack. It only removes unused modules via the <code>blockList</code>. What breaks efficient bundling:<br>• <b>Barrel exports</b> (<code>export * from</code>) — Metro can't skip the whole file<br>• <b>Dynamic requires</b> (<code>require(variable)</code>) — forces all possible modules into the bundle<br>• <b>Side effects</b> — Metro assumes imported files may have side effects unless <code>package.json</code> has <code>\"sideEffects\": false</code><br>• <b>Large icon libraries</b>: prefer importing individual icons over the full set<br>Tip: configure <code>metro.config.js</code> with <code>blockList</code> and <code>experimentalImportSupport</code> to minimize bundle size.",
  "expo::expert")

c("Expert",
  "What is the <code>+html.tsx</code> file in Expo Router?",
  "The <code>app/+html.tsx</code> file (SDK 51+) is a special file that customizes the <b>HTML shell</b> for web rendering. It wraps the entire app output:<br><code>export default function Root({ children }: { children: React.ReactNode }) {</code><br><code>  return (</code><br><code>    &lt;html lang=\"en\"&gt;</code><br><code>      &lt;head&gt;&lt;meta charSet=\"utf-8\" /&gt;...&lt;/head&gt;</code><br><code>      &lt;body&gt;{children}&lt;/body&gt;</code><br><code>    &lt;/html&gt;</code><br><code>  );</code><br><code>}</code><br>Use it to add analytics scripts, global meta tags, font preloading, CSS resets, and PWA manifest links. It's the HTML document root for web — native targets ignore it.",
  "expo::expert")

c("Expert",
  "How do you integrate <b>Sentry</b> for crash reporting in Expo?",
  "Use <code>@sentry/react-native</code> (wrapper around sentry-javascript + sentry-cocoa + sentry-android):<br>1. <code>npx expo install @sentry/react-native</code><br>2. Add config plugin: <code>\"plugins\": [[\"@sentry/react-native/expo\"]]</code> in <code>app.json</code><br>3. Initialize in app entry: <code>Sentry.init({ dsn: '...', enableNative: true })</code><br>4. Wrap root layout with <code>Sentry.wrap</code><br>5. Upload source maps during EAS Build: add a <code>postbuild</code> hook or use Sentry's EAS plugin<br>The config plugin automatically links the native Sentry SDK, sets up source map upload, and configures error boundary integration.",
  "expo::expert")

# ═══════════════════════════════════════════
# ASSEMBLY
# ═══════════════════════════════════════════

for deck_key, front, back, tags in C:
    decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))

filename = f"{TOPIC}_Zero_to_Hero.apkg"
genanki.Package(list(decks.values())).write_to_file(filename)
print(f"Built {len(decks)} decks with {len(C)} cards -> {filename}")
