# 1. Importing extensions
import streamlit as st
import google.generativeai as ai


# Step 1: Creating sidebar
with st.sidebar:
    key='AQ.Ab8RN6IS0slaWLuvzSDu84gSK3-bb0l4M2z46rRNO4jzwW0NFQ'
    
    # 2. Adding title
    st.title('Chat with AI Assistant✨')
    
    # 3. Taking user question
    question = st.chat_input('Ask anything..')

    propmt = f'''
    answer this question: {question}
    given this info:
    - you are an AI assitant for a restaurant named pizzahub
    - its an italian restrant
    - works 24 hours
    - whatsapp:025376478
    - menu:
    margrita pizza
    sizes:[small,midium,large]
    margrita prices
    'small':140,
    'midium':240,
    'large':300,
    

    pepproni pizza
    sizes:[small,midum,large]
    pepporni prices
    'small':140,
    'midium':240,
    'large':300,
    

  ranch pizza
    sizes:[small,midium,large]
    ranch prices
    'small':140,
    'midium':240,
    'large':250,
    


    '''


    
    # 4. Displaying user message
    if question:
        with st.chat_message('user'):
            st.write(question)
    
        # 5. Generating AI response
        ai.configure(api_key=key)
        model = ai.GenerativeModel('gemini-3.6-flash')
        
        with st.chat_message('ai'):
            with st.spinner('Generating..✨'):
                answer = model.generate_content(question)
            st.write(answer.text)
    

# 2. App title & caption
st.title(':shimmer[:red[Welcome to PizzaHub]]🍕', 
    text_alignment='center') 
st.subheader('The best Italian restuarant serving pizza & pasta!')

# 3. Creating app tabs
pizza_tab, pasta_tab, drinks_tab = st.tabs(
    ['Pizzas🍕', 'Pasta🍝', 'Drinks🍹'])

# 4. Building pizza tab
with pizza_tab:
    col1, col2, col3 = st.columns(3)
    sizes = ['Small', 'Medium', 'Large']
    
    with col1:
        # Adding pizza image and name
        st.image('https://www.papajohnsegypt.com/images/Products/product_50_1768290827.jpg')
        st.subheader('Magerita Pizza', text_alignment='center')
        
        # Adding the size option
        margerita_size = st.segmented_control('Size:', 
            options=sizes, key=1, default='Medium')
        
        # Margerita prices
        margerita_prices = {
            'Small':140,
            'Medium':180,
            'Large':200
        }
        
        # Displaying the price
        margertia_price = margerita_prices[margerita_size]
        st.write(f'Price: :red[**{margertia_price}**] EGP')
        
        # Selecting the quantity
        margerita_qty = st.number_input('Choose quantity:',
                min_value=0, max_value=100, key='mrg_qty')
        
    with col2:
        # Adding pizza image and name
        st.image('https://www.papajohnsegypt.com/images/Products/Chicken-Ranch---Spicy-Korean.jpg')
        st.subheader('Chicken Ranch', text_alignment='center')
        
        # Adding the size option
        ranch_size = st.segmented_control('Size:', 
                    options=sizes, key=2, default='Medium')
        
        # Ranch prices
        ranch_prices = {
            'Small':170,
            'Medium':200,
            'Large':230,
            None:0
        }
        # Displaying the price
        ranch_price = ranch_prices[ranch_size]
        st.write(f'Price: :red[**{ranch_price}**] EGP')
        
        # Selecting the quantity
        ranch_qty = st.number_input('Choose quantity:',
                min_value=0, max_value=100, key='rch_qty')
    
    with col3:
        # Adding pizza image and name
        st.image('https://www.papajohnsegypt.com/images/Products/product_9_1768291533.jpg')
        st.subheader('Pepperoni Pizza', text_alignment='center')
        
        # Adding the size option
        pepperoni_size = st.segmented_control('Size:', 
                    options=sizes, key=3, default='Medium')
        
        # Pepperoni prices
        pepperoni_prices = {
            'Small':180,
            'Medium':220,
            'Large':250,
            None:0
        }
        # Displaying the price
        pepperoni_price = pepperoni_prices[pepperoni_size]
        st.write(f'Price: :red[**{pepperoni_price}**] EGP')
        
        # Selecting the quantity
        pepperoni_qty = st.number_input('Choose quantity:',
                min_value=0, max_value=100, key='ppr_qty')

        
