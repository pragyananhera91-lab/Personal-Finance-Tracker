# mappings.py

CATEGORY_MAP = {
    'Food': ['pizza', 'burger', 'coffee', 'lunch', 'dinner', 'restaurant', 'grocery', 'swiggy', 'zomato'],
    'Clothing': ['shirt', 'pants', 't-shirt', 'shoes', 'dress', 'jeans', 'myntra', 'ajio'],
    'Travel': ['uber', 'ola', 'petrol', 'bus', 'train', 'flight', 'metro'],
    'Entertainment': ['netflix', 'movie', 'game', 'spotify', 'concert']
}

def auto_classify(description):
    desc = description.lower()
    for category, keywords in CATEGORY_MAP.items():
        for keyword in keywords:
            if keyword in desc:
                return category
    return "Other" # Agar kuch match na ho