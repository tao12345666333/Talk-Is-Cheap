#!/usr/bin/env python
# coding=utf-8
import thread
import time


all_ticket = 1000

def sale(name, ticket_lock):
    while True:
        if ticket_lock.acquire():
            try:
                global all_ticket
                if all_ticket <= 0:
                    break
                else:
                    print name, 'sale', all_ticket
                    all_ticket = all_ticket - 1

            finally:
                ticket_lock.release()

    thread.exit_thread()

lock = thread.allocate_lock()

id1 = thread.start_new_thread(sale, ('s1', lock))
id2 = thread.start_new_thread(sale, ('s2', lock))
id3 = thread.start_new_thread(sale, ('s3', lock))

time.sleep(2)
