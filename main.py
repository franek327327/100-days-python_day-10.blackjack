from art import logo
import random
import os

cards = {
    'A': [11, 1],
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

def showCards(playerCardsList, computerCardsList, endPlayerTurn = False):
  os.system('clear')
  playerPoints = countPoints(playerCardsList)
  computerPoints = countPoints(computerCardsList)
  print(logo)
  print(f"Your cards: {cardsListToString(playerCardsList)} ({playerPoints} points)")
  print(f"Computer cards: {cardsListToString(computerCardsList)} ({computerPoints} points)")

  checkGameStatus(playerPoints, computerPoints, endPlayerTurn)

  hitTemplate(playerCardsList, computerCardsList)

def computerTurn(playerCardsList, computerCardsList):
  while countPoints(computerCardsList) < 17:
    hit(computerCardsList)

  showCards(playerCardsList, computerCardsList, True)

def checkGameStatus(playerPoints, computerPoints, endPlayerTurn):
  if playerPoints > 21:
    print('You Lose!')
    endGameTemplate()
    
  if endPlayerTurn:
    if computerPoints > 21:
      print('You Win!')
      endGameTemplate()

    elif playerPoints > computerPoints:
      print('You Win!')
      endGameTemplate()

    elif playerPoints < computerPoints:
      print('You Lose!')
      endGameTemplate()

    elif playerPoints == computerPoints:
      print('Push!')
      endGameTemplate()

def hitTemplate(playerCardsList, computerCardsList):
  playerChoice = ''
  while playerChoice != 'hit' or playerChoice != 'stay':
    playerChoice = input('Do you wanna "stay" or "hit": ')
    if playerChoice == 'hit':
      hit(playerCardsList)
      showCards(playerCardsList, computerCardsList)
    elif playerChoice == 'stay':
      computerTurn(playerCardsList, computerCardsList)

def hit(cardsList):
  cardsList += chooseRandomCards(1)

def cardsListToString(cardsList):
  cardsString = ''
  for card in cardsList:
    cardsString += f'[{card}] '

  return cardsString

def countPoints(cardsList):
  cardsWithManyValues = []
  points = 0
  for card in cardsList:
    if isinstance(cards[card], list):
      cardsWithManyValues.append(cards[card])
    else:
      points += cards[card]

  if len(cardsWithManyValues) > 0:
    for moreValueCard in cardsWithManyValues:
      usedCard = False
      for value in moreValueCard:
        if usedCard:
          continue
          
        if points + value <= 21:
          points += value
          usedCard = True

  return points

def chooseRandomCards(numberOfCards = 1):
  playerCards = []
  for x in range(numberOfCards):
    playerCards.append(random.choice(list(cards.keys())))
  return playerCards

def endGameTemplate():
  loseChoice = ''
  while loseChoice != 'exit' and loseChoice != 'again':
    loseChoice = input('If you want to start again type "again" and "exit" if you want to exit the game: ')
    if loseChoice == 'exit':
      exit()
    elif loseChoice == 'again':
      startNewGame()

def startNewGame():
  playerCards = chooseRandomCards(2)
  ComputerCards = chooseRandomCards(1)
  showCards(playerCards, ComputerCards)



startNewGame()
  
  

