from pieces.piece import piece


class nullpiece(piece):
    alliance = None
    def __init__(self):
        pass

    def tostring(self):
        return "-"

