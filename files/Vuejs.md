# Vuejs

- uses declarative approach

## DOM Interaction

### [🌟] Creating a Vue application

- takes a component as an argument to configure the instance
- application instance provides a mount method that mounts the instance to an HTML element

[*syntax*]

```js
const app = Vue.createApp({
    [~properties~]
    ...
});

...

app.mount(~id~);
```

### [🌟] Deleting a Vue application

- unmounts the app
- `app.unmount()`

### [🌟] [🌟] Properties

1. `data() { return {~data~}}`
    [⚙️] Used to define data for elements in `<template></template>`

    e.g.

    ```js
    const app = Vue.createApp({
        data() {
            return {
                year : 2023,
                born : 2000,
            }
        }
    })
    ```

2. `components: {}`
    [⚙️] Used to import components

    e.g.

    ```js
    import 404NotFound from '/components/404NotFound.vue'

    export default {
        components: {
            404NotFound,
        }
    }
    ```

3. `methods : [~object~]`
    [🤝] Use with event binding OR data binding
    [🔨] Executed for every "re-render" cycle of the component
    [⚙️] Use for events or data that really needs to be re-evaluated all the time
    - it allows for the execution of functions when an event happens

    e.g.

    ```js
    const app = Vue.createApp({
        methods : {
            calcAge() {
                return this.year - this.born;
            }
        }
    })
    ```

4. `computed : [~object~]`
    [🤝] Use with data binding
    [🔨] Constantly re-evaluated to keep up with changes in one of their "used values"
    [⚙️] Use for data that depends on other data
    - for definition of `computed` properties
    - vue is aware of the "used values" -> it will cach the value of the property and only reevaluate it when one of the "used values" is changed
    - unlike methods, when used inside {{ }}, it is executed every single time a var is changed

5. `watch : [~object~]`
    [🤝] Not used directly in template
    [🔨] Allows you to run any code in reaction to some changed data (e.g. send HTTP request etc.)
    [⚙️] Use for any non-data update you want to make
    - repeat a data or computed name
    - executes the function when the property of the same name changes

    [*syntax*]

    ```js
    func(~newValue~, ~oldValue~) {
        ...
    }
    ```

    e.g.

    ```js
    const app = Vue.createApp({
        data() {
            return {
                name : '',
            }
        },
        watch : {
            name(oldName, newName) {
                ...
            }
        }
    })
    ```

### [🌟] Interpolation

- the insertion of smth of a different nature into smth else
- use mustache syntax to define an area where data/expressions can be injected into a component's HTML template
- use for default text

[*syntax*] HTML Document

``` html

</p> {{ .... }} </p>
```

### [🌟] [🌟] Directives

- all directives starts with `v-`

1. [❗] `v-bind:~attributeName~`
    - used on a HTML text
    - to set an attribute to a dynamic value
    - tells vue that text is to be interpreted as vue

    e.g. [Link]

    ```html
    ...
    <p> Learn more <a v-bind:href = "vueLink">about Vue</a></p> 
    ```

    e.g. [src]

    ```html
    ...
    <img v-bind:src = "imgURL"/>
    ```

2. [❗] `v-html`
    - helps to sets value of an attribute
    - tells vue that text is to be interpreted as HTML
    - similar to element.innerHTML in pure JS

3. [❗] `v-on:~event~ = "~code~"`
    - to respond to events
    - `~event~` : any JS events

    e.g.

    ```html
        <button v-on:click = "counter++">Add</button>
    ```

4. `v-on:input = "~code~"`
    - interaction between input element and code

    e.g.

    ```html
    <input v-on:input = "event => text = event.target.value + text">
    ```

5. `v-once`
    - tells that any dynamic data binding is only evaluated once

6. `v-model`
    - two way binding : listening to the event and writing the output back into input element through its value attribute
    - shortcut for `v-bind` + `v-on:input`

### [🌟] Shorthands

1. `@click`
    - shorthand for `v-on:click`

2. `:~attributeName~`
    - shorthand for `v-bind:~attributeName~`

### [🌟] [🌟] Modifiers

1. `.prevent`
    - performs the same function as event.preventDefault()

    e.g. [Preventing form submission from automatically reloading the webpage]

    ```html
        <form v-on:submit.prevent = "submitForm">
            <input type = "text">
            <button>Sign Up</button>
        </form>
    ```

2. `.right` / `.left` / `.middle`
    - specifies which mouse button v-on:click reacts to

3. `.stop`
    - stops event propagation

4. `.~specialKey~`
    - specifies which key v-on:event reacts to

### [🌟] Accessing app data

- using this keyword
- behind the scene, vuejs creates a application instance, hence it works as this kwyword refers to the instance

e.g.

```js
const app = Vue.createApp({
    data() {
        return {
            fruit : "orange",
            veg : "broccoli",
        }
    }

    methods : {
        listInventory() {
            const rng = Math.random();
            if (rng > 0.5) {
                return `We have ${this.fruit} in stock`;
            } else {
                return `We have ${this.veg} in stock`;
            }
        }
    }
})
```

| [🌟] Receiving native event object |

- passing the native event object into a function

e.g. [Pointing at the function]

```html
<button v-on:click = "func">Execute</button>
```

```js
<script>
export default {
    methods : {
        func(e) {
            ...
        }
    }
}
</script>
```

e.g. [Passing perimeters]

```html
<button v-on:click = "func($event, 'Cheong')">Execute</button>
```

```js
...
methods : {
    func(event, lastName) {
        this.name = event.target.value + ' ' + lastName;
    }
}
```

### [🌟] [🌟] Watchers

- executed when the value it watches changes
- repeat another data/computed property name in the `Object` passed to watch
- instead of updating/calculating the value of the variable like `computed`, `watch` is used to change values of other variables in reaction to the watched variable
- best used with only 1 dependency; >1 `computed` is a better choice

[*syntax*]

```js
watch: {
    // methods 
    // names of methods here matches the name of the variable it watches
    ~name~(value) { // the new value of the variable is automatically passed in as the first args
        // ...
    }
}
```

e.g.

