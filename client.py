import socket
import threading
import time
import sys

ENRU = {
	"I": "Я",
"We": "Мы",
"You": "Ты, вы",
"He": "Он",
"She": "Она",
"It": "(о неодуш. предметах)",
"They": "Они",
"Come": "Приходить",
"Do": "Делать",
"Drink": "Пить",
"Eat": "Есть",
"Give": "Давать",
"Go": "Идти",
"Have": "Иметь",
"Hear": "Слышать",
"Help": "Помогать",
"Like": "Нравиться",
"Live": "Жить",
"Put": "Класть, положить",
"Say": "Сказать",
"See": "Видеть",
"Sit": "Сидеть",
"Sleep": "Спать",
"Stand": "Стоять",
"Take": "Брать",
"Use": "Пользоваться, использовать",
"Want": "Хотеть",
"Work": "Работать",
"Boy": "Мальчик",
"Friend": "Друг",
"Girl": "Девочка",
"Man": "Мужчина, человек",
"People": "Люди",
"Woman": "Женщина",
"Country": "Страна, сельская местность",
"Home": "Дом (жилище)",
"Park": "Парк",
"Place": "Место",
"River": "Река",
"School": "Школа",
"Street": "Улица",
"Town": "Город",
"Bread": "Хлеб",
"Breakfast": "Завтрак",
"Dinner": "Обед",
"Fish": "Рыба",
"Food": "Еда",
"Juice": "Сок",
"Meat": "Мясо",
"Milk": "Молоко",
"Tea": "Чай",
"Water": "Вода",
"Afternoon": "День (время после полудня)",
"Day": "День",
"Evening": "Вечер",
"Month": "Месяц",
"Morning": "Утро",
"Night": "Ночь",
"Week": "Неделя",
"Year": "Год",
"Daughter": "Дочь",
"Family": "Семья",
"Father": "Отец",
"Mother": "Мать",
"Son": "Сын",
"Box": "Коробка, ящик",
"Bus": "Автобус",
"Car": "Машина",
"Clothes": "Одежда",
"Cup": "Чашка",
"Money": "Деньги",
"Name": "Имя",
"Pen": "Ручка",
"Rain": "Дождь",
"Thing": "Вещь, предмет",
"Bad": "Плохой",
"Beautiful": "Красивый",
"Big": "Большой",
"Cold": "Холодный",
"Every": "Каждый",
"Good": "Хороший",
"Long": "Длинный",
"New": "Новый",
"Old": "Старый",
"Short": "Короткий",
"Small": "Маленький",
"Warm": "Теплый",
"Black": "Черный",
"Blue": "Синий",
"Brown": "Коричневый",
"Green": "Зеленый",
"Red": "Красный",
"Yellow": "Желтый",
"Never": "Никогда",
"Now": "Сейчас",
"Often": "Часто",
"Today": "Сегодня",
"Tomorrow": "Завтра",
"Usually": "Обычно",
"Yesterday": "Вчера"
}

RUEN = {
"Я": "I",
"Мы": "We",
"Ты, вы": "You",
"Он": "He",
"Она": "She",
"(о неодуш. предметах)": "It",
"Они": "They",
"Приходить": "Come",
"Делать": "Do",
"Пить": "Drink",
"Есть": "Eat",
"Давать": "Give",
"Идти": "Go",
"Иметь": "Have",
"Слышать": "Hear",
"Помогать": "Help",
"Нравиться": "Like",
"Жить": "Live",
"Класть, положить": "Put",
"Сказать": "Say",
"Видеть": "See",
"Сидеть": "Sit",
"Спать": "Sleep",
"Стоять": "Stand",
"Брать": "Take",
"Пользоваться, использовать": "Use",
"Хотеть": "Want",
"Работать": "Work",
"Мальчик": "Boy",
"Друг": "Friend",
"Девочка": "Girl",
"Мужчина, человек": "Man",
"Люди": "People",
"Женщина": "Woman",
"Страна, сельская местность": "Country",
"Дом (жилище)": "Home",
"Парк": "Park",
"Место": "Place",
"Река": "River",
"Школа": "School",
"Улица": "Street",
"Город": "Town",
"Хлеб": "Bread",
"Завтрак": "Breakfast",
"Обед": "Dinner",
"Рыба": "Fish",
"Еда": "Food",
"Сок": "Juice",
"Мясо": "Meat",
"Молоко": "Milk",
"Чай": "Tea",
"Вода": "Water",
"День (время после полудня)": "Afternoon",
"День": "Day",
"Вечер": "Evening",
"Месяц": "Month",
"Утро": "Morning",
"Ночь": "Night",
"Неделя": "Week",
"Год": "Year",
"Дочь": "Daughter",
"Семья": "Family",
"Отец": "Father",
"Мать": "Mother",
"Сын": "Son",
"Коробка, ящик": "Box",
"Автобус": "Bus",
"Машина": "Car",
"Одежда": "Clothes",
"Чашка": "Cup",
"Деньги": "Money",
"Имя": "Name",
"Ручка": "Pen",
"Дождь": "Rain",
"Вещь, предмет": "Thing",
"Плохой": "Bad",
"Красивый": "Beautiful",
"Большой": "Big",
"Холодный": "Cold",
"Каждый": "Every",
"Хороший": "Good",
"Длинный": "Long",
"Новый": "New",
"Старый": "Old",
"Короткий": "Short",
"Маленький": "Small",
"Теплый": "Warm",
"Черный": "Black",
"Синий": "Blue",
"Коричневый": "Brown",
"Зеленый": "Green",
"Красный": "Red",
"Желтый": "Yellow",
"Никогда": "Never",
"Сейчас": "Now",
"Часто": "Often",
"Сегодня": "Today",
"Завтра": "Tomorrow",
"Обычно": "Usually",
"Вчера": "Yesterday",
}



