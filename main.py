# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# code for the new datatbse connection

Connection conn = dataSource.getConnection();
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT ID FROM USERS");

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


mylist = [1, 2, 3]
for item in mylist:
    print
    item

mydict = {1: 'one', 2: 'two', 3: 'three'}
for key in mydict:
    print
    key, mydict[key]

for i, item in enumerate(mylist):
    mylist[i] = item ** 2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