```js
export default {
    data() {
        return {
            name: '',
            fullname: '',
        }
    },

    watch: {
        name(value) {
            this.fullname = value + ' ' + 'Cheong';
        }
    }
}
// Once name is updated, fullname will also follow suit
```

### [🌟] [🌟] Styling Dynamically

e.g. [V-binding In-line Style]

```html
<div class = "demo" :style="{borderColor: boxASelected ? 'red' : '#acc'}" @click = "boxSelected('A')"></div>
```

e.g. [V-binding class, Adding CSS style dynamically]

1. Using ternary operator

    ```html
    <div 
    :class = "boxASelected ? 'demo active' : 'demo' "
    ></div>
    ```

2. Using `Object` (recommended)

    ```html
    <div 
    class = "demo" // Since it is not dynamically changed
    :class = "{active: boxASelected}" 
    @click = "boxSelected('A')"
    ></div>
    ```

3. Using `computed` properties
    - for more complex checks whether the class should be added

    ```js
    computed : {
        boxAClasses() {
            return { active: this.boxASelected }
        };
    }
    ```

    ```html
    <div 
    :class = "boxAClasses"
    ```

4. Arrays
    - allows for fixed and dynamic classes to be put together

    ```html
    <div :class = "['demo', {active: this.boxASelected}]"></div>
    ```

### Rendering Conditional Content

- rendering features only if some condition is met
- use cases : showing a loading spinner before the data arrives

| [🌟] [🌟] Directives |

1. `v-if = "~condition~"`
    - attaches and detaches elements from DOM based on whether the condition is fulfilled
    - manipulating DOM can result in performance issues
    `~condition~` : any expression that yields a truthy or falsy value

    e.g.

    ```html
    <p v-if="displayParagraph === 0">No goals have beend added</p>
    ```

2. `v-else-if = "~condition~"`
    - can only be used after an element with v-if

3. `v-else`
    - can only be used directly after an element with v-if

4. `v-show = "~condition~"`
    - it doesnt work with v-if, v-else-if, v-else
    - it toggles whether to display the element, with css
    - use for contents that switches a lot between states

5. `v-for = "~expression~"`
    - typically used to display all contents in a list
    - use `in` instead of `of` inside expression

    [*syntax*] Looping through array expression

    ```html
    <li v-for="(~element~, index) in ~iterable~">{{ `${index}: ` }} {{ goal }}</li>
    ```

    [*syntax*] Looping through object expression

    ```html
    <li v-for="(~value~, ~key~, index) in [~object~]">{{ `${index}: ` }} {{ goal }}</li>
    ```

6. `:key = "~identifier"`
    - always use with `v-for`
    - vue always re-uses DOM elements to optimize performance -> this can lead to bugs if elements contain state
    - allows vue to distinguish between different elements created by `v-for`, retaining any information attached to it instead of transferring it to another

## Behind the scene

### [🌟] Vue's Reactivity

- behaves similarly to JS proxies
- JS proxies allows you to intercept and customize operations performed on objects

e.g. [JS proxies]

```js
const data = {
    message : 'Hello!',
    longMessage: 'Hello! World',
};

const handler = {
    set(target, key, value) {
        // console.log(target); // outputs data object
        // console.log(key); // message
        // console.log(value); // 'Hello!!!'

        if (key === 'message') {
            target.longMessage = value + 'World!'
        }
        target.message = value;
    }
};

new proxy = Proxy(data, handler);

proxy.message = 'Hello!!!'

console.log(proxy.longMessage); // outputs "Hello!!!World!"
```

## [🌟] [🌟] One App VS Multiple App

- apps do not have connection to each other; data in one cannot be accessed by the other
- when to use one app: for website requiring synergy among different components
- when to use multiple app: for website requiring different independent parts controlled by vue

## [🌟] Vue Templates

- vue templates are syntactically valid HTML that can be parsed by browsers and HTML parsers

1. `app.mount()`
    - most common way of defining a template

2. `template` property
    - defining it inside the app

    e.g.

    ```js
    const app = Vue.createApp({
        template : <p>{{ favouriteMeal }} </p>,
    })
    ```

## [🌟] Refs

- allows a direct reference to a specific DOM element or child component instance after it's mounted to be obtained

e.g.

```html
<input ref="input">
```

```js
...
this.$refs.input.value = '';
```

| [🌟] [🌟] [🌟] How Vue updates the DOM |

Sequentially...

[1] Vue Instance
    [❓] Stores data, computed, properties, methods
    [✨] Data and computed properties may change

[2] Virtual DOM
    [❓] JS-based DOM which exists only in memory
    [✨] updates are made to the virtual DOM first, only differences are then rendered to the real DOM

[3] Browser DOM
    [❓] Vue-controlled template is rendered in the DOM
    [✨] Updates should be reflected, but Vue does not re-render everything

### [🌟] [🌟] [🌟] Vue Instance Lifecycle

- when vue starts creating the app, and starts bringing something on to the screen, it reaches certain "checkpoints" known as lifecycle phases, where methods can be executed by defining relevant lifecycle hooks

[⚙️] Event: Executed `createApp({...})`

[🪝] #1: `beforeCreate()`
    - called before the app is fully initialised

[🪝] #2: `created()`
    - called thereafter

[⚙️] Event: Compile template

[🪝] #1: `beforeMount()`
    - right after vue is going to bring something to the screen

[🪝] #2: `mounted()`
    - now the vue app has been initialized, the template was compiled, Vue knows what to show on the screen. And it handed instructuions off to the browser, so that the browser really adds all the HTMl elements with all the content we need, as defined by our Vue app

[⚙️] Event: Mounted Vue Instance

[⚙️] In the event of a change in data

[🪝] #1:`beforeUpdate()`

[🪝] #2:`updated()`

[⚙️] In the event that the app is unmounted

[🪝] #1: `beforeUnmount()`

[🪝] #2: `unmounted()`

## Development Setup & Workflow

### [🌟] Why Development Server?

- "double-clicking" index.html is unrealistic
    1. we use the `file://` protocol instead of `https://` protocol
    2. Some (modern JS or Browser) features will not work there
    3. the final, deployed app will be served via `https://`

