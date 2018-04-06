import pysolr

SERVER = "http://localhost:8983/solr/booksearch"

connection = pysolr.Solr(SERVER)

print("Deleting all records in Solr")
connection.delete(q="*:*")

print("Indexing Demo documents in Solr")
connection.add([
    {"pk": 1,
     "type": "book",
     "title_s": "Charlotte's Web"}
])

connection.commit()