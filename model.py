input_lvs = [
    {
        'X': (0, 100, 1),  # Діапазон рівня води, %
        'name': 'Water_Level',
        'terms': {
            'low': ('trimf', 0, 0, 50),
            'medium': ('trimf', 30, 50, 70),
            'high': ('trimf', 60, 100, 100),
        }
    },

    {
        'X': (1, 4, 1),  # Сезон: 1 - Весна, 2 - Літо, 3 - Осінь, 4 - Зима
        'name': 'Season',
        'terms': {
            'spring': ('singleton', 1),
            'summer': ('singleton', 2),
            'autumn': ('singleton', 3),
            'winter': ('singleton', 4),
        }
    },

    {
        'X': (-10, 40, 0.1),  # Температура, °C
        'name': 'Temperature',
        'terms': {
            'cold': ('trapmf', -10, -10, 5, 15),
            'moderate': ('trapmf', 10, 20, 25, 30),
            'hot': ('trapmf', 25, 35, 40, 40),
        }
    },
]

output_lv = {
    'X': (0, 100, 1),  # Діапазон необхідності наповнення, %
    'name': 'Refill_Need',
    'terms': {
        'no need': ('trimf', 0, 0, 40),
        'partial': ('trimf', 20, 50, 80),
        'necessary': ('trimf', 60, 100, 100),
    }
}

rule_base = [
    (('low', 'spring', 'cold'), 'necessary'),      
    (('low', 'spring', 'moderate'), 'partial'),    
    (('low', 'spring', 'hot'), 'partial'),         
    (('low', 'summer', 'cold'), 'partial'),        
    (('low', 'summer', 'moderate'), 'partial'),    
    (('low', 'summer', 'hot'), 'no need'),         
    (('low', 'autumn', 'cold'), 'partial'),        
    (('low', 'autumn', 'moderate'), 'partial'),    
    (('low', 'autumn', 'hot'), 'no need'),         
    (('low', 'winter', 'cold'), 'necessary'),      
    (('low', 'winter', 'moderate'), 'partial'),    
    (('low', 'winter', 'hot'), 'partial'),         
    
    (('medium', 'spring', 'cold'), 'partial'),     
    (('medium', 'spring', 'moderate'), 'partial'), 
    (('medium', 'spring', 'hot'), 'no need'),      
    (('medium', 'summer', 'cold'), 'no need'),     
    (('medium', 'summer', 'moderate'), 'partial'), 
    (('medium', 'summer', 'hot'), 'partial'),      
    (('medium', 'autumn', 'cold'), 'partial'),     
    (('medium', 'autumn', 'moderate'), 'partial'), 
    (('medium', 'autumn', 'hot'), 'no need'),      
    (('medium', 'winter', 'cold'), 'necessary'),    
    (('medium', 'winter', 'moderate'), 'partial'),  
    (('medium', 'winter', 'hot'), 'partial'),      
    
    (('high', 'spring', 'cold'), 'partial'),       
    (('high', 'spring', 'moderate'), 'no need'),  
    (('high', 'spring', 'hot'), 'no need'),        
    (('high', 'summer', 'cold'), 'no need'),      
    (('high', 'summer', 'moderate'), 'partial'),   
    (('high', 'summer', 'hot'), 'partial'),        
    (('high', 'autumn', 'cold'), 'partial'),       
    (('high', 'autumn', 'moderate'), 'no need'),  
    (('high', 'autumn', 'hot'), 'no need'),       
    (('high', 'winter', 'cold'), 'necessary'),     
    (('high', 'winter', 'moderate'), 'partial'),    
    (('high', 'winter', 'hot'), 'partial'),        
]

