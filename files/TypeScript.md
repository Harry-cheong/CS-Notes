# TypeScript

## ▷▷▷▷▷ C01: TS Introduction ◁◁◁◁◁

- TypeScript is a syntactic superset of JavaScript which adds static typing
- uses compile time type checking i.e. checking if the specified types match before running the code

Comparison

1. JavaScript

   - JavaScript is a loosely typed language. It can be difficult to understand what types of data are being passed around in JavaScript.
   - function parameters and variables don't have any information. So, developers need to look at documenation, or guess based on the implementation

2. TypeScript
   - allows specifying the types of data being passed around within the code, and has the ability to report errors when the types do not match

## ▷▷▷▷▷ CO2: Getting Started ◁◁◁◁◁

1. Install the compiler

   - installed in the `node_modules` directory and can be run with `npx tsc`

   ```cmd
   npm install typescript --save-dev
   ```

   [FYI] `--save-dev` adds the third-party package to the package's development dependencies. It would not be installed when installing packages.

2. [❗] Configuring the compiler

   - compiler configured using a `tsconfig.json` file

   ```cmd
   npx tsc --init
   ```

   e.g. `tsconfig.json`

   ```ts
    // Configure TypeScript compiler to transpile TypeScript files located in the src/ directory of your project, into JavaScript files in the build/ directory
    {
    "include": ["src"],
    "compilerOptions": {
        "outDir": "./build"
    }
    }
   ```

## ▷▷▷▷▷ C03: TS Types ◁◁◁◁◁

### [🌟] Primitive Types

1. `boolean`

2. `number`: whole numbers and floating point values

3. `string`

4. `bigint`: whole numbers and floating point values, but allows large negative and positive numbers than the `number` type

5. `symbol`: used to create a globally unique identifier

### [🌟] [🌟] TypeScript Special Types

1. Type: any

   - `any` is a type that disables type checking and allows all types to be used

   ```ts
   let v: any = true;
   v = "string"; // no error as it can be "any type"
   Math.round(v); // no error as it can be "any" type
   ```

2. Type: unknown

   - `unknown` is similar but a safer alternative to `any`
   - TypeScript will prevent `unknown` types from being used
   - to add a type later, cast it; Casting it is when we use the `as` keyword to say property or variable is of the casted type.

3. Type: never

   - `never` throws an error whenever it is defined
   - rarely used, especially by itself, its primary use is in advanced generics

4. Type: undefined & null
   - `undefined` and `null` are types that refer to the JavaScript primitives `undefined` and `null`

### [🌟] Type Assignment

1. Explicit: writing out the type

   ```ts
   let firstName: string = "Harry";
   ```

2. Implicit: TypeScript will infer the type, based on the assigned value

   - TypeScript may not always properly infer what the type of a varaiable may be. In such cases, it will set the type to `any` which disables type checking.
   - this behaviour can be disabled by enabling `noImplicitAny` as an option in `tsconfig.json`

   ```ts
   let firstName = "Dylan";
   ```

### [🌟] [🌟] Union Types

- Union types are used when a value can be more than a single type

e.g. `string` or `number` parameter

```ts
function myFunc(myVar: string | number) {
  console.log(myVar);
}
```

[❗] TAKE NOTE: Union Type Errors happen when one type has access to certain methods/attributes that the other type does not

### [🌟] [🌟] Type Aliases

- Type Aliases allow defining with a custom name
- can be used for primitives like `string` or more complex types such as `objects` and `arrays`

e.g.

```ts
type GradYear = number;
type Cca = string;
type Gpa = number;
type Student = {
  year: GradYear;
  activity: Cca;
  score: Gpa;
};
```

### [🌟] [🌟] Interfaces

- similar to type aliases, except they **only** apply to `object` types

```ts
interface Rectangle {
  height: number;
  width: number;
}

const figure: Rectangle = {
  height: 20,
  width: 10,
};
```

### [🌟] [🌟] Extending Interfaces

- Extending an interface creates a new interface with the same properties as the orginal, plus something new

e.g.

```ts
interface Rectangle {
  height: number;
  width: number;
}

interface ColouredRectangle extends Rectangle {
  colour: string;
}

const colouredRectangle: ColouredRectangle = {
  height: 20,
  width: 10,
  colour: "red",
};
```

## ▷▷▷▷▷ C04:TS Arrays ◁◁◁◁◁

### [🌟] `Readonly`

- `readonly` keyword can prevent arrays from being changed

### [🌟] Tuples

- A tuple is a typed array with a pre-defined length and types for each index
- [❗] always make your tuple `readonly`; tuples only have strongly defined types for the initial values

e.g. Definition

