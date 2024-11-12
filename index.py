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

def obj_to_list(obj):
  # method 1: 
  # beta = []
  # for key, value in obj.items():
  #   beta.append([key, value])
  # return beta

  # method 2:
  beta = [[key, value] for key, value in obj.items()]
  return beta

print(obj_to_list(alpha))