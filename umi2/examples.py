# Module examples

from constants import (
  CAT_KEY,
  INST_KEY,
  SOL_KEY,
  CAT_EASY,
  CAT_MEDIUM,
  CAT_HARD,
  CAT_VERY_HARD,
)

examples = [
  {
    CAT_KEY: CAT_EASY,
    INST_KEY: [
      [5, 3, 0, 0, 7, 0, 0, 0, 0],
      [6, 0, 0, 1, 9, 5, 0, 0, 0],
      [0, 9, 8, 0, 0, 0, 0, 6, 0],
      [8, 0, 0, 0, 6, 0, 0, 0, 3],
      [4, 0, 0, 8, 0, 3, 0, 0, 1],
      [7, 0, 0, 0, 2, 0, 0, 0, 6],
      [0, 6, 0, 0, 0, 0, 2, 8, 0],
      [0, 0, 0, 4, 1, 9, 0, 0, 5],
      [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ],
    SOL_KEY: [
      [5, 3, 4, 6, 7, 8, 9, 1, 2],
      [6, 7, 2, 1, 9, 5, 3, 4, 8],
      [1, 9, 8, 3, 4, 2, 5, 6, 7],
      [8, 5, 9, 7, 6, 1, 4, 2, 3],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 6, 1, 5, 3, 7, 2, 8, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ],
  },
  {
    CAT_KEY: CAT_EASY,
    INST_KEY: [
      [0, 0, 0, 2, 6, 0, 7, 0, 1],
      [6, 8, 0, 0, 7, 0, 0, 9, 0],
      [1, 9, 0, 0, 0, 4, 5, 0, 0],
      [8, 2, 0, 1, 0, 0, 0, 4, 0],
      [0, 0, 4, 6, 0, 2, 9, 0, 0],
      [0, 5, 0, 0, 0, 3, 0, 2, 8],
      [0, 0, 9, 3, 0, 0, 0, 7, 4],
      [0, 4, 0, 0, 5, 0, 0, 3, 6],
      [7, 0, 3, 0, 1, 8, 0, 0, 0],
    ],
    SOL_KEY: [
      [4, 3, 5, 2, 6, 9, 7, 8, 1],
      [6, 8, 2, 5, 7, 1, 4, 9, 3],
      [1, 9, 7, 8, 3, 4, 5, 6, 2],
      [8, 2, 6, 1, 9, 5, 3, 4, 7],
      [3, 7, 4, 6, 8, 2, 9, 1, 5],
      [9, 5, 1, 7, 4, 3, 6, 2, 8],
      [5, 1, 9, 3, 2, 6, 8, 7, 4],
      [2, 4, 8, 9, 5, 7, 1, 3, 6],
      [7, 6, 3, 4, 1, 8, 2, 5, 9],
    ],
  },
  {
    CAT_KEY: CAT_EASY,
    INST_KEY: [
      [1, 0, 0, 4, 8, 9, 0, 0, 6],
      [7, 3, 0, 0, 0, 0, 0, 4, 0],
      [0, 0, 0, 0, 0, 1, 2, 9, 5],
      [0, 0, 7, 1, 2, 0, 6, 0, 0],
      [5, 0, 0, 7, 0, 3, 0, 0, 8],
      [0, 0, 6, 0, 9, 5, 7, 0, 0],
      [9, 1, 4, 6, 0, 0, 0, 0, 0],
      [0, 2, 0, 0, 0, 0, 0, 3, 7],
      [8, 0, 0, 5, 1, 2, 0, 0, 4],
    ],
    SOL_KEY: [
      [1, 5, 2, 4, 8, 9, 3, 7, 6],
      [7, 3, 9, 2, 5, 6, 8, 4, 1],
      [4, 6, 8, 3, 7, 1, 2, 9, 5],
      [3, 8, 7, 1, 2, 4, 6, 5, 9],
      [5, 9, 1, 7, 6, 3, 4, 2, 8],
      [2, 4, 6, 8, 9, 5, 7, 1, 3],
      [9, 1, 4, 6, 3, 7, 5, 8, 2],
      [6, 2, 5, 9, 4, 8, 1, 3, 7],
      [8, 7, 3, 5, 1, 2, 9, 6, 4],
    ],
  },
  {
    CAT_KEY: CAT_MEDIUM,
    INST_KEY: [
      [0, 2, 0, 6, 0, 8, 0, 0, 0],
      [5, 8, 0, 0, 0, 9, 7, 0, 0],
      [0, 0, 0, 0, 4, 0, 0, 0, 0],
      [3, 7, 0, 0, 0, 0, 5, 0, 0],
      [6, 0, 0, 0, 0, 0, 0, 0, 4],
      [0, 0, 8, 0, 0, 0, 0, 1, 3],
      [0, 0, 0, 0, 2, 0, 0, 0, 0],
      [0, 0, 9, 8, 0, 0, 0, 3, 6],
      [0, 0, 0, 3, 0, 6, 0, 9, 0],
    ],
    SOL_KEY: [
      [1, 2, 3, 6, 7, 8, 9, 4, 5],
      [5, 8, 4, 2, 3, 9, 7, 6, 1],
      [9, 6, 7, 1, 4, 5, 3, 2, 8],
      [3, 7, 2, 4, 6, 1, 5, 8, 9],
      [6, 9, 1, 5, 8, 3, 2, 7, 4],
      [4, 5, 8, 7, 9, 2, 6, 1, 3],
      [8, 3, 6, 9, 2, 4, 1, 5, 7],
      [2, 1, 9, 8, 5, 7, 4, 3, 6],
      [7, 4, 5, 3, 1, 6, 8, 9, 2],
    ],
  },
  {
    CAT_KEY: CAT_HARD,
    INST_KEY: [
      [0, 0, 0, 6, 0, 0, 4, 0, 0],
      [7, 0, 0, 0, 0, 3, 6, 0, 0],
      [0, 0, 0, 0, 9, 1, 0, 8, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 5, 0, 1, 8, 0, 0, 0, 3],
      [0, 0, 0, 3, 0, 6, 0, 4, 5],
      [0, 4, 0, 2, 0, 0, 0, 6, 0],
      [9, 0, 3, 0, 0, 0, 0, 0, 0],
      [0, 2, 0, 0, 0, 0, 1, 0, 0],
    ],
    SOL_KEY: [
      [5, 8, 1, 6, 7, 2, 4, 3, 9],
      [7, 9, 2, 8, 4, 3, 6, 5, 1],
      [3, 6, 4, 5, 9, 1, 7, 8, 2],
      [4, 3, 8, 9, 5, 7, 2, 1, 6],
      [2, 5, 6, 1, 8, 4, 9, 7, 3],
      [1, 7, 9, 3, 2, 6, 8, 4, 5],
      [8, 4, 5, 2, 1, 9, 3, 6, 7],
      [9, 1, 3, 7, 6, 8, 5, 2, 4],
      [6, 2, 7, 4, 3, 5, 1, 9, 8],
    ],
  },
  {
    CAT_KEY: CAT_HARD,
    INST_KEY: [
      [2, 0, 0, 3, 0, 0, 0, 0, 0],
      [8, 0, 4, 0, 6, 2, 0, 0, 3],
      [0, 1, 3, 8, 0, 0, 2, 0, 0],
      [0, 0, 0, 0, 2, 0, 3, 9, 0],
      [5, 0, 7, 0, 0, 0, 6, 2, 1],
      [0, 3, 2, 0, 0, 6, 0, 0, 0],
      [0, 2, 0, 0, 0, 9, 1, 4, 0],
      [6, 0, 1, 2, 5, 0, 8, 0, 9],
      [0, 0, 0, 0, 0, 1, 0, 0, 2],
    ],
    SOL_KEY: [
      [2, 7, 6, 3, 1, 4, 9, 5, 8],
      [8, 5, 4, 9, 6, 2, 7, 1, 3],
      [9, 1, 3, 8, 7, 5, 2, 6, 4],
      [4, 6, 8, 1, 2, 7, 3, 9, 5],
      [5, 9, 7, 4, 3, 8, 6, 2, 1],
      [1, 3, 2, 5, 9, 6, 4, 8, 7],
      [3, 2, 5, 7, 8, 9, 1, 4, 6],
      [6, 4, 1, 2, 5, 3, 8, 7, 9],
      [7, 8, 9, 6, 4, 1, 5, 3, 2],
    ],
  },
  {
    CAT_KEY: CAT_HARD,
    INST_KEY: [
      [0, 0, 0, 4, 0, 0, 1, 0, 0],
      [6, 0, 0, 0, 0, 0, 0, 0, 0],
      [2, 5, 0, 0, 7, 0, 0, 4, 0],
      [0, 0, 9, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 0, 0, 8],
      [4, 7, 0, 0, 2, 0, 0, 1, 0],
      [0, 0, 1, 0, 9, 0, 0, 0, 0],
      [5, 9, 0, 0, 0, 2, 3, 0, 0],
      [0, 0, 6, 0, 0, 0, 0, 5, 0],
    ],
    SOL_KEY: [
      [9, 8, 7, 4, 5, 6, 1, 3, 2],
      [6, 1, 4, 2, 3, 8, 5, 7, 9],
      [2, 5, 3, 9, 7, 1, 8, 4, 6],
      [8, 3, 9, 1, 6, 7, 4, 2, 5],
      [1, 6, 2, 5, 4, 3, 7, 9, 8],
      [4, 7, 5, 8, 2, 9, 6, 1, 3],
      [3, 4, 1, 6, 9, 5, 2, 8, 7],
      [5, 9, 8, 7, 1, 2, 3, 6, 4],
      [7, 2, 6, 3, 8, 4, 9, 5, 1],
    ],
  },
  {
    CAT_KEY: CAT_VERY_HARD,
    INST_KEY: [
      [0, 2, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 6, 0, 0, 0, 0, 3],
      [0, 7, 4, 0, 8, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 0, 0, 2],
      [0, 8, 0, 0, 4, 0, 0, 1, 0],
      [6, 0, 0, 5, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 7, 8, 0],
      [5, 0, 0, 0, 0, 9, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 4, 0],
    ],
    SOL_KEY: [
      [1, 2, 6, 4, 3, 7, 9, 5, 8],
      [8, 9, 5, 6, 2, 1, 4, 7, 3],
      [3, 7, 4, 9, 8, 5, 1, 2, 6],
      [4, 5, 7, 1, 9, 3, 8, 6, 2],
      [9, 8, 3, 2, 4, 6, 5, 1, 7],
      [6, 1, 2, 5, 7, 8, 3, 9, 4],
      [2, 6, 9, 3, 1, 4, 7, 8, 5],
      [5, 4, 8, 7, 6, 9, 2, 3, 1],
      [7, 3, 1, 8, 5, 2, 6, 4, 9],
    ],
  },
]
