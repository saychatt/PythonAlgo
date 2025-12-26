
# https://w.amazon.com/bin/view/Users/conorapm/WorkflowLimitsQuestion/
class WorkflowLimiter:
    def __init__(self, limits):
        self.limits = {
            'Fleet': {},
            'Region': {},
            'ServerType': {}
        }
        self.current_workflows = []

        for limit in limits:
            self.limits[limit['type']][limit['value']] = limit['limit']

    def can_execute_workflow(self, workflow):
        # Check limits for Fleet, Region, and ServerType
        for limit_type in ['Fleet', 'Region', 'ServerType']:
            current_count = sum(1 for w in self.current_workflows
                                if getattr(w, limit_type.lower()) == workflow[limit_type.lower()])

            if current_count >= self.limits[limit_type].get(workflow[limit_type.lower()], float('inf')):
                return False

        return True

    def add_workflow(self, workflow):
        if self.can_execute_workflow(workflow):
            self.current_workflows.append(workflow)
            return True
        return False

    def remove_workflow(self, workflow_id):
        self.current_workflows = [w for w in self.current_workflows if w['id'] != workflow_id]
