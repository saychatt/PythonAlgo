from typing import List, Dict, Literal

class Limit:
    def __init__(self, 
                 type: Literal['Fleet', 'Region', 'ServerType'], 
                 value: str, 
                 limit: int):
        self.type = type
        self.value = value
        self.limit = limit