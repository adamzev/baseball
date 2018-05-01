class Bases(object):
    def __init__(self):
        self.first = None
        self.second = None
        self.third = None

    def __str__(self):
        result = ""
        for base in (self.first, self.second, self.third):
            if base:
                result += "X"
            else:
                result += "-"
        return result
    def are_loaded(self):
        return self.first and self.second and self.third

    def are_empty(self):
        return not(self.first or self.second or self.third)

    def players_in_scoring_pos(self):
        return self.second or self.third

    def forced_advance(self, new_runner):
        runs = 0
        if not self.first:
            self.first = new_runner
        elif self.first and not self.second:
            self.second = self.first
            self.first = new_runner
        elif self.first and self.second and not self.third:
            self.third = self.second
            self.second = self.first
            self.first = new_runner
        elif self.are_loaded():
            self.third = self.second
            self.second = self.first
            self.first = new_runner
            runs = 1
        return runs

    def advance_runners_keep_spacing(self, bases_advanced, new_runner):
        home = new_runner
        runs = 0
        for i in range(bases_advanced):
            if self.third:
                runs += 1
            self.third = self.second
            self.second = self.first
            self.first = home
            home = None
        return runs

    def clear_bases(self):
        self.first = None
        self.second = None
        self.third = None
