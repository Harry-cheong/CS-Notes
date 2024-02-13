# HTML & CSS

## ▷▷▷▷▷ HTML ◁◁◁◁◁

- stands for Hyper Text Mark-up Language
- ! + Tab automatically creates a html doc w basic config

### [🌟] HTML Tags

1. Generic box
   `<div> </div>`

2. Form box
   `<form> </form>`

3. Inputs
   `<input type="text" placeholder="Your name" />`

4. Buttons
   `<btn> Press Me! </btn>`

5. Links
   `<a href="https://google.com"></a>`

## ▷▷▷▷▷ Basic Structure ◁◁◁◁◁

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

### [🌟] Head

[*Syntax*]

```html
<head>
  ...
</head>
```

### [🌟] Body

- what is visible on the webpage

[*Syntax*]

```html
<body>
  ...
</body>
```

### [🌟] Paragraph

- `<p></p>`
- for including text on the webpage

### [🌟] Headers

- `<h1> </h1>`
- p1-6; decreasing size of font on webpage

### [🌟] Attributes

[*Syntax*]
`<a...> </a...>`

1. Links

   - Specify link to website
     `<a href="..."> Harry on LinkedIn </a>`

2. Images

   - No closing tag
   - Specify file path
     `<img src="...">`

## ▷▷▷▷▷ Classes and IDs ◁◁◁◁◁

- Crucial for identifying elements & DOM Manipulation
- IDs has to be unique while classes can be used over and over again

e.g. [*Classes*]

```html
  <p class = "second>
      ...
  </p>
```

e.g. [*IDs*]

```html
<img id="course-image" src="..." /> />
```

## ▷▷▷▷▷ Styling ◁◁◁◁◁

- To link html to css : `<link href = "style.css" rel="stylesheet" >`

[*Syntax*]

```html
<style>
  body {
    ...;
  }
</style>
```

### [🌟] Text Styles

1. `color`

2. `font-family`

3. `font-size`

4. `text-align: center`

5. `text-decoration: [text-decoration-line] [text-decoration-color] [text-decoration-style] [text-decoration-thickness]`
   - text-decoration-line: `underline` `overline` `line-through`
   - text-decoration-style: `solid` `wavy` `double` `dotted` `dashed`

### [🌟] Selector

1. `body{...}`
2. `h1{...}`
3. `\* {...}`

### [🌟] [🌟] Background

- Text box with background

[*Syntax*]

```css
.background {
  background-image: url("URL");
  background-repeat: false;
  background-position: center center;
  background-size: auto auto;
}
```

1. `background-image: url("URL")`

   - use `url` with relative path to display images in dir

2. `background-repeat: [bool]`

   - repeats the image when space allows

3. `background-position: 0% 0%` / `background-position: xpos ypos`

   - the first value is the horizontal positon and the second value is the vertical
   - the first value is the horizontal position and the second value is the vertical

4. `background-size: auto auto`
   - scales the image

### [🌟] [🌟] Element Display

[*Syntax*]
`display: value`

1. inline

   - displays an element as an inline element

2. block

   - displays an element as a block element; it starts on new line and takes up the whole width

3. flex

   - displays an element as a block-level flex container

4. grid

   - displays an element as a block-level grid container (all child elements are displayed in block)

5. table

   - let the element behave like a `<table>` element (all child elements are displayed inline)

6. inline-block

   - displays an element as an inline-level block container

7. inline-flex

   - displays an element as an inline-level flex container

8. inline-table

   - displays an element as an inline-level table

9. none

   - hide display

### [🌟] [🌟] Position

[*Syntax*]

```css
.position {
  positon: value;
  top: value;
  left: value;
}
```

1. relative

   - element is positoned relative to its normal position
   - e.g. "left: 20px" adds 20 pixels to the element's LEFT position

2. absolute
   - positioned relative to its first positioned

### [🌟] [🌟] Useful Snippets

1. Centralising a box relative to another element

   [*Syntax*]

   ```css
   .center {
     positon: absolute;
     top: 50%;
     left: 50%
     transform: translate(-50%, -50%);
   }
   ```

2. Image with link

   [*syntax*]

   ```html
   <a href="https://google.com">
      <img src="/pic.png" />
   </a>  
   ```

## ▷▷▷▷▷ The CSS Box Model ◁◁◁◁◁

- Any webpage can be broken down into boxes
- Each box has 5 properties: content, padding, border, margin and fill area

1. Context - text, images, etc
2. Padding - transparent area around the content, inside of the box
3. Border - goes around the padding and the content
4. Margin - space between boxes 5. Fill area - area that gets filled with background color or background image
