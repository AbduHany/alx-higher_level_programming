#include <Python.h>

/**
 * print_python_string - prints Python strings and info about them.
 * @p: pointer to PyObject struct.
 *
 * Return: void.
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t strlen;
	PyTypeObject *type;
	int unicodetype;
        Py_UNICODE *string;

	fflush(stdout);
	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
	{
		string = PyUnicode_AsWideCharString(p, &strlen);
		strlen = PyUnicode_GET_LENGTH(p);
		if (PyUnicode_IS_COMPACT_ASCII(p))
		{
			printf("  type: compact ascii\n");
		}
		else
		{
			printf("  type: compact unicode object\n");
		}
		printf("  length: %ld\n", strlen);
		printf("  value: %ls\n", string);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
