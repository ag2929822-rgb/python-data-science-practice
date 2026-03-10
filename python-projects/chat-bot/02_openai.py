from openai import OpenAI
client = OpenAI(
    api_key ="your-api-key-here",
)

from openai import OpenAI
client = OpenAI()

command = '''
Give two examples of popular Operating Systems and mention one use of each.
[8:55 am, 13/01/2026] Anurag: OS question to be remember
[7:12 pm, 15/01/2026] Anurag: One attendance in control system
[8:45 am, 16/01/2026] Anurag: Take a look at this Premium Stylish Lightweight Comfortable Shoe Running Shoes For Men on Flipkart
https://dl.flipkart.com/s/xfTLZXNNNN
[8:55 am, 16/01/2026] Anurag: Take a look at this Premium Lightweight Comfortable Regular Wear Walking Shoes For Men on Flipkart
https://dl.flipkart.com/s/xkvqprNNNN
[5:03 pm, 16/01/2026] Anurag: https://www.redeemu.com/dominos-coupons?cid=571208#close
[5:03 pm, 16/01/2026] Anurag: https://www.redeemu.com/dominos-coupons?cid=571208#close
Website fore dominos coupon code

'''
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are person named harry who speaks hindi as well as english. He is from India and his is a coder. You analyzed chat history and respond like harry"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)