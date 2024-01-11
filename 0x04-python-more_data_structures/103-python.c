#include <Python.h>

/**
 * print_python_bytes - prints infor for Python bytes objects.
 * @p: pointer to the PyObject struct.
 * Return: void.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytesize, i;
	char *bytestring;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		bytestring = PyBytes_AsString(p);
		bytesize = PyBytes_Size(p) + 1;
		printf("  size: %ld\n", PyBytes_Size(p));
		printf("  trying string: %s\n", bytestring);
		if (bytesize >= 10)
			bytesize = 10;
		printf("  first %ld bytes:", bytesize);
		for (i = 0; i < 10 && i < bytesize; i++)
		{
			if (bytestring[i] < 0)
				printf(" %02x", bytestring[i] + 256);
			else
				printf(" %02x", bytestring[i]);
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}


/**
 * print_python_list - prints list info for PyObject.
 * @p: pointer to the PyObject struct.
 * Return: void.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t listsize, i;
	PyObject *element;

	listsize = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", listsize);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < listsize; i++)
	{
		element = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, (((PyObject*)(element))->ob_type)->tp_name);
		if (PyBytes_Check(element))
			print_python_bytes(element);

	}
}
