input = "()(()())())"

def valid_parenthesis(input):
  if len(input) % 2 != 0:
    return False
  
  tracker = 0
  
  for e in input:
    if tracker < 0:
      return False
    
    match e:
      case "(":
        tracker += 1
      case ")":
        tracker -= 1
  return True

print(valid_parenthesis(input))