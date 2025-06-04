JAVASCRIPT

Javascript will allow us to write code that runs inside the user's web browser on the client
   - faster computation
   - more interactive web pages
   - manipulation of dom

<script>
    function hello{
        alert('Hello, world');
    }
</script>
<button onclick="hello()">Click here</button>
<script src ='counter.js'></script>
🔹 BASICS
- Variables: var, let, const
- Data Types: String, Number, Boolean, Object, Array, null, undefined
- Comments: // single-line, /* multi-line */

<script>
    let counter =0;  //creating and initializing variable

    function count(){
        counter++;
        alert(counter);
    }
</script>
<h1>Hello</h1>
<button onclick="hello()">Count</button>

improve

<script>
    let counter =0; 

    function count(){
        counter++;
        document.querySelector('h1').innerHTML = counter;
        if(counter % 10=== 0){
            alert(`Count is now ${counter}`) //template literal  ${rate.toFixed(3)} rounded to 3 decimal points 
        }
        document.addEventListener(DOMContentLoaded',function(){document.querySelector('button').onclick  =count;
        });
         // functional programming
    }
</script>
<h1>0</h1>
<button>Count</button>

🔹 OPERATORS
- Arithmetic: + - * / % **
- Comparison: == === != !== > < >= <=
- Logical: && || !
- Assignment: = += -= *=

🔹 CONTROL STRUCTURE
- if, else if, else
- switch
- for, while, do...while
- break, continue

🔹 FUNCTIONS
- Declaration: function greet() { }
- Expression: const greet = function() { }
- Arrow: const greet = () => { }
- autofocus
- setInterval(count,1000);
- toUpperCase()

🔹 ARRAYS
- Methods: push(), pop(), shift(), unshift(), splice(), slice(), map(), filter(), reduce(), forEach()
- Access: arr[i], arr.length

🔹 OBJECTS
- Properties: obj.key or obj["key"]
- Loop: for...in
- Methods: keys(), values(), entries(), first

🔹 EVENTS
- onclick, onchange, onsubmit, onload, onmouseover,onkeydown, onkeyup, onblur
- addEventListener("event", function handler)

🔹 DOM MANIPULATION(document object model)
- document.getElementById()
- document.querySelector()
    - document.querySelector('tag')
    - document.querySelector('#id')
    - document.querySelector('.class')
    - name = document.querySelector('#name').value

- element.innerHTML, element.textContent
- element.style.property
    - document.querySelector('#name').style..color = 'red';
- createElement()
    - li = document.createElement('li');
- appendChild()

disabled property
    document.querySelector('#submit').disabled = 'true';

data attributes

document.querySelectorAll('button').forEach(function(button)){
    button.onclick = function(){
        document.querySelector('#hello').style.color = button.dataset.color;
    }
}
<button data-color = "red"></button>

<head>
<script>
    function hello(){
        if(document.querySelector('h1').innerHTML ==='Hello'){
            document.querySelector('h1').innerHTML ='Goodbye!';   /*looks throught html page and extracts the element we want to modify and the innerHTML accesses the inner html property and update it*/
        }
        else{
            document.querySelector('h1').innerHTML ='Hello';   
        }
        
    }
</script>
</head>
<body>
    <h1>Hello</h1>
    <button onclick="hello()">Click here</button>
</body>

to improve the code

<head>
<script>
    function hello(){
        const heading = document.querySelector('h1');
        if(heading.innerHTML ==='Hello'){
            heading.innerHTML ='Goodbye!'; 
        }
        else{
            heading.innerHTML ='Hello';   
        }
        
    }
</script>
</head>
<body>
    <h1>Hello</h1>
    <button onclick="hello()">Click here</button>
</body>

🔹 BOM (Browser Object Model)
- alert(), prompt(), confirm()
- window.location, history, navigator

🔹 JSON(JavaScript Object notation)
- JSON.stringify(obj)
- JSON.parse(str)

🔹 DEBUGGING
- console.log(), console.error()
- DevTools (F12)

🔹 ES6+ FEATURES
- let & const
- Arrow Functions ()=> //creates a function
- Template Literals: `Hello ${name}`
- Destructuring: const {a, b} = obj
- Spread/Rest: [...arr], (...args)
- Classes: class Person { constructor() { } }
- Modules: export/import

🔹 PROMISES & ASYNC
- Promise: new Promise(resolve, reject)
- then(), catch()
- async/await

🔹 FETCH API
- fetch(url).then(res => res.json()).then(data => ...)

🔹 FORM VALIDATION
- e.preventDefault()
- Check required fields, types

