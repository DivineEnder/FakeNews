# @Author: DivineEnder <DivinePC>
# @Date:   2017-03-08 12:27:35
# @Email:  danuta@u.rochester.edu
# @Last modified by:   DivineEnder
# @Last modified time: 2017-03-20 21:45:08

# from Utils.db_utils import commits_connection as cc
# from Utils.db_utils import uses_connection as uc
import Utils.connection_utils as glc

# -----------
# | Sources |
# -----------
def get_all_sources(cursor = None):
	return glc.execute_db_query("""SELECT * FROM SOURCES""", cursor = cursor)

def get_sources(ids, cursor = None):
	return glc.execute_db_query("""SELECT * FROM sources WHERE source_id = ANY(%s)""", (ids,), cursor = cursor)

def get_source(iden, cursor = None):
	return get_sources([iden], cursor = cursor)[0]

def get_sources_named(names, cursor = None):
	return glc.execute_db_query("""SELECT * FROM sources WHERE name = ANY(%s)""", (names,), cursor = cursor)

def get_source_named(name, cursor = None):
	return get_sources_named([name], cursor = cursor)[0]
# -----------
# | Sources |
# -----------

# ------------
# | Articles |
# ------------
def get_all_articles(cursor = None):
	return glc.execute_db_query("""SELECT * FROM articles""", cursor = cursor)

def get_articles(ids, cursor = None):
	return glc.execute_db_query("""SELECT * FROM articles WHERE article_id = ANY(%s)""", (ids,), cursor = cursor)

def get_article(iden, cursor = None):
	return get_articles([iden], cursor = cursor)[0]

def get_articles_linked(urls, cursor = None):
	return glc.execute_db_query("""SELECT * FROM articles WHERE url = ANY(%s)""", (urls,), cursor = cursor)

def get_article_linked(url, cursor = None):
	return get_articles_linked([url], cursor = cursor)[0]

def get_articles_entitled(title, cursor = None):
	return glc.execute_db_query("""SELECT * FROM articles WHERE title = %s""", (title,), cursor = cursor)
# ------------
# | Articles |
# ------------

# -----------
# | Authors |
# -----------
def get_all_authors(cursor = None):
	return glc.execute_db_query("""SELECT * FROM authors""", cursor = cursor)

def get_authors(ids, cursor = None):
	return glc.execute_db_query("""SELECT * FROM authors WHERE author_id = ANY(%s)""", (ids,), cursor = cursor)

def get_author(iden, cursor = None):
	return get_authors([iden], cursor = cursor)[0]

def get_author_named(first_name, last_name, cursor = None):
	return glc.execute_db_query("""SELECT * FROM authors WHERE first_name = %s AND last_name = %s""", (first_name, last_name), cursor = cursor)[0]

def get_authors_first_named(first_name, cursor = None):
	return glc.execute_db_query("""SELECT * FROM authors WHERE first_name = %s""", (first_name,), cursor = cursor)

def get_authors_last_named(last_name, cursor = None):
	return glc.execute_db_query("""SELECT * FROM authors WHERE last_name = %s""", (last_name,), cursor = cursor)
# -----------
# | Authors |
# -----------

# --------
# | Tags |
# --------
def get_all_tags(cursor = None):
	return glc.execute_db_query("""SELECT * FROM tags""", cursor = cursor)

def get_tags(ids, cursor = None):
	return glc.execute_db_query("""SELECT * FROM tags WHERE tag_id = ANY(%s)""", (ids,), cursor = cursor)

def get_tag(iden, cursor = None):
	return get_tags([iden], cursor = cursor)[0]

def get_tags_named(tag_names, cursor = None):
	return glc.execute_db_query("""SELECT * FROM tags WHERE tag_name = ANY(%s)""", (tag_names,), cursor = cursor)

def get_tag_named(tag_name, cursor = None):
	return get_tags_named([tag_name], cursor = cursor)[0]
# --------
# | Tags |
# --------

# ---------
# | Links |
# ---------
def get_article_authors(article_id, cursor = None):
	return glc.execute_db_query("""SELECT author_id FROM article_authors WHERE article_id = %s""", (article_id,), cursor = cursor)
# ---------
# | Links |
# ---------