import re
from collections import defaultdict

class Claim:
    claim_re = re.compile('\A#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)\Z')

    def __init__(self, claim_str):
        groups = Claim.claim_re.match(claim_str).groups()
        assert(len(groups) == 5)

        self.id = int(groups[0])
        self.left = int(groups[1])
        self.top = int(groups[2])
        self.wide = int(groups[3])
        self.tall = int(groups[4])

    def __str__(self):
        return 'id: {}, left: {}, top: {}, wide: {}, tall: {}'.format(
            self.id, self.left, self.top, self.wide, self.tall
        )
    
class Fabric:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._canvas = [0] * (width * height)
        self._claims = defaultdict(list)
    
    """
    adds all cells occupied by the claim to this fabric's canvas
    """
    def add_claim(self, claim):
        for cell in self._get_claim_cells(claim):
            self._claims[claim.id].append(cell)
            self._canvas[cell] += 1

    """
    returns the number of cells that are shared between two or more claims
    """
    def get_num_overlapped_cells(self):
        return sum([1 for x in self._canvas if x > 1])

    """
    finds a claim that has no overlapping cell with any other claims
    """
    def find_disjoint_claim(self):
        for claim_id, cells in self._claims.items():
            for cell in cells:
                if self._canvas[cell] != 1:
                    break
            else:
                return claim_id
        return -1

    def clear(self):
        self._canvas = [0] * (self.width * self.height)
        self._claims = defaultdict(list)

    """
    computes all cells the claim occupies
    """
    def _get_claim_cells(self, claim):
        for i in range(claim.tall):
            curr_height = self.height * (claim.top + i)
            row_start = curr_height + claim.left
            row_end = row_start + claim.wide
            for cell in range(row_start, row_end):
                assert(cell <= self.height * self.width - 1)
                yield cell

with open('input.txt') as f:
    claims_input = f.read().splitlines()

FABRIC_SIZE = 1000
fabric = Fabric(FABRIC_SIZE, FABRIC_SIZE)
for claim_str in claims_input:
    claim = Claim(claim_str)
    fabric.add_claim(claim)

print('overlapping cells:', fabric.get_num_overlapped_cells())
print('disjoint claim id:', fabric.find_disjoint_claim())