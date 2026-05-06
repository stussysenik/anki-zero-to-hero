#!/usr/bin/env python3
"""DSPy Zero-to-Hero Anki deck. ~200 cards from first principles to custom optimizers."""

import genanki, random

OUTPUT = "/home/senik/Desktop/DSPy_Zero_to_Hero.apkg"

R = lambda: random.randrange(1 << 30, 1 << 31)

model = genanki.Model(
    R(), "DSPy Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "Card", "qfmt": '<div class="front">{{Front}}</div>',
                "afmt": '{{FrontSide}}<hr id="answer"><div class="back">{{Back}}</div>'}],
    css=""".card { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 22px;
              text-align: center; color: #cdd6f4; background-color: #1e1e2e; padding: 20px; }
         .front { font-weight: bold; margin-top: 60px; }
         .back  { font-size: 20px; text-align: left; padding: 10px 30px; }
         code, pre { font-family: "Fira Code", "Monaco", monospace; background: #313244;
                     padding: 2px 6px; border-radius: 4px; font-size: 18px; }
         hr { border-color: #45475a; }""")

decks = {
    "Fundamentals": genanki.Deck(R(), "DSPy::Zero2Hero::01-Fundamentals"),
    "Signatures":   genanki.Deck(R(), "DSPy::Zero2Hero::02-Signatures"),
    "Modules":      genanki.Deck(R(), "DSPy::Zero2Hero::03-Modules"),
    "Optimizers":   genanki.Deck(R(), "DSPy::Zero2Hero::04-Optimizers"),
    "Metrics":      genanki.Deck(R(), "DSPy::Zero2Hero::05-Metrics"),
    "Assertions":   genanki.Deck(R(), "DSPy::Zero2Hero::06-Assertions"),
    "Data":         genanki.Deck(R(), "DSPy::Zero2Hero::07-Data-Examples"),
    "Patterns":     genanki.Deck(R(), "DSPy::Zero2Hero::08-Advanced-Patterns"),
    "Gotchas":      genanki.Deck(R(), "DSPy::Zero2Hero::09-Gotchas"),
    "Expert":       genanki.Deck(R(), "DSPy::Zero2Hero::10-Expert-Opinions"),
}

C = []
def c(deck, front, back, tags):
    C.append((deck, front, back, tags))

# ═══ 01 - FUNDAMENTALS ══════════════════════════════════════════════════════════

c("Fundamentals", "What is DSPy?",
  "A framework for <b>programming</b>—not prompting—language models. You write Python programs with declarative modules, and DSPy <i>compiles</i> them by automatically optimizing prompts or fine-tuning weights.",
  ["L0_primitives"])

c("Fundamentals", "What problem does DSPy solve that raw prompting doesn't?",
  "Raw prompting is brittle: changing the model, task, or data requires manual prompt rewrites. DSPy separates <i>program logic</i> from <i>prompt engineering</i>—you define what the LM should do, and the optimizer finds <i>how</i> to tell it.",
  ["L0_primitives"])

c("Fundamentals", "What are the 3 core abstractions in DSPy?",
  "1. <b>Signatures</b> — declare input/output fields (the interface)<br>2. <b>Modules</b> — compose signatures into pipelines (the logic)<br>3. <b>Optimizers</b> — tune prompts/few-shot examples/weights (the training)",
  ["L0_primitives"])

c("Fundamentals", "What does it mean to 'compile' a DSPy program?",
  "Calling <code>optimizer.compile(program, trainset)</code> automatically generates optimized prompts, selects few-shot examples, or fine-tunes weights. The output is a version of your program that performs better on your task.",
  ["L0_primitives"])

c("Fundamentals", "What's the philosophical shift from 'prompt engineering' to 'DSPy programming'?",
  "Prompt engineering = manually writing string templates. DSPy programming = writing declarative Python that specifies <i>what</i> the LM should do. The optimizer figures out <i>how</i> to prompt or fine-tune for it.",
  ["L0_primitives"])

c("Fundamentals", "What is a DSPy program?",
  "A Python class inheriting from <code>dspy.Module</code> that composes any number of sub-modules (<code>Predict</code>, <code>ChainOfThought</code>, etc.) into a multi-step pipeline. Like a neural network but made of LM calls.",
  ["L0_primitives"])

c("Fundamentals", "What is the typical workflow for building a DSPy solution?",
  "1. Define the task: signature (inputs &rarr; outputs)<br>2. Write the program: a <code>dspy.Module</code><br>3. Collect/generate labeled data: <code>dspy.Example</code>s<br>4. Define a metric<br>5. Compile: <code>optimizer.compile(program, trainset)</code><br>6. Evaluate & iterate",
  ["L2_composition"])

c("Fundamentals", "How does DSPy handle different LM providers?",
  "Through LM clients: <code>dspy.LM('openai/gpt-4o')</code>, <code>dspy.LM('anthropic/claude-sonnet-4-20250514')</code>, or local models via <code>dspy.LM('ollama/llama3', api_base='...')</code>. Configure once, all modules use it.",
  ["L1_mechanics"])

