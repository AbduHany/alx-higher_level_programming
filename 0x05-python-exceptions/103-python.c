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

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		bytestring = ((PyBytesObject *)p)->ob_sval;
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


void print_python_float(PyObject *p)
{
	double value;
	PyFloatObject *obj;
	char *floatstr;

	obj = (PyFloatObject*)p;
	value = obj->ob_fval;
	printf("[.] float object info\n");
	if (PyFloat_Check(p))
	{
		floatstr = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	        printf("  value: %s\n", floatstr);
		return;
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
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

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		listsize = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %ld\n", listsize);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < listsize; i++)
		{
			element = PyList_GET_ITEM(p, i);
			printf("Element %ld: %s\n", i, (((PyObject*)(element))->ob_type)->tp_name);
			if (PyBytes_Check(element))
				print_python_bytes(element);
			else if (PyFloat_Check(element))
				print_python_float(element);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
