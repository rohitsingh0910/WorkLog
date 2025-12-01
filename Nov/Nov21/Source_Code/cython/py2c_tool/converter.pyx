# cython: boundscheck=False
# cython: wraparound=False
# cython: nonecheck=False
# cython: cdivision=True

from libc.stdio cimport fopen, fclose, fgets, fputs, FILE
from libc.stdlib cimport malloc, free
from libc.string cimport strlen, strncmp, strstr

cdef int MAX_LINE = 4096

cdef void convert_file(const char* input_path, const char* output_path):
    cdef FILE* in_file = fopen(input_path, "r")
    cdef FILE* out_file = fopen(output_path, "w")

    cdef char *buf
    cdef char *p
    cdef int indent = 0
    cdef int i
    cdef char c

    if not in_file or not out_file:
        if in_file: fclose(in_file)
        if out_file: fclose(out_file)
        return

    # Allocate buffer
    buf = <char*> malloc(MAX_LINE)

    # Write header
    fputs("/* Auto-generated C (template) from Python source */\n", out_file)
    fputs("#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\n", out_file)

    # Read lines
    while fgets(buf, MAX_LINE, in_file) != NULL:

        # Trim leading spaces
        p = buf
        while p[0] == ' ' or p[0] == '\t':
            p += 1

        # Detect function definitions: def something():
        if strncmp(p, "def ", 4) == 0:
            fputs("\n/* function translated */\n", out_file)
            fputs("void ", out_file)

            # copy name + args until ':'
            for i in range(strlen(p)):
                c = p[i]
                if c == ':':
                    fputs(" {\n", out_file)
                    break
                else:
                    fputs(bytes([c]), out_file)

            indent += 1
            continue

        # translate return
        if strstr(p, "return ") != NULL:
            fputs("    /* return translated */\n", out_file)
            fputs("    return;\n", out_file)
            continue

        # translate print
        if strstr(p, "print(") != NULL:
            fputs("    /* print translated */\n", out_file)
            fputs("    printf(\"(value)\\n\");\n", out_file)
            continue

        # close blocks when blank line appears
        if p[0] == '\n' or p[0] == 0:
            if indent > 0:
                indent -= 1
                fputs("}\n", out_file)
            continue

        # fallback: output as comment
        fputs("/* py: ", out_file)
        fputs(p, out_file)
        fputs("*/\n", out_file)

    free(buf)
    fclose(in_file)
    fclose(out_file)

# Python wrapper so Python can call the C function
    def convert_file_py(input_path: bytes, output_path: bytes):
        convert_file(<const char*> input_path, <const char*> output_path)

