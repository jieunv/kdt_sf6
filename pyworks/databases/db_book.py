# 도서 관리 db
# 테이블 생성 - book
import sqlite3

def getconn():
    # db가 없으면 생성되고 있으면 연결
    conn = sqlite3.connect('./output/bookdb.db')
    return conn


def create_book():
    conn = getconn() # getconn() 호출
    cursor = conn.cursor() # 작업 객체
    sql = """
        CREATE TABLE book(
            book_no INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """
    cursor.execute(sql)
    conn.commit() #commit() 해줌
    conn.close()

def insert_book():
    conn = getconn()
    cursor = conn.cursor()
    # ? - 동적 바인딩 기호
    sql = "INSERT INTO book (title, author, price) VALUES (?, ?, ?)"
    cursor.execute(sql, ("천개의 파랑", "천선란", 12600))
    conn.commit()
    conn.close()
# create_book()
insert_book()