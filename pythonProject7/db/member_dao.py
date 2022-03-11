import pymysql
def create(vo): #회원가입
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

        # sql문을 보내보자.
        sql = "insert into member values ( %s, %s, %s, %s )"

        # 커서로 sql문을 보냄
        result = cur.execute(sql,vo)
        print('sql문 전송 결과>', result)

        conn.commit()  # insert한것 반영해줘
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
        cur = conn.cursor()
        sql = "DELETE FROM member WHERE id = %s "
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
        sql = "SELECT * FROM member WHERE id = %s "
        result = cur.execute(sql, id)
        if result == 1:
            # read인 경우, 커서로 스트림(연결통로)에 있는 검색결과를 꺼내주어야한다.
            one = cur.fetchone()  # row하나만 꺼내와라
            print(one)
            return one
        else:

            one = None
            return one
        conn.close()

    except Exception as e:
        print("db 연결 중 에러 발생")
        print("에러 정보:", e)


def login(vo):
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
        sql = "SELECT * FROM member WHERE id = %s and pw= %s"
        result = cur.execute(sql, vo)
        print('sql문 전송 결과>', result)
        if(result==1):
            return "로그인 성공"
        else:
            return " 로그인 실패 "
        conn.close()
    except Exception as e:
        print("db 연결 중 에러 발생")
        print("에러 정보:", e)