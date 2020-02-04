class listener():
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.last_log = None

    def _log_message(self, message):
        self.last_log = message

    def _end_keyword(self, name, attrs):
        if attrs['status'] == 'FAIL':
            print("\n******\n", self.last_log['message'])