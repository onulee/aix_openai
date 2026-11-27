from django.shortcuts import render
import oracledb
from dotenv import load_dotenv
from pathlib import Path
import os

# 전역변수
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
env_file = BASE_DIR/'.env'
load_dotenv(env_file)
ora_conn = os.getenv('ora_conn')
print('확인 : ',BASE_DIR)


def blist(request):
    # db접속
    conn = oracledb.connect(ora_conn)
    cursor = conn.cursor()
    sql = '''select bno,nickname,btitle,bcontent,bgroup,bstep,bindent,bhit,bdate
            from board a,member b where a.id = b.id'''
    cursor.execute(sql)
    # 컬럼정보
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    print('확인 : ',columns)
    rows_list = [dict(zip(columns,row)) for row in rows]
    cursor.close()
    conn.close()
    context={'blist':rows_list}
    return render (request,'blist.html',context)
