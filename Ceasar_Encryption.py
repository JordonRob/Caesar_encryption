alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def main():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  
  
  def caesar(direction, text, shift):
      cipher_text = ""
  
      for letter in text:
          position = alphabet.index(letter)
          new_position = 0
          if direction == "encode": 
              if (position + shift) <= 25:
                new_position = position + shift
                #print(f"this is the position: {new_position}")
              elif (position + shift) > 25:
                new_position += ((position + shift) % 26)
                  #print(f"this is the position: {new_position}")
                
          elif direction == "decode":
              if (position - shift) >= 0:
                  new_position = position - shift
              elif (position - shift) < 0:
                new_position = (26 - ((position + shift)% 26))
        
          cipher_text += alphabet[new_position]
      print(f"Here is the {direction}d result of {text}:  {cipher_text}")
      print("")
      status = input("Do you want to contine? Type 'Yes' or 'No':  ").lower()
  
      if status == "yes":
        main()
      else:
        print("Goodbye")
    
  
  caesar(direction, text, shift)
main()

