---
layout: default
nav_order: 2
title: Example Markdown
---

# Example Markdown

Github Flavored Markdown (GFMD) is based on [Markdown Syntax Guide](http://daringfireball.net/projects/markdown/syntax).
 * Described at [Github Flavored Markdown](http://github.github.com/github-flavored-markdown/)
 * Basic syntax examples: https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
 * Table Examples: https://docs.github.com/en/github/writing-on-github/organizing-information-with-tables

## Text Writing
It is easy to write in GFMD. Just write simply like text and use the below simple "tagging" to mark the text and you are good to go!  

To specify a paragraph, leave 2 spaces at the end of the line

## Headings
To create a heading, add one to six # symbols before your heading text. The number of # you use will determine the size of the heading. (Please don't use more than four)

```
## Sample H2
### Sample H3
```

will produce
## Sample H2
### Sample H3

---


## Text Formatting

**Bold Text** is done using `**Bold Text**`  

**Bold Text** is also done using `__Bold Text__`  

*Italic Text* is done using `*Italic Text*`

_Italic Text_ is also done using `_Italic Text_`

---

## Hyperlinks
- GFMD will automatically detect URL and convert them to links like this http://www.futureworkz.com
- To specify a link on a text, do this:

```
This is [an example](http://example.com/ "Title") inline link.
[This link](http://example.net/) has no title attribute.
```

---

## Creating list

Adding a `-` will change it into a list:

```
- Item 1
- Item 2
- Item 3
```

will produce

- Item 1
- Item 2
- Item 3

---

## Horizontal Rules

Horizontal rule is created using `---` on a line by itself.

---

## Coding - Block

<pre>
```ruby
# The Greeter class
class Greeter
  def initialize(name)
    @name = name.capitalize
  end

  def salute
    puts "Hello #{@name}!"
  end
end

# Create a new object
g = Greeter.new("world")

# Output "Hello World!"
g.salute
```
</pre>
 
will produce  

```ruby
# The Greeter class
class Greeter
  def initialize(name)
    @name = name.capitalize
  end

  def salute
    puts "Hello #{@name}!"
  end
end

# Create a new object
g = Greeter.new("world")

# Output "Hello World!"
g.salute
```

Note: You can specify the different syntax highlighting based on the coding language eg. ruby, sh (for shell), php, etc  
Note: You must leave a blank line before the `\`\`\``

## Coding - In-line
You can produce inline-code by using only one \` to enclose the code:

```
This is some code: `echo something`
```

will produce  

This is some code: `echo something`

---

## Adding Image

```
![Branching Concepts](http://git-scm.com/figures/18333fig0319-tn.png "Branching Map")
```

---

## Escape sequence
You can escape using \\ eg. \\\`

---


## Quoting

You can create a quote using `>`:

```
> This is a quote
```

will produce

> This is a quote

## Tables
You can create tables with pipes | and hyphens -. Hyphens are used to create each column's header, while pipes separate each column. You must include a blank line before your table in order for it to correctly render.

```
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
```
will produce

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

