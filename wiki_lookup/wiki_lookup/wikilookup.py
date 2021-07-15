import wikipedia

library = {}

def run ():
  """Spustí vyhledávání ve Wikipedii ovládané z příkazového řádku.
  """
  print('*'*100)
  name = input('\nZadejte název článku: \n\n')
  print()
  
  if name in library.keys():
    print(library[name])
  else:
    try:
      summ = wikipedia.summary(name, auto_suggest=False)
      print(summ)
      library[name] = summ

    except wikipedia.exceptions.PageError as e:
      no_searches = wikipedia.search(name)
      no_text = f'Článek s názvem "{name}" nebyl nalezen. Zadaný text se vyskytuje v článcích s tímto názvem: \n{", ".join(x for x in no_searches)}'
      print(no_text)
      library[name] = no_text

    except wikipedia.exceptions.DisambiguationError as e:
      ambig_searches = wikipedia.search(name)
      ambig_text = f'Článek s názvem "{name}" není jednoznačný. Název může mít tyto významy: \n{", ".join(x for x in ambig_searches)}'
      print(ambig_text)
      library[name] = ambig_text

def multirun():
  """Umožní opakované spuštění vyhledávání ve Wikipedii ovládané z příkazového řádku.
  """
  while True:
    run()
    print()
    while True:
      print('*'*100)
      answer = input('Chcete vyhledat další článek? (A/N): ').strip()
      if (len(answer) > 0) and (answer[0] in '01ANan'):
          break     
      print('Odpověď musí začínat některým ze znaků "AN"\n'
              'Zkuste odpovědět znovu.')
    if answer[0] in '0nN':
      break     
    print('\nZadali jste opakování vyhledávání.\n')
  print('\nVyledávání bylo na Váš pokyn ukončeno.\n')

def initialize():
  """Inicializuje vyhledávání.
  """
  wikipedia.set_lang("cs")
  global library
  print('\nPro zadaný název bude vypsán souhrn článku. Vyhledávání můžete opakovat.\n')
  multirun()







