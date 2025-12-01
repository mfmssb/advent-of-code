filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for i, x in enumerate(data):
    print(i, len(x))

# # Problem 1

d = data[1].split("\n")
d = [[x for x in y] for y in d]


# ## Intermediate Steps 1

def number_of_energized_cells(matrix):
    """ The matrix contains "." and "#" indicating a cell is energized or not """
    counter = 0
    for y in matrix:
        for x in y:
            if x not in [".", "#"]:
                raise ValueError("Not valid cell value.", x, y, matrix)
            if x == "#":
                counter += 1
    return counter


def valid_pos(matrix, x, y):
    """ Check if beam position is valid in matrix"""
    max_x = len(matrix[0])
    max_y = len(matrix)
    return (0 <= x < max_x) and (0 <= y < max_y)


class Beam:
    def __init__(self, x, y, vx, vy):
        self.pos = (x, y)
        self.vel = (vx, vy)
        self.active = True

    def __str__(self):
        return f"Position: {self.pos}, Velocity: {self.vel}, Active: {self.active}"

    def take_step(self, board):
        self.pos = (self.pos[0] + self.vel[0],
                    self.pos[1] + self.vel[1])

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
        if mirror_type == ".":
            return (0, 0, 0, 0)
        
        x = self.pos[0]
        y = self.pos[1]

        vx = self.vel[0]
        vy = self.vel[1]

        if mirror_type not in [".", "|", "\\", "/", "-"]:
            raise ValueError("Not valid mirror type:", mirror_type)

        

        # Split cases
        if (vx == 1 or vx == -1) and (mirror_type == "|"):
            self.deactivate()
            return (0, -1, 0, 1)  # Make new beams with these velocities

        if (vy == 1 or vy == -1) and (mirror_type == "-"):
            self.deactivate()
            return (-1, 0, 1, 0)  # Make new beams with these velocities

        # Rotate direction
        if mirror_type == "\\":
            if vx == 1: self.vel = (0, 1)
            if vx == -1: self.vel = (0, -1)
            if vy == 1: self.vel = (1, 0)
            if vy == -1: self.vel = (-1, 0)

        if mirror_type == "/":
            if vx == 1: self.vel = (0, -1)
            if vx == -1: self.vel = (0, 1)
            if vy == 1: self.vel = (-1, 0)
            if vy == -1: self.vel = (1, 0)

        return (0, 0, 0, 0)  # Don't make new beams


def run_loop(d, _x, _y, _vx, _vy, threshold, verbose = False):  
    beams = [Beam(_x, _y, _vx, _vy)]
    
    energized = [["." for x in y] for y in d]
    
    steps_since_new_energized_cell = 0
    while(beams and steps_since_new_energized_cell <= threshold):
        
        state_before = number_of_energized_cells(energized)
        
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
                new_beams.append(Beam(x, y, new_beam1_vx, new_beam1_vy))
                new_beams.append(Beam(x, y, new_beam2_vx, new_beam2_vy))

        beams.extend(new_beams)

        ## Update beam positions
        for beam in beams:
            beam.take_step(d)
            beam.validate_vel()  # check if velocity is as expected

        state_after = number_of_energized_cells(energized)
        if state_after > state_before:
            steps_since_new_energized_cell = 0
        else:
            steps_since_new_energized_cell += 1
            
        if verbose:
            for beam in beams:
                print(beam)

            for x in d:
                print(("").join(x))
            print()
            for x in energized:
                print(("").join(x))
            print(number_of_energized_cells(energized))
            
    return state_after


# %%time
ans1 = run_loop(d, _x=0, _y=0, _vx=1, _vy=0, threshold=2)

# ## Solution 1

print(ans1)

# # Problem 2

# ## Intermediate Steps 2

# +
max_x = len(d[0]) - 1
max_y = len(d) - 1

starting_positions = []

# +
# Top edge (moving downward)
for x in range(max_x):
    starting_positions.append((x, 0, 0, 1))

# Bottom edge (moving upward)
for x in range(max_x):
    starting_positions.append((x, max_y, 0, -1))

# Left edge (moving rightward)
for y in range(max_y):
    starting_positions.append((0, y, 1, 0))

# Right edge (moving leftward)
for y in range(max_y):
    starting_positions.append((max_x, y, -1, 0))

# Special cases for corners if needed
# Top-left corner
starting_positions.append((0, 0, 1, 0))  # Rightward
starting_positions.append((0, 0, 0, 1))  # Downward

# Top-right corner
starting_positions.append((max_x, 0, -1, 0))  # Leftward
starting_positions.append((max_x, 0, 0, 1))   # Downward

# Bottom-left corner
starting_positions.append((0, max_y, 1, 0))   # Rightward
starting_positions.append((0, max_y, 0, -1))  # Upward

# Bottom-right corner
starting_positions.append((max_x, max_y, -1, 0))  # Leftward
starting_positions.append((max_x, max_y, 0, -1))  # Upward
# -

print(len(starting_positions))

# %%time
energized_scores = []
_max = 0
for (x, y, vx, vy) in starting_positions:
    score = run_loop(d, _x=x, _y=y, _vx=vx, _vy=vy, threshold=2)
    if score > _max:
        _max = score
        print(x, y, vx, vy, "\t", score, _max)
    energized_scores.append(score)

# ## Solution 2

max(energized_scores)
