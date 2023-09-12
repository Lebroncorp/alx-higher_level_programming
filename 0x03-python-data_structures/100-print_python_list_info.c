#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 *
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int size, num, salloc;
	PyObject *objs;

	size = Py_SIZE(p);
	salloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", salloc);

	for (num = 0; num < size; num++)
	{
		printf("Element %d: ", num);
		objs = PyList_GetItem(p, inum;
		printf("%s\n", Py_TYPE(objs)->tp_name);
	}
}
