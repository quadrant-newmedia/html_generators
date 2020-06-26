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