# html_generators

For anyone who wants to generate html with python.

Inspired by React and other "hyperscript" libraries from the javascript world.

## Quick Start

## Background/Philosophy

### Auto Escaping
Attribute values are always escaped. 

### Incremental Adoption
You can use html_generators to generate all of your site's html, or mix it with your existing framework's template system. Ie- in Django, you might implement all of your custom template tags with html_generators, but use the template system to build the majority of your pages).

"Rendering"(TODO: link to rendering) any of our objects generates "safe strings" (which implement `__html__()`). Django and markupsafe (and possibly other python modules) 

### Lazy/Streaming
### Performance

## Package Contents
This section gives a high-level overview of all the features of this package. This is not a complete api reference. For that, just read the source. Anything you can import/access without a leading underscore is considered part of the public api. We recommend installing the package, and reading the source in your python editor of choice.

### \_base.HTMLGenerator
### Element
### Document
### Fragment
### Comment
### Join
### MarkSafe
### classes/styles
### django.DjangoTemplate

## Tips/Warnings
### Render Only Once
### Updating Elements <a name="updating_elements"></a>
### RawTextElement <a name="raw_text_elements"></a>
