class Workflow:
    def __init__(self,
                 fleet: str,
                 region: str,
                 server_type: str,
                 workflow_id: str):
        self.fleet = fleet
        self.region = region
        self.server_type = server_type
        self.id = workflow_id