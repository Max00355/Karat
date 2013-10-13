import uuid
import landerdb

config = {

"port":3334,
"relay":False,
"id":uuid.uuid4().hex,
"broker":("", 3333),
"db":landerdb.Connect("nodes.db"),

}