c("Fundamentals", "What is <code>dspy.configure()</code>?",
  "Sets the default LM globally. <code>dspy.configure(lm=dspy.LM('openai/gpt-4o'))</code>. All modules will use this LM unless overridden per-module.",
  ["L1_mechanics"])

c("Fundamentals", "How does DSPy differ from LangChain?",
  "LangChain = imperative chains of prompt templates you manually engineer. DSPy = declarative programs where prompts are <i>learned</i> by optimizers from data. LangChain is a framework for connecting things; DSPy is a framework for <i>optimizing</i> LM behavior.",
  ["L3_design"])

c("Fundamentals", "What does 'declarative' mean in the context of DSPy?",
  "You declare <i>what</i> the inputs and outputs are (via signatures) and <i>what</i> the flow is (via modules), but NOT <i>how</i> the LM should be prompted. The optimizer fills in the 'how' automatically.",
  ["L0_primitives"])

c("Fundamentals", "What version of Python does DSPy require?",
  "Python 3.9+. Install: <code>pip install dspy-ai</code>. Note the package name is <code>dspy-ai</code>, not <code>dspy</code> (which is a different package).",
  ["L1_mechanics"])

# ═══ 02 - SIGNATURES ════════════════════════════════════════════════════════════

c("Signatures", "What is a DSPy Signature?",
  "A declarative specification of a module's input and output fields. Example: <code>\"question: str -> answer: str\"</code>. It's the <i>interface</i>—what goes in, what comes out.",
  ["L0_primitives"])

c("Signatures", "How do you define a signature as a string?",
  "<code>\"question -> answer\"</code><br><code>\"context: str, question: str -> answer: str\"</code><br>Use <code>:</code> to separate inputs from outputs. Multiple fields separated by <code>,</code>.",
  ["L1_mechanics"])

c("Signatures", "How do you define a signature as a class?",
  "<pre>class QASignature(dspy.Signature):<br>    \"\"\"Answer questions based on context.\"\"\"<br>    context = dspy.InputField(desc=\"the source text\")<br>    question = dspy.InputField()<br>    answer = dspy.OutputField(desc=\"a concise answer\")</pre>",
  ["L1_mechanics"])

c("Signatures", "What is an <code>InputField</code> and what can it include?",
  "Declares an input to a signature. Can include: <code>desc</code> (description for the LM), <code>prefix</code> (text before the field value), <code>format</code> (type hint). Example: <code>dspy.InputField(desc=\"the user's question\", prefix=\"Question:\")</code>",
  ["L1_mechanics"])

c("Signatures", "What is an <code>OutputField</code> and what can it include?",
  "Declares an expected output. Can include: <code>desc</code> (what the output should be), <code>prefix</code> (text before the generated output). The <code>desc</code> is critical—it guides the LM's generation.",
  ["L1_mechanics"])

c("Signatures", "Why use a class-based signature over a string signature?",
  "Class-based gives more control: field descriptions, prefixes, multiple fields per side, and programmatic field manipulation. String signatures are quicker for prototyping simple tasks. Both compile equally well.",
  ["L5_opinion"])

c("Signatures", "How do you specify types in a signature field?",
  "Use <code>dspy.InputField(desc=\"...\", format=str)</code> or with typing: <code>dspy.InputField(desc=\"...\")</code><br>DSPy infers types from the field value. For structured output, use <code>TypedPredictor</code> with Pydantic models.",
  ["L1_mechanics"])

c("Signatures", "How do you make a signature field optional?",
  "Default the field to <code>None</code> in the class signature. DSPy will only include it in the prompt when a value is provided. Example: <code>history = dspy.InputField(default=None)</code>.",
  ["L3_design"])

c("Signatures", "What does the signature docstring do?",
  "The class docstring (<code>\"\"\"...\"\"\"</code>) becomes the <i>instruction</i> to the LM. It's the most important prompt element—describe what the module should do, how to handle edge cases, and the output format.",
  ["L1_mechanics"])

c("Signatures", "How do you specify output structure (JSON, list, etc.) in a signature?",
  "1. In the docstring: \"Produce a JSON object with keys...\"<br>2. Use <code>dspy.OutputField(desc=\"a JSON object {key: value}\")</code><br>3. Use <code>TypedPredictor</code> with Pydantic models for guaranteed structure<br>4. Use <code>constraints</code> in <code>TypedChainOfThought</code>",
  ["L2_composition"])

# ═══ 03 - MODULES ═══════════════════════════════════════════════════════════════

c("Modules", "What is <code>dspy.Module</code>?",
  "The base class for all DSPy programs. Subclass it and define a <code>forward()</code> method. Modules compose sub-modules (like <code>Predict</code>, <code>ChainOfThought</code>) into multi-step pipelines.",
  ["L0_primitives"])

c("Modules", "What is <code>dspy.Predict</code>?",
  "The simplest module—makes a single LM call given a signature. No chain-of-thought, no reasoning. Good for classification, extraction, and simple generation.",
  ["L1_mechanics"])

