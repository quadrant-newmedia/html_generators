### 1.5.1
Fix bug introduced in 1.5.0 (void elements and raw text elements were not normalizing attribute names).

## 1.5.0
Added `classes` and `styles` utility functions, and `add_classes` and `add_styles` methods to `Element`.

### 1.4.1

Attributes which clash with python keywords can now be postfixed with '_', as well as prefixed (PEP 8 recommends postfix).

## 1.4

Added `h.Join(joiner, iterable)`

### 1.3.1

Ensure that attributes with value 0 are rendered (the only values skipped are False and None).

## 1.3.0

Add support for comments.

### 1.2.1

Ensure that children with value 0 (any number type) are rendered (the only values skipped are False and None).

## 1.2.0

Support "Safe Strings" from frameworks like Django. Children with `__html__()` method will not be escaped.

## 1.1.0

Do not escape contents of `<script>` and `<style>`

# 1.0.0

Changed import names in top-level module. We now import all names directly from `elements.py`, and dropped the 'e' alias. 

We now recommend importing the entire package with an alias of 'h':
```
import html_generators as h
```

`html_generators.django_template` has been renamed to `html_generators.django`

## 0.3.0

Added `django_template.DjangoTemplate`, for easier inclusion of django templates.

## 0.2.0

`str()` output now implements `__html__()`, so many frameworks (including Django) know they don't need to escape it.

## 0.1.0
Added Fragment

# 0.0.0