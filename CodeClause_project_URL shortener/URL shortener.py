# import pyshortners library for shortening URL
import pyshorteners

# variable for instance of pyshortners method shortner
shortener = pyshorteners.Shortener()

# long URL for user input URL
long_url = input("Enter a long URL to shorten: ")

# after shortning URL using tinyurl.short 
short_url = shortener.tinyurl.short(long_url)

#print the output
print("Shortened URL: " , short_url)

