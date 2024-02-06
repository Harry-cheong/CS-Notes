# JavaScript

## [🌟] [🌟] [🌟] JavaScript

1. High-Level

   - Do not need to manage resources
     e.g. Python, JS

2. Garbage-collected

   - Cleaning the memory so we don't have to

3. Interpreted or just-in-time complied

   - higher abstraction

4. Multi-paradigm

   - An approach and mindset of structuring code, which will direct your coding sytle and technique
   - Paradigms consist of Procedural Programming, Object Oriented Programming and Functional Programming

5. Protype-based object-Oriented
   <> Object Oriented Programming

6. First-class functions

   - functions are simply treated as variables

7. Dynamic

   - data types are automatically determined during runtime

8. Single-threaded

   - JavaScript runs in one single thread, so it can only do one thing at a time

9. Non-blocking event loop
   - an event loop takes long running tasks, executes them in one "background", and puts them back in the main thread once they are finished.

## ▷▷▷▷▷ C01: Resources ◁◁◁◁◁

1. [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

---

## ▷▷▷▷▷ C02: IO ◁◁◁◁◁

### [🌟] Output

1. `console.log(..., ..., ...)` -> unlimited var, executes js to c results on console

### [🌟] Input

1. `prompt(~promptmsg~)` -> returns a str

---

## ▷▷▷▷▷ C03: Types ◁◁◁◁◁

### [🌟] Primitive Data Types

- stored in the call stack, as part of an execution context

  1. `Number`: All numbers, used for decimals and ints
  2. `String`
  3. `Boolean`: true/false (not in upper case)

     / Falsy and Truthy Values

     - 5 Falsy Values; 0, '', undefined, null, Naming
     - All other objects are truthy values

  4. `Undefined`: Value taken by a varable that is not yet defined('empty value')
  5. `Null`: Also means 'empty value'
  6. `Symbol` (ES2015): Value that is unique and cannot be changed
  7. `BigInt` (ES2020): Large integers that the Number type cannot hold

  - JavaScript has dynamic typing: not need to manually define the data type of the value; automatic
    One variable can be changed from one type to another w.o. an error

### [🌟] Reference Types

- stored in the heap

  1. Object literal
  2. Arrays
  3. Functions
  4. Many more...

### [🌟] [🌟] Primitive vs Reference Types

e.g. [Primitive]

```js
let age = 30; // the identifier 'age' points to the address where 30 is stored
let oldAge = age;
age = 31;
console.log(age); // 31
console.log(oldAge); // 30
```

e.g. [*Reference Types*]

```js
const me = {
  name: "Jonas",
  age: 30,
};
const friend = me; // points to the same ref as me
friend.age = 27;
console.log("Friend", friend); // {name: 'Jonas', age: 27}
console.log("Me", me); // {name: 'Jonas', age: 27}
```

- Implication is that new variables created are actually pointing at the same object

### [🌟] Functions ${03-functions}

1. `typeof`
   e.g. typeof true

### [🌟] Type Conversion

1. Number() -> converts str to num
   e.g. console.log(Number('1991'))

2. String() -> Converts num to str

3. Boolean() -> converts truthy and falsy values to true and false respectively
   - refer to section on truthy and falsy values
   - very rarely used; typically type coercion happens instead for logic operations

### [🌟] [🌟] [🌟] Type Conversion vs Type Coercion

- Type Conversion is manual
- Type Coercion is automatic, js does the conversion behind the scene

  e.g. [*Type Coercion*]

```js
console.log("I am" + 23 + "years old");
console.log("23" - "10" - 3);
```

-> [+] triggers conversion of str to num by type coercion
-> [-] [*] [/] triggers conversion of num to str by type coercion

---

## ▷▷▷▷▷ C04: Variables ◁◁◁◁◁

### [🌟] Defining Variables

1. `let`

   - Defining mutable var

     e.g.

   ```js
   let js = let jonas_matilda = "JM";
   age = 31;
   ```

2. const

   - Defining Immutable Variables
   - Cannot be empty
   - Default for clean code, keeping mutable var to a min

     e.g.

   ```js
   const birthYear = 1991;
   ```

3. var [Advanced]

   - avoid using
   - creates a new property in object window
     <> Behind the Scene JavaScript - Hoisting

     e.g.

     ```js
     var job = "programmer";
     job = "teacher";
     ```

### | [🌟] Naming Conventions |

1. Never start normal variables with capital letters
   Variables with capital letters are reserved for OOP

2. Only can use symbols '$' and '\_' before variable

3. var firstNamePerson -> f (lower case), N and P (upper case)

4. var with all upper case is reserved for constants that will never change

   e.g.

   ```js
   let PI = 3.1415;
   ```

5. Be clear when naming variables

---

## ▷▷▷▷▷ C05: Strings ◁◁◁◁◁

### [🌟] Format

1. backticks `

   - template str/literal
   - works for any str

     [*Syntax*]
     `... ${any var/js expression}`

   e.g.

   ```js
   const jonasNew = `I'm ${any var/js expression}`
   ```

2. `\n\`

   - to move to the next line in a '' str
   - not the case for `` str

### [🌟] Properties {#05-properties}

1. `.length`
   - the length of the string

### [🌟] [🌟] Methods {$05-methods}

- Calling a method on a string converts it to an object, and after it's done, it is converted back to a primitive type

  e.g.

  ```js
  console.log(typeof new String('Jonas')) // returns Object`

  console.log(typeof new String('Jonas).slice(0, 3)) // returns string
  ```

  1. `.indexOf(~element~)`

     - returns the index of specified element from the front
     - case sensitive

  2. `.lastIndexOf(~element~)`

     - finding and returning the index of specified element from the end
     - case sensitive

  3. `.slice(~beginIndex~, ~endIndex~)` -> startIndex is incl, endIndex is excl

     - slices the string into a substring
     - does not modify the og string

  4. `.toLowerCase()`

     - lowercases all chars in the string
     - does not modify the og string

  5. `.toUpperCase()`

     - uppercases all chars in the string
     - does not modify the og string

  6. `.trim()`

     - removes whitespace from both ends of a string and returns a new string
     - does not modify the og string

  7. `.trimStart()`

  8. `.trimEnd()`

  9. `.replace(~substring~, ~substring~)`

  10. `.replaceall(~substring~, ~substring~)`

      - finds and replaces all occurrences of a substring

  11. `.includes(~substring~)` // returns bool

      - checks whether the string contains the substring

  12. `.startsWith(~substring~)` // returns bool

      - checks whether the starts with the specified substring

  13. `.endsWith(~substring~)`

  14. `.split(~separator~)` // returns an array

  15. `.padStart(~desiredlen~, ~fillerchar~)`

      - adds the fillerchar at the start of the string until the desired len is reached

  16. `.padEnd(~desiredlen~, ~fillerchar~)`

  17. `.repeat(~count~)`
      - repeats the string count no. of times

## ▷▷▷▷▷ C06: Numbers ◁◁◁◁◁

- all numbers are stored as floating points

### [🌟] Numeric Separators

- for ease of interpreting large values
- cant put underscore before and after decimal point

  e.g. [287,460,000,000]

  ```js
  const diameter = 287_460_000_000;
  console.log(diameter); // returns 287460000000
  ```

### [🌟] Properties {#06-properties}

1. Math.MAX_SAFE_INTEGER
   - 9007199254740991; the largest number that can be safely represented by JavaScript

### [🌟] Functions {#06-functions}

1. `Number.parseInt([*string*], [*regex*])`

   - [regex] : the base of the number system we are using - searches for numbers from the start of the string

   e.g.

   ```js
   console.log(Number.parseInt("30px", 10)); // returns 30
   console.log(Number.parseInt("e23", 10)); // returns NaN
   ```

2. `Number.parseFloat([*string*])`

   - also searches for decimals

   e.g.

   ```js
   console.log(Number.parseFloat("  3.5rem  ")); // returns 3.5

   // In comparison ...
   console.log(Number.parseInt("  3.5rem  ")); // returns 3
   ```

3. `Number.isNaN([*value*])`

   - checks whether value is NaN (Not a Number)
   - edge case: 23/0

   e.g.

   ```js
   console.log(Number.isNaN(23 / 0)); // returns false; does this mean it is a number?
   ```

4. `Number.isInteger([*value*])`
   - checks whether value is Finite
   - works for any rational number

### [🌟] BigInt

- used to store and represent values larger than Number.MAX_SAFE_INTEGER
- include n at the end of the number to convert it to BigInt OR using `BigInt()` constructor
- arithmetic operators work with BigInts
- any functions or methods from math class does not work

e.g. [*adding n*]

```js
console.log(34891284892348129n);
```

e.g. [using constructor]

```js
console.log(BigInt(2342813490));
```

## ▷▷▷▷▷ C07: Math ◁◁◁◁◁

### [🌟] Properties ${07-properties}

1. `Math.PI`
   - pi value

### [🌟] Generic

1. `Math.random()`

   - returns a random floating number between 0 and 1

2. `Math.sqrt([*number*])`

   - sqrts the number

3. `Math.max([*array*])`

   - returns the highest number in an array

4. `Math.min([*array*])`
   - returns the smallest number in an array

### [🌟] Rounding

1. `Math.trunc()`

   - removes all the decimals; rounding integers

2. `Math.round([*float*])`

   - always rounds to the nearest integer

3. `Math.ceil([*float*])`

   - always round up to the largest integer

4. `Math.floor([*float*])`

   - always round down to the smallest integer

5. `[*decimal*].toFixed(*noOfDecimalPlaces*)`
   - rounds to nearest noOfDecimalPlaces

## ▷▷▷▷▷ C08: QoL ◁◁◁◁◁

### [🌟] Commenting

```js
/*
    (Anything here is ignored by console)
    */
```

### [🌟] Refractoring Code

- Finding a general case for if..else statements
  e.g. instead of when score > guess and score < guess, use a single case score != guess ..
- Creating functions

## ▷▷▷▷▷ C09: Operators ◁◁◁◁◁

### [🌟] Arithmetic Operators

1. `-`

2. `+`

3. `*`

4. `**` : Exponential

5. `/`

6. `%` : Remainder

   - used to check for odd and even numbers

   e.g.

   ```js
   const isEven = (n) => num % 2 === 0;
   ```

### [🌟] Assignment Operators

1. `+=`, `-=`, `*=`

2. (new) `++`

   e.g. [*Suffixed ++*]

   ```js
       let x = 0;
       console.log(x++) // returns 0
       console.log(x) // returns 1
   * x++ returns the origianl value of x
   ```

   e.g. [Prefixed ++]

   ```js
       let x = 0;
       console.log(++x) // returns 1
   * ++x returns the new value of x
   ```

3. (new) `--`
   e.g. `x-- // x = x - 1`

### [🌟] Comparison Operators

1. `>`
2. `<`
3. `>=`
4. `<=`

### [🌟] Boolean Operators

1. `&&` : and

   - `&` : evaluates both side of the operator
   - `&&` : evaluates the RHS only if the LHS is true
   - [❗] Short Circuiting - shorts circuit when the value is falsy

   e.g.

   ```js
   console.log(0 && "Jonas"); // returns 0
   ```

2. `||` : or

   - [❗] Short Circuiting
   - shorts circuit when the value is truthy

   e.g.

   ```js
   console.log(undefined || 0 || "" || "Hello" || 23 || null); // returns 'Hello'
   ```

3. `!` : not

### [🌟] [🌟] [🌟] Logical Assignment Operators (ES2021)

1. `||=`

   - assigns value to the variable if that exact variable is currently falsy
   - red herring: 0 is also a falsy value

   e.g.

   ```js
   let owner = null;
   owner ||= "Harry";
   console.log(owner); // returns 'Harry'
   ```

2. `??=`

   - assigns value to the variable if that exact variable is currently nullish
     e.g.

   ```js
   let noOfGuest = 0;
   noOfGuest ??= 10;
   console.log(noOfGuest); // returns 0
   ```

3. `&&=`

   - assigns value to the variable if that exact variable is currently truthy

   e.g.

   ```js
   let owner = "Harry";
   owner &&= "<ANOYMOUS>";
   console.log(owner); // returns <ANOYMOUS>
   ```

### [🌟] [🌟] Equality Operations

<> Type Conversion vs Type Coercion

1. `===` or strict equality operation

   - No Type Coercion
   - default; for clean code

2. `==` or loose equality operation

   - Type Coercion

3. `!==`

### [🌟] [🌟] [🌟] Ternary/Conditional Operator

- shortform for if..else statement

1. `?` -> when condition is true
2. `!` -> when condition is false

e.g. [*Comparison with if..else*]

```js
  const age = 23;
  e.g. [w. statements]
  age >= 18
  ? console.log('I like to drink wine')
  : console.log('I like to drink water');

  e.g. [w. expressions]
  const drink = age >= 18 ? 'wine' : 'water';
  console.log(drink);

  console.log(`I like to drink ${age >= 18 ? 'wine': 'water'}`)
```

```js
    e.g.
    let drinkk:
    if (age>=18) {
    drink2 = 'wine';
    } else {
    drink2 = 'water';
    }
    console.log(drink2)
```

- In conclusion, the use of the conditional operator makes code shorter and cleaner

### [🌟] [🌟] Spread Operator

- works on all iterables e.g. strings, maps, arrays and sets etc.
- used in places where otherwise values separated by commas are written
  [*Syntax*]

  ```js
  const ~var~ = [1, 2, ...[3, 4]] // ... on the right side of the operator, thus SPREAD
  ```

Use cases

1. Arrays when individual elements of an array is needed

   e.g.

   ```js
   const arr = [7, 8, 9];
   const newArr = [1, 2, ...arr];
   console.log(newArr); // returns [1, 2, 7, 8, 9]
   ```

   e.g. [*Breaking arrays into individual elements*]

   ```js
   console.log(...arr); // returns 7 8 9
   ```

   e.g. [*Copy array*]

   ```js
   const copyArray = [...arr];
   ```

   e.g. [*Join 2 arrays*]

   ```js
       const joinedArray = [...arr, ...newArr]\
   ```

2. Strings

   e.g.

   ```js
   const str = "James";
   const letters = [...str, "", "s."];
   console.log(letters);
   ```

3. Objects
   - `...[*object*]` returns all the properties of an object

### [🌟] [🌟] Rest Pattern

1. Destructuring

   - collect unused elements in a destructuring operation
   - must be the last element
   - can only be one in a destructuring operation

   e.g.

   ```js
   const [a, b, ...others] = [1, 2, 3, 4, 5];
   console.log(others); // returns [3, 4, 5]
   ```

2. Functions

   - using rest parameters/arguments

   e.g.

   ```js
   const add = function(...numbers) {
       let sum = 0;
       for (num : numbers)
   }
   ```

### [🌟] [🌟] [🌟] Nullish Coalescing Operator (ES2020)

- only considers nullish values: null and undefined (NOT 0 or '')
- works with shortcircuiting

e.g.

```js
guestNum = 0;
const guests = guestNum ?? 10;
console.log(guests); // returns 0

// HOWEVER, with...

const guests = guestNum || 10;
console.log(guests); // returns 10
```

### [🌟] [🌟] [🌟] Operator Precedence

- good to have a general idea

```js
    // From most precedence to lowest precedence
    21 - Grouping [(...)]
    16 - [**]
    15 - [*] [/] [%]
    14 - [+] [-]
    13 - Bitwise Operations
    12 - [>] [<=] [>] [>=]
    11 - [==] [!=] [===] Strict Equality
    3 - Assignment
```

## ▷▷▷▷▷ C10: Logic Operations ◁◁◁◁◁

### [🌟] If-Else Statements

[*Syntax*]

```js
if (~condition~) {
...

    } else if (~condition~) {
        ...

    } else {
        ...

    }
```

### [🌟] Switch Statements |

e.g.

```js
const day = 'monday';

switch (day) {
    case 'monday': // day === 'monday' -> strict Comparison
        console.log('Monday')
        break;

    case 'wednesday':
    case 'thursday': -> (if day === 'wednesday' or day === 'thursday' )
        console.log('wednesday or thursday');
        break;

    default: -> works similar to else
        console.log('Not mon, weds or thurs')
}
```

### [🌟] Statement vs Expression

- Expression returns a value

e.g.

```js
3 + 4;
true && false && !false;
```

- Statement does not return a value

e.g.

```js
const str = "23 is bigger";
```

- [❗] Important to know as js expect expression/statement in certain contexts

e.g.

```js
const me = "Jonas";
console.log(`I'm ${2037 - 1991} years old ${me}`);
```

## ▷▷▷▷▷ C11: Loops ◁◁◁◁◁

### [🌟] For-Loop

- run the loop for a specific no of times

1. Default statement
   [*Syntax*]

   ```js
   for (~counter~; ~running when condition true~; ~update the counter~) {
   ...
   };
   ```

   e.g. [*Looping forward*]

   ```js
   for (let i = 0; i < years.length; i++) {
     ages.push(2037 - years[i]);
   }
   ```

   e.g. [*Looping backward*]

   ```js
   for (let i = jonas.length - 1; i >= 0; i--) {
     ages.push(2037 - years[i]);
   }
   ```

2. For...of loops
   [*Syntax*]

   ```js
   for (const ~placeholder~ of ~iterable~) {
   ...
   }
   ```

### [🌟] Keywords {10-keywords}

1. `continue`

   - Exits the current iteration of the loop

2. `break`

   - Exits the whole loop

### [🌟] While-Loop

- can only specify the Condition
- used when the duration of the loop is unknown

e.g.

```js
let rep = 1;
while (i <= 10) {
  console.log(`Lifting weights repetiition ${i}`);
  rep++;
}
```

## ▷▷▷▷▷ C12: Strict Mode ◁◁◁◁◁

- Must be on the first line of the script
- Write more secure code; avoid accidental bugs into the code
- How it helps:

1. Forbids certain 'things' ?

   - Reserved names that may be used in the future

   e.g.

   ```js
   const interface = "Audio";
   const private = 534; // 'Uncaught SyntaxError: Unexpected strict mode reserved word' in console
   ```

2. Produce visible errors in certain situation where javascript without strict mode will fail silently

   e.g. [*discreet error becoz no strict mode*]

   ```js
   // 'use strict'; -> no strict mode
   let hasDriversLicense = false;
   const passTest = true;
   if (passTest) hasDriverLicense = true;
   if (hasDriversLicense) console.log("I can drive :D");
   ```

   - in this case, no output in console

   e.g. [Conversely]

   ```js
   "use strict";
   ```

   - in this case, 'script.js:6 Uncaught ReferenceError: hasDriverLicense is not defined' in console

## ▷▷▷▷▷ C13: Functions ◁◁◁◁◁

- reusable code blocks
- dry (dun repeat urself) code

### [🌟] Declaration

- A function can be called before initialization/declaration

e.g.

```js
console.log(fruitProcessor(3, 4));
function fruitProcessor(apples, oranges) {
  console.log(apples, oranges);
  const juice = "Juice with ${apples} and ${oranges} oranges.";
  return juice;
}
```

e.g. [*Function Expression*]

```js
const calcAge2 = function (birthYear) {
  return 2037 - birthYear;
};
const age2 = calcAge2(1991);
```

### [🌟] Default Parameters

- simplying specifying the default value w '=' operator

e.g.

```js
const createBooking = function(flightNum, numPassengers = 1, price = 199) {
...
}
```

### [🌟] Properties {12-properties}

1. .name
   - name of function

### [🌟] How passing arguments work: Values VS References

- Primitive types are copied.
- Reference types e.g. objects are passed as a reference to the object in the memory heap but it points to the same object and the object itself will be manipulated
- take note that 2 functions can manipulate a single object, causing bugs
- JavaScript can only pass by values. In some cases, it is seems as if arguments are passed by "reference" but it is simply a value that contain a memory address

### [🌟] [🌟] Arrow Function

- Why should I choose arrow fn? 'this' keyword? Topic for later chapters
- '=>' keyword

1. One-line

   - Value is returned implicitly when there is no function body that is {...}

   e.g.

   ```js
   const calcAge3 = (birthYear) => 2037 - birthYear;
   ```

2. Multi-line, multi-var

   - Value has to be returned explicitly with 'return' keyword

   e.g.

   ```js
   const yearsUntilRetirement = (birthYar, firstName) => {
   ...
   }
    console.log(yearsUntilRetirement(1991, 'Jonas'))
   ```

### [🌟] [🌟] [🌟] First-Class vs Higher-Order Functions

a. First-Class

- just a concept; no such jargon in JavaScript
- treated as another "type" of object / simply values

- Use Cases:

1. Store functions in variable or properties

   e.g.

   ```js
   const add = function (a, b) {
     return a + b;
   };
   ```

2. Pass functions as arguments to OTHER functions

   e.g.

   ```js
   const greet = () => console.log("Hey User");
   btnClose.addEventListener("click", greet);
   ```

3. Return functions FROM functions

4. Call methods on functions

   e.g.

   ```js
   counter.inc.bind(someOtherObject);
   ```

b. Higher-order

- a fn that receives another function as an argument that returns a new function, or both
- only possible because of first-class fns
- Very commonly used in JavaScript as it creates [❗] a level of abstraction i.e. hiding details to enable a bigger picture

- Use Cases:

  1. Function that receives another function

     e.g.

     ```js
     btnClose.addEventListener("click", greet);
     ```

     - greet is known as a callback fn while addEventListener is known as a higher-order function

  2. Function that returns new function

     e.g.

     ```js
     function count() {
       // Higher Order function
       let counter = 0;
       return function () {
         // Returned function
         counter++;
       };
     }
     ```

### [🌟] [🌟] Function Accepting Callback Functions

e.g.

```js
const math = function (int, fn) {
  console.log(`Result: ${fn(int)}`);
};

const double = function (a) {
  return a * a;
};

math(8, double);
```

### [🌟] [🌟] Functions Returning Functions

e.g.

```js
const greet = function (greeting) {
  return function (name) {
    console.log(`${greeting} ${name}`);
  };
};

greet("Hey")("Jonas");
```

e.g. [Using arrow functions]

```js
const greet = (greetings) => (name) => {
  console.log(`${greeting} ${name}`);
};
```

### [🌟] [🌟] [🌟] Function Methods

1. `.call(~this~, ...args)`

    - specifies what 'this' refers to in the function
    - ...args are simply the args the function normally receives
    - calls the fn

2. `.apply(~this~, [...args])`

    - works the same way as .call except it takes an array of args
    - calls the fn

3. [❗] `.bind(~this~, ..otherFixedArgs)`

    - it does not immediately call the function, instead it returns a new function where the 'this' keyword is bound to the one specified
    - ...otherFixedArgs are args that are fixed for any call of the binded function down the road
    - use `null` to skip the first perimeter

    e.g.

    ```js

    const shinkansen = {
        country: JPN,
        speed: 800,
        rating: 5,
        reviews: [],
        addReview(user, text, time) {
            this.reviews.push(`At ${time}, ${user} posted ${text}`)
        }
    }

    const HSR = {
        country: PRC
        speed: 500,
        rating: 3,
        reviews: [],
    }

    const revShinkansen = addReview.bind(shinkansen, 'Harry');
    revShinkansen('It was a pleasant ride', 0900); // the object shinkansen is updated
    ```

    e.g. [addEventListener] // Always used here cos .bind does not call the fn

    ```js
    HSR.addRating = function(i, reviews) {
        this.rating += i;
    };

    const onButtonFn = HSR.addRating.bind(HSR, 1)
    document.querySelector('.button').addEventListener('click', HSR.addRating.bind(document.querySelector('.textarea').value))
    ```

### [🌟] [🌟] [🌟] Immediately Invoked Function Expression (IIFE)

- used mainly for async/wait
- scoping; var encapsulation, prevents data from being overwritten by other scripts or libraries

- done by wrapping parenthesis around the function

e.g. [Default function]

```js
(function() {
console.log('This will never run again');
})();
```

e.g. [Arrow function]

```js
(() => console.log('This will ALSO never run again'))();
```

### [🌟] Closures

- is not explicit; it just happens automatically in certain situations
- A function always has access to the variable environment of the execution context in which the function was created
- Closure: VE atatched to the function, exacctly as it was at the time and place the function was created
- the closure has priority over the scope chain
- is an internal property that cannot be accessed from our code

e.g.

```js
const secureBooking = function () {
    let passengerCount = 0;

    return function () {
        passengerCount++;
        console.log(`${passengerCount} passengers`);
    };
};

const booker = secureBooking();

booker(); // How does this work? How does this access the passengerCount var? ...closures
```

## ▷▷▷▷▷ C14: Arrays ◁◁◁◁◁

- Hold info of diff types

### [🌟] When should arrays be used?

1. Use when you need ordered list of values

2. Use when you need to manipulate data

### [🌟] Basics

1. Defining arrays

    e.g.

    ```js
    const friends = ['Michael', 'Steven', 'Peter']

    // OR 
    
    const years = new Arry(1991, 1984, 2008, 2020)
    ```

    - use of const in this case means that the array cannot be overwritten by another array

    Take note:

    ```js
        const years = [1, 2, 3]
        years = [1, 2] -> 'Uncaught TypeError: Assignment to constant variable.'
        // the memory address of the array is stored in a constant variable
    ```

2. Indexing
    e.g.

    ```js
        console.log(friends[0]);
    ```

### [🌟] Array Destructuring

- Destructuring works on nested arrays
- Use cases: inverse the values of two variables OR receive and assign 2 values separately from a function

  e.g.

  ```js
  const arr = [2, 3, 4];
  const [x, y, z] = arr;
  ```

### [🌟] Optional Chaining in Arrays

- check whether attribute exists

e.g.

```js
const users = [{ name: 'harry', email: 'harry@javascript.io' }];
console.log(users[0]?.name ?? 'User array empy');
```

### [🌟] Attributes

1. length

    e.g.

    ```js
    console.log(friends.length);
    ```

| [🌟] Array Mutation Methods |

1. `.push(...)`
    - adds element to the end of array

2. `.unshift(...)`
    - adds element to start of array

3. `.pop()`
    - removes and return the last element

4. `.shift()`
    - remove first and return first element

5. `.splice(~begin~, ~count~)`
    - `count` : the no. of elements to delete
    - mutate the original array

6. `.reverse()`
    - reverses the order of the elements in the array

7. `.sort()`
    - converts all elements to strings before sorting them

8. `.sort([callbackFunction])`
    - per iteration, it will pass (a, b) as args
    - `callbackFunction` returning - or + value based on how the sequence of the 2 elements are to be changed
    - Rule:
        return < 0; keep order // Resultant: A, B
        return > 0; switch order // Resultant: B, A

    e.g. [Arranging integers]

    ```js
    movements = [200, 450, -400, 3000, -650, -130, 70, 1300];

    // In ascending order
    movements.sort((a, b) => a - b);

    // In descending order
    movements.sort((a, b) => b - a);
    ```

9. `.fill(~element~,~begin~, ~end~)`
    - creates `element` and fills them in between `begin` an `end`

### [🌟] Array Searching Methods

1. `.indexOf(~element~)`
    - returns the index of specified element from the front
    - can only find an element from the array
    - case sensitive

2. `.includes()`
    - returns true/false whether element is in list

3. `.find(~callbackFunction~)`
    - `callbackFunction` returns bool value
    - returns the first element in the array that fulfills the condition

4. `.at(~i~)` // returns the element at i
    - useful as array[-1] is undefined

5. `.findIndex(~callbackFunction~)`
    - `callbackFunction` returns bool value
    - allows for more complex search operations as compared to .indexOf
    e.g.
        const index = accounts.findIndex(
            acc => acc.username === currentAccount.username // allows for comparing of object properties
        );

6. `.some(~callbackFunction~)`
    - `callbackFunction` returns bool value
    - returns bool based on whether there is any value in the array that fulfills the condition in the function

7. `.every(~callbackFunction~)`
    - The provided callbackFn function is called once for each element in an array, until the callbackFn returns a falsy value. If such an element is found, every() immediately returns false and stops iterating through the array. Otherwise, if callbackFn returns a truthy value for all elements, every() returns true.

    e.g. [Checking for all matches]

    ```js
    const num = [1, 3, 10, 20, 30]

    num.every((element) => element < 15) // Expected Output: false
    ```

### [🌟] [🌟] Array Generation

1. `Array.from(~iterableObject~, ~callbackFunction~)`
    - per iteration, it will pass (element, i) as args
    - `callbackFunction` returns a value for the element at pos i, similar to the function used in .map

    e.g. [Generating an array of 1-7]

    ```js
    const natureNo = Array.from({length : 7}, (_, i) => i + 1);
    console.log(natureNo);
    ```

2. `new Array(~count~) + .fill(~element~,~begin~, ~end~)`
    - `new Array(~count~)` : creates a array of length `count` with empty values

### [🌟] [🌟] New Array Creation Methods

- allows for method chaining as methods return new array as it is generally not a good idea to chain methods that mutate an arry
- key to functional programming in JavaScript

1. `.map(~callbackFunction~)`

    - per element, it will pass `(element, i, array)` into the `callbackFunction`
    - maps the value returned per execution to a new array

2. `.filter(~callbackFunction~)`

    - `callbackFunction` returns bool value
    - per iteration, it will pass `(element, i, array)` into the `callbackFunction`
    - returns a new array containing the array elements that passed a specified test condition

    e.g.

    ```js
    movements = [200, 450, -400, 3000, -650, -130, 70, 1300];

    const deposits = movements.filter((mov) => {
        return mov > 0;
    })

    console.log(deposits); // returns [200, 450, 3000, 70, 1300]
    ```

3. `~array1~.concat(~array2~)` // returns a new array made up of the 2 arrays

4. `.slice(~begin~, ~end~)` // returns a new array

    - begin is inclusive, end is exclusive
    - does not mutate the original array

5. `.flat(~depth~)`

    - returns a new array with elements extracted from nested arrays

    e.g.

    ```js
    const arrDeep = [[1, 2], [[3, 4], 5], [6, 7], 8];
    console.log(arrDeep.flat[2]) // returns [1, 2, 3, 4, 5, 6, 7, 8]
    ```

6. .flatMap(~callbackFunction~)

    - works the same way as`.map(~callbackFunction~)` with `.flat()`
    - take note that `.flatMap` only `.flat(1)`

### [🌟] [🌟] Other Methods

1. `.reduce(~callbackFunction~, ~initialValueOfAccumulator~)` // returns the reduced to value
    - per iteration, it will pass `(accumulator, current, i, array)` into the `callbackFunction`
    - boils all array elements down to one single value e.g. adding all elements together

    e.g. [Finding sum]

    ```js
    movements = [200, 450, -400, 3000, -650, -130, 70, 1300];

    const balance = movements.reduce((acc, cur) => {
        acc + curr
    }, 0)
    ```

    e.g. [Finding Max]

    ```js
    const max = movements.reduce((acc, cur) => {
        return acc = cur > acc ? cur : acc;
    })
    ```

2. `.entries()`
    - returns an array iterator object with key/value pairs

    e.g.

    ```js
    const fruits = ['Banana', 'Orange', 'Apple', 'Mango'];
    for (fruit of fruits.entries()) {
        console.log(fruit) // returns [1, 'Banana']...
    }
    ```

3. `.foreach(~callbackFunction~)`
    - per iteration, it will pass `(element, i, array)` in that order as args
    - [❗] [`.foreach` VS for-loop] :  it is not possible to break out of a .foreach loop; continue & break statements do not work

4. `.join(~separator~)`
    - creates and returns a new string by concatenating all of the elements in an array, with the separator between the elements

## ▷▷▷▷▷ C15: Objects ◁◁◁◁◁

- For key-value pair

### [🌟] When should objects be used?

1. More "traditional" key/value store

2. Easier to write and access values with . and []

3. Use when you need to include functions (methods)

4. Use when working with JSON (can convert to map)

### [🌟] Object Basics

1. Creating objects w. `{}`

    e.g.

    ```js
    const harry = {
        firstName : 'Harry',
        lastName : 'Cheong',
        age: 2037 - 1991,
        job: 'teacher',
        friends: ['Michael', 'Peter', 'Steven']
    }
    // the object harry has 5 properties
    ```

2. Retrieving properties

    - `.` & brackets are operators to retrieve properties

    e.g. [using . notation]

    ```js
    console.log(harry.lastName)
    ```

    e.g. [using brackets]
    - allows operation to be performed within []

    e.g.

    ```js
    const nameKey = 'Name';
    console.log(harry['first' + namekey])
    console.log(harry['last' + nameKey])
    ```

3. Adding properties

    e.g. [using `.`]

    ```js
    harry.location = 'Singapore'
    ```

    e.g. [using brackets]

    ```js
    harry['twitter'] = '@harry'
    ```

### [🌟] Object Destructuring

- nested object destructuring also works

e.g.

```js
const { firstName, lastName, age } = harry;
console.log(firstName, lastName, age);

const {
    firstName : harryFirstName,
    lastName : harryLastName,
    age : harryAge,
} = harry;
console.log(harryFirstName, harryLastName, harryAge);
```

1. Setting defaults
    - Useful especially when the data returned is not certain
    - Used in apis for eg

    e.g.

    ```js
    const {firstName : harryFirstName,
            favFood : harryFavFood = []
            } = harry;
    console.log(favFood) // returns []
    ```

2. Mutating Variables

    e.g.

    ```js
    let a = 111;
    let b = 999;
    const obj = {a : 23, b: 7, c: 14};
    ({a, b} = obj); // line is wrapped in parenthesis as line with "=" operator cannot start with curly brackets
    console.log(a, b);
    ```

3. Destructuring with functions

    e.g.

    ```js
    orderDelivery: function({starterIndex, mainIndex, time, address}) {
        ...
    }
    orderDelivery({
        time: "22:30",
        address: "23 East Coast Road",
        ...
    })
    ```

### [🌟] [🌟] Enhanced Object Literals (ES6)

- shorthands for writing objects

1. Defining methods

    - Implicit function type

    e.g.

    ```js
    const restaurant = {
        // ...
        order() { 
        // is the same as order = function() {...}
        }
    }
    ```

2. Nested objects in objects

    e.g.

    ```js
    const openingHours = {
    // ...
    }

    const restaurant = {
    // ...
    openingHours, // instead of openingHours = openingHours
    }
    ```

3. Compute property names

  e.g. [Defining object properties]

  ```js
  const openingHours = {
    Today : 133,
    `Day ${Today + 1}` : "0800 : 1800",
  }
  ```

### [🌟] Optional Chaining `?.`

1. Checking whether a property exists

    e.g.

    ```js

    restaurant = {
        openingHours: {
            thu : {
                open: 0,
                close: 18,
            }
        }  
     }
    console.log(restaurant.openingHours?.mon) // returns undefined
    console.log(restaurant.openingHours.mon) // throws AttributeNotFound error
    ```

2. Checking whether a method exists

    e.g.

    ```js
    console.log(restaurant.order?.(0,1)); // returns undefined
    ```

### [🌟] Object Methods

- Fn attached to an object

1. Defining methods

    - `this` in JS is similar to `self` in python
    - `this` does not have to be passed

    e.g.

    ```js
    const harry = {
        birthYear: 1991,
        calcAge : function () {
            return 2037 - this.birthYear
        }
    }
    ```

2. Executing method

    e.g.

    ```js
    harry.calcAge(~arguments~)
    ```

### [🌟] Functions

1. `Object.assign(~Object1~, ~Object2~)`
    - combines 2 objects into a new one that has a different memory address but the same properties as its predecessors
    - however, this only creates a shallow copy, not a deep clone as in objects inside the new object and its predecessor still have the same memory address
    - to create a deep clone, the use of an external library is needed

2. `Object.keys(~Object~)`

3. `Object.values((~Object~))`

4. `Object.entries(~Object~)`
    - returns an array of a given object's own enumerable string-keyed property key-value pairs
    - convert objects into maps

    e.g.

    ```js
    const scores = {
        'Harry' : 3,
        'Tony' : 5,
    }

    const scoresMap = new Map(Object.entries(scores))
    ```

## ▷▷▷▷▷ C16: Sets ◁◁◁◁◁

- only contains unique elements

  [syntax]

```js

  ~var~ = new Set([
  ...
  ])
```

| [🌟] When should sets be used? |

1. Better performance
    - up to 10x faster

2. Keys can have any data type; not limited to string type

3. Easy to iterate

4. Easy to compute size

5. Use when all is required is to to map keys to values

6. Use when working with unique values

7. Use when high-performance is really Important

8. Use to remove duplicates from arrays

### [🌟] Properties {16-properties}

1. `.size`
    - number of elements in a set

### [🌟] Methods {16-methods}

1. `.has(~element~)`
    - checks whether the element is present in the set

2. `.add(~element~)`
    - adds the element into the set

3. `.delete`
    - deletes the element from the set

4. `.clear()`
    - clears the set

5. `.foreach(~callbackFunction~)`
    - per iteration, it will pass `(value, _ : ~throwawayVar~ , array)` in that order as args
    - <> Array Methods [`.foreach` VS for-loop]

## ▷▷▷▷▷ C17: Maps ◁◁◁◁◁

- the big difference betw objects and maps is that in maps, keys can be any type e.g. objects, array or other maps but in objects, keys must be strings
- take note that for object keys to work, the key used to store and retrieve the value must have the same memory address

  [*syntax*]
  
```js
new Map = [] // Preferred when more key-value pairs are to be added

// OR

new Map([
    // ...
])
```

### [🌟] Methods

1. `.set(~key~, ~value~)` // returns the updated map \* can be chained

    e.g.

    ```js
    const rest = new Map();
    rest.set(1, 'Firenze, Italy').set('name', 'Classico Italiano');
    ```

2. `.get(~key~)` // returns corresponding value

3. `.delete(~index~)` // deletes at the specified index

4. `.clear()`

5. `.keys()`

6. `.values()`

7. `.entries()`

8. `hasOwnProperty()`
    TODO: In OOP Section

9. `.foreach(~callbackFunction~)`
    - per iteration, it will pass `(value, key, map)` in that order as args
    - <> Array Methods [`.foreach` VS for-loop]

## ▷▷▷▷▷ C18: Date ◁◁◁◁◁

- Initialization using date constructor

[*syntax*]

```js
  ~
  const ~var~ new Date(...);
  ~
```

### [🌟] Constructor Parser

1. Recommended

    e.g.

    ```js
    new Date(~year~, ~month~, ~date~, ~hours~, ~minutes~, ~seconds~)
    ```

    e.g. [Using a std string]

    ```js
    new Date('2019-11-01T13:15:33.035Z')
    ```

2. Current day
    - the current time
    e.g.

    ```js
    new Date()
    ```

3. Initial unix time

    e.g.

    ```js
    new Date(0)
    ```

4. Following day

    e.g.

    ```js
    new Date(3 * 24 * 60 * 1000) // 3 Days after initial unix time
    ```

5. Timestamp
    e.g.

    ```js
    new Date(1674747403615)
    ```

### [🌟] Functions {18-functions}

1. `Date.now()`
    - returns the current time

### [🌟] Methods {18-methods}

1. `.getFullYear()`

2. `.getMonth()`

3. `.getDate()`

4. `.getDay()`

5. `.getHours()`

6. `.getMinutes()`

7. `.getSeconds()`

8. `.toIOString()`
    - converts date object to a std date string

9. `.getTime()`
    - get timestamp i.e. miliseconds passed since initial unix time

10. `.setFullYear()`
    - changes the FullYear in date object

11. `.setMonth()`

12. `.getDate()`

13. `.getDay()`

14. `.getHours()`

15. `.getMinutes()`

16. `.getSeconds()`

### [🌟] Operations with dates

e.g. [Finding the number of days that passed]

```js
const calcDaysPassed = (date1, date2) => (date2 - date1) / (1000 _ 60 _ 60 \* 24);

calcDaysPassed(new Date(2024, 11, 24), new Date(2024, 11, 28));
```

### [🌟] Internationalization

1. Dates
    - Use `Intl.DateTimeFormat(~locale~, ...)`
    - `locale` : e.g. en-US, en-UK
    - `...` : other config options

    e.g.

    ```js
        const now = new Date();

        // Config
        const options = {
            hour: 'numeric',
            minute: 'numeric',
            day: 'number',
            month: 'long',
            year: 'numeric',
            weekday: 'long'
        }

        // Finding locale from browser
        const locale = navigator.language

        console.log(new Intl.DateTimeFormat(locale, options).format(now))
    ```

2. Int
    - Use `Intl.NumberFormat(~locale~, ~options~)`
    - [Options on MDN Web Dev](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat)

    e.g.

    ```js
        const num = 349238.342;

        const options = {
            style: 'unit', // 'unit', 'percent' or 'currency'
            unit: 'celsius',
        };

        console.log(new Intl.NumberFormat(navigator.language, options).format(num))
    ```

## ▷▷▷▷▷ C19: Timers ◁◁◁◁◁

- used for asynchronous programming

### [🌟] Functions {19-timers}

1. `setTimeout(~callbackFunction~, ~waitTime~, ~args~)`
    - schedules the callback function to be executed once after a set amount of time

    e.g.

    ```js
    const meeting = ["Meet-up with friends", "18:00" ];
    const reminder = setTimeout((event, time) => console.log(`${event} is coming up at ${time}`), 1000, ...meeting);
    ```

2. `clearTimeout()`
    - removes the timeout function assigned to the variable

    e.g.

    ```js
    reminder;

    if (meeting[0].split(' ').includes("Meet-up")) {clearTimeout(reminder)} // no output in console
    ```

3. `setTimeout(~callbackFunction~, ~delay~)`
    - executes `~callbackFunction~` every `~delay~`

## ▷▷▷▷▷ C20: DOM Manipulation ◁◁◁◁◁

### [🌟] What is the DOM?

- stands for Document Object MOdel; connects web pages to scripts or programming languaes by representing the structure of a document - such as HTML - in memory
- DOM Tree is generated from an HTML document, which we can then interact with
- is a very complex API that contains lots of methods and properties to interact with the DOM tree

### [🌟] How is the DOM organised?

- Parent method and property is inherited by child
- Any HTMLElement will have access to .addEventListener(), .cloneNode() or .closest() methods

[A hierachy tree for DOM]

```js

  [4] Event Target

  - .addEventListener()
  - .removeEventListener()

  *******************************

        ↪ [3] Node
        - .textContent
        - .childNodes
        - .parentNode
        - .cloneNode

            ↪ [2] Element
            - .innerHTML
            - .classList
            - .children
            - .parentElement
            - .append()
            - .remove()
            - .insertAdjacentHTML()
            - .querySelector()
            - .closest()
            - .matches()
            - .scrollIntoView()
            - .setAttribute()

            ↪ [2] Text

            ↪ [2] Comment

            ↪ [2] Document
            - .querySelector()
            - .createElement()
            - .getElementById()
            - .getElementByClassName()

  *******************************

        ↪ [3] Window
        // Global objext, lots of methods and properties, many unrelated to DOM
```

### [🌟] Event Handlers

1. `.addEventListener(~event~, ~callbackFunction~, ~capturingOrBubbling~)`
    - `~capturingOrBubbling~` captures the event at the capturing or bubbling phase

    e.g. [Passing "argument" into handler]

    ```js
    addEventListener(~event~, ~callbackFunction~.bind(~args~))
    // this keyword refers to the args
    ```

2. `.removeEventListener(~event~, ~callbackFunction~)`

3. Writing js in html file
    - DON'T use

    e.g.

    ```html
        <h1 onclick="alert('HTML alert')">

        </h1>
    ```

### [🌟] Event Types

1. `click`
    e.g. [Button]

    ```js
        document.querySelector('.check').addEventListener('.click', function() {
            ...
        })
    ```

2. `keydown`/`keyup`/`keypress`
    - considered global events
        e.g. [Keydown]

    ```js
    document.addEventListener('keydown', function(e) {
        console.log(e.key);
    })
    // the e object contains all the information about the vent
    ```

3. `mouseenter`
    - happens when the  mouse clicks on the element

4. `mouseover`
    - similar to 'mouseenter' except that it bubbles

5. `mouseleave`
    - happens when the mouse leaves

6. `mouseout`
    - similar to 'mouseleave' except that it bubbles

7. `scroll`
    - available on the window
    - poor performance as it triggers every time a small adjustment is made

8. `DOMContentLoaded`
    - happens when HTML is parsed and DOM truee built

    e.g.

    ```js
    document.addEventListener('DOMContentLoaded', function (e) {
        console.log('HTML pased and DOM tree built', e);
    });
    ```

9. 'load'
    - happens when page is completely loaded

    e.g.

    ```js
    window.addEventListener('load', function (e) {
        console.log('Page fully loaded', e);
    });
    ```

### [🌟] [🌟] Event Propagation

Phases

1. Capturing Phase
    - When an event occurs, the event is passed down the DOM tree

2. Target Phase
    - the event passes through all the parent nodes and eventually reaches the target phase

3. Bubbling Phase
    - the event passes through all the parent nodes and travels all the way up
    - Implication: If eventListeners are attached to both the parent and child node, both callback functions will be called

    e.g. [Illustration of phases]

    ```js
    document.querySelector('.nav\_\_link').addEventListener('click', function(e) {
        console.log(e.target, e.currentTarget);
        console.log(this == e.currentTarget); // true
    })
    // event.target is the "target" element that initiated the event, it doesn't change through the bubbling process
    // this is the "current" element, the one that has a currently running hander on it
    ```

### [🌟] [🌟] Event Delegation

- instead of adding eventListener to each element
- putting the eventListener on a common parent. When the event happens, it bubbles up and the parent will handle the event.
- improves code efficiency

e.g. [Implementing page navigation]

```js
    document.querySelector('.nav\_\_links').addEventListener('click', function(e) {
    e.preventDefault(); // prevent default href scrolling

            // Matching strategy: ensures that it is the intended element
            if (e.target.classList.contains('nav__link')) {
                const id = e.target.getAttribute('href');
                document.querySelector(id).scrollIntoView({behaviour : 'smooth'});
            }
        })
```

### [🌟] Working with Document

- this object is the root document object itself

1. `.querySelector('.~element~')` // returns the element node
    - selects a specific element

2. `.querySelectorAll('.~elementIdentifier~')` // returns a node list
    - selects all elements that is identifiable by the same elementIdentifier

3. `.getelementById(~id~)` OR `.querySelector('#~Id~')`
    - selects the element with that unique id

4. `.getElementByClassName(~className~)`
    - selects all elements with that className

5. `.createElement(~element~)`

6. `.documentElement`
    - returns the `Element` object that is the root element of the document

    a. `.clientHeight`
        - height of viewport

    b. `.clientWidth`
        - width of viewport

### [🌟] [🌟] Working with Elements |

1. `.insertAdjacentHTML(~position~)`
    - ~position~ : 'beforebegin', 'afterbegin', 'beforeend', 'afterend'
    - adds new HTML elements

2. `.innerHTML = '...'`
    - changes the HTML written under the element

3. [❗] `.classList`
    a. `.remove(...~className~)`
        - do not use '.'
        - removes the class assigned to the element

    b. `.add(...~className~)`
        - assigns the class to the element

    c. `toggle(~className~)`
        - if class is not assigned, assign it
        - if class is already assigned, remove it

    d. `contains(~className~)`
        - checks whether element has the class

4. `.clasName`
    - DON'T use: it overwrites all the classes in the element

5. `.src = ~FilePath~`
    - specific for certain HTML elements

6. [❗] `.style.~cssStyle~ = ...`
    - changes the css style sheet
    - console.log(~element~.style.~cssStyle~) only returns a value if it is an inline style; does not return a value if style is hidden inside classes
        a. .setProperty()
        - sets a new value for a property on a CSS style declaration object

7. `.getComputedStyle(~element~).color`
    - access all the styles as displayed by the browser

8. `.getAttribute(~attribute~)`
    - access non-standard attributes
    - special cases
        a. `src`
        - returns rel instead of abs path

        b. `href`
        - returns rel instead of abs path

9. `.setAttribute(~attribute~, ~value~)`
    - changes value of the specified attribute

10. `.remove()`
    - deletes the elements

11. `.removeChild(~parentNode~)`
    - removes child node of parent

12. `.append()`
    - creates and/or move element to the top

13. `.prepend()`
    - creates and/or move element to the bottom

14. `.cloneNode(~toCloneAllChild~)`
    - `~toCloneAllChild~` : if true, all the child nodes will be cloned as well

15. `.getBoundingClientRect()`
    - returns a DOMRect object providing information about the size of an element and its position relative to the viewport

16. [❗] `.scrollIntoView({behaviour : 'smooth' })`
    - scrolls the page downwards such that the element is in view
    - only supported in modern browser

17. [❗] `.preventDefault()`
    - cancels the event if it is cancelable, meaning that the default action that belongs to the event will not occur

### [🌟] [🌟] DOM Traversing Methods

[ Going Downwards ]

1. `.querySelector(~selectors~)`
    - returns the first element that is a descendent of the element on which it is invoked that matches the specified group of selectors

2. `.childNodes`
    - returns all the child nodes: text, comment etc.

3. `.children`
    - returns all the child elements
    - only works for direct children

4. `.firstElementChild`

5. `.lastElementChild`

[ Going Upwards ]

1. `.parentNode`

2. `.parentElement`

3. `.closest(~selector~)`
    - returns the node that matches the specified selectors

[ Going Sideways ]

1. `.previousElementSibling`

2. `.nextElementSibling`

3. `.previousSibling`

4. `.nextSibling`

5. `.parentElement.children`
    - to find all children

### [🌟] Working with window

1. `.window.pageXOffset`
    - the x-coordinates of where the page is
    - for scrolling

2. `.window.pageYOffset`
    - the y-coordinates of where the page is
    - for scrolling

3. Extent of scroll effect

[*syntax*]

```js
scrollTo({
    left: ~left~,
    top: ~left~,
    behaviour: 'smooth'
})
```

### [🌟] [🌟] Intersection Observer API

- allows our code to observe if a certain target element intersets another element, or the way it intersects the viewport

[*syntax*]

```js
// ~CallbackFunction~
const obsCallback = function(entries, observer) {...};

// ~options~
const options = {...}

// Constructor
const observer = new IntersectionObserver(obsCallback, options);
observer.observe(~observedTarget~)

```

[ Perimeters ]

1. `Options` object
    - `~root~` can be either the ~element~ or null [viewport]
    - `~threshold~`
        #1: `0`
        - it will be triggered when it first comes into view and also when it disappears from view

        #2: `1`
        - when 100% of the target is visible

        #3: `[...]`
        - an array of percentage
        - the `~callbackFunction~` will be called when either one of the percentage is reached
    - `~rootMargin~` is a the set number of pixels that will be applied outside of our target element

    e.g.

    ```js
        const options = {
            root: null,
            threshold: 0.1,
            rootMargin: '-90px',
        }
    ```

2. Callback Function
    - called when the target element intersects the root at the specified threshold

[ Functions ]

1. `.observe(~element~)`

2. `.unobserve(~element~)`

[ Use Cases ]

1. Sticky Navigation Bar

2. Revealing Elements on Scroll

3. Lazy Loading Images

### [🌟] [🌟] [🌟] Script Loading

1. Normal Script End of Body
    - Scripts are fetched and executed after the HTML is completely parsed
    - [❗] Use if old browsers need to be supported

    e.g.

    ```html
    <script src="script.js"></script>
    ```

2. `async` in Head
    - Scripts are fetched asynchronously and executed immediately
    - Usually the DOMContentLoaded event waits for all scripts to execute, except for async scripts. So, DOMContentLoaded does not wait for an async script
    - Scripts are not guranteed to execute in order
    - [❗] Use for 3rd-party scripts where order doesn't matter (e.g. Google Analytics)

    e.g.

    ```html
    <script async src="script.js"></script>
    ```

3. `defer` in Head
    - Scripts are fetched asynchronously and executed after the HTML is completely parsed
    - DOMContentLoaded event fires after defer script is executed
    - Scripts are executed in order
    - [❗] This is overall the best solution! Use for your own scripts, and when order matters (e.g. including a library)

    e.g.

    ```html
    <script defer src="script.js"></script>
    ```

## ▷▷▷▷▷ C21: Object Oriented Programming ◁◁◁◁◁

- is a programming paradigm based on the concept of objects
- objects may contain data and code. By using objects, we pack data and the corresponding behaviour into one block
- developed with the goal of organizing code, to make it more flexible and easier to maintain (avoid "spaghetti code")`

### [🌟] Principles of OOP

1. Abstraction
    - ignoring or hiding details that don't matter, allowing us to get an overview perspective of the thing we're implementing, instead of messing with details that don't really matter to our implementation

2. Encapsulation
    - keeping properties and methods private inside the class, so they are not accessible from outside the class. Some methods can't be exposed as a public interface (API)
    - prevents external code from accidentally manipulating internal properties/state
    - allows to change internal implementation without the risk of breaking external code

3. Inheritance
    - making all properties and methods of a certain class available to a child class, forming a hierachical relationship between classes. This allows us to reuse common logic and to model real-world relationships

4. Polymorphism
    - a child class can overwirte a method it inherited form a parent class

### [🌟] OOP in JavaScript

1. "Classical OOP": Classes
    - objects are instantiated from a class, which functions like a blueprint

2. OOP in JS: Prototypes
    - objects are linked to a prototype object
    - Prototypical inheritance: the prototype contains methods that are accessible to all objects linked to that prototype
    - Behavior is delegated to the linked prototype object (the methods are not copied, simply delegated when called)
    - How are objects created?
        a. Constructor function
        b. ES6 Classes
        c. `Object.create()`

### [🌟] `new` Keyword

- `new` is used to create an instance of an object that has a constructor function

  e.g.

    ```js
    const Person = function(firstName, birthYear) {
        this.firstName = firstName;
        this.birthYear = birthYear;
    }
    const harry = new Person('Harry', 2006)
    ```

- [❗] Do not put any functions inside the constructor function as each and every instance will have the function and that will affect performance instead define it inside the prototype

[How does `new` work?]

1. A new empty object is crated
2. Sets the new object's internal, inaccessible, `[[prototype]]` (i.e. `__proto__`) to be the constructor function's external, accessible, `prototype` object
3. Makes `this` point to the newly created object.
4. Executes the constructor function, using the newly created object
5. Returns the newly created object

### [🌟] [🌟] Prototypes

- `prototype` property is used to add new properties to object constructors
- [❗] Only modify your own prototypes. Never modify the prototypes of standard JavaScript object

e.g. [Defining object functions]

```js
Person.prototype.calcAge = function() {
    console.log(2037 - this.birthYear)
};
jonas.calcAge()
```

e.g. [Defining common attributes]

```js
Person.prototype.species = 'Homo Sapiens';
console.log(jonas.species) // returns 'Homo Sapiens'
```

### [🌟] [🌟] Prototype and Inheritance

```text
// Cool Diagram
                                        Prototype
    Constructor Function    -->    [Object.prototype]
        Object()                    __proto__ : null


                                          /|\
                                           |

                                        Prototype
    Constructor Function    -->    [Object.prototype]
        Object()                    `__proto__` : null


                                          /|\
                                           |

                                         Object
                                         [jonas]
```

### [🌟] ES6 Classes

- modern alternative to constuctor syntax
- "syntactic suger" : behind the scenes, ES6 classes work exactly like constructor functions

e.g.

```js
  class Person {
    constructor(firstName, birthYear) {
        this.firstName = firstName;
        this.birthYear = birthYear;
    },

    // Methods will be added to .prototype automatically
    calAge() {
        console.log(2037 - this.birthYear);
    }
    
    // the constructor function must be syntaxed this way
    // any functions defined outside of the constructor function will be on the prototype
}
```

[To take note]

1. Classes are NOT hoisted
2. Classes are like first class functions
3. Classes are executed in strict mode

### [🌟] Setters and Getters

- for that, we use get and set

1. get
    - to define a getter method to get the propoerty value, but they do not calculate the propoerty's value until it is accessed

2. set
    - to define a setter method to set the property value

### [🌟] Static Methods

- Usually utility functions, such as functions to create or clone objects
- Not inherited by other instances
  e.g. `Array.from`

e.g. [E36 Class]

```js
class Student {
    static attendence() {
        console.log("I'm here!")
    }
}
```

e.g. [Constructor Function]

```js
Student.attendence() = function() {
    console.log("I'm here!");
}
```

### [🌟] Functions & Methods

1. `Object.create(~prototype~)`
    - the easiest and most striaghtforward of linking an object to a prototype object - used for class inheritance

2. `instanceof ~instance~`
    - checks whether it is an instance of a class

3. `.__proto__`
    - returns the prototype of the object

4. `~objName~.isPrototypeOf(~instance~)`
    - returns whether the instance has the same prototype as objName

5. `.hasOwnProperty(~property~)`
    - checks whether the property belongs to the object (true) or inherited from prototype (false)

## ▷▷▷▷▷ C22: How does JavaScript work? ◁◁◁◁◁

### [🌟] About JavaScript Engine

- program that executes JavaScript Code
- two components: call stack i.e. where our code is stored and heap i.e. an unstructured memory pool
  which stores all the objects our program needs
- Happens in special threads that we can't access from code

- JavaScript Engine FlowChart

```text
  [Execution] \* Happens in call stack

      /|\
       |    * During which, the machine code is constantly optimized to improve performance, allowing v8 engine to achieve high processing speed

[Compilation] \* Just-in-time compilation

      /|\
       |

[Parsing]

      /|\
       |

[Source Code]
```

### [🌟] [🌟] CS: Compilation vs Interpretation

1. What is Compilation?
    - Entire code is converted into machine code at once, and written to a binary file that can be executed by a computer

    ```text
      [Program Running]

           /|\   Step 2 : Execution
            |    * can happen way after compilation

     [Portable File] * can be ran on any machine

           /|\   Step 1 : Compilation
            |

      [Source Code]
    ```

2. What is Interpretation?
    - Interpreter runs through the source code and executes it line by line

    ```text
       [Program Running]

           /|\   Step 1 : Execution line by line
            |    * code still needs to be converted to machine code

        [Source Code]
    ```

3. Just-in-time(JIT) Compilation
    - Entire code is converted into machine code at once, then executed immediately

    ```text
    [Program Running]

           /|\   Step 2 : Execution
            |    * happens immediately

     [Machine Code] * NOT a portable file

           /|\   Step 1 : Compilation
            |

      [Source Code]
    ```

### [🌟] [🌟] JavaScript Runtime on browers

- Web runtime contains all JS-related items: Js Engine, web APIs i.e. functionalities provided to the engine, accessible on window object, callback queue i.e. Callback function from DOM event listener

- The event loop puts callback function in the callback queue into the call stack to be executed
  <> The Bigger Picture: JavaScript Runtime slides

### [🌟] [🌟] [🌟] The Call Stack

- "Place" where execution contexts get stacked on top of each other, to keep track of where we are in the execution

### [🌟] [🌟] [🌟] Execution Context

- environment in which a piece of JavaScript is executed. Stores all the necessary information for some code to be executed.

```text
[Execution of functions and waiting for callbacks]

      /|\
       |   * One execution context per function: For each function call, a new execution context is created.

[Execution of top-level code (inside global EC)] \* Just-in-time compilation

      /|\
       |

[Creation of global execution context(for top-level code)] \* Not inside a function

      /|\
       |

[Compilation]
```

### [🌟] [🌟] [🌟] Execution Context in Detail

What's inside execution context

- Generated during "creation phase", right before execution

1. Variable Environemnt
    - let, const and var declarations
    - functions
    - arguments object ( [❗] Not in arrow fn)
        <> Argument Object

2. Scope chain

3. this keyword ( [❗] Not in arrow fn)

### [🌟] Argument Object

- is an array of argument passed
- for kwargs/variadic functions

e.g.

```js
const addExpr = function (a, b) {
console.log(arguments) // using argument keyword
}
```

### [🌟] [🌟] Scoping and Scope

- Scoping : How our program's variables are organized and accessed. "Where do variables live?" or "Where can we access a certain variable, and where not?"

- Scope of a variable : Region of our code where a certain variable can be accessed

- Lexical scoping: Scoping is controlled by placement of functions and blocks in the code
  e.g. a fn written inside a fn has access to variables in the parent fn

- Scope: Space or enviornment in which a certain variable is declared. There is global scope, function scope, and block scope

1. Global Scope

    - outside of any function or block
    - variables declared in global scope are accessible everywhere

2. Function Scope

    - variables are accessible only inside function, not outside
    - also called local scope

3. Block Scope (ES6)

    - variables are accessible Only inside block (block scoped)
    - [❗] this only applies to let and const variables
    - [❗] however, var variables are function-scoped, and they will be scoped to the current fn or global scope; ignore blocks
    - Functions are also block scoped (only in strict mode)

### [🌟] [🌟] Scope Chain

- Every scope always has access to all the variables from all its outer scopes.
- ia a one-way street; a scope will never, ever have access to the variables of an inner scope
- is equal to adding together all the variable environemtns of the all parent scopes

### [🌟] [🌟] Hoisting

- makes some types of variables accessible/usable in the code before they are actually declared
- [How it works behind the scene?] Before execution, code is scanned for vaiable declarations, and for each variable, a new property is created in the variable environment object.

Declarations

1. Function
    ✅Hoisted
    💫Actual Value
    🔍Block

2. var variables
    ✅Hoisted
    💫Undefined
    - which is a major source of bugs; avoid using var
    🔍Block

3. let and cost variables
    ❌Hoisted
    - Technically, yes. But not in practice
    💫TDZ (Temporal Dead Zone) i.e. the region of the scope in which the variable is defined but can be used in any way; as if the var didn't exist
    🔍Block

4. Function expressions and arrows
    - depends if using var or let/const

### [🌟] [🌟] 'this' keyword

- special variable that is created for every execution context (every function). Takes the value of (points to) the "ownder of the function in which the this keyword is used.

- this is NOT static. It depends on how the function is called, and its value is only assigned when the function is actually called.

Circumstances

1. Method 'this' - object that is calling the method

2. Simple Function call 'this'
    - undefined (in strict mode)
    - window (otherwise)

3. Arrow Function 'this'
    - inherits 'this' keyword from parent

4. Event Listener 'this'

5. new, call, apply, bind

## ▷▷▷▷▷ END ◁◁◁◁◁