### [🌟] [🌟] Vue CLI

- helps us create projects with a pre-set configuration certain built-in tools
- helps us to create projects and manage projects that allows us to build a more realistic, bigger applications

Current state
    a. We always need to reload the page whenever we make any change
    b. IDE auto-completion is highly limited
    c. we work in just one file OR we need to handle multiple files with multiple `<script src="..."></script>` imports

Wanted state
    a. Saved changes should be auto-detected and page should reload/update
    b. IDE should provide better auto-completion and hints
    c. We should be able to split code into multiple files and export/import via ES Modules

[Include this in package.json]

1. Windows

    ```js
    "scripts": {  
    "serve": "set NODE_OPTIONS=--openssl-legacy-provider && vue-cli-service serve",  
    "build": "set NODE_OPTIONS=--openssl-legacy-provider && vue-cli-service build",  
    "lint": "set NODE_OPTIONS=--openssl-legacy-provider && vue-cli-service lint"
    },
    ```

2. Mac and Linux

    ```js
    "scripts": {  
    "serve": "export NODE_OPTIONS=--openssl-legacy-provider && vue-cli-service serve",  
    "build": "export NODE_OPTIONS=--openssl-legacy-provider && vue-cli-service build",  
    "lint": "export NODE_OPTIONS=--openssl-legacy-provider && vue-cli-service lint"
    },
    ```

### [🌟] [🌟] Getting started

[⚙️] Option #1 : Use Vue CLI

1. Installation
    a. ensure all dependencies e.g. nodejs are installed on computer
    b. run `npm install -g @vue/cli`
        - vue cli will be downloaded globally

2. Create new project
    a. `vue create ~projectName~` to init a new project

3. Running local server
    a. `cd` to specific folder
    b. run `npm run serve` to start dev server

4. Extensions
    e. install &/ enable veutur

OR

[⚙️] Option #2 : Domentation method

1. Create new project
    a. run "npm init vue"

2. Extensions
    a. install volar

[⚙️] Option #3: Importing a pre-existing project

1. `npm install` to install all dependency packages in package.json
    - most of the time projects do not come with the node_modules folder as it is too big

### [🌟] Inspecting created project

[Listing Files & Folders]

1. `node_modules`
    - houses the dependencies we need, specified in package.json

2. `public` folder
    ↪ [File]  index.html

3. `src` folder
    - our main workng directory
    ↪ [File]  .vue files
        - files for different pages of the application
    ↪ [SubFolder] components
        - files for components that are imported to build different pages
    ↪ [SubFolder] utils
        - exports useable code snippets e.g. HTTP requests

4. Configuration Files
    ↪ babel.config.js
    ↪ jsconfig.json
    ↪ vue.config.js

5. `package.json`
    - defines the scripts we can execute e.g. `npm run serve` and stores var of certain pacakges

### [🌟] .vue files

- allows us to write Vue components in a much nicer way
- allow us to split our template into three diferent sections i.e. HTML code that belongs to an app or a component, script part, styles

e.g.

```html
<template>
    <!-- ... -->
</template>

<script>
    // ...
</script>
```

### [🌟] Using a build workflow

[⚙️] Stage #1: Writing out code with next-gen and Vue specific syntax and features

[⚙️] Stage #2: Building for production; where code is compiled into standard JS code

[⚙️] Stage #3: Hosting on a development or real server

## Components

- allows for easy replication and encapsulation of HTML code, with attached data and logic
- splitting a big application into multiple smaller chunks

### [🌟] Global Component Registration

[*syntax*]

```js
const app = Vue.createApp({
    ...
})

app.component(~customTag~, ~configObj~)
app.mount("#app")
```

```html
<~customTag~><~customTag~>
```

- ~customTag~ : Custom html tag which can be inserted to use the HTML to use the component; id should have two chars to differentiate from default Js ones with only one char
- ~configObj~ : an component object

### [🌟] Multiple apps vs Multiple components

1. Multiple Apps
    - if there are multiple, independent parts of HTML pages, then multiple Vue apps will be used

2. Multiple Components
    - used in SPAs or Single Page Applications where instead a user interace is built up with multiple components
    - [Why?] Vue apps are independent from each other - they can't really communicate, while components do offer communication mechnanisms that allow exchange of data between them

## Component Communication

- Components are used to build UIs by combining them
- Components build "parent-child" relations and use "unidirectional data flows" for communication

### [🌟] Props (parent => child)

- used to pass data down from the parent to child component
- should be defined in advance, possibly in great detail (type, required, default, validator etc.)
- once it is passed to the child component, value is immutable unless force re-render
- for values that change, consider...
    1. use parent prop as init value
        a. setting a data property as the prop value received from the parent component
        b. show and display that data property

    2. [❗] `emit` events
        <> Custom Events

e.g. [Declaring Props in Vue]

```html
<!-- Component -->
<script>
    export default {
        props: ["name"] // Props are values received from the parent
    }
</script>
```

```html
<!-- HTML Tag -->
<friend-contact name = "Tony"></friend-contact>
```

### [🌟] Validating Props

- makes sure that the data passed from parent component is valid

[*syntax*]

```js
export default {
    props : {
        type: ~type~/~func~,
    }
}
// ~func~ should return true/false 
```

### [🌟] Dynamic Prop Values

- to pass non-string values
- to loop through iterable

e.g. [using v-bind]
    `v-bind:isFavourite = "true"`

e.g. [Iterating and passing values as prop dynamically]

```html
<friend-request v-for = "friend in friends"
    :key = "friend.id"
    :name = "friend.name">
    
    ...
</friend-request>
```

### [🌟] [🌟] [🌟] Prop Fallthroughs

- vue has built-in support for prop "fallthrough"
- props and events that are not defined inside the child component will automatically fall through to the root component
- use the built in $attrs property to access these fallthrough props

### [🌟] [🌟] Custom Events (Child => Parent Communication)

- are emitted (via $emit) to trigger a method in a parent component
- can carry data which can be used in the called method

[*syntax*]

