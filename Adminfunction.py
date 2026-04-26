def Administrator():
    
    import mysql.connector as sc
    mycon = sc.connect(host="localhost", user="root", passwd="bvm", database="NomNomNation")
    if mycon.is_connected():
        print('Connected')
    else:
        print('Not connected')
    cur=mycon.cursor()

    from prettytable import PrettyTable

    A = PrettyTable()
    M = PrettyTable()
    D = PrettyTable()
    Disp = PrettyTable()


    while True:
        print('\n1. Add details of an item')
        print('\n2. Modify details of an item')
        print('\n3. Delete the details of an item ')
        print('\n4. Display the details of all items ')
        print('\n0. Exit')
        ch=int(input('Enter Choice '))
        
        if ch==1:
            cur.execute('select * from menu_data;')
            A.field_names = ["S.No","Category", "Item Name", "Price"]
            data=cur.fetchall()
            print('\nDetails of item')
            for x in data:
                A.add_row(x)
            print(A)

            mid=input('Enter Menu ID ')
            cat=input('Enter Category ')
            Iname=input('Enter Item Name ')
            price=int(input("Enter Price of the item "))
            cur.execute('insert into menu_data values("{}", "{}", "{}", "{}");'.format(mid,cat,Iname,price))
            mycon.commit()

        elif ch==2:
            cur.execute('select * from menu_data;')
            M.field_names = ["S.No","Category", "Item Name", "Price"]
            data=cur.fetchall()
            print('\nDetails of item')
            for x in data:
                M.add_row(x)
            print(M)
            
            mid=input('Enter Menu ID ')
            Iname=input("Enter the new name of the item ")
            price=int(input('Enter the new price of the item '))
            cur.execute('update menu_data set Iname="{}",Price="{}" where MID= "{}";'.format(Iname,price,mid))
            print(Iname, 'Item updated.....')
            mycon.commit()


        elif ch==3:
            cur.execute('select * from menu_data;')
            D.field_names = ["S.No","Category", "Item Name", "Price"]
            data=cur.fetchall()
            print('\nDetails of item')
            for x in data:
                D.add_row(x)
            print(D)
            
            mid=input('Enter Menu ID ')
            cur.execute('delete from menu_data where MID= "{}";'.format(mid))
            print('Item Deleted...')
            mycon.commit()

        elif ch==4:
            cur.execute('select * from menu_data;')
            Disp.field_names = ["S.No","Category", "Item Name", "Price"]
            data=cur.fetchall()
            print('\nDetails of item')
            for x in data:
                Disp.add_row(x)
            print(Disp)

        elif ch==0:
            print('Exiting....')
            break

        else:
            print('Invalid Choice')
            mycon.close()
