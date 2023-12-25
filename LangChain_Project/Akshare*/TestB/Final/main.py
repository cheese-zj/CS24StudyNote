import write_data as W
import Initialize as I
import store_csi_index_300 as C
import update_ids
import insert_task
import Applications

def main():
    I.initialize()
    while True:
        print()
        print("Here are your options:")
        print("1.Update CSI_INDEX_300")
        print("2.Finish all tasks")
        print("3.Update ids")
        print("4.Insert tasks")
        print("5.Applications")
        print("6.exit")

        a = input("")
        if a == "1":
            C.run()
        elif a == "2":
            W.wr_data()
        elif a == "3":
            update_ids.updates()
        elif a == "4":
            insert_task.Insert_task()
        elif a == "5":
            Applications.Menu()
        elif a == "6":
            break

    return

def test():
    I.initialize()
    C.run()
    pass


if __name__=="__main__":
    main()