```js
// Child Component
export default {
    methods : {
        toggleFavourite: {
            this.$emit([~customEvent~], [~args~]...);
        }
    }
}
```

```html
<!-- Parent Component -->
<template>
    ...
        @~customEvent~="~code~"
    ...
</template>
```

### [🌟] Defining & Validating Custom Event

- for documentation of all custom events for improved code readiblity
- validation to ensure that all args required are passed when the event is emitted by default

e.g.

```js
// Child component
emits: {
    'toggle-favourite': function(id) {
        if (id) {
            return true;
        } else {
            console.warn("Id is missing");
            return false;
        }
    }
}
```

### [🌟] [🌟] Provide + Inject

- if data needs to be passed through the parent-child chain, use `provide`/`inject`
- `provide` in a parent component, `inject` it in a child component
- any component, regardless of how deep it is, can receive data by `inject` from `provide` in components higher in its parent chain

[*syntax*] Provide

```js
provide() {
    return {
        ...
    }
}
```

[*syntax*] Inject

```js
inject : [~key~, ...]
```

- Use Cases
    1. Properties/States

    2. Functions/Methods
        - providing function in the parent for the child to execute it

## Component Deep Dive

### [🌟] QoL

1. `#`
    - shorthand for v-slot:

    e.g.

    ```html
    <template #default>
        ...
    </template>
    ```

### [🌟] Global vs Local Components

Global Components
    - imported in main.js
    - can be accessed anywhere in the app
    - all global components are downloaded initially by the browser -> may be a problem for bigger application
    - ambiguous as to where the components are used as some may only be needed in certain areas  

Local Components
    - defined inside parent components
    - for components that are only used in one other component
    - keep main.js short

### [🌟] [🌟] Local Component Registration

[*syntax*]

```html
<script> 
~importStatement~

export default {
    components: {
        ~key~: ~value~ 

        OR 

        ~key~ // if the key has the same name as imported component
    }
}

</script>
```

### [🌟] Scoped Style

- by default, style scripts are applied globally
- it is implemented by assigning an attribute with an unique id
- to localise scope, use "scoped"

e.g.

```html
<style scoped>
...

</style>
```

### [🌟] Slots

- placeholder in parent  for dynamic HTML code

e.g.

```html
<!-- <MyComponent> Child Component -->
<template>
    <slot></slot> <!-- Slot Outlet -->
</template>
```

```html
<!-- Parent Component -->
<template>
    <MyComponent>
        <!-- Slot Content -->
    </MyComponent>
</template>
```

## [🌟] Named Slots

- A `<slot>` outlet without `name` implicityly has the name "default"
- to pass multiple slot content fragments, we need named slots

e.g.

```html
<!-- <MyComponent> Child Component -->
<template>
    <div>
        <slot name="header"></slot> <!-- "header" Slot Outlet-->
    </div>
    <div>
        <slot></slot> <!-- "default" Slot Outlet-->
    </div>
</template>
```

```html
<!-- Parent Component -->
<template>
    <MyComponent>
        <template v-slot:header>
            <!-- "header" Slot Content -->
        </template>
        <!-- "default" Slot Content -->
    </MyComponent>
</template>
```

### [🌟] Conditional Slots

e.g. Render only if slot exists

```html
<template>
    <header v-if="$slots.header">
        <slot name = "header">
            <!-- "header" Slot Content -->
        </slot>
    </header>
</template>
```

### [🌟] [🌟] Scoped Slots

- there are cases where it could be useful if a slot's content can make use of data from both the parent scope and the child scope
- to achieve that, we need a way for the child to pass data to a slot when rendering it
- we can pass attributes to a slot outlet just like passing props to a componnent

e.g.

```html
<!-- <MyComponent> Child Component-->
<div>
    <slot :text="greetingsMessage"
        :count="1">
    </slot>
</div>
```

```html
<!-- Parent Component -->
<MyComponent v-slot="slotProps">
    {{ slotProps.text }}
    {{ slotProps.count }}
</MyComponent>
```

- Props passed to the slot by the child are available as the value of the corresponding `v-slot` directive, which can be accessed by expressions ins ide the slot.
- Think of a scoped slot as a function being passed into the child component; the child component then calls it, passing props as arguments

### [🌟] Keeping Dynamic Components Alive

- wrapping dynamic component with a `<keep-alive>` element
- caches tab component instances once they are created for the first time
- any input field will retain its state even when not rendered

e.g.

```html
<keep-alive>
    <!-- Content -->
</keep-alive>
```

### [🌟] [🌟] Teleporting elements

- used to move elements around in the DOM tree
- for accessiblity and HTML semantics; nested elements may result in styling bugs

e.g.

```html
<teleport to="body">
    <!-- Content -->
</teleport>
```

### [🌟] Style Guide

