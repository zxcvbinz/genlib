# genlib
General login tool library for flask back-end

## Installation

Clone this repo in your flask project

```bash
git clone git@github.com:zxcvbinz/genlib.git

pip install -r requirements.txt
```

## Usage

```python
import genlib
#OR
from genlib import 'package'

#database connection
connection = genlib.database.connectToDB(mysql)
if not connection:
   return False

#select from database
sql = "SELECT * FROM `table`"
json_data = genlib.database.selectQuery(connection, sql)
if not json_data:
   return False
```

## License
[MIT](https://github.com/zxcvbinz/genlib/blob/main/LICENSE)