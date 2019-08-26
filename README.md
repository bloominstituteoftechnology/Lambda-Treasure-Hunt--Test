# Lambda Treasure Hunt Server

Student facing test server for Lambda Treasure Hunt.


## 1. Deploy server
* `git clone https://github.com/br80/Lambda-Treasure-Hunt--Server/`
* `pipenv install`
* `pipenv shell`
* `./manage.py migrate`
* `./manage.py runserver`

## 2. Migrate world
* `./manage.py shell`
* copy/paste `util/create_world.py` into Python shell

## 3. Create a user
* `curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password1":"testpassword", "password2":"testpassword"}' localhost:8000/api/registration/`
```
# Response
{"key":"1d52b631a2325f5816d094e7ccf82dbfe4416544"}
```

## 4. Move around

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

## 5. Add player to a group (custom cooldown)
* `./manage.py shell`
* `from adventure.models import Player, Room, Item, Group`
* `p = Player.objects.get(name="testuser")`
* `g = Group.objects.get(name="default")`
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



