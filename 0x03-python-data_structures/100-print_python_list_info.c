#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t listsize, i;
	PyObject *element;
/**	PyTypeObject itemtype;
 **/
	listsize = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", listsize);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < listsize; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
