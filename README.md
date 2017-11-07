# test_exercise
## Core of Event Log REST Service

### Functionality:
- it’s possible to push new event to the top of the stream. Service
consumes events in the form of a string like “I just won a lottery
#update @all”, parses them to JSON / Object format and stores in
memory.
- it’s possible to get 10 last events from the top of the stream
- - by category (#update, #poll, #warn)
- - by person (@all, @john, @all-friends)
- - by time

How to construct requests:
There are 3 base object types: events, categories, persons

GET

- Get lists of objects:
- - "events": http --form GET "http://<base_url>/events/"
- - "categories": http --form GET "http://<base_url>/categories/"
- - "persons": http --form GET "http://<base_url>/persons/"

- Get specified object
- - http --form GET http://<base_url>/<object_type>/<object_id>

- Get last 10 events by

- - category(if 10 or more)

http --form GET http://<base_url>/events/?search=<category_name>

- -person(if 10 or more)

http --form GET http://<base_url>/events/?search=<person_name>

- - time(if 10 or more)

http --form GET http://<base_url>/events/?search=<YYYY-mm-dd HH:MM:SS> 

example: 2017-11-07 09:19:08

Last 10 Events are displayed with Paginator mechanism, so you can get next 10
with adding page=<page_nr> to the request.

Example: http://<base_url>/events/?page=2&search=furniture


POST 

- Create event
http --form POST http://127.0.0.1:8000/events/ text="<event_text>"

- Create category or person:
http --form POST http://127.0.0.1:8000/<categories_or_persons>/ name="<name>"


PUT

- Edit event
http --form PUT http://127.0.0.1:8000/events/<event_id>/ text="<event_text>"

- Edit category or person
http --form PUT http://127.0.0.1:8000/<categories_or_persons>/<id>/ name="<name>"


DELETE

http --form DELETE http://127.0.0.1:8000/<event_category_person/<id>/
