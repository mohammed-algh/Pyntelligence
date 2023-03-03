# word count tool
import re

#function to cound words in text
def count_words(message: str) -> int :
    remove_specials = re.sub(r"[^a-zA-Z0-9]"," ",message)
    striped_message = re.sub(" +", ' ',remove_specials).strip()
    number_words = striped_message.split(" ")
    return int(len(number_words))


