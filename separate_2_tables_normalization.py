def parse_item(self, response): 
  wsearch = ['train','murder']
  lstitle = []
  x = response.url
  
  booktitle = str(x) 
  booktitle = booktitle.split("/")[4]
  booktitle = booktitle.split("_")[0]
  
  [lstitle.append(i) for i in booktitle.split("-")]
  
  check =  any(item in wsearch for item in lstitle)
  
  if check is True:
   
   myquery = """INSERT INTO links (url,book)
   values(%s,%s)
   """
   val=(x,booktitle)
   cursor.execute(myquery,val)
   mydb.commit()
   
  else:
   myquery = """INSERT INTO links2 (url,book)
   values(%s,%s)
   """
   val=(x,booktitle)
   cursor.execute(myquery,val)
   mydb.commit()
