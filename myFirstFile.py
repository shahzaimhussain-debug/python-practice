#item_name= "wireless MOUSE"
#wireless_mouse= 2499
#quanttity= 3
#clean=item_name.strip().title()
#total= wireless_mouse*quanttity
#print(f"{clean} x3 = RS {total}")

#raw_code= "ord-2024-0042"
#clean=raw_code.replace("-","").upper()
#print(f"order {clean} has {len(raw_code)} characters")

# A receipt line. The item name is " wireless MOUSE ", the price is 2499 and the quantity is 3. Print exactly: Wireless Mouse x3 = Rs 7,497. Work out the total in code; don't type the number

#orders = [
#    {"id": "A101", "total": 4500, "status": "delivered"},
  #  {"id": "A102", "total": 12800, "status": "pending"},
 #   {"id": "A103", "total": 2300, "status": "delivered"},
#]

#pending_count = 0
#for order in orders:
 #   if order["status"] == "pending":
 #       pending_count += 1
 #       print(f"Pending: {order['id']}")

#print(f"{pending_count} order(s) pending"marks = 12800
#total = 80
#if total < 50:
#    print("fail")
#elif total > 80 :
#    print("A")
#elif total > 65-79 :
#    print("B")
#elif total > 50-64 :
#    print("C")


#def format_rupees(amount)
#    return f"Rs{amount:,}"
#print(format_rupees(12800))
#print(format_rupees(999))
#print(format_rupees(1250000))
#print("Noor Foods owes",format_rupees(11520))
#rate=0
#rate +="subtotal,rate,add_tax,returns"
#tax="subtotal,rate"
#rate=0.18
#aad_tax=7200
#returns=7560
#sub_total=rate
#print(f"sub_total")
orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]

# pending_count = 0
# for board in orders:
#     if board["status"] == "delivered":
#      pending_count += board['total']
#         #print(f"Pending: {board['id']}")

# print(f"total revenue: RS {pending_count} ")

# orders = [
#     {"id": "A101", "total": 4500, "status": "delivered"},
#     {"id": "A102", "total": 12800, "status": "pending"},
#     {"id": "A103", "total": 2300, "status": "delivered"},
# ]
# biggest_order=orders[0]
# for bo in orders:
#     if bo["total"] > biggest_order["total"]:
#        biggest_order = bo

# print(f"Biggest order: {biggest_order['id']} (Rs {bigges
orders = [
    {"customer": "Noor Foods", "total": 4500},
    {"customer": "Karachi Crafts", "total": 12800},
    {"customer": "Noor Foods", "total": 2300},
    {"customer": "Bilal Traders", "total": 7600},
    {"customer": "Karachi Crafts", "total": 3900},
    {"customer": "Noor Foods", "total": 6100},
]
customer_total = {}
for cus in orders:
    cus_name = cus["customer"]
    cus_total = cus["total"]
    if cus_name in customer_total:
        customer_total[cus_name] += cus_total
    else:
        customer_total[cus_name] = cus_total

for customer, total in customer_total.items():
 print(f"{customer }: Rs {total ,}")
# Noor_Foods= Rs 12,900
# Karachi_Crafts= Rs 16,700
# Bilal_Traders= Rs 7,600
