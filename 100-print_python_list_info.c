#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: PyObject
 *
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size;
	const char *item_type;
	PyListObject *list;

	size = PyList_Size(p);
	list = (PyListObject*)p;

	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)list->allocated);
	for (i = 0; i < size; i++)
	{
		item_type = Py_TYPE(PyList_GetItem(p,i))->tp_name;
		printf("Element %d: %s\n", (int)i, item_type);
	}	
}