c("Modules", "What is <code>dspy.ChainOfThought</code>?",
  "Like <code>Predict</code> but injects 'Let's think step by step.' into the prompt and adds a <code>rationale</code> output field. Improves accuracy for reasoning tasks at the cost of more tokens.",
  ["L1_mechanics"])

c("Modules", "What is <code>dspy.ReAct</code>?",
  "An agent module that interleaves reasoning (<code>Thought</code>) and tool use (<code>Action</code>) in a loop. The signature must include <code>tools</code>. DSPy manages the ReAct loop transparently.",
  ["L1_mechanics"])

c("Modules", "What is <code>dspy.ProgramOfThought</code>?",
  "Generates code (Python) as the reasoning step, executes it, and uses the result to produce the final answer. Effective for math, symbolic reasoning, and algorithmic tasks.",
  ["L1_mechanics"])

c("Modules", "What is <code>dspy.MultiChainComparison</code>?",
  "Runs multiple ChainOfThoughts in parallel and asks the LM to compare/merge their outputs. Useful when diversity of reasoning matters more than any single chain.",
  ["L2_composition"])

c("Modules", "What is <code>dspy.TypedPredictor</code>?",
  "Ensures structured output by enforcing a Pydantic model schema. Internally retries if the output doesn't parse. Each field in the Pydantic model gets its own signature field. Use when you need guaranteed JSON structure.",
  ["L2_composition"])

c("Modules", "What is <code>dspy.TypedChainOfThought</code>?",
  "Combines <code>ChainOfThought</code> reasoning with <code>TypedPredictor</code>'s structured output. Has <code>rationale</code> + typed fields. Best for reasoning tasks that need structured JSON output.",
  ["L2_composition"])

c("Modules", "How do you compose modules into a multi-step pipeline?",
  "<pre>class RAG(dspy.Module):<br>    def __init__(self):<br>        self.retrieve = dspy.Retrieve(k=3)<br>        self.answer = dspy.ChainOfThought(\"context, question -> answer\")<br>    def forward(self, question):<br>        ctx = self.retrieve(question)<br>        return self.answer(context=ctx, question=question)</pre>",
  ["L2_composition"])

c("Modules", "What is <code>dspy.Retrieve</code>?",
  "A retrieval module. Configure with <code>dspy.settings.configure(rm=your_rm)</code> where <code>your_rm</code> is a retriever model (ColBERT, Chroma, etc.). Use <code>k</code> to specify number of passages.",
  ["L1_mechanics"])

c("Modules", "How do you access the generated <code>rationale</code> from ChainOfThought?",
  "Access <code>result.rationale</code> (the 'Let's think step by step' output before the final answer). Useful for debugging, logging, or feeding into downstream modules.<br><code>pred = cot(context=ctx, question=q)<br>print(pred.rationale)</code>",
  ["L1_mechanics"])

c("Modules", "How does <code>dspy.ReAct</code> decide when to stop?",
  "The signature includes a <code>Finish</code> action. When the LM generates <code>Action: Finish[final answer]</code>, the loop ends. The required signature pattern: <code>question, tools -> answer</code> where tools are passed via <code>dspy.Tool</code>.",
  ["L2_composition"])

c("Modules", "What is a <code>dspy.Tool</code>?",
  "A function wrapped for ReAct agents. Example:<br><code>def search(query: str) -> str: ...</code><br><code>tool = dspy.Tool(search, name=\"web_search\", desc=\"Search the web\")</code><br>The <code>desc</code> tells the LM when to use it.",
  ["L2_composition"])

c("Modules", "Can a module call another module that itself was compiled?",
  "Yes. Each sub-module can be independently compiled. Compose compiled modules into larger pipelines. The compilation is per-module, so each one has its own optimized prompts/examples.",
  ["L3_design"])

c("Modules", "What happens if you don't provide a required input field to a module?",
  "DSPy raises a <code>ValueError</code> at prediction time. Check your <code>forward()</code> method to ensure all signature input fields receive values.",
  ["L4_diagnosis"])

# ═══ 04 - OPTIMIZERS ════════════════════════════════════════════════════════════

c("Optimizers", "What is an Optimizer (formerly called a 'teleprompter') in DSPy?",
  "An algorithm that takes a program + training data + metric and produces an improved version of the program. It may: add few-shot examples, rewrite prompt instructions, or fine-tune weights.",
  ["L0_primitives"])

c("Optimizers", "What is <code>BootstrapFewShot</code>?",
  "The foundational optimizer. It runs your program on training examples, collects successful (correct per metric) traces, and inserts them as few-shot demonstrations. Simple, effective baseline.",
  ["L1_mechanics"])

c("Optimizers", "What is <code>BootstrapFewShotWithRandomSearch</code>?",
  "Like BootstrapFewShot but generates multiple candidate programs with different random seeds, then picks the best one based on validation set performance. More robust but slower.",
  ["L2_composition"])

c("Optimizers", "What is <code>MIPROv2</code>?",
  "Multiprompt Instruction PROposal — the current recommended optimizer. It automatically generates instruction candidates, selects few-shot examples, and runs Bayesian optimization to find the best prompt+example combination. State-of-the-art for most tasks.",
  ["L3_design"])

