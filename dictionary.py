oxford = {
 "apple" : ("fruit",8),
 "orange" : ("also a fruit",9),
 "mango" : ("even better fruit",7)
}
word = raw_input("enter a fruit name:")
if (word in oxford):
 (m,n) = oxford[word]
 print m

