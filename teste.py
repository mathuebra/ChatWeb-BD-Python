from database import Database

db = Database('/home/mathuebra/VS/DatabasePython/ChatWeb/chatweb')

print(db.verify_login('mathuebra@gmail.com', '123e456'))