- Read the [full guide](https://v2.vuejs.org/v2/style-guide/?redirect=true)

[Priority A: Essential]

- These rules help prevent errors, so learn and abide by them at all costs
- Exceptions may exist, but should be very rare and only be made by those with expert knowledge of both JavaScript and Vue

1. Multi-Word Component Names
    [✅] Component names should always be multi-word, except for root `App` componennts, and built-in components provided by Vue, such as `<transiton>` or `<component>`  
    - This prevents conflicts with existing and future HTML elements, since all HTML elements are a single word

2. Component Data
    [✅] value of `data` property on a component must be a function that returns an object
    - when the value of `data` is an object, it is shared across all instances of a component

    e.g.

    ```js
    // ❌ Bad
    export default {
        data: {
            foo: 'bar'
        }
    }
    ```

    ```js
    // ✅ Good
    export default {
        data() {
            return {
                foo: 'bar'
            }
        }
    }
    ```

3. Prop Definitions
    [✅] should be as detailed as possible
    - try to specify `type`, `required`, `validator`
    - `validator` accepts a validator function that returns a bool based on whether the received bool fulfills a condition

    e.g.

    ```js
    // ❌ Bad
    props : ['status']
    ```

    ```js
    // ✅ Good
    props: {
        status: {
            type: String,
            required: true,
            validator: function (value) {
                if (value.length > 10) {
                    return false
                } else {
                    return true
                }
            }
        }
    }
    ```

4. Keyed `v-for`
    [✅] `key` with `v-for` is always required on components, in order to maintain internal component state down the subtree.
    - updating the DOM, Vue will optimize rendering to perform the cheapest DOM muations. That might mean deleting the first element in the list, then adding it again at the end of the list
    - the problem is, there are cases it is important to delete element that will remian in the DOM.

5. Avoid `v-if` with `v-for`
    [✅] Do not use `v-if` on the same element as `v-for`
    - when Vue processes directives, `v-for` has a higher priority than `v-if`; Vue will iterate over and check the entire list every time we re-render, whether or not the values in the list have changed

6. Component Style Scoping
    [✅] Styles in a top-level `App` component and in layout components may be global, but all other components should always be scoped wiith `scoped` attribute
    - Consistent scoping ensure that styles only apply to the components they are meant for

7. Private Property Names
    [✅] Use module scoping to keep private functions inaccessible from the outside. If that is not possilbe, always use the `$_` prefix for custom private properties in a plugin, mixin, etc that should not be considered public API. Then to avoid conflicts with code by other authors, also include a named scope (e.g. `$_yourPluginName_`)
    - `_` prefix is used by Vue to define its own private properties, so using the same prefix risks overwriting an instance property

[Priority B: Strongly Recommended]

1. Component Files
    [✅] Whenever a build system is availabel to concatenate files, each component should be in its own file
    - This helps you to more quickly find a component when you need to edit it or review how to use it

    e.g. Bad

    ```js
    Vue.component('TodoList', {
    // ...
    })

    Vue.component('TodoItem', {
    // ...
    })
    ```

    e.g. Good

    ```text
    components/
    |- TodoList.vue
    |- TodoItem.vue
    ```

2. Component Names
    [✅] Filenames of single-file components should either be always PascalCase or always kebab-case

    e.g. Bad

    ```text
    components/
    |- mycomponent.vue
    ```

    ```text
    components/
    |- myComponent.vue
    ```

    e.g. Good

    ```text
    components/
    |- MyComponent.vue
    ```

    ```text
    components/
    |- my-component.vue
    ```

3. Base Component Names
    [✅] Base Components (aka presentational, dumb, or pure components) that apply app-specific styling and conventions should all begin with a specific prefix, such as `Base`, `App`, or `V`

    e.g. Bad

    ```text
    components/
    |- MyButton.vue
    |- VueTable.vue
    |- Icon.vue
    ```

    e.g. Good

    ```text
    components/
    |- BaseButton.vue
    |- BaseTable.vue
    |- BaseIcon.vue
    ```

    ```text
    components/
    |- AppButton.vue
    |- AppTable.vue
    |- AppIcon.vue
    ```

    ```text
    components/
    |- VButton.vue
    |- VTable.vue
    |- VIcon.vue
    ```

4. Single-instance Commponent Names
    [✅] Components that should only ever have a single active instance should begin the the `The` prefix, to denote that there can be only one
    - is only used once per page; never accepts any props, since they are specific to the app, not their context within the app

    e.g. Bad

    ```text
    components/
    |- Heading.vue
    |- MySidebar.vue
    ```

    e.g. Good

    ```text
    components/
    |- TheHeading.vue
    |- TheSidebar.vue
    ```

5. Tightly Coupled Component Names
    [✅] Child components that are tightly coupled with their parent should include the parent component name as a prefix

    e.g. Bad

    ```text
    components/
    |- TodoList.vue
    |- TodoItem.vue
    |- TodoButton.vue
    ```

    e.g. Good

    ```text
    components/
    |- TodoList.vue
    |- TodoListItem.vue
    |- TodoListItemButton.vue
    ```

6. Order of Word in Component Names
    [✅] Component names should start with the highest-level words and end with descriptive modifying words

    e.g. Bad

    ```text
    components/
    |- ClearSearchButton.vue
    |- ExcludeFromSearchInput.vue
    |- LaunchOnStartupCheckbox.vue
    |- RunSearchButton.vue
    |- SearchInput.vue
    |- TermsCheckbox.vue
    ```

    e.g. Good

    ```text
    components/
    |- SearchButtonClear.vue
    |- SearchButtonRun.vue
    |- SearchInputQuery.vue
    |- SearchInputExcludeGlob.vue
    |- SettingsCheckboxTerms.vue
    |- SettingsCheckboxLaunchOnStartup.vue
    ```

7. Component Name Casing in JS
    [✅] Component Names in JS should always be PascalCase, though they may be kebab-case inside strings for simpler applications that only use global component registration through `Vue.component`

    e.g. Bad

    ```js
    Vue.component('myComponent', {
    // ...
    })
    ```

    ```js
    import myComponent from './MyComponent.vue'
    ```

    ```js
    export default {
        name: 'myComponent',
        // ...
    }
    ```

    e.g. Good

    ```js
    Vue.component('MyComponent', {
    // ...
    })
    ```

    ```js
    import MyComponent from './MyComponent.vue'
    ```

    ```js
    export default {
        name: 'MyComponent',
        // ...
    }
    ```

8. Full-word Component Names
    [✅] Component names should prefer full words over abbreviations

9. Prop name Casing
    [✅] Prop names should always use camelCase during declaration, but kebab-case in templates and JSX

10. Multi-attribute elements
    [✅] Elements with multiple attributes should span multiple lines, with one attribute per line

11. Simple Expression in templates
    [✅] Component templates should only include simple expressions, with more complex expressions refactored into computed properties or methods

12. Simple Computed Properties
    [✅] Complex computed properties should be split into as many simper properties as possible

[Priority C: Recommended] EXISTS

## Forms

### [🌟] v-model

- listens and updates attribute
- <> Interaction with DOM

### [🌟] v-model Modifiers

1. `v-model.number`
    - forces `v-model` to convert input into number

2. `v-model.lazy`
    - v-model syncs with the state of the `Vue` instance on every input event while the .lazy modifier changes our `v-model` so it only syncs after change events

3. `v-model.trim`
    - removes leading and trailing white spaces

### [🌟] v-model Dropdowns

- works the same way for dropdowns

e.g.

```html
<template> 
    <div class="form-control">
        <label for="referrer">How did you hear about us?</label>
        <select id="referrer" name="referrer" v-model="referrer">
        <option value="google">Google</option>
        <option value="wom">Word of mouth</option>
        <option value="newspaper">Newspaper</option>
        </select>
    </div>
</template>

<script>
export default {
    data() {
        return {
            referrer: 'wom'
        }
    },
}
</script>
```

### [🌟] v-model checkboxes and radiobuttons

- checkboxes: as many options can be selected at once
- radiobutton: only one option can be selected at once

- for single-select, a bool is returned based on whether checkbox/radiobutton is selected; for multi-select, returns array

e.g.

```html
<template>
<form>

    <!-- Multi-select Checkbox -->
    <div>
        <div>
            <input name="interest" id="interest-tennis" type="checkbox" value="tennis" v-model="interest" />
        </div>
        <label for="interest-tennis">Tennis</label>

        <div>
            <input name="interest" id="interest-bowling" type="checkbox" value="bowling" v-model="interest" />
        </div>
        <label for="interest-bowling">Bowling</label>
    </div>   

    <!-- Single-select Checkbox -->
    <div>
        <input name="terms" id="terms-of-service" type="checkbox" v-model="toc"/>
        <label for="terms-of-service">Agree terms and conditions</label>
    </div> 
</form>
</template>

<script>
export default {
    data() {
        return {
            interest: [],
            toc: false,
        }
    }
}
</script>
```

### [🌟] [🌟] Using v-model on Custom Components

- special props ('modelValue') and event ('update:modelValue') used under the hood when v-model is used on custom components

e.g.

```html
<!-- Child Component -->
<template>
    <!-- ... -->
</template>

<script>
    export default {
        props: ['modelvalue'],
        emits: ['update:modelValue'],
    }
</script>
```

```html
<!-- Parent Component -->
<template> 
    <rating-form v-model="rating"></rating-form>
</template>
```

## HTTP requests

- allows the vue app to connect to a backend
- can be done more conveniently with third-party libraries like Axios

### [🌟] Requests

1. `POST` request
    - data is commonly transferred in the json format

    [*syntax*]

    ```js
    fetch(~URL~, {
        method: ~method~,

        //  METHOD : POST, GET, DELETE, ... 

        headers: {   

            // HEADERS : provides additional information about the context from which the request originated

        },
        body: {

            // BODY : data

        }
    })
    ```

    e.g. Firebase Server

    ```js
    fetch(
        'https://vue-http-demo-5801a-default-rtdb.asia-southeast1.firebasedatabase.app/surveys.json',
        {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name: this.userName,
            rating: this.chosenRating,
        }),
        }
    );
    ```

2. `GET` request
    - use Promnise as there may be a slight delay between request and response
    - typically called in the mounted() method  

    e.g. Firebase Server

    ```js
    fetch('https://vue-http-demo-5801a-default-rtdb.asia-southeast1.firebasedatabase.app/surveys.json').then(response => {
        if (response.ok) {
            return response.json();
        }
    }).then((data) => {
        console.log(data);
    })
    ```

### [🌟] Loading screen

e.g.

```html
<template>
    <p v-if="isLoading">Loading...</p>
</template>


<script>
export default {
    data() {
        return {
            this.isLoading = true
        }
    }

    methods: {
        fetch('https://vue-http-demo-5801a-default-rtdb.asia-southeast1.firebasedatabase.app/surveys.json').then(response => {
            if (response.ok) {
                return response.json()
            }
        }).then((data) => {
            this.isLoading = false
        })
    }
}
</script>
```

### [🌟] Catching Errors

1. Technical/Browser-side Errors (GET)

    e.g.

    ```js
    fetch(url)
    .then((response) => {
        // ...
    })
    .then((data) => {
        // ...
    })
    .catch((error) => {
        // ...
    })
    ```

2. Handling Error Response (POST)

    e.g.

    ```js
    fetch(url) {
        method: 'POST',
        headers : {
            // ...
        },
        body : {
            // ...
        }
    }
    // Bad request etc. 
    .then(response.ok) {
        // ...
    }


    // Technical Error - URL error etc.
    .catch((error) => {
        // ...
    })
    ```

## Routing

- allows us to build Single Page Applications (SPA) which are JavaScript driven client side web applications, entirely controlled by JS running in the browser
- has the same URl wherever you are on the applications

### [🌟] Installation

1. `cd` to the project
2. run `npm install vue-router@latest`

### [🌟] Setup

1. Imports
2. Registering Plugins
3. Rendering Components

e.g.

```js
/*
__________ main.js __________
*/

// 1. Imports 
import { createRouter, createWebHistory } from 'vue-router';

// 2. Registering Components
const router = createRouter({
    history = createWebHistory(),
    routes: [
        // Routes
    ]
})

app.use(router)
app.mount("#app")
```

```html
<!-- app.vue  -->
<template> 
    <router-view></router-view>
</template>
```

### [🌟] [🌟] Route Perimeters

1. `name: String`
    <> Dynamic Routes with named routes

2. `path: String`

3. `component: Object`
    - component to load when at path

4. `props: Bool`
    - determines whether route params are passed as props when routed
    - default: false

5. `redirect: String`
    - the path to which this path will redirect to in the event the user lands on it
    - the URL changes

6. `alias: String`
    - the URL does not change

7. `children: Object`

    e.g. Nested Routes

    ```js
    const router = createRouter({
        history: createWebHistory(),
        routes: [
            {
                path: '/users', 
                component: Users,
                children: [
                    { path: ':userId', component: IndividualUsers, props: true},
                    ...
                ]
            }
        ]
    })
    ```

### [🌟] Navigating

- `<router-link>` will not reload the whole page

[*syntax*] `<router-link :to="~route~"></router-link>`

e.g. Dynamic Paths

```html
<router-link :to="'/users/' + id">View user</router-link>
```

### [🌟] Programmatic Navigation

- navigate to another page when a certain event happens

1. `this.$router.push(~destinationPage~)`
    - redirects user to specified page

2. `this.$router.forward()`
    - emulates the default browser forward feature

3. `this.$router.back()`
    - emulates the default browser back feature

### [🌟] [🌟] Styling Active Links

- use the .router-link-active in styles to set property of elements that are tagged with "router-link-active"
- to change the default class names, set some optionos in the createRouter function

e.g.
    const router = createRouter({
        ...
        linkActiveClass: 'active',
        linkExactActiveClass: 'exact-active',
    })

### [🌟] [❗] Dynamic Routes

- map routes with similar pattern to the same component
- always put dynamic routes after static routes to prioritise static routes

e.g.

```js
    // main.js
    const routes = [
        { path: '/users/:id', component: User}
    ]
```

```js
// Component
console.log(this.$route.params.id); 

// use this.$route.params.id to access the parameters specific to the dynamic route
```

### [🌟] Updating param data with watch

- in some cases, redirecting from one dynamically generated route to another can result in no change at all -> data is loaded when page is first rendered
- use watch to re-render the page when the route param is changed so that the page change is reflected

e.g.

```js
watch: {
    $route(newRoute) {
        loadPage(newRoute);
    }
}
```

### [🌟] "Catch all" Route

- to deal with routes that are not defined
- added at the end so that it does not overwrite any other routes

e.g.

```js
const router = createRouter(
    history: createWebHistory(),
    routes: [
        // other static, dynamic routes
        {path: '/:notFound(.*)', redirect: '/users'} // Catch all route
    ]
)
```

### [🌟] Nested routes

- use `<router-view>` in route component to display nested route component

### [🌟] Named routes

- routes generated dynamically with `name` attribute will still work even if routepath is changed in main.js

e.g.

```js
computed: {
    linkTo() {
        return { name: 'user', params: { id: this.id} }
    }
}
```

### [🌟] Query Params

- the `?` in webpage links
- are optional, thus does not need to be included in the route object
- can be accessed by `this.$route.query`

e.g.

```js
computed: {
    linkTo() {
        return { 
            name: 'user', 
            params: { id: this.id},
            query: {
                sort: "asc",
            }
            
        }
    }
}
```

### [🌟] Rendering Multiple Routes on Single Page

- using named `<router-view>`

e.g.

```html
<template>
    <div>
        <router-view></router-view>
    </div>
    <div>
        <router-view name="remarks"></router-view>
    </div>
</template>
```

```js
const router = createRouter(
    history: createWebHistory(),
    routes: [
        {
            path: '/users',
            components: {
                default: UsersList,
                footer: UsersFooter,
            },
        }
    ]
)
```

### [🌟] [🌟] Controlling Scroll Behaviour

- include `scrollBehaviour(to, from, savedPosition)` in router object

e.g.

```js
const router = createRouter({
    // ...
    scrollBehaviour(to, from, savedPosition) {
        // console.log(to, from, savedPosition);
        if (savedPosition) {
            return savedPosition
        } else {
            return {left: 0, top: 0}
        }
    }
})
```

### [🌟] [🌟] Navigation Guard

- used to redirect or canceling navigation
- verify/authenticate that user has permission to proceed to destination page

[*syntax*]

```js
beforeEach(function(to, from, next) {
    // ...
    if (condition):
        next(); // next() redirects the user
    return false // false cancels navigation
})
```

1. Global Navigation Guard
    - runs every single time route changes
    - register global before guards using `router.beforeEach`

    [*syntax*]

    ```js
    router.beforeEach(function(to, from, next) {
        if (condition):
            next();
    })
    ```

2. Per-route Navigation Guard
    - only runs when users are at a specific route
    - defined either
        1. `beforeEnter` guards directly on a route's configuration object

        2. `beforeEnter` guards in the component

    e.g. Route Configuration Object

    ```js
    const routes = [
        {
            path: '/users/:id',
            component: UserDetails,
            beforeEnter: (to, from) => {
                // reject the navigation 
                return false
            }
        }
    ]
    ```

    e.g. Component

    ```js
    export default{
        beforeEnter(to, from, next) {
            if (condition) {
                next()
            }
            return false
        }
    }
    ```

3. Special Use Case Reloading component
    - applicable for components that are not reloaded but instead reused

    e.g.

    ```js
    export default {
        beforeRouteUpdate(to, from, next) {
            loadTeamMembers(to.params.teamId);
            next()
        }
    }
    
    ```

4. `aftereach()` Guard
    - useful to logging information to server as it is too late at this point to affect users

5. Route Leave Guard
    - allows route navigation to be cancelled in situations such as unsaved forms etc

    e.g.

    ```js
    beforeRouteLeave() {
        if (this.savedChanges) {
            next(true);
        } else {
            const result = confirm("Unsaved Changes. Are you sure to proceed?");
            next(result)
        }
    }
    ```

### [🌟] [🌟] Route Metadata

- used to store arbitrary information e.g. transition, names or auth
- used in navigation guides and accessed inside the route with `.meta.~attribute~`

[*syntax*]

```js
route : [
    {
        // ...
        meta : {
            'needsAuth' : false,
        }
    }
]
```

## Composition API

### [🌟] Why?

- substitute to Options API
- a function-based solution that allows you to keep logically related code together

e.g. Comparing Options vs Composition API

```js
// Options API
export default {
    data() {
        return { name: 'Max'}
    },
    
    methods: { doSmth() {...} }
}
```

```js
// Composition API

export default {
    setup() {
        const name = ref('Max');
        function doSmth() {...};
        return { name, doSmth };
    }
}

```

### [🌟] API Setup

- is called by Vue on component creation; should define all data + logic for initial render
- receives two arguments automatically: reactive props and context
- setup() or `<script setup></script>`

### [🌟] 'data' -> `ref()`

- replaces `data() {...}` used in Options API
- 'ref' creates a reactive value that vue can keep track of
- `ref.value` to access value stored
- passing `ref` will allow template to pick up changes to `ref.value`
- `setup()` returns an object that holds key-value pairs to expose refs  

e.g. Setup Function

```html
<script>
    import { ref } from 'vue';

    export default {
        setup() {
            let uName = ref('Harry');

            return { userName : uName };
        }
    }
</script>
```

e.g. Setup HTML Tag

```html
<script setup>

import { ref } from 'vue';

const uName = ref('Maximilian');

setTimeout(function() {
    uName.value = 'Max';
}, 2000);

</script>
```

### [🌟] 'data' -> 'reactive({...})'

- using `reactive` from vue (reactive only works on objects)
- 'isReactive' to test whether the object is reactive
- 'toRefs' converts a normal object into one that has all its attribute as refs

e.g. Comparing Refs and Reactive

```html
<!-- Refs -->
<script setup>

const user = refs({
    name: 'Harry',
    age: 16,
})

user.value.name = 'Tony';

return {user: user}

</script>
        
    }
```

```html
<!-- Reactive -->
<script setup>

const user = reactive({
    name: 'Harry',
    age: 16,
})

user.age = 17; // shorter code 

return {user: user};
    
</script>
```

### [🌟] 'methods : {}' -> nested functions

- instead define and return functions inside `setup()`

e.g.

```html
<script>

import { ref } from 'vue';

setup() {
    const uAge = ref(31);

    function setNewAge() { // Define setNewAge()
        uAge.value = 32
    };

    return { userName: uName, setAge: setNewAge} // Return a key-value pair with setNewAge()
}

</script>
```

### [🌟] `computed : {}` -> `computed()`

- with `computed(~function~)`

e.g.

```html
<script>

import { computed } from 'vue';

setup() {
    const username = computed(function() {
        return firstName + ' ' + lastName;
    })
}
</script>
    
```

### [🌟] `watch : {}` -> `watch()`

- using `watch(~dependencies~, ~function~)`
- dependencies : either one object or a list of objects
- function : executed once the dependency changes

e.g.

```html
<script>

import { watch } from 'vue';

setup() {
    watch(uName, function(oldValue, newValue) {
        console.log(`Old age value: ${oldValue}`);
        console.log(`New age value: ${newValue}`);
    })
}

</script>
```

### [🌟] [🌟] Template refs

- used for direct access to underlying DOM elements. To achieve this, we can use the special `ref` attribute on an element

e.g.

```html
<template>
    <p2>{{ age }}</p2>
    <div>
        <input type="text" placeholder="Age" ref="ageInput"/>
        <btn @click="setAge"></btn>
    </div>
</template>

<script setup>

const ageInput = ref(null); // as ref
const age = ref('');

const setAge = function() {
    age.value = ageInput.value.value;

    // Note that: ageInput.value is a pointer to the DOM element, thus its .value will be the value input
}

</script>
```

### [🌟] Components, Props

- mostly the same as option API
- `setup()` receives two parameters by default: `props`, `context`

e.g. Script

```html
<script>

export default {
    props : {
        // ... 
        // refer to Options API prop definition
    },

    setup(props, context) {
        const uName = computed(function() {
            return props.firstName + ' ' + props.lastName; // use props.[property] to access prop property
        })
    }
}

</script>
```

e.g. Script Setup Tag

```html
<script setup>
    import { computed, defineProps } from 'vue';
    
    /*
    import ... // importing component; value in the scope of <script setup> can be used directly as custom component tag names
    */

    const props = defineProps(['firstName', 'lastName']);

    const uName = computed(function() {
        return props.firstName + ' ' + props.lastName;
    })
</script>
```

### [🌟] Emitting custom event

- instead of Options API `this.$emit()`, we use `context.emit()` in Composition API

e.g.

```html
<script>

export default {
    setup(props, context) {
        context.emit('event-proceed', auth);
    }
}
</script>
```

### [🌟] `Provide`, `Inject`

- instead of Options API's `provide() { return { ... }}`, in Composition API we use `provide(~key~, ~value~)`
- `key` : injection key which is used by child components to lookup the desired value to inject
- `value` : provided value; can be of any type, including reacttive state such as refs
- instead of Options API's `inject: [...]`, in composition API, we use `inject(~key~)`

e.g.

```html
<!-- Parent Component -->
<script>

import { ref, provide } from 'vue'

export default {
    const age = ref(19);
    setup() {
        provide('age', age)
    }
}

</script>
```

```html
<!-- Child Component -->
<script>
import { inject } from 'vue'

export default {
    setup() {
        const age = inject('age') // use the same 'key' used in parent component; 
    }
}
</script>
```

### [❗] Summary

1. data
    - `data() { return {} }` -> `ref({...})`
    - `data() { return {} }` -> `reactive({...})`

2. methods
    - `methods : {}` -> nested functions

3. computed
    - `computed: {}` -> `computed(~function~)`

4. watch
    - `watch()` -> `watch(~dependencies, function(oldValue, newValue))`

5. provide + inject
    - `provide() { return {} }` -> `provide(~key~, ~value~)`
    - `inject[...]` -> `inject(~key~)`

### [🌟] Lifecycle Hooks

- import it as a function and call it within the setup function

[Options API  -> Composition API]

1. beforeCreate, created -> Not needed (setup() replace these hooks)

2. beforeMount, mounted -> onBeforeMount, onMounted

3. beforeUpdate, updated -> onBeforeUpdate, onUpdated

4. beforeUnmount, unmounted -> onBeforeUnmount, onUnmounted

### [🌟] Routing

1. `$route.params`
    a. pass route params as props

    b. importing composition hooks

    e.g.

    ```html
    <script>
    
    import { useRouter } from 'vue-router';

    export default{
        setup() {
            const router = useRouter();
            const id = router.params.id;
        }
    }
    </script>
    ```

2. Programmatic Navigation
    a. use composition hooks

    e.g.

    ```html
    <script>
    
    import {useRouter} from 'vue-router';

    const router = useRouter();

    const onClick = function() {
        router.push('/details/')
    }
    </script>
        
    ```

## Reusing Code

- Mixins (Options API)
- Custom Composition Functions (Composition API)
