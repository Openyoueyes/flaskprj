from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Game_glo(metaclass=SingletonMeta):
    def __init__(self):
        self.game_pole = [[Cell("стена", "Ты уперся в стену дальше идти нельзя"),
                           Cell("Балкон", "Ты успешно добрался до балкона, поздравляю! Игра закончена!"),
                           Cell("стена", "Ты уперся в стену дальше идти нельзя")],
                          [Cell("Спальня", "Ты в спальне, отдохни и продолжай путь!"), Cell("Хол", "Ты в холе!"),
                           Cell("Кухня", "Ты на кухне!")],
                          [Cell("Подземелье", "Ты в подземелье!"), Cell("Коридор", "Ты в коридоре!"),
                           Cell("Оружейная", "Ты в оружейной!")]]
        self.start_i = 2
        self.start_j = 0
        self.current = [self.start_i, self.start_j]

    def __getitem__(self, item):
        i, j = item
        return self.game_pole[i][j].data

    def check_step(self, dir, step):
        phrase = "Ты не можешь двигаться дальше!"
        maximum = 2
        i = self.current[0]
        j = self.current[1]
        if dir == 1:
            res = j + step
            if res > 2:
                res = step - (res - maximum)
                return [phrase, res]
            else:
                return [step]
        elif dir == 3:
            res = j - step
            if res < 0:
                res = step + res
                return [phrase, res]
            else:
                return [step]
        elif dir == 2:
            res = i + step
            if res > 2:
                res = step - (res - maximum)
                return [phrase, res]
            else:
                return [step]
        elif dir == 0:
            res = i - step
            if res <= 0 and (j == 0 or j == 2):
                res = step + res - 1
                return ["Ты уперся стену! Найди другой путь!", res]
            elif res < 0:
                res = step + res
                return [phrase, res]
            else:
                return [step]

    def move(self, direction, step):
        results = self.check_step(direction, step)
        steps = results[1] if len(results) == 2 else results[0]
        phrases = []
        i = self.current[0]
        j = self.current[1]
        if direction == 0:  # check only j
            while steps:
                self.current[0] -= 1
                phrases.append(self.game_pole[self.current[0]][j].phrase)
                steps -= 1
            return phrases + results[:1] if len(results) == 2 else phrases
        elif direction == 1:  # check only j
            while steps:
                self.current[1] += 1
                phrases.append(self.game_pole[i][self.current[1]].phrase)
                steps -= 1
            return phrases + results[:1] if len(results) == 2 else phrases

        elif direction == 2:  # check only j
            while steps:
                self.current[0] += 1
                phrases.append(self.game_pole[self.current[0]][j].phrase)
                steps -= 1
            return phrases + results[:1] if len(results) == 2 else phrases

        elif direction == 3:  # check only j
            while steps:
                self.current[1] -= 1
                phrases.append(self.game_pole[i][self.current[1]].phrase)
                steps -= 1
            return phrases + results[:1] if len(results) == 2 else phrases

    def reboot(self):
        self.current = [2, 0]

    def check_end_game(self):
        if self.current == [0, 1]:
            return "Ты успешно добрался до балкона поздравляю!Нажми на главную, чтобы перезагрузить игру!"


class Cell:
    def __init__(self, data=None, phrase=None):
        self.data = data
        self.phrase = phrase

    def __repr__(self):
        return self.data


a = [1, 2, 3]
print(a[:1])