c("Optimizers", "What is <code>BetterTogether</code>?",
  "An optimizer that uses multiple weaker LMs to produce a stronger composite program. Each sub-LM votes or collaborates. Useful when you want to use cheaper models to approximate an expensive one.",
  ["L3_design"])

c("Optimizers", "What is <code>GEPA</code> (Generative Evolutionary Prompt Algorithm)?",
  "An evolutionary optimizer that mutates prompts through genetic operations (crossover, mutation) and selects for fitness based on your metric. Introduced ~2025 for reflective prompt evolution. Good for open-ended creative tasks.",
  ["L5_opinion"])

c("Optimizers", "How do you compile a DSPy program?",
  "<pre>from dspy.teleprompt import BootstrapFewShot<br>optimizer = BootstrapFewShot(metric=my_metric)<br>compiled = optimizer.compile(program, trainset=trainset)</pre><br>The returned <code>compiled</code> is a new version of <code>program</code> with optimized prompts.",
  ["L1_mechanics"])

c("Optimizers", "What is a 'bootstrap' trace in DSPy?",
  "A complete execution trace of your program on one input, showing every module call, its inputs, and outputs. Successful traces (where the metric passes) become few-shot examples. BootstrapFewShot collects these.",
  ["L2_composition"])

c("Optimizers", "How does <code>BootstrapFewShot</code> handle multi-module programs?",
  "It bootstraps traces independently for each module in your program. Each module gets its own set of few-shot demonstrations, selected based on which traces led to correct final outputs.",
  ["L2_composition"])

c("Optimizers", "What does the <code>max_labeled_demos</code> parameter do?",
  "Limits how many few-shot examples are used per module. Trade-off: more examples = better accuracy but higher token cost and possible overfitting. Typical values: 4–16 for BootstrapFewShot.",
  ["L3_design"])

c("Optimizers", "What does the <code>max_bootstrapped_demos</code> parameter do?",
  "Limits how many <i>generated</i> (bootstrapped) demonstrations are added beyond labeled ones. BootstrapFewShot generates unsuccessful traces, tries again, and keeps successes. Control this to manage prompt length.",
  ["L3_design"])

c("Optimizers", "How does MIPROv2 generate instruction candidates?",
  "It uses an LM to propose multiple instruction variants based on the signature + training data. Each candidate is a different 'take' on how to instruct the LM. It then evaluates which instruction + which few-shot set works best.",
  ["L3_design"])

c("Optimizers", "What does <code>MIPROv2</code>'s Bayesian optimization optimize over?",
  "The search space: (instruction candidate &times; few-shot example set). It runs evaluations on a validation set and uses Bayesian optimization to efficiently find the best combination without exhaustively testing every pair.",
  ["L3_design"])

c("Optimizers", "Can you compile a program with multiple different optimizers sequentially?",
  "Yes—called 'stacking'. Example: first BootstrapFewShot for examples, then MIPROv2 for instruction tuning. <code>compiled_v1 = bfsw.compile(program, trainset)</code> then <code>final = mipro.compile(compiled_v1, trainset)</code>",
  ["L3_design"])

c("Optimizers", "What happens if your metric is always 0 (program always fails)?",
  "BootstrapFewShot can't find successful traces and compiles nothing useful. The optimizer relies on at least <i>some</i> successes to bootstrap from. Fix: use an easier model during compilation, simplify the task, or start with hand-written examples.",
  ["L4_diagnosis"])

c("Optimizers", "What is the <code>metric_threshold</code> parameter?",
  "In BootstrapFewShot: a trace is 'successful' only if the metric score &ge; this threshold. Default is 1.0 for binary metrics. Lower it to 0.8 to accept partially correct traces as few-shot examples.",
  ["L3_design"])

# ═══ 05 - METRICS ═══════════════════════════════════════════════════════════════

c("Metrics", "What is a metric in DSPy?",
  "A Python function that takes <code>(example, prediction, trace=None)</code> and returns a float (higher = better). It defines what 'correct' means for your task. This is the <i>only</i> thing you must define manually.",
  ["L0_primitives"])

c("Metrics", "What's the signature of a DSPy metric function?",
  "<pre>def my_metric(example, pred, trace=None) -> float:<br>    # example.gold_answer is the ground truth<br>    # pred.answer is the model's output<br>    return 1.0 if match else 0.0</pre><br>The <code>trace</code> parameter is optional and receives the full execution trace.",
  ["L1_mechanics"])

c("Metrics", "What built-in metrics does DSPy provide?",
  "<code>dspy.evaluate.metrics.answer_exact_match</code> — exact string match<br><code>dspy.evaluate.metrics.answer_passage_match</code> — containment<br>For anything beyond trivial matching, write your own metric.",
  ["L1_mechanics"])

c("Metrics", "Why should metrics return continuous scores (0.0–1.0) rather than binary?",
  "Continuous scores give optimizers like MIPROv2 more signal. A 0.7 tells the optimizer 'close, adjust this direction' while a 0/1 gives less granular feedback. Use <code>round()</code> or partial-credit scoring in your metric.",
  ["L3_design"])

