# Rosie
Rosie is a compiled and object-oriented programming language designed to be simpler than c++, without loosing preformance. For example, a simple hello world in c++ requires:
```
#include <iostream>
int main(){
  std::cout << "hello world";
}

```
however, we can write the same program in Rosie in just two lines:
```
add io/io
io.out("hello world")
```
The Rosie compiler is also easy to use! To compile a program, just type `Rosie <file>`, or add custom aurguments like `--clean=false`,`--clang` or `--gcc` to change how the compiler acts.
Ready to give Rosie a try? Download the [installer](https://github.com/CardboardDog/Rosie-Lang/releases/download/installer-window/install.exe) for windows, or [build](https://github.com/CardboardDog/Rosie-Lang/archive/refs/heads/main.zip) it your self!
<br\>
### Note: building from the source is suggested becuase it will always be up to date, while the installer is only released for major versions
