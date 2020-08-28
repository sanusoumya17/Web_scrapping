import json
import requests


with open("udemy.csv", 'w', encoding="utf-8") as f1:
    f1.write('Title, Url, Created_on, Published, Subscribers, Reviews, Rating, Price, Discounted_Price' + '\n')	
f1.close()
    
page_counter = 0
while True:
    page_counter += 1



    course_url = 'https://www.udemy.com/api-2.0/discovery-units/all_courses/?p=' + str(page_counter) + '&page_size=16&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&category_id=288&source_page=category_page&locale=en_US&currency=inr&navigation_locale=en_US&skip_price=true&sos=pc&fl=cat'
    response = requests.get(course_url).content.decode()
    data = json.loads(response)
    
    if data =='{"detail":"Invalid page size"}' :
        break
    
    data = data['unit']['items']
    
    
    ids=[]
    for j in range(len(data)):
        id_num = data[j]['id']
        ids.append(id_num)
    
    price_url = 'https://www.udemy.com/api-2.0/pricing/?course_ids=' + str(ids)[1:-1] +'&fields[pricing_result]=price,discount_price,list_price,price_detail,price_serve_tracking_id'
    response1 = requests.get(price_url).content.decode()
    data1 = json.loads(response1)
    
    data1 = data1['courses']
    
    for i in range(len(data)):
        title = data[i]['title']
        title = title.strip().replace(',', '')
        
        list_price = data1[str(data[i]['id'])]['list_price']['amount']
        
        try:
            discount_price = data1[str(data[i]['id'])]['discount_price']['amount']
        except Exception:
            discount_price = None
        # getting all the required attributes    
        scrapped_data=str(title)+","+str(data[i]['url'])+","+str(data[i]['created'])+","+str(data[i]['published_time'])+","+str(data[i]['num_subscribers'])+","+str(data[i]['num_reviews'])+","+str(data[i]['rating']) +","+ str(list_price) +","+ str(discount_price)
        # writing the attributes in a csv file
        with open("udemy.csv", 'a',encoding="utf-8") as f2:
            f2.write(scrapped_data + '\n')
    f2.close()
      
    
    
        
                    
        
         
        
