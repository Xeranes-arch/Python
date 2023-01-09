from Test import yes


def test_yes():
    assert yes()


class Car(Vehicle):
    """weee"""

    def __init__(self, model, color):
        """init"""
        pass

    def __repr__(self) -> str:
        return super().__repr__()

    @property
    def model(self):
        return self.__model
