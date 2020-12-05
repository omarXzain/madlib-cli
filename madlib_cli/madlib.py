import re

def welcome():
  print(f"""
Hello Sir and welcome to the Madlib Game ....
In my game you'll be asked a few questions
Answer them or suffer in my infinit loop >:)
let's go .....
""")
    

def read():
    with open('./assets/template.txt') as f:
        contents = f.read()
    return contents


def parse(content):
  contentArr = []
  data = re.findall(r'\{.*?\}', content)
  for x in data:
    dataCopy = x.strip('{ }')
    contentArr.append(dataCopy)
  return contentArr



def merge(content, words):  
  return (re.sub(r' {[^}]*}',' {}', content)).format(*words)

    

def write(content):
  with open('assets/your_answer.txt', 'w') as f2:
    f2.write(content)
  print(' ')
  print("*****************************************************")
  print("also you can find your answer inside your_answer.txt")
  print("*****************************************************")
  print(' ')
  print(content)


if __name__ == "__main__":
    welcome()
    template = read()
    parsedContent = parse(template)
    inputsArr = []
    for x in range(len(parsedContent)):
      inputsArr.append(input('Enter {} '.format(parsedContent[x])))
    merging = merge(template, inputsArr)
    write(merging)