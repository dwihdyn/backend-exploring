<h2>Step by step how to launch</h2>
<ol>
<li>git clone, create conda env python 3.7 , </l1>
<li>pip install peewee, peewee-db-evolve, psycopg2-binary</li>
<li> terminal -> `python` -> `from migrate import *` -> `from models import *` </l1>
<li> new terminal -> `createdb todo_list` -> `psql todo_list` -> `\dt` to see all tables</li>
<li> terminal -> `python` -> insert dummy data, can be found  in `main.py`  ->`from main import *`</li>
</ol>

<h5>if still lost, refer to `notes` in this file </h5>

<h6>remember to exit, reenter python everytime you make any changes in any .py file !!!!!</h6>