```ts
// Define ourTuple
let ourTuple: [number, boolearn, string];

// Initialize
ourTuple = [5, false, "Coding is fun"];
```

### [🌟] Named Tuples

- Named Tuples alow us to provide context for what our index values represent
- [❗] Order of value matter for Tuples

```ts
const scores: [math: number, gp: number] = [70.0, 65.0];
```

## ▷▷▷▷▷ C05: TS Objects ◁◁◁◁◁

e.g. Explicit

```ts
const student: { class: string; gpa: number; year: number } = {
  class: "6C42",
  gpa: 9.0,
  year: 2024,
};
```

e.g. Implicit

```ts
const student = {
  class: "6C42",
};
```

### [🌟] Optional Properties

- Optional Properties are properties that do not have to defined in the object definition

```ts
const student: { class: string; gpa?: number } = {
  // no error
  class: "6C42",
};
student.gpa = 9.0;
```

### [🌟] [🌟] Index Signatures

- used for objects without a defined list of properties

```ts
const class: { [index: string]: number} = {};
class.harry = 17; // no error
class.yuheng = "cool"; // Error: Type 'string' is not assignable to type 'number'
```

[KIV] Index Signatures can also be expressed with utility types like `Record<string, number>` ↪*TypeScipt Utility Types*

### [🌟] [🌟] [🌟] TypeScript Enums

- An `enum` is a special "class" that represents a group of constants
- comes in two flavours `string` and `numeric`

1. Numberic Enums - Default

   - By default enums will initialise the first value to `0` and add ` to each additional value

   ```ts
   enum Directions {
     North,
     East,
     South,
     West,
   }
   console.log(currentDirection.North); // logs 0
   currentDirection = 1; // Error: "1" is not assignable to type 'Directions'
   ```

2. Numeric Enums - Initialized

   - Set the value of the first numeric and have it auto increment

   e.g.

   ```ts
   enum Directions {
     North = 1,
     East,
     South,
     West,
   }

   // logs 1
   console.log(Directions.North);

   // Logs 4
   console.log(Directions.West);
   ```

3. Numeric Enums - Fully Initialized

   - Assign unique number values for each enum value, then the values will not be incremented automatically

   e.g.

   ```ts
   enum StatusCodes {
     NotFound = 404,
     Success = 200,
     Accepted = 202,
     BadRequest = 400,
   }

   // logs 404
   console.log(StatusCodes.NotFound);

   // logs 200
   console.log(StatusCodes.Success);
   ```

4. String Enums

   - more common, because of their readability and intent

   e.g.

   ```ts
   enum Directions {
     North = "North",
     East = "East",
     South = "South",
     West = "West",
   }

   // logs "North"
   console.log(Directions.North);

   // logs "West"
   console.log(Directions.West);
   ```

## ▷▷▷▷▷ C06: TS Functions ◁◁◁◁◁

### [🌟] Return Type

- type of value returned by the function can be explicitly defined

e.g. Explicit Type

```ts
// the ': number' here specifies that this function returns a number
function getTime(): number {
  return new Date().getTime();
}
```

e.g. Void Type

```ts
// the type 'void' can be used to indicate a function doesn't return any value
function printHello(): void {
  console.log("Hello! ");
}
```

### [🌟] Parameters

1. Basic Parameters

   - if no parameter is defined, TypeScript will default to using `any`

   ```ts
   function multiply(a: number, b: number) {
     return a * b;
   }
   ```

2. Optional Parameters

   - by default TypeScript will assume all parameters are required, but they can be explicitly marked as optional

   ```ts
   // the '?' operator here marks paramter 'c' as optional
   function add(a: number, b: number, c?: number) {
     return a + b + (c || 0);
   }
   ```

3. Default Parameters

   - goes after the type annotation

   ```ts
   function pow(value: number, exponent: number = 10) {
     return value ** exponent;
   }
   ```

4. Named Parameters

   - similar pattern to typing normal parameters

   ```ts
   function divide({
     divident,
     divisor,
   }: {
     divident: number;
     divisor: number;
   }) {
     return divident / divisor;
   }
   ```

5. Rest Parameters

   - type of rest parameters must be an array as rest parameters are always arrays

   ```ts
   function add(a: number, b: number, ...rest: number[]) {
     return a + b + c + rest.reduce((p, c) => p + c, 0);
   }
   ```

### [🌟] [🌟] Type Alias

- function type can be specified separately from functions with type aliases
- written similary to arrow functions

```ts
type Negate = (value: number) => number;