server = socket.socket(
	socket.AF_INET,
	socket.SOCK_STREAM,
)

server.bind(("127.0.0.1", 1235))
server.listen(5)

server_users = []
listeners = []

class thread_with_trace(threading.Thread):
	def __init__(self, *args, **keywords):
		threading.Thread.__init__(self, *args, **keywords) 
		self.killed = False
  
	def start(self):
		self.__run_backup = self.run 
		self.run = self.__run       
		threading.Thread.start(self) 
	def __run(self):
		sys.settrace(self.globaltrace) 
		self.__run_backup() 
		self.run = self.__run_backup 
  
	def globaltrace(self, frame, event, arg):
		if event == 'call':
			return self.localtrace
		else:
			return None
	def localtrace(self, frame, event, arg):
  		if self.killed:
  			if event == 'line':
  				raise SystemExit()
  				return self.localtrace
	def close(self):
		self.killed = True


LOG = ""

	

def listen_user(user_socket, id, address):
	while True:
		data = user_socket.recv(1024)
		ask = data.decode()
		global LOG
		LOG += str(time.ctime(time.time())) + f"{address} ask about {ask} word\n"
		
		if ask in RUEN:
			try:
				user_socket.send(bytes(RUEN[ask], encoding="UTF-8"))
			except BrokenPipeError:
				pass
		elif ask in ENRU:
			try:
				user_socket.send(bytes(ENRU[ask], encoding="UTF-8"))
			except BrokenPipeError:
				pass
		elif ask == "end":
			LOG += str(time.ctime(time.time())) + f"{address} disconnected\n"
			break
			user_socket.send(bytes('Thank You', encoding="UTF-8"))
			listeners[id].close()
		elif ask == "who":
			try:
				LOG += str(time.ctime(time.time())) + f"{address} who command\n"
				user_socket.send(bytes('Eugene Goloven, 8 variant(Traslator)', encoding="UTF-8"))
			except BrokenPipeError:
				pass
		else:
			try:
				LOG += str(time.ctime(time.time())) + f"{address} asked about {ask} word, but i don\'t know it\n"
				user_socket.send(bytes('I don\'t know such word', encoding="UTF-8"))
			except BrokenPipeError:
				pass




def start_server():
	global LOG
	LOG += str(time.ctime(time.time())) + "Server has been started\n"
	print("Server has been started...")

	try:
		while True:
			user_socket, address = server.accept()
			print(f"User {address} has connected to the server")
			
			LOG += str(time.ctime(time.time())) + f"User {address} has connected to the server" + "\n"
			server_users.append(user_socket)
			user_socket.send(bytes(f"Hello user {len(server_users)}", encoding="UTF-8"))
			listener = thread_with_trace(target=listen_user, args=(user_socket, len(listeners), address,))
			listeners.append(listener)
			listener.start()

	except KeyboardInterrupt:
		server.close()
		LOG += str(time.ctime(time.time())) + "Server stoped\n"
		for listener in listeners:
			listener.close()
		for user in server_users:
			# user.disconnect()
			user.send(bytes('end', encoding="UTF-8"))
		with open("logs.txt", "w+") as file:
			file.write(LOG)
	


if __name__ == '__main__':
	start_server()
