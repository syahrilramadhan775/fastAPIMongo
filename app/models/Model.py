from databases.DatabaseSQL import SessionDepedency

class modelSession(object):
    def __init__(self, session) -> None:
        self.session = session

    def model_session(self):
        return self.session

modelSessions = modelSession(SessionDepedency).model_session()