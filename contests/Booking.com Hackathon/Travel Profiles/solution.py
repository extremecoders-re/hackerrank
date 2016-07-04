hotel_list = {}

def find_hotels(max_budget, reqd_facil):
    global hotel_list
    found = []
    for key in hotel_list.keys():
        hotel_price = (hotel_list[key])[0]
        hotel_facil = (hotel_list[key])[1]
        
        if hotel_price <= max_budget:
            if reqd_facil <= hotel_facil:
                found.append(key)
                
    return found
    

def hotel_sorter(hotel1_id, hotel2_id):
    global hotel_list
    
    # Sort by features
    if len((hotel_list[hotel1_id])[1]) > len((hotel_list[hotel2_id])[1]):
        return -1
    
    elif len((hotel_list[hotel1_id])[1]) < len((hotel_list[hotel2_id])[1]):
        return 1
    
    # Sort by price
    if (hotel_list[hotel1_id])[0] < (hotel_list[hotel2_id])[0]:
        return -1
    
    elif (hotel_list[hotel1_id])[0] > (hotel_list[hotel2_id])[0]:
        return 1
    
    # Sort by id
    return hotel1_id - hotel2_id    
    

N = input()
for i in range(N):
    line = raw_input()
    vals = line.strip().split()
    hotel_id, hotel_price, hotel_facil = int(vals[0]), int(vals[1]), vals[2:]
    hotel_list[hotel_id] = [hotel_price, set(hotel_facil)]
    
    
M = input()
for i in range(M):
    line = raw_input()
    vals = line.strip().split()
    max_budget, reqd_facil = int(vals[0]), set(vals[1:])
    
    found_hotels = find_hotels(max_budget, reqd_facil)
    
    if len(found_hotels) == 0:
        print
        
    else:
        found_hotels = sorted(found_hotels, cmp = hotel_sorter)
        for hotel in found_hotels:
            print hotel,
        print 