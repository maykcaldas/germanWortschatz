import googletrans
import google_trans_new

class Group:
  def __init__(self,c):
    self.name=c
    self.entries=[]
  
  def getEntries(self):
    return self.entries

  def addEntry(self, entry):
    self.entries.append(entry)

def createClass(c, classes):
  if c not in classes.keys():
    classes[c]=Group(c)

translator=googletrans.Translator()
translator=google_trans_new.google_translator()

k=translator.translate("carro")
print(k)

file = open("voc.dat",'r')
classes={}

for line in file:
  inp = line[:-1].strip().split('·')
  if len(inp) == 1:
    if inp[0] not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ü','ä','ö']:
      createClass("Idiom",classes)
      inp.append('Idiom')
      classes["Idiom"].addEntry(inp)
  elif len(inp) == 2:
    c=inp[-1].split()[-1]
    createClass(c,classes)
    classes[c].addEntry(inp)
  else:
    print("What?")



for k in classes:
  out=open(f'{k}.csv','w')
  for line in classes[k].getEntries():
    word=line[0].strip()
    trs=translator.translate(f'{word}', lang_src='de', lang_tgt='pt')
    # print(trs)
    if line[1].split()[-1] != 'Noun':
      out.write(f'{word},{trs}\n')
    else:
      if line[1].strip().split()[0][0]=="M": art='der'
      elif line[1].strip().split()[0][0]=="F": art='die'
      elif line[1].strip().split()[0][0]=="N": art='das'
      else: 
        art="WHAT"
        print(line)
        print("MERDA")
      out.write(f'{word},{art},{trs}\n')
  out.close
