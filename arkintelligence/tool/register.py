import inspect

from docstring_parser import parse


def _is_parameter_required(func, arg_name):
    # Inspect from function signature
    sig = inspect.signature(func)
    param = sig.parameters.get(arg_name)
    if not param:
        return True
    return param.default == inspect.Parameter.empty


def parse_function_info(func):
    docstring = parse(func.__doc__)

    name = func.__name__
    short_desc = docstring.short_description
    long_desc = docstring.long_description
    if short_desc != None and long_desc != None:
        desc = f"{short_desc} {long_desc}"
    elif short_desc != None and long_desc == None:
        desc = short_desc
    elif short_desc == None and long_desc != None:
        desc = long_desc
    else:
        # TODO(LotsoTeddy): Add warning-level log.
        print("Function desc not provided!")
        desc = "No description provided. Plese understand the function ability according to the function name."

    tool = {
        "type": "function",
        "function": {
            "name": name,
            "description": desc,
            "parameters": {
                "type": "object",
                "properties": {
                    arg.arg_name: {
                        "type": arg.type_name,
                        "description": arg.description,
                    }
                    for arg in docstring.params
                },
                "required": [
                    arg.arg_name
                    for arg in docstring.params
                    if _is_parameter_required(func, arg.arg_name)
                ],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }

    return tool


def ArkTool(func):
    if not hasattr(ArkTool, "registry"):
        ArkTool.registry = {}
        ArkTool.function = {}
    tool = parse_function_info(func)
    ArkTool.registry[tool["function"]["name"]] = tool
    ArkTool.function[tool["function"]["name"]] = func
    return func
