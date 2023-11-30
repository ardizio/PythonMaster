## Accessing Files

The open function in Python supports several modes and options for reading and writing files. Here are the commonly used modes:

### Read Modes:

`r`: Open for reading (default).

`rb`: Open for reading in binary mode.

### Write Modes:

`w`: Open for writing. Creates a new file or truncates the existing file.

`wb`: Open for writing in binary mode.

`a`: Open for writing. Creates a new file or appends to the existing file.

`ab`: Open for writing in binary mode.

### Text and Binary Modes:

`t`: Text mode (default). If not specified, it is assumed.

`b`: Binary mode.

### Read and Write Modes:

`r+`: Open for reading and writing.

`w+`: Open for reading and writing. Creates a new file or truncates the existing file.

`a+`: Open for reading and writing. Creates a new file or appends to the existing file.

`rb+`: Open for reading and writing in binary mode.

`wb+`: Open for reading and writing in binary mode.

`ab+`: Open for reading and writing in binary mode.

### Append Modes:

`a`: Open for writing. Creates a new file or appends to the existing file.

`ab`: Open for writing in binary mode.

### Exclusive Creation:

`x`: Exclusive creation. If the file already exists, the operation will fail.