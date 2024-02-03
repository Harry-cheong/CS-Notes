# \***\*\*\*\*\***\_\_\_\***\*\*\*\*\*** HTML \***\*\*\*\*\***\_\_\_\***\*\*\*\*\***

- stands for Hyper Text Mark-up Language
- ! + Tab automatically creates a html doc w basic config

## **\*\*\*\***\_\_**\*\*\*\*** Basic Structure **\*\*\*\***\_\_**\*\*\*\***

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>...</h1>
    <p></p>
  </body>
</html>
```

| [🌟] Head |

[~Syntax~]

```html
<head>
  ...
</head>
```

| [🌟] Body |

- what is visible on the webpage

[~Syntax~]

```html
<body>
  ...
</body>
```

| [🌟] Paragraph |

- `<p></p>`
- for including text on the webpage

| [🌟] Headers |

- `<h1> </h1>`
- p1-6; decreasing size of font on webpage

| [🌟] Attributes |

[~Syntax~]
`<a...> </a...>`

1. Links

   - Specify link to website
     `<a href="..."> Harry on LinkedIn </a>`

2. Images

   - No closing tag
   - Specify file path
     `<img src="...">`

## **\*\*\*\***\_\_**\*\*\*\*** Classes and IDs **\*\*\*\***\_\_**\*\*\*\***

- Crucial for identifying elements & DOM Manipulation
- IDs has to be unique while classes can be used over and over again

e.g. [Classes]

````html
  <p class = "second>
      ...
  </p>
  ```

e.g. [IDs]

```html
<img id = "course-image" src="..."> />
'''

## **\*\*\*\***\_\_**\*\*\*\*** Basic Features **\*\*\*\***\_\_**\*\*\*\***

  1. Generic box

  [~Syntax~]
  `<div> </div>`

  2. Form box
  * Semantics: using the most suitable <>

  [~Syntax~]
  `<form> </form>`

  3. Inputs
  `<input type="text" placeholder="Your name" />`

## ****\*\*****\_\_****\*\***** Styling ****\*\*****\_\_****\*\*****

- To link html to css : `<link href = "style.css" rel="stylesheet" >`

```html
<style>
  body {
      ...
  }
</style>
'''

| [🌟] Properties |

  1. background-color

  2. font-family

  3. font-size

  4. border: border-thickness typeofline color

  5. margin
  - sets margin on all 4 sides
  - margin ~position~ to set the size of specific side

  6. padding

  7. text-align: center

| [🌟] Selector | 1. body{...} 2. h1{...} 3. \* {...}

**\*\*\*\***\_**\*\*\*\*** The CSS Box Model **\*\*\*\***\_**\*\*\*\***

- Any webpage can be broken down into boxes
- Each box has 5 properties: content, padding, border, margin and fill area

1. Context

- text, images, etc

2. Padding

- transparent area around the content, inside of the box

3. Border

- goes around the padding and the content

4. Margin

- space between boxes

5. Fill area

- area tha gets filled with background color or background image
````
