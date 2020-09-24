# html_generators

TODO - explain how to use

## Escaping
In general, anything you pass as content or an attribute of an Element will be escaped.

The only exceptions are:
- Style
- Script
- Comment

Content passed to these nodes will NOT be escaped (since the escaping rules for them are more relaxed, and you often want/need to put literal '<' or '>' characters in them). You should never pass untrusted user content to these generators. 

In addition, any content passed to MarkSafe will not be escaped.
