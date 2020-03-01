# Lambda Treasure Hunt Server

Student facing test server for Lambda Treasure Hunt.


## 1. Deploy server
* `git clone https://github.com/br80/Lambda-Treasure-Hunt--Server/`
* `pipenv shell`
    * if you're on a mac with postgres installed via homebrew (while inside the pipenv shell):
        * `export LDFLAGS="-L/usr/local/opt/openssl/lib" export CPPFLAGS="-I/usr/local/opt/openssl/include"`
* `pipenv install`
* configure postgres with a new db
* create your `.env` file:
    * 
    ```
    SECRET_KEY="randomkey"
    DEBUG=True
    ALLOWED_HOSTS=['localhost','127.0.0.1']
    DATABASE_URL=postgres://USER:PASS@localhost/DBNAME

    PUSHER_APP_ID=xxx
    PUSHER_KEY="xxx"
    PUSHER_SECRET="xxx"
    PUSHER_CLUSTER="us2"
    ```
* `./manage.py makemigrations`
* `./manage.py migrate`
* `./manage.py shell < util/create_world.py`
* `./manage.py runserver`


## 2. Create a user
* `curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password1":"testpassword", "password2":"testpassword"}' localhost:8000/api/registration/`
```
# Response
{"key":"1d52b631a2325f5816d094e7ccf82dbfe4416544"}
```

## 3. Move around

* `curl -X GET -H 'Authorization: Token 1d52b631a2325f5816d094e7ccf82dbfe4416544' localhost:8000/api/adv/init/`
```
# Response
{"room_id": 0,
"title": "A brightly lit room",
"description": "You are standing in the center of a brightly lit room. You notice a shop to the west and exits to the north, south and east.",
"coordinates": "(60,60)",
"elevation": 0,
"terrain": "NORMAL",
"players": [],
"items": ["boots", "jacket"],
"exits": ["n", "s", "e", "w"],
"cooldown": 1.0,
"errors": [],
"messages": []}
```

* `curl -X POST -H 'Authorization: Token 1d52b631a2325f5816d094e7ccf82dbfe4416544' -H "Content-Type: application/json" -d '{"direction":"w"}' localhost:8000/api/adv/move/`
```
# Response
{"room_id": 1,
"title": "Shop",
"description": "You are standing in a small shop. A sign behind the mechanical shopkeeper says 'WILL PAY FOR TREASURE'.",
"coordinates": "(59,60)",
"elevation": 0,
"terrain": "NORMAL",
"players": [],
"items": ["tiny treasure"],
"exits": ["e"],
"cooldown": 60.0,
"errors": [],
"messages": ["You have walked west."]}
```

## 4. Add player to a group (custom cooldown)
* `./manage.py shell`
* `from adventure.models import Player, Room, Item, Group`
* `p = Player.objects.get(name="testuser")`
* `g = Group.objects.get(name="test group")`
    * if you need to create a group:
        1. `g = Group(name="test group")`
        1. `g.save()`
* `p.group = g`
* `p.save()`
* `exit()`
* `curl -X POST -H 'Authorization: Token 1d52b631a2325f5816d094e7ccf82dbfe4416544' -H "Content-Type: application/json" -d '{"direction":"e"}' localhost:8000/api/adv/move/`
```
# Response
{"room_id": 0,
"title": "A brightly lit room",
"description": "You are standing in the center of a brightly lit room. You notice a shop to the west and exits to the north, south and east.",
"coordinates": "(60,60)",
"elevation": 0,
"terrain": "NORMAL",
"players": [],
"items": ["boots", "jacket"],
"exits": ["n", "s", "e", "w"],
"cooldown": 10.0,
"errors": [],
"messages": ["You have walked east."]}
```



