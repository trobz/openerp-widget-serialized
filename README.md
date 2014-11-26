OpenERP Web Serialized Widget
=============================

Form widget for `fields.serialized` type, providing a friendly JSON editor based on
[Jos de Jong JSON editor](https://github.com/josdejong/jsoneditor).


## Installation / Use

- install the module in your project
- define `serialized` widget for your field on view form:

```
<field name="arch" type="xml">
  <form string="Foo">
    ...
    <field name="bar" widget="serialized" />
    ...
  </form>
</field>
```

## Layout

**View mode**

![OpenERP serialized widget: view mode](https://raw.github.com/trobz/openerp-widget-serialized/master/doc/widget_serialized_view.png "View mode")

**WYSIWYG edit mode**

![OpenERP serialized widget: WYSIWYG edit mode](https://raw.github.com/trobz/openerp-widget-serialized/master/doc/widget_serialized_edit_wysiwyg.png "WYSIWYG edit mode")


**Code edit mode**

![OpenERP serialized widget: code edit mode](https://raw.github.com/trobz/openerp-widget-serialized/master/doc/widget_serialized_code.png "Code edit mode")


## Dependencies

This widget depend on [web unleashed](https://github.com/trobz/openerp-web-unleashed) module, helping on managing
the initialization of views and widgets on OpenERP.

Odoo 8.0 doesn't support `fields.serialized` anymore, you have to install the server wide module `base_field_serialized` from OCA [server-tools][1] repository.

Note: 

It's not a hard dependencies and you can refactor the code and remove this dependencies by change the way the widget is
initialized if you really don't need web unleashed (but you may have a look at features provided by unleashed first ;)).

  [1]: https://github.com/OCA/server-tools/
