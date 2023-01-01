from lupa import LuaRuntime

lua = LuaRuntime()

sandbox = lua.require("sandbox")[0]
finished, response = sandbox.run("return 1 + 1")

print(response)
