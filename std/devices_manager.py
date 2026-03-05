from dataclasses import dataclass

@dataclass
class RdpItem:

    name:str
    host:str
    user:str
    password:str
    multimonitor:bool=False
    ask_monitors:bool=False
    printers:bool=False