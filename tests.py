import unittest
from index import obj_to_list

class testAlgo(unittest.TestCase):
  def test_obj_to_list_base(self):
    [ key, value ] = ["k1", "v1"]
    alpha = { key: value }

    result = obj_to_list(alpha)
    expected = [[alpha[0][0], value[0][0]]]
    self.assertEqual(result, expected )

  def test_obj_to_list_ten(self):
    alpha = { 
      "k1": "v1",
      "k2": "v2",
      "k3": "v3",
      "k4": "v4",
      "k5": "v5",
      "k6": "v6",
      "k7": "v7",
      "k8": "v8",
      "k9": "v9",
      "k10": "v10",
       }

    result = obj_to_list(alpha),
    expected = [
      ["k1","v1"],
      ["k2", "v2"],
      ["k3", "v3"],
      ["k4", "v4"],
      ["k5", "v5"],
      ["k6", "v6"],
      ["k7", "v7"],
      ["k8", "v8"],
      ["k9", "v9"],
      ["k10", "v10"]
      ]
    self.assertEqual(result, expected )

if __name__ == '__main__':
    unittest.main()