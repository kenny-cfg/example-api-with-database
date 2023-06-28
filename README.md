# example-api-with-database
Example API with a database

## Setup

* `pipenv install` at the root of this repository
* Run `schema.sql` on your mySQL database

## Create user

Send a POST request to /user

```json
{
  "name": "some_name",
  "placeOfBirth": "the_place_to_be"
}
```