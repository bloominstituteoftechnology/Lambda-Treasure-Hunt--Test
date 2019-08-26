from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('take', api.take),
    url('drop', api.drop),
    url('status', api.status),
    url('sell', api.sell),
    url('wear', api.wear),
    url('remove', api.remove),
    url('examine', api.examine),
    url('change_name', api.change_name),
    url('pray', api.pray),
    url('fly', api.fly),
    url('dash', api.dash),
    url('player_state', api.player_state),
]
