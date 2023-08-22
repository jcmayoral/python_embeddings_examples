//#include<iostream>
#define PY_SSIZE_T_CLEAN

#include </usr/include/python3.10/Python.h>
//#include <Python.h>
#include<iostream>

int main(int argc, char** argv){
    std::cout << "hello" <<  std::endl;
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);

    if (program == NULL){
        fprintf(stderr, "Fatal Error: Program cannot decode");
        exit(1);
    }

    Py_SetProgramName(program);
    Py_Initialize();
    PyRun_SimpleString(
        "print('hello world python');" 
        "from math import sqrt\n" 
        "print(sqrt(20))\n" 
    );

    PyRun_SimpleString("exec(open('func.py').read())");


    if (Py_FinalizeEx() < 0){
        exit(120);
    }

    PyMem_RawFree(program);
    return 0;
}