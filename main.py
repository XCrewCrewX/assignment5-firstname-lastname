from machine import Pin # type: ignore
import time

import config
from motors import Car
from server import CommandServer
from hotspot import start_hotspot as connect_wifi