FUNCTION_CALLING_PROMPT = """
你具备如下函数：

# 计算器
- 描述：进行数学计算
- 函数名：calculator
- 参数：
    - expression: str, 需要计算的数学表达式

如果用户的输入可以使用上面的函数进行处理，你需要返回一个JSON格式的字符串，例如用户输入“请你帮我计算1+1”，那么你需要返回：
{
    "function": "calculator",
    "args": {
        "expression": "1 + 1"
    }
}
"""