c("Metrics", "How do you use an LLM as a metric (LLM-as-judge)?",
  "<pre>def llm_metric(example, pred, trace=None):<br>    judge = dspy.Predict(\"question, pred_answer, gold_answer -> score: float\"})<br>    result = judge(question=example.question, pred_answer=pred.answer, gold_answer=example.answer)<br>    return float(result.score)</pre><br>Use a different (cheaper) model for the judge to keep costs down.",
  ["L3_design"])

c("Metrics", "Can a metric use multiple signals (correctness + style + conciseness)?",
  "Yes—return a weighted sum. <code>return 0.5 * correctness + 0.3 * style_score + 0.2 * conciseness</code>. This lets you optimize for multiple qualities simultaneously.",
  ["L3_design"])

c("Metrics", "How does the metric interact with <code>BootstrapFewShot</code>?",
  "BFS runs your program on each training example, calls <code>metric(example, prediction)</code>. If the score &ge; <code>metric_threshold</code>, the trace is saved as a successful demonstration. The metric IS the success criterion.",
  ["L2_composition"])

c("Metrics", "What does <code>dspy.evaluate</code> do?",
  "Runs your program on a dev/test set and computes aggregate metrics. Returns score, and optionally displays per-example results. Use this to benchmark before and after compilation.<br><pre>from dspy.evaluate import Evaluate<br>evaluator = Evaluate(devset=devset, metric=my_metric)<br>score = evaluator(program)</pre>",
  ["L1_mechanics"])

# ═══ 06 - ASSERTIONS ════════════════════════════════════════════════════════════

c("Assertions", "What are DSPy Assertions?",
  "Declarative constraints on LM outputs. <code>dspy.Assert</code> (hard constraint—retries on failure) and <code>dspy.Suggest</code> (soft constraint—tries but doesn't force). They make programs self-correcting.",
  ["L3_design"])

c("Assertions", "What's the difference between <code>dspy.Assert</code> and <code>dspy.Suggest</code>?",
  "<code>Assert</code>: fails the LM call and retries (with feedback) until the condition passes or max retries exhausted.<br><code>Suggest</code>: records the failure but continues. The feedback is appended to the prompt but doesn't force retry. Use Suggest for nice-to-have constraints.",
  ["L3_design"])

c("Assertions", "How do you use an Assert in a module's forward()?",
  "<pre>def forward(self, question):<br>    pred = self.generate(question=question)<br>    dspy.Assert(pred.answer is not None, \"Answer must not be empty\")<br>    dspy.Assert(len(pred.answer) &lt; 500, f\"Too long: {len(pred.answer)} chars\")<br>    return pred</pre>",
  ["L3_design"])

c("Assertions", "What happens when an Assert fails?",
  "DSPy re-runs the module with feedback appended to the prompt (e.g., 'The previous answer was empty. Please provide an answer.'). It retries up to <code>max_retries</code> times (default: 1). On exhaustion, raises <code>dspy.AssertionError</code>.",
  ["L3_design"])

c("Assertions", "How do you provide custom feedback on Assert failure?",
  "The second argument to <code>dspy.Assert</code> is the feedback message. Make it specific: <code>dspy.Assert(len(pred.code) &gt; 0, \"The code block was empty. Please generate Python code.\")</code>",
  ["L3_design"])

c("Assertions", "Can Assertions reference fields from earlier in the pipeline?",
  "Yes—the <code>forward()</code> method has access to all intermediate results. Example: <code>dspy.Assert(len(pred.summary) &lt; len(pred.original_text), \"Summary must be shorter than original\")</code>",
  ["L3_design"])

c("Assertions", "How do you configure global Assertion behavior?",
  "<pre>from dspy.primitives.assertions import settings<br>settings.max_retries = 3<br>settings.backtrack_to = 'generate'  # which module to re-run</pre><br>Or per-assertion: <code>dspy.Assert(cond, msg, max_retries=3)</code>.",
  ["L3_design"])

c("Assertions", "What is <code>settings.backtrack_to</code> in assertions?",
  "When an Assert fails, DSPy can backtrack to a specific module (by name) and re-run from there. This enables targeted retries rather than re-running the entire pipeline. Default: re-run only the module that produced the failing output.",
  ["L3_design"])

# ═══ 07 - DATA & EXAMPLES ═══════════════════════════════════════════════════════

c("Data", "What is a <code>dspy.Example</code>?",
  "A dict-like object representing one labeled data point. Fields are accessed as attributes: <code>example.question</code>, <code>example.answer</code>. Created with <code>dspy.Example(question=\"...\", answer=\"...\")</code> and passed with <code>.with_inputs(\"question\")</code>.",
  ["L1_mechanics"])

c("Data", "How do you create a training set from a list of dicts?",
  "<pre>data = [{\"question\": \"What is 2+2?\", \"answer\": \"4\"}, ...]<br>trainset = [dspy.Example(**d).with_inputs(\"question\") for d in data]</pre><br><code>with_inputs()</code> marks which fields are inputs—everything else is a label.",
  ["L1_mechanics"])

