import oracledb
import os
from dotenv import load_dotenv

load_dotenv()
ora_conn = os.getenv('ora_conn')
conn = oracledb.connect(ora_conn)

cursor = conn.cursor()
# insert
no = 2
name = '홍길순'
school = '디지털고'
height=190
kor = 90
eng=90
math=90
total=270
avg=90
specialty='python'
srank=''

# 실행문
sql = f"insert into stuscore2 values ({no},'{name}',{school},{height},{kor},{eng},{math},{total},{avg},{specialty},{srank})"
cursor.execute(sql)

print('저장완료')
cursor.close()
#------------------------------
print('프로그램 종료')    
conn.close()
