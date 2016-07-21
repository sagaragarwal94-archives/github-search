import requests

def one_sort(by,order):
    sorted_list = sorted(json_obj, key=lambda k: k[by], reverse = order)
    return sorted_list

def double_sort(by1,by2,order):
    sorted_list = sorted(json_obj, key=lambda k: (k[by1],k[by2]), reverse = order)
    return sorted_list

def sort_by(json_obj):
    choice = int(raw_input("Enter Your Choice:\n1. Sort By Name\n2. Sort By Created Date\n3. Sort By Issues\n4. Sort By Contributors\n5. Sort By Name and Created Date\n6. Sort By Name and Issues\n7. Sort By Issues and Created Date\n>>>"))
    #sorting will first done for Capital letters and after that for small letters.
    if choice == 1:
        sorted_list = one_sort('name',False)
        for row in sorted_list:
            print "%s" %(row['name'])
    if choice == 2:
        sorted_list = one_sort('created_at',True)
        for row in sorted_list:
            print "%s = %s" %(row['name'],row['created_at'])
    if choice == 3:
        sorted_list = one_sort('open_issues',True)
        for row in sorted_list:
            print "%s = %s" %(row['name'],row['open_issues'])
    if choice == 4:
        pass
        #I am unable to find Contributors number in api!
    if choice == 5:
        sorted_list = double_sort('name','created_at',False)
        for row in sorted_list:
            print "%s = %s" %(row['name'],row['created_at'])
    if choice == 6:
        sorted_list = double_sort('name','open_issues',False)
        for row in sorted_list:
            print "%s = %s" %(row['name'],row['open_issues'])
    if choice == 7:
        sorted_list = double_sort('created_at','open_issues',False)
        for row in sorted_list:
            print "%s = %s = %s" %(row['name'],row['open_issues'],row['created_at'])



#main code starts here!
org_name = str(raw_input("Enter the name of the organisation: ")).lower()
api_url = "https://api.github.com/orgs/"+ org_name + "/repos"
r= requests.get(api_url)
json_obj = r.json()

try:
    json_obj['message']
    print "No such organisation exists!"
except:
    sort_by(json_obj)
