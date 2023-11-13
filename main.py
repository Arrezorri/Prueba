me_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }
if word in meme_dict.keys():
  word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
  print(word, meme_dict(word))
else:
    print("Esa palabra no se encuentra aquí, vuelve a intentar con otra")