// in this function, the parameter 'value' automatically gets assigned the type
const negateFunction: Negate = (value) => value * -1;
```

## ▷▷▷▷▷ C07: TS Casting ◁◁◁◁◁

- override the type of a variable, such as when incorrect types are provided by a library

### [🌟] Casting with `as`

- [❗] Casting does not change the type of the data within the variable

e.g.

```ts
let x: unknown = 4;
console.log((x as string).length);
// prints undefined since numbers don't have a length
// Error: Conversion of type 'number' to a type 'string' may be a mistake because neither type sufficiently overlaps with the other. If this was intentional, convert the expression to 'unknown' first.
```

### [🌟] [🌟] Casting with `<>`

- `<>` is a shorthand for `as`
- [❗] This type of casting will not work with TypeScript XML (TSX) file, such as when working on React files

e.g.

```ts
let x: unknow = "hello";
console.log((<string>x).length);
```

### [🌟] [🌟] [🌟] Force Casting

- To override type errors in TypeScript may throw when cast, first cast to `unknown`, then to the target type
- [❌] TSC: Property does not exist on type

e.g.

```ts
let x = "hello";
console.log((x as unknown as number).length);
```

?

## ▷▷▷▷▷ C08: TS Classes ◁◁◁◁◁

- TypeScript adds types and visiblity modifiers to JavaScript classes

### [🌟] [🌟] Members Types

- members of a class (properties & methods) are typed using type annotations, similar to variables

### [🌟] [🌟] Members Visiblity

1. `public`

   - default
   - allows access to the class member anywhere

2. `private`

   - only allows access to the class member from within the class

3. `protected`
   - allows access to the class member from itself and any classes that inherit it

e.g.

```ts
class Person {
  private name: string;

  public constructor(name: string) {
    this.name = name;
  }

  public getName(): string {
    return this.name;
  }
}

const person = new Person("Tony");
// console.log(person.name) -> person.name is not accessible outside the class since it is private
console.log(person.getName());
```

### [🌟] Parameter Properties

- TypeScript provides a shortcut to define class attributes in the constructor, by adding a visiblity modifiers to the parameter

e.g. with Parameter Properties

```ts
class Person {
  // name is a private member variable

  // ***********************
  public constructor(private name: string) {}
  // ***********************

  public getName(): string {
    return this.name;
  }
}
```

e.g. without Parameter Properties

```ts
class Person {
  // ***********************
  private name: string;

  public constructor(name: string) {
    this.name = name;
  }
  // ***********************

  public getName(): string {
    return this.name;
  }
}
```

### [🌟] [🌟] Readonly

- `readonly` prevents class members from being changed

```ts
class Person {
  private readonly name: string;

  public constructor(name: string) {
    // name cannot be changed after this initial definition, which has to be either at its declaration or in the constructor
    this.name = name;
  }