🔹 ERROR HANDLING
- try { ... } catch(err) { ... }
- .catch(error => {
    console.log('Error':error);
})

<script>
    docuument.addEventListener('DOMContentLoaded',() =>{
        document.querySelector('select').onchange = function(){
            document.querySelector('#hello').style.color = this.value;
        }
    })

<h1 id="hello">Hello!</h1>
<select>
   <option value="black">Black</option>
   <option value="red">Red</option>
   <option value="blue">Blue</option>   
   <option value="green">Green</option>
</select>

- LOCAL STORAGE
  - localStorage.getItem(key)
  - localStorage.setItem(key,value)

     if(!localStorage.getItem('counter')){
        localStorage.setItem('counter',0);
     }

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

USER INTERFACE

🎨 WHAT IS A USER INTERFACE (UI)?
- UI: The point of interaction between user and software/hardware.
- Goal: Make interactions intuitive, efficient, and accessible.

📐 UI DESIGN PRINCIPLES
1. **Clarity** – Make interface elements easily understandable.
2. **Consistency** – Reuse visual and interactive patterns.
3. **Feedback** – Inform users of actions, changes, and errors.
4. **Affordance** – Design cues show how elements are used (e.g., buttons look clickable).
5. **Simplicity** – Remove unnecessary complexity.

🔘 UI ELEMENTS
- Text Fields, Buttons, Checkboxes, Radio Buttons, Dropdowns
- Sliders, Modals, Tabs, Tooltips, Icons, Progress Bars

📋 FORMS & INPUTS
- Label every input clearly
- Use `required`, `placeholder`, and `type` attributes
- Validate: client-side (JS), server-side (Python/Flask/Django)

🧰 HTML + CSS + JS FOR UI
- HTML: Structure
- CSS: Styling (color, spacing, typography)
- JS: Interactivity (events, validation, dynamic updates)

📱 RESPONSIVE DESIGN
- Use flexible layouts (flexbox/grid)
- Media queries: `@media (max-width: 768px) { ... }`
- Mobile-first approach

⚙️ ACCESSIBILITY (a11y)
- Use semantic HTML (`<nav>`, `<header>`, `<main>`, etc.)
- Provide `alt` for images, `aria` labels where needed
- Ensure keyboard navigability and screen reader support

🧪 USABILITY TESTING
- Watch users interact with prototype
- Note friction points
- Iterate based on real feedback

📦 UI FRAMEWORKS
- Bootstrap, Tailwind CSS
- React (component-based UI)
- Django Templates (server-rendered UI)

🔄 STATE & EVENTS
- JS tracks dynamic UI states
- Event handling: `onclick`, `onchange`, `submit`, `input`
- DOM manipulation updates UI in response

🧠 UX vs UI
- **UI**: How it looks
- **UX**: How it works and feels

- Single Page Application
<style>
   div {
       display: none; //display: 'block'
   }
</style>
history.pushState({section: section}, "", `section${section}`);   // to change url when moving through different sections of the same page

window.onpopstate= function(event){
    console.log(event.state.section);
    showsection(event.state.section);
}  // to go the previous section you were on by pressing back 

window.innerWidth - width of window
window.innerHeight - height of window
window.scrollY - how much the user has scrolled up in pixels along the Y-axis
document.body.offsetHeight - the entire height of the webpage
window.onscroll

document is the whole webpage while a window is the portion of the webpage we can see at a given time

Animation
  
  <style>

    @keyframes grow
       from{
        font-size: 20px;
       }
       to {
        font-size: 100px;
       }

    h1 {
        position: relative;
        animation-name: grow;
        animation-duration: 2s;
        animation-fill-mode: forwards;
    }
  </style>


  <style>

    @keyframes move
       from{
        left: 0%;
       }
       to {
        left: 50%;
       }

    h1 {
        position: relative;
        animation-name:move;
        animation-duration: 2s;
        animation-fill-mode: forwards;
    }
  </style>


  @keyframes move
       0%{
        left: 0%;
       }
      50% {
        left: 50%;
       }
      100% {
        left: 0%;
       }

    h1 {
        position: relative;
        animation-name:move;
        animation-duration: 2s;
        animation-fill-mode: forwards;
    }
  </style>

  animationPlayState (property of style)
   - to control if the animation is playing or paused

   element.parentElement.remove()

  
  
REACT
 - Declarative Programming
     allows to describe what state should be displayed in the webpage and in what form.

     <h1>{num}</h1>  (view)
     num +=1         (logic)
    
    React.useState(0)


ReactDOM ReactDOM.render()

BABEL - converts jsx code into javascript    
