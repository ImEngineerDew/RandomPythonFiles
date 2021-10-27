
def reverse(text):
     return text[::-1]
	

if __name__ == '__main__':
     phrase =  input("Please type your text or phrase: ").lower().join('')  
     backwards = reverse(phrase)

     if phrase == backwards:
          print("It's a palindrome")
     else:
          print("This is not a palindrome")