import pysolr

<<<<<<< HEAD

=======
>>>>>>> resolve
SERVER = "http://localhost:8983/solr/booksearch"

connection = pysolr.Solr(SERVER)

print("Deleting all records in Solr")
connection.delete(q="*:*")

print("Indexing Demo documents in Solr")
<<<<<<< HEAD
connection.add([{
    "pk": 1,
    "type": "book",
    "title_s": "Charlotte's Web"
},
{
    "pk": 1,
    "type": "author",
    "last_name_s": "White",
    "first_name_s": "E.B."
},
{
    "pk": 2,
    "type": "author",
    "last_name_s": "Rowling",
    "first_name_s": "J.K."
}])

connection.commit()
=======
connection.add([
    {"pk": 1,
     "type": "book",
     "title_s": "Charlotte's Web"}
])

connection.commit()
>>>>>>> resolve
