from src.map.type import Type


class Map:

    def __init__(self):
        self.grid = []
        self.cheese = []
        self.robot = []
        self.wall = []

    def load(self, rows):
        for i, row in enumerate(rows):
            columns = list(map(lambda obj: Type.find(obj), row.split()))

            self.grid.append([])

            for j, column in enumerate(columns):
                if column == Type.PAREDE:
                    self.wall.append((i, j))

                if column == Type.ROBO:
                    self.robot.append((i, j))

                if column == Type.QUEIJO:
                    self.cheese.append((i, j))

                self.grid[i].append(column)

    def find(self, position, target: Type, trails):
        # Fazendo validações de segurança

        if position in trails:
            return None

        if position[0] < 0 or position[0] >= len(self.grid):
            return None

        if position[1] < 0 or position[1] >= len(self.grid[0]):
            return None

        # Verificando colisões com objetos

        if self.grid[position[0]][position[1]] == target:
            return [position]

        if self.grid[position[0]][position[1]] == Type.PAREDE:
            return None

        # Calculando caminhos perpendiculares

        moves = [
            (position[0], position[1] + 1),
            (position[0], position[1] - 1),
            (position[0] + 1, position[1]),
            (position[0] - 1, position[1])
        ]

        # Verificando caminhos perpendiculares

        route = None
        steps = None

        for move in moves:
            result = self.find(move, target, trails + [position])

            if result is not None:
                if steps is None or len(result) < steps:
                    route = result
                    steps = len(result)

        return [position] + route if route is not None else None
