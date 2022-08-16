from bs4 import BeautifulSoup

final_chat = list()

def get_message_author_from_bsfour(file_name):
    list_chat = list()
    with open(file_name, "rb") as file_data:
        for line in file_data.readlines():
            # temp_dict = dict()
            html_content = line.decode().strip()
            bs4_content = BeautifulSoup(html_content,'html.parser')
            chatbox_html = bs4_content.find_all("div",class_="TBMuR bj4p3b")
            for chat in chatbox_html:
                temp_dict = dict()
                span_msg = chat.find("div", class_="zs7s8d jxFHg").decode_contents().strip()
                if span_msg:
                    temp_dict["author"] = span_msg
                    author_message = chat.find("div", class_="iTTPOb VbkSUe")
                    if author_message:
                        temp_dict["message"] = author_message.text
                    else:
                        temp_dict["message"] = ""
                    list_chat.append(temp_dict)
                    # print(temp_dict)
    return  list_chat

def final_message(count, temp_dict):
    # pass
    #  final_chat = list()
     if temp_dict:
        temp_dict['message'] = temp_dict['message'].strip()
        if not temp_dict['message']:
            pass
        else:
            print("temp_dict['message']: ", temp_dict['message'])
            if temp_dict['message'][0].isalpha():
                pass
            else:
                temp_dict['message'] = temp_dict['message'][1:]
           
            if count > 1:
                # print(final_chat[-1])
                get_author_len = final_chat[-1].find(" : ")
                get_author_from_final_chat = final_chat[-1][0:get_author_len]
                if temp_dict['author'] == get_author_from_final_chat:
                    # pass
                    get_message_from_final_chat = final_chat[-1][get_author_len+2:]
                    
                    del final_chat[-1]
                    temp_dict['message'] = get_message_from_final_chat.strip() +" "+temp_dict['message'].strip()
                    write_str = f"{temp_dict['author']} : {temp_dict['message']}\n\n"
                else:  
                    write_str = f"{temp_dict['author']} : {temp_dict['message']}\n\n"
            else:  
                write_str = f"{temp_dict['author']} : {temp_dict['message']}\n\n"
                
            if temp_dict['message']:
                final_chat.append(write_str)            


def evaluate_message(list_chat):
    temp_dict = dict()
    count = -1
    for author_chat in list_chat:
        count += 1
    
        final_message(count, temp_dict)
                
        temp_dict = dict()
    
        if count >0 and author_chat['author'] == list_chat[count-1].get('author'):
            temp_dict['author'] = author_chat['author']
            temp_dict['message'] = ''
            msg = list_chat[count-1].get('message')
        
            new_msg = msg.strip()
            if not new_msg:
                continue
        
            if new_msg[-1].isalpha():
                pass
            else:
                new_msg = new_msg[:-1]
            
            lastTwoWords = new_msg.split()[-2:]
            lastOneWords = new_msg.split()[-1:]
        
            joined_two_word = " ".join(lastTwoWords)
            joined_one_word = "".join(lastOneWords)
        
            if list_chat[count-1].get('message').upper() == author_chat['message'].upper():
                # print("iffffffffff")
                temp_dict['message'] = ''
                continue
            elif joined_two_word.upper() in author_chat['message'].upper():
            
                author_chat['message'] = author_chat['message'].upper()
                joined_two_word = joined_two_word.upper()
                temp_dict['message'] = author_chat['message'].split(joined_two_word,1)[1]
                temp_dict['message'] = temp_dict['message'].lower()
                
                continue
            elif joined_one_word.upper() in author_chat['message'].upper():
            
                author_chat['message'] = author_chat['message'].upper()
                joined_one_word = joined_one_word.upper()
                temp_dict['message'] = author_chat['message'].split(joined_one_word,1)[1]
                temp_dict['message'] = temp_dict['message'].lower()            
                continue
            else:
                temp_dict['message'] = author_chat['message']
                continue
        
        if author_chat['author'] == list_chat[count-1].get('author'):
            temp_dict['author'] = author_chat['author']
            if list_chat[count-1].get('message').upper() == author_chat['message'].upper():
                # print("iffffffffff")
                temp_dict['message'] = ''
                continue
            elif list_chat[count-1].get('message').upper() in author_chat['message'].upper():
                temp_dict['message'] = author_chat['message'].replace(list_chat[count-1].get('message'), "")
                continue
            else:
                temp_dict['message'] = author_chat['message']
                continue
              
        if count >= 2 and author_chat['author'] == list_chat[count-2].get('author'):
        
            temp_dict['author'] = author_chat['author']
            temp_dict['message'] = ''
            old_msg = list_chat[count-2].get('message')
        
            new_msg = old_msg.strip()
            if not new_msg:
                continue
            print("new_msg: ", new_msg)
            if new_msg[-1].isalpha():
                pass
            else:
                new_msg = new_msg[:-1]
            
            lastTwoWords = new_msg.split()[-2:]
            lastOneWords = new_msg.split()[-1:]
        
            joined_two_word = " ".join(lastTwoWords)
            joined_one_word = "".join(lastOneWords)
        
            if list_chat[count-2].get('message').upper() == author_chat['message'].upper():
            
                temp_dict['message'] = ''
                continue
            elif joined_two_word.upper() in author_chat['message'].upper():
                print("joined_two_word: ", joined_two_word)
                print("author_chat['message']: ", author_chat['message'])
                author_chat['message'] = author_chat['message'].upper()
                joined_two_word = joined_two_word.upper()
                temp_dict['message'] = author_chat['message'].split(joined_two_word,1)[1]
                temp_dict['message'] = temp_dict['message'].lower()
                continue
            elif joined_one_word.upper() in author_chat['message'].upper():
                # temp_dict['message'] = author_chat['message'].split(joined_one_word,1)[1]
                author_chat['message'] = author_chat['message'].upper()
                joined_one_word = joined_one_word.upper()
                temp_dict['message'] = author_chat['message'].split(joined_one_word,1)[1]
                temp_dict['message'] = temp_dict['message'].lower()
                continue
            else:
                temp_dict['message'] = author_chat['message']
                continue     
        
        if author_chat['author'] != list_chat[count-1].get('author'):
            temp_dict['author'] = author_chat['author']
            temp_dict['message'] = author_chat['message']
            continue
        else:
            if list_chat[count-1].get('message').upper() in author_chat['message'].upper():
                temp_dict['message'] = author_chat['message'].replace(list_chat[count-1].get('message'), "")
                continue
            else:
                temp_dict['message'] = author_chat['message']
                continue

def final_messages_in_text(file_name):
    new_file = f"DEMO_{file_name}"
    with open(new_file, "w+") as out_file:
        out_file.writelines(final_chat)
    

    