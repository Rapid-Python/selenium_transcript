from bs4 import BeautifulSoup

list_chat = list()
with open("5254.txt","rb") as file_data:
    for line in file_data.readlines():
        temp_dict = dict()
        html_content = line.decode().strip()
        bs4_content = BeautifulSoup(html_content,'html.parser')
       
        chatbox_html = bs4_content.find_all("div",class_="TBMuR bj4p3b")
      
        for chat in chatbox_html:
           
            span_msg = chat.find("div", class_="zs7s8d jxFHg").decode_contents().strip()
            if span_msg:
                temp_dict["author"] = span_msg
                author_message = chat.find("div", class_="iTTPOb VbkSUe")
                if author_message:
                    temp_dict["message"] = author_message.text
                else:
                    temp_dict["message"] = ""
                list_chat.append(temp_dict)
           
                print(temp_dict)
                
# print(list_chat)
       
# exit()               
                
final_chat = list()
temp_dict = dict()
# count = -1
for author_chat in list_chat:

    if temp_dict.get('author') != author_chat['author']:
        if temp_dict:
            temp_dict["message"] = "".join(temp_dict["message"])
            write_str = f"{temp_dict['author']} : {temp_dict['message']}\n"
            # print(write_str)
            final_chat.append(write_str)
        temp_dict = dict()
        temp_dict['author'] = author_chat['author']
        temp_dict['message'] = [author_chat['message']]
        continue
    if temp_dict["message"][-1].upper() == author_chat["message"].upper():
        continue
    elif len(temp_dict["message"][-1]) < len(author_chat["message"]):
        old_upper_message = temp_dict["message"][-1].upper()
        # print(old_upper_message)
        # exit()
        new_upper_message = author_chat["message"].upper()
        if old_upper_message in new_upper_message:
            temp_dict["message"][-1] = author_chat["message"]
        else:
            temp_dict["message"].append(author_chat["message"])
    else:
        old_upper_message = temp_dict["message"][-1].upper()
        new_upper_message = author_chat["message"].upper()
        if new_upper_message in old_upper_message:
            continue
        else:
            temp_dict["message"].append(author_chat["message"])
         
# print(final_chat)

with open("5254_CHAT.txt","w+") as out_file:
    out_file.writelines(final_chat)