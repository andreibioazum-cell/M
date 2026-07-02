import re

class ProtonCompiler:
    def __init__(self):
        self.cpp_code = [
            "#include <iostream>",
            "#include 'engine.hpp'", // Твой мини-движок для Android
            "extern \"C\" void game_loop() {"
        ]

    def compile(self, code):
        lines = code.split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith("//"): continue

            # Замена alloc на new (ручное управление памятью)
            line = re.sub(r'var (\w+) = alloc (\w+)\((.*)\)', r'\2* \1 = new \2(\3)', line)
            
            # Замена free на delete
            line = re.sub(r'free (\w+)', r'delete \1', line)
            
            # Замена func на void
            line = re.sub(r'func (\w+)\(\)', r'void \1()', line)
            
            # Рисование
            line = re.sub(r'draw_rect\((.*)\)', r'Engine::DrawRect(\1)', line)

            self.cpp_code.append("    " + line)

        self.cpp_code.append("}")
        return "\n".join(self.cpp_code)

# Читаем Proton и сохраняем C++
with open("game.proton", "r") as f:
    source = f.read()

compiler = ProtonCompiler()
with open("jni/main.cpp", "w") as f:
    f.write(compiler.compile(source))
