# https://pypi.org/project/teradatasql/#SamplePrograms
import teradatasql
con = teradatasql.connect(host="host", user="user", password="pw")
cur = con.cursor()

"""Query and display the results"""
def executeQuery(query) :
    cur.execute(query)
    #print(cur.description, "\n")
    for col in cur.description:
        print(col[0], " | ", end="")
    print()
    #print("\n", cur.fetchmany(10))
    list = cur.fetchmany(5)
    for row in list:
        for col in row: 
            print(col," | ", end = '')
        print()
executeQuery("SELECT * FROM BASE_PORTAL.MASTER_TABLE")

