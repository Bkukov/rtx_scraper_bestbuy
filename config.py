""" for multiple sessions/cards that you want to scan through,
change the product URL and then inspect the buy button and copy its xpath
and put it into add_to_cart  """

keys = {
    'card_a':
        {
        "cart" : "https://www.bestbuy.com/cart/c/",
        "product_url" : "https://www.bestbuy.com/site/nvidia-geforce-rtx-2070-super-8gb-gddr6-pci-express-3-0-graphics-card-black-silver/6361328.p?skuId=6361328",
        "add_to_cart" : '//*[@id="fulfillment-add-to-cart-button-c14cc12d-9383-408a-8352-b82e42a6a146"]/div/div/button',
        "email" :  "",
        "password" : "",
        "last_three" : ""
        },
    'card_b':
        {
        "cart" : "https://www.bestbuy.com/cart/c/",
        "product_url" : "https://www.bestbuy.com/site/evga-super-xc-ultra-gaming-nvidia-geforce-rtx-2070-super-8gb-gddr6-pci-express-3-0-graphics-card-black-transparent/6373489.p?skuId=6373489",
        "add_to_cart" : '//*[@id="fulfillment-add-to-cart-button-fc592ffd-17b5-4d6d-b9c8-68e609a705ed"]/div/div/button',
        "email" :  "",
        "password" : "",
        "last_three" : ""
        },
}
