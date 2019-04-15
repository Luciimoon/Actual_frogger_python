def go( word ):
  count = word.count("aplus")

  if count > 1:
      return "yes"
  else:
      return "no"


print ( go( "dog#cat#pigaplus" ) )
print ( go( "pigs#apluscompsci#food" ) )
print ( go( "##catgiraffeapluscompsci" ) )
print ( go( "apluscatsanddogsaplus###" ) )
print ( go( "###" ) )
print ( go( "aplusdog#13337#pigaplusprogram" ) )
print ( go( "code#H00P#code1234" ) )
print ( go( "##wowgira77##eplus" ) )
print ( go( "catsandaplusdogsaplus###" ) )
print ( go( "7" ) )

