import pymysql

class MemberDAO:
    conn  = None
    cur = None
    def __init__(self):

            self.conn = pymysql.connect(
                host='localhost',
                port=3366,
                user='root',
                password='1234',
                db='big',
                charset='utf8'
            )
            self.cur = self.conn.cursor()

    def create(self, vo): #회원가입

            # sql문을 보내보자.
            sql = "insert into member values ( %s, %s, %s, %s )"

            # 커서로 sql문을 보냄
            result = self.cur.execute(sql,vo)
            print('sql문 전송 결과>', result)

            self.conn.commit()  # insert한것 반영해줘
            self.conn.close()

    def delete(self,id):
            sql = "DELETE FROM member WHERE id = %s "
            result = self.cur.execute(sql, id)
            print('sql문 전송 결과>', result)
            self.conn.commit()
            self.conn.close()


    def read(self, id): #1개

        sql = "SELECT * FROM member WHERE id = %s "
        result = self.cur.execute(sql, id)
        if result == 1:
            # read인 경우, 커서로 스트림(연결통로)에 있는 검색결과를 꺼내주어야한다.
            one = self.cur.fetchone()  # row하나만 꺼내와라
            print(one)
            return one
        else:
            one = None
            return one
        conn.close()


    def login(self, vo):

            sql = "SELECT * FROM member WHERE id = %s and pw= %s"
            result = self.cur.execute(sql, vo)
            print('sql문 전송 결과>', result)
            if(result==1):
                return "로그인 성공"
            else:
                return " 로그인 실패 "
            conn.close()



