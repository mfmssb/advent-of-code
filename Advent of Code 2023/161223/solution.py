filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for i, x in enumerate(data):
    print(i, len(x))

# # Problem 1

d = data[0].split("\n")
d = [[x for x in y] for y in d]

energized = [["." for x in y] for y in d]


# ## Intermediate Steps 1

def number_of_energized_cells(matrix):
    """ The matrix contains 0s and 1s indicating a cell is energized or not """
    counter = 0
    for y in matrix:
        for x in y:
            if x not in [".", "#"]:
                raise ValueError("Not valid cell value.", x, y, matrix)
            if x == "#":
                counter += 1
    return counter


def valid_pos(matrix, x, y):
    """ Check if new beam position is valid """
    max_x = len(matrix[0])
    max_y = len(matrix)
    return (0 <= x < max_x) and (0 <= y < max_y)


def make_new_beam(beams, pos, vel):
    new_ind = max(beams.keys()) + 1
    beams[new_ind] = {
        'active': True,
        'pos': pos,
        'vel': vel,
    }
    return beams


class Beam:
    def __init__(self, x, y, vx, vy, visited=set()):
        self.pos = (x, y)
        self.vel = (vx, vy)
        self.active = True
        self.visited = visited  # Set to store visited positions with velocity

    def __str__(self):
        return f"Position: {self.pos}, Velocity: {self.vel}, Active: {self.active}"

    def take_step(self, board):
        next_pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
        self.visited.add((self.pos, self.vel))
        self.pos = next_pos
        if (next_pos, self.vel) in self.visited:
            self.deactivate()
            return
        self.validate_pos(board)

    def validate_pos(self, board):
        if not valid_pos(board, self.pos[0], self.pos[1]):
            self.deactivate()

    def validate_vel(self):
        if self.vel[0] != 0 and self.vel[1] != 0:
            raise ValueError("Beam has diagonal movement")
        if self.vel[0] == 0 and self.vel[1] == 0:
            raise ValueError("Beam has no movement")
        if self.vel[0] > 1 or self.vel[1] > 1:
            raise ValueError("Velocity greater than 1")

    def deactivate(self):
        self.active = False

    def change_dir(self, mirror_type):
        x = self.pos[0]
        y = self.pos[1]

        vx = self.vel[0]
        vy = self.vel[1]

        if mirror_type not in [".", "|", "\\", "/", "-"]:
            raise ValueError("Not valid mirror type:", mirror_type)

        if mirror_type == ".":
            return (0, 0, 0, 0)

        # Split cases
        if (vx == 1 or vx == -1) and (mirror_type == "|"):
            self.deactivate()
            return (0, -1, 0, 1)  # Make new beam with these velocities

        if (vy == 1 or vy == -1) and (mirror_type == "-"):
            self.deactivate()
            return (-1, 0, 1, 0)  # Make new beam with these velocities

        # Rotate direction
        if mirror_type == "\\":
            if vx == 1:
                self.vel = (0, 1)
            if vx == -1:
                self.vel = (0, -1)
            if vy == 1:
                self.vel = (1, 0)
            if vy == -1:
                self.vel = (-1, 0)

        if mirror_type == "/":
            if vx == 1:
                self.vel = (0, -1)
            if vx == -1:
                self.vel = (0, 1)
            if vy == 1:
                self.vel = (-1, 0)
            if vy == -1:
                self.vel = (1, 0)

        return (0, 0, 0, 0)  # Don't make new beam


beams = [Beam(0, 0, 1, 0)]

verbose = True

# %%time
steps = 0
while(beams):
    ## Remove inactive beams
    beams = [beam for beam in beams if beam.active]

    ## Change beam velocity and make new beams when split
    new_beams = []
    for beam in beams:
        x = beam.pos[0]
        y = beam.pos[1]

        energized[y][x] = "#"  # Update energized matrix
        
        mirror_type = d[y][x]
        (new_beam1_vx, new_beam1_vy, new_beam2_vx, new_beam2_vy) = beam.change_dir(mirror_type)

        if (new_beam1_vx, new_beam1_vy, new_beam2_vx, new_beam2_vy) != (0, 0, 0, 0):
            new_beams.append(Beam(x, y, new_beam1_vx, new_beam1_vy, beam.visited))
            new_beams.append(Beam(x, y, new_beam2_vx, new_beam2_vy, beam.visited))

    beams.extend(new_beams)

    ## Update beam position
    for beam in beams:
        beam.take_step(d)
        beam.validate_vel()  # check if velocity is as expected

    steps += 1
    
    if verbose:
        for beam in beams:
            print(beam)

        for x in d:
            print(("").join(x))
        print()
        for x in energized:
            print(("").join(x))
        print(number_of_energized_cells(energized))

print(steps)

# ## Solution 1

# Tried: 6271

print(number_of_energized_cells(energized))

# # Problem 2

# ## Intermediate Steps 2



# ## Solution 2