# 7. Building pasta tab
with pasta_tab:
    col1, col2, col3 = st.columns(3)

    with col1:
        # Adding pasta image and name
        st.image(
            "https://images.unsplash.com/photo-1645112411341-6c4fd023714a?w=600&h=450&fit=crop"
        )
        st.subheader('Fettuccine Alfredo', text_alignment='center', anchor=False)

        # Alfredo price
        alfredo_price = 180
        st.write(f'Price: :red[**{alfredo_price}**] EGP')

        # Selecting the quantity
        alfredo_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='alfredo_qty'
        )

    with col2:
        # Adding pasta image and name
        st.image(
            "https://images.unsplash.com/photo-1626844131082-256783844137?w=600&h=450&fit=crop"
        )
        st.subheader('Spaghetti', text_alignment='center')

        # Bolognese price
        bolognese_price = 200
        st.write(f'Price: :red[**{bolognese_price}**] EGP')

        # Selecting the quantity
        bolognese_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='bolognese_qty'
        )

    with col3:
        # Adding pasta image and name
        st.image(
            "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=600&h=450&fit=crop"
        )
        st.subheader('Pesto Penne', text_alignment='center')

        # Pesto price
        pesto_price = 190
        st.write(f'Price: :red[**{pesto_price}**] EGP')

        # Selecting the quantity
        pesto_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='pesto_qty'
        )


# 8. Building drinks tab
with drinks_tab:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        # Adding drink image and name
        st.image(
            "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600&h=450&fit=crop"
        )
        st.subheader('Cola', text_alignment='center')

        # Cola price
        cola_price = 50
        st.write(f'Price: :red[**{cola_price}**] EGP')

        # Selecting the quantity
        cola_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='cola_qty'
        )

    with col2:
        # Adding drink image and name
        st.image(
            "https://images.unsplash.com/photo-1680404005217-a441afdefe83?w=600&h=450&fit=crop"
        )
        st.subheader('Sprite', text_alignment='center')

        # Sprite price
        sprite_price = 50
        st.write(f'Price: :red[**{sprite_price}**] EGP')

        # Selecting the quantity
        sprite_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='sprite_qty'
        )

    with col3:
        # Adding drink image and name
        st.image(
            "https://images.unsplash.com/photo-1613478223719-2ab802602423?w=600&h=450&fit=crop"
        )
        st.subheader('Orange Juice', text_alignment='center', anchor=False)

        # Orange juice price
        orange_juice_price = 70
        st.write(f'Price: :red[**{orange_juice_price}**] EGP')

        # Selecting the quantity
        orange_juice_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='orange_juice_qty'
        )

    with col4:
        # Adding drink image and name
        st.image(
            "https://images.unsplash.com/photo-1550505095-81378a674395?w=600&h=450&fit=crop"
        )
        st.subheader('Water', text_alignment='center')

        # Water price
        water_price = 20
        st.write(f'Price: :red[**{water_price}**] EGP')

        # Selecting the quantity
        water_qty = st.number_input(
            'Choose quantity:',
            min_value=0,
            max_value=100,
            key='water_qty'
        )

    #final step
    items=['margrita','pepperoni','ranch','water',
           'ornage juice','cola','sprite','alfredo',
           'pesto','bolongese']
    quantities =[margerita_qty,pepperoni_qty, ranch_qty,
                 water_qty,orange_juice_qty,cola_qty,sprite_qty,alfredo_qty,pesto_qty,bolognese_qty]
    st.table(
        {'item':items,'quantity': quantities}

    )

    with st.bottom:#inside section
        if st.button('calucate total',type='primary',
         use_container_width=True):
            total= (
                margertia_price*margerita_qty+
                   ranch_price*ranch_qty +
                   pepperoni_price*pepperoni_qty +
                   pesto_price*pesto_qty+
                   alfredo_price*alfredo_qty +
                   bolognese_price*bolognese_qty+
                   water_price*water_qty+
                   sprite_price*sprite_qty+
                   cola_price * cola_qty+
                   orange_juice_price*orange_juice_qty
                   
                   )
            st.subheader(f'total cost = {total} EGP')


        



