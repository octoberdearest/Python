rewards = [
    "Coke sakto",               # 0
    "Boy Bawang",               # 1
    "15pcs. Yucky candy",       # 2
    "15pcs. Pintura candy",     # 3
    "15PHP load",               # 4
    "3 pcs. Dove conditioner",  # 5
    "Cottonbuds",               # 6
    "One sheet of Biogesic",    # 7
    "100mL Pepper/Pintura",     # 8
]

#USER INPUT
entered_text = input('Please enter text:')

#USER INPUT LENGTH
entered_text_len = len(entered_text)

#REWARD NUMBER
reward_num = int(entered_text[0])
reward_val = rewards[reward_num]

#CUSTOMER NAME
cust_name = entered_text[2:-2].title()

print(f"Hi {cust_name}! You have successfully redeem reward #{reward_num} - {reward_val}! Thank you for using Aling Nena's Sari-sari store.", )



