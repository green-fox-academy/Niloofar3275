todoText = " - Buy milk\n"
str1 = "My todo:\n"
str2 = "- Buy milk\n"
newtodoText = " ".join((str1, str2))
print(newtodoText)
str3 = "- Download games\n"
str4 = "    - Diablo"
newtodoText2 = " ".join((str3, str4))
print(newtodoText2)
  
# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected output:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo
