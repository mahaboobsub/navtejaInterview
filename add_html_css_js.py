import json
import os

def load_db():
    if os.path.exists('modules.json'):
        with open('modules.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_db(db):
    with open('modules.json', 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

def main():
    db = load_db()
    
    # Module 7: HTML/CSS
    html_css = {
        "id": 7,
        "name": "HTML/CSS",
        "short": "HTML/CSS",
        "color": "c-gray",
        "count": 24,
        "subs": [
            {
                "head": "HTML",
                "qs": [
                    {
                        "q": "What is the difference between HTML4 and HTML5? Key new features?",
                        "a": "<h4>HTML4 vs. HTML5</h4>"
                            "<ul>"
                            "<li><strong>Syntax:</strong> HTML5 has simplified doctypes (<code>&lt;!DOCTYPE html&gt;</code>) and encoding declarations.</li>"
                            "<li><strong>Graphics:</strong> HTML5 adds native support for <code>&lt;canvas&gt;</code>, SVG, audio, and video elements.</li>"
                            "<li><strong>APIs:</strong> Adds Geolocation, Web Storage (localStorage), and Web Workers.</li>"
                            "<li><strong>Structure:</strong> Replaces layout divs with semantic structures (header, footer, nav, article).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What are semantic HTML5 elements? Give 6 examples and why they matter.",
                        "a": "<h4>Semantic HTML5</h4>"
                            "Elements that clearly describe their meaning to both browser and developer.<br/>"
                            "<em>Examples:</em> <code>&lt;header&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;section&gt;</code>, <code>&lt;article&gt;</code>, <code>&lt;aside&gt;</code>, <code>&lt;footer&gt;</code>.<br/>"
                            "<strong>Importance:</strong> Crucial for SEO ranking, accessibility (screen readers), and clean code structure."
                    },
                    {
                        "q": "What is the difference between <div> and <span>?",
                        "a": "<h4>div vs. span</h4>"
                            "<ul>"
                            "<li><strong><code>&lt;div&gt;</code>:</strong> Block-level element. Starts on a new line, takes up full width available, and permits custom height/margins.</li>"
                            "<li><strong><code>&lt;span&gt;</code>:</strong> Inline-level element. Remains inline, takes up only required content width, and disregards height modifications.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between block-level and inline elements?",
                        "a": "<h4>Block vs. Inline</h4>"
                            "Block elements (e.g. <code>p</code>, <code>div</code>, <code>h1</code>) start on new lines and fill full widths. Inline elements (e.g. <code>a</code>, <code>span</code>, <code>img</code>) display inline without line breaks."
                    },
                    {
                        "q": "What are HTML data attributes? How do you access them in JS?",
                        "a": "<h4>Data Attributes</h4>"
                            "Attributes starting with <code>data-</code> used to store custom metadata on elements.<br/>"
                            "<em>Accessing in JS:</em> Using the <code>dataset</code> property:<br/>"
                            "<pre>const val = element.dataset.userId; // accesses data-user-id</pre>"
                    },
                    {
                        "q": "What are meta tags? What does the viewport meta tag do?",
                        "a": "<h4>Meta Tags & Viewport</h4>"
                            "Tags inside <code>&lt;head&gt;</code> supplying page metadata (author, descriptions, keywords). The **viewport meta tag** coordinates responsive mobile layouts:<br/>"
                            "<pre>&lt;meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"&gt;</pre>"
                    },
                    {
                        "q": "What is the difference between href and src?",
                        "a": "<h4>href vs. src</h4>"
                            "<ul>"
                            "<li><strong><code>href</code>:</strong> Hypertext Reference. Establishes links to resources (stylesheets, websites). Does not block rendering.</li>"
                            "<li><strong><code>src</code>:</strong> Source. Imports/embeds resources into the document (script files, images). Pauses rendering while loading.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between localStorage and sessionStorage?",
                        "a": "<h4>Storage Comparison</h4>"
                            "<ul>"
                            "<li><strong>localStorage:</strong> Saved indefinitely on client browser until cleared explicitly via script or cache wipe.</li>"
                            "<li><strong>sessionStorage:</strong> Cleared automatically when the browser tab is closed.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What are ARIA attributes? Why do they matter for accessibility?",
                        "a": "<h4>ARIA Attributes</h4>"
                            "Accessible Rich Internet Applications attributes (e.g. <code>aria-label</code>, <code>role=\"button\"</code>) supplying metadata to screen readers to improve accessibility for disabled users."
                    },
                    {
                        "q": "What is the difference between <script>, <script async>, and <script defer>?",
                        "a": "<h4>Script Execution Modes</h4>"
                            "<ul>"
                            "<li><strong>Standard:</strong> Pauses HTML parsing to download and run scripts immediately.</li>"
                            "<li><strong>async:</strong> Downloads script in background, runs it the moment it finishes downloading, pausing HTML parsing. Non-blocking download, but execution order is not guaranteed.</li>"
                            "<li><strong>defer:</strong> Downloads script in background. Runs script only after the HTML document is fully parsed. Execution order is guaranteed.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between <link> and <script> placement in HTML?",
                        "a": "<h4>Resource Placement</h4>"
                            "Place <code>&lt;link rel=\"stylesheet\"&gt;</code> in the <code>&lt;head&gt;</code> to render styles before content loads. Place <code>&lt;script&gt;</code> at the bottom of <code>&lt;body&gt;</code> (or use <code>defer</code>) to prevent scripts from blocking HTML parsing."
                    },
                    {
                        "q": "What is a semantic form? What HTML5 input types exist?",
                        "a": "<h4>Semantic Forms</h4>"
                            "Forms using inputs that define specific data schemas (e.g. <code>email</code>, <code>url</code>, <code>date</code>, <code>tel</code>, <code>number</code>), triggering automatic browser validation checks."
                    }
                ]
            },
            {
                "head": "CSS",
                "qs": [
                    {
                        "q": "What is the CSS Box Model? Explain each layer.",
                        "a": "<h4>CSS Box Model</h4>"
                            "A design container wrapping every HTML element. Layers from inside out:<br/>"
                            "1. <strong>Content:</strong> The actual text/images.<br/>"
                            "2. <strong>Padding:</strong> Transparent space surrounding content inside borders.<br/>"
                            "3. <strong>Border:</strong> Line surrounding padding and content.<br/>"
                            "4. <strong>Margin:</strong> Transparent space separating the element from other elements."
                    },
                    {
                        "q": "What is the difference between margin and padding?",
                        "a": "<h4>Margin vs. Padding</h4>"
                            "<ul>"
                            "<li><strong>Margin:</strong> Outer spacing between elements.</li>"
                            "<li><strong>Padding:</strong> Inner spacing between content and border.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between position: static, relative, absolute, fixed, and sticky?",
                        "a": "<h4>CSS Position Options</h4>"
                            "<ul>"
                            "<li><strong>static (default):</strong> Flows standard document layout.</li>"
                            "<li><strong>relative:</strong> Positioned relative to its normal layout flow. Supports top/left offsets without affecting other elements.</li>"
                            "<li><strong>absolute:</strong> Positioned relative to its closest non-static parent element. Taken out of normal document flow.</li>"
                            "<li><strong>fixed:</strong> Positioned relative to the browser viewport. Remains locked in place during scroll.</li>"
                            "<li><strong>sticky:</strong> Hybrid. Behaves like relative until scroll threshold is reached, then locks in place like fixed.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is Flexbox? Name the key container and item properties.",
                        "a": "<h4>Flexbox Layout</h4>"
                            "A one-dimensional layout model for organizing elements in rows or columns.<br/>"
                            "<em>Container properties:</em> <code>display: flex</code>, <code>flex-direction</code>, <code>justify-content</code> (main axis alignment), <code>align-items</code> (cross axis alignment).<br/>"
                            "<em>Item properties:</em> <code>flex-grow</code>, <code>flex-shrink</code>, <code>flex-basis</code>, <code>align-self</code>."
                    },
                    {
                        "q": "What is CSS Grid? How is it different from Flexbox?",
                        "a": "<h4>CSS Grid vs. Flexbox</h4>"
                            "<ul>"
                            "<li><strong>Flexbox:</strong> One-dimensional (aligns elements in a single row OR column). Good for menu bars.</li>"
                            "<li><strong>Grid:</strong> Two-dimensional (aligns elements in rows AND columns simultaneously). Good for page layouts.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between display: none and visibility: hidden?",
                        "a": "<h4>Hiding Elements</h4>"
                            "<ul>"
                            "<li><strong><code>display: none</code>:</strong> Removes the element from the layout flow entirely. It takes up no space.</li>"
                            "<li><strong><code>visibility: hidden</code>:</strong> Hides the element, but the element still takes up its original space in the layout flow.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is CSS specificity? How is it calculated?",
                        "a": "<h4>CSS Specificity</h4>"
                            "The weight hierarchy determining which styles apply if rules conflict.<br/>"
                            "<em>Calculated as:</em> Inline styles (1000) > ID selectors (100) > Classes, attributes, pseudo-classes (10) > Elements and pseudo-elements (1)."
                    },
                    {
                        "q": "What is z-index? What is a stacking context?",
                        "a": "<h4>z-index & Stacking Context</h4>"
                            "<code>z-index</code> sets the vertical overlap priority of elements (requires non-static positioning). A **stacking context** is a conceptual group of elements moving together up/down the overlap layer."
                    },
                    {
                        "q": "What is responsive design? How do media queries work?",
                        "a": "<h4>Responsive Design</h4>"
                            "Design adaptively formatting across mobile, tablet, and desktop viewports. **Media queries** apply styles dynamically based on device queries:<br/>"
                            "<pre>@media (max-width: 768px) {\n  .sidebar { display: none; }\n}</pre>"
                    },
                    {
                        "q": "What is the difference between px, em, rem, vh, vw?",
                        "a": "<h4>CSS Units</h4>"
                            "<ul>"
                            "<li><code>px</code>: Absolute pixel units.</li>"
                            "<li><code>em</code>: Relative to the font-size of the parent element.</li>"
                            "<li><code>rem</code>: Relative to the font-size of the root element (<code>&lt;html&gt;</code>).</li>"
                            "<li><code>vh</code>/<code>vw</code>: Percentage units relative to 1% of viewport height/width.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a CSS pseudo-class vs a pseudo-element? Give examples.",
                        "a": "<h4>Pseudo selectors</h4>"
                            "<ul>"
                            "<li><strong>Pseudo-class:</strong> Targets element states. Example: <code>:hover</code>, <code>:focus</code>, <code>:nth-child()</code>.</li>"
                            "<li><strong>Pseudo-element:</strong> Targets virtual parts of elements. Example: <code>::before</code>, <code>::after</code>, <code>::first-letter</code>.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a CSS variable (custom property)? Syntax?",
                        "a": "<h4>CSS Variables</h4>"
                            "Allows defining reusable style tokens dynamically.<br/>"
                            "<em>Syntax:</em><br/>"
                            "<pre>:root {\n  --main-color: #4f8ef7;\n}\n"
                            ".btn { color: var(--main-color); }</pre>"
                    }
                ]
            }
        ]
    }
    
    # Module 8: JavaScript
    javascript_mod = {
        "id": 8,
        "name": "JavaScript",
        "short": "JS",
        "color": "c-coral",
        "count": 25,
        "subs": [
            {
                "head": "Core JS",
                "qs": [
                    {
                        "q": "What is the difference between var, let, and const?",
                        "a": "<h4>var vs. let vs. const</h4>"
                            "<table>"
                            "<tr><th>Feature</th><th>var</th><th>let</th><th>const</th></tr>"
                            "<tr><td><strong>Scope</strong></td><td>Function scope</td><td>Block scope</td><td>Block scope</td></tr>"
                            "<tr><td><strong>Hoisting</strong></td><td>Hoisted (initialized to undefined)</td><td>Hoisted (in Temporal Dead Zone)</td><td>Hoisted (in TDZ)</td></tr>"
                            "<tr><td><strong>Reassign</strong></td><td>Yes</td><td>Yes</td><td>No</td></tr>"
                            "</table>"
                    },
                    {
                        "q": "What is hoisting in JavaScript? Does let get hoisted?",
                        "a": "<h4>JavaScript Hoisting</h4>"
                            "Behavior where variable and function declarations are moved to the top of their scope during compilation.<br/>"
                            "<strong>Does let/const get hoisted?</strong> Yes, but they are not initialized. They reside in the <strong>Temporal Dead Zone (TDZ)</strong> until execution reaches their declaration line, throwing a ReferenceError if accessed early."
                    },
                    {
                        "q": "What is a closure? Give a real-world use case.",
                        "a": "<h4>Closures</h4>"
                            "A function that retains references to variables declared in its lexical scope environment, even when executed outside that scope.<br/>"
                            "<em>Use case:</em> Implementing private variables/methods (encapsulation).<br/>"
                            "<pre>function counter() {\n  let count = 0;\n  return () => ++count;\n}\n"
                            "const inc = counter(); inc(); // returns 1</pre>"
                    },
                    {
                        "q": "What is the event loop? Explain the call stack, Web APIs, and callback queue.",
                        "a": "<h4>The Event Loop</h4>"
                            "A mechanism enabling JS to run asynchronous tasks concurrently on a single thread.<br/>"
                            "<ul>"
                            "<li><strong>Call Stack:</strong> Executes synchronous code frames.</li>"
                            "<li><strong>Web APIs:</strong> Browser container managing async threads (timeouts, fetches).</li>"
                            "<li><strong>Callback (Task) Queue:</strong> Holds callbacks ready to run.</li>"
                            "<li><strong>Event Loop:</strong> Monitors the stack. When stack is empty, it pushes the first task from the callback queue onto the stack.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between == and ===?",
                        "a": "<h4>== vs. ===</h4>"
                            "<ul>"
                            "<li><strong><code>==</code>:</strong> Loose equality. Compares values after performing type coercion.</li>"
                            "<li><strong><code>===</code>:</strong> Strict equality. Compares both values AND types without coercion.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between null and undefined?",
                        "a": "<h4>null vs. undefined</h4>"
                            "<ul>"
                            "<li><strong><code>undefined</code>:</strong> Variable declared but holds no assigned value. Set automatically by JavaScript.</li>"
                            "<li><strong><code>null</code>:</strong> Intentional assignment representing the empty or non-existent value.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What does typeof null return and why?",
                        "a": "<h4>typeof null</h4>"
                            "Returns <code>\"object\"</code>. This is a legacy design bug in the original JavaScript implementation where variables were represented as type tags (objects shared tag 000, and null represented empty pointer which mapped to 000)."
                    },
                    {
                        "q": "What is prototypal inheritance?",
                        "a": "<h4>Prototypal Inheritance</h4>"
                            "The inheritance mechanism in JS. Every object has an internal link pointer (prototype) linking to other parent objects. Methods are inherited down this prototype chain."
                    },
                    {
                        "q": "What is the difference between function declaration and function expression?",
                        "a": "<h4>Function Declarations vs. Expressions</h4>"
                            "<ul>"
                            "<li><strong>Declaration:</strong> <code>function foo() {}</code>. Hoisted completely, can be called before declaration line.</li>"
                            "<li><strong>Expression:</strong> <code>const foo = function() {}</code>. Variable is hoisted, but function assignment is not. Cannot be called before assignment.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is an arrow function? How is this different inside it?",
                        "a": "<h4>Arrow Functions</h4>"
                            "Short function syntax (<code>() => {}</code>). Arrow functions do not declare their own <code>this</code> context; instead, they bind <code>this</code> lexically, inheriting it from the parent enclosing scope."
                    }
                ]
            },
            {
                "head": "Functions & Scope",
                "qs": [
                    {
                        "q": "What is the this keyword? How does its value change in different contexts?",
                        "a": "<h4>this Keyword Contexts</h4>"
                            "Refers to the execution context object.<br/>"
                            "<ul>"
                            "<li>Global scope: <code>window</code> (in browsers).</li>"
                            "<li>Method call: refers to the object calling the method.</li>"
                            "<li>Arrow functions: inherited lexically from enclosing parent scope.</li>"
                            "<li>Event handlers: refers to the DOM element receiving the event.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between call(), apply(), and bind()?",
                        "a": "<h4>call() vs. apply() vs. bind()</h4>"
                            "<ul>"
                            "<li><strong><code>call(obj, arg1, arg2)</code>:</strong> Executes function immediately, binding <code>this</code> to <code>obj</code>, passing arguments individually.</li>"
                            "<li><strong><code>apply(obj, [args])</code>:</strong> Executes function immediately, binding <code>this</code> to <code>obj</code>, passing arguments as an array.</li>"
                            "<li><strong><code>bind(obj)</code>:</strong> Returns a new function instance with <code>this</code> permanently bound to <code>obj</code>, to be executed later.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is a callback function? What is callback hell?",
                        "a": "<h4>Callbacks</h4>"
                            "A function passed as an argument to another function to execute after asynchronous operations complete. **Callback Hell** is nested asynchronous callbacks, resulting in hard-to-read 'pyramid of doom' code."
                    },
                    {
                        "q": "What is a Promise? What are its states?",
                        "a": "<h4>Promises</h4>"
                            "An object representing the eventual completion or failure of an asynchronous operation.<br/>"
                            "<em>States:</em> <code>pending</code> (initial state), <code>fulfilled</code> (operation succeeded), <code>rejected</code> (operation failed)."
                    },
                    {
                        "q": "What is async/await? How does it relate to Promises?",
                        "a": "<h4>async/await</h4>"
                            "Syntactic sugar built on top of JavaScript Promises, making asynchronous code look and behave like synchronous code."
                    },
                    {
                        "q": "What is the difference between synchronous and asynchronous JS?",
                        "a": "<h4>Sync vs. Async JS</h4>"
                            "Synchronous executes blocking statements in sequence line-by-line. Asynchronous delegates tasks (fetches, timeouts) to execution containers, allowing main threads to continue processing UI frames."
                    }
                ]
            },
            {
                "head": "Modern JS",
                "qs": [
                    {
                        "q": "What is destructuring? Show object and array destructuring.",
                        "a": "<h4>Destructuring</h4>"
                            "Unpacking values from arrays or objects directly into variables:<br/>"
                            "<pre>// Object:\nconst {name, age} = user;\n"
                            "// Array:\nconst [first, second] = arr;</pre>"
                    },
                    {
                        "q": "What is the spread operator vs rest parameter?",
                        "a": "<h4>Spread vs. Rest (<code>...</code>)</h4>"
                            "<ul>"
                            "<li><strong>Spread:</strong> Expands iterable elements (e.g. <code>[...arr1, ...arr2]</code>).</li>"
                            "<li><strong>Rest:</strong> Gathers multiple arguments into a single array (e.g. <code>function run(...args) {}</code>).</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is the difference between map(), filter(), and reduce()?",
                        "a": "<h4>Array Utilities</h4>"
                            "<ul>"
                            "<li><strong><code>map()</code>:</strong> Transforms array elements, returning a new array of same size.</li>"
                            "<li><strong><code>filter()</code>:</strong> Selects elements matching conditions, returning a filtered array.</li>"
                            "<li><strong><code>reduce()</code>:</strong> Aggregates elements into a single output value.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is event bubbling and event capturing?",
                        "a": "<h4>Event Propagation</h4>"
                            "<ul>"
                            "<li><strong>Event Capturing:</strong> Event starts at document root, propagating down to the target element.</li>"
                            "<li><strong>Event Bubbling (default):</strong> Event starts at the target element, propagating up the DOM tree to document root.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What is event delegation?",
                        "a": "<h4>Event Delegation</h4>"
                            "Adding a single event listener to a parent element to manage events for all children (present or future) by inspecting <code>event.target</code>."
                    },
                    {
                        "q": "What is the difference between localStorage, sessionStorage, and cookies?",
                        "a": "<h4>Storage Comparison</h4>"
                            "<table>"
                            "<tr><th>Feature</th><th>localStorage</th><th>sessionStorage</th><th>Cookies</th></tr>"
                            "<tr><td><strong>Capacity</strong></td><td>~5MB - 10MB</td><td>~5MB</td><td>~4KB</td></tr>"
                            "<tr><td><strong>Expiry</strong></td><td>Never</td><td>Tab close</td><td>Set manually</td></tr>"
                            "<tr><td><strong>Sent in request</strong></td><td>No</td><td>No</td><td>Yes (automatic)</td></tr>"
                            "</table>"
                    },
                    {
                        "q": "What is the fetch API? How do you handle errors with it?",
                        "a": "<h4>Fetch API</h4>"
                            "Modern interface to make network requests. Note: <code>fetch</code> does not reject on HTTP error codes (like 404 or 500). You must check response status manually:<br/>"
                            "<pre>fetch(url)\n"
                            "  .then(res => {\n"
                            "    if (!res.ok) throw new Error('API Error');\n"
                            "    return res.json();\n"
                            "  });</pre>"
                    },
                    {
                        "q": "What is JSON.parse() and JSON.stringify()?",
                        "a": "<h4>JSON Utilities</h4>"
                            "<ul>"
                            "<li><strong><code>JSON.parse()</code>:</strong> Converts a JSON string into a JavaScript object.</li>"
                            "<li><strong><code>JSON.stringify()</code>:</strong> Converts a JavaScript object into a JSON string.</li>"
                            "</ul>"
                    },
                    {
                        "q": "What are ES Modules? (import/export)",
                        "a": "<h4>ES Modules</h4>"
                            "Standard modular design in JS. Enables importing/exporting variables, functions, or classes across script files using <code>import</code> and <code>export</code> statements."
                    }
                ]
            }
        ]
    }
    
    # Check Module 7
    idx7 = -1
    for i, m in enumerate(db):
        if m['id'] == 7:
            idx7 = i
            break
    if idx7 != -1:
        db[idx7] = html_css
    else:
        db.append(html_css)
        
    # Check Module 8
    idx8 = -1
    for i, m in enumerate(db):
        if m['id'] == 8:
            idx8 = i
            break
    if idx8 != -1:
        db[idx8] = javascript_mod
    else:
        db.append(javascript_mod)
        
    save_db(db)
    print("HTML/CSS and JavaScript data populated successfully.")

if __name__ == '__main__':
    main()
