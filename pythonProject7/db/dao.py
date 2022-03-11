# data access module
# crud기능 ==== > def 4개 필요!
import pymysql

def create(vo):
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )
        print("1. 연결 성공", conn.host_info)
        # 연결 된 통로 (stream)을 통해 , sql문을 보내보자
        # 2. 연결 된 통로를 지정(접근할 수 있는 커서 객체를 획득)
        cur = conn.cursor()

        # sql문을 보내보자.
        sql = "insert into book values ( %s, %s, %s, %s )"

        # 커서로 sql문을 보냄
        result = cur.execute(sql,vo)
        print('sql문 전송 결과>', result)

        conn.commit()  # insert한것 반영해줘
        conn.close()
    except Exception as e:
        print("db 연결 중 에러 발생")
        print("에러 정보:", e)

def update(vo):
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )
        cur = conn.cursor()
        sql = "UPDATE book set name =  %s  where id =  %s "
        result = cur.execute(sql, vo)
        print('sql문 전송 결과>', result)

        conn.commit()
        conn.close()
    except Exception as e:
        print("db 연결 중 에러 발생")
        print("에러 정보:", e)


def delete(id):
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )
        print("1. 연결 성공", conn.host_info)
        cur = conn.cursor()
        sql = "DELETE FROM book WHERE id = %s "
        result = cur.execute(sql, id)
        print('sql문 전송 결과>', result)
        conn.commit()
        conn.close()
    except Exception as e:
        print("db 연결 중 에러 발생")
        print("에러 정보:", e)

def read(id): #1개
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )
        cur = conn.cursor()
        sql = "SELECT * FROM book WHERE id = %s "
        result = cur.execute(sql, id)
        print('sql문 전송 결과>', result)

        #read인 경우, 커서로 스트림(연결통로)에 있는 검색결과를 꺼내주어야한다.
        one = cur.fetchone() #row하나만 꺼내와라
        print(one)
        conn.close()
        return one
    except Exception as e:
        print("db 연결 중 에러 발생")
        print("에러 정보:", e)

def readall(): #1개
    try:
        conn = pymysql.connect(
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )
        cur = conn.cursor()
        sql = "SELECT * FROM book "
        result = cur.execute(sql)
        print('sql문 전송 결과>', result)

        #read인 경우, 커서로 스트림(연결통로)에 있는 검색결과를 꺼내주어야한다.
        all = cur.fetchall()#다 꺼내와 ...  fetchmany(5) ==>row 5개만 꺼내
        print(all)
        conn.close()
        return all
    except Exception as e:
        print("db 연결 중 에러 발생")
        print("에러 정보:", e)