  public getName(): string {
    return this.name;
  }
}
```

### [🌟] [🌟] Inheritance

1. `implements`

   - interfaces can be used to define the type of a class must follow though
   - a class can implement multiple interfaces by listing each one after `implements` e.g. `class Rectangle implements Shape, Colored {`

   ```ts
   interface Shape {
     getArea: () => number;
   }

   class Rectangle implements Shape {
    public constructor(protected reeadonly width: number, protected readonly  height: number) {}

    // ***********************
    // ensures compliance with Shape type
    public getArea(): number {
      return this.width * this.height;
    }
    // ***********************
   }
   ```

2. `extends`

   - classes can extend each other through the `extends` keyword
   - `super()` exectues the constructor of the base class

   ```ts
   interface Shape {
     getArea: () => number;
   }

   class Rectangle implements Shape {
    public constructor(protected reeadonly width: number, protected readonly  height: number) {}

    public getArea(): number {
      return this.width * this.height;
    }
   }

     // ***********************
    class Square extends Rectangle {
      public constructor(width: number) {
        super(width, width);
      }

      // getArea gets inherited from Rectangle
    }
    // ***********************
   ```

3. `override`

   - when a class extends another class, it can replace the members of the parent class with the same name
   - by default, the `override` keyword is optional, but helps to prevent accidentally overriding a method that does not exist
   - [❗] Use the setting `noImplicitOverride` to force it to be used when overriding

   ```ts
   interface Shape {
     getArea: () => number;
   }

   class Rectangle implements Shape {
    public constructor(protected reeadonly width: number, protected readonly  height: number) {}

    public getArea(): number {
      return this.width * this.height;
    }

    // ***********************
    // this toString in parent class is replaced by `override` in child class
    public toString(): string {
      return `Rectangle[width=${this.width}, height=${this.height}]`;
    }
    // ***********************
   }

    class Square extends Rectangle {
      public constructor(width: number) {
        super(width, width);
      }

      // ***********************
      // this toString replaces the toString from Rectangle
      public override toString(): string {
        return `Square[width=${this.width}]`;
      }
      // ***********************
    }
   ```

4. `abstract`

   - `abstract` classes serve as a base class for subclasses which do implement all `abstract` members
   - `abstract` classes cannot be instantiated, as it does not have all of their members implemented
   - `abstract` members must exist inside an abstract class

   ```ts
   // ***********************
   abstract class Polygon {
     public abstract getArea(): number;

     public toString(): string {
       return `Polygon[area=${this.getArea()}]`;
     }
   }
   // ***********************
   // const polygon = new Polygon() -> cannot create an instance of an abstract class
   // instead, we have to make a derived class and implement the abstract members

   class Rectangle extends Polygon {
     public constructor(
       protected readonly width: number,
       protected readonly height: number
     ) {
       super();
     }

     public getArea(): number {
       return this.width * this.height;
     }
   }
   ```

## ▷▷▷▷▷ C09: TS Generics ◁◁◁◁◁

- Generics are used to create classes, functions & type aliases that work over a variety of types rather than a single one
- make it easier to write reusable code

### [🌟] Generic Function

e.g. "Hello World" of Generics

```ts
function createPair<S, T>(v1: S, v2: T): [S, T] {
  return [v1, v2];
}
console.log(createPair<string, number>("hello", 42)); // ['hello', 42]
```

### [🌟] Generic Classes

e.g.

```ts
class Group<T> {
  private _value: T[] | undefined;

  constructor(private name: string) {}

  public setValue(...rest: T[]) {
    this._value = rest;
  }

  public getValue(): T[] | undefined {
    return this._value;
  }

  public toString(): string {
    return `${this.name}: ${this._value?.join(" ")}`;
  }
}

// Group of numbers
const nums = new Group<number>("Number Group");
nums.setValue(1, 2, 3, 4);
console.log(nums.toString());

// Group of strings
const strings = new Group<string>("String Group");
strings.setValue("a", "b", "c", "d");
console.log(strings.toString());
```

## ▷▷▷▷▷ C10: TS Utility Types ◁◁◁◁◁

1. `Partial`

   - `Partial` changes all the properties in an object to be optional

   e.g.

   ```ts
   interface Point {
     x: number;
     y: number;
   }

   let pointPart: Partial<Point> = {}; // `Partial` allows x and y to be optional
   pointPart.x = 10;
   ```

2. `Required`

   - `Required` changes all the properties in an object to be required

   e.g.

   ```ts
   interface Car {
     make: string;
     model: string;
     mileage?: number;
   }

   let myCar: Required<Car> = {
     make: "Ford",
     model: "Focus",
     mileage: 12000, // `Required` forces mileage to be defined
   };
   ```

3. `Record`

   - `Record` is a shortcut to defining an object type with an specific key type and value type

   e.g.

   ```ts
   type name = "Alice" | "Bob";
   const nameAgeMap: Record<name, number> = {
     Alice: 21,
     Bob: 25,
   };
   ```

4. `Omit`

   - `Omit` removes keys from an object type

   e.g.

   ```ts
   interface Person {
     name: string;
     age: number;
     location?: string;
   }

   const bob: Omit<Person, "age" | "location"> = {
     name: "Bob",
     // `Omit` has removed age and location from the type and they cannot be defined here
   };
   ```

5. `Pick`

   - `Pick` removes all but the specified keys from an object type

   e.g.

   ```ts
   interface Person {
     name: string;
     age: number;
     location?: string;
   }

   const bob: Pick<Person, "name"> = {
     name: "Bob",
     // `Pick` has only kept name, so age and location were removed from the type and they cannot be defined here
   };
   ```

6. `Exclude`

   - `Exclude` removes types from a union

   e.g.

   ```ts
   type Primitive = string | number | boolean;
   const value: Exclude<Primitive, string> = true; // a string cannot be used here since Exclude removed it from the type
   ```

7. `ReturnType`

   - `ReturnType` extracts the return type of a function type

   e.g.

   ```ts
   type PointGenerator = () => { x: number; y: number };
   const point: ReturnType<PointGenerator> = {
     x: 10,
     y: 20,
   };
   ```

8. `Parameters`

   - `Parameters` extracts the parameter types of a function types as an array

   e.g.

   ```ts
   type PointPrinter = (p {x: number; y: number;}) => void;
   const point : Parameters<PointPrinter>[0] = {
    x: 10,
    y: 20
   }
   ```

9. `Readonly`
   - `Readonly` creates a new type where all properties are readonly, meaning they cannot be modified once assigned a value
