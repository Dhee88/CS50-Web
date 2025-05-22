# 📚 CS50 Web – Week 0 Notes  
### Topic: HTML, CSS & Git

---

## 📄 HTML Basics

- **HTML** (HyperText Markup Language) defines the **structure and content** of a webpage using tags and elements.

### 🧱 Basic HTML Structure
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>My Website</title>
  </head>
  <body>
    <h1>Hello!</h1>
  </body>
</html>

### 🔖 Common Tags
- <html>, <head>, <title>, <body>
- Headings: <h1> to <h6>
- Paragraphs: <p>Paragraph here</p>
- Links: <a href="https://example.com">Link</a>
- Images: <img src="image.jpg" alt="image" width="300">
- Line break: <br>, Horizontal line: <hr>
- Emphasis: <strong>, <em>
- Division/sections: <div>

---

## 🔢 Lists

### Ordered List (Numbered)
<ol>
  <li>First item</li>
  <li>Second item</li>
</ol>

### Unordered List (Bulleted)
<ul>
  <li>Item one</li>
  <li>Item two</li>
</ul>

---

## 📊 Tables
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dhee</td>
      <td>19</td>
    </tr>
  </tbody>
</table>

---

## 📝 Forms

<form>
  <input type="text" name="name" placeholder="Full Name">
  <input type="password" name="password" placeholder="Password">

  <label><input type="radio" name="gender" value="female"> Female</label>
  <label><input type="radio" name="gender" value="male"> Male</label>

  <input name="country" list="countries">
  <datalist id="countries">
    <option value="Afghanistan">
    <option value="Albania">
    <option value="India">
  </datalist>

  <input type="submit" value="Submit">
</form>

---

## 🎨 CSS Basics

### Types of CSS
- **Inline**: style="..."
- **Internal**: <style> tags inside HTML
- **External**: Linked .css file

### Inline CSS
<h1 style="color: red; text-align: center">Hello</h1>

### Internal CSS
<style>
  body {
    background-color: lightgray;
    font-family: Arial;
    font-size: 28px;
    font-weight: bold;
  }
  h1 {
    border: 3px solid black;
    color: navy;
    background-color: blue;
    width: 100px;
    height: 400px;
    padding: 20px;
    margin: 20px;
  }
</style>

### External CSS
<link rel="stylesheet" href="styles.css">

### CSS Selectors
h1, div {
  color: blue;
  font-size: 24px;
}

#foo {
  color: red;
}

.foo {
  color: red;
}

### CSS Specificity (Priority)
1. Inline
2. ID
3. Class
4. Type (element)

### Advanced Selectors
- a, b : Multiple Element
- a b : Descendant
- a > b : Direct Child
- a + b : Adjacent Sibling
- [attr=value] : Attribute Selector
- a:hover : Pseudo-class
- a::before : Pseudo-element

---

## 📱 Responsive Design

### Viewport Meta Tag
<meta name="viewport" content="width=device-width, initial-scale=1.0">

### Media Queries
<style>
  @media (min-width: 600px) {
    body {
      background-color: red;
    }
  }

  @media (max-width: 599px) {
    body {
      background-color: blue;
    }
  }
</style>

---

## 📐 Layouts

### Flexbox
<style>
  #container {
    display: flex;
    flex-wrap: wrap;
  }
</style>

### Grid
<style>
  #container {
    display: grid;
    padding: 20px;
    grid-column-gap: 20px;
    grid-row-gap: 10px;
    grid-template-columns: 200px 200px auto;
  }
</style>

---

## 🎨 Bootstrap (CSS Framework)

- A prebuilt CSS library to help style components quickly.
- Grid system based on 12-column layout.
- Responsive by default.

---

## 🧵 SASS (.scss)

- A CSS preprocessor — must be compiled into CSS.
- Allows variables, nesting, mixins, inheritance.

### Example
```scss
$color: red;

ul {
  font-size: 14px;
  color: $color;
}

ol {
  font-size: 18px;
  color: $color;
}

Inheritance
 %message {
  font-family: sans-serif;
  font-size: 18px;
  font-weight: bold;
}

.success {
  @extend %message;
  background-color: green;
}

