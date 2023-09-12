#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists.
 * @p: PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int size, goodlloc, num;
	PyObject *pyobjs;

	size = Py_SIZE(p);
	goodlloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", goodlloc);
	for (num = 0; num < size; num++)
	{
		pyobjs = PyList_GetItem(p, num);
		printf("Element %d: %s\n", num, Py_TYPE(pyobjs)->tp_name);
	}
}
