a=1                         #initialize the first deposit
b=1                         #initialize the second deposit

while a<=1000:              #change to your liking to go through the first n possibilities of the first deposit

  while b<=1000:            #change to your liking to go through the first n possibilities of the second deposit
  
    x=a+b                   #balance on day two
    y=x                     #temporary variable to store the balance
    x=y+a                   #new balance on day three (balance of day two + balance of day one, which in this case is also the first deposit)
    d=3                     #initialize the day counter, as from now on it will be used in the loop
    
    while x<1000000:        #loop till we reach one million
      z=y                   #temporary variable to store the previous balance
      y=x                   #temporary variable to store the current balance
      x=y+z                 #balance on next day
      d+=1                  #increment day counter
    
    if x==1000000:          #we have exited the loop as the number reached one million or more, but is it exactly one million?
      print("Success, reached 1 million on day "+str(d)+", first deposit was "+str(a)+" and second deposit was "+str(b)) #output of the first and second deposit used in case the balance is exactly one million, with the number of days it took
    
    b+=1                    #increment the second deposit for the next check
  
  a+=1                      #increment the first deposit by one so that we can go through another round of combinations with various second deposits
  b=1                       #reset the second deposit back to one for the next iteration