c("Data", "What does <code>.with_inputs()</code> do on an Example?",
  "Marks certain fields as <i>inputs</i> (provided to the program) vs. <i>labels</i> (used by the metric for scoring, NOT passed to the program). Never pass labels as inputs—the program shouldn't see the answer during prediction.",
  ["L1_mechanics"])

c("Data", "What's the difference between a training set and a dev set in DSPy?",
  "Training set: used by <code>optimizer.compile()</code> to learn prompts/examples.<br>Dev (validation) set: used by the optimizer to evaluate candidate programs and choose the best one.<br>Test set: held out, used only for final evaluation—never seen during compilation.",
  ["L2_composition"])

c("Data", "How do you handle conversation history in DSPy examples?",
  "Use a field with type <code>list[dict]</code>: <code>history = dspy.InputField(desc=\"conversation so far\")</code>. Each turn is <code>{\"role\": \"user\"/\"assistant\", \"content\": \"...\"}</code>. The LM adapter serializes it into the chat format.",
  ["L2_composition"])

c("Data", "How do you load a dataset from HuggingFace into DSPy?",
  "<pre>from datasets import load_dataset<br>ds = load_dataset(\"hotpot_qa\", \"distractor\", split=\"train\")<br>trainset = [dspy.Example(question=r['question'],<br>                        answer=r['answer']).with_inputs('question')<br>            for r in ds[:100]]</pre>",
  ["L1_mechanics"])

c("Data", "What does a <code>dspy.Dataset</code> object provide?",
  "A wrapper around a list of examples with extra utilities: <code>.train</code>, <code>.dev</code>, <code>.test</code> splits; <code>.map()</code> and <code>.filter()</code> methods; integration with DataLoader. Under active development.",
  ["L1_mechanics"])

c("Data", "How many training examples do you typically need for DSPy?",
  "BootstrapFewShot: 10–50 labeled examples is often enough (it generates more from successful traces). MIPROv2: 50–200 for good instruction search. Start small, measure, add more if performance plateaus.",
  ["L5_opinion"])

# ═══ 08 - ADVANCED PATTERNS ═════════════════════════════════════════════════════

c("Patterns", "How do you save and load a compiled DSPy program?",
  "<pre>compiled.save(\"my_program.json\")<br>loaded = dspy.Module.load(\"my_program.json\")</pre><br>This saves the optimized prompts, few-shot examples, and module structure. Re-load across sessions without recompiling.",
  ["L2_composition"])

c("Patterns", "How does DSPy caching work?",
  "Enable: <code>dspy.settings.configure(cache=True)</code>. DSPy caches LM calls by (model, prompt, kwargs) hash. Repeated identical calls return cached output. Saves $ and time during development. Clear cache: <code>dspy.settings.cache.clear()</code>.",
  ["L2_composition"])

c("Patterns", "How do you use multiple different LMs in the same program?",
  "Pass <code>lm=...</code> to module constructors or set per-call:<br><pre>cheap_lm = dspy.LM('openai/gpt-4o-mini')<br>classifier = dspy.Predict('text -> label')<br>classifier.lm = cheap_lm  # override globally configured LM</pre><br>Use cheap models for simple tasks, powerful ones for reasoning.",
  ["L3_design"])

c("Patterns", "What are DSPy Adapters?",
  "Adapters translate DSPy's internal representation to provider-specific formats. <code>dspy.LM('openai/gpt-4o')</code> automatically selects the ChatAdapter. Custom adapters for unusual APIs, custom LMs, or different prompt formats.",
  ["L3_design"])

c("Patterns", "How do you write a custom Adapter?",
  "Subclass <code>dspy.adapters.Adapter</code>, implement <code>format()</code> (converts DSPy fields to provider format) and <code>parse()</code> (converts provider response back to DSPy fields). Register with <code>dspy.settings.configure(adapter=MyAdapter())</code>.",
  ["L6_innovation"])

c("Patterns", "How do you implement retry logic in DSPy beyond Assertions?",
  "<pre>max_retries = 3<br>for attempt in range(max_retries):<br>    try:<br>        result = module(input=value)<br>        if validate(result): break<br>    except Exception as e:<br>        if attempt == max_retries - 1: raise</pre><br>Or use <code>dspy.Assert</code> + <code>settings.max_retries</code> for declarative retry.",
  ["L3_design"])

c("Patterns", "How do you stream output from a DSPy module?",
  "Use async mode: <code>result = await module(input=value)</code> in async functions. Or use <code>dspy.settings.configure(streaming=True)</code>. Available with recent DSPy versions and supported LM providers.",
  ["L2_composition"])

c("Patterns", "How do you use DSPy with local/self-hosted models?",
  "<pre>lm = dspy.LM('ollama/llama3.2', api_base='http://localhost:11434', api_key='')<br>dspy.configure(lm=lm)</pre><br>For vLLM/TGI: pass <code>api_base</code> with the OpenAI-compatible endpoint. DSPy uses the chat completions API.",
  ["L2_composition"])

