
import mysql.connector

mydb = mysql.connector.connect(
    host="103.76.228.222",
    user="user2",
    password="Learner@123",
    database="learnersdb"
)

print(mydb)

c = mydb.cursor()

insertQuery="""
INSERT INTO securitydata (ticker, company_name, market_sector, bid_price, ask_price, market_price, volume, day_high, day_low,pe_ratio)
values (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)
"""
data = [("Ama", "FAcebook Inc", "Technology", 343.0,322.0,22,222.3,222.2,322.3,1.2)]

c.executemany(insertQuery, data)
mydb.commit()

selectQuery = "select *from securitydata"
c.execute(selectQuery)
stock_data=c.fetchall()

for s in stock_data:
    print(s)

mydb.close()