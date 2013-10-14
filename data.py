import uuid
import landerdb

config = {

"host":"0.0.0.0",
"port":3334,
"relay":False,
"id":uuid.uuid4().hex,
"broker":("karat.zapto.org", 3333),
"db":landerdb.Connect("nodes.db"),

}
