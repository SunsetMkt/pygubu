import tkinter as tk
from pygubu.api.v1 import BuilderObject, register_custom_property


class FieldBOMixin:
    """Manages base field properties."""

    base_properties = ("fname", "initial", "required", "help_text")

    def _get_init_args(self, extra_init_args: dict = None):
        args = super()._get_init_args(extra_init_args)
        name = args.get("fname", None)
        if not name:
            args["fname"] = self.wmeta.identifier
        return args

    def _process_property_value(self, pname, value):
        if pname == "required":
            return tk.getboolean(value)
        return super()._process_property_value(pname, value)


register_custom_property("pygubu.forms.*", "fname", "identifierentry")
register_custom_property("pygubu.forms.*", "initial", "entry")
register_custom_property(
    "pygubu.forms.*",
    "required",
    "choice",
    values=("", "false", "true"),
    state="readonly",
)
register_custom_property("pygubu.forms.*", "help_text", "entry")
register_custom_property("pygubu.forms.*", "max_length", "naturalnumber")
register_custom_property("pygubu.forms.*", "min_length", "naturalnumber")
register_custom_property(
    "pygubu.forms.*",
    "strip",
    "choice",
    values=("", "false", "true"),
    state="readonly",
)
register_custom_property("pygubu.forms.*", "empty_value", "entry")