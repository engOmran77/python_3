artist = "Michael Jackson"
def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")
printer(artist) 
printer(internal_var)
 
 
Michael Jackson is an artist
Whitney Houston is an artist
