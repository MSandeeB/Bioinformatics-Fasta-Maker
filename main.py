import random
#import packages
import io 
def dnagenerator():
  #makes individual letters into seperate strings
  nucleotideslist = list("AGCT") 
  subrepeata = ''
  #randomly chooses a number from 1-150
  randomnum1 = random.randint(1,150) 
  for i in range(randomnum1):
    #adds a random sequence of nucleotides amounting to random1 to subrepeata
    subrepeata += random.choice(nucleotideslist) 
  #print(subrepeata)

  subrepeatb = ''
  #subtracts number of nucleotides in subrepeata from amount of subrepeatb
  randomnum2 = 150 - randomnum1 
  for i in range(randomnum2):
      #adds a random sequence of nucleotides amounting to random2 to subrepeatb
      subrepeatb += random.choice(nucleotideslist) 
  #print(subrepeatb)
  subset1 = subrepeata + subrepeatb
  #prints full sequence
  return(subset1 * 2)
#assigns function to a variable
generator = dnagenerator() 

filename = input("File name is: ")
header = input("File header: ")
#user inputs
#function to create fasta file
def spidroinFile(filename, header):
  #try is not needed but helps make the code run smoothly even with errors
  try: 
    with open(filename + ".fasta", "w") as fasta_handle: 
      #adds header into the file
      fasta_handle.write(">Gene info " + header + "\n")
      #adds the generated DNA sequence
      fasta_handle.write(generator)
  #detects error in the function
  except IOError as err: 
    print("error")
  return fasta_handle

spidroinFile(filename, header)
