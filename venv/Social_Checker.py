def go( word ):
  if word.find("-") == 3:
      word = word[4:]
      if word.find("-") == 2:
        word = word[3:]
        return word
      else:
          return "bad"
  else:
    return "bad"


print ( go( "463-44-5678" ) )
print ( go( "46-144-5678" ) )
print ( go( "111-44-5678" ) )
print ( go( "463044-5678" ) )
print ( go( "463-99-8888" ) )
print ( go( "123-11-5323" ) )
print ( go( "463-4-55678" ) )
print ( go( "46314415678" ) )