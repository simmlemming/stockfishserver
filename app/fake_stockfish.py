class Stockfish:

    def __init__(self, path, parameters=None):
        pass

    def get_board_visual(self):
        return """
+---+---+---+---+---+---+---+---+
| r | n | b | q | k | b | n | r | 8
+---+---+---+---+---+---+---+---+
| p | p | p | p |   | p | p | p | 7
+---+---+---+---+---+---+---+---+
|   |   |   |   | p |   |   |   | 6
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 5
+---+---+---+---+---+---+---+---+
|   |   |   | P |   |   |   |   | 4
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   | 3
+---+---+---+---+---+---+---+---+
| P | P | P |   | P | P | P | P | 2
+---+---+---+---+---+---+---+---+
| R | N | B | Q | K | B | N | R | 1
+---+---+---+---+---+---+---+---+
  a   b   c   d   e   f   g   h
        """

    def get_top_moves(self, number):
        return f"Get top moves, number = {number}."

    def get_top_moves_2(self, number1, number2):
        return f"Get top moves, number1 = {number1}, number2 = {number2}."

    def set_position(self, moves):
        return f"Moves were {moves}."

    def get_parameters(self):
        return "{}"