c("Patterns", "What is the 'ensembling' pattern in DSPy?",
  "Run multiple modules/prompts in parallel and aggregate results (voting, averaging, comparison). <code>MultiChainComparison</code> does this automatically. Or manually: run N predictors, pick the most common answer.",
  ["L3_design"])

c("Patterns", "How do you debug a compiled DSPy program?",
  "<code>dspy.settings.configure(lm=dspy.LM('openai/gpt-4o-mini'), trace=[])</code><br>Then: <code>dspy.inspect_history(n=1)</code> shows the last LM call's prompt and response. Use this to see what the optimizer actually generated.",
  ["L4_diagnosis"])

c("Patterns", "What is <code>dspy.inspect_history()</code>?",
  "Prints the most recent N LM calls: full prompts sent to the model AND the model's full responses. Essential for debugging: you can see what DSPy <i>actually</i> sent, including optimized instructions and few-shot examples.",
  ["L4_diagnosis"])

c("Patterns", "How do you handle large documents that exceed context windows?",
  "Chunk the input: use a retriever to find relevant passages, then pass only those chunks. Or implement a map-reduce pattern: process chunks independently, then aggregate. DSPy doesn't do chunking automatically—it's part of your program logic.",
  ["L3_design"])

# ═══ 09 - GOTCHAS ═══════════════════════════════════════════════════════════════

c("Gotchas", "Why is my compiled program performing worse than the uncompiled version?",
  "Common causes:<br>1. <b>Metric is wrong</b>—optimizing for the wrong thing<br>2. <b>Training set too small</b>—<code>&lt;10</code> examples for BootstrapFewShot<br>3. <b>Overfitting</b>—training set examples too specific, doesn't generalize<br>4. <b>Easy model used for compilation, hard model for inference</b>—compiled prompts work differently across models<br>Fix: validate on a held-out dev set, increase <code>max_labeled_demos</code>.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>dspy.LM('openai/gpt-4o')</code> raise a connection error?",
  "1. Missing API key: <code>export OPENAI_API_KEY=\"sk-...\"</code><br>2. Wrong model name: check exact name on provider's docs<br>3. Proxy/network: verify connectivity with <code>curl</code> first<br>4. Rate limits: add retry or reduce concurrency<br>DSPy also supports <code>OPENAI_API_BASE</code> for custom endpoints.",
  ["L4_diagnosis"])

c("Gotchas", "Why are my assertions not triggering retries?",
  "1. Assertions are imported from <code>dspy.primitives.assertions</code>, not Python builtins<br>2. They only work inside <code>dspy.Module.forward()</code> methods<br>3. <code>Suggest</code> never retries—it only records failures. Use <code>Assert</code> for retry behavior.<br>4. <code>settings.max_retries</code> might be set to 0",
  ["L4_diagnosis"])

c("Gotchas", "Why does my ChainOfThought output have a <code>rationale</code> field I didn't ask for?",
  "<code>ChainOfThought</code> always adds <code>rationale</code> to the output. It's a built-in artifact. If you don't want it, use <code>Predict</code> instead. If your downstream code doesn't expect it, just ignore it: <code>result.answer</code> still works.",
  ["L4_diagnosis"])

c("Gotchas", "Why does DSPy crash with 'No LM configured'?",
  "You forgot to call <code>dspy.configure(lm=...)</code> at the top of your script. Every DSPy program needs a default LM. Even if you compile, the compiled program still needs an LM to run.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>optimizer.compile()</code> take forever?",
  "BootstrapFewShot runs your program on EVERY training example. MIPROv2 evaluates MANY candidate programs. Solutions:<br>1. Use a smaller training set initially<br>2. Reduce <code>max_bootstrapped_demos</code><br>3. Use a cheaper/faster LM for compilation (<code>teacher_settings</code>)<br>4. Set <code>num_threads</code> for parallel compilation",
  ["L4_diagnosis"])

c("Gotchas", "Why does DSPy raise <code>ValueError: 'context' is a required field</code>?",
  "Your <code>forward()</code> isn't passing all fields defined in the signature. Check your module's signature and ensure every <code>InputField</code> gets a value in the method call chain.",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>.with_inputs()</code> sometimes not work as expected?",
  "You must call <code>.with_inputs()</code> on EACH <code>Example</code> individually. The fields you list as inputs will NOT be passed as labels during evaluation. If you accidentally mark a label as an input, the program sees the answer during prediction (data leakage).",
  ["L4_diagnosis"])

c("Gotchas", "Why does <code>dspy.evaluate</code> give a different score than my manual calculation?",
  "1. Your metric might have side effects or non-deterministic behavior<br>2. The evaluator calls your program once per example; make sure <code>forward()</code> is pure<br>3. Temperature &gt; 0 makes outputs non-deterministic—use <code>temperature=0</code> for evaluation<br>4. Assertions can modify outputs between metric calls",
  ["L4_diagnosis"])

# ═══ 10 - EXPERT OPINIONS ════════════════════════════════════════════════════════

