# Claridad Scraper

Scrapes and exports to CSV format current(01/05/2018) Claridad Puerto Rico website.
We will use this to migrate to Wordpress.

## Setup

1. Install `python 3.7`, `pip`, `virtualenv`. On Mac OS X you can install python via 
`brew install python` and that will include `pip`. After wards `virtualenv` should be
installed via `pip install virtualenv`. I would read its documentation for more detailed
instructions.

2. Create a `virtualenv`

We will install all of our dependencies on the `virtualenv`. Create a `virtualenv` using 
the `python 3.7` interpreter:

`virtualenv -p $(which python3.7) /path/to/env`

Take note of where you place `/path/to/env`, I recommend to place it under 
`~/.virtualenvs/claridad_scraper/`.

3. Activate the `virtualenv`

Run `source /path/to/env/bin/activate`, after doing this our `python` environment will use
our `virtualenv`. You can see this by running `which python` after activating the `virtualenv`.
It should be something like `/path/to/env/bin/python`. Now when we install dependencies, they
will be installed to our `virtualenv`.

You will need to activate the `virtualenv` in every single terminal tab that you will use the
project in, look for `(env)` on your command prompt, this will let you know the `virtualenv` 
is active.  

4. Clone the repo and install dependencies 

```bash

(env) prompt $ git clone https://github.com/wilbertom/claridad_scraper
(env) prompt $ cd claridad_scraper
(env) prompt $ pip install -r requirements.txt
```


Now you should be ready to run the project.

## Scraper

Running the scraper will take while.

```bash
(env) prompt $ ./cli scraper --help
(env) prompt $ ./cli scraper --db-path output
```

The scraper will every web page one by one saving its contents in a database. We only scrape
one page at a time because we don't know how much load the website can take. The initial scrape
will be several hours but running the scraper a second time will be much faster because the
scraper will use cached responses from the database, meaning it won't fetch the same web pages
twice. If you want to make changes to the code and see the difference, you can rerun the scraper
with a different `--db-path` and see the differences in the databases.

Storing the data in the database allows us to use cached responses during scraping and it lets use
the local data while parsing instead of having to fetch the data everytime we want to change our
data parsing.

## Database

The database has some useful data if you want to poke around with `sqlite3`.

```
	id           - Incremental row id
	link TEXT    - The webpage url
	content TEXT - Raw content without any encoding. Use this for binaries like PDF and jpegs instead of the text column.
	status_code  - HTTP response code 
	headers      - HTTP response headers 
	error        - True when we had an error scraping the webpage
	content_type - Content type ie: text/html, image/jpeg and so on 
	text         - The webpage content encoded as utf8 
	encoding     - Webpage encoding, we parse this from the webpage html meta because, HTTP headers are wrong
```

## Wordpress Exports


### Users

We export users to a CSV file that needs to be imported directly into Wordpress using MySQL.
This must be done before importing posts because if the author names are not present in the
database, the posts importer will assign the wrong author.

```bash
(env) prompt $ ./cli export-users --help
(env) prompt $ ./cli export-users --db-path output --to 'users.csv' --starting-id 2
```

The `--starting-id` is important, it should be one higher than the current the biggest `id` in Wordpress to avoid
collisions:

```
mysql> select (select max(id) from wp_users) + 1;
```

Then from mysql we can import the users:

```
mysql> LOAD DATA INFILE '/var/lib/mysql-files/users.csv' into table wp_users
  CHARACTER SET 'utf8'
  FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\r\n'
  IGNORE 1 ROWS;
```

The file might need to be placed on the MySQL server secure data directory if MySQL is configured with `--secure-file-priv`. 

```
mysql> SHOW VARIABLES LIKE "secure_file_priv";
```

### Posts

We export posts into a CSV file that is process by [Really Simple CSV Importer](https://wordpress.org/plugins/really-simple-csv-importer/).

```bash
(env) prompt $ ./cli export-posts --help
(env) prompt $ ./cli export-posts --db-path output --to 'posts.csv'
```

Then you can take CSV file and upload it via the Wordpress Admin panel.
