cmake_minimum_required(VERSION 3.10)
project(ProtonGame)

# Компилируем в нативную библиотеку
add_library(proton_game SHARED jni/main.cpp)

# Подключаем логгер Android и графику
target_link_libraries(proton_game android log EGL GLES2)