c("Expert", "BootstrapFewShot vs MIPROv2: when to use which?",
  "BFS: fast, simple, good baseline. Use when you have a clear task and &ge;20 examples. BFS+RandomSearch: better generalization.<br>MIPROv2: slower, better, state-of-the-art. Use when you need max accuracy and have 50+ examples + a dev set. Worth the extra compile time for production systems.<br>Start with BFS, switch to MIPROv2 if accuracy isn't high enough.",
  ["L5_opinion"])

c("Expert", "When should you NOT use DSPy?",
  "1. One-off prompts (DSPy overhead isn't worth it)<br>2. Tasks with &lt;5 training examples (nothing to optimize from)<br>3. Extremely creative/generative tasks where 'correctness' is hard to define as a metric<br>4. When you need full control over every token of the prompt (DSPy adds its own structure)<br>5. Latency-critical single-call applications (compilation takes compute)",
  ["L5_opinion"])

c("Expert", "What's the best way to structure a complex multi-module DSPy program?",
  "Pattern: <b>Plan → Execute → Verify</b><br>1. <code>Planner</code>: decomposes the task into sub-tasks<br>2. <code>Executor</code>: a module per sub-task, run sequentially or in parallel<br>3. <code>Verifier</code>: Checks the final output, uses <code>dspy.Assert</code> to retry on failure<br>Each module compiled independently with its own training data. Works for complex RAG, code generation, multi-hop QA.",
  ["L5_opinion"])

c("Expert", "How do you make DSPy programs reliable in production?",
  "1. Compile with MIPROv2 + a held-out dev set<br>2. Freeze the compiled program: <code>.save()</code> and never recompile dynamically<br>3. Add <code>dspy.Assert</code> for output validation<br>4. Use a LLM-as-judge metric during compilation for quality alignment<br>5. Implement a fallback: if Assert fails 3x, return a safe default<br>6. Monitor: log <code>inspect_history()</code> for debugging regressions",
  ["L5_opinion"])

c("Expert", "What is the cheapest LM architecture that works well with DSPy?",
  "Use <code>gpt-4o-mini</code> or <code>claude-haiku</code> for compilation, then swap to a stronger model for inference. Or: use open-weight models like Llama 3.1 8B through Ollama for BFS compilation, GPT-4o for production. Compilation is where the token spend happens—optimize there.",
  ["L5_opinion"])

c("Expert", "How do you build a custom DSPy Optimizer?",
  "Subclass <code>dspy.teleprompt.Teleprompter</code> and implement <code>compile(self, program, trainset)</code>. Your method returns a modified copy of the program. The base class provides hooks for example selection, parameter management, and trace collection. Study <code>BootstrapFewShot</code> source as reference.",
  ["L6_innovation"])

c("Expert", "How does DSPy handle tool use beyond ReAct?",
  "Define tools as <code>dspy.Tool(func, name, desc)</code>. Pass them to any module's signature via <code>tools</code> field. For non-ReAct modules, you can call tools imperatively in <code>forward()</code> and feed results back into the next module call. Tools are just Python functions—DSPy doesn't restrict how you use them.",
  ["L3_design"])

c("Expert", "What's the relationship between DSPy and fine-tuning?",
  "DSPy optimizers primarily work at the <i>prompt level</i> (instructions, few-shot examples). However, DSPy can also drive fine-tuning: compile with BootstrapFewShot to generate high-quality training data, then use that data to fine-tune a smaller model. The <code>BetterTogether</code> optimizer explicitly targets this workflow.",
  ["L5_opinion"])

c("Expert", "How do you think about DSPy's compilation as a form of 'learned prompting'?",
  "Traditional ML: learn model parameters from data. DSPy: learn prompt parameters (instructions, examples) from data—same optimization principle, different parameter space. MIPROv2 literally runs Bayesian optimization over prompts. This is program synthesis for language: given a spec (signature + metric + data), synthesize the implementation (prompt).",
  ["L6_innovation"])

c("Expert", "What's the hardest part of DSPy that most beginners get wrong?",
  "<b>Metric design.</b> People write metrics that are too strict (exact match on free text) or too loose (always returns 0.5). A good metric captures <i>task success</i> with continuous granularity. Invest time here—the optimizer can only optimize what you measure. LLM-as-judge metrics are often worth the cost for tasks without clear parsing.",
  ["L5_opinion"])

c("Expert", "What does the future of DSPy look like (2025+)?",
  "1. <b>RL-driven optimization</b>: using reinforcement learning to tune module parameters<br>2. <b>GEPA evolution</b>: evolutionary prompt optimization for creative tasks<br>3. <b>MCP integration</b>: Model Context Protocol for standardized tool use<br>4. <b>Multi-agent orchestration</b>: compiler-aware multi-module systems<br>5. <b>Automatic program synthesis</b>: given a dataset, DSPy proposes entire program architectures",
  ["L6_innovation"])

# ── Build ──────────────────────────────────────────────────────────────────────
def build():
    for deck_key, front, back, tags in C:
        decks[deck_key].add_note(genanki.Note(model=model, fields=[front, back], tags=tags))
    genanki.Package(list(decks.values())).write_to_file(OUTPUT)
    print(f"Built {len(C)} cards across {len(decks)} decks -> {OUTPUT}")

if __name__ == "__main__":
    build()
