| Category         | Data Type     | Description              | Example                             |
| ---------------- | ------------- | ------------------------ | ----------------------------------- |
| Integer          | `int8`        | 8-bit signed integer     | -128 to 127                         |
|                  | `int16`       | 16-bit signed integer    | -32,768 to 32,767                   |
|                  | `int32`       | 32-bit signed integer    | Common on many systems              |
|                  | `int64`       | 64-bit signed integer    | Very large integers                 |
| Unsigned Integer | `uint8`       | 8-bit unsigned integer   | 0 to 255                            |
|                  | `uint16`      | 16-bit unsigned integer  | 0 to 65,535                         |
|                  | `uint32`      | 32-bit unsigned integer  | Positive integers only              |
|                  | `uint64`      | 64-bit unsigned integer  | Very large positive integers        |
| Floating Point   | `float16`     | Half precision           | Lower memory usage                  |
|                  | `float32`     | Single precision         | Common in Machine Learning          |
|                  | `float64`     | Double precision         | Default floating-point type         |
| Complex Numbers  | `complex64`   | Two `float32` values     | `2+3j`                              |
|                  | `complex128`  | Two `float64` values     | Higher precision                    |
| Boolean          | `bool_`       | Stores `True` or `False` | `True`                              |
| String           | `str_`        | Unicode strings          | `"Hello"`                           |
| Bytes            | `bytes_`      | Byte strings             | `b"Hello"`                          |
| Object           | `object_`     | Stores Python objects    | Lists, dictionaries, custom objects |
| Date & Time      | `datetime64`  | Dates and timestamps     | `2026-07-28`                        |
| Time Difference  | `timedelta64` | Duration between dates   | `5 days`                            |
