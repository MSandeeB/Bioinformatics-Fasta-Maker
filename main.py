import random
import io #import packages
def dnagenerator():
  nucleotideslist = list("AGCT") #makes individual letters into seperate strings
  subrepeata = ''
  randomnum1 = random.randint(1,150) #randomly chooses a number from 1-150
  for i in range(randomnum1):
    subrepeata += random.choice(nucleotideslist) #adds a random sequence of nucleotides amounting to random1 to subrepeata
  #print(subrepeata)

  subrepeatb = ''
  randomnum2 = 150 - randomnum1 #subtracts number of nucleotides in subrepeata from amount of subrepeatb
  for i in range(randomnum2):
      subrepeatb += random.choice(nucleotideslist) #adds a random sequence of nucleotides amounting to random2 to subrepeatb
  #print(subrepeatb)
  subset1 = subrepeata + subrepeatb
  return(subset1 * 2) #prints full sequence
generator = dnagenerator() #assigns function to a variable

filename = input("File name is: ")
header = input("File header: ")
#user inputs
def spidroinFile(filename, header): #function to create fasta file
  try: #not neededbut helps make the code run smoothly even with errors
    with open(filename + ".fasta", "w") as fasta_handle: 
      fasta_handle.write(">Gene info " + header + "\n") #adds header into the file
      fasta_handle.write(generator) #adds the generated DNA sequence
  except IOError as err: #detects error in the function
    print("error")
  return fasta_handle

spidroinFile(filename, header)